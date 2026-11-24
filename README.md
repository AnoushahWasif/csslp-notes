# CSSLP study notes

My notes for the ISC2 CSSLP (Certified Secure Software Lifecycle Professional) exam, following the exam outline that took effect on 15 September 2023. Every term has a short explanation in plain words, written as a study aid. They are not copied from the official study guide, and there are no real exam questions here. The quick checks inside the lessons are questions I wrote to test myself.

## Progress by domain

"Got it" and "shaky" are my own ratings after each lesson. "Lessons" counts terms with a full written lesson.

<!-- progress:start -->
| Domain | Weight | Terms | Got it | Shaky | Not yet | Lessons |
|---|---:|---:|---:|---:|---:|---:|
| [1. Secure Software Concepts](domains/01-secure-software-concepts.md) | 12% | 56 | 56 | 0 | 0 | 43 |
| [2. Secure Software Lifecycle Management](domains/02-secure-software-lifecycle-management.md) | 11% | 105 | 92 | 13 | 0 | 104 |
| [3. Secure Software Requirements](domains/03-secure-software-requirements.md) | 13% | 55 | 53 | 2 | 0 | 55 |
| [4. Secure Software Architecture and Design](domains/04-secure-software-architecture-and-design.md) | 15% | 101 | 86 | 15 | 0 | 101 |
| [5. Secure Software Implementation](domains/05-secure-software-implementation.md) | 14% | 86 | 78 | 8 | 0 | 86 |
| [6. Secure Software Testing](domains/06-secure-software-testing.md) | 14% | 83 | 72 | 11 | 0 | 83 |
| [7. Secure Software Deployment, Operations, Maintenance](domains/07-secure-software-deployment-operations-maintenance.md) | 11% | 74 | 21 | 3 | 50 | 24 |
| [8. Secure Software Supply Chain](domains/08-secure-software-supply-chain.md) | 10% | 55 | 0 | 0 | 55 | 0 |
| **Total** | 100% | 615 | 458 | 52 | 105 | 496 |
<!-- progress:end -->

The review list of shaky terms is in [review.md](review.md).

## How the repo is organised

```
domains/      one file per exam domain: sections, terms, "On the exam" tips, lessons
glossary.md   acronyms, short definitions and lists to memorise, grouped by section
review.md     every term marked shaky, with its explanation
log/          one file per study day, listing the lessons written that day
scripts/      build.py, which regenerates all of the above from my tracker export
```

Inside a domain file, a term marked "(review)" is one I rated shaky. Where a term has a lesson, it sits in a collapsed "Lesson" block with a quick check and its answer.

## About the "On the exam" tips

They are study heuristics: patterns in how scenario questions tend to be worded and which answer they usually point to, based on the outline and general study material. They are not leaked exam content.

## Rebuilding

The tracker export lives in `data/`, which is git-ignored. To regenerate the notes:

```
python scripts/build.py --data data --out .
```

Lesson dates in the tracker have no year, so the script takes the year from the export's timestamp (override with `--year`).

## License

[MIT](LICENSE)
