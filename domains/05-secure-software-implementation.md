# Domain 5: Secure Software Implementation

Exam weight: 14%

## 5.1 Secure coding practices

<a name="t-5-1-1"></a>
**Declarative vs imperative security**

Declarative is set in configuration and enforced by the container. Imperative (programmatic) is written in code: finer-grained but harder to maintain.

> On the exam: Declarative is consistent and changeable without recompiling. Use imperative when the rules are complex, e.g., approvals that depend on amount.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-2"></a>
**Race conditions / TOCTOU**

Time of check to time of use: state changes between checking and using a resource.

> On the exam: What it is: when timing between threads or processes changes results. TOCTOU: the program checks a condition (file permissions) and then uses the resource, but it changed in between.
Scenario cue: 'program checks a file is safe, then opens it; attacker swaps it for a link in between' → TOCTOU.
Fix: atomic operations, locks, open first and then check the open handle.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-3"></a>
**Thread safety, locks, deadlocks**

Use mutexes and synchronization; avoid deadlock and starvation.

> On the exam: Thread safety: code works correctly when many threads run it at once. Locks/mutexes allow one thread at a time in critical sections.
Deadlock: two threads each wait for the other's lock forever, an availability problem. Avoid with consistent lock order and timeouts.
Scenario cue: 'two users withdraw at the same time and the balance goes wrong' → race condition; use locking or transactions.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-4"></a>
**Database concurrency controls**

Locking, isolation levels, optimistic vs pessimistic concurrency.

> On the exam: Pessimistic locking prevents conflicts but slows things; optimistic detects conflicts at commit time.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-5"></a>
**Input validation**

Validate server-side for type, length, range, format. Allow-lists beat deny-lists.

> On the exam: Treat all input as untrusted, including headers, cookies, files and APIs. Client-side validation is for usability only.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-6"></a>
**Canonicalization**

Convert input to its simplest standard form before validating (stops encoding tricks).

> On the exam: What it is: converting input to its standard simplest form (decoding URL encoding, Unicode, resolving '../') before validating it.
Why it matters: attackers encode malicious input so filters miss it, then it's decoded later.
Scenario cue: 'path traversal works with %2e%2e%2f but not ../' → validation happened before canonicalization.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-7"></a>
**Injection**

SQL, OS command, LDAP, XPath, XML/XXE. Fix with parameterized queries and validation.

> On the exam: Root cause: mixing data with commands. Stored procedures help only if they don't build dynamic SQL inside.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-8"></a>
**Error and exception handling**

Show generic messages to users, log details internally, fail secure, no stack traces.

> On the exam: Rules: catch exceptions; show users a generic message and a reference ID; log details internally; fail securely (deny); release resources in finally blocks.
Scenario cue: 'error page shows a stack trace and SQL query' → information disclosure; use generic errors.
Trap: empty catch blocks hide failures and can leave the system in an insecure state.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-9"></a>
**Output encoding**

Context-aware encoding (HTML, JavaScript, URL) to prevent XSS.

> On the exam: What it is: converting output so the browser treats it as data, not code. Must match the context: HTML body, HTML attribute, JavaScript, URL, CSS.
Scenario cue: 'user comments run scripts in other users' browsers' → XSS; primary fix is output encoding (plus input validation and Content Security Policy).
Don't confuse: input validation checks what comes in; output encoding protects where it goes out.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-10"></a>
**Obfuscation**

Making code or data hard to read; slows attackers but is not a security control on its own.

> On the exam: What it is: making code or data harder to read (renaming, scrambling logic, hiding strings).
Use: slowing reverse engineering, protecting intellectual property.
Trap: it's not encryption; it never protects secrets like keys or passwords on its own.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-11"></a>
**Secure logging**

No passwords, keys or unneeded PII in logs; prevent log injection; protect integrity.

> On the exam: Encode log entries to prevent log injection. Log security events: logins, failures, privilege changes.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-12"></a>
**Session management**

Random IDs, regenerate on login (prevents session fixation), timeouts, invalidate on logout.

> On the exam: Rules: long random session IDs from a CSPRNG; new session ID after login (prevents session fixation); idle and absolute timeouts; invalidate on logout on the server; transmit only over TLS; never in URLs.
Scenario cue: 'attacker sets a victim's session ID before login and then uses it' → session fixation; regenerate the ID at login.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-13"></a>
**Cookie flags**

Secure (HTTPS only), HttpOnly (no script access), SameSite (CSRF defense).

> On the exam: Secure: cookie only sent over HTTPS. HttpOnly: JavaScript can't read it, reducing theft through XSS. SameSite (Strict/Lax): cookie not sent on cross-site requests, reducing CSRF.
Scenario cue: 'session cookie stolen through an XSS script' → missing HttpOnly.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-14"></a>
**Trusted vs untrusted APIs and libraries**

Vet third-party code; avoid banned functions like strcpy and gets.

> On the exam: Trusted: vetted, maintained, from known sources. Untrusted: unknown origin, abandoned, or dangerous functions.
Banned functions: unsafe C functions like strcpy, gets, sprintf; use bounded, safe versions.
Scenario cue: 'a library pulled from an unknown website' → untrusted; use approved repositories and SCA.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-15"></a>
**Resource management**

Prevent memory leaks, buffer overflows, use-after-free, integer overflow, resource exhaustion.

> On the exam: Buffer overflows can lead to code execution; quotas and limits prevent resource-exhaustion DoS.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-16"></a>
**Secure configuration management**

Baseline configuration; no hardcoded credentials; secrets in a vault.

> On the exam: What it is: secure, consistent configuration: secure defaults, no default accounts, debugging off in production, secrets stored outside code in a vault, configs version-controlled and reviewed.
Scenario cue: 'database password found in source code on GitHub' → hardcoded credentials; rotate and move to a secrets manager.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-17"></a>
**Tokenization**

Replace sensitive data with a meaningless token; the real value stays in a secure vault.

> On the exam: Shrinks PCI scope because systems only see tokens. Unlike encryption, a token has no mathematical link to the real value.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Not directly tested; taught.

</details>

<a name="t-5-1-18"></a>
**Sandboxing and isolation**

Run code with restricted access: sandboxes, VMs, containers.

> On the exam: What it is: running code in a restricted environment so it can't harm the rest of the system: browser sandboxes, VMs, containers, restricted processes.
Scenario cue: 'the app must open untrusted uploaded files safely' → process them in a sandbox.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-19"></a>
**Separation Kernel Protection Profile**

High-assurance kernel that strictly isolates partitions.

> On the exam: What it is: a protection profile for separation kernels that split a system into isolated partitions that can communicate only through defined, controlled channels.
Use: high-assurance systems (military, avionics) where one component's failure or compromise must not affect others.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-20"></a>
**Encryption scope**

Payload, field-level, transport (TLS 1.2/1.3), storage (at rest).

> On the exam: TLS protects data only in transit. Field-level encryption protects specific data even from database admins.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-21"></a>
**Crypto agility**

Design so algorithms can be swapped without rewriting the app.

> On the exam: What it is: designing so algorithms, key lengths and libraries can be changed through configuration without rewriting the app.
Why it matters: algorithms get broken (SHA-1, DES) and post-quantum migration is coming.
Scenario cue: 'switching from RSA required rewriting every module' → lack of crypto agility.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Not directly tested; taught.

</details>

<a name="t-5-1-22"></a>
**Algorithm selection** (review)

Use AES-GCM, SHA-256+, RSA 2048+/ECC. Avoid DES, RC4, MD5, SHA-1, ECB mode.

> On the exam: Good choices: AES (GCM mode), SHA-256 or higher, RSA 2048+ or ECC, TLS 1.2/1.3. Avoid: DES, 3DES, RC4, MD5, SHA-1, ECB mode.
Trap: ECB encrypts identical blocks the same way, so patterns leak. Use authenticated encryption (GCM) to get confidentiality and integrity.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-23"></a>
**Password storage**

Salted, slow hashing: bcrypt, scrypt, Argon2, PBKDF2.

> On the exam: Never encrypt passwords (that's reversible); hash them. Salt defeats rainbow tables; slow hashing defeats brute force.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-24"></a>
**Random numbers**

Use a cryptographically secure PRNG for keys and tokens.

> On the exam: What it is: keys, IVs, salts, tokens and session IDs need a cryptographically secure random number generator (CSPRNG) with good entropy.
Scenario cue: 'password reset tokens can be predicted' → generated with a normal PRNG or timestamp; use a CSPRNG.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-25"></a>
**Don't roll your own crypto**

Use vetted libraries and validated modules.

> On the exam: What it means: never invent your own algorithm or implement standard ones from scratch; use well-reviewed libraries and validated modules (FIPS 140).
Why: crypto is easy to get subtly wrong, and secret custom algorithms violate open design.
Scenario cue: 'developer created a custom XOR encryption' → replace with a standard library.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Not directly tested; taught.

</details>

<a name="t-5-1-26"></a>
**Trust zones and function permissions**

Group components by trust level; authorize each function.

> On the exam: Trust zones: group components by trust level (internet, DMZ, internal, restricted) and validate and authenticate whenever data crosses zones.
Function permissions: check authorization for each function or API, not just page access.
Scenario cue: 'a hidden admin function works if you call its URL directly' → missing function-level authorization.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-27"></a>
**Access control models**

RBAC (roles), DAC (owner decides), MAC (system enforces labels), ABAC (attributes), rule-based.

> On the exam: MAC: classified systems, users can't change labels. DAC: owners share files. RBAC: business apps with job roles. ABAC: fine-grained context like time or location.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-28"></a>
**Processor security extensions**

Intel SGX enclaves, ARM TrustZone, AMD SEV, NX bit, control-flow enforcement.

> On the exam: Examples: Intel SGX (secure enclaves), ARM TrustZone (secure world), AMD SEV (encrypted VMs), NX bit (non-executable memory), Intel CET and ARM pointer authentication (stop control-flow hijacking).
Scenario cue: 'process sensitive data so even a compromised OS can't read it' → trusted execution environment/enclave.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-29"></a>
**Transport encryption (TLS)**

TLS protects data in transit: the handshake authenticates the server with its certificate, agrees a cipher suite and creates session keys; then data is encrypted with symmetric keys.

> On the exam: Best practice: TLS 1.2 or 1.3 only, strong cipher suites, perfect forward secrecy (ECDHE), HSTS for websites, validate certificates.
Scenario cue: 'attacker forces an old protocol version' → downgrade attack; disable old versions.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Not directly tested; taught.

</details>

<a name="t-5-1-30"></a>
**Database encryption**

Options: Transparent Data Encryption (TDE: whole database files, protects stolen disks and backups), column/field-level encryption (specific sensitive fields), application-level encryption (encrypted before reaching the database).

> On the exam: Trap: TDE doesn't protect against someone querying through the database with valid access; field or application-level encryption does.
Scenario cue: 'protect card numbers even from DBAs' → application-level or field-level encryption with keys outside the database.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-31"></a>
**Salt, IV and nonce**

Salt: random value added to a password before hashing so identical passwords hash differently. IV/nonce: random or unique value so the same plaintext encrypts differently each time.

> On the exam: Trap: salts aren't secret but must be unique; reusing a nonce with the same key can break encryption (especially GCM).

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-32"></a>
**Data protection techniques compared**

Encryption: reversible with a key. Hashing: one-way. Tokenization: swap with a token, real data in a vault. Masking: hide part of the value (****1234).

> On the exam: Scenario cue: 'reduce PCI scope' → tokenization. 'Display to support staff' → masking. 'Store passwords' → hashing. 'Protect a file sent to a partner' → encryption.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-33"></a>
**XSS types**

Reflected (non-persistent): script in a link is bounced back in the response. Stored (persistent): script saved in the app (comments) and served to every viewer, most dangerous. DOM-based: client-side JavaScript writes untrusted data into the page without the server being involved.

> On the exam: Defenses: context-aware output encoding, input validation, Content Security Policy, HttpOnly cookies.
Scenario cue: 'every visitor to the forum page gets attacked' → stored XSS.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** HttpOnly correct; first said reflected/DOM, then self-corrected to STORED (persistent). Kept shaky for re-check.

</details>

<a name="t-5-1-34"></a>
**Cross-site request forgery (CSRF)**

Tricks a logged-in user's browser into sending an unwanted request (transfer money) to a site that trusts it, using the user's cookies.

> On the exam: Defenses: anti-CSRF tokens, SameSite cookies, re-authentication for sensitive actions, checking origin headers.
Don't confuse: XSS abuses the user's trust in the site; CSRF abuses the site's trust in the user's browser.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-35"></a>
**Insecure direct object references (IDOR)**

The app uses user-supplied IDs to fetch records without checking ownership (changing /invoice/1001 to /invoice/1002).

> On the exam: Defense: check authorization on every object access; use indirect references (per-user mapping) where helpful.
OWASP: now part of broken access control.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-36"></a>
**Unvalidated redirects and forwards**

The app redirects users to a URL taken from input, so attackers create links that look trusted but go to phishing sites.

> On the exam: Defense: avoid user-controlled redirects; use an allow-list or mapped IDs instead of full URLs.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-37"></a>
**Other injection types**

OS command injection (input runs system commands), LDAP injection (alters directory queries), XML injection and XXE (external entities read files or call internal systems), XPath injection, NoSQL injection, client-side injection on mobile.

> On the exam: Common fix: never build commands or queries by joining strings with input; use safe APIs and parameterization, validate with allow-lists, disable XML external entities.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-38"></a>
**Buffer overflows: stack and heap**

Writing more data than a buffer holds. Stack overflow can overwrite the return address to run attacker code; heap overflow corrupts dynamic memory structures.

> On the exam: Defenses: bounds checking, safe functions, memory-safe languages, stack canaries, ASLR, DEP.
Related memory flaws: dangling pointers / use-after-free, integer overflow, format string bugs (user input used as a printf format string).

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-39"></a>
**File attacks**

Path/directory traversal ('../' to reach other files), file inclusion (local/remote, running attacker files), unrestricted file upload (uploading a web shell), insecure temp files.

> On the exam: Defenses: canonicalize then validate paths, allow-list file types, store uploads outside the web root with random names, scan uploads.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-40"></a>
**Server-side request forgery (SSRF)**

Attacker makes the server send requests to destinations of their choice, often internal systems or cloud metadata services that hold credentials.

> On the exam: Defenses: allow-list destinations, block internal and metadata addresses, network segmentation.
Scenario cue: 'image-from-URL feature used to read cloud instance credentials' → SSRF.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-41"></a>
**Insecure deserialization**

Turning untrusted data back into objects can let attackers run code or change logic.

> On the exam: Defenses: don't deserialize untrusted data; use simple formats (JSON) with strict schemas; sign serialized data; run with low privilege.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 2: Input, output and server-side attacks (10 topics)**

*Exam angle: most attacks start with untrusted input. This batch is about handling data safely in, safely out, and the attacks that happen when you don't.*

**1. Input validation (topic 5)**

- **Validate on the server.** Client-side checks are for convenience only (never trust the client!).
- Check **type, length, range and format** (e.g. age must be a number from 0 to 130).
- **Allow-list beats deny-list:**
  - **Allow-list** = define what's **good** and reject everything else (e.g. ZIP code = exactly 5 digits)
  - **Deny-list** = try to block what's **bad** (e.g. block `&lt;script>`). Attackers always find a variation you didn't list.
- Validate **all** input: form fields, URL parameters, headers, cookies, file uploads, API data, and data from **other systems** (upstream data, 4.2).
- **Reject** bad input rather than trying to "clean" it, where possible.

**Hook:** **Allow-list = a guest list at the door. Deny-list = a list of known troublemakers, and new troublemakers walk right in.**

**2. Canonicalization (topic 6)**

- **Canonical form** = the **single, simplest standard form** of a piece of data.
- **The problem:** the same thing can be written many ways. `../` can be written as `%2e%2e%2f`, `..%2f`, or double-encoded as `%252e%252e%252f`. If you validate **before** decoding, the attacker's encoded version **slips past**, then gets decoded **later** and does damage.
- **The rule: decode and normalize FIRST, then validate.**
- It applies to URLs, file paths, Unicode (different characters that look identical), and upper/lower case.

**Hook:** **Canonicalize, then check. Undress the input before you inspect it.**

**3. Injection (topic 7)**

Untrusted input gets **interpreted as code or commands** instead of plain data.

- **SQL injection:** input changes the database query (`' OR '1'='1`).
- **The main fix: parameterized queries (prepared statements):** the query structure is fixed, and input is **always treated as data**.
- **Supporting controls:** input validation, **least-privilege database accounts**, stored procedures (**only** if they don't build SQL by gluing strings), and escaping as a last resort.

**4. Other injection types (topic 37)**

The same idea, aimed at different interpreters:

- **OS command injection:** input runs **system commands** (`; rm -rf /`). **Main fix:** don't build shell strings; call a safe API that takes input as a **separate argument**. Supporting: allow-list validation (e.g. valid hostnames only).
- **LDAP injection:** input changes **directory queries** (`*)(uid=*`). Fix: escape LDAP special characters, validate.
- **XPath injection:** input changes **XML queries**. Fix: parameterized XPath, validation.
- **XML injection / XXE (XML External Entity):** a malicious XML document makes the parser **read server files** or reach internal systems. Fix: **disable external entities and DTDs** in the parser.
- **NoSQL injection:** input changes **NoSQL queries** (e.g. sending `{"$ne": null}` as a password in MongoDB). Fix: type-check input, use safe query builders.
- **Template injection (SSTI):** input runs inside a **server-side template engine**, which can lead to code execution. Fix: never put user input into template code.
- **CRLF / header injection:** line-break characters inject fake **HTTP headers** or split responses. Fix: strip or encode CR/LF.
- **Log injection:** fake lines written into **logs** (from 4.2). Fix: encode before logging.

**The universal rule:** keep **data** and **commands** **separate**, so input can never become code.

**5. Output encoding (topic 9)**

- **Encode data when it's sent OUT**, based on **where** it lands (**context-aware**):
  - **HTML body:** `&lt;` becomes `&lt;`
  - **HTML attribute**, **JavaScript**, **URL** and **CSS** contexts each need their **own** encoding
- It's the **main defense against XSS**: the browser shows the attacker's script as harmless **text** instead of running it.
- Use your framework's built-in encoding, which most modern frameworks do by default.

**Hook:** **Validate on the way IN, encode on the way OUT.**

**6. Error and exception handling (topic 8)**

- **Users get a generic message** ("Something went wrong, reference #4521"). **Details go to the logs**, not the screen.
- **Never show** stack traces, SQL errors, file paths, version numbers or internal IPs. They're a **map for attackers** (information disclosure, the **I** in STRIDE).
- **Fail secure:** if an error happens mid-check, **deny** access; don't skip the check.
- **Catch errors properly:** don't swallow them silently; handle them, and release resources.
- Use a **global error handler**, so nothing unexpected leaks.

**7. Secure logging (topic 11)**

- **Log** security events: logins, failures, access denied, privilege changes, admin actions, with **who, what, when, where, and the outcome**.
- **Never log** passwords, keys, session tokens, full card numbers, or unneeded PII.
- **Prevent log injection:** encode input before writing it to logs.
- **Protect integrity:** send logs to a central place, append-only, where admins can't delete them (the camera footage from 4.2).
- **Sync the time** (NTP), so events can be correlated across systems.

**8. Unvalidated redirects and forwards (topic 36)**

- The app redirects to a URL **taken from input**: `bank.com/login?next=evil.com`. The link looks trustworthy (it **starts with the real domain**), but the user ends up on a **phishing site**.
- **Fixes:** avoid user-controlled redirects; if needed, use an **allow-list** of destinations, or **IDs that map to URLs** on the server (`?next=3` → /account), and warn the user before leaving the site.

**9. File attacks (topic 39)**

- **Path / directory traversal:** `../../etc/passwd` to read files **outside** the intended folder. Fix: canonicalize the path, then check it stays inside the allowed directory; use IDs instead of filenames.
- **File inclusion:** **local** (LFI) or **remote** (RFI) files get loaded and **executed** by the app. Fix: never build include paths from input.
- **Unrestricted file upload:** uploading a script (e.g. a `.php` web shell) that the server then runs. Fixes: allow-list file types **and check the real content** (not just the extension), **rename** files, **store outside the web root**, scan for malware, limit size.
- **Zip slip:** archive entries with `../` in their names write files **outside** the extraction folder.

**10. Insecure deserialization (topic 41)**

- **Serialization** = turning objects into data (to save or send). **Deserialization** = turning data back into objects.
- **The risk:** deserializing **untrusted** data can let attackers **create unexpected objects**, change logic, or even **run code** (remote code execution). It's been behind many major breaches.
- **Fixes:**
  - **Don't deserialize untrusted data**; prefer simple data formats like **JSON** with strict parsing
  - **Allow-list** which classes may be created
  - **Sign** serialized data (integrity check) before trusting it
  - Run deserialization with **low privileges**, and log failures

**On the exam**

- "Validation blocks `&lt;script>` but attackers use `&lt;ScRiPt>`" → deny-list weakness → **allow-list**
- "Encoded `%2e%2e%2f` slips past the filter" → **canonicalize first**, then validate
- "Main defense against SQL injection" → **parameterized queries**
- "Parser reads `/etc/passwd` from a crafted XML file" → **XXE** → disable external entities
- "Shell command built from user input" → **OS command injection**
- "Login page shows a full SQL error with table names" → **improper error handling** (information disclosure)
- "`login?next=evil.com` sends users to a phishing site" → **unvalidated redirect**
- "Uploaded `.php` file executes on the server" → **unrestricted upload** → allow-list type, check content, store outside web root
- "Untrusted serialized object leads to code execution" → **insecure deserialization**
- **Traps:** client-side validation alone is never enough; output encoding (not input validation) is the main XSS fix; validate **after** canonicalizing, never before.

**Hooks**

- **Allow-list = the guest list. Deny-list = the troublemaker list.**
- **Canonicalize, then check.**
- **Data and commands never share a seat.**
- **Validate IN, encode OUT.**

**Quick check + your answers**

1. `%2e%2e%2f` gets past a `../` filter: what was done in the wrong order? → **Canonicalize first, then validate** ✅

2. `ping ` + host built from user input → **OS command injection** ✅. Fix: you said allow-list (supporting control); the **main** fix is a safe API with the host as a **separate argument** (no shell string).

3. Login error shows SQL column and table names → **improper error handling** (information disclosure) ✅. User should see a **generic message + reference number**; details go to the logs.

**Quick check:** (1) %2e%2e%2f gets past a ../ filter: wrong order? (2) 'ping ' + host from user input: attack + fix? (3) Login error shows SQL table/column: what's wrong, what should users see?

**Answer:** Canonicalize then validate; OS command injection (main fix = safe API, separate argument; allow-list supporting); improper error handling (generic message + reference, details to logs). Correct.

</details>

<a name="t-5-1-42"></a>
**Clickjacking**

A malicious page hides the real site in a transparent frame so users click buttons they can't see.

> On the exam: Defense: X-Frame-Options or Content Security Policy frame-ancestors to stop the site being framed.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-43"></a>
**Broken authentication and session attacks**

Credential stuffing (reusing leaked passwords), brute force, dictionary attacks, session hijacking (stealing session IDs), session fixation, weak password recovery.

> On the exam: Defenses: MFA, rate limiting and lockout, breached-password checks, secure session handling, safe password reset tokens.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-44"></a>
**Man-in-the-middle and replay attacks**

MITM: attacker secretly intercepts and possibly alters communication (ARP spoofing, rogue Wi-Fi). Replay: attacker captures valid traffic and resends it.

> On the exam: Defenses: TLS with certificate validation (and pinning for apps), mutual authentication; nonces, timestamps and sequence numbers against replay.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 1: Web and session attacks (10 topics)**

*Exam angle: these are mostly familiar from Domain 4. The focus here is what's new and what the exam asks.*

**1. XSS types (topic 33)**

XSS = the attacker's script runs **on your site** in other users' browsers. Three types:

- **Stored (persistent):** the script is **saved on the server** (a comment, a review, a profile field) and hits **everyone** who views it. The most dangerous.
- **Reflected (non-persistent):** the script is in a **crafted link**, and the server **bounces it back** in the response. It hits only whoever **clicks the link**.
- **DOM-based:** it all happens **in the browser's JavaScript**; the server never sees the payload (e.g. code writes `location.hash` into the page).

**Fixes:** **context-aware output encoding** (the main fix) + **Content Security Policy (CSP)** to block inline scripts + **HttpOnly** cookies so scripts can't steal sessions + input validation.

**The quick test: where does the script live?**

- **Saved on the server, hits every visitor, no link needed** → **stored**
- **In a link the victim clicks, hits only them** → **reflected**
- **Only in the browser's JavaScript, never reaches the server** → **DOM-based**

**Clue words:** "posts" / "saved" / "every visitor" → stored · "link" / "clicks" → reflected · "only in the browser" → DOM.

**Hook:** **Stored = a booby trap left in the room. Reflected = a booby-trapped link. DOM = the trap is in the browser itself.**

**2. CSRF (topic 34)**

The user's logged-in **browser is tricked** into sending a request it didn't intend, because cookies are attached automatically.

**Fixes:** **anti-CSRF (synchronizer) tokens**, **SameSite** cookies, **re-authentication** for sensitive actions (change password, transfer), and checking the Origin/Referer header. **GET requests must never change data.**

**3. IDOR (topic 35)**

The app uses an ID from the user (`/invoice/552`) and **never checks ownership**. (It's the same as **BOLA** for APIs.)

**Fix:** an **authorization check on every object, every request**. Random IDs or **indirect references** make guessing harder, but they're **not** the fix on their own.

**4. Cookie flags (topic 13)**

- **Secure:** sent over **HTTPS only**
- **HttpOnly:** **JavaScript can't read it** (blocks XSS cookie theft)
- **SameSite:** Strict / Lax / None, which controls sending on cross-site requests (CSRF defense)
- Also: tight **Domain** and **Path** scope, and **short expiry** for session cookies

**5. Session management (topic 12)**

- **Long, random session IDs** from a secure generator
- **New session ID at login** (stops **session fixation**)
- **Idle + absolute timeouts**
- **Invalidate the session on the server at logout**, not just by deleting the cookie
- Never put session IDs in **URLs** (they leak in logs and Referer headers)

**6. Broken authentication and session attacks (topic 43)**

- **Credential stuffing:** reusing passwords leaked from other sites
- **Brute force:** trying every combination · **dictionary attack:** common words · **password spraying:** **one** common password tried against **many** accounts (avoids per-account lockouts)
- **Session hijacking** (stealing the ID) · **session fixation** (planting a known ID)

**Fixes:** **MFA**, rate limiting, lockout or delays, breached-password checks, and the session rules above.

**7. SSRF (topic 40)**

The attacker makes **your server** send requests to destinations **they choose**, often **internal** systems the attacker can't reach directly, or the **cloud metadata service** (`169.254.169.254`), which can hand out **cloud credentials**.

**Fixes:** **allow-list** permitted destinations, block internal/private IP ranges and metadata addresses, don't return raw responses to the user, and use network segmentation.

**Hook:** **SSRF = tricking the server into making the call for you.**

**8. Clickjacking (topic 42)**

A malicious page loads your real site in an **invisible frame**, so users think they're clicking one thing but actually click **your** button ("Delete account," "Allow").

**Fix:** forbid framing: **`X-Frame-Options: DENY`** or **CSP `frame-ancestors`**.

**9. Man-in-the-middle and replay (topic 44)**

- **MITM:** the attacker **secretly sits between** two parties, reading or changing traffic (ARP spoofing, rogue Wi-Fi, fake certificates). **Fix:** **TLS with proper certificate validation**, HSTS, certificate pinning in apps.
- **Replay:** the attacker **resends** a valid captured message. **Fix:** **nonces, timestamps, sequence numbers**, short-lived tokens. (Remember: encryption alone doesn't stop replay.)

**10. Race conditions / TOCTOU (topic 2)**

The state **changes between the check and the use**. *Example:* the app **checks** the balance is $100, then **withdraws**, but two requests arrive at once and **both pass the check**, so $200 leaves.

**Fixes:** **atomic operations**, locks, database transactions, doing check-and-use **in one step**.

**On the exam**

- "Script saved in a forum post or review runs for every visitor" → **stored XSS**. "Script in a phishing link" → **reflected**. "Never reaches the server" → **DOM-based**
- "One common password tried across thousands of accounts" → **password spraying**
- "Server fetches a user-supplied URL that points to 169.254.169.254" → **SSRF**
- "Site loaded in an invisible iframe" → **clickjacking** → X-Frame-Options / frame-ancestors
- "Two withdrawals both pass the balance check" → **race condition / TOCTOU** → atomic transaction
- "Session ID unchanged after login" → **fixation** → new ID at login
- **Trap:** random IDs don't fix IDOR; **authorization checks** do.

**Quick check + your answers**

1. Product review with JavaScript steals every shopper's session: XSS type + cookie flag? → **Stored (persistent)** + **HttpOnly**. (You first said reflected/DOM, then corrected yourself to stored.)

2. "Winter2026!" tried once on each of 50,000 accounts despite per-account lockout → **password spraying** ✅

3. Preview URL pointing to 169.254.169.254 returns cloud credentials → **SSRF**, fixed by **allow-listing destinations** ✅

**Quick check:** (1) Review with JS steals every shopper's session: XSS type + cookie flag? (2) 'Winter2026!' tried once on 50,000 accounts: attack? (3) Preview URL to 169.254.169.254 leaks cloud creds: attack + fix?

**Answer:** Password spraying; SSRF + allow-list; HttpOnly. Correct.

</details>

<a name="t-5-1-45"></a>
**Spoofing** (review)

Pretending to be another user, system or source (IP, email, DNS, caller ID).

> On the exam: Defenses: strong authentication, digital signatures, mutual TLS, DNSSEC, email authentication (SPF, DKIM, DMARC).

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Spoofing named; SPF/DKIM/DMARC not recalled. Marked shaky.

</details>

<a name="t-5-1-46"></a>
**Password attacks and rainbow tables**

Brute force (try everything), dictionary (common words), hybrid, credential stuffing, rainbow tables (precomputed hash lookups).

> On the exam: Defense: unique salts defeat rainbow tables; slow hashing (bcrypt, Argon2) makes brute force expensive; MFA makes stolen passwords insufficient.

<details><summary>Lesson (10 Nov 2026)</summary>

**5.1 Batch 3: Crypto in code (10 topics)**

*Exam angle: no math. Pick the right crypto tool for the job, spot dangerous choices (weak algorithms, missing salts, reused IVs), and know what each control does and doesn't protect against.*

**1. Password storage (topic 23)**

- **Never store passwords in plain text, and never encrypted.** Encryption is **reversible**, so whoever gets the key gets every password.
- **Store a salted, slow (adaptive) hash:**
  - **Argon2id** (the modern recommendation) · **bcrypt** · **scrypt** · **PBKDF2** (when FIPS-approved algorithms are required)
  - "**Slow**" is the point: a **work factor** makes each guess expensive, so cracking millions of guesses takes far longer.
- **Never use fast hashes alone** (MD5, SHA-1, or even plain SHA-256). They're built for speed, so attackers can test **billions of guesses per second**.
- **Unique salt per password**, stored next to the hash.
- **Optional pepper:** an extra **secret** value stored **separately** from the database (e.g. in an HSM), so a stolen database alone isn't enough.
- **Upgrade path:** when moving to a stronger algorithm, **re-hash at the user's next login**.

**2. Password attacks and rainbow tables (topic 46)**

- **Online attacks:** guessing against the **live login page** (brute force, dictionary, spraying, stuffing). Defense: **rate limiting, lockout, MFA**.
- **Offline attacks:** the attacker **already stole the hash database** and cracks it on their own machines, with no limits. Defense: **slow, salted hashes**.
- **Brute force** (every combination) · **dictionary** (common words) · **hybrid** (words + variations like `Password1!`)
- **Rainbow tables:** **precomputed** tables of password → hash. The attacker just **looks up** each stolen hash instantly.
  - **Defeated by salts:** each password has a **different random salt**, so a precomputed table would be needed **for every salt**, which is impossible.

**Hook:** **A rainbow table is a cheat sheet of answers. A salt changes the question for every user, so the cheat sheet is useless.**

**3. Salt, IV and nonce (topic 31) — exam favorite: three "random extras" with different jobs**

- **Salt** → for **password hashing**: random, **unique per password**, stored **with** the hash, **not secret**. Stops **rainbow tables** and hides when two users share a password.
- **IV (initialization vector)** → for **encryption**: a random **starting value**, so the **same plaintext with the same key** gives **different ciphertext** each time. **Not secret**; must be **unique** (and **unpredictable** for CBC mode).
- **Nonce ("number used once")** → for **uniqueness**: must **never repeat** with the same key. In **AES-GCM**, nonce reuse is **catastrophic** (exposes data, breaks integrity protection). Also used in protocols to **stop replay**.
- **Pepper** → the only one that **is secret**.

**Hook:** **Salt seasons passwords. IV varies the encryption. Nonce is used once. Pepper is the secret ingredient.**

**4. Transport encryption: TLS (topic 29)**

- **TLS 1.2 or 1.3 only.** Disable SSL 2.0/3.0 and TLS 1.0/1.1.
- **TLS 1.3** removes weak ciphers and **always uses forward secrecy**.
- **Strong cipher suites:** authenticated encryption (AES-GCM, ChaCha20-Poly1305) + **ECDHE** (forward secrecy: stealing the server's key later can't decrypt old traffic).
- **Validate certificates properly:** hostname, trusted chain, expiry, revocation. Disabling validation "to make it work" = opening the door to MITM.
- **HSTS** forces browsers to always use HTTPS.
- **Encrypt internal traffic too** (zero trust); **mTLS** between services where needed.

**5. Database encryption (topic 30)**

- **TDE (Transparent Data Encryption):** encrypts the **database files and backups** (data AT REST).
  - ✅ Protects against **stolen disks, files or backups**
  - ❌ Does **NOT** protect against **SQL injection** or anyone querying through the app: the database **decrypts automatically** for valid queries
- **Column / field-level encryption:** specific sensitive fields; even **DBAs** can't read them without the key; harder to search/index.
- **Application-level encryption:** the **app encrypts before data reaches the database** — strongest separation.
- **Keys kept separate** from data (KMS/HSM); **backups encrypted** too.

**Hook:** **TDE locks the filing cabinet. SQL injection walks in through the front office and asks the clerk (the database) to read the files out loud.**

**6. Tokenization (topic 17)**

- Replace the sensitive value with a **random token**; the real value lives only in a secure **token vault**.
- **Unlike encryption**, a token has **no mathematical relationship** to the original: it **can't be decrypted**, only **looked up**.
- **Reduces PCI DSS scope** (systems holding only tokens aren't handling card data). **Format-preserving** tokens keep old systems working.
- **The vault** is the high-value target.

**7. Crypto agility (topic 21)**

- Swap algorithms or key sizes **without rewriting the app** (config, not code).
- **How:** crypto abstraction layer · **store the algorithm identifier** with each ciphertext/hash · **inventory** of crypto use (CBOM).
- **Why now:** algorithms get retired (MD5, SHA-1); **post-quantum** is coming — NIST's first PQC standards in **2024** (FIPS 203, 204, 205).

**8. Don't roll your own crypto (topic 25)**

- Never invent algorithms or write your own implementations (side channels, padding oracles, weak randomness).
- **Use vetted libraries** (platform crypto API, libsodium, OpenSSL/BoringSSL, Bouncy Castle) and **FIPS 140-validated modules** where required.
- Prefer **high-level APIs** with safe defaults; misusing a good library (ECB mode, hard-coded IV) is almost as bad. (= open design + leverage existing components, Domain 1.)

**9. Algorithm selection (topic 22)**

- **Symmetric:** **AES** (128/256) in an **authenticated mode**: **GCM** or **ChaCha20-Poly1305**. ❌ **Never ECB** — identical blocks → identical ciphertext, patterns show (the "ECB penguin").
- **Asymmetric:** **RSA 2048+** (3072 long-term) or **ECC** (P-256, Curve25519; same strength, shorter keys).
- **Hashing:** **SHA-256/384, SHA-3**. ❌ MD5, SHA-1 (collisions).
- **Key exchange:** **ECDHE** (forward secrecy). **Passwords:** Argon2/bcrypt, not a general hash.
- **Retired:** DES, 3DES, RC4, MD5, SHA-1, RSA-1024.

**10. Encryption scope (topic 20)**

Decide **what**, **where**, at **what level**, driven by **data classification**:

- **At rest:** disks, databases, files, **backups** · **In transit:** TLS everywhere incl. internal · **In use:** memory (confidential computing enclaves, e.g. Intel SGX)
- **Granularity:** **full-disk** protects only a **powered-off, stolen** device (running + unlocked = readable) · file · database · field · **end-to-end** (only endpoints can read)
- **Key management** is the hardest part: encryption is only as strong as where the keys live.

**On the exam**

- Unsalted SHA-256 cracked in hours via precomputed lookups → **rainbow tables / fast hash** → **unique salts + Argon2/bcrypt**
- Help desk can decrypt passwords → wrong: **hash**, never encrypt
- Same plaintext always → same ciphertext → missing/reused **IV** (or **ECB**)
- Nonce reused in AES-GCM → **catastrophic**
- TDE on, SQL injection still dumps card numbers → TDE = files at rest only → **field/app-level encryption or tokenization** + fix the injection
- Reduce PCI scope → **tokenization** · switch algorithms fast → **crypto agility** · custom cipher → **don't roll your own**
- **Traps:** salts and IVs are **not secret** (pepper is); full-disk encryption doesn't protect a running system; tokens can't be decrypted, only looked up.

**Hooks**

**Salt seasons passwords. IV varies encryption. Nonce = once. Pepper = the secret. Rainbow table = cheat sheet; salt changes the question. TDE locks the cabinet, not the drawer. Never ECB: the penguin shows through.**

**Quick check + your answers**

1. Unsalted SHA-256 table cracked via precomputed lookups: attack + two fixes → **Rainbow tables**; fixes **unique salts** ✅ (you got this) + **slow hash (Argon2/bcrypt)**. (You said "app-level encryption" for the attack.)

2. Identical records → identical ciphertext: what's missing → **a unique random IV** (or ECB mode is in use). (You said catastrophic/algorithm selection — that's nonce reuse, a different issue.)

3. TDE on, SQLi dumps card numbers in plain text: why, and what helps → TDE is **at rest** (files/disk), the DB **decrypts for any valid query**, so injection gets plain text → **field/app-level encryption or tokenization** + **parameterized queries**. (You said TDE = in transit; it's at rest.)

**Quick check:** (1) Unsalted SHA-256 cracked via precomputed lookups: attack + two fixes? (2) Identical records give identical AES ciphertext: what's missing? (3) TDE on, SQL injection dumps card numbers: why, and what helps?

**Answer:** Mixed up; see corrections in lesson (rainbow tables + salt/slow hash; unique IV; TDE = at rest, DB decrypts for queries). Marked shaky.

</details>

<a name="t-5-1-47"></a>
**Side channel attack types**

Timing attacks, power analysis (simple and differential), electromagnetic emanations (TEMPEST), acoustic cryptanalysis, differential fault analysis (inducing errors), cold boot attacks (reading memory after power off), distant observation (shoulder surfing).

> On the exam: Defenses: constant-time code, shielding (TEMPEST), clearing keys from memory, tamper-resistant hardware.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-48"></a>
**Diffie-Hellman and key exchange**

Lets two parties create a shared secret over an insecure network without sending it. It doesn't authenticate either party on its own.

> On the exam: Trap: plain Diffie-Hellman is vulnerable to man-in-the-middle unless combined with authentication (certificates). Ephemeral versions (DHE/ECDHE) give perfect forward secrecy.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-49"></a>
**Digital envelope and hybrid encryption**

Encrypt data with a fast symmetric key, then encrypt that key with the recipient's public key. Used by TLS, PGP and S/MIME.

> On the exam: Why: symmetric is fast for bulk data; asymmetric solves key distribution.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-50"></a>
**Crypto key concepts**

Key length and strength (longer = stronger; ECC gives equal strength with shorter keys than RSA), work factor (effort needed to break), symmetric key count problem (n(n-1)/2 keys for n users), key clustering.

> On the exam: Scenario cue: 'strong encryption on a low-power device' → ECC.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-51"></a>
**Cryptanalysis attacks**

Brute force, known plaintext, chosen plaintext, ciphertext-only, birthday attack (finding hash collisions), downgrade attacks, side channels.

> On the exam: Defenses: strong modern algorithms and key lengths, collision-resistant hashes (no MD5/SHA-1), disable old protocol versions.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-52"></a>
**Steganography and watermarking**

Steganography hides data inside other data (an image). Digital watermarking embeds ownership marks to trace leaks or prove ownership.

> On the exam: Security angle: steganography can be used to exfiltrate data; watermarking supports anti-piracy and leak tracing.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 5: Crypto deep dive + protecting data (9 topics)**

*Exam angle: which technique does what (key exchange vs encryption vs hashing vs hiding), and the names of attacks.*

**1. Diffie-Hellman and key exchange (topic 48)**

- Two parties **create a shared secret key over an insecure network without ever sending the key**.
- Analogy: each mixes a **secret paint color** into a shared public color, swaps the mix, adds their secret again → both get the **same final color**; an eavesdropper can't work it out.
- **⚠️ DH doesn't authenticate anyone** → a **MITM** can run a separate exchange with each side. Fix: authenticate (certificates, digital signatures), as TLS does.
- **Ephemeral** DH (**DHE / ECDHE**) = fresh keys per session → **forward secrecy**. **ECDH** = elliptic curve version.

*Hook: DH = agreeing on a secret in a crowded room — but still check who you're whispering with.*

**2. Digital envelope and hybrid encryption (topic 49)**

- Symmetric = fast but key-sharing problem; asymmetric = solves sharing but slow.
- Envelope: (1) encrypt **data** with a random **symmetric key** (AES) → (2) encrypt that key with the **recipient's public key** → (3) recipient unlocks the key with their **private key**, then the data.
- Used in TLS, PGP, S/MIME, cloud **envelope encryption** (KMS): **DEK** encrypts data, **KEK/master key** encrypts the DEK.
- **Why not encrypt everything with the master key?** Slow for big data, every file would go to the KMS, and the master key should **never leave** the HSM/KMS; a leaked data key exposes only its own file.

*Hook: lock the letter in a fast box (AES), then put the box's key in an envelope only the recipient can open.*

**3. Crypto key concepts (topic 50)**

- Longer = stronger; **ECC same strength with shorter keys**: ~**256-bit ECC ≈ 3072-bit RSA ≈ 128-bit AES**.
- **Key space** (2ⁿ) · **work factor** (effort to break) · **key stretching** (PBKDF2, bcrypt) · **cryptoperiod / rotation** · **KEK vs DEK** · key escrow · split knowledge / dual control.
- **Exam math:** symmetric keys for n people = **n(n−1)/2**; asymmetric = **2n**. 10 people → **45** vs **20**.

**4. Cryptanalysis attacks (topic 51)**

Least → most attacker power: **ciphertext-only** (only ciphertext) → **known-plaintext** (plaintext + ciphertext pairs) → **chosen-plaintext** (picks plaintexts, sees them encrypted) → **chosen-ciphertext** (picks ciphertexts, sees them decrypted).

Others: **brute force** · **birthday** (hash **collisions**, ~2^(n/2) tries) · **meet-in-the-middle** (why double DES isn't much stronger) · **frequency analysis** · **downgrade** (force weaker protocol/cipher: POODLE, FREAK) · **rubber-hose** (coercion).

**5. Steganography and watermarking (topic 52)**

- **Steganography** = hiding the **existence** of a message inside other data (image/audio low bits); used for exfiltration/hiding malware; detected by steganalysis, DLP.
- **Watermarking** = embedding an **ownership/identity mark** (visible or invisible) to **trace leaks** (unique mark per copy); deters + traces, doesn't prevent copying.

*Hook: encryption hides what it SAYS, steganography hides that it EXISTS, watermarking shows who OWNS it.*

**6. Data protection techniques compared (topic 32)**

Encryption (reversible with key; confidentiality) · hashing (one-way; integrity, passwords) · tokenization (vault lookup; PCI scope) · masking (`****1234`; **static** for test data vs **dynamic** at display) · anonymization (irreversible; GDPR no longer applies) · pseudonymization (reversible with separate key; still personal data) · redaction (permanently removed) · **encoding/Base64 = NOT security**.

*Hook: encoding is a costume, not a lock.*

**7. Obfuscation (topic 10)**

Rename identifiers, scramble control flow, encrypt strings, add dead code → slows **reverse engineering**, protects IP/licensing (bytecode languages). **Not a control on its own** (security through obscurity); harder debugging; malware uses it too.

**8. Spoofing (topic 45)**

Pretending to be another user/system/source (STRIDE **S**):

- **IP spoofing** (DoS reflection, IP-based trust) → ingress/egress filtering; never trust IP alone
- **Email spoofing** (fake From, phishing) → **SPF** (guest list of allowed sending servers) · **DKIM** (Digital Key In Mail: cryptographic signature) · **DMARC** (the Manager: policy for failures — reject/quarantine/report — plus reports)
- **ARP spoofing** (LAN MITM) → dynamic ARP inspection · **DNS spoofing / cache poisoning** → **DNSSEC** · caller ID, MAC, look-alike domains
- General fix: **authenticate the source cryptographically**.

**9. Secure configuration management (topic 16)**

Secure baseline + **secure defaults** (debug off, default accounts removed, unneeded features off) · **no hard-coded credentials** (vault, runtime injection) · protect config files (permissions, encrypt sensitive values) · separate config per environment · changes via change mgmt / IaC · detect and fix **drift**.

**On the exam**

- Agree a key without sending it → **DH** (needs authentication vs MITM) · fresh keys per session → **ECDHE / forward secrecy**
- AES data + AES key encrypted with recipient public key → **digital envelope**
- Symmetric keys for 10 people → **45** · submit any text, see ciphertext → **chosen-plaintext**
- Two files, same hash → **birthday/collision** · forced onto old protocol → **downgrade**
- Data hidden in an image → **steganography** · unique mark per copy → **watermarking**
- Fake sender in emails → **email spoofing** → SPF, DKIM, DMARC
- **Traps:** Base64 is encoding, not encryption; obfuscation isn't protection; DH alone doesn't authenticate.

**Quick check + your answers**

1. Data key encrypts files, master key in KMS encrypts the data key → **digital envelope (envelope encryption)** ✅; why: big data is slow with the master key, master key never leaves KMS/HSM, a leaked data key exposes only one file (your reason was vague; refined here).

2. Type any text into "encrypt this" and see the result → **chosen-plaintext** ✅

3. Emails appear from the CEO but come from an attacker server → **email spoofing** ✅; the three controls **SPF, DKIM, DMARC** were not recalled → spoofing marked shaky.

**Quick check:** (1) Data key + KMS master key pattern: name + why not master key directly? (2) Type any text into 'encrypt this' and see the result: attack class? (3) Emails appear from CEO, sent by attacker server: attack + three email controls?

**Answer:** Digital envelope (why refined); chosen-plaintext; email spoofing. Correct.

</details>

<a name="t-5-1-53"></a>
**Access control: NDAC, resource-based and role hierarchies**

Non-discretionary access control: central authority assigns access (RBAC is a form of it). Resource-based access control: access depends on the resource's identity. Role hierarchies: senior roles inherit junior roles' rights.

> On the exam: RBAC supports least privilege and separation of duties by giving roles only needed rights and preventing conflicting roles for one user.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-54"></a>
**Trusted subsystem vs impersonation and delegation**

Trusted subsystem: the app accesses the database with its own service identity, not the user's (common in web apps); simple but the app must enforce user authorization. Impersonation/delegation: the app acts as the user downstream, so the database sees the real user.

> On the exam: Scenario cue: 'database auditing must show which end user made each change' → impersonation/delegation, not a trusted subsystem.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

<a name="t-5-1-55"></a>
**Interpreted, compiled and hybrid languages**

Compiled (C, C++): turned into machine code before running; fast, but memory errors possible. Interpreted (Python, JavaScript): executed line by line at runtime. Hybrid (Java, C#): compiled to bytecode, then run by a virtual machine with JIT compilation.

> On the exam: Security angle: interpreted and bytecode programs are easier to reverse engineer; compiled native code is more prone to memory corruption.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-56"></a>
**Memory management basics**

Stack: fixed-size, holds function calls and local variables. Heap: dynamic memory allocated at runtime. Garbage collection frees unused memory automatically in managed languages.

> On the exam: Security: free memory exactly once, clear sensitive data (keys) from memory after use, avoid relying on garbage collection to erase secrets.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 4: Memory, languages and concurrency (9 topics)**

*Exam angle: what goes wrong when code manages memory and shared resources badly, and which defenses fit which problem.*

**1. Memory management basics (topic 56)**

- **Stack:** fixed-size area for **function calls**, **local variables**, **return addresses**; freed automatically on return (LIFO).
- **Heap:** **dynamic** memory allocated at runtime (`new`, `malloc`); freed **manually** (C/C++) or by **garbage collection** (Java, C#, Python).
- **Classic memory bugs:**
  - **Memory leak:** never freed → runs out (DoS risk)
  - **Use-after-free:** using freed memory → crash or **code execution**
  - **Double free:** freeing twice → heap corruption
  - **Dangling pointer** · **null pointer dereference** → crash
  - **Uninitialized memory:** leftover data (may hold secrets)
- **Zeroize secrets** (passwords, keys) in memory after use.

**2. Buffer overflows: stack and heap (topic 38)**

Writing **more data than a buffer holds**, spilling into neighboring memory.

- **Stack overflow:** overwrites the **saved return address** → execution jumps to **attacker code** (classic).
- **Heap overflow:** corrupts **heap data/metadata** (function pointers, adjacent objects).
- **Causes:** unchecked copies (`strcpy`, `gets`, `sprintf`), off-by-one, **integer overflow** in length math.
- **Defenses in layers:** code (bounds checks, **safe functions** `strncpy`/`strlcpy`, `snprintf`, `fgets`, length validation) · language (**memory-safe**: Rust, Go, Java, C#) · compiler/OS (**stack canaries**, **ASLR**, **DEP/NX**, CFI / Intel CET) · testing (SAST + **fuzzing**).

*Hook: 2 liters into a 1-liter glass — it spills onto whatever is next to it, and the attacker decides what spills.*

**3. Interpreted, compiled and hybrid languages (topic 55)**

- **Compiled** (C, C++, Rust, Go): machine code before running; fast; C/C++ memory risks; harder to reverse engineer.
- **Interpreted** (Python, JS, PHP, Ruby): run line by line; **source often shipped** (logic + secrets exposed); `eval()` → injection risk.
- **Hybrid** (Java, C#): **bytecode / IL** on a **VM** (JVM, .NET CLR) with **JIT**; managed memory; **easy to decompile** → obfuscation.

**4. Resource management (topic 15)**

- **Acquire → use → release** (files, sockets, DB connections, locks) even on errors (`try/finally`, `using`, `with`).
- **Limits:** quotas, timeouts, max sizes, connection pools → prevents **resource exhaustion** (DoS).
- **Integer overflow** (255 + 1 = 0 in 8 bits) → wrong sizes → overflows; validate, safe math.
- Check return values · **algorithmic complexity attacks** (e.g. **ReDoS**).

**5. Thread safety, locks and deadlocks (topic 3)**

- Shared data changed by several threads → corruption / **race conditions**.
- Tools: **mutexes/locks**, semaphores, **atomic operations**, **immutable objects**.
- **Deadlock:** A holds lock 1 waits for 2; B holds 2 waits for 1 → forever. Fix: **same lock order**, **timeouts**, short locked sections.
- **Starvation** (never gets a turn; fair scheduling) · **livelock** (keep reacting, no progress).

*Hook: deadlock = two people in a narrow hallway, each waiting for the other to step aside.*

**6. Database concurrency controls (topic 4)**

- **ACID:** Atomicity (all or nothing) · Consistency (valid states) · Isolation (no interference) · Durability (committed = permanent).
- **Isolation levels** (weak → strong): read uncommitted (**dirty reads**) → read committed → repeatable read → **serializable**.
- **Pessimistic** locking: lock first (safe, slower, deadlock risk) · **optimistic**: version check at save, retry on conflict (fast when conflicts rare).
- Weak control → **lost updates**, **race conditions** (double withdrawal).

**7. Random numbers (topic 24)**

- **Normal PRNGs** (`Math.random()`, `rand()`, `System.Random`) are **predictable** → never for security.
- **CSPRNG:** `SecureRandom` (Java), `RandomNumberGenerator` (.NET), `crypto.getRandomValues` (JS), Python `secrets`, `/dev/urandom`.
- For keys, IVs, nonces, salts, **session IDs**, tokens, **reset links**. Needs good **entropy**; NIST **SP 800-90A** (DRBGs).

*Hook: Math.random() is a coin you can predict; a CSPRNG is a coin nobody can.*

**8. Side channel attack types (topic 47)**

- **Timing** → constant-time code
- **Power analysis:** **SPA** (simple: read secrets directly from one trace) · **DPA** (differential: statistics over many traces)
- **Electromagnetic** emanations (**TEMPEST**) · **acoustic** cryptanalysis · **cache** attacks (Spectre/Meltdown family) · **fault injection / glitching**
- Defenses: constant-time code, **masking/blinding**, shielding, noise, **secure elements**.

**9. Trusted vs untrusted APIs and libraries (topic 14)**

- Trusted = vetted, maintained, known source; untrusted = unknown, abandoned, unvetted.
- Vet: SCA, license, maintenance, reputation · **wrap** untrusted libraries · least privilege.
- **Banned functions** (Microsoft SDL list): `strcpy`, `strcat`, `sprintf`, `gets`, unbounded `scanf` → bounded safe versions.
- Treat data **from third-party APIs** as untrusted (validate).

**On the exam**

- `strcpy` into fixed buffer, return address overwritten → **stack buffer overflow** → safe functions + canaries/ASLR/DEP
- Memory used after freed → **use-after-free** · decompiled Java logic → **hybrid/bytecode** → obfuscation
- Unclosed files/connections exhaust server → **resource management** (DoS)
- Threads wait for each other's locks → **deadlock** → lock order, timeouts
- Tokens from `Math.random()` → predictable **PRNG** → **CSPRNG**
- Key extracted from many power traces → **DPA** · strongest isolation → **serializable**
- **Traps:** managed languages still have logic flaws; obfuscation isn't protection; normal PRNG never OK for tokens.

**Quick check + your answers**

1. `strcpy` 200 bytes into a 64-byte stack buffer → **stack buffer overflow**; defenses **safe functions** (code) + **stack canaries** (compiler) ✅

2. Reset tokens from `Math.random()` → normal **PRNG** is predictable → use a **CSPRNG** ✅

3. Two threads each holding one lock, waiting for the other → **deadlock** → **timeouts** (+ consistent lock order) ✅

**Quick check:** (1) strcpy 200 bytes into 64-byte stack buffer: attack + code defense + compiler/OS defense? (2) Reset tokens from Math.random(): what's wrong + fix? (3) Two threads each hold one lock, wait for the other: name + prevention?

**Answer:** Stack buffer overflow, safe functions + canaries; PRNG → CSPRNG; deadlock → timeouts (+ lock order). All correct.

</details>

<a name="t-5-1-57"></a>
**Privileged code and secure startup**

Keep privileged code small and separate; switch privilege levels only when needed. Secure startup: initialize the app into a secure state (load config safely, verify integrity, fail closed if setup fails).

> On the exam: Scenario cue: 'app starts in debug mode if config is missing' → insecure startup; should fail securely.

<details><summary>Lesson (12 Nov 2026)</summary>

**5.1 Batch 6: Access control, trust and privilege (9 topics)**

*Exam angle: how authorization is built (config vs code, which model), whose identity reaches the backend, and how to contain powerful code.*

**1. Declarative vs imperative security (topic 1)**

- **Declarative:** rules **declared in configuration/annotations**, enforced by the **framework/container** (`[Authorize(Roles = "Admin")]` in .NET, `@PreAuthorize` in Spring, `security-constraint` in web.xml). ✅ consistent, centralized, **easy to audit**, change **without recompiling** · ❌ **coarse-grained** ("admins only", not "only the owner of this invoice").
- **Imperative (programmatic):** checks **written in code** (`if (invoice.OwnerId != currentUser.Id) return Forbid();`). ✅ **fine-grained, context-aware** (ownership, amounts, time) · ❌ scattered, easy to **forget one**, harder to audit.
- **Combine:** declarative for broad role rules, imperative for object-level checks (how IDOR gets fixed).

*Hook: declarative = the "Staff only" sign on the door; imperative = the guard checking whether this file is yours.*

**2. Access control models (topic 27)**

- **DAC:** owner decides (ACLs); malware running as you gets your access.
- **MAC:** system enforces labels/clearances; nobody overrides (military, Bell-LaPadula, SELinux).
- **RBAC (role-based):** permissions → roles → users; scalable, least privilege; risk = **role explosion**.
- **ABAC:** attributes of user, resource, action, **environment** (department, clearance, time, location, device); most fine-grained; policies in **XACML**.
- **Rule-based:** global rules for everyone (firewall rules, "no logins after 10 pm").
- **Risk-based / adaptive:** live risk score (new device → MFA).
- **⚠️ Trap:** Role-based vs Rule-based both "RBAC": role = job title; rule = global condition.

*Hooks: DAC = owner's Decision · MAC = Must follow labels · RBAC = job Role · ABAC = Attributes (who, what, where, when).*

**3. NDAC, resource-based access and role hierarchies (topic 53)**

- **NDAC:** central authority assigns access; users can't change it; RBAC + rule-based are forms of NDAC.
- **Identity-based** policy (on the user/role) vs **resource-based** policy (on the resource itself, e.g. **AWS S3 bucket policy**).
- **Role hierarchies:** senior roles **inherit** junior permissions (Manager ⊇ Employee); easy admin, can silently over-grant.
- **SoD in RBAC:** **static SoD** = can never be assigned conflicting roles · **dynamic SoD** = may hold both, can't activate both in one session.

**4. Trusted subsystem vs impersonation and delegation (topic 54)**

- **Trusted subsystem:** app authenticates the user, then reaches the DB with **its own service account**; DB trusts the app. ✅ simple, connection pooling, no direct DB access · ❌ DB can't see the real user → **the APP must log the real user for every action**; app compromise = everything the service account can do → keep it **least-privileged** (separate control; doesn't fix the audit gap).
- **Impersonation:** server acts **as the user** on the **same machine**; resource sees the real user; no pooling.
- **Delegation:** impersonation across **network hops** to other servers (**Kerberos constrained delegation**); restrict where it can go.

*Hook: concierge — own master key (trusted subsystem), wears your badge in this building (impersonation), takes your badge to other buildings (delegation).*

**5. Trust zones and function permissions (topic 26)**

- Group components by **trust level** (internet → DMZ → app → data; untrusted vs trusted modules) and **check every crossing**.
- **Function-level authorization:** authorize **every function/endpoint/action**, not just the page/menu. Failure = hidden admin API (`/api/admin/deleteUser`) callable by a normal user (**broken function level authorization**, OWASP).
- Mobile app permissions; ARM TrustZone secure vs normal world.

**6. Processor security extensions (topic 28)**

- **Intel SGX:** **enclaves** even the OS/hypervisor can't read (confidential computing; side-channel history)
- **AMD SEV / Intel TDX:** encrypt **VM memory** so the **hypervisor/cloud host** can't read it
- **ARM TrustZone:** **secure world** (keys, payments) vs **normal world**
- **NX/XD bit** (hardware DEP) · **Intel CET** (shadow stack + indirect branch tracking → blocks **ROP**) · **SMEP/SMAP** (kernel can't execute/access user memory)

**7. Separation Kernel Protection Profile, SKPP (topic 19)**

NSA **Common Criteria protection profile** for **separation kernels**: tiny, high-assurance kernel splitting one system into **isolated partitions** with **only policy-approved flow** between them; basis of **MILS** (military, avionics); ties to **small TCB / reference monitor**. Older, still examined.

*Hook: apartment walls so thick neighbors can't hear each other, with one strictly guarded door.*

**8. Privileged code and secure startup (topic 57)**

- **Privilege separation:** tiny privileged part + unprivileged worker (OpenSSH).
- **Elevate only when needed, drop immediately** (bind port 443 as root, then switch to a normal user).
- **Secure startup:** start in a secure state (load + **verify** config/integrity, secure defaults), **fail secure** if init fails, don't run as admin/root, part of the secure boot chain.

**9. Sandboxing and isolation (topic 18)**

Restricted execution to **contain** damage: OS sandboxes (**seccomp**, AppArmor/SELinux profiles), **browser** sandboxes, mobile app sandboxes, **containers**, **VMs**, **WebAssembly**, managed runtimes. Strength: process &lt; container &lt; VM &lt; physical machine. Use for untrusted code, plugins, risky file parsing, **AI agents' tools**.

*Hook: a sandbox is a playpen — whatever happens inside stays inside.*

**On the exam**

- Edit only invoices you created → **imperative** · change permissions without recompiling → **declarative**
- Department + time + device decide → **ABAC** · owner sets → **DAC** · unoverridable labels → **MAC**
- Policy on an S3 bucket → **resource-based** · never both conflicting roles → **static SoD**
- One service account, DB logs can't show the user → **trusted subsystem** → audit in the app
- User's identity used to reach another server → **delegation**
- Normal user calls hidden admin API → **broken function-level authorization**
- VM memory safe from the hypervisor → **AMD SEV / Intel TDX** · tiny partitioning kernel → **SKPP**
- Bind 443 as root then switch user → **dropping privileges**
- **Traps:** role-based vs rule-based; hiding a button isn't authorization; trusted subsystem loses the user's identity at the DB.

**Quick check + your answers**

1. "Edit only invoices you created" → **imperative** ✅; why refined: it depends on ownership of the specific record, which declarative role rules can't express.

2. One service account, DB can't show which user → **trusted subsystem** ✅; auditing refined: the **application must log the real user**; least-privilege account is a separate control.

3. VM memory protected from the hypervisor → **Intel TDX** ✅ (or AMD SEV).

**Quick check:** (1) 'Edit only invoices you created': declarative or imperative, why? (2) One service account for all users; DB logs can't show who: model + auditing? (3) VM memory protected from the cloud hypervisor: technology?

**Answer:** Imperative (ownership needs record context); trusted subsystem (app must log real user); Intel TDX / AMD SEV. Correct with refinements.

</details>

## 5.2 Analyze code for security risks

<a name="t-5-2-1"></a>
**Secure code reuse**

Reuse vetted, maintained code; track it and patch it.

> On the exam: What it is: reusing existing code or components safely: use trusted sources, review before reuse, track versions (SBOM), keep them patched.
Scenario cue: 'old internal library with known flaws copied into new projects' → insecure reuse; patch the source and track all copies.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-2"></a>
**OWASP Top 10**

Most critical web app risks (broken access control, injection, crypto failures...). Know the current list.

> On the exam: What it is: OWASP's list of the most critical web app risks, updated every few years. Recent lists include broken access control (first), cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, authentication failures, integrity failures, logging failures, SSRF.
Trap: it's an awareness document, not a complete standard; for complete requirements use ASVS.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-3"></a>
**CWE vs CVE**

CWE is a type of weakness; CVE is a specific vulnerability in a specific product.

> On the exam: CWE (Common Weakness Enumeration): a category of mistake, e.g., CWE-89 SQL injection. CVE (Common Vulnerabilities and Exposures): a specific vulnerability in a specific product version, e.g., Log4Shell CVE-2021-44228.
Scenario cue: 'which list helps developers avoid classes of coding errors?' → CWE. 'Which tracks a specific flaw in a product?' → CVE.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-4"></a>
**CWE / SANS Top 25**

Most dangerous software weaknesses.

> On the exam: What it is: the 25 most dangerous software weaknesses, based on real CVE data (out-of-bounds write, XSS, SQL injection, use-after-free, missing authorization and similar).
Use: prioritize training, coding standards and SAST rules on these.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-5"></a>
**SAST** (review)

Static analysis of source or binaries without running it. White-box, early, fast, but more false positives.

> On the exam: Runs early, even before the code compiles. Finds injection patterns and hardcoded secrets; can't see runtime or configuration problems.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** Did not map SAST to own-code CWE. Shaky.

</details>

<a name="t-5-2-6"></a>
**Code coverage and linting**

How much code tests exercise; linters catch risky patterns and style issues.

> On the exam: Code coverage: how much code tests executed (statement, branch, path). Linting: automated checks for bad patterns and style.
Trap: 100% coverage doesn't mean secure; it shows code ran, not that it was tested for attacks.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-7"></a>
**Manual code review** (review)

Finds business logic and design flaws tools miss; peer review.

> On the exam: Strengths: finds business logic flaws, authorization mistakes, crypto misuse and backdoors that tools miss. Weaknesses: slow, depends on reviewer skill.
Best practice: use tools first, then manually review high-risk code (authentication, authorization, crypto, input handling).
Scenario cue: 'which method best finds a flaw in business logic?' → manual code review.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** Did not name manual code review as the catching practice. Shaky.

</details>

<a name="t-5-2-8"></a>
**Malicious code**

Backdoors, logic bombs, time bombs, hidden accounts; high-entropy strings can reveal hidden secrets or packed code.

> On the exam: Logic bomb fires on an event; time bomb on a date. Insiders plant backdoors, so code review and separation of duties are the defense.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

<a name="t-5-2-9"></a>
**SAMATE and OWASP guides**

NIST SAMATE (Software Assurance Metrics And Tool Evaluation) evaluates code analysis tools and provides test suites. OWASP Code Review Guide, Testing Guide and Developer Guide give practical methods.

> On the exam: Scenario cue: 'reference test cases to evaluate a static analysis tool's accuracy' → NIST SAMATE.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** CWE vs CVE, logic bomb, SAMATE correct.

</details>

## 5.3 Implement security controls

<a name="t-5-3-1"></a>
**Watchdogs**

Timers that detect a hung process and restart it.

> On the exam: What it is: a timer the program must reset regularly; if it doesn't (because it hung or crashed), the watchdog restarts or alerts.
Use: availability in embedded and critical systems.
Scenario cue: 'device must recover automatically if its software freezes' → watchdog timer.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-3-2"></a>
**File integrity monitoring (FIM)**

Compares file hashes to a baseline to detect changes.

> On the exam: What it is: compares current hashes of critical files (binaries, configs) with a known-good baseline and alerts on changes (e.g., Tripwire, OSSEC).
Control type: detective.
Scenario cue: 'detect unauthorized changes to web server files' → FIM.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-3-3"></a>
**Anti-malware** (review)

Signature- and behavior-based detection.

> On the exam: Signature-based: matches known malware, misses new variants. Heuristic/behavior-based: spots suspicious actions, catches new malware with more false positives.
Scenario cue: 'detect zero-day malware' → behavior-based or EDR, not signatures alone.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Answered "traps"; answer = behavior-based (heuristic). Shaky.

</details>

## 5.4 Address identified security risks

<a name="t-5-4-1"></a>
**Risk strategy**

Mitigate, accept, transfer, or avoid; prioritize by severity and business impact.

> On the exam: Options: mitigate (fix or add controls), accept (document, owner signs), transfer (insurance, contract), avoid (remove the feature or don't do the activity).
Scenario cue: 'a feature has a vulnerability with no fix and low business value' → avoid by removing the feature.
Who decides: the business/risk owner, not the developer.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-4-2"></a>
**Exceptions**

Documented, approved acceptance of risk with an owner and review date.

> On the exam: What it is: formal, approved permission to not meet a requirement for now.
Must include: business justification, risk owner sign-off, compensating controls, expiration or review date.
Scenario cue: 'a team ignores a policy because of a deadline' → should go through the exception process.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

## 5.5 Evaluate and integrate components

<a name="t-5-5-1"></a>
**Systems-of-systems integration**

Security must hold where independent systems connect.

> On the exam: What it is: combining independent systems into a larger one. Each may be secure alone but create gaps together (different assumptions about authentication, encoding or trust).
Scenario cue: 'two secure systems connected leak data through their interface' → test security at integration points.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-5-2"></a>
**Trust contracts**

Agreements defining what each integrated component guarantees.

> On the exam: Spell out assumptions like 'input is already validated', then verify them rather than trusting them.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-5-3"></a>
**Software composition analysis (SCA)** (review)

Inventories third-party and open source components; flags known vulnerabilities and license issues.

> On the exam: What it is: tools that inventory third-party and open-source components, match them to known vulnerabilities (CVEs) and check license obligations; can produce an SBOM.
Scenario cue: 'find vulnerable open-source libraries in our application' → SCA.
Don't confuse: SAST checks your code; SCA checks components you imported.

<details><summary>Lesson (13 Nov 2026)</summary>

**5.2 + SCA, Batch A: Analyzing code for security risks (10 topics)**

*Exam angle: which technique finds which kind of problem (tools vs humans, your code vs other people's code), and the names of the standard lists and resources.*

**1. Secure code reuse (5.2.1)**

- Reusing **vetted, maintained** code = fewer bugs (leverage existing components, Domain 1).
- **But you inherit its vulnerabilities:** track it (inventory / SBOM), check licenses, keep it patched.
- **No copy-paste** from forums, blogs or AI assistants without review.

**2. OWASP Top 10 (5.2.2)**

Most critical **web app risks**; an **awareness** document, not a standard. 2021 list (used by most CSSLP materials):

A01 **Broken Access Control** (#1) · A02 Cryptographic Failures · A03 **Injection** (XSS included) · A04 **Insecure Design** (missing threat modeling) · A05 Security Misconfiguration · A06 Vulnerable and Outdated Components · A07 Identification and Authentication Failures · A08 Software and Data Integrity Failures (unsigned updates, insecure deserialization, CI/CD tampering) · A09 Security Logging and Monitoring Failures · A10 SSRF.

**3. CWE vs CVE (5.2.3)**

- **CWE** (MITRE) = a **type** of weakness (CWE-89 SQLi, CWE-79 XSS) → root cause, coding standards, training.
- **CVE** = **one specific vulnerability in one product version** (CVE-2021-44228 Log4Shell) → NVD adds CVSS → patching.

*Hook: CWE = the type of disease; CVE = one specific patient.*

**4. CWE/SANS Top 25 (5.2.4)**

MITRE's yearly list of the **most dangerous software weaknesses** from real data: out-of-bounds write, XSS, SQLi, use-after-free, OS command injection, improper input validation, path traversal, CSRF, missing authorization. Use to prioritize training + SAST rules. OWASP Top 10 = web risk categories; CWE Top 25 = weakness types for any software.

**5. SAST (5.2.5)**

Static analysis of source/bytecode/binaries **without running** (white-box). ✅ early (IDE, PR, CI), **exact file + line**, injection patterns, **hard-coded secrets**, unsafe functions. ❌ false positives, no runtime/config/deployment view, weak on business logic/authorization, language-specific. Tune rules, triage, incremental scans.

**Family: SAST = your code at rest · DAST = running app from outside · IAST = inside running app · SCA = other people's code you include.**

**6. Code coverage and linting (5.2.6)**

- **Coverage** = how much code tests run: statement · branch/decision · condition · path (hardest). **High coverage ≠ secure.**
- **Linting** = style + risky-pattern checks (ESLint, Pylint, Roslyn analyzers) with security plugins, in CI.

**7. Manual code review (5.2.7)**

Humans catch **business logic flaws**, authorization bypasses, design issues, race conditions, crypto misuse. Forms: PR peer review, pair programming, **Fagan inspection**, security-focused review of high-risk code. Checklists (OWASP Code Review Guide), small chunks, high-risk focus, combine with tools. **Two-person rule** (nobody merges their own code). **Catches malicious code like logic bombs that tools see as valid code** ("why does this exist? which requirement?").

**8. Malicious code (5.2.8)**

Backdoor (bypasses authentication) · **logic bomb** (triggers on a CONDITION) · **time bomb** (triggers at a DATE/TIME) · hidden/hard-coded accounts · Easter eggs · trojan code · exfiltration. Signs: unexplained obfuscation, unexplained network calls, hard-coded credentials, **high-entropy strings**, code with **no requirement** (backward traceability). Catch: manual review of every diff, SAST, signed commits, separation of duties.

*Hook: logic bomb = "IF this happens…"; time bomb = "WHEN the clock says…".*

**9. SAMATE and OWASP guides (5.2.9)**

- **NIST SAMATE** (Software Assurance Metrics And Tool Evaluation) **evaluates code analysis tools**; **SARD** (Software Assurance Reference Dataset) = test programs with **known flaws** to benchmark SAST tools (**Juliet** test suite).
- **OWASP:** Code Review Guide, WSTG, Cheat Sheet Series, ASVS (the standard), Top 10, SAMM, Dependency-Check.

*Hook: SAMATE tests the testers.*

**10. Software composition analysis, SCA (5.5.3)**

Inventories third-party/open-source components incl. **transitive** · matches vulnerability DBs (NVD, GitHub Advisories, OSV) · **license** checks (GPL in closed source) · generates the **SBOM** · monitors **after release** (new CVEs, Log4j) · **reachability analysis** cuts noise. Tools: Dependabot, Snyk, OWASP Dependency-Check.

*Hook: SAST checks the code you wrote; SCA checks the code you borrowed.*

**On the exam**

- #1 OWASP 2021 risk → **broken access control** · missing threat modeling → **insecure design**
- CWE-79 → weakness type · CVE-2021-44228 → specific vulnerability
- Scan source before it runs, exact line → **SAST** · known-vulnerable library version → **SCA**
- 95% coverage, flaws remain → **coverage ≠ security** · business-logic flaw → **manual code review**
- Wipes data if developer fired → **logic bomb** · on 1 January → **time bomb**
- NIST known-flaw test programs for SAST tools → **SAMATE / SARD**
- **Traps:** Top 10 = awareness list (ASVS = standard); SAST can't see runtime config; high coverage ≠ secure.

**Quick check + your answers**

1. CWE-89 in your code, CVE-2021-44228 in a library → weakness type vs specific vulnerability ✅; tools: **SAST** finds CWE-89 in your code, **SCA** finds the library CVE (you didn't know the tools; said "Log4Shell will find each").

2. Code deletes payroll if the developer's ID is removed → **logic bomb** ✅; practice: **manual code review / peer review of every change** (you didn't know).

3. NIST known-flaw test programs → **SAMATE** ✅

**Quick check:** (1) CWE-89 in your code, CVE-2021-44228 in a library: which is which, which tool finds each? (2) Code deletes payroll if developer's ID removed: name + review practice? (3) NIST project with known-flaw test programs for tools?

**Answer:** Did not map SCA to library CVE. Shaky.

</details>

<a name="t-5-5-4"></a>
**Dependency confusion / typosquatting** (review)

Attackers publish lookalike or same-named packages to get them installed.

> On the exam: Dependency confusion: attacker publishes a public package with the same name as your internal one and a higher version, so the build pulls theirs. Typosquatting: lookalike names (reqeusts instead of requests).
Defenses: private registry with scoped names, pin versions, verify hashes, review new dependencies.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Named dependency confusion; fix not recalled. Shaky.

</details>

## 5.6 Security during the build

<a name="t-5-6-1"></a>
**Code signing**

Proves publisher and integrity of build output.

> On the exam: What it is: signing builds with a private key so users and systems can verify who published it and that it wasn't changed.
Key points: protect signing keys in an HSM; use timestamping so signatures stay valid after the certificate expires.
Trap: a signature proves origin and integrity, not that the code is free of bugs or malware.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-2"></a>
**Obfuscation**

Anti-reverse-engineering and anti-tampering measure.

> On the exam: What it is: scrambling compiled code (renaming, control-flow changes, string encryption) to make reverse engineering and tampering harder.
Use: mobile and desktop apps where attackers have the binary.
Trap: slows attackers but doesn't stop them; never rely on it to hide secrets.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-3"></a>
**Compiler switches**

Stack canaries (/GS, -fstack-protector), ASLR/PIE, DEP/NX, CFG, FORTIFY_SOURCE, RELRO.

> On the exam: Examples: stack canaries (/GS, -fstack-protector) detect stack overflows; ASLR/PIE randomizes addresses; DEP/NX blocks executing data; Control Flow Guard and CET block hijacked jumps; FORTIFY_SOURCE adds bounds checks; RELRO protects tables.
Scenario cue: 'reduce the impact of memory corruption without changing source code' → enable compiler and linker security switches.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-4"></a>
**Compiler warnings**

Fix them; treat warnings as errors.

> On the exam: What it means: compiler warnings often reveal real issues (uninitialized variables, type mismatches, unsafe functions). Set the build to treat warnings as errors.
Scenario cue: 'thousands of ignored warnings in the build' → potential vulnerabilities hidden in them.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-5"></a>
**Reproducible builds**

Same source produces the same binary, so tampering can be detected.

> On the exam: What it is: building the same source always produces bit-for-bit the same binary, so independent parties can verify nothing was injected during the build.
Scenario cue: 'how do you detect a compromised build server inserting malicious code (like SolarWinds)?' → reproducible builds and comparing outputs.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-6"></a>
**Anti-reversing techniques**

Obfuscation, packing and encrypting code, anti-debugging checks (detecting debuggers, e.g., IsDebuggerPresent), integrity self-checks, stripping symbols.

> On the exam: Testing: anti-reversing protection testing confirms these work. Trap: they raise attacker effort; they don't make secrets safe on the client.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

<a name="t-5-6-7"></a>
**DRM and anti-piracy**

Digital Rights Management controls how content or software is used (copying, devices, expiry). Anti-piracy: license keys, activation, online checks, code signing, watermarking.

> On the exam: Legal: the DMCA makes circumventing these protections illegal in the US.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch B: Security during the build (5.6) + runtime controls (5.3) — 10 topics**

*Exam angle: the build pipeline is where you harden the binary and prove it's genuine; then three classic runtime controls watch it in production.*

**1. Code signing (5.6.1)**

- Sign build outputs (executables, packages, container images, updates, scripts) with the publisher's **private key** + a **code-signing certificate** from a trusted CA.
- Proves **who** published it and that it **hasn't changed**; OSes check it (Windows SmartScreen, macOS Gatekeeper).
- **Timestamping:** a **timestamp authority (TSA)** records **when** it was signed → signature **stays valid after the certificate expires**.
- Protect the signing key: **HSM**, sign only in a **controlled pipeline step**, tight access. Stolen key → attackers sign malware as you → **revoke** immediately.
- Container images: **Sigstore/cosign**, Notary. **⚠️ Signed ≠ safe** (SolarWinds was signed).

**2. Obfuscation at build time (5.6.2)**

Build tools: **ProGuard/R8** (Android), .NET obfuscators, JS minifiers/obfuscators. Renaming, **string encryption**, control-flow scrambling. Protects IP/licensing; **not** a control alone. Can break **reflection**; keep **mapping files** secure (needed for crash reports).

**3. Compiler switches (5.6.3)**

| Protection | Windows (MSVC) | Linux (GCC/Clang) |

|---|---|---|

| Stack canary | **/GS** | **-fstack-protector-strong** |

| ASLR | **/DYNAMICBASE** | **-fPIE -pie** |

| DEP / NX | **/NXCOMPAT** | **-z noexecstack** |

| Control-flow protection | **/guard:cf** (CFG) | **-fcf-protection** (CET) |

| Checked library functions | safe CRT | **-D_FORTIFY_SOURCE** |

| Read-only relocations | — | **-Wl,-z,relro,-z,now** (Full RELRO) |

Sanitizers (ASan, UBSan) = testing builds, not production.

*Hook: /GS = Guard the Stack · /DYNAMICBASE = moving base · /NXCOMPAT = No eXecute.*

**4. Compiler warnings (5.6.4)**

Raise levels (`-Wall -Wextra`, `/W4`), **treat warnings as errors** (`-Werror`, `/WX`). Warnings flag real bugs: uninitialized variables, format strings, implicit conversions/truncation, ignored return values.

**5. Reproducible builds (5.6.5)**

Same source + same environment → **bit-for-bit identical** output → anyone can rebuild and **compare hashes**; different hash = **build tampering** (SolarWinds-type). Needs pinned dependencies/toolchains, no timestamps/randomness. Supports **SLSA** provenance.

*Hook: same recipe, same cake; a different cake means someone tampered with the kitchen.*

**6. Anti-reversing techniques (5.6.6)**

Obfuscation · **packing** (self-unpacking compressed/encrypted executable) · code encryption · **anti-debugging** (`IsDebuggerPresent`, timing checks, breakpoint detection) · **anti-tampering / self-integrity checks** · root/jailbreak detection · emulator/VM detection · certificate pinning. Only **raise cost**; malware uses the same tricks.

**7. DRM and anti-piracy (5.6.7)**

**DRM** controls how content/software is used (copying, devices, expiry, offline). Anti-piracy: **license keys**, **online activation**, **hardware binding / node-locking**, **license servers** (floating/concurrent), **dongles**, **watermarking**. Trade-offs: usability, privacy, availability (activation server down), still crackable. Legal: **DMCA** anti-circumvention.

**8. Watchdogs (5.3.1)**

Monitored process must **check in regularly** ("kick/pet"); if it stops (hung/crashed), the watchdog **restarts/resets** it. Hardware (embedded/IoT) or software (systemd watchdog, **Kubernetes liveness probes**). Availability. **Log every restart** (repeated restarts may signal an attack).

*Hook: a dead man's switch.*

**9. File integrity monitoring, FIM (5.3.2)**

**Baseline hashes** of critical files → compare periodically/real-time → **alert on unauthorized change**. Tools: **Tripwire**, AIDE, OSSEC/Wazuh. **Required by PCI DSS**. Tie expected changes to **change management** to cut noise.

**10. Anti-malware (5.3.3)**

- **Signature-based:** known patterns/hashes; fast, few false positives; **misses zero-day + polymorphic** malware.
- **Heuristic / behavior-based:** suspicious **actions** (mass encryption, process injection); catches **new** threats; more false positives.
- **Sandboxing/detonation** · **EDR** (continuous monitoring, investigation, response) · **application allow-listing** (only approved programs run — often the strongest) · keep updated · scan uploads.

*Hook: signature = a wanted poster (known faces only); behavior = a guard watching what people do.*

**On the exam**

- Signature valid after cert expired → **timestamping** · stolen signing key → HSM + **revoke**
- /GS → canaries · /DYNAMICBASE → ASLR · /NXCOMPAT → DEP
- Independent rebuild hash differs → **reproducible builds** reveal **build tampering**
- Refuses to run under a debugger → **anti-debugging** · license tied to one machine → **node-locking**
- Hung service auto-restarted → **watchdog** · `/bin/login` changed with no change ticket → **FIM** → investigate
- Brand-new ransomware → **behavior-based** detection · only approved programs run → **application allow-listing**
- **Traps:** signed ≠ safe; obfuscation/anti-reversing raise cost only; signature AV misses zero-days.

**Quick check + your answers**

1. Signature still valid two years later after the cert expired → **timestamping** ✅

2. Independent rebuilds give a different hash than the release → **build tampering**, detectable thanks to **reproducible builds** ✅

3. Brand-new ransomware → **behavior-based (heuristic)** detection (you answered "traps"; allow-listing would also stop it).

**Quick check:** (1) Signature still valid after code-signing cert expired: why? (2) Independent rebuilds give a different hash than the release: meaning + practice? (3) Brand-new ransomware: which anti-malware detection?

**Answer:** Timestamping; build tampering via reproducible builds. Correct.

</details>

## 5.AI AI additions in the current outline

<a name="t-5-ai-1"></a>
**Prompt injection**

Direct (from the user) or indirect (hidden in content the model reads) instructions that hijack an LLM.

> On the exam: Defenses: treat model output as untrusted, give tools least privilege, separate instructions from data, require human approval for actions.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-ai-2"></a>
**Sanitizing LLM inputs**

Validate and filter what goes into the model, not just what comes out.

> On the exam: What it means: filter and validate what goes into an LLM (user input and retrieved documents), and also treat what comes out as untrusted before displaying or executing it.
Scenario cue: 'model output containing script tags is shown in the web page' → improper output handling leading to XSS.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-ai-3"></a>
**Provenance of AI-generated code**

Track where code came from; review and scan it like any untrusted code.

> On the exam: What it means: know which code came from AI tools, review and scan it like third-party code, and check it doesn't copy licensed code.
Scenario cue: 'AI-generated code contains a vulnerable, outdated function' → insufficient review of generated code.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Formal exception; dependency confusion; prompt injection. Correct.

</details>

<a name="t-5-ai-4"></a>
**Constraining AI agents** (review)

Declarative boundaries limiting what autonomous agents can do.

> On the exam: What it means: limit agents with allow-listed tools, least-privilege credentials, rate limits, and human approval for high-impact actions.
Scenario cue: 'an agent deleted production data after reading a malicious instruction' → missing constraints and approvals.

<details><summary>Lesson (13 Nov 2026)</summary>

**Batch C: Handling risk (5.4), integrating components (5.5), AI (5.AI) — 9 topics, the last of Domain 5**

*Exam angle: what to do after you find a risk (fix, accept or formally except it), what goes wrong between systems, and how AI changes secure coding.*

**1. Risk strategy (5.4.1)**

Responses: **mitigate** (fix/controls; usual) · **transfer** (insurance, contracts) · **avoid** (remove the feature) · **accept** (documented, signed by the **business owner**).

Prioritize: severity (CVSS) × likelihood × **business impact** (asset criticality), with **remediation SLAs**. Fix the **root cause**; if delayed, a **compensating control** (WAF virtual patch); track in the **risk register**; **retest** fixes.

**2. Exceptions (5.4.2)**

When a requirement can't be met now (legacy, vendor limit, deadline): **formal exception request** — what's not met, the **risk**, **business justification**, **compensating controls** · **owned and approved by the business owner** at the right level (not the developer) · **time-bound** (expiry/review date) · **tracked** in the risk register. **Not** permission to ignore; permanent "temporary" exceptions are a classic failure.

*Hook: an exception is a permission slip with an expiry date, signed by the owner.*

**3. Systems-of-systems integration (5.5.1)**

Independent systems (own owners, tech, lifecycles) joined into a bigger one (hospital: lab + billing + pharmacy + insurer). **Emergent risk at the connections:** mismatched assumptions (A thinks B validated; B thinks A did — nobody did) · weakest link · cascading failures · shared identity/federation. Mitigate: interface specs, **end-to-end threat modeling**, **validate at every boundary**, mutual authentication, consistent policies, **integration testing**.

**4. Trust contracts (5.5.2)**

Explicit agreements on what each component **guarantees** and **expects**: input formats + who validates, authn/authz, data classification/handling, error behavior, SLAs. **Design by contract:** **preconditions**, **postconditions**, **invariants**. Documented as interface specs / API schemas (OpenAPI) and ISAs/MOUs between organizations. **Trust but verify** (test them).

*Hook: a handshake written down, so nobody assumes the other one checked.*

**5. Dependency confusion and typosquatting (5.5.4)**

- **Dependency confusion:** public package with the **same name** as your private one (`acme-utils`) and a **higher version** → build pulls the attacker's code (2021 research). **Fixes:** **scoped/namespaced** packages (`@acme/utils`) · build fetches internal names **only from the private registry** · **pin versions + lockfile + hash checks** · **register internal names publicly**.
- **Typosquatting:** look-alike names (`reqeusts`). Fixes: dependency allow-lists, review new dependencies, SCA reputation checks.
- **Slopsquatting:** attackers register names AI assistants hallucinate.

*Hook: dependency confusion = same name, newer badge; typosquatting = near-identical name.*

**6. Prompt injection (5.AI.1)**

Instructions that hijack an LLM. **Direct** (user types "ignore your instructions…") vs **indirect** (hidden in content the model reads: web pages, emails, documents, RAG data). **OWASP LLM Top 10 #1 (LLM01).** Impact: data leakage, unauthorized tool actions. **Can't be fully prevented** → defense in depth.

**7. Sanitizing LLM inputs (5.AI.2)**

Length limits · flag/strip instruction-like patterns · **separate system instructions from user content** (roles, delimiters) · **treat retrieved content as untrusted data, never instructions** · guardrail classifiers · **redact PII/secrets** before sending · rate limits · still **validate outputs**. Filtering reduces, doesn't eliminate.

**8. Provenance of AI-generated code (5.AI.3)**

Label/record AI-generated code (commit metadata) · **mandatory human review** + **SAST + SCA** · check insecure patterns, hard-coded secrets, **hallucinated packages**, **license/copyright** · audit trail · only **approved AI tools**.

**9. Constraining AI agents (5.AI.4)**

**Declarative boundaries:** least-privilege tools/permissions · scoped short-lived credentials · **allow-listed actions/recipients** · **human approval** for high-impact actions (payments, deletion, external email) · sandboxed execution · rate/budget limits · full **logging** · **kill switch**. Risk name: **excessive agency (OWASP LLM06)**.

*Hook: an AI agent is an intern with superpowers — a short task list, a supervisor, and no master key.*

**On the exam**

- Fix delayed months, risk temporarily accepted → **formal exception** (owner-approved, time-bound, compensating controls, risk register) · who signs → **business owner**
- Each system assumed the other validated → **systems-of-systems** → validate at every boundary
- Documented preconditions/guarantees → **trust contract**
- Public package with internal name installed → **dependency confusion** → scoped names, private feed, pinning · `reqeusts` → **typosquatting**
- Hidden web text makes chatbot leak data → **indirect prompt injection**
- Agent deletes records without approval → **excessive agency** → least privilege + human approval
- **Traps:** exception ≠ permanent acceptance; prompt injection can't be fully filtered; AI code gets the same scrutiny as untrusted code.

**Quick check + your answers**

1. Legacy app can't support MFA for 6 months → **formal exception** ✅ (+ owner-approved, time-bound, compensating controls, risk register)

2. Public `acme-utils` v99 installed over internal v1.2 → **dependency confusion** ✅; fix not recalled → scoped names / private-only feed / pinning + lockfile / register names publicly.

3. Email assistant obeys hidden "forward all invoices" → **(indirect) prompt injection** ✅; control not given → human approval for external sends, draft-only least privilege, allow-listed recipients, treat email content as data.

**Quick check:** (1) Legacy app can't support MFA for 6 months: governance handling? (2) Public acme-utils v99 installed over internal v1.2: attack + one fix? (3) Email assistant obeys hidden 'forward all invoices': attack + one control?

**Answer:** Named prompt injection; limiting control not given. Shaky.

</details>
