# Domain 3: Secure Software Requirements

Exam weight: 13%

## 3.1 Software security requirements

<a name="t-3-1-1"></a>
**Functional requirements**

What the system must do: business requirements, use cases, user stories.

> On the exam: What it is: what the system must do. Security functional requirements describe security features: login with MFA, role-based menus, audit logging of admin actions.
Scenario cue: 'the system shall lock the account after 5 failed attempts' → functional security requirement.
Don't confuse: functional = a behavior; non-functional = a quality like performance or availability.

<details><summary>Lesson (16 Oct 2026)</summary>

**Functional requirements**

- Functional requirement = WHAT the system must DO (features, behaviors).
- Requirement = written statement of what software must do or be; design/code/tests trace back (RTM).

**Sources/forms**

- business requirements
- USE CASES (actor interacts step by step to reach a goal)
- USER STORIES (As a [role], I want [feature], so that [benefit]).

**Security functional requirements = security FEATURES the system performs**

- lock after 5 failed logins, MFA, admins view audit logs, encrypt card numbers.

**On the exam**

- reset password via email = functional
- As a..I want..so that = user story
- actor interacts to reach goal = use case.

**Trap**

- security requirements CAN be functional if they describe a feature performed.

**Test**

- remove it
- does a FEATURE disappear? Yes = functional.

**Hook**

- functional = what it DOES
- if you can watch it happen, it is functional.

**Quick check:** (1) log every failed admin login with timestamp + IP (2) login page loads under 2 seconds: which is functional?

**Answer:** User said both; reasoning for #1 correct. #2 is NON-FUNCTIONAL (performance, how well). Remove-it test.

</details>

<a name="t-3-1-2"></a>
**Non-functional requirements**

How well it must do it: security, performance, operational, continuity, deployment.

> On the exam: Often forgotten. Must be measurable, e.g., '99.9% availability' or 'lock account after 5 failed attempts'.

<details><summary>Lesson (16 Oct 2026)</summary>

**Non-functional requirements**

- Non-functional = HOW WELL the system does things; quality attributes, the -ilities (reliability, availability, scalability, maintainability, usability).

**Categories**

- SECURITY (CIA qualities: salted slow hash, TLS 1.2+)
- PERFORMANCE (speed, response, capacity)
- OPERATIONAL (logging, monitoring, backups, patching, log retention)
- CONTINUITY (RTO, RPO)
- DEPLOYMENT (cloud/on-prem, platforms, environment).

**Why security cares**

- key properties are non-functional
- easy to forget
- must be specific + testable ("must be secure" useless; "data at rest AES-256" testable).

**Pairs**

- MFA login = functional
- resist 1,000 guesses/sec = non-functional
- must back up = functional
- data loss max 15 min = non-functional.

**On the exam**

- response time = performance
- 99.9% availability = availability/continuity
- logs kept 1 yr = operational.

**Traps**

- security FEATURES are functional, security QUALITIES non-functional
- vague words (secure, fast, user-friendly) = bad requirement.

**Hook**

- functional = what it does
- non-functional = how well.

**Quick check:** Email alert on admin creation / 99.95% availability / API within 500 ms under peak: label.

**Answer:** Functional, non-functional, non-functional. Correct.

</details>

<a name="t-3-1-3"></a>
**Security user stories and acceptance criteria**

"As a user I want my session to expire after 15 minutes idle" with testable criteria.

> On the exam: Format: 'As a [role], I want [feature] so that [benefit]', plus acceptance criteria that can be tested.
Why it matters: in Agile, security only gets built if it's in the backlog. Testable acceptance criteria let QA verify it.
Trap: 'the app must be secure' is not testable and is a bad requirement.

<details><summary>Lesson (16 Oct 2026)</summary>

**Security user stories and acceptance criteria**

- Agile way to write security requirements: USER STORY + ACCEPTANCE CRITERIA (specific, testable pass/fail conditions for done).
- Story: As a [role], I want [x], so that [benefit]. e.g. bank customer, session expires after 15 min idle, so nobody uses an unlocked computer.

**Criteria often GIVEN / WHEN / THEN (BDD)**

- logged in + 15 min idle -> session ends
- expired + Back button -> no data
- old token reused -> rejected.

**Why**

- removes ambiguity
- testable
- links to Definition of Done
- test cases + RTM.
- EVIL USER STORY / ABUSER STORY = attacker view (As an attacker I want to guess passwords so I can take over accounts) -> write blocking stories (lockout, rate limit); links to misuse cases (3.6).
- Good criteria: specific numbers, testable, include NEGATIVE cases.

**On the exam**

- security reqs in Agile = security user stories + acceptance criteria
- testable done conditions = acceptance criteria
- attacker perspective = evil/abuser story.

**Trap**

- story without criteria is not testable.

**Habit**

- could a tester check this with yes/no?

**Hook**

- story = what and why
- acceptance criteria = how we will know it is done.

**Quick check:** As an admin I want strong password rules so accounts are secure: missing? one criterion?

**Answer:** Missing acceptance criteria: correct. Criterion (no personal/guessable info) right idea, not testable. Better: reject &lt;12 chars; reject breached-list passwords; reject containing username/email (NIST 800-63).

</details>

<a name="t-3-1-4"></a>
**Policy decomposition**

Breaking high-level policies into specific, testable requirements.

> On the exam: Example: policy 'protect customer data' becomes 'encrypt PII at rest with AES-256, mask card numbers in the UI, log all access'.

<details><summary>Lesson (16 Oct 2026)</summary>

**Policy decomposition**

- Breaking a HIGH-LEVEL POLICY into SPECIFIC, TESTABLE software requirements (management intent -> what the code must do).

**Level 1 policy**

- customer data protected from unauthorized disclosure. Level 2 objectives (CIA areas): confidentiality at rest, in transit, authorized-only access, traceable access. Level 3 requirements: AES-256 at rest
- TLS 1.2+
- MFA before viewing
- region-limited access
- log every access with user ID, time, record ID.

**Picture**

- tree
- policy = trunk, objectives = branches, requirements = leaves
- each traces back.
- Also for regulations (GDPR appropriate measures) and standards/contracts (PCI).

**Why**

- traceability + compliance evidence (RTM)
- nothing forgotten.

**On the exam**

- high-level policy -> specific requirements = policy decomposition.

**Trap**

- stopping at objective level is not enough
- must be specific + testable.

**Exam habit**

- correct option is usually the MOST SPECIFIC, testable one.

**Hook**

- policy = trunk, requirements = leaves
- break down until a tester can check it.

**Quick check:** Decompose "Only authorized employees may access payroll data" into two testable requirements.

**Answer:** Process correct (objectives -> testable, incl. logging). Stayed general. Examples: Payroll role only, others access denied; log user ID/timestamp/record/old+new values; MFA for payroll.

</details>

<a name="t-3-1-5"></a>
**Subject-object matrix**

Table of which roles (subjects) can do which actions on which data (objects).

> On the exam: What it is: a matrix with roles (subjects) on one axis and data or functions (objects) on the other, showing allowed actions (create, read, update, delete).
Why it matters: creates clear authorization requirements and reveals over-privileged roles.
Scenario cue: 'how do you derive access control requirements for each role?' → subject-object matrix.

<details><summary>Lesson (16 Oct 2026)</summary>

**Subject-object matrix**

- Table of which ROLES (SUBJECTS) can do which ACTIONS on which DATA/RESOURCES (OBJECTS): documents access control requirements.
- Subject = active requester (user, role, process, service). Object = passive resource (file, table, API, record). Actions = CRUD (create, read, update, delete).

**Example HR**

- employee R own
- manager R team salary (no update)
- HR admin CRUD
- auditor R incl. audit logs. Empty cell = no access (default deny).

**Why**

- finds gaps early
- shows least privilege + separation of duties
- each cell = testable requirement + test case incl. NEGATIVE tests
- feeds RBAC design.
- Built in requirements, often with policy decomposition and data owners.

**On the exam**

- roles x actions x resources table = subject-object (access control) matrix
- check least privilege in requirements.

**Trap**

- subjects act, objects are acted upon
- a file is never the subject.

**Hook**

- subject = who does it
- object = what it is done to.

**Quick check:** Manager tries to update team salary: what happens, how does matrix help testers?

**Answer:** Denied; matrix shows can/cannot. Correct. Added: every cell = test case incl. negative tests.

</details>

<a name="t-3-1-6"></a>
**Requirements elicitation**

Brainstorming, interviews, surveys, data classification, use and misuse cases.

> On the exam: Methods: interviews, workshops, brainstorming, surveys, policy decomposition, data classification, subject-object matrix, use and misuse cases, reviewing laws and contracts.
Scenario cue: 'how do you capture security requirements early?' → involve stakeholders (business, legal, privacy, security) during requirements gathering.

<details><summary>Lesson (16 Oct 2026)</summary>

**Requirements elicitation**

- Elicitation = DRAWING OUT requirements from stakeholders (business, users, legal, security, ops).
- BRAINSTORMING: fast, creative; unstructured, shallow/incomplete, loud voices, must be vetted.
- INTERVIEWS: deep, follow-ups; time-consuming, one view may be biased.
- SURVEYS/QUESTIONNAIRES: reach MANY quickly, comparable; LIMITED DEPTH, only what you asked.
- DATA CLASSIFICATION: sensitivity drives requirement strength.
- USE + MISUSE CASES: misuse = attacker abuse; one of the best for security requirements.
- Also policy decomposition, subject-object matrix, document/regulation review, prototypes, JAD workshops.

**Why security effort**

- stakeholders describe features, not threats
- ask about threats, sensitivity, compliance, abuse.

**On the exam**

- gather security reqs = elicitation
- many stakeholders fast, little depth = surveys
- unstructured group = brainstorming
- attacker abuse = misuse cases.

**Trap**

- combine techniques.

**Hook**

- brainstorm wide, interview deep, survey many, think like an attacker.

**Quick check:** 300 employees in 20 countries in two weeks: technique and weakness?

**Answer:** Questionnaire/survey; limited depth. Correct.

</details>

<a name="t-3-1-7"></a>
**Continuity requirements**

RTO, RPO, maximum tolerable downtime.

> On the exam: Terms: MTD = how long the business can survive without it; RTO = target time to restore; RPO = acceptable data loss measured in time.
Why it matters: these become design requirements (redundancy, backup frequency, failover).
Scenario cue: 'the business can lose no more than 1 hour of transactions' → RPO of 1 hour, so back up or replicate at least hourly.

<details><summary>Lesson (16 Oct 2026)</summary>

**Continuity requirements**

- Non-functional continuity requirements from the BIA: how fast back, how much data loss acceptable.
- RPO (Recovery Point Objective) = max DATA loss measured in time, looking BACK from disaster; drives BACKUP FREQUENCY (RPO 1h = back up at least hourly; near zero = real-time replication).
- RTO (Recovery Time Objective) = target TIME TO RESTORE, looking FORWARD; drives recovery setup (short = hot standby).
- MTD (Maximum Tolerable Downtime; also MTPD, MAO) = absolute longest the business survives before serious damage. RTO &lt;= MTD.
- WRT (Work Recovery Time) = time after system back to verify/catch up; RTO + WRT &lt;= MTD.
- MTTR (mean time to recover) = AVERAGE measured in ops (2.9), NOT the MTD limit.
- Cost: shorter RTO/RPO = more expensive; set by business need.

**On the exam**

- max data loss = RPO = backup frequency
- target restore time = RTO
- longest survivable = MTD
- RTO > MTD = plan inadequate.

**Trap**

- RPO = data (back), RTO = time (forward).

**Hook**

- RPO = Point in the past
- RTO = Time to get back up
- MTD = the Death line.

**Quick check:** Backups every 24h; business can lose only 15 min of orders: which metric broken, what changes?

**Answer:** RPO + backup frequency: correct. Also said RTO exceeds MTD (not in question) and MTD = mean time to recover (wrong: MTD = Maximum Tolerable Downtime; MTTR = mean time to recover). Marked shaky.

</details>

<a name="t-3-1-8"></a>
**Protection needs elicitation (PNE)**

The process of discovering security requirements: identify assets, threats and protection needs together with stakeholders, through brainstorming, surveys (questionnaires and interviews), policy decomposition, data classification and use/misuse cases.

> On the exam: Scenario cue: 'what is the process of determining security requirements called?' → PNE.
Trap: brainstorming alone is quick but unstructured; surveys reach more stakeholders.

<details><summary>Lesson (16 Oct 2026)</summary>

**Protection needs elicitation (PNE)**

- PNE = requirements elicitation focused on SECURITY: discover what to protect, from what, how much, TOGETHER with stakeholders.
- vs elicitation: elicitation = all requirements; PNE = protection needs only.
- Identifies: ASSETS (data, systems, reputation); THREATS; PROTECTION NEEDS (C, I, A per asset) -> security requirements.
- Techniques: brainstorming; surveys (questionnaires AND interviews); policy decomposition; data classification; use/misuse cases.

**Who**

- business owners, data owners, users, legal/compliance, security (guides). Business knows value/impact
- security knows threats. Business decides, security advises.

**On the exam**

- identify assets/threats/protection needs with stakeholders = PNE.

**Trap**

- not done by security alone
- collaborative.

**Why**

- alone = over-protect some, under-protect others.

**Hook**

- what to protect, from what, how much, worked out together.

**Quick check:** Security team writes all security requirements alone: why weak?

**Answer:** Must involve stakeholders; collaborative. Correct. Added: security lacks business value/impact -> over/under-protection.

</details>

<a name="t-3-1-9"></a>
**Other requirement types**

Sequencing and timing (prevent race conditions, timeouts), international (language, encoding, export and local laws), procurement (security in purchasing contracts), deployment environment (where it runs, network and hardware constraints), archiving (what to keep, where, how long), anti-piracy (licensing, code protection).

> On the exam: Scenario cue: 'software must support multiple character sets and comply with each country's laws' → international requirements. 'Prevent TOCTOU issues' → sequencing and timing requirements.

<details><summary>Lesson (16 Oct 2026)</summary>

**Other requirement types**

- 1 SEQUENCING AND TIMING: right order + time limits. RACE CONDITION = two processes on same resource, result depends on who finishes first (double withdrawal). TOCTOU = time of check to time of use (checked, then changed before use). Timeouts. Requirement: ATOMIC transaction.
- 2 INTERNATIONAL: language/character ENCODING (bad handling can bypass input validation); EXPORT CONTROLS on strong encryption; local laws, data residency.
- 3 PROCUREMENT: security requirements in PURCHASING CONTRACTS (patch SLA, SBOM, right to test, breach notice); otherwise no leverage.
- 4 DEPLOYMENT ENVIRONMENT: where it runs (cloud/on-prem, zones, hardware, OS, air-gapped, proxy).
- 5 ARCHIVING: what to keep, where, how long, decided up front.
- 6 ANTI-PIRACY: license keys/activation, obfuscation, anti-tamper, code signing (IP).

**On the exam**

- same balance read at once = race condition = sequencing/timing
- check then swap = TOCTOU
- cannot ship crypto to some countries = international/export
- vendor contract clauses = procurement
- unlicensed copies/reverse engineering = anti-piracy.

**Hook**

- when, where in the world, who we buy from, where it runs, how long we keep it, who copies it.

**Quick check:** Same last seat sold to two customers within a millisecond: flaw + requirement type?

**Answer:** Race condition: correct (first said procurement). Requirement type = SEQUENCING AND TIMING (atomic check + reserve).

</details>

<a name="t-3-1-10"></a>
**Configuration parameters management requirements**

Requirements that configuration settings (connection strings, keys) be protected, not hardcoded, encrypted where sensitive and changeable without recompiling.

> On the exam: Scenario cue: 'database credentials stored in plaintext config' → violates configuration management requirements.

<details><summary>Lesson (16 Oct 2026)</summary>

**Configuration parameters management requirements**

- Requirements for storing, protecting, changing app configuration settings (connection strings, API keys, passwords, keys, URLs, flags, timeouts).
- 1 NEVER HARDCODE (in source = anyone with repo/leak gets it; change needs recompile); secret scanning.
- 2 PROTECT: encrypt or SECRETS MANAGER/VAULT, HSM for keys; least privilege + log access; keep secrets out of logs/errors/URLs.
- 3 CHANGEABLE WITHOUT RECOMPILING: externalized (config files, env vars, vault) -> rotation.
- 4 SEPARATE BY ENVIRONMENT: different creds dev/test/prod; prod secrets never in dev/test.
- 5 SECURE DEFAULTS (debug off, verbose errors off) + change management + CMDB.

**On the exam**

- password in repo = hardcoded -> vault + ROTATE
- best place for API keys = vault
- change connection string without redeploy = externalized config.

**Trap**

- removing a leaked secret from code does not un-leak it (history) -> rotate.

**Hook**

- no secrets in code
- vault
- change without rebuild
- rotate after any leak.

**Quick check:** AWS key public in Git 2 weeks; dev deletes line + pushes: solved?

**Answer:** No; history keeps it; rotate. Correct. Added: move to vault, check AWS logs for misuse.

</details>

## 3.2 Compliance requirements

<a name="t-3-2-1"></a>
**Regulatory authority**

Laws enforced by regulators: GDPR, HIPAA, SOX, GLBA, FISMA, CCPA/CPRA.

> On the exam: GDPR: EU residents' personal data, wherever the company is. HIPAA: US health data. SOX: integrity of public companies' financial reporting. GLBA: US financial institutions' customer data.

<details><summary>Lesson (16 Oct 2026)</summary>

**Regulatory authority**

**What it is:** requirements that come from **laws**, enforced by a **government regulator** that can **investigate, fine or punish** you. They are **mandatory**: you don't choose them, and "we didn't know" isn't a defense.

**Background terms**

- **Law / regulation** = rules made by a government (a regulation is usually the detailed rulebook an agency writes to carry out a law).
- **Regulator** = the government body that enforces it, e.g. the **FTC** (US Federal Trade Commission), the **SEC** (US securities), **HHS OCR** (US health privacy), or an EU **data protection authority**.
- **Jurisdiction** = **whose rules apply**, usually decided by **where your customers or their data are**, not just where your company is.

**The main regulations in the outline**

- **GDPR** (EU): personal data of people in the EU
- **HIPAA** (US): health information
- **SOX** (US): accuracy of public companies' financial reporting
- **GLBA** (US): privacy and security of financial customers' data
- **FISMA** (US): security of federal government systems
- **CCPA/CPRA** (California): privacy rights of California residents

**Regulation vs other requirements**

- **Regulatory** = **law**, enforced by a **government**, with fines and even criminal penalties. Mandatory.
- **Industry** (3.2.2) = set by an **industry body** through **contracts**, like PCI DSS. Mandatory if you're in that business, but not a law.
- **Company-wide** (3.2.3) = **your own** internal rules. Mandatory for your staff.

**Reach beyond borders**

**GDPR** applies to **any company anywhere** that offers goods or services to people in the EU, or monitors their behavior. A US startup with EU customers **must** comply.

**What it means for software**

The law says *what outcome* is required (protect data, keep records, let people delete their data). The team must **decompose** it into **specific requirements** (3.1): encryption, access control, audit logs, a "delete my account" feature.

**On the exam**

- "Requirements imposed by law and enforced by a government agency" → **regulatory**.
- "A US company with customers in Germany must follow…" → **GDPR** (reaches beyond the EU).
- **Trap:** **PCI DSS is not a regulation**; it's an industry standard enforced by contract.
- **Trap:** jurisdiction follows the **people and their data**, not just the company's HQ.

**Hook**

**Regulatory = the government can fine you.** Industry = your business partners can drop you. Company = your boss can.

**Quick check:** A US online shop sells to customers in France and Spain; owner says GDPR does not apply because they are American. Right?

**Answer:** No: GDPR follows the people and their data; selling to EU customers brings the shop under GDPR wherever it is based; EU regulators can fine it. Correct.

</details>

<a name="t-3-2-2"></a>
**Industry-specific**

Defense (ITAR, CMMC), healthcare (HIPAA/HITECH), financial (SOX, GLBA), payments (PCI DSS).

> On the exam: Examples: defense (ITAR export rules, CMMC for US defense suppliers), healthcare (HIPAA/HITECH), finance (SOX, GLBA, banking regulators), payments (PCI DSS).
Scenario cue: 'software that stores card numbers' → PCI DSS requirements apply, such as encryption and never storing the CVV.
Trap: PCI DSS is a contractual industry standard, not a law.

<details><summary>Lesson (16 Oct 2026)</summary>

**Industry-specific requirements**

**What it is:** requirements that apply because of **which industry you're in**. Some are **laws** aimed at one sector; some are **industry standards** enforced through contracts. Learn them **by industry**.

**Defense**

- **ITAR (International Traffic in Arms Regulations):** US law controlling **export of defense items and technical data**, including software and documentation for weapons/military systems. Only authorized **US persons** may access ITAR data without an export license. *Software requirement:* restrict access by **nationality**; keep ITAR data **in the US**.
- **CMMC (Cybersecurity Maturity Model Certification):** US **DoD** program requiring **defense contractors** to prove cybersecurity level (**Levels 1–3**) before winning contracts; largely based on **NIST SP 800-171** (protecting **CUI**, Controlled Unclassified Information). Not CMMI (process maturity, 2.8).

**Healthcare**

- **HIPAA** protects **PHI (Protected Health Information)**: medical records, diagnoses, anything linking health data to a person. **Privacy Rule** (who may see PHI) + **Security Rule** (safeguards for electronic PHI).
- **HITECH** (2009) **strengthened HIPAA**: bigger fines, **breach notification**, and made **business associates** (vendors handling PHI: cloud, billing) **directly liable**.

**Financial**

- **SOX (Sarbanes-Oxley):** **public companies** must ensure **financial reports are accurate** → **internal controls** over financial systems (COSO/COBIT, 2.2). Software: audit trails, change control, access control on financial systems.
- **GLBA (Gramm-Leach-Bliley Act):** **financial institutions** must protect **customers' personal financial data** and tell customers how it's used.

**Payments**

- **PCI DSS** (2.8): anyone handling **card data**; **industry standard enforced by contract**, not a law.

**How to answer: spot the industry + data type**

- Weapons/military tech → **ITAR**; defense contractor security level → **CMMC**
- Patient data → **HIPAA/HITECH**
- Public company financial reporting → **SOX**
- Bank/insurer customer data → **GLBA**
- Credit cards → **PCI DSS**

**On the exam**

- "Defense contractor must reach a certified cybersecurity level" → **CMMC**.
- "Restricts foreign nationals from accessing military technical data" → **ITAR**.
- "Made HIPAA business associates directly liable and added breach notification" → **HITECH**.
- **Trap:** **SOX = financial *reporting* accuracy** (integrity); **GLBA = financial *customer privacy*** (confidentiality).

**Hook**

**Guns → ITAR/CMMC. Health → HIPAA/HITECH. Books → SOX. Bank customers → GLBA. Cards → PCI.**

**Quick check:** Match: (1) hospital billing vendor processing patient claims (2) firm building targeting software for a military drone (3) public retailer whose auditors check financial reporting systems.

**Answer:** HIPAA/HITECH, ITAR, SOX. All correct. Billing vendor = business associate -> HITECH made directly liable.

</details>

<a name="t-3-2-3"></a>
**Company-wide requirements**

Approved tools, standards, frameworks and protocols.

> On the exam: What it is: internal rules every project must follow: approved languages and frameworks, crypto libraries, logging standards, authentication service, approved protocols.
Why it matters: consistency, fewer unknown components, easier support.
Scenario cue: 'a developer picks an unapproved crypto library' → violates company-wide requirements.

<details><summary>Lesson (16 Oct 2026)</summary>

**Company-wide requirements**

**What it is:** security requirements from **your own organization**, not a law or industry body. They apply to **every project**, so teams don't reinvent their own rules.

**Where they come from:** the company's **policies, standards and baselines** (2.4), turned into requirements every app must meet.

**The four kinds**

- **Approved tools:** SAST/DAST scanners, IDEs, CI/CD platform, secrets manager, AI coding assistants teams must (or may) use. *"All repos must be scanned with the approved SAST tool."*
- **Approved standards:** internal technical standards. *"Passwords hashed with Argon2id," "logs follow the central format."*
- **Approved frameworks:** what everyone builds on. *"Use the standard authentication library," "follow OWASP ASVS Level 2."*
- **Approved protocols:** allowed communication/crypto protocols. *"TLS 1.2+ only," "OAuth 2.0 / OpenID Connect for login," "no FTP; use SFTP."*

**Why companies set them**

- **Consistency:** same security floor for every team.
- **Less risk:** vetted, configured tools/libraries instead of each developer's pick (possibly insecure or hallucinated, 2.AI).
- **Easier support and auditing:** one approved way to monitor, patch, prove.
- **Cover several regulations at once:** one standard ("encrypt PII at rest with AES-256") can satisfy GDPR, HIPAA and PCI together.

**Exceptions**

Something not on the approved list → **formal exception / risk acceptance**: risk assessment, business owner approves with security advice, **documented and time-limited**.

**On the exam**

- "Every project must use the organization's approved encryption library" → **company-wide (internal) requirement**.
- "Team wants an unapproved open-source framework" → **exception process**, not "just use it."
- **Trap:** company-wide requirements are **mandatory for staff** even though they aren't laws.

**Hook**

**Company-wide = "the way we do it here."** Approved **tools, standards, frameworks, protocols.**

**Quick check:** Team wants a new unapproved logging library because it is faster. What happens first?

**Answer:** Exception process: risk assessment, documented approval before use. Correct.

</details>

<a name="t-3-2-4"></a>
**US laws to recognize**

SOX (financial reporting integrity), GLBA (financial customer privacy: Privacy Rule, Safeguards Rule), HIPAA/HITECH (health data), FISMA (federal agency security), COPPA (children under 13 online), FERPA (student records), CFAA (Computer Fraud and Abuse Act: unauthorized computer access is a crime), DMCA (copyright; bans circumventing copy protection).

> On the exam: Scenario cue: 'app collects data from children under 13' → COPPA. 'Bypassing DRM' → DMCA. 'Unauthorized access to a computer' → CFAA.

<details><summary>Lesson (16 Oct 2026)</summary>

**US laws to recognize**

**Recognition level:** know **what each law protects** and **who it applies to**.

**Ones you know**

- **SOX:** public companies' **financial reporting** accuracy (internal controls)
- **HIPAA / HITECH:** **health data** (PHI); HITECH added breach notification + business associate liability
- **FISMA (Federal Information Security Modernization Act):** **federal agencies** must run security programs; why RMF and NIST 800-53 exist (2.8). Only government systems.

**GLBA in detail (financial institutions: banks, insurers, lenders, credit unions, investment firms)**

- **Privacy Rule:** tell customers how data is collected/shared; let them **opt out** of some sharing
- **Safeguards Rule:** must have a **written security program** to protect customer data
- **Pretexting provisions:** ban getting customer info **under false pretenses** (calling a bank pretending to be the customer)

**New ones**

- **COPPA:** sites/apps aimed at **children under 13** need **verifiable parental consent** before collecting personal data. Software: age checks, consent flow.
- **FERPA:** protects **student education records** at schools receiving US federal funding.
- **CFAA (Computer Fraud and Abuse Act):** **unauthorized access to computers is a federal crime** (hacking, exceeding authorized access, malware). Main US anti-hacking law.
- **DMCA:** digital copyright; illegal to **bypass copy-protection** (DRM); takedown process.

**Two kinds of laws (KEY IDEA)**

- **Duties on the company** ("you must protect this"): HIPAA, GLBA, SOX, FISMA, COPPA, FERPA. After a hospital hack, HIPAA asks: did the hospital protect the data and notify people?
- **Punishes the attacker** ("breaking in is a crime"): **CFAA**. The hacker is prosecuted under CFAA.
- CFAA clue words: crime, prosecute, unauthorized access, break into, exceeded authorized access, **former employee logs in**.

**Match by what is protected or punished**

Kids' data → COPPA · financial **customers'** data → GLBA · government systems → FISMA · financial **reports** → SOX · education records → FERPA · **breaking in** → CFAA · bypassing DRM → DMCA

**On the exam**

- Educational app for 10-year-olds collects names/photos → **COPPA**
- University portal exposing grades → **FERPA**
- Bank/insurer needs a written security program → **GLBA Safeguards Rule**
- Caller pretends to be a customer → **GLBA pretexting**
- Prosecuting someone who broke into servers → **CFAA**
- Software bypassing a game's DRM → **DMCA**
- **Trap:** COPPA = **under 13**, not 18. FISMA = **federal only**.

**Hooks**

**Books, Banks, Bodies, Bureaucrats, Babies, Backpacks, Break-ins, Bypass** → SOX, GLBA, HIPAA, FISMA, COPPA, FERPA, CFAA, DMCA.

**CFAA = the cop chasing the hacker**; the other laws are **inspectors checking the company**.

**Quick check:** Match: (1) math game for 8-year-olds collects emails (2) insurer must create written plan to protect customer financial data (3) fired employee logs into server with old password. Re-check: hacker breaks into hospital (which law makes the break-in a crime?); credit union must tell members how data is shared + opt out.

**Answer:** User: COPPA, FISMA, SOX (1/3). Correct: COPPA, GLBA Safeguards Rule, CFAA. Re-check: HIPAA (wrong, CFAA) and GLBA (correct, Privacy Rule). Taught: duty-on-company laws vs CFAA punishes the attacker. Marked shaky.

</details>

<a name="t-3-2-5"></a>
**Breach notification laws**

California SB 1386 (2003) was the first US state breach notification law; now every US state has one. They require notifying affected residents when personal information is or is believed to be accessed by unauthorized people.

> On the exam: Design impact: encrypting personal data often creates a safe harbor from notification.
Scenario cue: 'which control can exempt a company from notifying after laptop theft?' → encryption of the data.

<details><summary>Lesson (16 Oct 2026)</summary>

**Breach notification laws**

Builds on 2.8 (GDPR 72 hours, HIPAA 60 days, SEC 4 business days); adds **US state laws** and where they started.

**The first one: California SB 1386 (2003)**

- **California** passed the **first** US state breach notification law, **SB 1386**, effective **2003**.
- Required notifying **California residents** when **unencrypted personal information** was, or was **reasonably believed to be**, acquired by an unauthorized person.
- Others copied it; **today all 50 US states** (plus DC and territories) have one.

**What they typically require**

- **Trigger:** personal info **is, or is believed to be**, accessed/acquired by someone unauthorized. No proof needed; **reasonable belief** is enough.
- **Who to tell:** **affected residents**, often the **state attorney general**/regulator, sometimes credit bureaus.
- **When:** "without unreasonable delay" or a set deadline (often **30–60 days**).
- **Personal information:** a **name + a sensitive item**: SSN, driver's license, financial account/card number with security code or password; in many states also health data, biometrics, **username + password**.

**Two key rules**

- **Encryption safe harbor:** properly encrypted + key not compromised → usually **no notification**.
- **The resident's state law applies**, not the company's. A company with customers in 12 states checks **all 12** and usually follows the **strictest**.

**What it means for software**

- **Encrypt personal data at rest** (can avoid the duty entirely).
- **Logging and monitoring** to detect breaches and know **whose** data was touched.
- **Know where users live** (their state decides which law applies).

**On the exam**

- First US state breach law → **California SB 1386 (2003)**
- How many states → **all 50**
- Unconfirmed but likely breach → **yes, notify** ("believed to be")
- Stolen laptop with full-disk encryption, key not on it → usually **no notification**
- **Trap:** the **customer's** state law applies, not just the company's home state.

**Hook**

**SB 1386 = Sunny state first, 2003.** California started it; now every state follows.

**Quick check:** Ohio company: attacker probably accessed unencrypted names + SSNs; customers in 12 states. Notify? Whose laws?

**Answer:** Yes, must notify (correct). Complete: believed-to-be is enough; unencrypted = no safe harbor; name + SSN = personal info. Laws of EACH of the 12 residents' states apply; follow the strictest.

</details>

<a name="t-3-2-6"></a>
**International laws to recognize**

GDPR (EU personal data, replaced the Data Protection Directive), UK Data Protection Act 2018, UK Computer Misuse Act (unauthorized access and modification), Basel II/III (bank capital and operational risk), PIPEDA (Canada), and various national data localization laws.

> On the exam: Scenario cue: 'UK law making hacking a criminal offense' → Computer Misuse Act. 'Banks must manage operational risk' → Basel II.

<details><summary>Lesson (16 Oct 2026)</summary>

**International laws to recognize**

Recognition level: know what each covers and where. Several pair up with US laws you know.

**GDPR (General Data Protection Regulation), EU**

- Protects **personal data of people in the EU**; applies to companies **anywhere** that serve them.
- In force **2018**; **replaced** the **EU Data Protection Directive (1995)**. A *directive* had to be turned into each country's law (rules differed); a *regulation* applies **directly and the same way** in every EU country.
- Fines up to **€20 million or 4% of global annual turnover**, whichever is **higher**.
- Privacy principles (minimization, erasure) covered in **3.4 Privacy**.

**UK Data Protection Act 2018**

- After Brexit the UK kept GDPR rules (**UK GDPR**) supported by the **DPA 2018**: the **UK's version of GDPR**.

**UK Computer Misuse Act (1990)**

- **Unauthorized access** and **unauthorized modification** (e.g. malware) are **crimes** in the UK.
- **The UK's CFAA**: punishes the **attacker** ("cop" type of law).

**Basel II / Basel III**

- International **banking** agreements on how much **capital** banks hold for risks, incl. **operational risk** (failed systems, processes, people, **cyber incidents**).
- Software: strong risk management, controls, reliable systems.

**PIPEDA (Canada)**

- Personal Information Protection and Electronic Documents Act: **private-sector** privacy (collect/use/disclose personal info in commercial activity). Canada's GDPR in spirit.

**Data localization laws**

- Certain data (often citizens') must be **stored/processed inside the country**.
- Software: **deployment environment** + **international** requirements (3.1): server, backup, cloud region location.

**Easy pairs**

- **GDPR / UK DPA 2018 / PIPEDA** = privacy (EU / UK / Canada)
- **Computer Misuse Act** = UK's **CFAA**
- **Basel II/III** = bank capital + operational risk
- **Data localization** = data must stay in the country

**On the exam**

- EU regulation that replaced the Data Protection Directive → **GDPR**
- UK law criminalizing unauthorized access/modification → **Computer Misuse Act**
- Canadian private-sector privacy → **PIPEDA**
- Banking framework for operational risk → **Basel II/III**
- Citizens' data on servers inside the country → **data localization**
- **Trap:** GDPR is a **regulation** (direct everywhere); the old Directive wasn't.

**Hook**

**GDPR = Europe's privacy rulebook. CMA = Britain's CFAA. PIPEDA = Canada's privacy. Basel = bank risk. Localization = keep it at home.**

**Quick check:** Match: (1) Canadian online retailer collecting customer data (2) hacker in London breaks in + installs malware (3) country requires citizens health data stored only inside its borders.

**Answer:** PIPEDA, Computer Misuse Act, data localization. All correct.

</details>

<a name="t-3-2-7"></a>
**Challenges of regulatory compliance**

Different laws can conflict, change over time, and vary by country; requirements are often vague, so they must be translated into specific, testable software requirements.

> On the exam: Scenario cue: 'operating in many countries with conflicting data laws' → map requirements per jurisdiction and design for data residency.

<details><summary>Lesson (16 Oct 2026)</summary>

**Challenges of regulatory compliance**

Why turning laws into software requirements is **hard**, and how teams handle it. Four challenges:

**1. Laws can conflict**

- Keep vs delete: GDPR **right to erasure** vs a **financial law** requiring transaction records for **7–10 years**.
- **Localization** (data stays in-country) vs a global cloud that **replicates** worldwide.
- **Handle it:** **legal** decides which obligation wins per case (a specific legal retention duty usually overrides an erasure request **for that data**); document it. *"Delete the profile on request; keep invoices 7 years, restricted and encrypted."*

**2. Laws change over time**

- New/updated laws (privacy, AI, breach deadlines).
- **Handle it:** legal/compliance **monitor regulatory changes**; requirements **reviewed regularly** (living documents); crypto agility + externalized config make change cheaper.

**3. Laws vary by country (and US state)**

- Different definitions of personal data, deadlines, consent rules.
- **Handle it:** **compliance mapping / common controls framework** (map many laws onto **one set of internal controls**, build once); **meet the strictest** where practical; **configurable** rules where countries truly differ (regional storage, local consent text).

**4. Laws are vague**

- "Appropriate security," "reasonable measures," "adequate protection."
- **Handle it:** **policy decomposition** (3.1) into **specific, testable** requirements; record **why** → **traceability** (RTM) for auditors.

**Who's involved**

**Legal/compliance** interpret; **business owner** decides on risk; **security** translates into controls; **developers** build. Not security's job alone.

**On the exam**

- GDPR erasure vs 7-year retention → **consult legal**; keep only what the law requires (restricted), delete the rest.
- "Appropriate technical measures" → **decompose** into specific, testable requirements.
- Many overlapping regulations efficiently → **map to a common set of controls**.
- **Trap:** developers should not interpret laws alone; involve legal/compliance.

**Worked example (quick check)**

Customer in Germany requests deletion; banking law requires 10-year transaction records → legal decides; keep **only** required transaction records (legal duty overrides erasure for that data); **delete everything else**; restrict + encrypt what's kept; **tell the customer** what was kept and why; auto-delete after 10 years.

**Hook**

**Conflict, Change, Country, Cloudy (vague).** Fix with: legal decides, monitor changes, map to common controls, decompose into testable requirements.

**Quick check:** German customer asks bank to delete all data under GDPR; banking law requires 10-year transaction records. What should the bank do?

**Answer:** Legal decides (correct). Usual outcome: keep only legally required records, delete the rest, restrict/encrypt kept data, tell the customer, delete after 10 years.

</details>

## 3.3 Data classification

<a name="t-3-3-1"></a>
**Data owner**

Accountable for the data; decides classification and who gets access.

> On the exam: Usually a business manager, not IT. The owner is accountable; the custodian is responsible for implementing.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data owner, custodian and steward (taught together)**

Two you met in 2.2 (**owner decides, custodian does**); here's the full trio.

**1. Data owner: DECIDES**

- A **senior business person** (department head/business manager), **not IT**, **accountable** for a set of data. *Head of HR owns employee data.*
- **Decides:** **classification**, **who gets access**, retention, which risks are accepted.
- **Accountable** if something goes wrong, even if others did the daily work.

**2. Data custodian: DOES the technical protection**

- Usually **IT**: DBAs, sysadmins, cloud ops.
- **Implements and maintains** the owner's decisions day to day: **backups**, **access permissions**, **patching**, **encryption**, logs.
- Doesn't decide who gets access; **carries out** the decision.

**3. Data steward: keeps it RIGHT (quality, proper use)**

- Usually a **business-side expert** (sometimes a data governance team).
- Ensures data is **accurate, consistent, complete** and used for its **proper business purpose**; defines field meanings, fixes errors/duplicates, enforces data standards.
- *HR steward makes job titles consistent, birth dates valid.*

**Clean split**

- **Owner** = accountable; decides classification + access
- **Custodian** = technical; protects (backups, permissions, encryption)
- **Steward** = quality; accurate + properly used

**Library analogy**

Owner = director (which books restricted, who borrows) · Custodian = maintenance/security (locks, alarms, repairs) · Steward = cataloguer (labeled, shelved, listed right)

**On the exam**

- Who decides classification → **owner**
- Who runs backups / applies permissions → **custodian**
- Who ensures records are accurate/consistent → **steward**
- **Trap:** **IT doesn't own data**; it's the custodian. Ownership is the **business**.
- **Trap:** custodian **implements** access; owner **approves** it.

**Hook**

**Owner decides. Custodian protects. Steward perfects.**

**Quick check:** Label: (1) Head of Sales decides contact lists are Confidential, sales-only (2) DBA sets permissions + nightly encrypted backups (3) analyst merges 3,000 duplicates + standardizes country names.

**Answer:** Owner, custodian, steward. All correct.

</details>

<a name="t-3-3-2"></a>
**Data custodian**

Implements and maintains the controls day to day (e.g., IT, DBA).

> On the exam: What it does: day-to-day protection of data the owner is accountable for: backups, applying access rights, patching, monitoring. Usually IT or DBAs.
Scenario cue: 'who performs the backups and implements access controls?' → custodian. 'Who decides who gets access?' → owner.
Trap: the custodian is responsible for doing; the owner remains accountable.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data owner, custodian and steward (taught together)**

Two you met in 2.2 (**owner decides, custodian does**); here's the full trio.

**1. Data owner: DECIDES**

- A **senior business person** (department head/business manager), **not IT**, **accountable** for a set of data. *Head of HR owns employee data.*
- **Decides:** **classification**, **who gets access**, retention, which risks are accepted.
- **Accountable** if something goes wrong, even if others did the daily work.

**2. Data custodian: DOES the technical protection**

- Usually **IT**: DBAs, sysadmins, cloud ops.
- **Implements and maintains** the owner's decisions day to day: **backups**, **access permissions**, **patching**, **encryption**, logs.
- Doesn't decide who gets access; **carries out** the decision.

**3. Data steward: keeps it RIGHT (quality, proper use)**

- Usually a **business-side expert** (sometimes a data governance team).
- Ensures data is **accurate, consistent, complete** and used for its **proper business purpose**; defines field meanings, fixes errors/duplicates, enforces data standards.
- *HR steward makes job titles consistent, birth dates valid.*

**Clean split**

- **Owner** = accountable; decides classification + access
- **Custodian** = technical; protects (backups, permissions, encryption)
- **Steward** = quality; accurate + properly used

**Library analogy**

Owner = director (which books restricted, who borrows) · Custodian = maintenance/security (locks, alarms, repairs) · Steward = cataloguer (labeled, shelved, listed right)

**On the exam**

- Who decides classification → **owner**
- Who runs backups / applies permissions → **custodian**
- Who ensures records are accurate/consistent → **steward**
- **Trap:** **IT doesn't own data**; it's the custodian. Ownership is the **business**.
- **Trap:** custodian **implements** access; owner **approves** it.

**Hook**

**Owner decides. Custodian protects. Steward perfects.**

**Quick check:** Label: (1) Head of Sales decides contact lists are Confidential, sales-only (2) DBA sets permissions + nightly encrypted backups (3) analyst merges 3,000 duplicates + standardizes country names.

**Answer:** Owner, custodian, steward. All correct.

</details>

<a name="t-3-3-3"></a>
**Data steward**

Ensures data quality and proper business use.

> On the exam: What it does: manages data quality, definitions and correct business use; maintains metadata and the data dictionary.
Scenario cue: 'reports disagree because fields are defined differently' → data steward issue.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data owner, custodian and steward (taught together)**

Two you met in 2.2 (**owner decides, custodian does**); here's the full trio.

**1. Data owner: DECIDES**

- A **senior business person** (department head/business manager), **not IT**, **accountable** for a set of data. *Head of HR owns employee data.*
- **Decides:** **classification**, **who gets access**, retention, which risks are accepted.
- **Accountable** if something goes wrong, even if others did the daily work.

**2. Data custodian: DOES the technical protection**

- Usually **IT**: DBAs, sysadmins, cloud ops.
- **Implements and maintains** the owner's decisions day to day: **backups**, **access permissions**, **patching**, **encryption**, logs.
- Doesn't decide who gets access; **carries out** the decision.

**3. Data steward: keeps it RIGHT (quality, proper use)**

- Usually a **business-side expert** (sometimes a data governance team).
- Ensures data is **accurate, consistent, complete** and used for its **proper business purpose**; defines field meanings, fixes errors/duplicates, enforces data standards.
- *HR steward makes job titles consistent, birth dates valid.*

**Clean split**

- **Owner** = accountable; decides classification + access
- **Custodian** = technical; protects (backups, permissions, encryption)
- **Steward** = quality; accurate + properly used

**Library analogy**

Owner = director (which books restricted, who borrows) · Custodian = maintenance/security (locks, alarms, repairs) · Steward = cataloguer (labeled, shelved, listed right)

**On the exam**

- Who decides classification → **owner**
- Who runs backups / applies permissions → **custodian**
- Who ensures records are accurate/consistent → **steward**
- **Trap:** **IT doesn't own data**; it's the custodian. Ownership is the **business**.
- **Trap:** custodian **implements** access; owner **approves** it.

**Hook**

**Owner decides. Custodian protects. Steward perfects.**

**Quick check:** Label: (1) Head of Sales decides contact lists are Confidential, sales-only (2) DBA sets permissions + nightly encrypted backups (3) analyst merges 3,000 duplicates + standardizes country names.

**Answer:** Owner, custodian, steward. All correct.

</details>

<a name="t-3-3-4"></a>
**Data dictionary**

Catalog of data elements, their meaning and classification.

> On the exam: What it is: a catalog describing each data element: name, meaning, format, source, owner and classification.
Why it matters: lets you apply the right protection to each field consistently (e.g., all fields marked PII get encrypted and masked).

<details><summary>Lesson (17 Oct 2026)</summary>

**Data dictionary**

**What it is:** a **catalog of every data element** (field) in a system: **what it is, its format, where it lives, how sensitive it is**. The reference book for the data.

**A typical entry**

- **Name:** `customer_dob` · **Meaning:** customer's date of birth · **Type/format:** date, YYYY-MM-DD
- **Rules:** in the past; 18 or older · **Source:** sign-up · **Stored:** CRM, `customers` table
- **Owner:** Head of Customer Operations · **Classification:** Confidential, PII · **Retention:** 7 years after closure

**Why it matters for security**

- **You can't protect what you don't know you have:** shows where every PII/PHI/card field is.
- **Drives requirements:** "Confidential / PII" triggers encryption, access control, log masking, retention (policy decomposition).
- **Privacy compliance:** answering GDPR access/erasure requests needs every field about a person.
- **Input validation:** allowed formats/values tell developers what to accept/reject.
- **Consistency:** shared definitions, maintained by the **steward**.

**Who maintains it**

**Steward** maintains; **owner** sets classification; **custodian** records storage/protection.

**Related**

- **Data inventory / data map:** where data lives and how it **flows** (2.6)
- **Metadata:** "data about data" (what a dictionary is). Not **logs** (logs record events).

**On the exam**

- Catalog of elements with definitions, formats, classification → **data dictionary**
- First step to find PII fields before encrypting → **consult/build the data dictionary / inventory** (legacy: build it, often with data-discovery tools scanning for SSNs, emails)
- **Trap:** the dictionary is the **description** (metadata), not the data itself.

**Hook**

**Data dictionary = the data's ID card.**

**Quick check:** Must encrypt every PII field in a large legacy app; nobody knows which fields. Use/build what first?

**Answer:** Data dictionary first: correct. Term fix: it is metadata/catalog, not logs. Legacy: build it, often with data-discovery tools.

</details>

<a name="t-3-3-5"></a>
**Labeling by sensitivity and impact**

E.g., FIPS 199 impact levels: low, moderate, high.

> On the exam: Rate impact on confidentiality, integrity and availability separately; the overall level is the highest one (high-water mark).

<details><summary>Lesson (17 Oct 2026)</summary>

**Labeling by sensitivity and impact + Government vs commercial labels (taught together)**

Two sides of one idea: **how you label data so everyone knows how carefully to handle it.**

**Part 1: Labeling by impact (FIPS 199)**

Rates data/systems by **harm** from a loss, separately for **C, I and A**:

- **Low:** limited adverse effect · **Moderate:** serious adverse effect · **High:** severe or catastrophic
- *Public website:* C = Low, I = Moderate, A = Moderate.
- **High-water mark:** overall rating = the **highest** of the three (Low, Low, High → **High**). Picks the **800-53B baseline** (FIPS 199 → baseline → tailor).

**Part 2: Government (US military) labels, highest → lowest, by damage to national security**

1. **Top Secret:** **exceptionally grave** damage

2. **Secret:** **serious** damage

3. **Confidential:** **damage**

4. **Unclassified:** no damage to national security (may still be restricted, e.g. **CUI**)

**Damage ladder:** "damage" → Confidential · "*serious* damage" → Secret · "*exceptionally grave* damage" → Top Secret

**Commercial labels, highest → lowest (names vary by company)**

1. **Confidential** (or Proprietary): **company secrets**: trade secrets, source code, merger plans, unreleased designs

2. **Private:** **personal** info about employees/customers: HR records, medical, salaries, home addresses

3. **Sensitive** (or Internal): not public, lower harm: internal plans, org charts

4. **Public:** marketing, press releases

**Test:** about a **person** → Private. **Company secret** → Confidential.

**⚠️ Big trap**

"Confidential" = **lowest** classified level in government, **highest** in commercial. Check which scheme.

**Why labels matter for software**

- Label **drives controls**: encryption, access, logging, retention, destruction (clear/purge/destroy).
- Labels **visible + machine-readable** (file tags, data dictionary) so systems enforce automatically (DLP blocks emailing "Confidential").
- **Data owner** decides the label.

**On the exam**

- Exceptionally grave → **Top Secret** · Serious → **Secret** · Damage → **Confidential**
- Highest commercial (trade secrets) → **Confidential**
- Employee medical/salary records → **Private**
- C/I/A = Low/Moderate/High overall → **High**

**Hooks**

Government: **"Top Secret Spies Carry Umbrellas"** (TS, S, C, U). Commercial: **"Can People See Public?"** (Confidential, Private, Sensitive, Public).

**Quick check:** (1) C=Moderate, I=Low, A=High overall? (2) unreleased product designs commercial label? (3) serious damage to national security?

**Answer:** C=Moderate, I=Low, A=High -> High (high-water mark). Correct.

</details>

<a name="t-3-3-6"></a>
**Government vs commercial labels**

Top secret/secret/confidential/unclassified vs confidential/private/sensitive/public.

> On the exam: Government (highest first): Top Secret, Secret, Confidential, Unclassified (sometimes Sensitive but Unclassified).
Commercial (highest first): Confidential/Proprietary, Private, Sensitive, Public.
Why it matters: classification decides the controls: who can access, encryption, labeling, retention, destruction.

<details><summary>Lesson (17 Oct 2026)</summary>

**Labeling by sensitivity and impact + Government vs commercial labels (taught together)**

Two sides of one idea: **how you label data so everyone knows how carefully to handle it.**

**Part 1: Labeling by impact (FIPS 199)**

Rates data/systems by **harm** from a loss, separately for **C, I and A**:

- **Low:** limited adverse effect · **Moderate:** serious adverse effect · **High:** severe or catastrophic
- *Public website:* C = Low, I = Moderate, A = Moderate.
- **High-water mark:** overall rating = the **highest** of the three (Low, Low, High → **High**). Picks the **800-53B baseline** (FIPS 199 → baseline → tailor).

**Part 2: Government (US military) labels, highest → lowest, by damage to national security**

1. **Top Secret:** **exceptionally grave** damage

2. **Secret:** **serious** damage

3. **Confidential:** **damage**

4. **Unclassified:** no damage to national security (may still be restricted, e.g. **CUI**)

**Damage ladder:** "damage" → Confidential · "*serious* damage" → Secret · "*exceptionally grave* damage" → Top Secret

**Commercial labels, highest → lowest (names vary by company)**

1. **Confidential** (or Proprietary): **company secrets**: trade secrets, source code, merger plans, unreleased designs

2. **Private:** **personal** info about employees/customers: HR records, medical, salaries, home addresses

3. **Sensitive** (or Internal): not public, lower harm: internal plans, org charts

4. **Public:** marketing, press releases

**Test:** about a **person** → Private. **Company secret** → Confidential.

**⚠️ Big trap**

"Confidential" = **lowest** classified level in government, **highest** in commercial. Check which scheme.

**Why labels matter for software**

- Label **drives controls**: encryption, access, logging, retention, destruction (clear/purge/destroy).
- Labels **visible + machine-readable** (file tags, data dictionary) so systems enforce automatically (DLP blocks emailing "Confidential").
- **Data owner** decides the label.

**On the exam**

- Exceptionally grave → **Top Secret** · Serious → **Secret** · Damage → **Confidential**
- Highest commercial (trade secrets) → **Confidential**
- Employee medical/salary records → **Private**
- C/I/A = Low/Moderate/High overall → **High**

**Hooks**

Government: **"Top Secret Spies Carry Umbrellas"** (TS, S, C, U). Commercial: **"Can People See Public?"** (Confidential, Private, Sensitive, Public).

**Quick check:** (1) C=Moderate, I=Low, A=High overall? (2) unreleased product designs commercial label? (3) serious damage to national security?

**Answer:** User: unreleased designs = Private (wrong: Confidential, company secret); serious damage = Top Secret (wrong: Secret). Re-check: exceptionally grave = Top Secret, employee addresses + salaries = Private, both correct. Marked shaky.

</details>

<a name="t-3-3-7"></a>
**Structured vs unstructured data**

Databases vs documents, emails, images.

> On the exam: Structured: organized in fixed fields (databases, spreadsheets), easy to search and control. Unstructured: documents, emails, images, chat, easy to lose track of.
Scenario cue: 'sensitive data is spread across shared documents and emails' → unstructured data; use discovery and DLP tools.

<details><summary>Lesson (17 Oct 2026)</summary>

**Structured vs unstructured data**

**Structured**

- **Fixed format**, rows and columns: database tables, spreadsheets, CSV.
- Every field has a defined type and place (`email` always in the email column).
- **Easy to secure:** you know where sensitive fields are (data dictionary) → encrypt a column, mask, restrict per field.

**Unstructured**

- **No fixed format:** documents (Word, PDF), **emails**, **chat messages**, **images**, scanned forms, audio/video, free-text notes.
- Sensitive data can be **anywhere inside** (card number pasted in a support chat, scanned passport, health details in a comments box).
- **Hard to secure:** no column to encrypt. Most of an org's data (often 80%+).

**Semi-structured**

- Some structure, no rigid table: **JSON, XML**, log files (tags/keys, varying fields).

**How unstructured data gets protected**

- **Data discovery and classification tools** scan files/email/storage for patterns (SSN, card formats) and **auto-label**.
- **DLP** watches email, uploads, copies; blocks sensitive content leaving.
- **Encrypt whole containers:** file share, disk, bucket.
- **Requirements:** avoid free-text fields where possible (structured, validated phone field instead of a notes box); tell users not to paste sensitive data into comments.

**Why it matters**

Classification/privacy requirements (erasure, retention, breach scoping) must cover **both**. Forgetting attachments, chat logs, scanned forms is a classic gap.

**On the exam**

- Database table of customer records → **structured**
- Scanned contracts, emails, chat logs → **unstructured**
- Hardest to classify and protect → **unstructured**
- Finds sensitive data inside documents/emails → **data discovery / DLP**
- **Trap:** erasure or breach response that only checks databases misses unstructured copies.

**Hook**

**Structured = a spreadsheet: every value in its box. Unstructured = a junk drawer: anything could be anywhere.**

**Quick check:** GDPR deletion request; team deletes the customer rows from the database. What did they miss?

**Answer:** Unstructured data + data discovery: correct. E.g. support emails, chat logs, scanned IDs, attachments, notes, copies in logs/backups.

</details>

<a name="t-3-3-8"></a>
**Data lifecycle**

Create, store, use, share, archive, destroy.

> On the exam: Stages: create/collect → store → use → share → archive → destroy.
Why it matters: requirements apply at every stage, e.g., encryption when stored, masking when used, secure transfer when shared, verified destruction at the end.
Trap: forgetting the destroy stage is a common mistake.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data lifecycle + Data states (taught together)**

The **lifecycle** = **stages** data passes through; the **states** = **where it physically is** at any moment.

**Part 1: The data lifecycle (6 stages)**

1. **Create:** generated/collected (sign-up form, sensor, upload). **Classify HERE** (owner's job).

2. **Store:** saved to DB, file share, bucket. Encrypt at rest, access controls.

3. **Use:** viewed/processed/changed. Access control, least privilege, logging.

4. **Share:** sent to people/systems/third parties. Encrypt in transit, contracts, DLP.

5. **Archive:** long-term storage (2.6). Encrypted, restricted, readable.

6. **Destroy:** securely removed (clear/purge/destroy, crypto-shredding). Cover **every** copy.

**Mnemonic:** "Can Someone Use Shared Archived Data?"

**Key ideas:** classification at Create follows the data; each stage needs its own controls; destroy is planned from the start (retention, 3.4).

**Part 2: The three data states**

- **At rest:** stored, not moving (disk, DB, backup, USB). Protect: **encryption at rest** (AES-256, full-disk), access control, secure key storage.
- **In transit (in motion):** moving across a network (browser↔server, service↔service, to backup site). Protect: **TLS 1.2+**, VPN, SSH; never plain HTTP/FTP.
- **In use:** being processed **in memory** (RAM/CPU); apps usually **decrypt** to work, so it's exposed. Protect: limit what's loaded, **clear sensitive data from memory** after use, process access control, **confidential computing** (secure enclaves/TEEs). **Hardest state to protect**; targeted by memory scraping (POS malware).

**How they connect**

Stage = what's happening; state = where it is. Share → in transit. Store/Archive → at rest. Use → in use.

**On the exam**

- Laptop hard drive → **at rest** · browser to API → **in transit** · card number in RAM → **in use**
- Hardest state → **in use** · TLS → **in transit** · full-disk encryption → **at rest**
- Classify when? → **creation** · last stage → **destroy**
- **Trap:** encryption at rest doesn't protect **in use** or **in transit**.

**Hook**

**Rest = parked. Transit = driving. Use = being worked on in the garage, hood open.**

**Quick check:** (1) POS malware reads card numbers from memory during processing: which state? (2) which stage to first classify? (3) AES-256 on all databases: protects data between web servers and DB?

**Answer:** In use; create; no (at rest only, in transit needs TLS). All correct.

</details>

<a name="t-3-3-9"></a>
**PII, PHI, publicly available information**

Personal, health, and public data each need different handling.

> On the exam: PII: identifies a person (name, ID number, email). PHI: health info linked to a person (HIPAA). Publicly available info: already public, so confidentiality is low, but integrity still matters.
Scenario cue: 'combining public data creates a profile' → aggregation can make public data sensitive.

<details><summary>Lesson (17 Oct 2026)</summary>

**PII, PHI, publicly available information + Data remanence (taught together)**

Both are about data that is **more sensitive or more persistent than people assume**.

**Part 1: PII, PHI, publicly available information**

**PII (Personally Identifiable Information):** anything that can **identify a specific person**, alone or combined.

- **Direct identifiers:** full name + address, **SSN**, passport, email, phone, biometrics.
- **Indirect (quasi-) identifiers:** DOB, ZIP, gender, job title. **ZIP + DOB + gender** uniquely identifies most people in the US.
- **Sensitive PII:** SSN, financial accounts, health, biometrics, religion, sexual orientation (GDPR "special categories" need extra protection).

**PHI (Protected Health Information):** **health info linked to a person**, held by a provider, insurer or **business associate** (HIPAA/HITECH).

- Diagnoses, prescriptions, test results, medical record numbers, appointment dates **when tied to an identifiable person**.
- **Test:** health data **+** identifier = PHI. Anonymous statistics aren't PHI.

**Publicly available information:** legally accessible to anyone (public posts, directories, government records, news).

- **Trap: public ≠ no rules.** Under **GDPR**, public personal data is **still protected** (scraping profiles for marketing needs a lawful basis).
- **Aggregation risk:** harmless public facts combined reveal sensitive things (doxxing, targeted phishing).

**Requirements:** PII → privacy laws (GDPR, CCPA, breach notification); PHI → HIPAA safeguards; public → lighter, but still minimization + aggregation checks.

**Part 2: Data remanence**

**Data left behind** after supposed deletion (2.6: formatting removes pointers). Where it hides:

- **Deleted files:** contents stay until overwritten.
- **Freed memory (RAM):** passwords/card numbers stay until overwritten; memory dumps and **crash reports** expose them.
- **Swap/page and hibernation files:** in-use secrets end up at rest.
- **Temp files, caches, debug logs.**
- **Old disks/SSDs:** wear leveling leaves hidden copies.
- **Cloud:** deleted volumes, snapshots, backups, replicas; freed disks reassigned to another tenant if not wiped.

**Software requirements to prevent it:**

- **Clear/overwrite sensitive data in memory** right after use; secure memory APIs; avoid immutable strings for secrets.
- **No secrets in logs, temp files or crash dumps** (mask/exclude).
- **Encrypt at rest**; **crypto-shredding** in the cloud.
- **Sanitize media** per **NIST 800-88**; delete **every copy**.

**On the exam**

- Name + SSN → **PII (direct, sensitive)** · ZIP + DOB + gender → **indirect identifiers = PII together**
- Diagnosis linked to name at a clinic → **PHI**
- Scraped public profiles → **still personal data**
- Password readable in memory dump after logout → **remanence (memory)**
- Deleted cloud volume recovered by another tenant → **remanence**
- **Traps:** deleting a file doesn't remove contents; public data isn't free of privacy rules.

**Hooks**

**PII = who you are. PHI = health + who you are. Public ≠ permission.** **Remanence = data's ghost.**

**Quick check:** (1) Dataset with no names but ZIP + full DOB + gender: non-personal? (2) Crash dump after logout contains plain-text password: name + one requirement.

**Answer:** Not safe, combined = PII; data remanence, overwrite/clear memory after use (also keep secrets out of crash dumps/logs). Both correct.

</details>

<a name="t-3-3-10"></a>
**Data states**

At rest (stored), in transit (moving over networks), in use (being processed in memory).

> On the exam: Controls: at rest → storage/database encryption; in transit → TLS; in use → access control, memory protection, enclaves.
Scenario cue: 'data must be protected while it's being processed' → data in use; hardest state to protect.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data lifecycle + Data states (taught together)**

The **lifecycle** = **stages** data passes through; the **states** = **where it physically is** at any moment.

**Part 1: The data lifecycle (6 stages)**

1. **Create:** generated/collected (sign-up form, sensor, upload). **Classify HERE** (owner's job).

2. **Store:** saved to DB, file share, bucket. Encrypt at rest, access controls.

3. **Use:** viewed/processed/changed. Access control, least privilege, logging.

4. **Share:** sent to people/systems/third parties. Encrypt in transit, contracts, DLP.

5. **Archive:** long-term storage (2.6). Encrypted, restricted, readable.

6. **Destroy:** securely removed (clear/purge/destroy, crypto-shredding). Cover **every** copy.

**Mnemonic:** "Can Someone Use Shared Archived Data?"

**Key ideas:** classification at Create follows the data; each stage needs its own controls; destroy is planned from the start (retention, 3.4).

**Part 2: The three data states**

- **At rest:** stored, not moving (disk, DB, backup, USB). Protect: **encryption at rest** (AES-256, full-disk), access control, secure key storage.
- **In transit (in motion):** moving across a network (browser↔server, service↔service, to backup site). Protect: **TLS 1.2+**, VPN, SSH; never plain HTTP/FTP.
- **In use:** being processed **in memory** (RAM/CPU); apps usually **decrypt** to work, so it's exposed. Protect: limit what's loaded, **clear sensitive data from memory** after use, process access control, **confidential computing** (secure enclaves/TEEs). **Hardest state to protect**; targeted by memory scraping (POS malware).

**How they connect**

Stage = what's happening; state = where it is. Share → in transit. Store/Archive → at rest. Use → in use.

**On the exam**

- Laptop hard drive → **at rest** · browser to API → **in transit** · card number in RAM → **in use**
- Hardest state → **in use** · TLS → **in transit** · full-disk encryption → **at rest**
- Classify when? → **creation** · last stage → **destroy**
- **Trap:** encryption at rest doesn't protect **in use** or **in transit**.

**Hook**

**Rest = parked. Transit = driving. Use = being worked on in the garage, hood open.**

**Quick check:** (1) POS malware reads card numbers from memory during processing: which state? (2) which stage to first classify? (3) AES-256 on all databases: protects data between web servers and DB?

**Answer:** In use; create; no (at rest only, in transit needs TLS). All correct.

</details>

<a name="t-3-3-11"></a>
**Data remanence**

Data left behind after deletion (deleted files, freed memory, old disks, cloud volumes).

> On the exam: Defenses: secure wiping, crypto-shredding, physical destruction, clearing memory after use.
Scenario cue: 'a resold hard drive contained customer files' → data remanence.

<details><summary>Lesson (17 Oct 2026)</summary>

**PII, PHI, publicly available information + Data remanence (taught together)**

Both are about data that is **more sensitive or more persistent than people assume**.

**Part 1: PII, PHI, publicly available information**

**PII (Personally Identifiable Information):** anything that can **identify a specific person**, alone or combined.

- **Direct identifiers:** full name + address, **SSN**, passport, email, phone, biometrics.
- **Indirect (quasi-) identifiers:** DOB, ZIP, gender, job title. **ZIP + DOB + gender** uniquely identifies most people in the US.
- **Sensitive PII:** SSN, financial accounts, health, biometrics, religion, sexual orientation (GDPR "special categories" need extra protection).

**PHI (Protected Health Information):** **health info linked to a person**, held by a provider, insurer or **business associate** (HIPAA/HITECH).

- Diagnoses, prescriptions, test results, medical record numbers, appointment dates **when tied to an identifiable person**.
- **Test:** health data **+** identifier = PHI. Anonymous statistics aren't PHI.

**Publicly available information:** legally accessible to anyone (public posts, directories, government records, news).

- **Trap: public ≠ no rules.** Under **GDPR**, public personal data is **still protected** (scraping profiles for marketing needs a lawful basis).
- **Aggregation risk:** harmless public facts combined reveal sensitive things (doxxing, targeted phishing).

**Requirements:** PII → privacy laws (GDPR, CCPA, breach notification); PHI → HIPAA safeguards; public → lighter, but still minimization + aggregation checks.

**Part 2: Data remanence**

**Data left behind** after supposed deletion (2.6: formatting removes pointers). Where it hides:

- **Deleted files:** contents stay until overwritten.
- **Freed memory (RAM):** passwords/card numbers stay until overwritten; memory dumps and **crash reports** expose them.
- **Swap/page and hibernation files:** in-use secrets end up at rest.
- **Temp files, caches, debug logs.**
- **Old disks/SSDs:** wear leveling leaves hidden copies.
- **Cloud:** deleted volumes, snapshots, backups, replicas; freed disks reassigned to another tenant if not wiped.

**Software requirements to prevent it:**

- **Clear/overwrite sensitive data in memory** right after use; secure memory APIs; avoid immutable strings for secrets.
- **No secrets in logs, temp files or crash dumps** (mask/exclude).
- **Encrypt at rest**; **crypto-shredding** in the cloud.
- **Sanitize media** per **NIST 800-88**; delete **every copy**.

**On the exam**

- Name + SSN → **PII (direct, sensitive)** · ZIP + DOB + gender → **indirect identifiers = PII together**
- Diagnosis linked to name at a clinic → **PHI**
- Scraped public profiles → **still personal data**
- Password readable in memory dump after logout → **remanence (memory)**
- Deleted cloud volume recovered by another tenant → **remanence**
- **Traps:** deleting a file doesn't remove contents; public data isn't free of privacy rules.

**Hooks**

**PII = who you are. PHI = health + who you are. Public ≠ permission.** **Remanence = data's ghost.**

**Quick check:** (1) Dataset with no names but ZIP + full DOB + gender: non-personal? (2) Crash dump after logout contains plain-text password: name + one requirement.

**Answer:** Not safe, combined = PII; data remanence, overwrite/clear memory after use (also keep secrets out of crash dumps/logs). Both correct.

</details>

## 3.4 Privacy requirements

<a name="t-3-4-1"></a>
**Data collection scope / minimization**

Collect only what's needed for the stated purpose.

> On the exam: What it is: collect only the personal data truly needed for the stated purpose, and nothing extra 'just in case'.
Why it matters: data you never collect can't be breached, lowers compliance scope.
Scenario cue: 'a sign-up form asks for date of birth that isn't needed' → violates data minimization.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data minimization + Purpose limitation and consent (taught together)**

The two most basic privacy questions: **what** data do you collect, and **why**?

**Part 1: Data minimization (collection scope)**

Collect **only the personal data you actually need** for a **specific, stated purpose**.

- **Fewer fields:** age range (18+) instead of DOB; ZIP instead of full address.
- **Less precision:** city instead of GPS; year of birth instead of full date.
- **Less time:** keep only as long as needed (retention, 3.4.7).

**Why for security:** data you don't collect **can't be breached**; smaller breach impact, compliance scope (like tokenization for PCI), cost.

**In requirements:** every field has a **documented reason**. Test: *remove this field: does the feature break?* If not, don't collect it.

**Part 2: Purpose limitation and consent**

**Purpose limitation:** data collected for **one stated purpose** must **not** be reused for a **different, unrelated purpose** without a new legal basis (usually **new consent**). *Emails for order confirmations → used for marketing = violation.*

**Valid consent (GDPR):**

- **Freely given** (no "agree to marketing or no app")
- **Specific** (per purpose, no blanket "I agree to everything")
- **Informed** (clear language)
- **Unambiguous, clear action** (**active opt-in**; no pre-ticked boxes)
- **Withdrawable** (as easy to withdraw as to give)

**Six GDPR legal bases:** consent, contract, legal obligation, vital interests, public task, legitimate interests. Shipping to an address = **contract** (no consent needed). Consent matters most for **optional** uses like marketing.

**In requirements:** **consent records** (who, what, when, which terms version); **separate checkbox per purpose**; easy **withdraw**; **tag data with its purpose** so systems block reuse.

**Principle vs process (pre-test mix-up)**

- **Minimization / purpose limitation = principles** (the rules).
- **PIA/DPIA = process** that **checks** a project follows them (3.4.10).
- Collecting an unneeded SSN → principle broken = **minimization**; a PIA should have **caught** it.

**On the exam**

- Collects more than needed → **minimization**
- Reused for a new purpose without consent → **purpose limitation**
- Pre-ticked consent box → **invalid consent** (needs active opt-in)
- Which field to remove? → the one **not needed** for the stated purpose
- **Trap:** PIA is a **process**, not a principle.

**Worked example (quick check)**

Delivery app collects GPS **only during delivery**; marketing wants stored location history for ads → violates **purpose limitation**; needs **new specific opt-in consent**; **minimization** says don't store the history at all (delete after delivery).

**Hook**

**Minimization = what you take (only what you need). Purpose limitation = what you do with it (only what you said).** *"Take only what you need, use it only as promised."*

**Quick check:** Delivery app collects GPS only during delivery; marketing wants stored location history for ads. (1) principle violated (2) needed first (3) what minimization says about storing history.

**Answer:** Purpose limitation (after first saying minimization); new specific consent; do not store the history at all. Correct. Pre-test: Q1 said PIA (process) instead of minimization (principle); Q2 purpose limitation correct.

</details>

<a name="t-3-4-2"></a>
**Purpose limitation and consent**

Use data only for what users agreed to.

> On the exam: What it is: data collected for one purpose can't be reused for an unrelated purpose without a legal basis or new consent. Consent must be informed, specific and freely given, and can be withdrawn.
Scenario cue: 'support ticket data is used to train a marketing model' → purpose limitation issue.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data minimization + Purpose limitation and consent (taught together)**

The two most basic privacy questions: **what** data do you collect, and **why**?

**Part 1: Data minimization (collection scope)**

Collect **only the personal data you actually need** for a **specific, stated purpose**.

- **Fewer fields:** age range (18+) instead of DOB; ZIP instead of full address.
- **Less precision:** city instead of GPS; year of birth instead of full date.
- **Less time:** keep only as long as needed (retention, 3.4.7).

**Why for security:** data you don't collect **can't be breached**; smaller breach impact, compliance scope (like tokenization for PCI), cost.

**In requirements:** every field has a **documented reason**. Test: *remove this field: does the feature break?* If not, don't collect it.

**Part 2: Purpose limitation and consent**

**Purpose limitation:** data collected for **one stated purpose** must **not** be reused for a **different, unrelated purpose** without a new legal basis (usually **new consent**). *Emails for order confirmations → used for marketing = violation.*

**Valid consent (GDPR):**

- **Freely given** (no "agree to marketing or no app")
- **Specific** (per purpose, no blanket "I agree to everything")
- **Informed** (clear language)
- **Unambiguous, clear action** (**active opt-in**; no pre-ticked boxes)
- **Withdrawable** (as easy to withdraw as to give)

**Six GDPR legal bases:** consent, contract, legal obligation, vital interests, public task, legitimate interests. Shipping to an address = **contract** (no consent needed). Consent matters most for **optional** uses like marketing.

**In requirements:** **consent records** (who, what, when, which terms version); **separate checkbox per purpose**; easy **withdraw**; **tag data with its purpose** so systems block reuse.

**Principle vs process (pre-test mix-up)**

- **Minimization / purpose limitation = principles** (the rules).
- **PIA/DPIA = process** that **checks** a project follows them (3.4.10).
- Collecting an unneeded SSN → principle broken = **minimization**; a PIA should have **caught** it.

**On the exam**

- Collects more than needed → **minimization**
- Reused for a new purpose without consent → **purpose limitation**
- Pre-ticked consent box → **invalid consent** (needs active opt-in)
- Which field to remove? → the one **not needed** for the stated purpose
- **Trap:** PIA is a **process**, not a principle.

**Worked example (quick check)**

Delivery app collects GPS **only during delivery**; marketing wants stored location history for ads → violates **purpose limitation**; needs **new specific opt-in consent**; **minimization** says don't store the history at all (delete after delivery).

**Hook**

**Minimization = what you take (only what you need). Purpose limitation = what you do with it (only what you said).** *"Take only what you need, use it only as promised."*

**Quick check:** Delivery app collects GPS only during delivery; marketing wants stored location history for ads. (1) principle violated (2) needed first (3) what minimization says about storing history.

**Answer:** Purpose limitation (after first saying minimization); new specific consent; do not store the history at all. Correct. Pre-test: Q1 said PIA (process) instead of minimization (principle); Q2 purpose limitation correct.

</details>

<a name="t-3-4-3"></a>
**Anonymization vs pseudonymization**

Anonymized data can't be re-identified. Pseudonymized data can, with a separately stored key.

> On the exam: Anonymization: irreversible; the data no longer identifies anyone and is no longer personal data under GDPR.
Pseudonymization: identifiers replaced with aliases; the mapping key exists separately, so it can be reversed and is still personal data.
Scenario cue: 'analysts need to link records over time without seeing names' → pseudonymization.

<details><summary>Lesson (17 Oct 2026)</summary>

**Anonymization vs pseudonymization + De-identification techniques (taught together)**

Topic 3 = the **goal** (how identifiable data still is); topic 4 = the **toolbox**.

**Part 1: Anonymization vs pseudonymization**

**Anonymization:** changed so the person **can never be re-identified**, by anyone, by any reasonable means. **Irreversible.**

- GDPR: truly anonymized data is **no longer personal data** → GDPR **doesn't apply**.
- **Hard:** ZIP + DOB + gender re-identify "nameless" data. **Removing names ≠ anonymization.**

**Pseudonymization:** identifiers **replaced with a substitute** (code/token/pseudonym); link back kept **separately** under strict control. **Reversible** with the key.

- *Patient names → `P-48213`, mapping table locked away.*
- GDPR: **still personal data** → GDPR **still applies**; recognized as a good **security measure**.
- **Tokenization** (PCI, 2.8) is a form of pseudonymization.

**Test:** can anyone, with any key or reasonable effort, link it back? **Yes** → pseudonymized (still personal). **Never** → anonymized (not personal).

**Part 2: The toolbox**

1. **Masking:** hides part of a visible value (`**** **** **** 4821`). **Static** = permanently changed copy (test/dev). **Dynamic** = hidden on the fly by viewer role (support sees `****4821`, finance sees full). Best for screens, test/dev, logs.

2. **Generalization:** less precise (age 34 → 30–39; ZIP 94107 → 941**; date → year).

3. **Suppression:** remove a value or whole record (drop SSN column; drop the only 95-year-old in a small town).

4. **k-anonymity:** every person indistinguishable from **at least k−1 others** on quasi-identifiers (k = 5: each ZIP area + age range + gender combo matches ≥5 people); achieved via generalization + suppression. **Weakness:** if all in a group share the same sensitive value, it leaks (l-diversity fixes).

5. **Differential privacy:** **calculated random noise** added to **query results/statistics** so output barely changes whether or not one person is included. **Mathematical guarantee**; used by Apple, Google, US Census. Trade-off: more noise = more privacy, less accuracy.

**Clue words**

- "shows only last 4 digits" → **masking**
- "age ranges instead of exact age" → **generalization**
- "removed the record entirely" → **suppression**
- "each record matches at least k others" → **k-anonymity**
- "random noise added to statistics" → **differential privacy**
- "replaced with a code, key kept separately" → **pseudonymization / tokenization**

**On the exam**

- Re-identifiable with separately held key → **pseudonymization**; GDPR **still applies**
- Can't be re-identified by any means → **anonymization**; GDPR **no longer applies**
- Testers need realistic data without real cards → **static masking** (or tokenized test data)
- Mathematical guarantee no individual detectable → **differential privacy**
- **Traps:** removing names ≠ anonymization; pseudonymized data is still personal data.

**Hooks**

**Pseudonym = a nickname** (someone still knows who you are). **Anonymous = no name at all, ever.**

Toolbox: **Mask it, blur it, drop it, blend it, fuzz it** → masking, generalization, suppression, k-anonymity, differential privacy.

**Quick check:** (1) Customer IDs replaced with random tokens, map kept in separate vault: GDPR still applies? (2) last 4 digits of phone / age 40-49 instead of 43 / noise added to stats.

**Answer:** GDPR still applies (pseudonymization, reversible) after first saying no; masking, generalization, differential privacy. All correct. Pre-test: Q3 pseudonymization correct; Q4 said masking for noise (should be differential privacy).

</details>

<a name="t-3-4-4"></a>
**De-identification techniques**

Masking, generalization, k-anonymity, differential privacy.

> On the exam: k-anonymity: each record matches at least k-1 others. Differential privacy adds statistical noise to results.

<details><summary>Lesson (17 Oct 2026)</summary>

**Anonymization vs pseudonymization + De-identification techniques (taught together)**

Topic 3 = the **goal** (how identifiable data still is); topic 4 = the **toolbox**.

**Part 1: Anonymization vs pseudonymization**

**Anonymization:** changed so the person **can never be re-identified**, by anyone, by any reasonable means. **Irreversible.**

- GDPR: truly anonymized data is **no longer personal data** → GDPR **doesn't apply**.
- **Hard:** ZIP + DOB + gender re-identify "nameless" data. **Removing names ≠ anonymization.**

**Pseudonymization:** identifiers **replaced with a substitute** (code/token/pseudonym); link back kept **separately** under strict control. **Reversible** with the key.

- *Patient names → `P-48213`, mapping table locked away.*
- GDPR: **still personal data** → GDPR **still applies**; recognized as a good **security measure**.
- **Tokenization** (PCI, 2.8) is a form of pseudonymization.

**Test:** can anyone, with any key or reasonable effort, link it back? **Yes** → pseudonymized (still personal). **Never** → anonymized (not personal).

**Part 2: The toolbox**

1. **Masking:** hides part of a visible value (`**** **** **** 4821`). **Static** = permanently changed copy (test/dev). **Dynamic** = hidden on the fly by viewer role (support sees `****4821`, finance sees full). Best for screens, test/dev, logs.

2. **Generalization:** less precise (age 34 → 30–39; ZIP 94107 → 941**; date → year).

3. **Suppression:** remove a value or whole record (drop SSN column; drop the only 95-year-old in a small town).

4. **k-anonymity:** every person indistinguishable from **at least k−1 others** on quasi-identifiers (k = 5: each ZIP area + age range + gender combo matches ≥5 people); achieved via generalization + suppression. **Weakness:** if all in a group share the same sensitive value, it leaks (l-diversity fixes).

5. **Differential privacy:** **calculated random noise** added to **query results/statistics** so output barely changes whether or not one person is included. **Mathematical guarantee**; used by Apple, Google, US Census. Trade-off: more noise = more privacy, less accuracy.

**Clue words**

- "shows only last 4 digits" → **masking**
- "age ranges instead of exact age" → **generalization**
- "removed the record entirely" → **suppression**
- "each record matches at least k others" → **k-anonymity**
- "random noise added to statistics" → **differential privacy**
- "replaced with a code, key kept separately" → **pseudonymization / tokenization**

**On the exam**

- Re-identifiable with separately held key → **pseudonymization**; GDPR **still applies**
- Can't be re-identified by any means → **anonymization**; GDPR **no longer applies**
- Testers need realistic data without real cards → **static masking** (or tokenized test data)
- Mathematical guarantee no individual detectable → **differential privacy**
- **Traps:** removing names ≠ anonymization; pseudonymized data is still personal data.

**Hooks**

**Pseudonym = a nickname** (someone still knows who you are). **Anonymous = no name at all, ever.**

Toolbox: **Mask it, blur it, drop it, blend it, fuzz it** → masking, generalization, suppression, k-anonymity, differential privacy.

**Quick check:** (1) Customer IDs replaced with random tokens, map kept in separate vault: GDPR still applies? (2) last 4 digits of phone / age 40-49 instead of 43 / noise added to stats.

**Answer:** GDPR still applies (pseudonymization, reversible) after first saying no; masking, generalization, differential privacy. All correct. Pre-test: Q3 pseudonymization correct; Q4 said masking for noise (should be differential privacy).

</details>

<a name="t-3-4-5"></a>
**User rights**

Access, correction, erasure (right to be forgotten), portability, objection.

> On the exam: Rights (GDPR-style): access, correction, erasure (right to be forgotten), restriction, portability, objection.
Design impact: you must be able to find, export and delete a person's data everywhere, including logs, backups and third parties.
Scenario cue: 'a user asks to delete their account' → delete data everywhere and tell third parties.

<details><summary>Lesson (17 Oct 2026)</summary>

**User rights**

Rights privacy laws give people over **their own personal data**; software must be **built** to honor them (functional requirements).

**GDPR rights**

- **Be informed:** told what's collected and why (privacy notice).
- **Access:** get a **copy** of all their data; request = **DSAR** (data subject access request); **one month** to respond.
- **Rectification:** have **incorrect** data **corrected**.
- **Erasure ("right to be forgotten"):** data **deleted**. **Not absolute:** refused where a **legal duty to keep** applies (bank's 10-year records).
- **Restrict processing:** "keep it, but stop **using** it" (e.g. during a dispute).
- **Data portability:** data in a **structured, machine-readable format** (CSV/JSON) to **move** to another service.
- **Object:** object to certain processing; **absolute for direct marketing** (must stop).
- **Automated decisions:** not subject to decisions made **solely by automated means** (incl. profiling) with significant effects (AI loan rejection without human review).

**CCPA/CPRA (California)**

Know, delete, correct, **opt out of sale/sharing**, limit sensitive data use, **non-discrimination**.

**Software requirements**

- **Self-service:** download my data, edit profile, delete account, marketing preferences.
- **Verify identity FIRST:** otherwise attackers file fake requests and receive others' data (social engineering / pretexting). Verify via what's **on file** (log in, original email), **not** a new address the requester supplies; a request to send to a new address is a red flag.
- **Find every copy:** data dictionary + unstructured data + backups/logs (3.3).
- **Track deadlines** (one month) and record each request.
- **Machine-readable exports** for portability.

**On the exam**

- Copy of all their data → **access (DSAR)** · format to move to a competitor → **portability**
- Fix incorrect data → **rectification** · delete → **erasure** (unless legal obligation)
- Objects to direct marketing → **must stop** (absolute)
- **Trap:** fulfill only **after verifying identity**.

**Hook**

**"I want to SEE it, FIX it, DELETE it, TAKE it, PAUSE it, or say STOP."** → access, rectification, erasure, portability, restriction, objection.

**Quick check:** Someone claiming to be a customer emails support asking for a full copy of their data sent to a NEW email address. What first?

**Answer:** Verify identity first (correct). Use what is on file (log in / original email), not the new address; new-address request is a red flag (social engineering/pretexting). Pre-test Q5 portability correct.

</details>

<a name="t-3-4-6"></a>
**Marketing preferences and third-party sharing**

Opt-in vs opt-out; controls on sharing with partners; clear terms of service.

> On the exam: Opt-in: user actively agrees (GDPR generally requires this for marketing). Opt-out: included until they say no.
Third-party sharing must be disclosed and controlled by contract. Terms of service and privacy notices must be clear.
Scenario cue: 'a pre-ticked marketing checkbox' → not valid consent under GDPR.

<details><summary>Lesson (17 Oct 2026)</summary>

**Marketing preferences and third-party sharing**

Core from the pre-test: **pre-ticked box = opt-out = not valid GDPR consent.**

**Opt-in vs opt-out**

- **Opt-in:** person takes an **active step** to say yes (ticks an **empty** box); nothing happens unless they agree. Required by **GDPR** (+ EU ePrivacy) for most marketing emails/cookies.
- **Opt-out:** included **by default**; must act to say no (untick, unsubscribe). Allowed for US commercial email under **CAN-SPAM** (working unsubscribe honored within **10 business days**).
- **Opt-in is stronger**; when in doubt, opt-in is the privacy-friendly answer.

**Marketing preference requirements**

- **Preference center:** choose what (newsletters, offers, SMS) and how, separately.
- **Unsubscribe works everywhere:** sync across CRM, email, SMS **and partners**.
- **Record consent:** who, when, what, which wording version.
- **No dark patterns:** tiny gray "no," double negatives, harder opt-out than opt-in = **invalid consent**.

**Third-party sharing**

- **Disclosure:** privacy notice says **who** and **why**.
- **Legal basis/consent:** selling/sharing for partners' marketing usually needs **consent** (EU) or an **opt-out right** (California **"Do Not Sell or Share My Personal Information"**, CCPA/CPRA).
- **Contracts:** **data processing agreement (DPA)** limiting what vendors do (controller decides, processor follows); require partners to **stop and delete** on opt-out.
- **Minimization in sharing:** only the fields they need.
- **Clear terms:** plain-language terms and notice → **informed** consent.

**On the exam**

- Pre-ticked partner-offers box → **opt-out** → invalid GDPR consent
- Unsubscribed from email but still gets SMS from another system → **preferences not synced**
- California users stop sale of data → **"Do Not Sell or Share"** opt-out
- Contract limiting vendor's use → **DPA**
- **Trap:** dark pattern = **invalid consent**

**Worked example (quick check)**

User unsubscribes; two weeks later a partner emails offers using shared data → (1) **sync opt-outs everywhere incl. partners**; (2) **control sharing**: consent / Do Not Sell, DPA limiting use + stop/delete on opt-out.

**Hook**

**Opt-in = the door is closed until they open it. Opt-out = the door is open until they close it.** Privacy prefers closed doors.

**Quick check:** User unsubscribes; two weeks later store partner emails offers using shared data. Two requirements the store missed?

**Answer:** Gave one: opt-out not synced across systems. Second: control third-party sharing (consent / Do Not Sell + DPA requiring partner to stop and delete). Pre-test Q6 opt-out correct.

</details>

<a name="t-3-4-7"></a>
**Data retention**

How long, where, and what is kept; delete when no longer needed.

> On the exam: Define how long each data type is kept, where (location and system) and what exactly is kept, then delete it when the period ends.
Why it matters: keeping data longer than needed increases breach impact and legal risk.
Trap: legal holds override retention schedules.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data retention + Cross-border requirements (taught together)**

Retention = **how long** data lives; cross-border = **where** it lives and **whose laws** follow it.

**Part 1: Data retention**

**Both directions:**

- **Minimum:** keep some records **at least** a set time (tax/financial 7 years, HIPAA documentation 6 years). Deleting too early breaks the law.
- **Maximum:** privacy laws require deleting personal data **once no longer needed**. Keeping too long breaks the law (**storage limitation**).
- **Retention schedule** (2.6) sets both per data type: what, where, how long, what happens at the end.

**Requirements:**

- **Automatic deletion** (scheduled purge job).
- **Cover every copy:** backups, logs, warehouses, exports, unstructured files. Backups: delete from them or let them **expire** on a short rotation.
- **Legal hold overrides deletion.**
- **Record the deletion** as evidence.

**Part 2: Cross-border requirements**

- **Data residency:** **where** data is **physically stored** (often a business choice: Frankfurt region).
- **Data sovereignty:** **whose laws apply**. Usually the storage country, but it can **follow the company that controls it**: the **US CLOUD Act** can reach data held by **US-owned** providers **even when stored abroad**.
- **Data localization:** a **legal requirement** that data **must stay inside** a country.

**Transfer mechanisms (EU personal data abroad):**

- **Adequacy decision:** EU rules a country adequate (UK, Japan, Canada commercial) → free flow.
- **Standard Contractual Clauses (SCCs):** EU-approved contract terms; most common.
- **Binding Corporate Rules (BCRs):** approved internal rules **within one multinational group**.
- **EU–US Data Privacy Framework (2023):** self-certifying US companies; replaced **Privacy Shield**, struck down in **2020 (Schrems II)**.
- SCCs often need a **transfer impact assessment** (do destination laws, e.g. surveillance, undermine protection?).

**Requirements:** choose **cloud regions** deliberately; make sure **backups, replicas, logs, support access** don't quietly cross borders; **map data flows**; put mechanisms in place **before** sending.

**On the exam**

- Delete when no longer needed → **storage limitation/retention** · keep 7 years → **minimum retention**
- Where physically stored → **residency** · whose laws govern → **sovereignty** · must stay in-country → **localization**
- EU data to non-adequate country → **SCCs** (BCRs within a group)
- Struck down Privacy Shield → **Schrems II (2020)** → **Data Privacy Framework (2023)**
- **Trap:** EU region ≠ only EU law (sovereignty can follow the company: CLOUD Act).

**Worked examples (quick check)**

1. Policy says delete 2 years after closure; purge only cleans main DB, backups kept forever → backups must be purged/expire; otherwise the promise is false (storage limitation).

2. German company, US-owned cloud, Frankfurt data center → **sovereignty**: US law (CLOUD Act) may reach it because the provider is US-owned.

**Hooks**

Retention: **"Not too short, not too long, and every copy."**

Cross-border: **Residency = where it sleeps. Sovereignty = whose rules it lives under. Localization = it's not allowed to leave home.**

**Quick check:** (1) Purge job cleans main DB only; backups kept indefinitely. Problem? (2) German company, US-owned cloud, Frankfurt DC: which concept explains US law reaching the data?

**Answer:** Backups must be purged too: correct. Pre-test Q7 correct.

</details>

<a name="t-3-4-8"></a>
**Cross-border requirements**

Data residency (where stored), sovereignty (whose laws apply), transfer mechanisms.

> On the exam: May require storing data in-country or using approved transfer mechanisms such as standard contractual clauses.

<details><summary>Lesson (17 Oct 2026)</summary>

**Data retention + Cross-border requirements (taught together)**

Retention = **how long** data lives; cross-border = **where** it lives and **whose laws** follow it.

**Part 1: Data retention**

**Both directions:**

- **Minimum:** keep some records **at least** a set time (tax/financial 7 years, HIPAA documentation 6 years). Deleting too early breaks the law.
- **Maximum:** privacy laws require deleting personal data **once no longer needed**. Keeping too long breaks the law (**storage limitation**).
- **Retention schedule** (2.6) sets both per data type: what, where, how long, what happens at the end.

**Requirements:**

- **Automatic deletion** (scheduled purge job).
- **Cover every copy:** backups, logs, warehouses, exports, unstructured files. Backups: delete from them or let them **expire** on a short rotation.
- **Legal hold overrides deletion.**
- **Record the deletion** as evidence.

**Part 2: Cross-border requirements**

- **Data residency:** **where** data is **physically stored** (often a business choice: Frankfurt region).
- **Data sovereignty:** **whose laws apply**. Usually the storage country, but it can **follow the company that controls it**: the **US CLOUD Act** can reach data held by **US-owned** providers **even when stored abroad**.
- **Data localization:** a **legal requirement** that data **must stay inside** a country.

**Transfer mechanisms (EU personal data abroad):**

- **Adequacy decision:** EU rules a country adequate (UK, Japan, Canada commercial) → free flow.
- **Standard Contractual Clauses (SCCs):** EU-approved contract terms; most common.
- **Binding Corporate Rules (BCRs):** approved internal rules **within one multinational group**.
- **EU–US Data Privacy Framework (2023):** self-certifying US companies; replaced **Privacy Shield**, struck down in **2020 (Schrems II)**.
- SCCs often need a **transfer impact assessment** (do destination laws, e.g. surveillance, undermine protection?).

**Requirements:** choose **cloud regions** deliberately; make sure **backups, replicas, logs, support access** don't quietly cross borders; **map data flows**; put mechanisms in place **before** sending.

**On the exam**

- Delete when no longer needed → **storage limitation/retention** · keep 7 years → **minimum retention**
- Where physically stored → **residency** · whose laws govern → **sovereignty** · must stay in-country → **localization**
- EU data to non-adequate country → **SCCs** (BCRs within a group)
- Struck down Privacy Shield → **Schrems II (2020)** → **Data Privacy Framework (2023)**
- **Trap:** EU region ≠ only EU law (sovereignty can follow the company: CLOUD Act).

**Worked examples (quick check)**

1. Policy says delete 2 years after closure; purge only cleans main DB, backups kept forever → backups must be purged/expire; otherwise the promise is false (storage limitation).

2. German company, US-owned cloud, Frankfurt data center → **sovereignty**: US law (CLOUD Act) may reach it because the provider is US-owned.

**Hooks**

Retention: **"Not too short, not too long, and every copy."**

Cross-border: **Residency = where it sleeps. Sovereignty = whose rules it lives under. Localization = it's not allowed to leave home.**

**Quick check:** (1) Purge job cleans main DB only; backups kept indefinitely. Problem? (2) German company, US-owned cloud, Frankfurt DC: which concept explains US law reaching the data?

**Answer:** Said laws apply where data is stored (would point to German law); missed the twist + term: SOVEREIGNTY can follow the US-owned provider (CLOUD Act). Pre-test Q8 SCCs correct. Marked shaky.

</details>

<a name="t-3-4-9"></a>
**Privacy by design**

Build privacy in from the start; privacy as the default setting.

> On the exam: Seven principles: proactive not reactive; privacy as the default; privacy embedded in design; full functionality (not a trade-off); end-to-end lifecycle protection; visibility and transparency; respect for the user.
Scenario cue: 'privacy settings are set to share by default' → violates privacy by default.

<details><summary>Lesson (17 Oct 2026)</summary>

**Privacy by design + PIA / DPIA (taught together)**

**Privacy by design (PbD)**

Build privacy in **from the start** (requirements, design), not bolted on. **Ann Cavoukian**'s **7 principles**:

- **Proactive, not reactive** · **Privacy as the default** (most private settings on by default) · **Embedded into design** · **Full functionality** (privacy AND features) · **End-to-end security** (whole lifecycle) · **Visibility and transparency** · **Respect for the user**

GDPR makes it law: **"data protection by design and by default."**

**PIA / DPIA**

Formal **assessment of privacy risks BEFORE processing**, so problems are fixed in design.

- **PIA** = general term. **DPIA** = GDPR version, **mandatory** when processing is **likely high risk** (large-scale sensitive data, systematic monitoring, location tracking, profiling, biometrics).
- **Contents:** what data and why; **necessary and proportionate?**; risks to people; **safeguards**.
- **Link:** PbD = the **principle**; PIA/DPIA = the **process** that checks it.

**On the exam**

- Most private settings by default → **privacy by default**
- Assess privacy risks before high-risk processing → **DPIA**
- When? → **early, before processing / during design**
- **Trap:** a PIA done after launch defeats its purpose.

**Worked example (quick check)**

Facial recognition in stores to track repeat shoppers → **DPIA before launch, mandatory** (biometric special category + systematic monitoring = high risk), plus privacy by design.

**Hook**

**PbD = bake it in. DPIA = taste-test before serving.**

**Quick check:** Store facial recognition to track repeat shoppers: what must it do before launch under GDPR, why?

**Answer:** Bake it in (PbD) + taste (DPIA). Exam answer: mandatory DPIA before launch (biometrics + systematic monitoring = high risk). Pre-test Q9, Q10 correct.

</details>

<a name="t-3-4-10"></a>
**Privacy impact assessment (PIA / DPIA)**

Assess privacy risks before processing personal data.

> On the exam: What it is: an assessment of privacy risks of a new system or processing, done early in requirements and design. GDPR requires a DPIA for high-risk processing.
Scenario cue: 'a new app will process health data at large scale' → perform a DPIA before building.

<details><summary>Lesson (17 Oct 2026)</summary>

**Privacy by design + PIA / DPIA (taught together)**

**Privacy by design (PbD)**

Build privacy in **from the start** (requirements, design), not bolted on. **Ann Cavoukian**'s **7 principles**:

- **Proactive, not reactive** · **Privacy as the default** (most private settings on by default) · **Embedded into design** · **Full functionality** (privacy AND features) · **End-to-end security** (whole lifecycle) · **Visibility and transparency** · **Respect for the user**

GDPR makes it law: **"data protection by design and by default."**

**PIA / DPIA**

Formal **assessment of privacy risks BEFORE processing**, so problems are fixed in design.

- **PIA** = general term. **DPIA** = GDPR version, **mandatory** when processing is **likely high risk** (large-scale sensitive data, systematic monitoring, location tracking, profiling, biometrics).
- **Contents:** what data and why; **necessary and proportionate?**; risks to people; **safeguards**.
- **Link:** PbD = the **principle**; PIA/DPIA = the **process** that checks it.

**On the exam**

- Most private settings by default → **privacy by default**
- Assess privacy risks before high-risk processing → **DPIA**
- When? → **early, before processing / during design**
- **Trap:** a PIA done after launch defeats its purpose.

**Worked example (quick check)**

Facial recognition in stores to track repeat shoppers → **DPIA before launch, mandatory** (biometric special category + systematic monitoring = high risk), plus privacy by design.

**Hook**

**PbD = bake it in. DPIA = taste-test before serving.**

**Quick check:** Store facial recognition to track repeat shoppers: what must it do before launch under GDPR, why?

**Answer:** Bake it in (PbD) + taste (DPIA). Exam answer: mandatory DPIA before launch (biometrics + systematic monitoring = high risk). Pre-test Q9, Q10 correct.

</details>

## 3.5 Data access provisioning

<a name="t-3-5-1"></a>
**User provisioning**

Joiner, mover, leaver process; remove access promptly on exit.

> On the exam: Joiner: grant only needed access. Mover: remove old access when roles change. Leaver: remove all access immediately on exit.
Scenario cue: 'a former employee still logs in' → leaver process failure.
Best practice: automate provisioning from HR records.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.5 Data access provisioning (all 4 topics taught together)**

Who gets access, and making sure it doesn't pile up.

**1. User provisioning: Joiner, Mover, Leaver (JML)**

- **Joiner:** only what the role needs, approved by manager (+ **data owner** for sensitive data), ideally via **RBAC** (access comes with the role).
- **Mover:** gets the **new** access **and loses the old**. Most often skipped.
- **Leaver:** **disable all access immediately** (accounts, VPN, badges, SaaS, API keys), ideally **automated** from HR.
- **Deprovisioning** = formal word for removing access.

**2. Service accounts (non-human: apps, scripts, jobs)**

- **Least privilege** · **no interactive login** · **credentials in a vault, rotated** · **named human owner** (else orphaned, like `svc_reporting` in 2.6).

**3. Reapproval / access recertification**

- **Periodic reviews** (e.g. quarterly): managers/data owners **confirm each person still needs access**; remove the rest.
- The **safety net** for what JML missed.
- **Rubber-stamping** ("approve all" without checking) defeats it.

**4. Privilege creep**

- Access **piling up** as people move roles. Fixed by a proper **Mover** step + **recertification**.

**On the exam**

- Moved from Finance to Sales, still has Finance access → **privilege creep** from a missed **Mover** step
- Fired employee's account active a week later → failed **Leaver / deprovisioning**
- Quarterly manager review of access → **access recertification**
- Account for a nightly batch job → **service account** (least privilege, no interactive login, rotated, owned)
- **Trap:** "approve all" recertification = weakness

**Hook**

**Joiner = give only what's needed. Mover = swap, don't stack. Leaver = cut everything, fast.** Recertification = the yearly checkup.

**Quick check:** HR specialist moves to Marketing; 6 months later she can still view all salaries. What failed, what should catch it?

**Answer:** Mover step failed (old access not removed) -> privilege creep; recertification should catch it. Correct.

</details>

<a name="t-3-5-2"></a>
**Service accounts**

Non-human accounts: least privilege, no interactive login, rotated credentials, an owner.

> On the exam: Classic scenario: shared admin service account with its password in a config file → use a vault or managed identity, least privilege, rotation.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.5 Data access provisioning (all 4 topics taught together)**

Who gets access, and making sure it doesn't pile up.

**1. User provisioning: Joiner, Mover, Leaver (JML)**

- **Joiner:** only what the role needs, approved by manager (+ **data owner** for sensitive data), ideally via **RBAC** (access comes with the role).
- **Mover:** gets the **new** access **and loses the old**. Most often skipped.
- **Leaver:** **disable all access immediately** (accounts, VPN, badges, SaaS, API keys), ideally **automated** from HR.
- **Deprovisioning** = formal word for removing access.

**2. Service accounts (non-human: apps, scripts, jobs)**

- **Least privilege** · **no interactive login** · **credentials in a vault, rotated** · **named human owner** (else orphaned, like `svc_reporting` in 2.6).

**3. Reapproval / access recertification**

- **Periodic reviews** (e.g. quarterly): managers/data owners **confirm each person still needs access**; remove the rest.
- The **safety net** for what JML missed.
- **Rubber-stamping** ("approve all" without checking) defeats it.

**4. Privilege creep**

- Access **piling up** as people move roles. Fixed by a proper **Mover** step + **recertification**.

**On the exam**

- Moved from Finance to Sales, still has Finance access → **privilege creep** from a missed **Mover** step
- Fired employee's account active a week later → failed **Leaver / deprovisioning**
- Quarterly manager review of access → **access recertification**
- Account for a nightly batch job → **service account** (least privilege, no interactive login, rotated, owned)
- **Trap:** "approve all" recertification = weakness

**Hook**

**Joiner = give only what's needed. Mover = swap, don't stack. Leaver = cut everything, fast.** Recertification = the yearly checkup.

**Quick check:** HR specialist moves to Marketing; 6 months later she can still view all salaries. What failed, what should catch it?

**Answer:** Mover step failed (old access not removed) -> privilege creep; recertification should catch it. Correct.

</details>

<a name="t-3-5-3"></a>
**Reapproval / access recertification**

Periodic reviews to confirm access is still needed.

> On the exam: What it is: periodic review (e.g., quarterly) where managers or data owners confirm each person's access is still needed.
Scenario cue: 'how do you detect access that's no longer needed?' → access recertification.
Catches: privilege creep, orphaned accounts, toxic combinations violating separation of duties.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.5 Data access provisioning (all 4 topics taught together)**

Who gets access, and making sure it doesn't pile up.

**1. User provisioning: Joiner, Mover, Leaver (JML)**

- **Joiner:** only what the role needs, approved by manager (+ **data owner** for sensitive data), ideally via **RBAC** (access comes with the role).
- **Mover:** gets the **new** access **and loses the old**. Most often skipped.
- **Leaver:** **disable all access immediately** (accounts, VPN, badges, SaaS, API keys), ideally **automated** from HR.
- **Deprovisioning** = formal word for removing access.

**2. Service accounts (non-human: apps, scripts, jobs)**

- **Least privilege** · **no interactive login** · **credentials in a vault, rotated** · **named human owner** (else orphaned, like `svc_reporting` in 2.6).

**3. Reapproval / access recertification**

- **Periodic reviews** (e.g. quarterly): managers/data owners **confirm each person still needs access**; remove the rest.
- The **safety net** for what JML missed.
- **Rubber-stamping** ("approve all" without checking) defeats it.

**4. Privilege creep**

- Access **piling up** as people move roles. Fixed by a proper **Mover** step + **recertification**.

**On the exam**

- Moved from Finance to Sales, still has Finance access → **privilege creep** from a missed **Mover** step
- Fired employee's account active a week later → failed **Leaver / deprovisioning**
- Quarterly manager review of access → **access recertification**
- Account for a nightly batch job → **service account** (least privilege, no interactive login, rotated, owned)
- **Trap:** "approve all" recertification = weakness

**Hook**

**Joiner = give only what's needed. Mover = swap, don't stack. Leaver = cut everything, fast.** Recertification = the yearly checkup.

**Quick check:** HR specialist moves to Marketing; 6 months later she can still view all salaries. What failed, what should catch it?

**Answer:** Mover step failed (old access not removed) -> privilege creep; recertification should catch it. Correct.

</details>

<a name="t-3-5-4"></a>
**Privilege creep**

Accumulating rights over time as people change roles.

> On the exam: What it is: users keep collecting rights as they change jobs, without losing old ones.
Scenario cue: 'an employee who moved departments still has finance access' → privilege creep.
Fix: remove access on role change (mover process), RBAC, regular reviews.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.5 Data access provisioning (all 4 topics taught together)**

Who gets access, and making sure it doesn't pile up.

**1. User provisioning: Joiner, Mover, Leaver (JML)**

- **Joiner:** only what the role needs, approved by manager (+ **data owner** for sensitive data), ideally via **RBAC** (access comes with the role).
- **Mover:** gets the **new** access **and loses the old**. Most often skipped.
- **Leaver:** **disable all access immediately** (accounts, VPN, badges, SaaS, API keys), ideally **automated** from HR.
- **Deprovisioning** = formal word for removing access.

**2. Service accounts (non-human: apps, scripts, jobs)**

- **Least privilege** · **no interactive login** · **credentials in a vault, rotated** · **named human owner** (else orphaned, like `svc_reporting` in 2.6).

**3. Reapproval / access recertification**

- **Periodic reviews** (e.g. quarterly): managers/data owners **confirm each person still needs access**; remove the rest.
- The **safety net** for what JML missed.
- **Rubber-stamping** ("approve all" without checking) defeats it.

**4. Privilege creep**

- Access **piling up** as people move roles. Fixed by a proper **Mover** step + **recertification**.

**On the exam**

- Moved from Finance to Sales, still has Finance access → **privilege creep** from a missed **Mover** step
- Fired employee's account active a week later → failed **Leaver / deprovisioning**
- Quarterly manager review of access → **access recertification**
- Account for a nightly batch job → **service account** (least privilege, no interactive login, rotated, owned)
- **Trap:** "approve all" recertification = weakness

**Hook**

**Joiner = give only what's needed. Mover = swap, don't stack. Leaver = cut everything, fast.** Recertification = the yearly checkup.

**Quick check:** HR specialist moves to Marketing; 6 months later she can still view all salaries. What failed, what should catch it?

**Answer:** Mover step failed (old access not removed) -> privilege creep; recertification should catch it. Correct.

</details>

## 3.6 Misuse and abuse cases

<a name="t-3-6-1"></a>
**Misuse case** (review)

How an actor could misuse the system, intentionally or by accident.

> On the exam: What it is: describes how someone could misuse the system, deliberately or by mistake, written next to the normal use case.
Why it matters: turns 'what could go wrong' into concrete security requirements and test cases.
Scenario cue: 'how do you capture security requirements from an attacker's view during requirements?' → misuse cases.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.6 Misuse and abuse cases (all 4 taught together)**

Thinking like an attacker **during requirements**.

**1. Misuse case**

How someone could **misuse** the system, **on purpose OR by accident**.

- Accidental: 5 GB upload crashes the server; typo deletes the wrong record; nurse opens the wrong patient.
- Intentional: attacker tries thousands of passwords.
- Drawn as the **mirror of a use case** (normal actor vs **mis-actor**).

**2. Abuse case**

**Intentional, malicious** only, from the **attacker's** view (like the evil user story, 3.1).

- *"As an attacker, I change the account ID in the URL to see other customers' orders."*

**Difference:** misuse = accidental or intentional; abuse = always malicious. Every abuse case is a misuse case, not vice versa.

**3. Mitigating control identification**

Every misuse/abuse case must lead to a **security requirement or control** (in requirements, BEFORE code exists; not a patch, which comes after release).

- Password guessing → lockout + rate limiting + MFA
- ID changed in URL → server-side authorization on every request
- 5 GB upload → size limit + input validation
- Nurse/wrong patient → show photo + DOB, require confirmation

A misuse case with no control is unfinished.

**4. Attack trees**

Attacker's **goal** at the **root**, branches = all the ways to reach it.

- Root "Steal customer data" → SQL injection | phish an admin (fake email, fake support call) | steal a backup tape
- **OR** branches = any one path works; **AND** = all steps needed together.
- See every path; control the cheapest/easiest first.

**On the exam**

- Accidental or intentional misuse → **misuse case** · malicious, attacker's view → **abuse case**
- Goal at root, ways as branches → **attack tree**
- Purpose of a misuse case → **find security requirements/controls**
- **Trap:** abuse = always malicious; misuse can be an accident.

**Hooks**

**Misuse = "oops or evil." Abuse = "evil only." Attack tree = the attacker's family tree of options.** **Misuse case in → security requirement out.**

**Quick check:** (1) Nurse accidentally views wrong patient record: misuse or abuse? (2) What should come out of every misuse case?

**Answer:** Nurse opens wrong record by accident = misuse case. Correct.

</details>

<a name="t-3-6-2"></a>
**Abuse case**

Intentional, malicious use, from the attacker's point of view.

> On the exam: What it is: an intentional, malicious use of the system described step by step from the attacker's side.
Why it matters: shows exactly which controls are needed and which negative tests QA should run.
Note: the exam often uses misuse and abuse cases almost interchangeably.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.6 Misuse and abuse cases (all 4 taught together)**

Thinking like an attacker **during requirements**.

**1. Misuse case**

How someone could **misuse** the system, **on purpose OR by accident**.

- Accidental: 5 GB upload crashes the server; typo deletes the wrong record; nurse opens the wrong patient.
- Intentional: attacker tries thousands of passwords.
- Drawn as the **mirror of a use case** (normal actor vs **mis-actor**).

**2. Abuse case**

**Intentional, malicious** only, from the **attacker's** view (like the evil user story, 3.1).

- *"As an attacker, I change the account ID in the URL to see other customers' orders."*

**Difference:** misuse = accidental or intentional; abuse = always malicious. Every abuse case is a misuse case, not vice versa.

**3. Mitigating control identification**

Every misuse/abuse case must lead to a **security requirement or control** (in requirements, BEFORE code exists; not a patch, which comes after release).

- Password guessing → lockout + rate limiting + MFA
- ID changed in URL → server-side authorization on every request
- 5 GB upload → size limit + input validation
- Nurse/wrong patient → show photo + DOB, require confirmation

A misuse case with no control is unfinished.

**4. Attack trees**

Attacker's **goal** at the **root**, branches = all the ways to reach it.

- Root "Steal customer data" → SQL injection | phish an admin (fake email, fake support call) | steal a backup tape
- **OR** branches = any one path works; **AND** = all steps needed together.
- See every path; control the cheapest/easiest first.

**On the exam**

- Accidental or intentional misuse → **misuse case** · malicious, attacker's view → **abuse case**
- Goal at root, ways as branches → **attack tree**
- Purpose of a misuse case → **find security requirements/controls**
- **Trap:** abuse = always malicious; misuse can be an accident.

**Hooks**

**Misuse = "oops or evil." Abuse = "evil only." Attack tree = the attacker's family tree of options.** **Misuse case in → security requirement out.**

**Quick check:** (1) Nurse accidentally views wrong patient record: misuse or abuse? (2) What should come out of every misuse case?

**Answer:** Correct (accident = misuse, not abuse).

</details>

<a name="t-3-6-3"></a>
**Mitigating control identification** (review)

Each misuse case leads to a security requirement or control.

> On the exam: What it is: for every misuse case, decide which control prevents or detects it, and add it as a requirement.
Chain: misuse case → mitigating control → requirement → test case, tracked in the traceability matrix.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.6 Misuse and abuse cases (all 4 taught together)**

Thinking like an attacker **during requirements**.

**1. Misuse case**

How someone could **misuse** the system, **on purpose OR by accident**.

- Accidental: 5 GB upload crashes the server; typo deletes the wrong record; nurse opens the wrong patient.
- Intentional: attacker tries thousands of passwords.
- Drawn as the **mirror of a use case** (normal actor vs **mis-actor**).

**2. Abuse case**

**Intentional, malicious** only, from the **attacker's** view (like the evil user story, 3.1).

- *"As an attacker, I change the account ID in the URL to see other customers' orders."*

**Difference:** misuse = accidental or intentional; abuse = always malicious. Every abuse case is a misuse case, not vice versa.

**3. Mitigating control identification**

Every misuse/abuse case must lead to a **security requirement or control** (in requirements, BEFORE code exists; not a patch, which comes after release).

- Password guessing → lockout + rate limiting + MFA
- ID changed in URL → server-side authorization on every request
- 5 GB upload → size limit + input validation
- Nurse/wrong patient → show photo + DOB, require confirmation

A misuse case with no control is unfinished.

**4. Attack trees**

Attacker's **goal** at the **root**, branches = all the ways to reach it.

- Root "Steal customer data" → SQL injection | phish an admin (fake email, fake support call) | steal a backup tape
- **OR** branches = any one path works; **AND** = all steps needed together.
- See every path; control the cheapest/easiest first.

**On the exam**

- Accidental or intentional misuse → **misuse case** · malicious, attacker's view → **abuse case**
- Goal at root, ways as branches → **attack tree**
- Purpose of a misuse case → **find security requirements/controls**
- **Trap:** abuse = always malicious; misuse can be an accident.

**Hooks**

**Misuse = "oops or evil." Abuse = "evil only." Attack tree = the attacker's family tree of options.** **Misuse case in → security requirement out.**

**Quick check:** (1) Nurse accidentally views wrong patient record: misuse or abuse? (2) What should come out of every misuse case?

**Answer:** Said "security patches". Output is a security REQUIREMENT / mitigating control (requirements phase, before code); patches come after release. Marked shaky.

</details>

<a name="t-3-6-4"></a>
**Attack trees**

Tree of an attacker's goal broken into ways to achieve it.

> On the exam: What it is: diagram with the attacker's goal at the root; branches show ways to reach it (AND/OR nodes); leaves are concrete steps.
Why it matters: helps find the easiest or cheapest attack path and where one control blocks many paths.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.6 Misuse and abuse cases (all 4 taught together)**

Thinking like an attacker **during requirements**.

**1. Misuse case**

How someone could **misuse** the system, **on purpose OR by accident**.

- Accidental: 5 GB upload crashes the server; typo deletes the wrong record; nurse opens the wrong patient.
- Intentional: attacker tries thousands of passwords.
- Drawn as the **mirror of a use case** (normal actor vs **mis-actor**).

**2. Abuse case**

**Intentional, malicious** only, from the **attacker's** view (like the evil user story, 3.1).

- *"As an attacker, I change the account ID in the URL to see other customers' orders."*

**Difference:** misuse = accidental or intentional; abuse = always malicious. Every abuse case is a misuse case, not vice versa.

**3. Mitigating control identification**

Every misuse/abuse case must lead to a **security requirement or control** (in requirements, BEFORE code exists; not a patch, which comes after release).

- Password guessing → lockout + rate limiting + MFA
- ID changed in URL → server-side authorization on every request
- 5 GB upload → size limit + input validation
- Nurse/wrong patient → show photo + DOB, require confirmation

A misuse case with no control is unfinished.

**4. Attack trees**

Attacker's **goal** at the **root**, branches = all the ways to reach it.

- Root "Steal customer data" → SQL injection | phish an admin (fake email, fake support call) | steal a backup tape
- **OR** branches = any one path works; **AND** = all steps needed together.
- See every path; control the cheapest/easiest first.

**On the exam**

- Accidental or intentional misuse → **misuse case** · malicious, attacker's view → **abuse case**
- Goal at root, ways as branches → **attack tree**
- Purpose of a misuse case → **find security requirements/controls**
- **Trap:** abuse = always malicious; misuse can be an accident.

**Hooks**

**Misuse = "oops or evil." Abuse = "evil only." Attack tree = the attacker's family tree of options.** **Misuse case in → security requirement out.**

**Quick check:** (1) Nurse accidentally views wrong patient record: misuse or abuse? (2) What should come out of every misuse case?

**Answer:** Taught; not directly tested.

</details>

## 3.7 Security requirements traceability matrix

<a name="t-3-7-1"></a>
**SRTM / RTM**

Maps each requirement to design, code and test cases.

> On the exam: What it is: a table linking each requirement to its design element, code module and test cases.
Why it matters: proves every security requirement was built and tested, shows the impact of changes, supports audits.
Scenario cue: 'how do you confirm all security requirements were tested?' → requirements traceability matrix.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.7 Security requirements traceability matrix (all 3 taught together)**

Proving every requirement got built and tested, and nothing extra sneaked in.

**1. SRTM / RTM (RTM from 2.4)**

- **Table** linking each requirement → **design** → **code** → **test cases**; SRTM = security-focused.
- Row: `SR-07: Lock after 5 failed logins` → design §4.2 → `AuthService.lockout()` → TC-112.
- **Evidence** for auditors; shows **gaps** (requirement with no test case).

**2. Bidirectional traceability**

- **Forward** (requirement → test): every requirement designed, built, tested. Catches **MISSED** requirements.
- **Backward** (feature/code → requirement): every feature traces back to a requirement. Catches **UNREQUESTED EXTRAS**.

**3. Gold plating vs scope creep**

- **Gold plating** = **developers add** features nobody asked for. Extra = **untested attack surface**.
- **Scope creep** = **requirements keep growing** (usually stakeholders) **without change control**.
- Both appear as **features with no requirement**.

**On the exam**

- Every security requirement tested → **SRTM / forward**
- Dev adds unrequested admin debug page → **gold plating**, caught by **backward**
- Stakeholders keep adding features without approval → **scope creep**
- **Trap:** extras aren't a bonus; they're unreviewed attack surface.

**Hook**

**Forward = nothing missing. Backward = nothing extra.** Gold plating = devs add; scope creep = requirements grow.

**Quick check:** Unrequested "export all users to CSV" button added by a developer to be helpful: name, which traceability direction caught it?

**Answer:** Correct.

</details>

<a name="t-3-7-2"></a>
**Bidirectional traceability**

Every requirement is tested, and every feature traces back to a requirement.

> On the exam: Forward traceability: requirement → design → code → test (nothing missed). Backward traceability: code or test → requirement (nothing extra).
Scenario cue: 'a feature exists in code that no requirement asked for' → found through backward traceability; may be a backdoor or gold plating.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.7 Security requirements traceability matrix (all 3 taught together)**

Proving every requirement got built and tested, and nothing extra sneaked in.

**1. SRTM / RTM (RTM from 2.4)**

- **Table** linking each requirement → **design** → **code** → **test cases**; SRTM = security-focused.
- Row: `SR-07: Lock after 5 failed logins` → design §4.2 → `AuthService.lockout()` → TC-112.
- **Evidence** for auditors; shows **gaps** (requirement with no test case).

**2. Bidirectional traceability**

- **Forward** (requirement → test): every requirement designed, built, tested. Catches **MISSED** requirements.
- **Backward** (feature/code → requirement): every feature traces back to a requirement. Catches **UNREQUESTED EXTRAS**.

**3. Gold plating vs scope creep**

- **Gold plating** = **developers add** features nobody asked for. Extra = **untested attack surface**.
- **Scope creep** = **requirements keep growing** (usually stakeholders) **without change control**.
- Both appear as **features with no requirement**.

**On the exam**

- Every security requirement tested → **SRTM / forward**
- Dev adds unrequested admin debug page → **gold plating**, caught by **backward**
- Stakeholders keep adding features without approval → **scope creep**
- **Trap:** extras aren't a bonus; they're unreviewed attack surface.

**Hook**

**Forward = nothing missing. Backward = nothing extra.** Gold plating = devs add; scope creep = requirements grow.

**Quick check:** Unrequested "export all users to CSV" button added by a developer to be helpful: name, which traceability direction caught it?

**Answer:** Did not name the direction: BACKWARD (feature → requirement) catches extras; forward catches missed requirements. Marked shaky.

</details>

<a name="t-3-7-3"></a>
**Gold plating / scope creep**

Features with no requirement show up as gaps in the matrix.

> On the exam: Gold plating: developers add features nobody asked for. Scope creep: requirements keep growing during the project.
Why it matters: unplanned features are untested and unreviewed, adding attack surface.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.7 Security requirements traceability matrix (all 3 taught together)**

Proving every requirement got built and tested, and nothing extra sneaked in.

**1. SRTM / RTM (RTM from 2.4)**

- **Table** linking each requirement → **design** → **code** → **test cases**; SRTM = security-focused.
- Row: `SR-07: Lock after 5 failed logins` → design §4.2 → `AuthService.lockout()` → TC-112.
- **Evidence** for auditors; shows **gaps** (requirement with no test case).

**2. Bidirectional traceability**

- **Forward** (requirement → test): every requirement designed, built, tested. Catches **MISSED** requirements.
- **Backward** (feature/code → requirement): every feature traces back to a requirement. Catches **UNREQUESTED EXTRAS**.

**3. Gold plating vs scope creep**

- **Gold plating** = **developers add** features nobody asked for. Extra = **untested attack surface**.
- **Scope creep** = **requirements keep growing** (usually stakeholders) **without change control**.
- Both appear as **features with no requirement**.

**On the exam**

- Every security requirement tested → **SRTM / forward**
- Dev adds unrequested admin debug page → **gold plating**, caught by **backward**
- Stakeholders keep adding features without approval → **scope creep**
- **Trap:** extras aren't a bonus; they're unreviewed attack surface.

**Hook**

**Forward = nothing missing. Backward = nothing extra.** Gold plating = devs add; scope creep = requirements grow.

**Quick check:** Unrequested "export all users to CSV" button added by a developer to be helpful: name, which traceability direction caught it?

**Answer:** Gold plating + attack surface. Correct.

</details>

## 3.8 Third-party vendor requirements

<a name="t-3-8-1"></a>
**Security requirements in contracts**

Secure development, testing, patching, breach notification, right to audit.

> On the exam: Typical requirements: secure development practices, testing evidence, vulnerability notification timelines, patch timelines, data protection, right to audit, breach notification, subcontractor rules.
Scenario cue: 'a vendor refuses to share test results after the contract is signed' → the requirement should have been in the contract.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.8 Third-party vendor requirements (both taught together)**

How you make vendors secure, and how you check they are.

**1. Security requirements in contracts**

In writing **before signing** (no leverage later; procurement 3.1):

- **Secure development** (secure SDLC, e.g. SSDF; tests code)
- **Patching SLA** (critical vulns fixed within X days)
- **Breach notification** to YOU within X hours (so you meet GDPR 72h)
- **Right to audit**
- **Data handling:** residency; return/deletion at end with certificate (2.6); **DPA** (3.4)
- **SBOM**
- **Flow-down** to their subcontractors

**2. Vendor assurance (proof)**

- **SOC 2:** independent auditor's report on security controls.
  - **Type I** = controls **designed** properly at **one point in time** (snapshot)
  - **Type II** = controls **worked over a period** (6–12 months) → **stronger**
  - **SOC 1** = financial reporting controls; **SOC 3** = short public summary
- **Certifications:** ISO 27001, PCI DSS, FedRAMP (US gov cloud)
- **Questionnaires:** SIG, CSA CAIQ
- **Attestations:** vendor formally states in writing it complies (SSDF attestation, 2.2)

**On the exam**

- Clause to inspect vendor security → **right to audit**
- Best evidence controls operated over time → **SOC 2 Type II**
- Designed properly at a single point → **SOC 2 Type I**
- Vendor tells you about breaches within 24h → **breach notification clause**
- **Trap:** Type II > Type I.

**Hook**

**Type I = a photo. Type II = a video.**

**Quick check:** Vendor A: SOC 2 Type I; Vendor B: SOC 2 Type II over 12 months. Stronger assurance?

**Answer:** Vendor B: track record over time. Correct.

</details>

<a name="t-3-8-2"></a>
**Vendor assurance**

SOC 2 reports, certifications, questionnaires, attestations.

> On the exam: Evidence types: independent audit reports (SOC 2 Type II, ISO 27001 certificate), pentest results, questionnaires, SBOMs, attestations (e.g., SSDF).
Scenario cue: 'which provides the strongest assurance about a vendor?' → an independent third-party audit over a period of time.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.8 Third-party vendor requirements (both taught together)**

How you make vendors secure, and how you check they are.

**1. Security requirements in contracts**

In writing **before signing** (no leverage later; procurement 3.1):

- **Secure development** (secure SDLC, e.g. SSDF; tests code)
- **Patching SLA** (critical vulns fixed within X days)
- **Breach notification** to YOU within X hours (so you meet GDPR 72h)
- **Right to audit**
- **Data handling:** residency; return/deletion at end with certificate (2.6); **DPA** (3.4)
- **SBOM**
- **Flow-down** to their subcontractors

**2. Vendor assurance (proof)**

- **SOC 2:** independent auditor's report on security controls.
  - **Type I** = controls **designed** properly at **one point in time** (snapshot)
  - **Type II** = controls **worked over a period** (6–12 months) → **stronger**
  - **SOC 1** = financial reporting controls; **SOC 3** = short public summary
- **Certifications:** ISO 27001, PCI DSS, FedRAMP (US gov cloud)
- **Questionnaires:** SIG, CSA CAIQ
- **Attestations:** vendor formally states in writing it complies (SSDF attestation, 2.2)

**On the exam**

- Clause to inspect vendor security → **right to audit**
- Best evidence controls operated over time → **SOC 2 Type II**
- Designed properly at a single point → **SOC 2 Type I**
- Vendor tells you about breaches within 24h → **breach notification clause**
- **Trap:** Type II > Type I.

**Hook**

**Type I = a photo. Type II = a video.**

**Quick check:** Vendor A: SOC 2 Type I; Vendor B: SOC 2 Type II over 12 months. Stronger assurance?

**Answer:** Vendor B: track record over time. Correct.

</details>

## 3.AI AI additions in the current outline

<a name="t-3-ai-1"></a>
**Excessive agency**

Requirements that stop AI agents from taking unauthorized autonomous actions.

> On the exam: What it is: giving an AI agent more permissions, tools or autonomy than it needs (an OWASP LLM risk).
Requirement examples: least-privilege tools, read-only by default, human approval for payments, deletions or emails.
Scenario cue: 'a chatbot can issue refunds without limits' → excessive agency.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.AI AI requirements (all 4 taught together)**

Writing requirements for AI features.

**1. Excessive agency (from 2.AI)**

Stop agents acting beyond what they should: **least privilege** for tools, **human approval** for high-impact actions (payments, deletions, email), action allow-list. *"Bot may look up orders; refunds over $50 need human approval."*

**2. Hallucination and bias thresholds (like AI build-break, 2.AI)**

**Non-functional** requirements with **numbers**, written early, testable. *"Hallucination &lt; 2% on eval set." "Approval rates across age groups differ ≤ 5%."* "Accurate and fair" alone is untestable.

**3. Function creep (new)**

AI use **quietly expands beyond its approved purpose**. *Visitor-counting camera reused to identify shoppers; car-counting traffic AI used by police to track people.*

- = **purpose limitation** (3.4) for AI. **Requirement:** document **approved scope**; any new use needs **new risk assessment / DPIA + approval**.
- vs **scope creep** (3.7): function creep = how an EXISTING system gets **used**; scope creep = new features being built.

**4. Abuse cases for jailbreaks and prompt injection**

Misuse/abuse cases (3.6) for AI: *"As an attacker, I trick the chatbot into ignoring its rules to reveal other customers' orders."* Each → a requirement: input/output filtering, no secrets in system prompts, least privilege, human approval, red-team testing.

- **Jailbreak** = trick model into breaking **safety rules**. **Prompt injection** = sneak in **instructions** overriding the developer's (direct/indirect).

**On the exam**

- Approved for one purpose, reused without review → **function creep**
- Cap on AI error rate → **hallucination threshold** (non-functional)
- Agent sends emails without approval → **excessive agency**
- Attacker-view chatbot scenario → **abuse case for prompt injection/jailbreak**

**Hook**

**Function creep = the AI's job description grows on its own.**

**Quick check:** Traffic AI approved to count cars; police later use it to track specific people, no review. Name + preventing requirement?

**Answer:** Function creep; purpose limitation (document approved scope; new use needs DPIA + approval). Correct.

</details>

<a name="t-3-ai-2"></a>
**Hallucination and bias thresholds**

Non-functional requirements setting acceptable error and bias rates.

> On the exam: What it is: measurable non-functional requirements like 'factual error rate under 2% on the evaluation set' or 'no group's approval rate differs by more than 5%'.
Why it matters: without a threshold nobody can test or enforce it.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.AI AI requirements (all 4 taught together)**

Writing requirements for AI features.

**1. Excessive agency (from 2.AI)**

Stop agents acting beyond what they should: **least privilege** for tools, **human approval** for high-impact actions (payments, deletions, email), action allow-list. *"Bot may look up orders; refunds over $50 need human approval."*

**2. Hallucination and bias thresholds (like AI build-break, 2.AI)**

**Non-functional** requirements with **numbers**, written early, testable. *"Hallucination &lt; 2% on eval set." "Approval rates across age groups differ ≤ 5%."* "Accurate and fair" alone is untestable.

**3. Function creep (new)**

AI use **quietly expands beyond its approved purpose**. *Visitor-counting camera reused to identify shoppers; car-counting traffic AI used by police to track people.*

- = **purpose limitation** (3.4) for AI. **Requirement:** document **approved scope**; any new use needs **new risk assessment / DPIA + approval**.
- vs **scope creep** (3.7): function creep = how an EXISTING system gets **used**; scope creep = new features being built.

**4. Abuse cases for jailbreaks and prompt injection**

Misuse/abuse cases (3.6) for AI: *"As an attacker, I trick the chatbot into ignoring its rules to reveal other customers' orders."* Each → a requirement: input/output filtering, no secrets in system prompts, least privilege, human approval, red-team testing.

- **Jailbreak** = trick model into breaking **safety rules**. **Prompt injection** = sneak in **instructions** overriding the developer's (direct/indirect).

**On the exam**

- Approved for one purpose, reused without review → **function creep**
- Cap on AI error rate → **hallucination threshold** (non-functional)
- Agent sends emails without approval → **excessive agency**
- Attacker-view chatbot scenario → **abuse case for prompt injection/jailbreak**

**Hook**

**Function creep = the AI's job description grows on its own.**

**Quick check:** Traffic AI approved to count cars; police later use it to track specific people, no review. Name + preventing requirement?

**Answer:** Function creep; purpose limitation (document approved scope; new use needs DPIA + approval). Correct.

</details>

<a name="t-3-ai-3"></a>
**Function creep**

AI use expanding beyond its scoped business case.

> On the exam: What it is: an AI system gradually gets used for things it wasn't designed or approved for.
Scenario cue: 'an FAQ bot now gives medical advice' → function creep; reassess risk and requirements.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.AI AI requirements (all 4 taught together)**

Writing requirements for AI features.

**1. Excessive agency (from 2.AI)**

Stop agents acting beyond what they should: **least privilege** for tools, **human approval** for high-impact actions (payments, deletions, email), action allow-list. *"Bot may look up orders; refunds over $50 need human approval."*

**2. Hallucination and bias thresholds (like AI build-break, 2.AI)**

**Non-functional** requirements with **numbers**, written early, testable. *"Hallucination &lt; 2% on eval set." "Approval rates across age groups differ ≤ 5%."* "Accurate and fair" alone is untestable.

**3. Function creep (new)**

AI use **quietly expands beyond its approved purpose**. *Visitor-counting camera reused to identify shoppers; car-counting traffic AI used by police to track people.*

- = **purpose limitation** (3.4) for AI. **Requirement:** document **approved scope**; any new use needs **new risk assessment / DPIA + approval**.
- vs **scope creep** (3.7): function creep = how an EXISTING system gets **used**; scope creep = new features being built.

**4. Abuse cases for jailbreaks and prompt injection**

Misuse/abuse cases (3.6) for AI: *"As an attacker, I trick the chatbot into ignoring its rules to reveal other customers' orders."* Each → a requirement: input/output filtering, no secrets in system prompts, least privilege, human approval, red-team testing.

- **Jailbreak** = trick model into breaking **safety rules**. **Prompt injection** = sneak in **instructions** overriding the developer's (direct/indirect).

**On the exam**

- Approved for one purpose, reused without review → **function creep**
- Cap on AI error rate → **hallucination threshold** (non-functional)
- Agent sends emails without approval → **excessive agency**
- Attacker-view chatbot scenario → **abuse case for prompt injection/jailbreak**

**Hook**

**Function creep = the AI's job description grows on its own.**

**Quick check:** Traffic AI approved to count cars; police later use it to track specific people, no review. Name + preventing requirement?

**Answer:** Function creep; purpose limitation (document approved scope; new use needs DPIA + approval). Correct.

</details>

<a name="t-3-ai-4"></a>
**Abuse cases for jailbreaks and prompt injection**

Misuse cases targeting chatbots and inference engines.

> On the exam: Example abuse cases: 'user tells chatbot to ignore its rules', 'hidden instruction in an uploaded document makes the AI leak data'.
Why it matters: they become requirements (input/output filtering, privilege limits) and test cases.

<details><summary>Lesson (18 Oct 2026)</summary>

**3.AI AI requirements (all 4 taught together)**

Writing requirements for AI features.

**1. Excessive agency (from 2.AI)**

Stop agents acting beyond what they should: **least privilege** for tools, **human approval** for high-impact actions (payments, deletions, email), action allow-list. *"Bot may look up orders; refunds over $50 need human approval."*

**2. Hallucination and bias thresholds (like AI build-break, 2.AI)**

**Non-functional** requirements with **numbers**, written early, testable. *"Hallucination &lt; 2% on eval set." "Approval rates across age groups differ ≤ 5%."* "Accurate and fair" alone is untestable.

**3. Function creep (new)**

AI use **quietly expands beyond its approved purpose**. *Visitor-counting camera reused to identify shoppers; car-counting traffic AI used by police to track people.*

- = **purpose limitation** (3.4) for AI. **Requirement:** document **approved scope**; any new use needs **new risk assessment / DPIA + approval**.
- vs **scope creep** (3.7): function creep = how an EXISTING system gets **used**; scope creep = new features being built.

**4. Abuse cases for jailbreaks and prompt injection**

Misuse/abuse cases (3.6) for AI: *"As an attacker, I trick the chatbot into ignoring its rules to reveal other customers' orders."* Each → a requirement: input/output filtering, no secrets in system prompts, least privilege, human approval, red-team testing.

- **Jailbreak** = trick model into breaking **safety rules**. **Prompt injection** = sneak in **instructions** overriding the developer's (direct/indirect).

**On the exam**

- Approved for one purpose, reused without review → **function creep**
- Cap on AI error rate → **hallucination threshold** (non-functional)
- Agent sends emails without approval → **excessive agency**
- Attacker-view chatbot scenario → **abuse case for prompt injection/jailbreak**

**Hook**

**Function creep = the AI's job description grows on its own.**

**Quick check:** Traffic AI approved to count cars; police later use it to track specific people, no review. Name + preventing requirement?

**Answer:** Function creep; purpose limitation (document approved scope; new use needs DPIA + approval). Correct.

</details>
