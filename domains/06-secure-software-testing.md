# Domain 6: Secure Software Testing

Exam weight: 14%

## 6.1 Security testing strategy and plan

<a name="t-6-1-1"></a>
**ISO/IEC/IEEE 29119**

International software testing standard.

> On the exam: What it is: international software testing standard covering concepts, test processes, documentation (test plans, test cases, reports) and techniques.
Scenario cue: 'which ISO standard defines a software testing process and documentation?' → ISO/IEC/IEEE 29119.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-2"></a>
**OSSTMM**

Open Source Security Testing Methodology Manual: measurable operational security testing.

> On the exam: What it is: the Open Source Security Testing Methodology Manual (ISECOM), a peer-reviewed methodology for measurable operational security testing across channels (human, physical, wireless, telecom, data networks).
Scenario cue: 'a scientific, measurable methodology for operational security testing' → OSSTMM.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-3"></a>
**Software Engineering Institute (SEI)**

Carnegie Mellon; CERT secure coding and testing guidance.

> On the exam: What it is: Carnegie Mellon's Software Engineering Institute, home of CERT. Known for CERT secure coding standards, CMMI (maturity model), the hybrid threat modeling method and security testing guidance.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-4"></a>
**NIST SP 800-115**

Technical guide to security testing and assessment.

> On the exam: What it is: NIST's technical guide to security testing: review techniques (documentation, logs, code), target identification (network discovery, scanning), vulnerability validation (pentesting, password cracking), with planning, execution and post-execution phases.
Scenario cue: 'which NIST publication guides planning a security assessment or pentest?' → SP 800-115.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-5"></a>
**OWASP WSTG and ASVS** (review)

Web testing guide; verification standard with levels 1-3.

> On the exam: WSTG: OWASP's Web Security Testing Guide, how to test web apps. ASVS: Application Security Verification Standard, a list of security requirements to verify, with levels: L1 basic (opportunistic attacks), L2 standard for most apps with sensitive data, L3 critical apps.
Scenario cue: 'define what to verify for a banking app' → ASVS Level 2 or 3. 'How to test for each issue' → WSTG.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** Mixed WSTG/ASVS (ASVS = checklist with levels; WSTG = how-to). Level 2 correct. Shaky.

</details>

<a name="t-6-1-6"></a>
**Functional security testing**

Do security features work correctly? Tests logic such as authorization rules.

> On the exam: What it is: testing that security features work as specified: login, lockout, access rules, encryption, logging.
Example: confirm user A can't open user B's invoice by changing an ID.
Don't confuse: functional checks the feature works; penetration testing checks whether attackers can break or bypass it.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-7"></a>
**Non-functional security testing**

Reliability, performance, load, scalability under stress.

> On the exam: What it is: testing qualities like reliability, performance, scalability and recoverability under stress.
Example: under heavy load, lockout still works and the system doesn't fail open.
Scenario cue: 'does the application stay available during a traffic spike?' → non-functional (load/stress) testing.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-8"></a>
**Known environment (white-box)** (review)

Tester has full knowledge of code and design.

> On the exam: What it is: tester knows everything: source code, architecture, credentials.
Strengths: most thorough coverage, finds logic flaws and hidden code paths. Weakness: less like a real outside attacker.
Scenario cue: 'maximum coverage in limited time with full access to code' → white-box.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** White-box correct but called it the attacker view (that is black-box); advantage thorough, drawback less realistic. Shaky.

</details>

<a name="t-6-1-9"></a>
**Unknown environment (black-box)**

Tester has no inside knowledge, like an outside attacker.

> On the exam: What it is: tester knows nothing about the internals, like an outside attacker.
Strengths: realistic view of what attackers see. Weaknesses: may miss code paths, takes longer.
Scenario cue: 'simulate an external attacker with no inside knowledge' → black-box.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-10"></a>
**Partially known (gray-box)**

Some knowledge, e.g., credentials or design docs.

> On the exam: What it is: tester has some knowledge, like user credentials or design documents.
Strengths: realistic yet efficient; simulates an insider or authenticated attacker.
Scenario cue: 'test what a logged-in customer could do maliciously' → gray-box.

<details><summary>Lesson (17 Nov 2026)</summary>

**Domain 6: Secure Software Testing — 6.1 Batch 1: Testing standards + kinds of testing (topics 1–10)**

*Domain exam angle: which test, which tool, which standard fits a situation, and who/when/how testing is planned.*

**1. ISO/IEC/IEEE 29119**

International standard for **software testing in general** (not security-specific). Parts: **1** concepts/definitions · **2** **test processes** (organizational, test management, dynamic testing) · **3** **test documentation** templates (test plan, status report, completion report) · **4** **test techniques** (specification-, structure-, experience-based) · **5** keyword-driven testing. Replaced **IEEE 829**. Promotes **risk-based testing**.

*Hook: 29119 = the rulebook for testing anything.*

**2. OSSTMM**

**Open Source Security Testing Methodology Manual** (**ISECOM**): peer-reviewed **operational** security testing. **Scientific and measurable** (repeatable, consistent, numeric results). Five **channels**: **human**, **physical**, **wireless**, **telecommunications**, **data networks**. Measures **attack surface**, controls and trust via **RAV** (risk assessment values). Report = **STAR** (Security Test Audit Report).

*Hook: OSSTMM = security testing with a measuring tape.*

**3. Software Engineering Institute (SEI)**

Carnegie Mellon research center (US government funded). Home of **CERT/CC** (vulnerability coordination since 1988) and the **CERT Secure Coding Standards** (C, C++, Java, Android); origin of CMMI, OCTAVE, hTMM. Exam: SEI = secure coding + testing guidance + CERT.

**4. NIST SP 800-115**

"Technical Guide to Information Security Testing and Assessment." Techniques: **review** (docs, logs, rulesets, configs, sniffing, file integrity) · **target identification and analysis** (network discovery, port/service ID, **vulnerability scanning**, wireless scanning) · **target vulnerability validation** (**password cracking**, **pen testing**, **social engineering**). Pen test model: **planning → discovery → attack → reporting** (discovery/attack loop).

*Hook: review, find, validate.*

**5. OWASP WSTG and ASVS**

- **WSTG (Web Security Testing Guide) = HOW to test**: methodology + test cases (info gathering, config, authentication, authorization, sessions, input validation, error handling, crypto, **business logic**, client-side, APIs). **No levels.**
- **ASVS (Application Security Verification Standard) = WHAT to verify**: requirements list in **3 levels**: **L1** basic (largely checkable from outside) · **L2** standard — **recommended for most apps with sensitive data** · **L3** high assurance for critical apps (medical, military, high-value finance), deep verification incl. architecture + code.
- Mobile: **MASVS** (what) and **MASTG** (how).

*Hook: WSTG = the how-to guide; ASVS = the checklist with three levels of strictness.*

**6. Functional security testing**

Do security features **work as specified**? From **security requirements** (+ traceability matrix). Authentication (lockout after N attempts), authorization (user can't reach admin data), session timeout, password policy, audit logging records events, encryption applied. **Positive + negative tests**.

**7. Non-functional security testing**

How well it **holds up under stress**: load (expected peak) · stress (beyond limits) · scalability · reliability/availability (failover) · resilience · DoS resistance. Security must **hold under pressure**: rate limiting keeps working, no detail leaks in errors, **fail secure** (closed).

*Hook: functional = does the lock work? non-functional = does it still work when 10,000 people push on the door?*

**8. Known environment (white-box)**

**Full knowledge** (source, architecture, docs, credentials); also **clear-box**. ✅ **Thorough, efficient**, deep issues (logic flaws, hidden paths), includes code review/SAST. ❌ **NOT the attacker's view** → less realistic.

**9. Unknown environment (black-box)**

**No inside knowledge** = the **attacker's view**. ✅ **Realistic** (DAST, external pen tests). ❌ Misses hidden code paths; discovery takes time.

**10. Partially known environment (gray-box)**

**Some** knowledge (user credentials, docs, API specs). ✅ Balance of realism + efficiency; very common (**authenticated** pen testing).

*Hook: white-box = lights on, blueprints in hand · black-box = breaking in at night with no map · gray-box = the visitor's guide.*

**On the exam**

- Test processes + documentation for any software → **29119** · measurable operational testing across 5 channels → **OSSTMM** · CERT + secure coding standards → **SEI** · planning/discovery/attack/reporting → **800-115**
- How to test a web app → **WSTG** · requirements to verify at levels 1–3 → **ASVS** · most apps with sensitive data → **Level 2**
- Lockout after 5 failures → **functional** · rate limiting at 10× traffic → **non-functional**
- Source code + admin creds → **white-box** · nothing → **black-box** · a normal user account → **gray-box**
- **Traps:** 29119 isn't security-specific; ASVS = what, WSTG = how; black-box most realistic but least thorough; white-box is NOT the attacker's view.

**Quick check + your answers**

1. Requirements to verify with levels → **ASVS** (+ Level 2 for most apps) — you said WSTG for the requirements part, then ASVS for the levels; ASVS answers both. Level 2 ✅

2. Source code + diagrams + admin creds → **white-box** ✅; you called it the attacker's view — it's the opposite: advantage = **thorough/deep**, drawback = **less realistic** (attacker's view = black-box).

3. Login skips MFA under heavy load → **non-functional** ✅

**Quick check:** (1) Requirements to verify with stricter levels: which OWASP resource + level for most apps? (2) Source code + diagrams + admin creds: type + one advantage + one drawback? (3) Login skips MFA under heavy load: which testing?

**Answer:** ASVS L2; white-box; non-functional.

</details>

<a name="t-6-1-11"></a>
**Acceptance testing (UAT)**

Confirms the system meets user and business needs before release.

> On the exam: What it is: users or the customer confirm the software meets business needs and acceptance criteria before going live; includes security acceptance criteria.
Scenario cue: 'final step before the business signs off on release' → acceptance testing (a validation activity).

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-12"></a>
**Test environment**

Mirrors production but is isolated from it.

> On the exam: What it is: an environment that mirrors production (versions, configs) but is isolated from it.
Rules: no connections to production systems; sanitize any production data; restrict access.
Scenario cue: 'tests pass but production fails' → test environment doesn't match production.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-13"></a>
**Interoperability testing**

Security still holds when working with other systems.

> On the exam: What it is: making sure the software works securely with other systems, platforms, browsers and protocol versions.
Scenario cue: 'to stay compatible with an old partner system, TLS 1.0 was enabled' → interoperability pressure weakening security.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-14"></a>
**Test harness**

Drivers, stubs and tools that run tests automatically.

> On the exam: What it is: the framework that runs tests automatically: test drivers (call the code), stubs (stand in for missing components), data and result reporting.
Why it matters: makes tests repeatable, which regression and continuous testing depend on.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-15"></a>
**Bug bounty**

Paying outside researchers for valid vulnerabilities.

> On the exam: What it is: paying outside researchers for valid vulnerabilities they find, within defined scope and rules.
Key points: needs clear scope, rules, legal safe harbor and a triage team ready to respond. Complements internal testing, never replaces it.
Scenario cue: 'get continuous testing from many skilled researchers, paying only for results' → bug bounty.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-16"></a>
**Vulnerability disclosure program** (review)

Public process to report flaws, with coordinated disclosure and safe harbor.

> On the exam: Gives researchers a legal way to report. Safe harbor promises not to sue good-faith researchers.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP named; key element (safe harbor / coordinated disclosure / security.txt) not given. Shaky.

</details>

<a name="t-6-1-17"></a>
**Software testing lifecycle (STLC)**

Phases: requirements analysis, test planning, test case design, test environment setup, test execution, test closure (report and lessons).

> On the exam: Security angle: security test cases come from security requirements and misuse cases during design of tests, not added at the end.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-18"></a>
**Quality assurance vs quality control**

QA: process-focused and preventive (standards, reviews, process audits). QC: product-focused and detective (testing the actual product).

> On the exam: Scenario cue: 'improve the development process to prevent defects' → QA. 'Run tests to find defects in the build' → QC.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-19"></a>
**Testing artifacts**

Test strategy (high-level approach and goals), test plan (scope, schedule, resources, criteria), test case (inputs, steps, expected result), test script (automated steps), test suite (collection of test cases), test harness (framework that runs them).

> On the exam: Scenario cue: 'document describing what to test, by whom, when and the pass/fail criteria' → test plan.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-20"></a>
**Flaw hypothesis method (FHM)**

A penetration testing method: 1) hypothesize flaws from documentation and known weaknesses, 2) confirm them by testing, 3) generalize to find similar flaws, 4) eliminate them.

> On the exam: Scenario cue: 'pentest approach that starts by predicting flaws from design documents' → FHM.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.1 Batch 2: The testing process + outside help (topics 11–20)**

*Exam angle: who tests, where, with which documents, and the differences between similar-sounding things (bug bounty vs VDP, QA vs QC, strategy vs plan).*

**11. Acceptance testing (UAT)**

End users / business confirm it meets **their needs** incl. security requirements, **before release**; ends in **formal sign-off**. Related: **alpha** (internal) / **beta** (external) · **operational acceptance (OAT)** (backups, recovery, monitoring, maintainability) · **contract** and **regulatory** acceptance. Security angle: roles/permissions right, security features usable; realistic but **sanitized** data.

**12. Test environment**

**Mirrors production** (same OS, versions, configs) → valid results · **isolated** (separate network/credentials) → can't break prod, prod data not exposed · **no real personal data** (synthetic/sanitized) · **staging** = most prod-like before release · **drift** from prod → results can't be trusted.

**13. Interoperability testing**

Works **correctly and securely with other systems**: protocols, data formats, **federated login** (SAML/OIDC), **TLS versions/ciphers**, API contracts. Risk: weakening security to "make it work" (fallback to old TLS = downgrade, weaker auth). Ties to trust contracts + systems of systems (5.5).

**14. Test harness**

Framework that runs tests **automatically and repeatably** (runners, data, reporting) plus **drivers** (call the component; stand in for the **caller**; **bottom-up**), **stubs** (fake components it calls; stand in for what's **below**; **top-down**), **mocks** (fakes that also check how they were called). Tests components before neighbors exist; runs in CI.

*Hook: driver = a fake boss giving orders; stub = a fake helper taking orders.*

**15. Bug bounty**

**Pay outside researchers per valid vulnerability** (HackerOne, Bugcrowd). Needs **scope**, **rules of engagement** (no DoS, no real user data), **reward tiers by severity**, **triage**. ✅ continuous, many eyes, pay for results · ❌ noise, duplicates, cost; doesn't replace internal testing.

**16. Vulnerability disclosure program (VDP)**

**Public way for anyone to report**, **no payment required** (thanks / hall of fame). Key elements: **safe harbor** (no legal action vs good-faith researchers) · **coordinated disclosure** (wait for the fix, commonly ~**90 days**) · clear contact (**`security.txt`**). Standards: **ISO/IEC 29147** (disclosure) · **ISO/IEC 30111** (internal handling). **US federal agencies must have a VDP** (CISA directive).

*Hook: VDP = a front door for reporting bugs; bug bounty = the same door plus a cash reward.*

**17. Software testing lifecycle (STLC)**

1 **Requirement analysis** (testable security requirements?) → 2 **Test planning** (strategy, scope, resources, schedule, **entry/exit criteria**) → 3 **Test case design** (cases, scripts, data) → 4 **Environment setup** → 5 **Execution** (run, log defects) → 6 **Closure** (report, metrics, lessons learned). **Entry criteria** = conditions to start a phase; **exit criteria** = conditions to finish.

**18. QA vs QC**

**QA** = **process**, **preventive**, proactive (standards, defined processes, reviews, **process audits**, training) — builds quality in. **QC** = **product**, **detective**, reactive (**testing**, inspection) — finds defects. **Testing is part of QC.**

*Hook: QA = the recipe and the kitchen rules; QC = tasting the dish before it's served.*

**19. Testing artifacts**

**Test strategy** (organization-wide approach, rarely changes) · **test plan** (this project's scope, schedule, resources, entry/exit criteria, risks) · **test case** (inputs, preconditions, steps, **expected result**) · **test script** (automated steps) · **test suite** (collection) · **test harness** · test data, logs/results, **defect reports**, **test summary (completion) report**, **traceability matrix**.

*Hook: strategy = HOW we test, everywhere; plan = WHAT, WHEN, WHO for this project.*

**20. Flaw hypothesis method (FHM)**

Classic pen test method (1970s) from knowledge of the system: 1 **gather information** (docs, specs, design, known weaknesses) → 2 **hypothesize flaws** (list) → 3 **confirm** (test each, most promising first) → 4 **generalize** (pattern → similar flaws elsewhere) → 5 **eliminate** (fixes).

*Hook: a detective's method — suspect → test the suspicion → look for accomplices → lock them up.*

**On the exam**

- Users confirm business needs + sign off → **UAT** · can ops back up/restore/monitor → **OAT**
- Test results don't match prod → environment **drift** · partner forces TLS 1.0 → **interoperability** risk (downgrade)
- Fake component not yet built → **stub** · public channel, no pay, safe harbor → **VDP** · paid per finding → **bug bounty**
- Disclosure standard → **ISO/IEC 29147** · internal handling → **ISO/IEC 30111**
- Process audits + coding standards → **QA** · testing the release candidate → **QC**
- This release's scope/schedule/exit criteria → **test plan** · brainstorm flaws from docs, test, find similar → **FHM**
- **Traps:** VDP doesn't have to pay; QA is not testing; strategy ≠ plan.

**Quick check + your answers**

1. Anyone can report safely, no rewards → **VDP** ✅; key element not named → safe harbor / coordinated disclosure / security.txt contact.

2. Coding standards + peer reviews + process audits → **QA** ✅

3. Docs → list likely weaknesses → test each → search similar → **flaw hypothesis method** ✅

**Quick check:** (1) Anyone can report safely, no rewards: program + one key element? (2) Coding standards, peer reviews, process audits to prevent defects: QA or QC? (3) Docs → likely weaknesses → test each → find similar: method?

**Answer:** VDP; QA; flaw hypothesis method. Correct.

</details>

<a name="t-6-1-21"></a>
**Other test types**

Smoke/sanity (quick check the build works), alpha (internal users) and beta (external users), logic testing (business rules can't be bypassed), privacy testing (data handling and consent), environment testing (secure configuration of the environment), disaster recovery testing, usability and accessibility testing.

> On the exam: Scenario cue: 'verify the discount can't be applied twice' → logic testing.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-1-22"></a>
**Motive, opportunity and means**

For an attack (and for proving cybercrime) three things are needed: motive (why), opportunity (a weakness and access) and means (skills and tools).

> On the exam: Security testing reduces opportunity by finding and removing weaknesses before attackers do.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-1-23"></a>
**Testing security functions vs security testing**

Testing security functionality checks that security features work as designed (login, encryption). Security testing checks whether an attacker can break or bypass the software, including features that aren't security features.

> On the exam: Trap: passing functional security tests doesn't mean the software is secure.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

## 6.2 Security test cases

<a name="t-6-2-1"></a>
**Attack surface validation**

Confirm entry points match the design and that unneeded ones are closed.

> On the exam: What it is: checking that the real entry points (ports, APIs, pages, parameters) match what the design and threat model say, and that unneeded ones are closed.
Scenario cue: 'a test finds an undocumented debug API' → attack surface validation failure.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-2"></a>
**DAST**

Tests the running app from outside. Black-box, no source needed, finds runtime issues, can't point to code lines.

> On the exam: Good for configuration, authentication, session and injection issues at runtime. Needs a running app, so it comes later in the SDLC.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-3"></a>
**IAST**

Agent inside the running app; combines runtime testing with code-level detail and fewer false positives.

> On the exam: What it is: Interactive Application Security Testing. An agent inside the running app watches code execution during tests.
Strengths: pinpoints the exact line of vulnerable code, low false positives, sees runtime data flow. Needs test traffic to exercise the app.
Scenario cue: 'find vulnerabilities in a running app and show which code line caused them' → IAST.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-4"></a>
**SAST vs DAST vs IAST vs SCA**

Code at rest / running app from outside / running app from inside / third-party components.

> On the exam: Earliest = SAST. Third-party libraries = SCA. Real-time protection in production = RASP (a control, not a test).

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-5"></a>
**Vulnerability scan vs penetration test**

A scan finds known issues automatically; a pentest exploits them to prove impact.

> On the exam: Scanning gives breadth; pentesting gives depth and proof. Written authorization is required before any pentest.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-6"></a>
**Penetration test phases**

Rules of engagement and written permission, recon, scanning, exploitation, reporting.

> On the exam: Rules of engagement set scope, timing and allowed techniques. Testing without written permission is illegal.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-7"></a>
**Fuzzing**

Sending malformed or random input to find crashes and unhandled errors.

> On the exam: What it is: sending large amounts of malformed, unexpected or random input to find crashes, hangs and memory errors.
Best for: parsers, file formats, network protocols, APIs.
Scenario cue: 'find unknown input-handling flaws in a file parser' → fuzzing.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 3: Test types, attacker thinking, start of 6.2 (6.1.21–23, 6.2.1–7)**

*Exam angle: which test catches which problem, and the differences between the main testing tools (a top Domain 6 comparison).*

**1. Other test types (6.1.21)**

**Smoke** (does the build work at all? "does it catch fire?") · **sanity** (narrow check of one area after a small change/fix) · **alpha** (internal, early) / **beta** (real external users) · **logic testing** (business rules can't be bypassed: negative quantities, skipping payment, coupon twice) · **privacy testing** (minimization, consent, retention, PII masking, settings honored) · **environment testing** (servers/OS/middleware/cloud hardened, patched, no default creds) · **DR testing** (restores work, failover, RTO/RPO met) · **usability + accessibility** (security features usable; WCAG).

*Hook: smoke = "does it turn on?"; sanity = "did my fix work?"*

**2. Motive, opportunity and means (6.1.22)**

**Motive** (why) · **opportunity** (access + weakness + time) · **means** (skills, tools, resources). Remove one → attack fails. Defenders reduce **opportunity** (patching, least privilege, monitoring) and **means** (allow-listing). Used in investigations and threat modeling.

*Hook: MOM — take away one and the crime can't happen.*

**3. Testing security functions vs security testing (6.1.23)**

**Security functionality testing** = security features work as designed (login, MFA, encryption, roles): "does the lock work?" · **Security testing** = adversarial, break/bypass anything incl. non-security features (upload, search, checkout): "can I get in some other way?" Both needed — passing all function tests can still leave XSS in a comment box.

*Hook: testing the lock vs trying every window.*

**4. Attack surface validation (6.2.1)**

Real surface must **match the design/threat model**: enumerate ports, URLs, APIs, admin + **debug endpoints**, compare, **close unneeded**. Tools: port scans, API discovery, crawling, config review; track vs baseline (RASQ). Finds shadow/zombie APIs, debug mode, test accounts.

**5. DAST (6.2.2)**

Running app **from outside**, real requests, **black-box**, no source. ✅ runtime + config issues (injection, XSS, misconfig, auth/session, headers, TLS), language-independent. ❌ late, **no code line**, misses unreached paths (needs crawling + login), can be disruptive → test env. Tools: **OWASP ZAP**, **Burp Suite**.

**6. IAST (6.2.3)**

**Agent inside the running app** while **functional/QA tests** run. ✅ accurate (few false positives) **+ exact code location**. ❌ instrumentation, language support, performance overhead, only covers **exercised** code. **IAST tests (QA); RASP protects (production, blocks).**

**7. SAST vs DAST vs IAST vs SCA (6.2.4)**

| | SAST | DAST | IAST | SCA |

|---|---|---|---|---|

| Looks at | your code at rest | running app, outside | running app, inside | third-party components |

| Box | white | black | gray | inventory |

| When | earliest (IDE, PR, CI) | late (deployed test env) | during QA | any time + after release |

| Strength | exact line | runtime + config | accurate + line | known CVEs, licenses, SBOM |

| Weakness | false positives, no runtime | no line, late | agent + tests needed | only known issues in others' code |

*Hook: SAST reads the code, DAST pokes from outside, IAST watches from inside, SCA checks the ingredients.*

**8. Vulnerability scan vs penetration test (6.2.5)**

**Scan:** automated, broad, known issues, frequent, cheap, false positives, **doesn't exploit**. **Pen test:** manual + tools, deep, **exploits** (often chaining) to **prove impact**, less frequent, costly, skilled testers, **written authorization**. Vulnerability assessment = scan + analysis/prioritization.

*Hook: a scan finds unlocked doors; a pen test walks through them to show what's inside.*

**9. Penetration test phases (6.2.6)**

1 **Pre-engagement:** scope, **rules of engagement** (targets, timing, allowed/forbidden e.g. no DoS/social engineering, data handling, emergency contacts), **written authorization** → 2 **Reconnaissance** (passive OSINT + active) → 3 **Scanning/enumeration** → 4 **Exploitation** → 5 **Post-exploitation** (privilege escalation, **lateral movement/pivoting**, persistence, proof of data access) → 6 **Reporting + cleanup** (remove tools/accounts). **No written permission = illegal** (CFAA); verbal isn't enough.

*Hook: Permission → Recon → Scan → Exploit → Post-exploit → Report.*

**10. Fuzzing (6.2.7)**

Automated **malformed/random/unexpected input** → crashes, hangs, memory errors, unhandled exceptions; run with **sanitizers** (ASan); **coverage-guided** fuzzers (AFL, libFuzzer). ✅ parsers, file formats, protocols, APIs. ❌ weak on business logic.

**On the exam**

- Coupon applied 5× → **logic testing** · new build even starts? → **smoke**
- Skills + tools but no access → missing **opportunity** · all security features pass but comment box has XSS → **function testing ≠ security testing**
- Debug endpoint in prod → **attack surface validation** · outside, no source → **DAST** · accurate + code lines during QA → **IAST** · vulnerable library versions → **SCA**
- Prove SQLi reaches data → **pen test** · first step → **scope + RoE + written authorization** · web server → DB server → **lateral movement** · corrupted PDFs into parser → **fuzzing**
- **Traps:** IAST ≠ RASP; scans don't exploit; verbal permission isn't enough; fuzzing misses logic flaws.

**Quick check + your answers**

1. Coupon five times on one order → **logic testing** ✅

2. Accurate findings + code locations during QA functional tests → **IAST** ✅

3. Manager said "go ahead" on a call → missing **scope, rules of engagement, written authorization** ✅ (why: otherwise legally unauthorized access, and no agreed limits).

**Quick check:** (1) Coupon applied five times: which testing? (2) Accurate findings + code locations while QA runs functional tests: tool? (3) Pen test started on a verbal 'go ahead': what's missing, why?

**Answer:** Logic testing; IAST; scope + RoE + written authorization. All correct.

</details>

<a name="t-6-2-8"></a>
**Generation-based fuzzing** (review)

Builds inputs from a specification or grammar; smarter, needs more setup.

> On the exam: What it is: inputs are created from a model, grammar or specification of the expected format.
Strengths: understands structure (checksums, lengths), reaches deeper logic. Weakness: needs effort to build the model.
Scenario cue: 'fuzz a complex protocol with checksums' → generation-based (smart) fuzzing.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation correct; drawback (more setup/model) not given. Shaky.

</details>

<a name="t-6-2-9"></a>
**Mutation-based fuzzing**

Modifies valid sample inputs; easy to start, less coverage of deep logic.

> On the exam: What it is: takes valid sample inputs and randomly changes bits or fields.
Strengths: easy and fast to start. Weakness: changed inputs may fail basic checks and never reach deep code.
Scenario cue: 'quick fuzzing with sample files and no specification' → mutation-based.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-10"></a>
**Simulation testing**

Production-like environment and data (sanitized).

> On the exam: What it is: testing in an environment that copies production as closely as possible (configs, load, realistic data).
Why: some security and performance problems only appear at production scale. Production data used must be sanitized first.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-11"></a>
**Synthetic transactions**

Scripted transactions that test or monitor behavior continuously.

> On the exam: What it is: scripted, fake transactions run regularly through the system, like a robot user.
Uses: testing, and continuous monitoring of availability and response time in production.
Scenario cue: 'detect that checkout is broken before customers report it' → synthetic transactions.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-12"></a>
**Fault injection** (review)

Deliberately introducing errors to see whether the system fails securely.

> On the exam: What it is: deliberately causing faults (network loss, disk full, bad responses, memory errors) to see how the system reacts.
Why: confirms it fails securely and recovers properly.
Scenario cue: 'verify the app denies access when the authentication server is unreachable' → fault injection.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** I answered the principle (fail secure) instead of the technique (fault injection). Shaky.

</details>

<a name="t-6-2-13"></a>
**Stress, load, and break testing**

Load = expected peak; stress = beyond limits; break = until failure.

> On the exam: Load: expected peak usage. Stress: beyond expected limits to see how it breaks. Break/destructive: pushed until failure. Soak/endurance: long duration to find leaks.
Scenario cue: 'how does the system behave during a DoS-level spike?' → stress testing.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-14"></a>
**Chaos engineering**

Randomly breaking production-like components to test resilience.

> On the exam: What it is: intentionally breaking components (shutting down servers, adding latency) in production-like environments to prove the system is resilient.
Scenario cue: 'prove the system survives random server failures' → chaos engineering.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-15"></a>
**Cryptographic validation**

Check PRNG quality, entropy, key lengths, correct implementation; FIPS 140-3 validated modules.

> On the exam: What it is: checking crypto is used correctly: approved algorithms, key lengths, good randomness and entropy, correct modes, validated modules (FIPS 140-3), proper key handling.
Scenario cue: 'keys generated on devices at first boot are similar to each other' → low entropy in the random number generator.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-16"></a>
**Unit testing**

Tests individual functions; developers write it early.

> On the exam: What it is: testing individual functions or classes, usually by developers, early and automated.
Security angle: include negative tests (invalid, malicious, boundary input), not just the happy path.
Scenario cue: 'earliest point to catch an input validation bug in a function' → unit testing.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-17"></a>
**Code coverage types**

Statement, branch, condition, path coverage.

> On the exam: Statement coverage: each line ran. Branch/decision coverage: each true/false outcome ran. Condition coverage: each condition in a decision. Path coverage: every possible route through the code (strongest, often impractical).
Scenario cue: 'every if/else outcome was tested' → branch coverage.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 4: Fuzzing, resilience testing, crypto validation, unit testing (topics 8–17)**

*Exam angle: which test fits which goal — crashes (fuzzing), behavior under failure (fault injection, chaos), under load (stress), in production (synthetic transactions).*

**8. Generation-based fuzzing**

Builds inputs from a **specification/grammar/protocol model** (knows the format: PNG, HTTP); inputs look valid, pass early checks, reach **deep logic**. ✅ smarter, deeper coverage · ❌ **more setup** (someone must build the model). Aka **smart / model-based**.

**9. Mutation-based fuzzing**

Takes real valid samples (**seed corpus**) and **randomly changes** them (flip bits, change lengths, insert chars). ✅ **easy to start**, no spec · ❌ many inputs rejected early (checksums, validation) → **shallower**. Aka **dumb** fuzzing; **coverage-guided** fuzzers (AFL, libFuzzer) keep mutations reaching new code.

*Hook: mutation = scribble on a real letter; generation = write new letters following the grammar, mistakes planted inside.*

**10. Simulation testing**

**Production-like environment** with realistic (sanitized) data, traffic, conditions (load patterns, latency, real integrations) → finds problems that only show up in real-world conditions.

**11. Synthetic transactions**

**Scripted fake transactions** run **automatically and regularly** (every 5 minutes: robot account logs in, adds item, checks out), in test or **production** → **synthetic monitoring** of availability, performance, correct behavior. vs **RUM** (passive real-user monitoring). Security: confirm controls still work (MFA still required), spot outages early.

*Hook: a mystery shopper that visits every 5 minutes.*

**12. Fault injection**

**Deliberately introduce errors** (kill a dependency, fill the disk, corrupted responses, drop the network) to check graceful handling and **failing secure**: fail **closed**, no detail leaks, no auth bypass via errors. Exercises rarely-run error-handling code. (Hardware glitching = side-channel cousin.)

**Exam tip:** "what kind of testing?" → name the TECHNIQUE (fault injection), not the PRINCIPLE it verifies (fail secure).

**13. Stress, load and break testing**

**Load** = expected peak · **stress** = beyond limits (degrade + recover?) · **break/destructive** = until failure (breaking point) · **soak/endurance** = long run (memory leaks) · **spike** = sudden bursts. Security: DoS resilience, fail secure, no leaks under exhaustion.

*Hook: load = rush hour; stress = a stampede; break = keep adding people until the bridge collapses.*

**14. Chaos engineering**

Deliberately, **randomly break components** in production-like or **production** environments to prove resilience (Netflix **Chaos Monkey**). Scientific: **hypothesis**, **limited blast radius**, observe, learn. **Security chaos engineering:** break a security control, check detection/response notices. vs **fault injection** = specific targeted error, usually in testing.

*Hook: Chaos Monkey loose in the server room.*

**15. Cryptographic validation**

Approved algorithms + key lengths · correct modes (no ECB) · IV/nonce handling · randomness/entropy tests (**NIST SP 800-22**) · key management · certificate validation · TLS config scans · **known-answer tests (KATs)**. Validated modules: **FIPS 140-3** via **CMVP** (whole modules) · **CAVP** (individual algorithms). **FIPS 140 levels:** **L1** basic (software OK) · **L2** **tamper-evidence** + role-based auth · **L3** **tamper-resistance** + identity-based auth · **L4** highest, full physical + environmental protection.

*Hook: correct → shows tampering → resists tampering → survives anything.*

**16. Unit testing**

Smallest units (functions/methods) **in isolation** (mocks, stubs); by **developers**; earliest + cheapest; automated in CI; heart of **TDD**. Include **security unit tests** (validator rejects bad input, authorization helper denies, crypto wrappers correct).

**17. Code coverage types**

Weakest → strongest: **function** · **statement/line** · **branch/decision** (every true AND false outcome of each `if`) · **condition** (each part of `a && b` true and false) · **MC/DC** (each condition independently changes the outcome; **required in avionics, DO-178C**) · **path** (every route; strongest, often impossible). **Coverage ≠ security.**

*Hook: statement = visited every room; branch = opened every door both ways; path = walked every possible route through the house.*

**On the exam**

- Valid-looking PNGs from the spec → **generation** · random bit flips in samples → **mutation**
- Robot test purchase every 5 minutes in prod → **synthetic transactions**
- Kill DB/authz connection to check the app denies access → **fault injection** (verifies fail secure)
- User count where it collapses → **break** · expected peak → **load** · hours-long run finds memory leak → **soak**
- Randomly terminating prod servers → **chaos engineering**
- Validates crypto modules vs FIPS 140-3 → **CMVP** · FIPS level adding tamper-resistance → **Level 3**
- Developer tests one function in isolation → **unit** · every true/false outcome → **branch** · every route → **path**
- **Traps:** mutation easy but shallow vs generation more setup but deeper; chaos ≠ fault injection; coverage ≠ secure.

**Quick check + your answers**

1. Fuzzer knows the PNG format, plants errors deep inside → **generation-based** ✅; drawback not given → **more setup (must build the model)**.

2. Robot account purchase every 5 minutes in prod with alerts → **synthetic transactions** ✅

3. Cut the authorization service to check the app denies access → you said "fail secure" (the principle); the TESTING TYPE = **fault injection**.

**Quick check:** (1) Fuzzer knows PNG structure, plants deep errors: type + drawback? (2) Robot purchase every 5 min in prod with alerts: name? (3) Cut authz service to check app denies access: what testing?

**Answer:** Generation; synthetic transactions. Correct.

</details>

<a name="t-6-2-18"></a>
**Regression testing**

Confirms changes didn't break existing features or reintroduce old bugs.

> On the exam: What it is: re-running existing tests after changes to confirm nothing broke and old bugs didn't return.
Security angle: add a test for every fixed vulnerability, so it can't silently come back.
Scenario cue: 'a fixed SQL injection reappeared in a later release' → missing regression test.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-19"></a>
**Integration testing**

Tests how components work together; interfaces are a common weak spot.

> On the exam: What it is: testing how components work together through their interfaces.
Security angle: catches wrong assumptions between components (each thinks the other validates input or checks authorization).
Scenario cue: 'each module passed unit tests but data passes between them unvalidated' → integration testing finds it.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-20"></a>
**Continuous testing**

Automated tests in the CI/CD pipeline on every change.

> On the exam: What it is: automated tests (unit, SAST, SCA, DAST) running on every change in the CI/CD pipeline.
Why: fast feedback to developers and automatic enforcement of break/build criteria.
Scenario cue: 'find security issues within minutes of a commit' → continuous testing in the pipeline.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-21"></a>
**Misuse and abuse test cases**

Tests derived from misuse cases written during requirements.

> On the exam: What it is: negative test cases built from the misuse and abuse cases written during requirements; they test that the system resists the attack.
Scenario cue: 'how do you verify the attack scenarios found in requirements were mitigated?' → misuse/abuse test cases, tracked in the traceability matrix.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-22"></a>
**Boundary value and equivalence testing** (review)

Test at the edges of input ranges and one value per input class.

> On the exam: Boundary value: test at and just outside limits (0, 1, max, max+1). Equivalence partitioning: divide inputs into groups that behave the same and test one from each.
Scenario cue: 'a field accepts 1-100; which values to test?' → 0, 1, 100, 101 plus one valid and one invalid group value.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** I named the technique, not the values (17, 18, 65, 66). Shaky.

</details>

<a name="t-6-2-23"></a>
**Penetration testing in detail**

Authorized simulated attack to find and exploit weaknesses and prove impact. Types: external, internal, application, network, social engineering; black, gray or white box.

> On the exam: Key points: written authorization and rules of engagement first; testers report, they don't fix; retest after fixes.
Trap: a pentest is a snapshot in time; it doesn't replace secure development.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-24"></a>
**Scanning types**

Network/port scanning (find hosts and open ports), fingerprinting (identify OS and versions; active sends probes, passive watches traffic), banner grabbing (read version info services reveal), vulnerability scanning (match versions and configs to known flaws), content scanning (find sensitive data or malware in content), privacy scanning (find exposed personal data).

> On the exam: Defense against fingerprinting: remove or change version banners. Scenario cue: 'server headers reveal exact versions' → banner grabbing risk.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-25"></a>
**Security testing tool categories**

Reconnaissance tools, port scanners, sniffers/protocol analyzers, vulnerability scanners, web proxies and DAST scanners, exploitation frameworks, password crackers, fuzzers, static analyzers, debuggers, disassemblers and decompilers, wireless tools.

> On the exam: Scenario cue: 'inspect traffic for cleartext credentials' → sniffer/protocol analyzer.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-26"></a>
**Testing specific controls**

Input validation (malformed and boundary input), injection (special characters), scripting/XSS (script payloads), nonrepudiation (are actions logged and attributable?), spoofing (can identities be faked?), error handling (does it fail securely without leaking?), privilege escalation (horizontal: other users' data; vertical: admin functions).

> On the exam: Scenario cue: 'a normal user can open admin pages' → vertical privilege escalation. 'Can see another customer's orders' → horizontal.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

<a name="t-6-2-27"></a>
**Red, blue and purple teams**

Red team: simulates real attackers with broad goals. Blue team: defends and detects. Purple team: both working together to improve detection.

> On the exam: Don't confuse: a pentest finds as many vulnerabilities as possible in a scope; a red team tests whether defenders detect and respond to a realistic attack.

<details><summary>Lesson (17 Nov 2026)</summary>

**6.2 Batch 5: Test levels, techniques, pen testing and teams (topics 18–27), the last of 6.2**

*Exam angle: the level of testing (unit → integration → regression → continuous), how to choose test inputs, and the pen testing vocabulary: types, scans, tools, teams.*

**18. Regression testing**

Re-run tests after **every change** (fix, feature, patch, config) → nothing else broke, old bugs not back. Automated; select by **impact analysis**. **Security regression tests:** for every fixed vulnerability, add a test reproducing the attack so it never silently returns.

**19. Integration testing**

How components **work together**; **interfaces** are weak spots (formats, service-to-service auth, error propagation, trust assumptions). Approaches: **big bang** (all at once, hard to locate failures) · **top-down** (top first, **stubs** below) · **bottom-up** (bottom first, **drivers** above) · **sandwich/hybrid**. Security: authn/authz between services, validation at every boundary, mTLS, contract tests.

**20. Continuous testing**

Automated tests in **CI/CD on every change** (unit, SAST, SCA, secret scanning, IaC scans, integration, DAST in staging). Fast feedback, shift left; **quality gates** fail the build past the **bug bar**. Needs reliable fast tests (flaky tests get ignored).

**21. Misuse and abuse test cases**

**Negative tests from the misuse/abuse cases** written during requirements (3.6): "attacker views another user's order", "bot submits 10,000 logins". Verify the system resists. Traceability: misuse case → security requirement → test case.

**22. Boundary value and equivalence testing**

- **Equivalence partitioning:** classes that should behave the same → **one value per class** (age 18–65: valid 40, too low 10, too high 80, non-numeric "abc").
- **Boundary value analysis:** test **at and around the edges** (bugs cluster there: off-by-one, overflows) → **17, 18, 19 and 64, 65, 66**, plus 0, empty, null, very long, max + 1.
- Use both.

*Hook: equivalence = one sample from each bucket; boundary = test the edges of each bucket.*

**23. Penetration testing in detail**

Authorized simulated attack to **exploit** weaknesses and **prove impact**. Types: **external** · **internal** (insider/compromised host) · **application** (web, mobile, API) · **network/infrastructure** · **wireless** · **physical** · **social engineering** (phishing, pretexting, tailgating). Black/gray/white box. **Double-blind** = defenders not told (tests detection/response). Typically **annually + after significant change**; report + **retest**.

**24. Scanning types**

**Network/port** (live hosts, open ports; Nmap; TCP connect vs **SYN half-open**, quieter) · **fingerprinting** (OS/versions: **active** probes vs **passive** traffic watching, stealthier) · **banner grabbing** (versions services announce → suppress banners) · **vulnerability scanning** (versions/configs vs known flaws; Nessus, OpenVAS; **credentialed** scans more accurate) · **content scanning** (sensitive data/malware in files) · **privacy scanning** (exposed personal data).

**25. Security testing tool categories**

Recon/OSINT: Maltego, Shodan · port scanners: **Nmap** · sniffers/protocol analyzers: **Wireshark**, tcpdump · vulnerability scanners: **Nessus**, OpenVAS · web proxies/DAST: **Burp Suite**, **OWASP ZAP** · exploitation: **Metasploit** · password crackers: **John the Ripper**, **Hashcat** (offline), **Hydra** (online) · fuzzers: AFL, libFuzzer · static analyzers: SonarQube, Semgrep · debuggers: gdb, WinDbg · disassemblers/decompilers: IDA Pro, **Ghidra** · wireless: Aircrack-ng.

**26. Testing specific controls**

Input validation (malformed, boundary) · injection (`'` `"` `;` `--`) · scripting/XSS (payloads) · **nonrepudiation** (actions logged + attributable, tamper-proof logs) · **spoofing** (fake headers, tokens, senders) · error handling (fail secure, no leaks) · **privilege escalation:** **horizontal** = another user's data at the same level (IDOR) · **vertical** = higher privileges (user → admin).

*Hook: horizontal = sideways into your neighbor's apartment; vertical = upstairs into the penthouse.*

**27. Red, blue and purple teams**

**Red** = real adversary simulation, one broad goal ("get into the CEO's email"), **stealthy**, weeks, technical + social + physical; tests **detection and response** · **Blue** = defenders (SOC, detection, response, hardening) · **Purple** = red + blue **collaborating** in real time to improve detection · **White** = referees. **Red team ≠ pen test:** pen test = as many vulns as possible in scope; red team = one objective, stealthily, people + process + tech.

*Hook: red attacks, blue defends, purple mixes, white referees.*

**On the exam**

- Test reproducing a fixed SQLi on every build → **security regression testing** · top-down with stubs → **top-down integration**
- 18–65: test 17, 18, 65, 66 → **boundary value analysis** · one per class → **equivalence partitioning**
- Tests from requirement-phase misuse cases → **misuse/abuse test cases** · defenders not told → **double-blind**
- OS identified by watching traffic → **passive fingerprinting** · "Apache 2.4.49" announced → **banner grabbing** → suppress · scan that logs in → **credentialed**
- Wireshark → sniffer · Metasploit → exploitation · Ghidra → decompiler
- Changed ID → other customer's statements → **horizontal** · gets admin functions → **vertical**
- Weeks-long stealthy goal-driven attack → **red team** · live collaboration → **purple team**
- **Traps:** red team ≠ pen test; horizontal vs vertical; passive fingerprinting sends nothing.

**Quick check + your answers**

1. Changed account ID in the URL, sees another customer's statements → **horizontal** ✅

2. Age 18–65, boundary values → you named the technique but not the values → **17, 18, 65, 66** (+ 19, 64).

3. Test reproducing the fixed SQLi, run on every build → **security regression testing** ✅

**Quick check:** (1) Changed account ID → another customer's statements: horizontal or vertical? (2) Age 18–65: which boundary values? (3) Test reproducing a fixed SQLi on every build: name?

**Answer:** Horizontal; security regression testing. Correct.

</details>

## 6.3 Verify and validate documentation

<a name="t-6-3-1"></a>
**Installation and setup guides**

Should describe secure defaults and hardening steps.

> On the exam: What to check: the guide sets up secure defaults, includes hardening steps, doesn't tell users to disable security (firewalls, antivirus) or use default passwords.
Scenario cue: 'install guide says run the service as administrator for convenience' → documentation finding.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-3-2"></a>
**Error messages**

Must not leak sensitive details (stack traces, SQL, paths).

> On the exam: What to check: messages help users fix the problem but reveal nothing internal (stack traces, SQL, file paths, versions). Login errors shouldn't say whether the username or the password was wrong.
Scenario cue: 'error says "user not found"' → allows username enumeration.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-3-3"></a>
**User guides and release notes**

Accurate, include security guidance and known issues.

> On the exam: What to check: accurate, include security guidance (how to use security features safely), release notes describe security fixes and known issues responsibly.
Why: wrong documentation leads users to insecure configurations.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

## 6.4 Undocumented functionality

<a name="t-6-4-1"></a>
**Undocumented features** (review)

Backdoors, debug code, hidden admin functions, maintenance hooks, Easter eggs.

> On the exam: Debug code and maintenance hooks left in production are classic backdoors; remove them before release.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Unsure on maintenance hook (thought vulnerable account); detection methods not given. Shaky.

</details>

<a name="t-6-4-2"></a>
**Finding them** (review)

Code review, binary analysis, comparing behavior to the requirements matrix.

> On the exam: Methods: code review, comparing behavior to the traceability matrix, binary analysis, monitoring for unexpected network connections or open ports, reviewing hidden parameters.
Scenario cue: 'how to discover hidden features not in any requirement?' → backward traceability plus code review.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Unsure on maintenance hook (thought vulnerable account); detection methods not given. Shaky.

</details>

## 6.5 Security implications of test results

<a name="t-6-5-1"></a>
**Prioritization**

Rank findings by severity and business impact.

> On the exam: How: severity of the flaw × how exposed it is × value of the affected asset × exploitability.
Scenario cue: 'medium flaw on an internet-facing payment page vs high flaw on an isolated internal tool' → the exposed payment flaw may come first.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-5-2"></a>
**Impact on product management**

Findings affect release dates, scope and risk acceptance.

> On the exam: What it means: security results affect schedule, cost and features. Security teams report risk; product owners and management make the release decision and accept residual risk.
Scenario cue: 'who decides to ship with a known high-risk flaw?' → the business owner, documented as risk acceptance.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-5-3"></a>
**Break/build criteria**

Apply the bug bar: does this finding block the release?

> On the exam: What it means: compare test results to the predefined bug bar. If findings exceed the bar (e.g., any critical or high), the build fails and the release stops.
Scenario cue: 'what objectively decides if the build can be released?' → break/build criteria agreed in advance.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-5-4"></a>
**False positives and false negatives**

Reported but not real vs real but missed (more dangerous).

> On the exam: False positive: tool reports a problem that isn't real (wastes time, erodes trust in tools). False negative: real problem missed (dangerous, false confidence).
Scenario cue: 'developers ignore scanner results' → too many false positives; tune the tool.
Trap: false negatives are the more dangerous of the two.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

## 6.6 Classify and track security errors

<a name="t-6-6-1"></a>
**Defect, error, vulnerability**

Error = human mistake; defect = resulting fault; vulnerability = exploitable weakness.

> On the exam: Error: a human mistake. Defect (bug/fault): the resulting problem in the code. Failure: when the defect causes wrong behavior at runtime. Vulnerability: a defect that can be exploited to break security.
Scenario cue: 'every vulnerability is a defect, but not every defect is a vulnerability'.

<details><summary>Lesson (17 Nov 2026)</summary>

**Batch 6: Documentation (6.3), hidden features (6.4), test results (6.5), terms (6.6.1) — 10 topics**

*Exam angle: testing goes beyond the code — documents must be secure, hidden features must be found, and results must be prioritized and turned into release decisions.*

**1. Installation and setup guides (6.3.1)**

Describe **secure installation + secure defaults** and **hardening** (change default passwords, disable unneeded services, file permissions, TLS, logging, **least-privileged** service accounts); how to **verify the installer** (hash/signature). Testers check following the guide produces a secure system. Watch for insecure examples (`debug=true`, `chmod 777`, "disable certificate validation") that get copy-pasted into production.

**2. Error messages (6.3.2)**

Users see **generic messages** (+ reference ID); never stack traces, SQL, paths, versions, internal IPs. **Login errors identical** for wrong username or password ("Invalid username or password") → prevents **account enumeration**. Details to server-side logs; documented error codes for support.

**3. User guides and release notes (6.3.3)**

Accurate, with **security guidance** (enable MFA, configure roles). Release notes list **security fixes** (CVE IDs) + **known issues/workarounds**, but no exploitable details before users can patch.

**4. Undocumented features (6.4.1)**

Not in requirements/docs: **backdoors** · **debug code/endpoints** in prod · **hidden admin functions** · **maintenance hooks** (developer shortcuts that **bypass security** "for maintenance") · Easter eggs · test accounts · hard-coded credentials. Bypass controls, unreviewed code; often accidental, sometimes malicious.

*Hook: a maintenance hook is a secret staff entrance someone forgot to brick up.*

**5. Finding them (6.4.2)**

Code review (every diff) · binary analysis / reverse engineering · **backward traceability** (code with no requirement = suspicious) · **attack surface validation**, crawling, fuzzing for hidden endpoints · traffic analysis (unexpected outbound connections) · string searches (hard-coded passwords) · remove before release; **build flags** keep debug code out.

**6. Prioritization (6.5.1)**

Rank by **severity (CVSS)**, **exploitability**, **business impact/asset value**, **exposure** (internet-facing first). Risk-based, not counts. Group by **root cause**.

**7. Impact on product management (6.5.2)**

Findings can delay releases, cut features, need resources. **Product/business owners decide trade-offs** incl. **risk acceptance** (not testers). Communicate early; track **security debt** in the backlog.

**8. Break/build criteria (6.5.3)**

**Bug bar as a quality gate** ("any unresolved critical/high fails the build / blocks release"); defined **in advance** (requirements), objective, **automated in CI**; exceptions only via formal risk acceptance.

**9. False positives and false negatives (6.5.4)**

**False positive** = reported, not real (wasted time, **alert fatigue**, distrust). **False negative** = real, missed (**more dangerous**, false sense of security). Tuning trades them off; reduce FPs with triage/accurate tools (IAST); reduce FNs by **combining techniques** (SAST + DAST + manual review).

*Hook: false positive = a false alarm; false negative = a silent burglar.*

**10. Error, defect, vulnerability (6.6.1)**

**Error** = human mistake → **defect** (fault/bug) = flaw in the product → **failure** = defect runs, visible misbehavior → **vulnerability** = exploitable defect. Not every defect is a vulnerability.

*Hook: error (the person) → defect (the product) → failure (what you see) → vulnerability (what an attacker can use).*

**On the exam**

- Install guide says disable cert validation → insecure documentation · "username not found" → **account enumeration** → identical generic message
- Hidden URL lets support log in as anyone → **maintenance hook / backdoor** · code with no requirement → found via **backward traceability**
- What to fix first → highest **risk** · who ships with a known high → **business/product owner**
- Build fails on any unresolved critical → **break/build criteria**
- 150 non-issues → **false positives** · missed real SQLi → **false negative** (more dangerous)
- Misread requirement → **error** · resulting bug → **defect** · exploitable → **vulnerability**
- **Traps:** FN worse than FP; testers don't accept risk; not every defect is a vulnerability.

**Quick check + your answers**

1. "Username not found" vs "Wrong password" → **account enumeration** → identical generic message ✅

2. 150 fake issues → **false positives**; missed real SQLi → **false negative** (more dangerous) ✅

3. Hidden "maintenance" URL to log in as any user → you weren't sure ("vulnerable account?") → **maintenance hook (backdoor)**; found by code review, backward traceability, attack surface validation.

**Quick check:** (1) 'Username not found' vs 'Wrong password': problem + fix? (2) 150 fake issues vs missed real SQLi: names + more dangerous? (3) Hidden maintenance URL to log in as anyone: name + one way testing finds it?

**Answer:** Account enumeration + generic message; FP/FN, FN more dangerous. Correct.

</details>

<a name="t-6-6-2"></a>
**Bug vs flaw**

Bug = implementation problem; flaw = design problem (harder to fix).

> On the exam: Bug: implementation problem in code (buffer overflow), often found by tools. Flaw: design problem (no authentication between services), found by threat modeling and design review, and expensive to fix.
Scenario cue: 'which issue type requires architecture changes?' → flaw.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-6-3"></a>
**Severity vs priority**

Severity = how bad technically; priority = how soon to fix.

> On the exam: Severity: technical impact if exploited (set by security/QA). Priority: order of fixing based on business needs (set by product/management).
Scenario cue: 'a critical bug in a feature no one uses, scheduled for next quarter' → high severity, low priority.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-6-4"></a>
**Bug tracking**

Track every finding to closure with owner and status.

> On the exam: What it is: logging every finding in a central system with severity, owner, status and due date, tracked until it's fixed and verified.
Why: nothing is forgotten, supports metrics (time to fix) and audits.
Trap: security bugs may need restricted visibility so details don't leak.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-6-5"></a>
**Risk scoring with CVSS**

Consistent severity scores for prioritization.

> On the exam: What it is: scoring findings with CVSS so severity is consistent. Base score = built-in severity; environmental metrics adjust for your system (exposure, data sensitivity, controls).
Scenario cue: 'same CVE, but the system is internal only and isolated' → environmental score lowers it.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-6-6"></a>
**Defect report contents**

Defect ID, title, description, steps to reproduce, expected vs actual results, environment and build number, screenshots or logs, severity, priority, reporter and assignee, status.

> On the exam: Security: restrict access to security defect details; include reproduction steps so fixes can be verified.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-6-7"></a>
**Impact assessment and corrective action**

For each defect, assess impact and decide the action: fix now, defer to a later release (with risk acceptance), add compensating controls, or accept.

> On the exam: Scenario cue: 'a high-risk defect can't be fixed before release' → document risk acceptance and add compensating controls.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

## 6.7 Secure test data

<a name="t-6-7-1"></a>
**Synthetic test data**

Generated data that keeps referential integrity, statistical quality, and looks like production.

> On the exam: What it is: realistic fake data generated for testing. Must keep referential integrity (linked records match), statistical quality (realistic distributions) and look like production.
Scenario cue: 'testers need realistic data without privacy risk' → synthetic data is best.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-7-2"></a>
**Reusing production data**

Risky; must be sanitized first. Non-production environments are usually less protected.

> On the exam: Risk: test environments usually have weaker security and more people with access, so real data there is easily exposed.
Rule: avoid it; if you must, sanitize/mask before it leaves production and protect it as production data.
Scenario cue: 'production customer data copied to test as-is' → a data breach waiting to happen.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-7-3"></a>
**Data masking**

Static (permanent copy) vs dynamic (masked at query time).

> On the exam: Static masking: permanently replaces sensitive values in a copy (for test environments). Dynamic masking: hides values on the fly for users without rights, while the real data stays unchanged (for live systems).
Scenario cue: 'support agents should see only the last 4 card digits' → dynamic masking.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-7-4"></a>
**Sanitization, anonymization, tokenization**

Remove or replace sensitive values before testing.

> On the exam: Sanitization: removing or replacing sensitive data. Anonymization: irreversibly removing identity. Tokenization: replacing values with tokens that keep the format and relationships, so tests still work.
Scenario cue: 'test data must keep valid-looking card numbers and links between tables' → tokenization or format-preserving masking.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 7: Tracking defects (6.6.2–7) + secure test data (6.7.1–4) — 10 topics**

*Exam angle: classifying findings correctly (bug vs flaw, severity vs priority), tracking them to closure, and testing without exposing real people's data.*

**1. Bug vs flaw (6.6.2)**

**Bug** = implementation/coding mistake (missing output encoding on one page), local cheaper fix, found by SAST/code review. **Flaw** = design problem (no authorization layer, trusting client prices), harder/costlier (re-architecture), found by threat modeling, design review, manual testing.

*Hook: bug = a mistake while building; flaw = a mistake in the blueprint.*

**2. Severity vs priority (6.6.3)**

**Severity** = how bad technically (testers/security, CVSS). **Priority** = how soon to fix (product/business owner, context). Can differ: **high severity, low priority** (critical crash in an unreleased/unused feature) · **low severity, high priority** (company name misspelled on the homepage the day before launch).

*Hook: severity = how bad; priority = how soon.*

**3. Bug tracking (6.6.4)**

Central tracker; every finding to closure with **owner + status**: new → triaged → assigned → in progress → fixed → **verified (retested)** → closed; or deferred/won't fix **only with risk acceptance**; reopened if the fix fails. **Restrict access to security bugs** (attacker's roadmap). Link to requirements/commits; metrics (time to fix, open by severity, SLA breaches). Never close without verification.

**4. Risk scoring with CVSS (6.6.5)**

Consistent 0–10 severity (base, temporal/threat, environmental; Low/Med/High/Critical). Environmental metrics = your context. **CVSS = severity, not full risk** → combine with exploit likelihood (CISA **KEV**, **EPSS**) and asset criticality.

**5. Defect report contents (6.6.6)**

Reproducible: **ID, title, description, steps to reproduce, expected vs actual, environment + build number**, affected versions/component, **evidence** (screenshots, logs), **severity, priority, reporter, assignee, status**. No real secrets/PII in reports; restricted visibility.

**6. Impact assessment and corrective action (6.6.7)**

Assess impact (C/I/A, users, data, exploitability) → **fix now** · **defer with documented risk acceptance** · **compensating controls** meanwhile · **formally accept**. Corrective action = fix + **root cause analysis** + verify + **prevent recurrence** (regression test, standards, training).

**7. Synthetic test data (6.7.1)**

Generated, not real; keeps **referential integrity**, **statistical quality**, production-like formats; no privacy risk; can include edge cases deliberately. **Preferred option.**

**8. Reusing production data (6.7.2)**

Risky: test/dev environments are **less protected** (more access, weaker controls, copies spread); privacy law (GDPR purpose limitation). If unavoidable: **sanitize first**, **data owner approval**, **smallest subset**, **protect the test env like production**, **delete afterwards**. Best alternative: **synthetic data**.

**9. Data masking (6.7.3)**

**Static (SDM)** = permanently masked **copy** for test/dev (real values not in the copy). **Dynamic (DDM)** = masked **on the fly** at query/display by role, real data intact — used in **production** (support sees `****1234`). Techniques: substitution, shuffling, nulling, character masking, date/number variance; keep realistic + consistent.

*Hook: static = a permanently blurred photocopy; dynamic = a live screen that blurs depending on who's looking.*

**10. Sanitization, anonymization and tokenization (6.7.4)**

**Sanitization** (remove/replace, general) · **anonymization** (irreversible; GDPR no longer applies) · **pseudonymization** (reversible with separate key) · **tokenization** (reversible only via the vault; **deterministic** tokens keep joins working). Prefer irreversible methods for test data.

**On the exam**

- No authorization layer → **flaw** · missing encoding on one page → **bug**
- Critical crash in unreleased feature → **high severity, low priority** · who sets priority → **product/business owner**
- Closed without retest → violates **verify before close** · steps/expected vs actual/build number → good **defect report**
- Defer a fix → only with **documented risk acceptance**
- Generated data keeping table relationships → **synthetic** (referential integrity)
- Support sees last 4 digits, DB keeps full value → **dynamic masking** · masked DB copy for testers → **static masking**
- **Traps:** severity ≠ priority; test environments are less protected; dynamic masking doesn't change stored data.

**Quick check + your answers**

1. Critical crash in unused admin report vs misspelled company name before launch → (a) **high severity, low priority**; (b) **low severity, high priority** ✅

2. Support sees last 4 digits in prod, DB keeps full value → **dynamic masking** ✅

3. Copy prod customer DB to test → right instinct (don't use real values) ✅; precise answer: **synthetic data** best; otherwise sanitized/**statically** masked smallest subset with owner approval (dynamic = production screens).

**Quick check:** (1) Critical crash in unused admin report vs misspelled company name before launch: severity vs priority? (2) Support sees last 4 digits in prod, DB keeps full: technique? (3) Copy prod customer DB to test: better option?

**Answer:** Severity/priority correct; dynamic masking; mask instead of real values (refined: synthetic best, static masking for copies).

</details>

<a name="t-6-7-5"></a>
**Data aggregation mitigation**

Masked fields combined together can still re-identify people.

> On the exam: What it means: masked fields combined can still identify people (ZIP + birth date + gender identifies most people).
Mitigation: generalize data (age range instead of birth date), remove unneeded fields, apply k-anonymity.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

## 6.8 Verification and validation testing

<a name="t-6-8-1"></a>
**Independent V&V (IV&V)**

Performed by a separate, independent team for objectivity.

> On the exam: Required for critical, high-assurance systems. Independence can be technical, managerial and financial.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-8-2"></a>
**Internal V&V**

Performed by the organization's own team.

> On the exam: What it is: verification and validation done by the organization's own staff (a separate QA team).
Pros: cheaper, knows the product. Cons: less objective than independent V&V.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-8-3"></a>
**Acceptance test**

Final check that the product meets requirements before sign-off.

> On the exam: What it is: final testing by the customer or business against acceptance criteria before formal sign-off and deployment.
Scenario cue: 'which test confirms the product is ready for the customer to accept?' → acceptance test.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-8-4"></a>
**Software acceptance completion criteria**

Before acceptance: functional and security requirements met, test results reviewed, open findings within the bug bar, documentation complete (install, admin, user guides, DRP and BCP), risk accepted and signed off.

> On the exam: Scenario cue: 'what confirms software is ready for formal acceptance?' → completion criteria are met.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-8-5"></a>
**Benefits of formal acceptance**

Confirms security requirements were met, gives management visibility of residual risk, creates accountability through sign-off, and stops insecure software going live.

> On the exam: Trap: acceptance is a management decision based on evidence, not just a test team's opinion.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-8-6"></a>
**Post-release verification and validation**

Independent assurance after release: FIPS 140 validation, Common Criteria evaluation, third-party testing.

> On the exam: Scenario cue: 'customers want independent proof the product's crypto meets federal standards' → FIPS 140 validation.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

## 6.AI AI additions in the current outline

<a name="t-6-ai-1"></a>
**Testing ML models**

Evaluate bias, drift, toxicity and adversarial evasion.

> On the exam: What to test: accuracy, bias (fair results across groups), drift (degrading over time), toxicity (harmful output), robustness to adversarial inputs, jailbreaks and prompt injection.
How: large evaluation datasets and red-teaming, measured statistically.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-ai-2"></a>
**Adversarial evasion**

Inputs crafted to fool a model into the wrong output.

> On the exam: What it is: inputs changed slightly (often invisibly to humans) so the model makes a wrong decision, e.g., stickers on a stop sign or modified malware evading an AI detector.
Defense: adversarial training, input preprocessing, ensemble models.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-ai-3"></a>
**AI-generated test scripts**

Using AI to generate edge-case security tests at scale.

> On the exam: What it is: using AI to generate edge-case and attack test cases quickly and at scale.
Trap: humans still review the tests and their coverage; AI may produce shallow or wrong tests.

<details><summary>Lesson (19 Nov 2026)</summary>

**Batch 8: Data aggregation (6.7.5), verification & validation (6.8), AI testing (6.AI.1–3) — 10 topics**

*Exam angle: the final gate before release (V&V and formal acceptance), and how testing changes for AI models.*

**1. Data aggregation mitigation (6.7.5)**

Masking fields separately isn't enough: **ZIP + birth date + gender** together re-identify most people. Mitigate: **generalize** (age ranges, partial ZIP) · **k-anonymity** (each record identical to ≥ k−1 others on combined fields) · **remove unneeded fields** · **add noise** (differential privacy) · control who can combine datasets. Ties to aggregation/inference (4.3).

**Verification vs validation**

**Verification = "built the product RIGHT?"** (meets the **spec**: reviews, inspections, tests vs spec). **Validation = "built the RIGHT product?"** (meets **users' real needs**: UAT, real use).

*Hook: verification checks against the blueprint; validation checks against what the customer actually wanted.*

**2. Independent V&V, IV&V (6.8.1)**

Separate independent team/org → **objectivity**, no conflict of interest. Independence: **technical** (own methods/tools) · **managerial** (doesn't report to dev managers) · **financial** (funding not dependent on devs). For high-assurance, safety-critical, government (NASA IV&V facility). More expensive.

**3. Internal V&V (6.8.2)**

Own team (QA, security). ✅ cheaper, faster, knows the system · ❌ less objective (bias, schedule pressure). Separate QA team = partial independence.

**4. Acceptance test (6.8.3)**

Final check that functional + security requirements are met before **sign-off**; by/for the customer/business against **acceptance criteria agreed up front**; feeds the go/no-go decision.

**5. Software acceptance completion criteria (6.8.4)**

Requirements met (**traceability matrix**) · test results reviewed · open findings **within the bug bar** (no open criticals/highs unless risk-accepted) · documentation complete (install, admin, user guides, **DRP + BCP**) · **residual risk accepted and signed off** by the business owner / authorizing official.

**6. Benefits of formal acceptance (6.8.5)**

Confirms security requirements met · **management visibility of residual risk** · **accountability** via sign-off · stops insecure software going live · **contractual evidence** (supplier delivered; payment) · operations baseline.

*Hook: formal acceptance = the signature on the delivery note: "I checked it, I accept it, it's on me now."*

**7. Post-release V&V (6.8.6)**

**FIPS 140** validation (CMVP) · **Common Criteria** (**ISO/IEC 15408**, **EAL1–7**, Protection Profiles + Security Targets) · third-party testing, pen tests, certifications · **re-validate after changes** (patches can invalidate certification).

**8. Testing ML models (6.AI.1)**

Beyond accuracy: **bias/fairness** · **drift** (data/concept) · **toxicity** · **robustness** to adversarial inputs · hallucination rate · privacy leakage (memorization) · explainability. Test on a **holdout set** separate from training; **red-team** LLMs. Thresholds from requirements (3.AI), enforced by build-break criteria (2.AI).

**9. Adversarial evasion (6.AI.2)**

Tiny (often invisible) input changes fool an **already-trained** model at **inference/run time** (stickers → stop sign read as speed limit; malware tweaked past an ML detector). vs **poisoning** = corrupting the model during **training**. Defenses: **adversarial training**, input preprocessing, ensembles, robustness testing, monitoring.

*Hook: poisoning = sabotaging the textbook; evasion = tricking the student during the exam.*

**10. AI-generated test scripts (6.AI.3)**

AI generates edge cases, fuzz inputs, abuse cases, unit tests at scale. Risks: non-existent APIs, missed edge cases, false confidence, insecure test code, leaking code/data to the vendor. Controls: **human review**, approved tools, prove tests work — they must **fail on known bugs** (**mutation testing**).

**On the exam**

- Masked data still re-identifies via ZIP + DOB + gender → **aggregation** → generalize / k-anonymity / remove fields
- Separate org, doesn't report to dev → **IV&V** (managerial independence)
- Built what users need? → **validation** · matches spec? → **verification**
- Requirements met, bug bar, docs, risk signed off → **acceptance completion criteria** · benefit of sign-off → **accountability** + residual risk visibility
- Crypto module validated post-release → **FIPS 140 / CMVP** · EAL4 → **Common Criteria**
- Accuracy drops as behavior changes → **drift** · stickers fool a trained model → **evasion** (not poisoning)
- AI-written tests actually catch bugs? → **mutation testing** / human review
- **Traps:** verification ≠ validation; evasion ≠ poisoning; AI tests need proof they work.

**Quick check + your answers**

1. ZIP + birth date + gender re-identify patients → **aggregation**; generalize / k-anonymity / remove fields ✅

2. Validation vs verification → self-corrected: **verification = against the blueprint/spec, validation = against what the customer wanted** ✅

3. Stickers fool an already-trained model → **evasion** (run-time trickery, not poisoning) ✅

**Quick check:** (1) ZIP + birth date + gender re-identify masked patients: problem + mitigation? (2) Validation vs verification? (3) Stickers fool an already-trained model: poisoning or evasion?

**Answer:** Aggregation + generalize/k-anonymity; verification = blueprint, validation = customer need (self-corrected); evasion. Correct.

</details>

<a name="t-6-ai-4"></a>
**Agent scope testing** (review)

Verify AI agents can't run commands outside their allowed scope.

> On the exam: What to test: an agent refuses actions outside its permissions, even when instructed by a user or hidden text, and high-impact actions require human approval.
Scenario cue: 'a document tells the agent to email all files to an outside address' → test that the agent refuses.

<details><summary>Lesson (19 Nov 2026)</summary>

**Last batch of Domain 6: AI testing, part 2 (6.AI.4–6)**

**1. Agent scope testing (6.AI.4)**

Verify an AI agent **can't act outside its allowed scope** — negative testing for **excessive agency (OWASP LLM06)**: try **disallowed tools/APIs** · **prompt injection to escalate** (direct + via content it reads) · **boundary escapes** (paths outside its folder, shell commands in tool arguments) · **data boundaries** (other users' data) · **approval gates** really stop high-impact actions (payments, deletions) · rate/budget limits hold · **every action logged**. Often **AI red-teaming**.

*Hook: trying to talk the intern into using the master key, and making sure they refuse.*

**2. Token limit stress testing (6.AI.5)**

**Context window** = max tokens in + out. Test near/over the limit: **truncation** (huge input pushes the **system prompt / safety rules out** → guardrails vanish) · **fail securely** (no stack traces, no half-processed state) · **cost/DoS** (**unbounded consumption, OWASP LLM10**) · **cut-off outputs** (half a JSON object breaks parsers). Controls: **input size limits**, rate limits + **per-user quotas**, chunking, **max output length**, graceful errors.

**3. NIST AI RMF (6.AI.6)**

**AI 100-1 (Jan 2023)**, **voluntary**. Four functions: **Govern** (culture, policies, roles, accountability — **cross-cutting**) → **Map** (context; identify risks/impacts) → **Measure** (analyze, test, track with metrics: bias, robustness, accuracy) → **Manage** (prioritize + act: respond, monitor, improve). Trustworthy AI: valid + reliable · safe · secure + resilient · accountable + transparent · explainable + interpretable · privacy-enhanced · fair with harmful bias managed. **Generative AI Profile (AI 600-1, 2024)**.

*Hook: Govern, Map, Measure, Manage = "Go Make More Money."*

**On the exam**

- Trick an AI agent into refunds above its limit → **agent scope testing** (not unbounded consumption)
- Long input pushes safety instructions out → **token limit stress testing** → input size limits
- Huge prompts run up the bill → **unbounded consumption** → quotas, rate limits
- Policies + accountability across everything → **Govern** · context + risks → **Map** · test/track with metrics → **Measure** · act → **Manage**
- **Traps:** Govern is cross-cutting; the AI RMF is voluntary, not a law.

**Quick check + your answers**

1. Trick agent into refunds above limit → you said "unbounded consumption" → **agent scope testing** (unbounded consumption = cost/resources).

2. Long input pushes safety instructions out → **token limit stress testing** ✅; control not named → input size limits / quotas / chunking.

3. Four functions → you said Govern, Map, Manage → **Govern, Map, Measure, Manage** (Measure missing).

**Quick check:** (1) Trick AI support agent into refunds above its limit: testing type? (2) Long input pushes safety instructions out of context: test + control? (3) NIST AI RMF four functions in order?

**Answer:** I said unbounded consumption; answer agent scope testing. Shaky.

</details>

<a name="t-6-ai-5"></a>
**Token limit stress testing** (review)

Check behavior when inputs hit or exceed model limits.

> On the exam: What to test: behavior when inputs approach or exceed the model's token limit: system instructions shouldn't get dropped, cost and resource use shouldn't explode (DoS), and errors are handled safely.

<details><summary>Lesson (19 Nov 2026)</summary>

**Last batch of Domain 6: AI testing, part 2 (6.AI.4–6)**

**1. Agent scope testing (6.AI.4)**

Verify an AI agent **can't act outside its allowed scope** — negative testing for **excessive agency (OWASP LLM06)**: try **disallowed tools/APIs** · **prompt injection to escalate** (direct + via content it reads) · **boundary escapes** (paths outside its folder, shell commands in tool arguments) · **data boundaries** (other users' data) · **approval gates** really stop high-impact actions (payments, deletions) · rate/budget limits hold · **every action logged**. Often **AI red-teaming**.

*Hook: trying to talk the intern into using the master key, and making sure they refuse.*

**2. Token limit stress testing (6.AI.5)**

**Context window** = max tokens in + out. Test near/over the limit: **truncation** (huge input pushes the **system prompt / safety rules out** → guardrails vanish) · **fail securely** (no stack traces, no half-processed state) · **cost/DoS** (**unbounded consumption, OWASP LLM10**) · **cut-off outputs** (half a JSON object breaks parsers). Controls: **input size limits**, rate limits + **per-user quotas**, chunking, **max output length**, graceful errors.

**3. NIST AI RMF (6.AI.6)**

**AI 100-1 (Jan 2023)**, **voluntary**. Four functions: **Govern** (culture, policies, roles, accountability — **cross-cutting**) → **Map** (context; identify risks/impacts) → **Measure** (analyze, test, track with metrics: bias, robustness, accuracy) → **Manage** (prioritize + act: respond, monitor, improve). Trustworthy AI: valid + reliable · safe · secure + resilient · accountable + transparent · explainable + interpretable · privacy-enhanced · fair with harmful bias managed. **Generative AI Profile (AI 600-1, 2024)**.

*Hook: Govern, Map, Measure, Manage = "Go Make More Money."*

**On the exam**

- Trick an AI agent into refunds above its limit → **agent scope testing** (not unbounded consumption)
- Long input pushes safety instructions out → **token limit stress testing** → input size limits
- Huge prompts run up the bill → **unbounded consumption** → quotas, rate limits
- Policies + accountability across everything → **Govern** · context + risks → **Map** · test/track with metrics → **Measure** · act → **Manage**
- **Traps:** Govern is cross-cutting; the AI RMF is voluntary, not a law.

**Quick check + your answers**

1. Trick agent into refunds above limit → you said "unbounded consumption" → **agent scope testing** (unbounded consumption = cost/resources).

2. Long input pushes safety instructions out → **token limit stress testing** ✅; control not named → input size limits / quotas / chunking.

3. Four functions → you said Govern, Map, Manage → **Govern, Map, Measure, Manage** (Measure missing).

**Quick check:** (1) Trick AI support agent into refunds above its limit: testing type? (2) Long input pushes safety instructions out of context: test + control? (3) NIST AI RMF four functions in order?

**Answer:** I named correctly; control not given. Shaky.

</details>

<a name="t-6-ai-6"></a>
**NIST AI RMF** (review)

AI Risk Management Framework: Govern, Map, Measure, Manage.

> On the exam: What it is: NIST's voluntary AI Risk Management Framework. Four functions: Govern (culture, policies, accountability, across everything), Map (context and risks), Measure (assess and track), Manage (prioritize and respond).
Scenario cue: 'which NIST framework guides AI risk management?' → AI RMF.

<details><summary>Lesson (19 Nov 2026)</summary>

**Last batch of Domain 6: AI testing, part 2 (6.AI.4–6)**

**1. Agent scope testing (6.AI.4)**

Verify an AI agent **can't act outside its allowed scope** — negative testing for **excessive agency (OWASP LLM06)**: try **disallowed tools/APIs** · **prompt injection to escalate** (direct + via content it reads) · **boundary escapes** (paths outside its folder, shell commands in tool arguments) · **data boundaries** (other users' data) · **approval gates** really stop high-impact actions (payments, deletions) · rate/budget limits hold · **every action logged**. Often **AI red-teaming**.

*Hook: trying to talk the intern into using the master key, and making sure they refuse.*

**2. Token limit stress testing (6.AI.5)**

**Context window** = max tokens in + out. Test near/over the limit: **truncation** (huge input pushes the **system prompt / safety rules out** → guardrails vanish) · **fail securely** (no stack traces, no half-processed state) · **cost/DoS** (**unbounded consumption, OWASP LLM10**) · **cut-off outputs** (half a JSON object breaks parsers). Controls: **input size limits**, rate limits + **per-user quotas**, chunking, **max output length**, graceful errors.

**3. NIST AI RMF (6.AI.6)**

**AI 100-1 (Jan 2023)**, **voluntary**. Four functions: **Govern** (culture, policies, roles, accountability — **cross-cutting**) → **Map** (context; identify risks/impacts) → **Measure** (analyze, test, track with metrics: bias, robustness, accuracy) → **Manage** (prioritize + act: respond, monitor, improve). Trustworthy AI: valid + reliable · safe · secure + resilient · accountable + transparent · explainable + interpretable · privacy-enhanced · fair with harmful bias managed. **Generative AI Profile (AI 600-1, 2024)**.

*Hook: Govern, Map, Measure, Manage = "Go Make More Money."*

**On the exam**

- Trick an AI agent into refunds above its limit → **agent scope testing** (not unbounded consumption)
- Long input pushes safety instructions out → **token limit stress testing** → input size limits
- Huge prompts run up the bill → **unbounded consumption** → quotas, rate limits
- Policies + accountability across everything → **Govern** · context + risks → **Map** · test/track with metrics → **Measure** · act → **Manage**
- **Traps:** Govern is cross-cutting; the AI RMF is voluntary, not a law.

**Quick check + your answers**

1. Trick agent into refunds above limit → you said "unbounded consumption" → **agent scope testing** (unbounded consumption = cost/resources).

2. Long input pushes safety instructions out → **token limit stress testing** ✅; control not named → input size limits / quotas / chunking.

3. Four functions → you said Govern, Map, Manage → **Govern, Map, Measure, Manage** (Measure missing).

**Quick check:** (1) Trick AI support agent into refunds above its limit: testing type? (2) Long input pushes safety instructions out of context: test + control? (3) NIST AI RMF four functions in order?

**Answer:** Govern, Map, Manage — missed Measure. Shaky.

</details>
