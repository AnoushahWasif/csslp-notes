"""Build the markdown notes from an export of the CSSLP study tracker.

Usage:
    python scripts/build.py [--data data] [--out .] [--year 2026]

Expected inside --data:
    tracker.html      the tracker page (holds `const DATA = [...]` and `const TIPS={...}`)
    progress.json     {"s": {"1.1.1": 2, ...}}  2 = got it, 1 = shaky, missing = not yet
    lessons/*.json    one file per term id, e.g. 1.1.12.json
    glossary/*.json   one file per section, each with "title" and "items"
"""

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

GOT_IT, SHAKY = 2, 1


def load_js_const(html: str, name: str):
    match = re.search(rf"^\s*const {name}\s*=(.*)$", html, re.MULTILINE)
    if not match:
        sys.exit(f"could not find `const {name}` in the tracker page")
    return json.loads(match.group(1).strip().rstrip(";"))


def load_json_dir(folder: Path) -> dict:
    if not folder.is_dir():
        return {}
    return {
        f.stem: json.loads(f.read_text(encoding="utf-8"))
        for f in sorted(folder.glob("*.json"))
    }


def kebab(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def esc(text: str) -> str:
    # GitHub drops raw tags like <script>, which shows up in a few XSS terms.
    return text.replace("<", "&lt;")


# The tracker's grading notes were written by the tutor about me ("User chose A", "You said X").
# These notes are mine, so they read in first person.
FIRST_PERSON = [
    (r"\bUser:\s*", "My answer: "),
    (r"\bUser (said|chose|named|wrote|picked|answered)\b", r"I \1"),
    (r"\bSkipped by user\b", "Skipped"),
    (r"\bYou (said|chose|named|wrote|picked|answered)\b", r"I \1"),
    (r"\(you got this\)", "(got this)"),
    (r"^(Said|Answered|Named|Wavered|Did not|First said)\b", r"I \1"),
]


def first_person(text: str) -> str:
    for pattern, repl in FIRST_PERSON:
        text = re.sub(pattern, repl, text, flags=re.MULTILINE)
    return re.sub(
        r"\bI (Said|Answered|Named|Wavered|Did not|First said)\b",
        lambda m: "I " + m.group(1)[0].lower() + m.group(1)[1:],
        text,
    )


def anchor(term_id: str) -> str:
    return "t-" + term_id.replace(".", "-").lower()


def lesson_date(raw: str, year: int):
    # The tracker stores dates like "Oct 6" with no year.
    try:
        return (
            dt.datetime.strptime(f"{raw} {year}", "%b %d %Y")
            .replace(tzinfo=dt.UTC)
            .date()
        )
    except (TypeError, ValueError):
        return None


def lesson_md(body: str) -> str:
    out = []
    for line in body.strip().splitlines():
        line = esc(first_person(line.rstrip()))
        if not line:
            continue
        if line.startswith("#"):
            out += ["", f"**{line.lstrip('#').strip()}**", ""]
        elif line.lstrip().startswith(("- ", "* ")):
            out.append(line)
        else:
            out += ["", line, ""]
    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def domain_file(dom: dict) -> str:
    return f"{dom['n']:02d}-{kebab(dom['t'])}.md"


def build(data_dir: Path, out: Path, year: int | None) -> dict:
    html = (data_dir / "tracker.html").read_text(encoding="utf-8")
    domains = load_js_const(html, "DATA")
    tips = load_js_const(html, "TIPS")
    progress_raw = json.loads((data_dir / "progress.json").read_text(encoding="utf-8"))
    progress = progress_raw.get("s", {})
    lessons = load_json_dir(data_dir / "lessons")
    glossary = load_json_dir(data_dir / "glossary")

    if year is None:
        updated = progress_raw.get("updated")
        if not updated:
            sys.exit("lesson dates have no year; pass --year")
        year = dt.datetime.fromtimestamp(updated / 1000, tz=dt.UTC).year

    for sub in ("domains", "log"):
        shutil.rmtree(out / sub, ignore_errors=True)
        (out / sub).mkdir(parents=True)

    known_ids = set()
    shaky_terms = []
    by_date = defaultdict(list)
    undated = []
    rows = []

    for dom in domains:
        fname = domain_file(dom)
        lines = [
            f"# Domain {dom['n']}: {dom['t']}",
            "",
            f"Exam weight: {dom['w']}%",
            "",
        ]
        counts = {"terms": 0, "got": 0, "shaky": 0, "lessons": 0}
        for sid, stitle, terms in dom["s"]:
            lines += [f"## {sid} {stitle}", ""]
            section_tips = tips.get(sid) or []
            for i, (term, expl) in enumerate(terms, 1):
                tid = f"{sid}.{i}"
                known_ids.add(tid)
                status = progress.get(tid)
                counts["terms"] += 1
                counts["got"] += status == GOT_IT
                counts["shaky"] += status == SHAKY
                tag = " (review)" if status == SHAKY else ""
                lines += [
                    f'<a name="{anchor(tid)}"></a>',
                    f"**{esc(term)}**{tag}",
                    "",
                    esc(expl),
                    "",
                ]
                tip = section_tips[i - 1] if i <= len(section_tips) else None
                if tip:
                    lines += [f"> On the exam: {esc(tip)}", ""]
                if status == SHAKY:
                    shaky_terms.append((dom, sid, stitle, tid, term, expl))
                lesson = lessons.get(tid)
                if lesson:
                    counts["lessons"] += 1
                    day = lesson_date(lesson.get("date"), year)
                    link = (term, dom, sid, stitle, tid)
                    (by_date[day].append(link) if day else undated.append(link))
                    summary = f"Lesson ({day:%d %b %Y})" if day else "Lesson"
                    lines += [
                        f"<details><summary>{summary}</summary>",
                        "",
                        lesson_md(lesson.get("body", "")),
                        "",
                    ]
                    if lesson.get("check"):
                        lines += [f"**Quick check:** {esc(lesson['check'])}", ""]
                    if lesson.get("answer"):
                        lines += [
                            f"**Answer:** {esc(first_person(lesson['answer']))}",
                            "",
                        ]
                    lines += ["</details>", ""]
        (out / "domains" / fname).write_text(
            "\n".join(lines).rstrip() + "\n", encoding="utf-8"
        )
        rows.append((dom, fname, counts))

    orphans = sorted(set(lessons) - known_ids) + sorted(set(progress) - known_ids)
    if orphans:
        print(
            f"warning: ids with no matching term, skipped: {orphans}", file=sys.stderr
        )

    write_glossary(out, glossary, domains)
    write_review(out, shaky_terms)
    write_log(out, by_date)

    stats = {
        "rows": rows,
        "undated": undated,
        "glossary_items": sum(len(g.get("items", [])) for g in glossary.values()),
        "log_days": len(by_date),
        "shaky": len(shaky_terms),
    }
    write_readme_progress(out, stats)
    return stats


def term_link(entry, prefix="domains/") -> str:
    term, dom, sid, stitle, tid = entry
    return f"[{esc(term)}]({prefix}{domain_file(dom)}#{anchor(tid)}) (Domain {dom['n']}, {sid} {stitle})"


def sort_key(sid: str):
    return [int(p) if p.isdigit() else 999 for p in re.split(r"[.\-]", sid)]


def write_glossary(out: Path, glossary: dict, domains: list):
    lines = [
        "# Glossary",
        "",
        "Short definitions and lists to memorise, grouped by section.",
        "",
    ]
    for key in sorted(glossary, key=sort_key):
        doc = glossary[key]
        title = doc.get("title", key)
        heading = title if re.search(r"\d", title) else f"{key} {title}"
        lines += [f"## {heading}", ""]
        groups = defaultdict(list)
        for item in doc.get("items", []):
            groups[item.get("g") or "Other"].append(item)
        for group in sorted(groups, key=str.lower):
            lines += [f"### {group}", ""]
            for item in sorted(groups[group], key=lambda x: x.get("t", "").lower()):
                full = (
                    f" ({esc(item['f'])})"
                    if item.get("f") and item["f"] != item.get("t")
                    else ""
                )
                lines.append(
                    f"- **{esc(item.get('t', ''))}**{full}: {esc(item.get('d', ''))}"
                )
            lines.append("")
    (out / "glossary.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_review(out: Path, shaky_terms: list):
    lines = [
        "# Review list",
        "",
        f"Terms I marked as shaky ({len(shaky_terms)}). Go through these before each practice test.",
        "",
    ]
    current = None
    for dom, sid, stitle, tid, term, expl in shaky_terms:
        if current != sid:
            if current is not None:
                lines.append("")
            lines += [f"## Domain {dom['n']}, {sid} {stitle}", ""]
            current = sid
        link = f"domains/{domain_file(dom)}#{anchor(tid)}"
        lines.append(f"- **[{esc(term)}]({link})**: {esc(expl)}")
    (out / "review.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_log(out: Path, by_date: dict):
    for day in sorted(by_date):
        entries = by_date[day]
        lines = [f"# {day:%d %B %Y}", "", f"Lessons written: {len(entries)}", ""]
        lines += [f"- {term_link(e, prefix='../domains/')}" for e in entries]
        (out / "log" / f"{day.isoformat()}.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )


def write_readme_progress(out: Path, stats: dict):
    """Fills the table between the progress markers in README.md, or prints it if there are none."""
    lines = [
        "| Domain | Weight | Terms | Got it | Shaky | Not yet | Lessons |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    tot = defaultdict(int)
    for dom, fname, c in stats["rows"]:
        not_yet = c["terms"] - c["got"] - c["shaky"]
        lines.append(
            f"| [{dom['n']}. {dom['t']}](domains/{fname}) | {dom['w']}% | {c['terms']} | {c['got']} "
            f"| {c['shaky']} | {not_yet} | {c['lessons']} |"
        )
        for k in ("terms", "got", "shaky", "lessons"):
            tot[k] += c[k]
        tot["not_yet"] += not_yet
    lines.append(
        f"| **Total** | 100% | {tot['terms']} | {tot['got']} | {tot['shaky']} | {tot['not_yet']} | {tot['lessons']} |"
    )
    if stats["undated"]:
        lines += ["", "Lessons with no date in the tracker:", ""]
        lines += [f"- {term_link(e)}" for e in stats["undated"]]
    table = "\n".join(lines)

    readme = out / "README.md"
    start, end = "<!-- progress:start -->", "<!-- progress:end -->"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if start in text and end in text:
            head, rest = text.split(start, 1)
            _, tail = rest.split(end, 1)
            readme.write_text(f"{head}{start}\n{table}\n{end}{tail}", encoding="utf-8")
            return
    print(table)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--data", type=Path, default=Path("data"), help="folder with the tracker export"
    )
    parser.add_argument(
        "--out", type=Path, default=Path("."), help="repo root to write into"
    )
    parser.add_argument(
        "--year",
        type=int,
        help="year for lesson dates (default: year of progress.json 'updated')",
    )
    args = parser.parse_args()
    if not (args.data / "tracker.html").exists():
        sys.exit(
            f"{args.data / 'tracker.html'} not found; put the tracker export in {args.data}/"
        )
    stats = build(args.data, args.out, args.year)
    terms = sum(c["terms"] for _, _, c in stats["rows"])
    lessons = sum(c["lessons"] for _, _, c in stats["rows"])
    print(
        f"terms={terms} lessons={lessons} glossary={stats['glossary_items']} "
        f"log_days={stats['log_days']} shaky={stats['shaky']} undated={len(stats['undated'])}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
