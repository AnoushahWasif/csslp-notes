# Domain 2: Secure Software Lifecycle Management

Exam weight: 11%

## 2.1 Security within a development methodology

<a name="t-2-1-1"></a>
**Waterfall**

Sequential phases. Security gates at each phase; changes late are expensive.

> On the exam: Security fits as formal reviews at each phase gate. Weakness: flaws found only in the testing phase are expensive to fix.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

A **linear, sequential** model: each phase is completed fully before the next starts, like water flowing down steps. Going back is difficult and expensive.

Phases: requirements → design → implementation → testing → deployment → maintenance.

**Strengths**

- Clear structure, milestones and documentation
- Easy to manage and audit
- Works well when requirements are **stable and well understood** (e.g., regulated, safety-critical, government contracts)

**Weaknesses**

- **Inflexible:** hard to change requirements later
- Working software appears **late**
- Problems found in testing are **expensive** (cost of fixing defects)
- Users may not see the product until it's nearly finished

**How security fits**

- **Formal security gates (checkpoints) at the end of each phase**:
- Requirements: security requirements approved
- Design: threat model and security design review approved
- Implementation: secure code review, SAST
- Testing: security testing, pentest
- Deployment: final security review, sign-off
- Strong documentation supports compliance and audits
- Risk: if security is skipped in early phases, it's found late (or never) and is costly to add

**On the exam**

- 'Stable, well-defined requirements; heavy documentation needed' → **Waterfall** fits
- 'Requirements expected to change often' → Waterfall is a **poor** fit (Agile/iterative better)
- Adding security to Waterfall → **phase gate reviews**
- **Trap:** late discovery of flaws is Waterfall's main security weakness

**Quick check:** A bank is building a regulatory reporting system whose requirements are fixed by law and won't change. Is Waterfall a good fit, and how should security be added to it?

**Answer:** **Yes, Waterfall fits:** requirements are fixed, well understood and heavily regulated, and the bank needs strong documentation. Add security through **formal gate reviews at each phase**: security requirements signed off before design, threat model approved before coding, code review/SAST before testing, security testing and a final security review before deployment. Risk: anything missed early is costly to fix late, so the requirements gate must be thorough.

</details>

<a name="t-2-1-2"></a>
**Agile / Scrum**

Short sprints. Add security user stories, abuse stories, and security in the definition of done.

> On the exam: No separate security phase; security goes into the backlog, acceptance criteria and definition of done. Scenario 'add security without slowing sprints' → security stories plus automated tests.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

An approach that delivers software in **short, repeated cycles** with constant feedback and change. Values (Agile Manifesto): individuals and interactions, working software, customer collaboration, responding to change.

**Scrum: the most common Agile framework**

- **Sprint:** fixed time-box, usually 1-4 weeks, producing a working increment
- **Product backlog:** prioritized list of everything to be built (as user stories)
- **Sprint backlog:** the items chosen for this sprint
- **Roles:** Product Owner (priorities), Scrum Master (process coach), Development Team
- **Events:** sprint planning, daily stand-up, sprint review (demo), retrospective (improve the process)
- **Definition of done (DoD):** the checklist an item must meet to count as finished

**Security challenges in Agile**

- No long separate 'security phase'; teams move fast
- Documentation is light, so security decisions can go unrecorded
- Security work loses priority against features

**How to build security into Agile**

- **Security user stories:** 'As a user, I want my session to expire after 15 minutes idle'
- **Abuse/evil user stories:** 'As an attacker, I want to reuse a stolen session token'
- **Security in the definition of done:** code reviewed, SAST/SCA passing, no high-severity findings, security tests pass
- **Lightweight threat modeling** each sprint for sensitive stories
- **Automated security testing** in the CI/CD pipeline
- **Security champions** in each team
- Security **non-functional requirements** as constraints applied to every story
- Security debt tracked in the backlog

**On the exam**

- 'How do you add security to Agile without slowing sprints?' → security stories, definition of done, automation, champions
- 'Requirements change frequently, frequent releases' → Agile fits
- **Trap:** adding a big security review phase at the end of each release isn't the Agile answer; build it into each sprint

**Quick check:** A Scrum team ships every two weeks and says there's 'no time for security.' How do you build security into their process without adding a separate security phase?

**Answer:** Build security **into the sprint process** instead of adding a separate phase: write **security user stories / abuse stories** in the backlog, add security to the **definition of done** (e.g., code reviewed, SAST passing, no high findings), do **lightweight threat modeling** when stories touch sensitive features, automate security tests in the pipeline, and use a **security champion** in each team.

</details>

<a name="t-2-1-3"></a>
**Spiral model**

Iterative and risk-driven; risk analysis in every loop.

> On the exam: What it's for: large, expensive or high-risk projects. Each loop goes through planning, risk analysis, engineering and evaluation.
Scenario cue: 'requirements are unclear and the project is high risk; which model?' → Spiral, because risk analysis happens every iteration.
Don't confuse: Waterfall has no repeated risk analysis; Agile focuses on fast delivery, not formal risk.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

An iterative model where **every cycle (loop of the spiral) begins with risk analysis**. Created by Barry Boehm (1986). Each loop gets bigger and more complete, like a spiral moving outward.

**The four quadrants of each loop**

- **1. Determine objectives:** what this cycle should achieve, alternatives, constraints
- **2. Identify and resolve risks:** risk analysis; often build a **prototype** to test the riskiest parts
- **3. Develop and test:** build and verify this cycle's version
- **4. Plan the next iteration:** review with stakeholders and decide whether to continue

**Strengths**

- **Risk-driven:** the biggest risks are tackled first, before heavy investment
- Good for **large, complex, expensive, high-risk** projects
- Handles changing requirements
- Prototypes clarify unclear requirements

**Weaknesses**

- Complex and costly to manage
- Needs real risk-assessment expertise
- Overkill for small, simple projects

**The security angle**

- Security risks are analyzed **every cycle**, as part of the built-in risk step
- Threat modeling and security risk assessment fit naturally into quadrant 2
- Security decisions are revisited as the system grows

**Spiral vs iterative**

- Both repeat cycles
- **Spiral adds formal risk analysis at the start of each cycle**

**On the exam**

- 'Large, high-risk project; requirements unclear; risk must be assessed each cycle' → **Spiral**
- 'Which model is risk-driven?' → Spiral
- **Trap:** Spiral is too heavy for small, simple projects

**Quick check:** A defense contractor is starting a large, expensive, high-risk project. Requirements are unclear and will evolve, and leadership wants risks formally reviewed at every stage. Which model fits best, and why?

**Answer:** **Spiral.** Requirements are unclear and the project is large and high-risk, and Spiral starts **every cycle with a formal risk analysis**, so the biggest risks (including security risks) are identified and reduced first, often with prototypes, before major investment.

</details>

<a name="t-2-1-4"></a>
**DevOps / DevSecOps**

Automated delivery with security built into the pipeline. Shift left: find issues earlier.

> On the exam: Automate security tests in the pipeline and make security everyone's job. Scenario cue: 'security review is a bottleneck before release' → automate it in CI/CD.

<details><summary>Lesson (08 Oct 2026)</summary>

**DevOps**

- Combines **Development and Operations** into one shared way of working
- Goals: **deliver software faster and more reliably** through collaboration and **automation**
- Key practices: CI/CD pipelines, infrastructure as code, automated testing, monitoring, fast feedback, small frequent releases
- Culture: shared responsibility; 'you build it, you run it'

**DevSecOps**

- **Security built into DevOps** from the start, as everyone's responsibility (not a separate team at the end)
- Core ideas:
- **Shift left:** security as early as possible (requirements, design, coding)
- **Automate security in the pipeline:** SAST, SCA, secret scanning, IaC and container scanning, DAST
- **Security as code:** policies and configurations written as code, reviewed and versioned
- **Fast feedback:** developers see security findings within minutes of committing
- **Shared responsibility** and security champions
- **Continuous monitoring** in production

**Why it matters**

- Teams may deploy many times a day; a manual security review at the end becomes a **bottleneck** (and gets skipped)
- Automation makes security consistent and scalable

**Securing the pipeline itself**

- The CI/CD pipeline can deploy to production, so it's a **high-value target**
- Protect it: least privilege, secrets in a vault, signed artifacts, approvals for production, audit logs

**On the exam**

- 'Security review is a bottleneck before release' → **automate security in the CI/CD pipeline (DevSecOps)**
- 'Shift left' → move security earlier
- 'Security is everyone's job' → DevSecOps culture
- **Trap:** DevSecOps doesn't remove humans; it automates repetitive checks so people focus on high-risk work

**Quick check:** A company deploys 20 times a day, but every release waits days for a manual security review, so teams start skipping it. What approach fixes this, and what would it look like?

**Answer:** Move security **into the pipeline and the teams** (DevSecOps): automate SAST, SCA, secret scanning, container/IaC scanning and DAST in CI/CD so every change is checked in minutes; set **break/build criteria** so critical findings block deployment automatically; keep the manual security review for high-risk changes only; train developers and add security champions. Security becomes a shared responsibility rather than a gate at the end.

</details>

<a name="t-2-1-5"></a>
**Microsoft SDL**

Training, requirements, design, implementation, verification, release, response.

> On the exam: What it is: Microsoft's Security Development Lifecycle. Key practices: security training, requirements and bug bars, threat modeling (STRIDE came from Microsoft), SAST, DAST/fuzzing, final security review, incident response plan.
Scenario cue: 'what happens before release?' → Final Security Review checks all SDL activities were done and the bug bar is met.
Trap: Response (incident response planning) is part of the SDL, so planning for incidents starts before release.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

Microsoft's **Security Development Lifecycle (SDL)**: a well-known, prescriptive process for building security into every phase of development. Introduced in 2004 after major worm outbreaks (and Bill Gates's 'Trustworthy Computing' memo, 2002).

**The phases and key practices**

- **Training:** core security training for developers, testers and managers (the foundation)
- **Requirements:** define security and privacy requirements, set **quality gates / bug bars** (e.g., no critical vulnerabilities at release), security and privacy risk assessment
- **Design:** **threat modeling** (STRIDE was created at Microsoft), attack surface analysis and reduction, design requirements
- **Implementation:** approved tools, **banned/unsafe functions** removed, **static analysis (SAST)**
- **Verification:** **dynamic analysis**, **fuzz testing**, attack surface review, threat model review
- **Release:** incident **response plan**, **Final Security Review (FSR)**, release and archive
- **Response:** execute the incident response plan when vulnerabilities are found after release

**Key exam points**

- **Training comes first**: security starts with people
- **Threat modeling** belongs in **design**
- The **Final Security Review (FSR)** checks that all SDL activities were done and the bug bar is met before release
- The **response plan** is prepared **before** release, not after an incident
- **Bug bar:** objective severity thresholds that block release

**Related models**

- **McGraw's Touchpoints:** seven security activities attached to existing development artifacts (code review, risk analysis, pen testing, etc.)
- **OWASP SAMM, BSIMM:** maturity models (Domain 2.8)

**On the exam**

- 'What happens just before release in the SDL?' → **Final Security Review**
- 'First step / foundation of the SDL?' → **training**
- 'Which phase includes threat modeling?' → **design**
- **Trap:** 'Response' is part of the SDL; incident response planning starts before release

**Quick check:** A team following Microsoft SDL ships a product without checking whether all critical security bugs were fixed, and has no plan for handling vulnerability reports. Which two SDL activities were skipped, and in which phase?

**Answer:** The **Final Security Review (FSR)** in the Release phase was skipped, so the bug bar (no open critical issues) wasn't enforced. And there was no incident **Response** plan prepared before release, which is also part of the SDL. Fix: make the FSR a mandatory release gate, and have the response plan ready before shipping.

</details>

<a name="t-2-1-6"></a>
**Security champions**

Developers on each team who promote and coordinate security.

> On the exam: Scales a small security team across many dev teams. Good answer for 'improve security culture among developers'.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

**Developers (or testers) inside each development team** who take on extra security responsibility. They're not full-time security staff; they're team members with extra training and interest.

**What they do**

- Act as the team's **first point of contact** for security questions
- Raise security concerns in planning and **design discussions** (e.g., 'this story needs a threat model')
- Help with **security code reviews** and triaging scanner findings
- Spread secure coding knowledge and good practices
- **Bridge** between the development team and the central security team (passing on new threats, standards and lessons learned)
- Promote a **security culture**

**Why organizations use them**

- Security teams are small; development teams are many → champions **scale** security
- Developers listen to peers more than outsiders
- Security issues get caught **earlier** (shift left)
- Builds a security culture from inside teams

**Making it work**

- Volunteers who are genuinely interested
- Dedicated **time** (e.g., a percentage of their week) and management support
- Extra **training**, regular meetups, recognition
- Clear role description

**Limits**

- Champions **support** the security team; they don't replace it
- Without time and support, the role becomes a title only

**On the exam**

- 'Small security team, many development teams; how to scale security?' → **security champions**
- 'Improve security culture within development teams' → security champions
- **Trap:** champions don't make the security team unnecessary

**Quick check:** A company has a 3-person security team and 40 development teams. Security issues are caught too late because the security team can't attend every team's planning. What program would help, and how does it work?

**Answer:** Appoint a **security champion** in each team: an interested developer given extra security training and time, who acts as the team's go-to person, spots issues early (design discussions, code reviews), shares knowledge, and links the team to the central security team. This scales security across 40 teams without hiring 40 security experts.

</details>

<a name="t-2-1-7"></a>
**Cost of fixing defects**

A flaw is far cheaper to fix in requirements or design than in production.

> On the exam: Why the exam usually prefers early activities (requirements, threat modeling, design review) over finding issues later.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

The **later a defect (bug or design flaw) is found in the lifecycle, the more it costs to fix.** Costs grow sharply from requirements to production.

**Why costs rise**

- Each later phase has built on top of the mistake: design → code → tests → documentation → deployment
- Fixing it means **going back** and redoing all of that work
- In production, add: emergency patches, downtime, customer impact, breach response, fines, legal costs and reputation damage

**Rough picture (often quoted)**

- Requirements/design: cheapest (change a document)
- Coding: more expensive
- Testing: much more
- Production: by far the most (often cited as **tens to 100 times** more than fixing in design)

Exact numbers vary by study; the exam cares about the **trend**, not the figures.

**What it means for security**

- **Shift left:** do security as early as possible
- Early activities give the best return: **security requirements, threat modeling, design reviews**
- Automated checks in development (SAST, SCA) catch issues before testing
- **Design flaws** (e.g., missing authentication between services) are the most expensive, because fixing them can mean re-architecting

**On the exam**

- 'Which activity gives the best return / is most cost-effective?' → usually the **earliest** one (requirements, threat modeling, design review)
- 'Why build security in early?' → defects cost far more to fix later
- **Trap:** penetration testing before release is valuable, but it's not the cheapest place to find design flaws

**Quick check:** A security budget allows one activity. Which gives the most cost-effective protection against a missing authentication design: (A) threat modeling during design, (B) penetration testing before release, or (C) a bug bounty after launch? Why?

**Answer:** **Option A: threat modeling during design.** It's the cheapest point to catch a missing authentication design: a few hours of review versus re-architecting the system, rewriting code, retesting and possibly handling a breach later. The rising cost of fixing defects is the reason security is 'shifted left'.

</details>

<a name="t-2-1-8"></a>
**SDLC phases**

Typical phases: requirements, design, development, testing, deployment, operations and maintenance, disposal.

> On the exam: Security in each: requirements (security and privacy requirements), design (threat modeling), development (secure coding, SAST), testing (DAST, pentest), deployment (hardening), operations (monitoring, patching), disposal (data destruction).
Scenario cue: 'where is it cheapest to fix a flaw?' → as early as possible.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

The **Software Development Lifecycle (SDLC)** is the series of phases software goes through from idea to retirement. Security must be built into **every** phase, not added at the end.

**The phases and their security activities**

- **1. Requirements (planning/analysis):** define security and privacy requirements, compliance needs, data classification, misuse/abuse cases, risk assessment
- **2. Design:** threat modeling, secure architecture, design reviews, choosing security controls (attack surface review)
- **3. Development (implementation/coding):** secure coding standards, code review, SAST, using approved libraries (SCA)
- **4. Testing (verification):** security testing, DAST, fuzzing, penetration testing, verifying security requirements were met
- **5. Deployment (release):** secure configuration/hardening, final security review, sign-off (risk acceptance), secure release
- **6. Operations and maintenance:** monitoring, patching, vulnerability management, incident response, change management
- **7. Disposal (retirement/decommissioning):** secure data destruction, removing accounts/keys/certificates, archiving

**Key ideas**

- **'Build security in, not bolt it on'**: security added late is costly and weak
- **Shift left:** move security activities earlier in the lifecycle
- Each phase's security output feeds the next (requirements → threat model → code → tests: the security profile chain)
- Disposal is a phase too; forgotten apps keep running with old accounts and data

**Where common activities belong (exam favorite)**

- Threat modeling → **design**
- Defining security requirements, data classification, misuse cases → **requirements**
- SAST, code review → **development**
- DAST, pentest → **testing**
- Hardening, final review → **deployment**
- Patching, monitoring → **operations**
- Data destruction → **disposal**

**On the exam**

- 'When should security first be considered?' → **the very beginning (requirements/planning)**
- **Trap:** testing finds problems, but it can't 'add' security that was never required or designed

**Quick check:** A team discovers during testing that their app stores full card CVV codes, which the payment industry forbids. In which SDLC phase should this rule have been captured, and why does fixing it now cost more?

**Answer:** **Requirements phase.** The rule came from the payment industry (PCI DSS: never store the CVV after authorization), a compliance requirement that should have been captured as a security requirement before design. Fixing it now means changing the database, code and tests (and possibly a breach response), far more costly than writing one requirement early.

</details>

<a name="t-2-1-9"></a>
**V-model**

Waterfall variant where each development phase has a matching test phase: requirements ↔ acceptance testing, design ↔ system/integration testing, coding ↔ unit testing.

> On the exam: Strength: test planning starts early, verification and validation built in.
Scenario cue: 'each phase is paired with a corresponding test phase' → V-model.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

A variation of Waterfall where **each development phase on the left side is paired with a matching test phase on the right side**. Drawn as a 'V': going down the left = building; going up the right = testing.

**The pairs**

- **Requirements ↔ Acceptance testing** (does it meet the user's needs? = validation)
- **System design ↔ System testing** (does the whole system work as designed?)
- **Architecture / high-level design ↔ Integration testing** (do components work together?)
- **Module / detailed design ↔ Unit testing** (does each piece work?)
- **Coding** sits at the bottom point of the V

**Key idea**

**Test planning starts early.** As soon as requirements are written, the acceptance tests for them are planned; as soon as the design is done, the matching tests are planned.

This builds **verification and validation (V&V)** into every phase.

**Strengths**

- Every requirement has a planned test → good **traceability**
- Defects in requirements and design are caught earlier (by writing tests against them)
- Disciplined, good for **safety-critical and regulated** systems (medical, automotive, aerospace)

**Weaknesses**

- Still rigid like Waterfall; changes are costly
- Working software appears late

**Security angle**

- Each **security requirement** gets a matching **security test** planned at the same time
- Misuse/abuse cases written in requirements → become security acceptance tests
- Supports the requirements traceability matrix (RTM)

**On the exam**

- 'Each development phase has a corresponding testing phase' → **V-model**
- 'Test planning begins during requirements' → V-model
- **Trap:** V stands for **Verification and Validation**, not 'version'

**Quick check:** A medical-device company wants a model where every development phase has a matching test phase, and test plans are written as soon as each phase's documents are approved. Which model is this, and how does it help security?

**Answer:** **V-model.** Each development phase is paired with a matching test phase, and test planning starts as soon as each phase is defined. Security-wise: security requirements are matched by acceptance testing; the security architecture by system/integration testing; module design by unit tests, so every security requirement has a planned test from the start.

</details>

<a name="t-2-1-10"></a>
**Prototyping and RAD**

Prototyping builds quick models to clarify requirements; Rapid Application Development builds fast with prototypes and user feedback.

> On the exam: Risk: prototypes often become production code without security being added.
Scenario cue: 'demo code was put into production' → prototype security risk.

<details><summary>Lesson (08 Oct 2026)</summary>

**Prototyping**

- Build a **quick, rough model** of the software to show users and clarify requirements
- Users react ('that's not what we meant'), and requirements improve
- **Throwaway prototype:** built only to learn, then discarded; the real system is built properly
- **Evolutionary prototype:** the prototype is gradually refined into the final product

**RAD (Rapid Application Development)**

- Focus on **speed**: build quickly using prototypes, reusable components and constant user feedback
- Short time-boxes; users heavily involved
- Good when requirements are unclear and fast delivery matters

**Strengths**

- Clarifies unclear requirements early
- Fast feedback, users feel involved
- Reduces the risk of building the wrong thing

**The big security risk**

- Prototypes are built **fast and without security**: hard-coded passwords, test accounts, no input validation, no access control, debug features left on
- Danger: **'the demo becomes the product'**. Management sees a working prototype and wants to release it
- Speed pressure in RAD can push security aside

**How to manage it**

- Treat prototypes as **disposable** by default
- If prototype code is kept, it must go through the **full secure SDLC** before release (security requirements, threat model, code review, testing, removing test credentials)
- Never use real sensitive data in prototypes
- Keep prototypes isolated from production systems

**On the exam**

- 'Prototype code was deployed to production' → security risk; must be rebuilt or fully reviewed
- 'Requirements are unclear; users need to see something to decide' → **prototyping**
- 'Speed is the top priority, heavy user involvement' → **RAD**

**Quick check:** A startup builds a quick prototype of its app for an investor demo. Investors love it, so the team launches the prototype code to real customers the next week. What's the security problem, and what should they have done?

**Answer:** The **throwaway prototype became production code** without security being added. Prototypes skip security for speed (hard-coded test passwords, no input validation, no authorization). Fix: treat prototypes as disposable; if any prototype code is kept, it must go through the full secure SDLC (security requirements, threat model, code review, security testing, removing hard-coded credentials) before release.

</details>

<a name="t-2-1-11"></a>
**Extreme Programming (XP) and TDD**

XP uses pair programming, short releases, continuous integration and test-driven development (write the test before the code).

> On the exam: Security angle: pair programming is a form of continuous peer review; TDD makes it natural to add security test cases first.

<details><summary>Lesson (08 Oct 2026)</summary>

**Extreme Programming (XP)**

An Agile method that pushes good engineering practices to the 'extreme'. Key practices:

- **Pair programming:** two developers at one computer; one writes (driver), one reviews (navigator), switching often
- **Test-driven development (TDD)**
- **Continuous integration:** merge and test code many times a day
- **Small, frequent releases**
- **Refactoring:** continuously simplifying and cleaning code
- **Collective code ownership:** anyone can improve any part of the code
- Simple design; customer on-site

**Test-driven development (TDD)**

- Cycle: **Red → Green → Refactor**
- 1. Write a test for the next small piece of behavior; it fails (red)
- 2. Write just enough code to pass it (green)
- 3. Clean up the code (refactor), keeping tests passing
- The tests become a safety net for every future change

**Security benefits**

- **Pair programming = continuous peer code review**: mistakes caught as they're typed
- **TDD lets you write security tests first**: e.g., 'login rejects SQL injection input', 'user A can't read user B's order'. Code is written to pass them
- Tests act as **regression tests**: a fixed vulnerability can't silently come back
- Refactoring keeps code simple (economy of mechanism)

**Limits and risks**

- Two developers who both lack security knowledge won't catch security flaws: still need **training** and **SAST**
- TDD only tests what you think to test: include **negative/abuse tests**, not just happy paths
- Collective ownership means everyone needs secure coding knowledge

**On the exam**

- 'Two developers share one workstation and review code as it's written' → **pair programming (XP)**
- 'Tests written before the code' → **TDD**
- Security link: pair programming = continuous review; TDD = security tests first + regression protection

**Quick check:** A team uses XP with pair programming and TDD. A manager asks how these practices help security, and what their limits are. What would you say?

**Answer:** Security has to be built into the work itself: **TDD makes it natural to write security tests first** (e.g., a test that SQL injection input is rejected, before writing the query code), and **pair programming acts as continuous code review**, catching mistakes as they're typed. But pair partners may both lack security knowledge, so add secure coding training, automated SAST in continuous integration, and security-focused tests.

</details>

<a name="t-2-1-12"></a>
**Kanban and Lean**

Visual board limiting work in progress, focused on continuous flow and removing waste.

> On the exam: Security angle: add security tasks as cards with the same visibility as features, or they get skipped.

<details><summary>Lesson (08 Oct 2026)</summary>

**Kanban**

- A **visual board** showing work as **cards** moving through **columns** (e.g., To Do → In Progress → Review → Done)
- **Work-in-progress (WIP) limits:** cap how many cards can be in a column at once, to avoid overload and bottlenecks
- **Continuous flow:** no fixed sprints; new work is **pulled** when capacity frees up
- Popular for operations, support and maintenance teams

**Lean**

- From Toyota manufacturing; focuses on **delivering value and eliminating waste**
- Waste examples: unfinished work, waiting, rework, unnecessary features, handoffs
- Principles: build quality in, deliver fast, defer decisions until needed, respect people, optimize the whole

**Security challenges**

- If security work isn't on the board, it's **invisible** and never pulled
- 'Eliminate waste' can be misread as 'security reviews are waste'
- Continuous flow means no natural checkpoint for security

**How to build security in**

- **Security tasks as cards** with the same visibility as features
- **Explicit policies per column**, e.g., a card can't move to Done until security checks pass
- A **'Security review' column** for sensitive changes
- **Classes of service:** an expedite lane for critical vulnerabilities
- Track security debt visually
- Lean view: **security flaws found late are waste** (rework), so building security in early IS Lean

**On the exam**

- 'Visual board, cards, WIP limits, continuous flow' → **Kanban**
- 'Eliminate waste, maximize value' → **Lean**
- Adding security: make it **visible** (cards, column policies)
- **Trap:** security isn't waste; rework from late-found vulnerabilities is

**Quick check:** An operations team uses a Kanban board. Security patches and fixes keep getting forgotten while feature cards move quickly to 'Done.' What's wrong, and how would you fix it using Kanban itself?

**Answer:** Security work isn't **visible** on the board, so it's never pulled. Fix: put security tasks on the board as **cards** with the same visibility and priority rules as features; add a **security step (column) or policy**, e.g., 'Security review' before 'Done', or make security checks part of the column's exit criteria; and treat security fixes as a class of service with fast-track priority for critical issues.

</details>

<a name="t-2-1-13"></a>
**CI, continuous delivery, continuous deployment**

CI: merge, build and test code often. Continuous delivery: every build is ready to release, with a manual approval. Continuous deployment: releases go to production automatically.

> On the exam: Security angle: automated tests and gates replace manual reviews, so the pipeline itself must be secured.
Scenario cue: 'changes go to production with no human approval' → continuous deployment; needs strong automated security gates.

<details><summary>Lesson (08 Oct 2026)</summary>

**Three related terms (often confused)**

- **Continuous Integration (CI):** developers **merge code into a shared repository frequently** (many times a day); each merge triggers an **automated build and tests**. Catches integration problems early.
- **Continuous Delivery (CD):** every change that passes the pipeline is **ready to release** at any time, but a **human approves** the actual production release.
- **Continuous Deployment (CD):** every change that passes the pipeline is **released to production automatically**, with **no human approval**.

**Memory trick**

- **Delivery** = delivered to the door, someone decides to open it (manual approval)
- **Deployment** = goes straight in automatically

**The pipeline**

Code commit → build → automated tests → security scans → artifact stored/signed → deploy to test/staging → (approval for delivery) → production

**Security in CI/CD**

- **Security gates** at each stage: SAST, SCA, secret scanning, IaC/container scanning, DAST
- **Break/build criteria:** critical findings automatically stop the pipeline
- **Signed artifacts:** only verified builds get deployed
- **Protect the pipeline:** least-privilege service accounts, secrets in a vault, separation of duties (no one can push straight to production alone), audit logs
- **Continuous deployment** needs the **strongest automated gates**, since no human checks each release
- Fast **rollback** and production **monitoring**

**On the exam**

- 'Code merged and tested automatically many times a day' → **CI**
- 'Always releasable, human approves release' → **continuous delivery**
- 'Released to production automatically with no human approval' → **continuous deployment**
- **Trap:** the pipeline is part of the attack surface; a compromised pipeline = supply chain attack

**Quick check:** A team's pipeline automatically builds, tests and releases every passing change straight to production with no human approval. Which practice is this, and what does it mean for security?

**Answer:** **Continuous deployment** (every passing change goes to production automatically, no human approval). Since no human checks each release, the **automated pipeline must contain strong security gates**: SAST, SCA, secret scanning, DAST, break/build criteria that stop deployment on critical findings, signed artifacts, and a protected pipeline, plus monitoring and fast rollback in production.

</details>

<a name="t-2-1-14"></a>
**Reverse engineering**

Analyzing a finished product (binary, protocol) to understand how it works without the source.

> On the exam: Uses: malware analysis, interoperability, security research, finding vulnerabilities. Risks: attackers steal intellectual property or find flaws; often restricted by EULA and law.
Defenses: obfuscation, anti-tamper, anti-debugging, keep secrets off the client.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

Analyzing a **finished product** (a compiled program, app, device or protocol) to work out **how it works**, without access to its source code or design documents. Working backwards from the result to the design.

**How it's done**

- **Disassemblers** turn machine code into assembly
- **Decompilers** turn compiled code back into readable source-like code (easy for Java, .NET, Android apps)
- **Debuggers** run the program step by step and inspect memory
- Network traffic analysis to understand protocols

**Legitimate uses**

- **Malware analysis:** understanding what a virus does
- **Security research:** finding vulnerabilities to fix them
- **Interoperability:** making software work with an undocumented system
- Recovering lost source code; verifying a vendor's claims

**Malicious uses**

- Stealing **intellectual property** (algorithms, trade secrets)
- Finding vulnerabilities to **exploit**
- Extracting **secrets embedded in code** (API keys, passwords, encryption keys)
- **Cracking** licenses and DRM, creating pirated versions
- Building counterfeit or tampered versions of apps

**Defenses (anti-reversing)**

- **Never put secrets in client-side code**; assume anything shipped can be read
- Do important checks on the **server**, not the client
- **Obfuscation:** make code harder to read
- **Anti-debugging** and **anti-tamper / integrity checks**
- Code signing (detect modified versions)
- Legal protection: EULA clauses, copyright, DMCA (anti-circumvention)

**Legal note**

Reverse engineering vendor software may break the **license (EULA)** or law; security teams should get **permission** first.

**On the exam**

- 'Attacker decompiled the app and found an embedded key' → **reverse engineering**; fix: no secrets in client code
- 'Analyze malware to understand its behavior' → legitimate reverse engineering
- **Trap:** obfuscation slows attackers; it doesn't make secrets safe (open design)

**Quick check:** An attacker downloads a company's mobile app, decompiles it, and finds an API key that gives access to the company's backend. What technique did the attacker use, and how should the company defend against it?

**Answer:** **Reverse engineering.** The defenses: **never store secrets (like API keys) in client code**: keep them on the server and give the app short-lived, per-user tokens; perform security checks **server-side**; and add **anti-reversing** measures (obfuscation, integrity/tamper checks) to raise attacker effort. Obfuscation slows attackers but can't protect secrets on its own.

</details>

<a name="t-2-1-15"></a>
**Re-engineering**

Restructuring or rebuilding existing software to improve it (new platform, refactoring) while keeping its function.

> On the exam: Security angle: re-engineered code needs the same reviews and full regression and security testing; old security assumptions may no longer hold.
Scenario cue: 'legacy app moved to the cloud without retesting' → new attack surface untested.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

**Restructuring, rewriting or rebuilding existing software** to improve it, while keeping what it does. Examples: moving a legacy app to the cloud, rewriting it in a new language, splitting a big app into microservices, major refactoring.

Often done as: **reverse engineer** the old system (understand it) → **redesign** → **rebuild** (forward engineering).

**Why organizations do it**

- Old technology is unsupported or hard to maintain
- Need better performance, scalability or new features
- Reduce technical debt

**Security risks**

- **Old security assumptions break:** e.g., the legacy app was safe only because it ran on a closed internal network; in the cloud it's exposed
- New platform = new **attack surface** (APIs, cloud services, new integrations)
- Security controls in the old system (sometimes undocumented) may be **lost** in the rewrite
- New bugs introduced during rewriting
- Data migration can expose or corrupt sensitive data

**How to do it securely**

- Treat it like **new development**: full secure SDLC
- **Redo the threat model** for the new architecture and environment
- Document the **existing security controls** first, so none are lost
- Full **security testing and regression testing** (does it still behave correctly and securely?)
- Protect data during migration (encryption, validation, secure disposal of the old copies)
- Decommission the old system securely (remove access, sanitize data)

**Re-engineering vs reverse engineering**

- **Reverse engineering:** understanding how something works (analysis)
- **Re-engineering:** changing/rebuilding it to improve it (often starts with reverse engineering)

**On the exam**

- 'Legacy app migrated to the cloud without new security review' → re-engineering risk; redo threat model and testing
- **Trap:** 'it was secure before' doesn't mean it's secure after re-engineering

**Quick check:** A company moves its 15-year-old internal billing system to the cloud and exposes a new API so partners can use it. They skip security testing because 'the old system never had problems.' What's this process called, and what's the security mistake?

**Answer:** **Re-engineering** (migrating/rebuilding legacy software). The security mistake: assuming the old system's security still applied. In the new environment (internet-facing cloud), old assumptions broke: the closed internal network no longer protects it. Fix: treat it as new software: **redo the threat model**, add authentication for the newly exposed API, and run **full security and regression testing** before go-live.

</details>

<a name="t-2-1-16"></a>
**Iterative model**

The project is split into small cycles, each going through requirements, design, build and test, producing a working piece.

> On the exam: Security angle: security activities must repeat in every iteration, not just once.
Don't confuse: iterative refines the product over cycles; spiral adds formal risk analysis to each cycle.

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

The project is built in **repeated cycles (iterations)**. Each iteration goes through requirements → design → build → test and produces a **working version**, which is improved and expanded in the next cycle.

**Iterative vs incremental**

- **Iterative:** build a rough version of the whole thing, then **refine** it each cycle
- **Incremental:** build and deliver it **piece by piece** (feature by feature)
- Most modern models (Agile) are **both**: deliver small pieces and improve them over time

**Strengths**

- Working software early; feedback from users each cycle
- Requirements can change and grow
- Risks and problems show up sooner

**Weaknesses**

- Scope can grow uncontrolled
- Architecture may need rework if early design was too rough
- Security can be forgotten if it's only done 'once'

**The security angle**

- **Security activities must repeat in every iteration**, not just the first:
- Update the **threat model** when new features, data or integrations are added
- Add **security requirements** for each new feature
- Run **security tests** each cycle, plus **regression tests** so old fixes stay fixed
- Watch for growing attack surface as features accumulate

**Iterative vs spiral (next topic)**

- Iterative: repeating build cycles
- Spiral: repeating cycles **with formal risk analysis at the start of each one**

**On the exam**

- 'Software is built in repeated cycles, each producing a working version' → **iterative**
- **Trap:** a threat model done only in iteration 1 becomes outdated; it must be revisited every cycle

**Quick check:** A team builds an online store iteratively. In iteration 1 they did a threat model for the product catalog. In iteration 4 they add online payments but don't revisit the threat model. What's the security problem?

**Answer:** **Security activities must repeat in every iteration.** Iteration 1's threat model only covered the catalog; payments added new data flows, a new trust boundary (the payment provider) and highly sensitive data. Each iteration should **update the threat model**, add security requirements for the new features, and run security tests (plus regression tests to make sure earlier features weren't broken).

</details>

<a name="t-2-1-17"></a>
**Information systems development lifecycle (NIST)**

NIST's view of the system lifecycle: initiation, development/acquisition, implementation/assessment, operations/maintenance, disposal.

> On the exam: Security in each: categorize and assess risk (initiation), define and build controls (development), test and authorize (implementation), monitor and change-manage (operations), sanitize and archive (disposal).

<details><summary>Lesson (08 Oct 2026)</summary>

**What it is**

NIST's (US National Institute of Standards and Technology) view of the system lifecycle, used heavily in government. It's the SDLC seen from a **system and risk management** angle, and it maps to the NIST Risk Management Framework (RMF).

**The five phases and their security activities**

- **1. Initiation:** define the need; **categorize the system** by impact (FIPS 199: low/moderate/high for C, I, A); initial risk assessment; identify security requirements
- **2. Development / Acquisition:** design or buy the system; select and design **security controls** (NIST SP 800-53); security in contracts if buying
- **3. Implementation / Assessment:** install and configure; **test (assess) the controls**; obtain **authorization to operate (ATO)** from a senior official who accepts the residual risk
- **4. Operations / Maintenance:** run the system; **continuous monitoring**, configuration and change management, patching, incident response
- **5. Disposal:** retire securely; **sanitize media** (NIST SP 800-88), archive what's required, remove access

**Mapping to the normal SDLC**

- Initiation ≈ requirements/planning
- Development/Acquisition ≈ design + development
- Implementation/Assessment ≈ testing + deployment (with formal authorization)
- Operations/Maintenance ≈ operations
- Disposal ≈ disposal

**Notable differences**

- Explicitly includes **acquisition** (buying) as well as building
- **Categorization** happens first and drives which controls are needed
- **Formal authorization (ATO)** before going live

**On the exam**

- 'Categorize the system by impact level' → **initiation**
- 'Select security controls' → **development/acquisition**
- 'Assess controls and obtain authorization to operate' → **implementation/assessment**
- 'Continuous monitoring' → **operations/maintenance**
- 'Media sanitization' → **disposal**

**Quick check:** A government agency builds a new system but skips categorizing how sensitive its data is. Later, they discover the system processes sensitive citizen records with only basic controls. Which NIST lifecycle phase was skipped, and why did it matter?

**Answer:** **Initiation.** That's where the system is **categorized** (FIPS 199: how sensitive the data is, impact on C/I/A) and initial risk assessed. Skipping it means nobody knew the system held sensitive citizen data, so the right controls were never chosen in development/acquisition.

</details>

## 2.2 Security standards and awareness

<a name="t-2-2-1"></a>
**Implementing security frameworks**

Adopt a recognized framework (SSDF, SAMM, ISO 27034) instead of inventing one.

> On the exam: What it's for: gives the organization a proven, repeatable structure instead of improvising, plus a common language with auditors and customers.
Scenario cue: 'a company has no consistent secure development process across teams; what first?' → adopt a framework (SSDF, SAMM, ISO 27034) and tailor it.
Don't confuse: a framework is flexible guidance; a standard is mandatory and specific.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

Using an **established, recognized framework** as the structure for your security program, rather than inventing your own from scratch.

**Framework vs standard (often tested)**

- **Framework:** a flexible structure of recommended practices, **tailored** to your organization (e.g., NIST SSDF, NIST CSF, OWASP SAMM)
- **Standard:** specific, **mandatory** requirements you must meet (e.g., PCI DSS, an internal 'TLS 1.2+' standard, ISO 27001 certification requirements)

**Benefits**

- **Proven:** built from industry experience; less chance of missing something
- **Consistent:** every team follows the same baseline
- **Common language** with auditors, customers and partners
- **Easier compliance and audits**: maps to regulations
- Gives a **roadmap** and a way to measure maturity
- Faster than inventing your own (component reuse thinking)

**How to implement one**

- **1. Choose** a framework that fits your goals and industry
- **2. Gap analysis:** compare current practices against it
- **3. Prioritize** gaps by risk and effort
- **4. Tailor:** adapt practices to your size and culture (frameworks aren't one-size-fits-all)
- **5. Roll out in phases** with leadership support (governance)
- **6. Measure and improve** continuously (metrics, maturity levels)

**Common software security frameworks**

- **NIST SSDF (SP 800-218):** secure development practices
- **OWASP SAMM:** maturity model for software assurance
- **BSIMM:** benchmark of what other organizations do
- **Microsoft SDL:** prescriptive development lifecycle
- **ISO/IEC 27034:** application security standard

**On the exam**

- 'Teams each do security differently; no consistency. First step?' → **adopt and tailor a recognized framework**
- **Trap:** frameworks are flexible guidance; standards are mandatory

**Quick check:** A company has 12 development teams, each doing security its own way. Auditors can't tell what the company's secure development process actually is. What should the company do?

**Answer:** **Adopt an established framework (e.g., NIST SSDF or OWASP SAMM) and tailor it** to the company: assess current practices against it (gap analysis), prioritize the gaps, roll it out in phases, and measure progress. This gives a common, proven, auditable baseline across all 12 teams instead of each team inventing its own.

</details>

<a name="t-2-2-2"></a>
**NIST SP 800-218 (SSDF)**

Secure Software Development Framework: prepare the org, protect software, produce well-secured software, respond to vulnerabilities.

> On the exam: Four groups: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW), Respond to Vulnerabilities (RV). Used for US federal supplier attestation.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**NIST SP 800-218, the Secure Software Development Framework (SSDF)**, version 1.1 (2022). A set of **high-level secure development practices** that can be added to **any SDLC** (waterfall, agile, DevOps).

**Key traits**

- **Outcome-based, not prescriptive:** says WHAT to achieve, not exactly HOW
- **Methodology-neutral:** fits any lifecycle
- Built from existing practices (BSIMM, SAMM, Microsoft SDL, OWASP)
- Common language between **software producers and buyers**

**The 4 practice groups (memorize)**

- **PO — Prepare the Organization:** people, processes, tools ready (roles, training, security requirements, toolchains)
- **PS — Protect the Software:** protect code and releases from tampering (access control on repos, signing/integrity verification, archiving each release + provenance/SBOM)
- **PW — Produce Well-Secured Software:** secure design, threat modeling, reuse vetted components, secure coding, code review, testing, secure default config
- **RV — Respond to Vulnerabilities:** identify, analyze, fix, and find **root causes** of vulnerabilities after release; includes a **vulnerability disclosure policy** and the roles/process to handle incoming reports
- Mnemonic: **Prepare, Protect, Produce, Respond**

**Why it matters**

- Linked to **US Executive Order 14028** (2021) on improving cybersecurity
- Software suppliers to the **US federal government** must **attest** to following SSDF practices (CISA secure software attestation form)
- **SP 800-218A (2024):** community profile adding practices for **generative AI and dual-use foundation models** (ties to AI sections)

**On the exam**

- 'Framework of secure development practices that works with any SDLC; required for federal software suppliers' → **SSDF / SP 800-218**
- Match a scenario to the group: training/roles → **PO**; code signing/repo protection → **PS**; threat modeling/code review → **PW**; vulnerability disclosure/patching → **RV**
- **Trap:** a reported flaw in RELEASED software with no one handling it is **RV**, even though 'roles' are mentioned
- **Trap:** SSDF doesn't replace your SDLC; it **plugs into** it

**Quick check:** An outside security researcher emails your company about a flaw in your released app, but no one knows who should handle it, and the flaw is never fixed. Which SSDF practice group is missing?

**Answer:** **RV — Respond to Vulnerabilities.** Clue words: *released app*, *flaw reported*, *never fixed*. RV itself includes having a vulnerability disclosure policy AND the roles/process to receive, triage and fix reports. **Trap:** 'no one knows who handles it' tempts you toward PO (roles), but PO is about general readiness (training, security requirements, toolchains). Roles for handling reported vulnerabilities belong to RV.

</details>

<a name="t-2-2-3"></a>
**ISO/IEC 27034**

International standard for application security.

> On the exam: Defines an Organization Normative Framework (ONF) and an Application Normative Framework (ANF) holding the security controls for each app.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**ISO/IEC 27034, 'Application security'**: an international standard that helps organizations **build security into applications** through **processes**. It extends the ISO 27001 ISMS idea down to the application level.

**Big idea**

- It's about **processes and a management framework**, not a list of coding rules
- It does NOT prescribe specific controls or an SDLC; it tells you how to organize, select and verify them
- 'Application' is broad: not just code, but **data, business context, regulatory context, technology, specifications, processes and people** around it

**Key terms (heavily tested)**

- **ONF — Organization Normative Framework:** the **organization-wide** repository of approved application security best practices, controls, policies, roles and processes. **One per organization.**
- **ANF — Application Normative Framework:** the **subset of the ONF** selected for **one specific application**, based on its risk. **One per application.**
- **ASC — Application Security Control:** a reusable control that includes a security **activity**, a **verification measurement** (how to prove it was done), and the lifecycle stage where it applies
- **Targeted level of trust:** the security level an application needs, set by risk assessment; ASCs are chosen to reach it
- **Actual level of trust:** the level verified in reality; compare it to the target
- **ASMP — Application Security Management Process:** the per-application process: specify requirements and environment, assess risk, create the ANF, provision and operate the application, audit its security

**Main parts**

- **Part 1:** overview and concepts
- **Part 2:** the ONF
- **Part 3:** the application security management process (ASMP)
- **Part 5:** protocols and ASC data structure
- **Part 6:** case studies
- **Part 7:** assurance prediction framework (reusing trust results across applications)

**On the exam**

- 'International standard for application security' → **ISO/IEC 27034**
- 'Organization-wide repository of app security practices' → **ONF**; 'subset for one app' → **ANF**
- 'Control with an activity plus a way to verify it' → **ASC**
- **Don't confuse:** ISO 27001 = ISMS for the whole organization; ISO 27034 = security of **applications**
- **Trap:** 27034 is process-oriented and does not give secure coding rules

**Quick check:** A company keeps all its approved application security practices in one central company-wide repository. For a new payroll app, it selects only the practices relevant to that app's risk. What are the repository and the selected subset called in ISO/IEC 27034?

**Answer:** **ONF (Organization Normative Framework)** = the company-wide repository of all approved application security practices and controls. **ANF (Application Normative Framework)** = the subset selected for one specific application (the payroll app). One ONF per organization; one ANF per application.

</details>

<a name="t-2-2-4"></a>
**Secure coding standards**

E.g., SEI CERT coding standards for specific languages.

> On the exam: What it's for: tells developers exactly how to code safely in their language, so reviews and tools can check against it. Examples: SEI CERT C/Java, OWASP Secure Coding Practices.
Scenario cue: 'code reviews keep finding the same flaw types across teams' → adopt a secure coding standard, train on it, enforce it with SAST rules.
Trap: a standard alone changes nothing; it must be trained and enforced.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

A **documented set of rules** developers must follow so code doesn't contain common vulnerabilities. Usually **language-specific** and **mandatory** within the organization.

**Why use them**

- **Prevent** common flaws (injection, buffer overflows, unsafe deserialization) at the source
- **Consistency** across developers and teams
- Give code reviewers and tools a clear **yardstick** to check against
- Cheaper than finding the flaws later in testing or production

**Well-known examples**

- **SEI CERT coding standards** (Carnegie Mellon): C, C++, Java, Android, Perl. Split into **rules** (violations likely cause defects; mandatory) and **recommendations** (improve quality; advisory)
- **OWASP Secure Coding Practices Quick Reference Guide:** technology-neutral **checklist** (input validation, output encoding, authentication, session management, error handling, etc.)
- **MISRA C/C++:** safety-critical systems (automotive, embedded)
- **Banned functions lists:** e.g., Microsoft's list of unsafe C functions such as **strcpy, strcat, gets, sprintf** (replace with bounded versions)
- Company-internal standards built from the above

**How they're enforced**

- **Training** developers on them
- **IDE plugins and linters** for instant feedback
- **SAST** rules in the CI/CD pipeline (fail the build on violations)
- **Code review** checklists
- Part of the **definition of done**

**On the exam**

- 'Language-specific rules to prevent vulnerabilities' → **secure coding standard** (e.g., **CERT**)
- **Don't confuse:** **OWASP Top 10** = awareness list of web risk categories; **CWE** = catalog of weakness types; **CVE** = specific known vulnerabilities in specific products. None of these is a coding standard
- **Trap:** a standard is **mandatory**; a guideline is **recommended**
- Best enforcement is **automated** (SAST/linters) plus code review, not just a document

**Quick check:** A team wants a mandatory, language-specific set of rules for its C and Java code that its SAST tool can check automatically. Which fits best: OWASP Top 10, CWE Top 25, or SEI CERT coding standards? Why?

**Answer:** **SEI CERT coding standards.** They are language-specific (C, C++, Java, Android, Perl), contain concrete rules, and are widely supported by SAST tools. OWASP Top 10 is an awareness list of web risk categories, and CWE Top 25 is a list of the most dangerous weakness types; neither is a set of coding rules.

</details>

<a name="t-2-2-5"></a>
**Security awareness and training**

Role-based training for developers, testers, managers.

> On the exam: What it's for: awareness changes behavior, training builds skills, education builds deep understanding. Training should be role-based: developers learn secure coding, testers learn security testing, managers learn risk.
Scenario cue: 'the root cause of repeated vulnerabilities is that developers don't know secure practices' → training is the best answer, ideally before tools.
Trap: one generic annual video is awareness, not training.

<details><summary>Lesson (09 Oct 2026)</summary>

**Three levels (often tested)**

- **Awareness:** makes people **notice** security and change basic behavior. Short, broad, for everyone. Examples: posters, phishing simulations, annual video, newsletters. Answers 'what' and 'why it matters'.
- **Training:** builds **specific skills** for a job role. Hands-on. Examples: secure coding workshops for developers, security testing for QA. Answers 'how'.
- **Education:** builds **deep understanding**, long-term. Examples: degrees, certifications like CSSLP. Answers 'why' at a deep level.

**Role-based training**

Different roles need different content:

- **Developers:** secure coding, OWASP Top 10, input validation, crypto use, secure libraries
- **Testers:** security testing, abuse cases, tools
- **Architects:** threat modeling, secure design
- **Project managers:** security in planning, risk, gates
- **Operations:** hardening, patching, incident response
- **Executives:** risk, governance, compliance
- **Everyone:** phishing, passwords, data handling, reporting incidents

**Making it effective**

- Relevant to the person's actual work (role-based)
- Hands-on and practical (labs, real examples from your own code)
- **Repeated regularly**, not once
- Measured: fewer vulnerabilities in code reviews, phishing click rates, test scores
- Updated as threats change

**Why it matters**

- Many vulnerabilities come from developers simply **not knowing** secure practices
- Training is often the **most cost-effective first step** (prevents flaws at the source)
- It's the first phase of Microsoft's SDL

**On the exam**

- 'Root cause: developers don't know secure coding' → **training** (role-based)
- 'Make all staff recognize phishing' → **awareness**
- **Trap:** a generic awareness video isn't training; developers need hands-on skills

**Quick check:** Code reviews keep finding SQL injection in new code. The developers have only ever watched a 20-minute annual security awareness video. What's the best fix, and why isn't the video enough?

**Answer:** **Role-based secure coding training** for developers (hands-on, covering the OWASP Top 10, input validation, parameterized queries), because the root cause is a **skills/knowledge gap**, not a lack of awareness or tools. A generic annual video is only awareness. Reinforce with secure coding standards, SAST rules and security champions.

</details>

<a name="t-2-2-6"></a>
**Security governance**

How senior management directs and controls security: strategy, policies, roles (board, CISO, steering committee), oversight and accountability.

> On the exam: Scenario cue: 'security efforts fail because no one with authority supports them' → governance problem; get senior management sponsorship.
Trap: management is always ultimately accountable for security.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**Security governance** is how an organization's **leadership directs, controls and oversees** security. It answers: who decides, who's accountable, what are the priorities, and how do we know it's working?

It's top-down: security starts with senior management, not the IT team.

**Key elements**

- **Strategy:** security aligned with business goals
- **Policies:** senior management approves the high-level security policy
- **Roles and responsibilities:** clear owners (board, CISO, data owners...)
- **Accountability:** someone is answerable for outcomes
- **Resources:** budget and staff
- **Oversight:** metrics, reporting to leadership, audits
- **Risk appetite:** leadership decides how much risk is acceptable

**Governance vs management**

- **Governance:** sets direction and oversees (the board / senior leadership: 'what and why')
- **Management:** plans and runs day-to-day activities to achieve that direction ('how')

**Common structures**

- **Board of directors** with risk/audit committee
- **Security steering committee:** cross-department leaders who set priorities
- **CISO** (Chief Information Security Officer) reporting to senior leadership

**Why it matters for software**

- Without leadership support, secure SDLC programs get skipped under deadline pressure (iron triangle)
- Governance makes security requirements, gates and budgets mandatory

**On the exam**

- 'Security efforts fail because no leader supports them' → **governance** problem; get **senior management support**
- 'Who is ultimately accountable for security?' → **senior management / the board**
- **Trap:** the security team can't succeed alone; the first step is usually executive sponsorship

**Quick check:** A security team keeps proposing secure coding rules, but development managers ignore them and there's no budget. Leadership has never approved a security policy. What's the root problem, and how should it be fixed?

**Answer:** **Governance** problem: security lacks **senior management support, authority and accountability**. Fix: get executive sponsorship, have the board/senior management **approve a security policy and strategy**, assign clear roles (e.g., a CISO reporting to leadership), set up a steering committee, fund the program, and report security risk to leadership regularly.

</details>

<a name="t-2-2-7"></a>
**PDCA (Deming cycle)**

Plan → Do → Check → Act: plan improvements, implement them, measure results, then act to adjust. Repeats continuously.

> On the exam: Used by ISO 27001 and other management systems for continual improvement.
Scenario cue: 'a review shows the new control didn't work; what's next?' → Act: adjust and plan again.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**PDCA (Plan-Do-Check-Act)**, also called the **Deming cycle** (popularized by W. Edwards Deming, based on Walter Shewhart's work). A repeating **four-step loop for continuous improvement**.

**The 4 phases**

- **Plan:** set objectives, assess risks, decide what to change, select controls
- **Do:** implement the plan (deploy controls, run the new process), ideally on a small scale first
- **Check:** **monitor and measure** results against objectives (metrics, testing, **audits**, reviews)
- **Act:** **take corrective action** and improve based on what Check found; standardize what worked; feed into the next Plan
- Then repeat; the cycle never 'ends'

**Where it shows up**

- Underlies **ISO management systems**: ISO 27001 (ISMS), ISO 9001 (quality), and the process thinking in ISO 27034
- Security programs, SDLC process improvement, incident 'lessons learned' loops
- Variant: **PDSA** (Plan-Do-**Study**-Act), Deming's later preferred wording

**Security example**

- **Plan:** risk assessment shows injection risk; decide to add SAST to the pipeline
- **Do:** roll SAST out to one team
- **Check:** measure findings and false positives; audit adoption
- **Act:** tune rules, roll out to all teams, update the standard

**On the exam**

- 'Continuous improvement cycle' / 'Deming' → **PDCA**
- Measuring, monitoring, auditing → **Check**
- Fixing, correcting, improving based on results → **Act**
- **Trap:** Check vs Act. Check **finds out**; Act **does something about it**
- **Trap:** Do = carry out the plan; not the same as Act

**Quick check:** An internal audit shows that the new code review process is being skipped by half the teams. Management updates the process and adds an automated gate to fix this. Which PDCA phase is management in?

**Answer:** **Act.** The audit (measuring whether controls work) was the **Check** phase. Updating the process to correct the problems found is **Act**, which then feeds the next **Plan**.

</details>

<a name="t-2-2-8"></a>
**ISO/IEC 27034 details**

Application security standard. Organization Normative Framework (ONF): the organization's approved security practices and controls. Application Normative Framework (ANF): the subset that applies to one application. Application Security Controls (ASCs) and target levels of trust.

> On the exam: Scenario cue: 'which ISO standard focuses specifically on securing applications across their lifecycle?' → 27034.

<a name="t-2-2-9"></a>
**Roles and responsibilities**

Senior management (accountable), security team (advises, oversees), developers (secure code), testers (verify), operations (secure deployment), data owners (classification).

> On the exam: Scenario cue: 'who is ultimately responsible for security of the product?' → senior management/business owner.

<details><summary>Lesson (09 Oct 2026)</summary>

**The key idea**

Security is a **shared responsibility**, but each role has a clear part. The exam often asks 'who should do X?'

**Main roles in software security**

- **Board / senior management:** ultimately **accountable**; set direction, approve policy, fund the program, **accept residual risk**
- **CISO:** leads the security program; reports security risk to leadership
- **Security team / architects:** set standards, **advise**, review designs, test, help teams; they **don't own** business risk decisions
- **Business / product owner:** owns the product and its risks; prioritizes security work; **signs off** on accepting risk
- **Data owner:** decides data classification and who gets access (accountable for the data)
- **Data custodian:** implements protection day to day (backups, access setup)
- **Developers:** write secure code, fix vulnerabilities, follow standards
- **Testers / QA:** verify security requirements, run security tests
- **Operations / admins:** secure deployment, patching, monitoring
- **Security champions:** security link inside development teams
- **Users:** follow policies, report incidents

**Accountable vs responsible**

- **Accountable:** answers for the outcome; only one owner (often senior management or the business owner)
- **Responsible:** does the work (can be many people)
- RACI charts map this: **R**esponsible, **A**ccountable, **C**onsulted, **I**nformed

**On the exam**

- 'Who accepts residual risk?' → **business owner / senior management**, not the security team or developers
- 'Who is ultimately accountable for security?' → **senior management**
- 'Who decides data classification?' → **data owner**
- **Trap:** security teams advise; they don't own business risk decisions

**Quick check:** A penetration test finds a medium-risk flaw one day before launch. Developers can't fix it in time. Who should decide whether to launch anyway, and what role does the security team play?

**Answer:** The **business owner (senior management / data owner)** decides and formally accepts the risk, because it's a business risk. The **security team advises** (explains the risk and options) but doesn't make business decisions; the **developers fix** issues. Senior management remains ultimately accountable.

</details>

<a name="t-2-2-10"></a>
**ITIL**

IT Infrastructure Library: best practices for IT service management (service strategy, design, transition, operation, continual improvement). Defines incident, problem, change and release management.

> On the exam: Scenario cue: 'framework for managing IT services and operations' → ITIL.
Don't confuse: ITIL = running IT services; COBIT = governing IT; ISO 27001 = security management system.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**ITIL (Information Technology Infrastructure Library):** the most widely used set of **best practices for IT service management (ITSM)**, i.e., how IT designs, delivers, runs and improves services for the business.

**Background**

- Created by the **UK government** (CCTA) in the 1980s; now owned by **AXELOS / PeopleCert**
- **ITIL v3 (2007/2011)** organized around a 5-stage **service lifecycle**: Service Strategy → Service Design → Service Transition → Service Operation → Continual Service Improvement
- **ITIL 4 (2019):** the **Service Value System**, service value chain, 7 guiding principles, and **34 practices**; fits Agile and DevOps
- ITIL is **guidance**; organizations certify against **ISO/IEC 20000** (the ITSM standard). Individuals get ITIL certifications

**Security-relevant practices**

- **Information security management:** protect information within IT services
- **Change enablement (change management):** assess, approve and control changes to reduce risk
- **Incident management:** **restore normal service as fast as possible**
- **Problem management:** find and remove the **root cause** of incidents
- **Release and deployment management:** move changes safely into production
- **Service configuration management:** track configuration items in a **CMDB**
- **Service level management:** agree and track SLAs
- **Continual improvement:** ongoing improvement (PDCA thinking)

**On the exam**

- 'IT service management best practices' → **ITIL**
- **Incident vs problem:** incident = **get it working again**; problem = **why did it happen / stop it recurring**
- ITIL ties to **operations** (Domain 7): change, configuration, incident, problem management
- **Don't confuse:** ITIL = IT service management; COBIT = IT governance; COSO = internal controls

**Quick check:** A production app has gone down three times this month. Each time, the ops team restored it quickly. Now a team is investigating why it keeps happening. Which ITIL practice is this?

**Answer:** **Problem management.** The first three outages were each handled by **incident management** (restore service fast). Investigating the **root cause** of the repeated outages so they stop recurring is **problem management**. Fixing it in production would then go through **change enablement**.

</details>

<a name="t-2-2-11"></a>
**COBIT**

Control Objectives for Information and related Technology (ISACA): framework for IT governance and control, linking IT to business goals.

> On the exam: Scenario cue: 'auditors need a framework for IT governance and controls' → COBIT. Often used with SOX compliance.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**COBIT (Control Objectives for Information and Related Technologies):** a framework for **governance and management of enterprise IT**, published by **ISACA**. Current version: **COBIT 2019** (previous: COBIT 5).

**Core purpose**

- **Align IT with business goals** so IT creates value
- Optimize IT **risk** and **resources**
- Give auditors and management a common set of **control objectives** for IT

**Key ideas**

- **Separates governance from management:**
  - **Governance** (board/executives) = set direction, decide priorities, monitor performance
  - **Management** (IT management) = plan, build, run and monitor activities to meet that direction
- **Goals cascade:** stakeholder needs → enterprise goals → alignment goals → governance and management objectives
- **40 governance and management objectives** grouped into 5 domains
- **Capability levels 0–5** (CMMI-based) to rate how mature a process is
- **Design factors** to tailor COBIT to the organization

**The 5 domains (know the governance one)**

- **EDM — Evaluate, Direct and Monitor** ← the **governance** domain
- **APO — Align, Plan and Organize** (management)
- **BAI — Build, Acquire and Implement** (management)
- **DSS — Deliver, Service and Support** (management)
- **MEA — Monitor, Evaluate and Assess** (management)

**Where it's used**

- **IT audits**, especially **SOX** compliance (COBIT covers the IT controls; COSO covers overall internal control)
- Building IT governance programs

**On the exam**

- 'IT governance', 'align IT with business goals', 'ISACA', 'control objectives' → **COBIT**
- **Don't confuse:** COBIT = IT **governance**; ITIL = IT **service management** (how to run services); COSO = enterprise **internal control** and financial reporting
- Board-level direction/oversight → **EDM**

**Quick check:** In a company using COBIT 2019, the board approves the IT strategy and later reviews whether IT is delivering the expected results. Which COBIT domain does this belong to?

**Answer:** **EDM (Evaluate, Direct and Monitor)**, the **governance** domain. Approving IT strategy (direct) and reviewing results (monitor) is the board's governance job. The other four domains (APO, BAI, DSS, MEA) are **management**, carried out by IT management.

</details>

<a name="t-2-2-12"></a>
**COSO**

Committee of Sponsoring Organizations: framework for internal controls and enterprise risk management, mainly over financial reporting.

> On the exam: Scenario cue: 'internal control framework used for SOX financial reporting' → COSO (COBIT covers the IT side).

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**COSO (Committee of Sponsoring Organizations of the Treadway Commission):** a US private-sector group (formed 1985 to fight **fraudulent financial reporting**) that publishes the most widely used **internal control** framework.

**The main frameworks**

- **Internal Control — Integrated Framework** (1992, updated **2013**): the one used for **SOX Section 404** compliance (internal control over financial reporting)
- **Enterprise Risk Management (ERM)** framework (2004, updated **2017**: 'Integrating with Strategy and Performance')

**Internal control: 3 objectives**

- **Operations:** effective and efficient operations
- **Reporting:** reliable financial and non-financial reporting
- **Compliance:** following laws and regulations

**Internal control: 5 components (memorize — mnemonic **CRIME**)**

- **C — Control environment:** the **'tone at the top'**: integrity, ethics, board oversight, structure. The **foundation** for everything else
- **R — Risk assessment:** identify and analyze risks to objectives (including **fraud** risk)
- **I — Information and communication:** getting the right info to the right people
- **M — Monitoring activities:** ongoing and separate evaluations of whether controls work
- **E — (Existing) control activities:** the actual controls: approvals, authorizations, reconciliations, **segregation of duties**, IT general controls
- Supported by **17 principles**; shown as the **COSO cube** (objectives × components × organization levels)

**On the exam**

- 'Internal controls', 'financial reporting', 'SOX', 'fraud', 'Treadway' → **COSO**
- 'Tone at the top' / leadership ethics → **control environment**
- **Don't confuse:** COSO = enterprise internal control (business-wide); COBIT = IT governance (often used together for SOX: COSO for the overall control framework, COBIT for IT controls); ITIL = IT service management

**Quick check:** The CEO and board consistently stress integrity and ethical behavior in every company meeting and set clear expectations for conduct. Which COSO internal control component does this represent?

**Answer:** **Control environment.** Leadership consistently emphasizing integrity and ethics is the **'tone at the top'**, which is the foundation component of COSO internal control.

</details>

<a name="t-2-2-13"></a>
**OASIS**

Standards body that produced security standards such as SAML (federated identity), XACML (access control policy language) and WS-Security (SOAP message security).

> On the exam: Scenario cue: 'XML language to express fine-grained authorization policies' → XACML (OASIS).

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**OASIS (Organization for the Advancement of Structured Information Standards):** a **nonprofit, international consortium** that develops **open standards**, especially for **security, identity, web services, cloud, IoT and data exchange**. Members are vendors, governments and individuals; standards are free to use.

**OASIS standards to know for CSSLP**

- **SAML (Security Assertion Markup Language):** XML-based exchange of **authentication and authorization assertions** between an identity provider and a service provider → **federated SSO** (very common on the exam)
- **XACML (eXtensible Access Control Markup Language):** XML language for writing and evaluating **fine-grained, attribute-based access control (ABAC) policies**. Architecture: **PEP** (enforces), **PDP** (decides), **PAP** (administers policy), **PIP** (supplies attributes)
- **WS-Security:** securing **SOAP web service messages** (signing, encrypting, attaching security tokens)
- **SPML (Service Provisioning Markup Language):** user account **provisioning** between systems
- **KMIP (Key Management Interoperability Protocol):** communication between **key management systems** and clients
- **STIX / TAXII:** format and transport for sharing **cyber threat intelligence**
- **CSAF (Common Security Advisory Framework):** machine-readable security advisories, including **VEX** (is a product actually affected by a CVE?)
- Others: **MQTT** (IoT messaging), **ODF** (OpenDocument Format)

**On the exam**

- 'SAML', 'XACML', 'WS-Security', 'SPML', 'KMIP' → **OASIS**
- Federated SSO with XML assertions → **SAML**; fine-grained ABAC policy → **XACML**
- **Don't confuse the standards bodies:** OASIS = SAML/XACML/WS-Security; **W3C** = XML, XML Signature, XML Encryption; **IETF** = TLS, OAuth 2.0, JWT (RFCs); **OpenID Foundation** = OpenID Connect

**Quick check:** A team needs a standard XML-based language to write fine-grained access control policies based on user attributes (department, clearance, time of day) and have a decision engine evaluate them. Which OASIS standard fits?

**Answer:** **XACML (eXtensible Access Control Markup Language).** It's the OASIS standard for writing fine-grained, attribute-based access control policies in XML and evaluating them. SAML would carry the user's identity/attributes between systems, but XACML is what expresses and decides the policy.

</details>

<a name="t-2-2-14"></a>
**Six Sigma**

Data-driven quality method aiming for near-zero defects (3.4 per million). Uses DMAIC: Define, Measure, Analyze, Improve, Control.

> On the exam: Security angle: measuring and reducing defects improves quality, which reduces vulnerabilities.
Scenario cue: 'process improvement using statistical defect reduction' → Six Sigma.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

**Six Sigma:** a **data-driven, statistical** methodology for improving quality by **reducing defects and process variation**. Started at **Motorola** (1986), made famous by **GE**.

**The number**

- A Six Sigma process produces no more than **3.4 defects per million opportunities (DPMO)**, i.e., about 99.99966% defect-free
- 'Sigma' = standard deviation; more sigmas between the process average and the failure limit = fewer defects

**Two core methods (know both)**

- **DMAIC** — for **improving an EXISTING process**:
  - **Define** the problem and goals
  - **Measure** current performance (baseline data)
  - **Analyze** data to find the **root cause**
  - **Improve** by fixing the root cause
  - **Control** to keep the gains (monitoring, standardization)
- **DMADV** (also **DFSS, Design for Six Sigma**) — for **designing a NEW process or product**:
  - **Define, Measure, Analyze, Design, Verify**

**Roles ('belts')**

- **Champion** (executive sponsor), **Master Black Belt**, **Black Belt** (leads projects full-time), **Green Belt** (part-time), **Yellow Belt**
- **Lean Six Sigma** = Six Sigma + Lean (eliminating waste)

**In software security**

- Treat vulnerabilities as **defects**: measure vulnerability density, find root causes, reduce variation between teams, keep improvements under control with metrics

**On the exam**

- '3.4 defects per million', 'DMAIC', 'reduce variation', 'statistical quality' → **Six Sigma**
- Existing process → **DMAIC**; new process/product → **DMADV**
- **Don't confuse:** PDCA = simple general improvement loop; Six Sigma = statistical, defect-focused; CMMI = process **maturity levels** (1–5)

**Quick check:** A team is building a brand-new secure release process from scratch and wants to use Six Sigma. Should they use DMAIC or DMADV?

**Answer:** **DMADV (Define, Measure, Analyze, Design, Verify)**, also called Design for Six Sigma. Clue words: *brand-new*, *from scratch*. DMAIC is for **improving an existing** process.

</details>

<a name="t-2-2-15"></a>
**Socratic methodology**

Handling people who resist security by questioning them back, often with their own question in negative form ('Why should we NOT protect this data?').

> On the exam: Purpose: gets resistant stakeholders to reason through security needs themselves rather than being told.
Scenario cue: 'a stakeholder argues security isn't needed; which technique?' → Socratic method.

<details><summary>Lesson (09 Oct 2026)</summary>

**What it is**

A way to handle people who **resist or disagree with security**, by **asking questions** instead of arguing or lecturing. Named after the Greek philosopher Socrates, who taught by questioning.

**How it works**

- Don't tell the person they're wrong; **ask questions** that lead them to think it through
- A classic CSSLP technique: **turn their objection into a question, often in negative form**
- They say: 'Why do we need input validation?' → You ask: '**Why should we NOT validate input?**' or 'What could happen if someone sends malicious input?'
- The person reasons through the consequences and **reaches the conclusion themselves**

**Why it works**

- People accept conclusions they reach themselves more readily than ones they're told
- Reduces defensiveness and conflict
- Builds real understanding and **buy-in**, not just compliance
- Surfaces genuine concerns (cost, deadlines) that can then be addressed

**Where it's useful**

- Stakeholders who see security as unnecessary cost
- Developers who push back on secure coding rules
- Requirement-gathering sessions where security needs are questioned

**On the exam**

- 'A stakeholder argues security isn't needed; which technique helps?' → **Socratic methodology**
- Key feature: **asking questions, often turning the question around in negative form**
- **Trap:** it's not about forcing compliance through policy; it's about guiding people to understand

**Quick check:** A product manager says, 'We don't need to encrypt customer passwords; nobody will hack us.' How would you respond using the Socratic method?

**Answer:** Use the **Socratic method**: instead of arguing, ask questions that lead him to reason it out, e.g., 'Why should we NOT encrypt customer passwords?', 'What would happen to our customers and our company if the database leaked?', 'How would we explain to customers that we skipped it?' He reaches the conclusion himself, which builds buy-in.

</details>

## 2.3 Strategy and roadmap

<a name="t-2-3-1"></a>
**Security milestones and checkpoints**

Defined points in the lifecycle where security is reviewed.

> On the exam: What it's for: puts security checks at planned points in the project (end of requirements, design, before release) so security isn't left to the end.
Scenario cue: 'how do you make sure security is reviewed throughout the project?' → define milestones and checkpoints in the project plan.
Don't confuse: a checkpoint is a review; a gate can stop the project.

<details><summary>Lesson (10 Oct 2026)</summary>

**What it is**

**Security milestones (checkpoints)** are **planned points in the project** where security work is **reviewed**. They make sure security happens throughout the lifecycle, not just at the end.

**Typical security checkpoints**

- **Requirements:** security requirements defined and approved; bug bar agreed
- **Design:** threat model done; security design/architecture review
- **Implementation:** secure code review; SAST results reviewed
- **Testing:** security testing, DAST, penetration test done
- **Release:** **Final Security Review (FSR)**; incident response plan ready

**Why they matter**

- **Find problems early,** when they're cheap to fix (cost of defects curve)
- **Visibility:** management sees security status at each stage
- **Evidence:** documented reviews for auditors and compliance
- **Accountability:** each checkpoint has an owner and sign-off

**Where they come from**

- Built into the **strategy and roadmap** for the software security program
- In Waterfall: at the end of each phase. In Agile: per sprint/release (Definition of Done, release readiness)

**On the exam**

- 'Defined points in the lifecycle where security is reviewed' → **security milestones / checkpoints**
- **Don't confuse:** a milestone is **where you look**; a **gate** is a checkpoint you **must pass** to continue (next topic)
- **Trap:** security only at the end (one big test before release) = no checkpoints = expensive late fixes

**Quick check:** A team says, 'We do security testing at the very end, right before release. Why do we need security checkpoints earlier in the project?' Give two reasons.

**Answer:** 1) **Cost:** a flaw found at the design checkpoint (e.g., missing authentication in the threat model) is far cheaper to fix than one found just before release. 2) **No surprises:** checkpoints spread security across the lifecycle, so problems surface while there's still time to fix them instead of delaying the release or shipping with known risk. (Also: they create evidence for auditors and let management see security status at each stage.)

</details>

<a name="t-2-3-2"></a>
**Control gates / quality gates**

The project can't move to the next phase until criteria are met.

> On the exam: What it's for: the project can't move forward until security criteria are met, e.g., no design sign-off without an approved threat model, no release with open criticals.
Scenario cue: 'teams keep skipping the threat model' → make it a gate requirement.
Don't confuse: gates are go/no-go; milestones just mark progress.

<details><summary>Lesson (10 Oct 2026)</summary>

**What it is**

A **control gate** (also called a **phase gate**, **stage gate**, or **quality gate**) is a checkpoint **with teeth**: the project **cannot move to the next phase** until it meets defined **exit criteria**.

**Milestone vs gate**

- **Milestone / checkpoint:** a point where security is **reviewed**
- **Gate:** a point where a **go / no-go decision** is made; failing **blocks progress**

**Possible gate decisions**

- **Go:** criteria met, move on
- **No-go:** stop; fix and come back (or cancel the project)
- **Go with conditions:** proceed, but with tracked actions and deadlines (a documented exception)

**Examples of security gate criteria**

- **Requirements gate:** security requirements and bug bar approved
- **Design gate:** threat model reviewed; high risks have mitigations
- **Code gate:** no high/critical SAST findings; code review done
- **Release gate:** pen test findings fixed; **Final Security Review (FSR)** passed

**Manual vs automated gates**

- **Manual:** review meetings and sign-offs (typical in Waterfall)
- **Automated quality gates:** the **CI/CD pipeline fails the build** if criteria aren't met (e.g., SAST finds a high-severity issue) → fits Agile/DevSecOps without slowing teams

**Exceptions**

- Bypassing a gate requires a **documented risk acceptance** by the **accountable business owner** (security advises), with conditions and an expiry date

**On the exam**

- 'Project can't proceed until criteria are met' → **control/quality gate**
- 'Pipeline blocks the build when a scan finds critical issues' → **automated quality gate**
- **Trap:** a gate without clear, pre-agreed criteria is just a meeting; criteria must be defined in advance (→ bug bar, next topic)
- **Trap:** a gate is **not** bypassed by whoever is in a hurry; exceptions go through risk acceptance

**Quick check:** A CI/CD pipeline blocks any release when SAST finds a high-severity issue. A product manager wants to push a release past it for an important demo tomorrow. What is this pipeline check called, and how should the exception be handled?

**Answer:** It's an **automated quality gate** (a security gate in the CI/CD pipeline). The product manager can't simply bypass it. An exception needs a **documented risk acceptance** signed by the **accountable business owner** (security advises on the risk), ideally with conditions and an expiry date, e.g., 'demo environment only, fix within 7 days.'

</details>

<a name="t-2-3-3"></a>
**Break/build criteria (bug bar)**

Rules for when a build fails, e.g., any critical vulnerability blocks release.

> On the exam: Agreed up front so release decisions are objective. If a critical flaw appears before launch, shipping anyway is a risk acceptance decision for the business owner, not the developer.

<details><summary>Lesson (10 Oct 2026)</summary>

**What it is**

**Break/build criteria**, also called the **bug bar**: rules **agreed in advance** that decide which security bugs are serious enough to **fail the build or block the release**. The term comes from the **Microsoft SDL**.

**How it works**

- Uses a **severity rating** for every bug, e.g., Critical / High / Medium / Low, or a **CVSS** score (Common Vulnerability Scoring System, 0-10)
- Sets a **rule for each level**, for example:
  - **Critical / High:** must be fixed before release → **break the build**
  - **Medium:** fix within a set time (e.g., 30 days) or by the next release
  - **Low:** goes to the backlog
- The bar can be **stricter for high-risk apps** (sensitive data, internet-facing)

**When it's set (heavily tested)**

- In the **requirements phase**, at the **start** of the project (Microsoft SDL: Requirements)
- Agreed by security, development and the business owner
- Then **applied** at gates and especially at the **Final Security Review (FSR)** before release

**Why it matters**

- **Objective:** no arguing about each bug at the last minute
- **Consistent:** same rule for every team and release
- **Gives gates their criteria:** a gate checks findings against the bug bar

**How the three 2.3 topics fit together**

- **Milestone** = **where** we stop and review
- **Gate** = **must pass** to continue
- **Bug bar** = **the rule** the gate uses to decide pass/fail

**On the exam**

- 'Any critical vulnerability blocks the release' → **bug bar / break-build criteria**
- 'When should the bug bar be defined?' → **requirements phase / early**
- **Trap:** defining it at release time = too late, invites negotiation
- **Trap:** the bug bar is not the gate; it's the **criteria** the gate uses
- Shipping with a bug above the bar → documented **risk acceptance** by the accountable owner

**Quick check:** During the Final Security Review, the team spends hours arguing whether a medium-severity XSS should block the release. What was missing, and when should it have been set?

**Answer:** A **bug bar** (break/build criteria) was missing. It should have been agreed in the **requirements phase**, at the start of the project, so the FSR simply checks the findings against the pre-agreed rule instead of debating it. (If the business wants to ship with a finding above the bar, that needs documented risk acceptance by the accountable owner.)

</details>

## 2.4 Security documentation

<a name="t-2-4-1"></a>
**Policy**

High-level, mandatory statement of management intent.

> On the exam: What it is: senior management's high-level, mandatory statement of intent, e.g., 'all customer data must be protected'. Technology-neutral and rarely changes.
Scenario cue: 'what does management issue first to show commitment?' → a policy.
Order of the hierarchy: policy → standards → procedures/baselines, with guidelines as optional advice.

<details><summary>Lesson (10 Oct 2026)</summary>

**Taught together: Policy, Standard, Procedure, Guideline**

**The document hierarchy**

- **Policy** (top) → supported by **Standards** and **Baselines** → carried out through **Procedures**
- **Guidelines** sit alongside as optional advice
- Each lower document must **support** the one above it

**Policy**

- **High-level statement of management intent**: WHAT and WHY, never HOW
- **Mandatory**; approved and signed by **senior management** (shows commitment = governance)
- **Technology-neutral**: doesn't name products or algorithms
- Short; **changes rarely**
- Types: **organizational/program** policy (the overall security program), **issue-specific** (acceptable use, passwords, remote work), **system-specific** (rules for one system)
- Example: 'The company protects customer data from unauthorized disclosure.'

**Standard**

- **Mandatory, specific** requirement that supports a policy
- **Technology-specific and measurable**: 'Use AES-256', 'TLS 1.2 or higher', 'passwords at least 14 characters'
- Can be **internal** or adopted **external** standards (ISO, PCI DSS)
- Changes when technology changes

**Procedure**

- **Mandatory step-by-step instructions** (HOW) for a specific task
- Most detailed; **changes most often**
- Gives **consistency** (everyone does it the same way) and **audit evidence**
- Example: '1. Generate the new key 2. Update the vault 3. Redeploy 4. Revoke the old key'

**Guideline**

- **Recommended, NOT mandatory**; flexible advice
- Used where a strict rule doesn't fit every case
- Example: 'Employees should consider using a password manager.'

**Quick sorting rules**

- **Mandatory:** policy, standard, baseline, procedure. **Optional:** guideline only
- Changes least → most: **policy → standard → procedure**

**On the exam**

- 'Management intent', broad, no technology → **policy**
- 'Must' + specific technology/number → **standard**
- Numbered steps → **procedure**
- 'Should', 'recommended', 'consider' → **guideline**
- **Trap:** a policy that names a specific algorithm is badly written; that detail belongs in a standard
- **Trap:** guidelines are the ONLY optional document

**Quick check:** Classify each: (a) 'The company protects customer data from unauthorized disclosure.' (b) 'Employees should lock their screens when stepping away.' (c) 'Passwords must be at least 14 characters.' (d) '1. Open the vault console. 2. Generate a new key. 3. Revoke the old key.'

**Answer:** (a) **Policy:** broad management intent, no technology named. (b) **Guideline:** 'should' = recommended, optional. (c) **Standard:** 'must' + a specific, measurable requirement. (d) **Procedure:** numbered step-by-step instructions.

</details>

<a name="t-2-4-2"></a>
**Standard**

Mandatory, specific requirement (e.g., use AES-256).

> On the exam: What it is: a mandatory, specific rule that supports a policy, e.g., 'use TLS 1.2 or higher', 'passwords at least 14 characters'.
Scenario cue: 'which document mandates a specific technology or setting?' → standard.
Don't confuse: a policy says what and why; a standard says which specific technology or value.

<details><summary>Lesson (10 Oct 2026)</summary>

**Taught together with Policy (see 2.4.1)**

**Standard**

- **Mandatory, specific** requirement that supports a policy
- **Technology-specific and measurable**: 'Use AES-256', 'TLS 1.2 or higher'
- Can be **internal** or adopted **external** (ISO, PCI DSS)
- Changes when technology changes

**On the exam**

- 'Must' + specific technology/number → **standard**
- Framework = Flexible; Standard = Strict

**Quick check:** Which statement is a standard: 'We protect customer data' or 'All laptops must use full-disk encryption with AES-256'?

**Answer:** See lesson 2.4.1 (Policy, Standard, Procedure and Guideline are taught together). Standard = mandatory + specific + measurable, e.g., 'Passwords must be at least 14 characters.'

</details>

<a name="t-2-4-3"></a>
**Procedure**

Mandatory step-by-step instructions.

> On the exam: What it is: mandatory, step-by-step instructions for a task, e.g., how to deploy a patch or rotate a key.
Scenario cue: 'different admins perform the same task differently and errors occur' → write a procedure.
Don't confuse: a procedure is how; a standard is what.

<details><summary>Lesson (10 Oct 2026)</summary>

**Taught together with Policy (see 2.4.1)**

**Procedure**

- **Mandatory step-by-step instructions** (HOW) for a specific task
- Most detailed; **changes most often**
- Gives **consistency** and **audit evidence**

**On the exam**

- Numbered steps → **procedure**

**Quick check:** A document lists the 4 steps to rotate an API key. What type is it?

**Answer:** See lesson 2.4.1. Procedure = mandatory numbered step-by-step instructions, e.g., the key rotation steps.

</details>

<a name="t-2-4-4"></a>
**Guideline**

Recommended, not mandatory.

> On the exam: What it is: recommended advice that isn't mandatory, e.g., tips for writing secure code comments.
Scenario cue: 'which document gives flexibility for situations not covered by standards?' → guideline.
Trap: guidelines are the only document in the hierarchy that is optional.

<details><summary>Lesson (10 Oct 2026)</summary>

**Taught together with Policy (see 2.4.1)**

**Guideline**

- **Recommended, NOT mandatory**; flexible advice
- The **only optional** security document

**On the exam**

- 'Should', 'recommended', 'consider' → **guideline**

**Quick check:** 'Employees should consider using a password manager.' Mandatory or optional, and what type?

**Answer:** See lesson 2.4.1. Guideline = recommended, optional ('should', 'consider').

</details>

<a name="t-2-4-5"></a>
**Baseline**

Minimum security configuration level.

> On the exam: What it is: the minimum required security configuration for a system type, e.g., a hardened server image based on CIS Benchmarks.
Scenario cue: 'how do we make sure all new servers start with the same minimum security?' → baseline.
Used for: detecting drift, since anything below the baseline is a finding.

<details><summary>Lesson (10 Oct 2026)</summary>

**What it is**

A **baseline** is the **minimum security configuration** every system of a given type **must** meet. It's **the floor**: you can go above it, never below.

**Example: Windows server baseline**

- Insecure protocols disabled (e.g., SMBv1)
- Default accounts removed/renamed
- Logging on, host firewall on, unneeded services off

**Sources**

- **CIS Benchmarks** (Center for Internet Security): most common
- **DISA STIGs** (US DoD Security Technical Implementation Guides)
- Vendor hardening guides; NIST National Checklist Program

**Baseline vs standard (both mandatory)**

- **Standard:** one specific rule ('TLS 1.2+')
- **Baseline:** the **full set of settings** for a type of system

**How it's used**

- **Hardening:** build new systems to it, often from a **golden image** (pre-hardened template) or infrastructure as code
- **Detect configuration drift:** compare current settings against the baseline with regular (ideally automated) compliance scans; **bring the system back** to the baseline
- The baseline itself changes **only through change control** (e.g., new benchmark version), never to match drift
- **Exceptions:** documented risk acceptance

**On the exam**

- 'Minimum security configuration all servers must meet' → **baseline**
- 'CIS Benchmark' / 'STIG' → baseline sources
- 'Systems no longer match approved configuration' → **configuration drift**
- **Trap:** baseline = minimum and mandatory, not a guideline
- **Trap:** fix drift by restoring systems to the baseline, not by rewriting the baseline

**Quick check:** An audit finds 30 of 200 web servers have TLS 1.0 turned back on and default admin accounts active, even though all were built correctly. What is this problem called, and what should they have been checked against?

**Answer:** **Configuration drift.** The servers should be checked against the **security baseline** (e.g., a CIS Benchmark) with regular automated compliance scans, and the drifted settings put back to match it. **Trap:** you do NOT change the baseline to match the drift; the systems are brought back to the baseline. The baseline itself only changes through formal change control (e.g., a new CIS version).

</details>

<a name="t-2-4-6"></a>
**Lifecycle documents**

Threat models, security requirements, architecture docs, test plans, runbooks.

> On the exam: What's included: security requirements, threat models, architecture/design docs, test plans and results, deployment and hardening guides, runbooks, incident response plans.
Why it matters: lets others review, audit, maintain and respond to incidents. Missing documentation is a common audit finding.
Scenario cue: 'a new team inherits an app and can't tell what controls exist' → documentation failure.

<details><summary>Lesson (10 Oct 2026)</summary>

**What it is**

**Lifecycle documents** are the security documents produced **throughout the SDLC**. They record what was decided, built and tested.

**Key documents by phase**

- **Requirements:** security requirements; **Requirements Traceability Matrix (RTM)**: a table linking each requirement to its design, code and test, so nothing gets dropped
- **Design:** **threat model**, security architecture/design docs, **data flow diagrams**, data classification
- **Implementation:** secure coding standard, code review records, SAST results
- **Testing:** **security test plan**, test results, penetration test report
- **Release:** **FSR** report, risk acceptance records, **SBOM**, release notes, **secure installation / hardening guide** for customers
- **Operations:** **runbooks** (step-by-step operational guides), incident response plan, baseline/configuration docs
- **Retirement:** decommissioning plan (2.6)

**Why they matter**

- **Knowledge transfer:** people leave; documents stay
- **Consistency** across teams and releases
- **Audit and compliance evidence**
- **Accountability:** who decided and signed off

**Keep them alive**

- **Version-controlled** and **updated when things change** (e.g., redo the threat model when the design changes)
- Outdated documents are a risk: people trust wrong information
- In Agile: 'just enough' documentation, but security artifacts are still required

**On the exam**

- 'Prove every security requirement was designed, built and tested' → **RTM**
- 'Operations staff follow it for routine tasks or incidents' → **runbook**
- 'Tells customers how to deploy the product securely' → **secure installation / hardening guide**
- **Trap:** a threat model is a living document, not a one-time file

**Quick check:** An auditor asks the team to prove that every security requirement was actually designed, built and tested. Which document provides this?

**Answer:** The **Requirements Traceability Matrix (RTM)**. It links each security requirement to where it was designed, built and tested, proving nothing was dropped.

</details>

## 2.5 Security metrics

<a name="t-2-5-1"></a>
**KPI vs KRI**

KPI measures performance against a goal; KRI signals rising risk.

> On the exam: KPI example: % of apps scanned before release. KRI example: number of unpatched critical vulnerabilities is rising.

<details><summary>Lesson (13 Oct 2026)</summary>

**KPI vs KRI**

- METRIC = a number tracked over time to show if security is improving.
- KPI (Key Performance Indicator) = how well we are DOING against a goal; past results. e.g. 95% of devs trained; 90% of criticals fixed in 30 days.
- KRI (Key Risk Indicator) = how much DANGER is building; early warning before an incident. e.g. unpatched criticals >30 days jumped 5 to 40.

**Test**

- "How well are we performing?" = KPI. "Is trouble coming?" = KRI.
- Exam cues: performance, goal, target, achieved, efficiency = KPI. Risk exposure, threshold, early warning, trending up, tolerance = KRI.

**Trap**

- same data can feed both
- read what the number is USED FOR.

**Hook**

- Performance = Past results. Risk = Red flag ahead.

**Quick check:** Board is notified when more than 10 apps run end-of-life components, so it can act before an incident. KPI or KRI?

**Answer:** KRI. Correct. Clue words: exceeds (threshold), notified, before an incident (early warning).

</details>

<a name="t-2-5-2"></a>
**Objectives and key results (OKRs)**

Goals paired with measurable results.

> On the exam: The objective is qualitative ('reduce release risk'); key results are measurable ('zero critical findings at release').

<details><summary>Lesson (13 Oct 2026)</summary>

**OKRs**

- OKR = Objectives and Key Results (Intel/Google goal-setting).
- OBJECTIVE = the goal in words, inspiring, NO numbers. e.g. Make our apps resistant to common web attacks.
- KEY RESULTS = 2-5 measurable outcomes with numbers + deadline proving the objective was met. e.g. Zero critical OWASP Top 10 findings in Q4 pen tests.
- KPI vs OKR: KPI = ongoing health check (dashboard). OKR = change toward a target in a set period, usually a quarter (GPS destination). A KPI can become a key result.
- Exam cues: objective, key results, quarterly goal, align teams to strategy, ambitious target = OKR.

**Traps**

- objective has no number
- a key result is an OUTCOME not an activity (run a workshop = activity).

**Hook**

- O = where we are going (words). KR = proof we got there (numbers).

**Quick check:** Which line is the key result? A culture of secure development / B hold four workshops / C reduce vuln density 3 to 1 per KLOC by end of Q2

**Answer:** C. Correct. A = objective (no number), B = activity, C = measurable outcome + deadline.

</details>

<a name="t-2-5-3"></a>
**Criticality level**

Ranking vulnerabilities or systems by importance and severity.

> On the exam: What it is: rating how important a system or how severe a vulnerability is (e.g., critical/high/medium/low).
Why it matters: lets you spend effort where risk is highest: critical flaw in a critical system gets fixed first.
Scenario cue: 'limited time, many findings, what first?' → highest criticality on the most critical asset.

<details><summary>Lesson (13 Oct 2026)</summary>

**Criticality level**

- Criticality = how important an app/system/vuln is to the business (how bad if hacked or down).

**Why metrics need it**

- raw counts lie
- criticality weights numbers and sets fix order.
- Assets: Critical/High/Medium/Low from a Business Impact Analysis (BIA: if we lose this system, what happens?). Business owner decides, security advises.
- Vulnerabilities: CVSS 0-10 = TECHNICAL severity (9.0-10 Critical); does not know business value.
- Fix order = severity of flaw + criticality of asset (+ exposure).

**On the exam**

- prioritize by business impact = criticality
- tier apps so most important get most testing = criticality/tiering.

**Trap**

- fix highest CVSS first is wrong when business impact or exposure is mentioned.

**Don't confuse**

- criticality = how much business needs the system
- data classification = how sensitive the information is.

**Quick check:** CVSS 9.8 in isolated internal demo app (no customer data, no internet) vs CVSS 7.5 in internet-facing payment system. Fix which first?

**Answer:** Finding 2 (payment system). Correct: low business impact + no exposure for demo app; payment app is critical and internet-facing.

</details>

<a name="t-2-5-4"></a>
**Average remediation time**

Mean time to fix vulnerabilities, usually tracked by severity.

> On the exam: What it is: mean time to remediate (MTTR), the average time between finding a vulnerability and fixing it, usually per severity.
Why it matters: shows whether the fixing process works and whether SLAs (e.g., criticals in 7 days) are met.
Scenario cue: 'how do we measure if the vulnerability management process is improving?' → falling mean time to remediate.

<details><summary>Lesson (13 Oct 2026)</summary>

**Average remediation time**

- Average remediation time = MTTR (mean time to remediate): average days from DISCOVERY to VERIFIED FIX.
- Remediation = a real fix (code change, patch, config), not a temporary workaround.
- Calc: sum of days open / number fixed (10, 20, 30 days = 20 average).

**Why**

- window of exposure = time attackers have
- lower MTTR shrinks it.

**Use properly**

- split by severity
- compare to SLAs (e.g. critical 7-15 days, high 30)
- watch the trend.

**Weaknesses**

- averages hide outliers
- MTTR only counts FIXED bugs, so still-open old bugs are invisible. Also track age of open vulns and % fixed within SLA. Measure to verified fix.

**On the exam**

- how quickly the team fixes after discovery = MTTR. Mainly a KPI
- if framed as rising danger, used as a KRI.

**Trap**

- good overall average can hide old critical bugs
- better answer breaks down by severity.

**Quick check:** MTTR 12 days vs 30-day target, but a critical SQLi has been open 200 days. How can both be true and what to track?

**Answer:** Correct: average hides it; break down by severity. Added: MTTR only counts fixed bugs, so an open bug is not in it; track age of open vulns + % within SLA.

</details>

<a name="t-2-5-5"></a>
**Complexity metrics**

E.g., cyclomatic complexity. More complex code tends to have more defects.

> On the exam: What it is: measures how complicated code is. Cyclomatic complexity counts independent paths through code.
Why it matters: complex code has more bugs and is harder to test and review.
Scenario cue: 'where should manual review focus?' → the most complex, highest-risk modules.

<details><summary>Lesson (13 Oct 2026)</summary>

**Complexity metrics**

- Complexity metrics = how complicated code is; complex code is harder to understand/test/review, so bugs hide there.
- Link: economy of mechanism (Saltzer & Schroeder, 1.2).
- Cyclomatic complexity (McCabe) = number of independent paths; each if/else/loop/case adds one. No decisions = 1. >10 risky (refactor); 20-50 very hard to test. Score = MINIMUM number of test cases to cover all paths.
- Others: LOC/KLOC (size), coupling (dependence between modules), depth of inheritance/nesting.

**Use**

- aim code review + extra testing at most complex modules
- quality gate on threshold
- SonarQube/SAST report it.

**On the exam**

- count of independent paths = cyclomatic complexity
- most intense review = highest complexity + criticality.

**Trap**

- complexity does not PROVE a vuln
- shows where vulns are MORE LIKELY = risk indicator.

**Quick check:** Auth module cyclomatic complexity 45, all others under 10. What does it mean, what to do?

**Answer:** Correct: very complicated, higher likelihood of vulns, risk indicator, reduce complexity (refactor). Added: first give it extra code review/testing now (auth is critical), refactor below 10; vulns are more LIKELY, not proven.

</details>

<a name="t-2-5-6"></a>
**Defect / vulnerability density**

Defects per thousand lines of code (KLOC).

> On the exam: What it is: number of defects or vulnerabilities per size of code, e.g., per thousand lines (KLOC).
Why it matters: lets you fairly compare a small app with a large one, or track quality across releases.
Trap: raw counts are misleading; a big app naturally has more bugs.

<details><summary>Lesson (13 Oct 2026)</summary>

**Defect / vulnerability density**

- Density = defects or vulns per amount of code, usually per KLOC (1,000 lines).
- Defect = any bug; vulnerability = exploitable defect (every vuln is a defect, not every defect a vuln).
- Calc: count / KLOC (30 vulns in 15,000 lines = 2 per KLOC).

**Why density not count**

- fair comparison across app sizes (50 in 100 KLOC = 0.5 vs 10 in 5 KLOC = 2
- smaller app is 4x buggier).

**Uses**

- compare teams/apps/releases
- trend across releases
- release criteria in a bug bar (e.g. no release above 1 vuln/KLOC).

**Weaknesses**

- more testing finds more bugs (density rises when detection improves)
- LOC varies by language/style
- treats all bugs equal, so pair with severity + criticality.

**On the exam**

- vulns per thousand lines = vulnerability density
- compare apps of different sizes fairly = density.

**Trap**

- a jump after adding a new SAST tool = better DETECTION, not worse code.

**Quick check:** Density 1.2 to 2.5 per KLOC after new thorough SAST tool. Manager says devs got careless. Justified?

**Answer:** Not justified. Correct: the tool improved detection of bugs already there. Added: fair comparison = rescan last release with the new tool.

</details>

<a name="t-2-5-7"></a>
**Leading vs lagging indicators**

Leading predicts future problems; lagging reports what already happened.

> On the exam: Leading indicators predict future results (e.g., % of developers trained, % of projects with threat models). Lagging indicators measure past results (e.g., number of incidents, vulnerabilities found in production).
Scenario cue: 'which metric helps prevent problems before they happen?' → a leading indicator.

<details><summary>Lesson (13 Oct 2026)</summary>

**Leading vs lagging indicators**

- LAGGING = measures what already happened (the result). e.g. incidents/breaches last quarter, vulns found in production, cost of incidents. Easy to measure; damage already done.
- LEADING = predicts what is likely to happen so you can act before. e.g. % devs trained, % projects with threat model, % code SAST-scanned before merge, open high-risk findings growing. Gives time to prevent; not a guarantee.

**Analogy**

- rear-view mirror = lagging
- windshield = leading.

**Fit**

- KRIs usually leading
- many KPIs lagging
- complexity = leading
- incident counts = lagging. Use both.
- TEST: Is this number the security OUTCOME itself (incidents, breaches, losses)? = lagging. Is it an activity/condition that PREDICTS the outcome? = leading. Ignore past tense: "% passed training" is past tense but still leading.

**On the exam**

- predicts / early warning / act before = leading. Past results / after the fact = lagging.

**Traps**

- zero incidents last quarter is lagging and does not prove security. Prevent problems = pick leading.

**Quick check:** Sort: 1 breaches this year; 2 % features with threat model before coding; 3 avg cost per incident last quarter; 4 % devs passed secure coding training.

**Answer:** My answer: lagging 1,3,4; leading 2. Score 3/4. #4 is LEADING: training predicts fewer bugs; past tense fooled it. Marked shaky.

</details>

<a name="t-2-5-8"></a>
**Good metrics**

Specific, measurable, repeatable, consistent, and tied to business goals.

> On the exam: Good metrics are SMART: specific, measurable, achievable, relevant, time-bound. They're collected consistently, cheap to gather, and support a decision.
Scenario cue: 'management ignores the security report' → metrics aren't tied to business goals or aren't actionable.

<details><summary>Lesson (13 Oct 2026)</summary>

**What makes a good metric**

- Good metric = useful for decisions.
- SMART: Specific, Measurable (ideally automated), Achievable/Actionable, Relevant (tied to business goal/risk), Time-bound.
- Also: Consistent (same tools/definitions), cheap to collect, actionable (drives a decision; if not = vanity metric), meaningful to the audience (board = business risk; devs = specific findings).
- Gaming / Goodhart's law: when a number becomes a target, people hit it without improving security (close tickets as won't fix). Defense: pair metrics (speed + verified quality), audit.

**On the exam**

- BEST metric = specific, measurable, tied to business risk, actionable. Poor: number of firewall rules, pages of policy written, scans run.

**Traps**

- easy to collect but drives no decision = vanity metric. For the board, present business risk, not raw technical counts.

**Hook**

- Busy is not better. Count RESULTS, not ACTIVITY.

**Quick check:** Board metric: A total SAST scans run 12,400 vs B critical vulns in customer-facing apps fixed within SLA rose 60% to 92%.

**Answer:** I chose A (wrong). Answer B: specific, tied to business risk, outcome not activity, trend, board-friendly. A = activity/vanity metric. Marked shaky.

</details>

## 2.6 Decommission applications

<a name="t-2-6-1"></a>
**End of Life (EOL) policy**

Plan for retiring software securely.

> On the exam: Retirement is part of the lifecycle. Forgotten apps keep running with open accounts and unpatched flaws.

<details><summary>Lesson (13 Oct 2026)</summary>

**End of Life (EOL) policy**

- EOL policy = management-level policy for retiring software safely.
- End of Life = product officially finished (not sold/improved/eventually supported); declared by a vendor or by your own company.

**Why**

- without it apps are forgotten, not retired = ORPHANED systems (old code, unpatched libs, active accounts, live data, nobody watching).

**Covers**

- who decides (business owner, security advises)
- retirement criteria
- notice periods
- data (keep/archive/destroy)
- remove accounts/keys/certs
- update asset inventory/docs.

**When to plan**

- from the START (Requirements/Design), though Disposal is the last SDLC phase.

**On the exam**

- software still running after no longer needed/patched = missing EOL policy/decommissioning. Approves retirement = business owner.

**Traps**

- decommissioning is not just turning the server off. Plan retirement early in the SDLC.

**Quick check:** Old customer portal replaced 3 years ago still on the internet with a working DB connection. What was missing, what risk?

**Answer:** Correct: missing EOL/retirement policy; attackers can break in and reach data not disposed of. Added: orphaned (unpatched, unmonitored); live DB connection = pivot into the CURRENT database.

</details>

<a name="t-2-6-2"></a>
**End of support (EOS)**

Vendor stops patches; continued use is a risk to accept or mitigate.

> On the exam: What it is: the vendor stops patches and support (Windows 7, old Java versions).
Options: upgrade or replace (best), isolate it with compensating controls like segmentation, or formally accept the risk.
Scenario cue: 'a critical app depends on an unsupported OS' → compensating controls plus a migration plan, with documented risk acceptance meanwhile.

<details><summary>Lesson (13 Oct 2026)</summary>

**End of support (EOS)**

- EOS = date vendor stops support, most importantly SECURITY PATCHES. Software still works; new vulns never fixed.
- EOL vs EOS: EOL = product finished (not sold/developed). EOS = no more patches/help, often AFTER EOL. For security, EOS is the date that matters.

**Danger**

- attackers watch EOS dates
- permanent unpatched holes
- compliance failures (PCI DSS needs supported software)
- applies to libraries/frameworks too (SBOM shows EOS components).

**Options**

- upgrade/migrate (BEST)
- extended paid support (temporary)
- compensating controls (isolate segment, WAF, restrict access, monitor)
- documented risk acceptance by business owner with expiry. Never: keep using silently = unmanaged risk.
- Compensating control = alternative safeguard when the normal control (patching) is not possible.

**On the exam**

- vendor no longer releases patches = EOS. Best = upgrade
- if impossible now = compensating controls + documented risk acceptance.

**Traps**

- still works fine is not safe
- extended support is temporary.

**Quick check:** Hospital imaging system on EOS OS; cannot move to new OS until next year. What meanwhile?

**Answer:** Correct options (extended support, risk acceptance, isolate). Exam-best answer COMBINES: isolate + restrict + monitor, extended support if available, documented risk acceptance by business owner with expiry = migration date. Not OR.

</details>

<a name="t-2-6-3"></a>
**Credential and configuration removal**

Delete accounts, keys, certificates, firewall rules and configs tied to the app.

> On the exam: The most common decommissioning mistake: service accounts, API keys and certificates left active after shutdown.

<details><summary>Lesson (13 Oct 2026)</summary>

**Credential and configuration removal**

- At retirement remove everything that lets someone/something access the app or lets it access others.
- Remove/revoke: user/admin/SERVICE accounts; secrets (API keys, passwords, connection strings, tokens); certificates (REVOKE via CA, not just delete); firewall rules, ports, VPN, load balancer entries; DNS records; scheduled jobs, webhooks, integrations; config files.

**Why**

- orphaned credentials (dead app service account still reaching live DB)
- dangling DNS = SUBDOMAIN TAKEOVER (attacker claims released cloud address, hosts content on your domain)
- leftover firewall holes.

**How**

- asset inventory + CMDB (list of IT components and connections)
- decommissioning checklist/procedure
- verify removal by scanning.

**On the exam**

- retired app service account used on prod DB = credentials not removed. Attacker content on old subdomain = subdomain takeover / dangling DNS.

**Traps**

- revoke certificates, do not just delete. Shutting the server does not remove accounts/keys on OTHER systems.

**Quick check:** Old reporting server shut down; 6 months later svc_reporting logs into main customer DB. What went wrong, what should have been done?

**Answer:** Correct: credentials not retired; remove/revoke accounts, DNS, secrets, certs. Added: account lived on the DB, so server shutdown did not touch it; now treat logins as a possible incident and investigate.

</details>

<a name="t-2-6-4"></a>
**License cancellation and SLAs**

End contracts and services so they aren't left running or billed.

> On the exam: What it means: when retiring an app, cancel licenses, cloud subscriptions and support contracts, and end the SLAs.
Why it matters: forgotten cloud services keep costing money and stay exposed to the internet.
Scenario cue: 'an old test environment is still running and was breached' → incomplete decommissioning.

<details><summary>Lesson (13 Oct 2026)</summary>

**License cancellation and SLAs**

- At retirement end contracts and paid services so nothing is left running, billed or exposed.
- Terms: license = paid right to use software; SLA = contract promising service level (uptime, support); SaaS = rented online software.
- Cancel/close: software licenses; cloud resources (VMs, buckets, DBs, backups); SaaS subscriptions + third-party services; support/maintenance contracts; hosting/SLA agreements.

**Security reasons**

- forgotten cloud resources keep running (public bucket with customer data)
- third parties still hold your data (require return/deletion per contract clause + certificate of destruction)
- vendor support accounts keep access
- cost/audit.

**Timing**

- cancel AFTER data is migrated/archived
- check notice periods (30-90 days).

**On the exam**

- retired app bucket publicly exposed = resources not decommissioned. Ending SaaS = data returned or securely deleted WITH PROOF.

**Traps**

- cancellation does not automatically delete data at provider
- cancel after migration/archive, not before.

**Quick check:** Retiring SaaS HR app; finance wants to cancel today. Two things first?

**Answer:** Correct: 1) migrate/retrieve the data first; 2) vendor must delete data on their side (cancellation does not delete). Added: get written proof (certificate of destruction); revoke vendor access/integrations; check notice period.

</details>

<a name="t-2-6-5"></a>
**Archiving**

Keep data or code needed for legal or business reasons.

> On the exam: What it is: moving data or code to long-term storage because laws or the business require keeping it.
Key points: archives keep their classification and protections; they must be retrievable for legal or audit requests; delete them when retention ends.
Don't confuse: archive = long-term retention; backup = recovery after loss.

<details><summary>Lesson (13 Oct 2026)</summary>

**Archiving**

- Archiving = moving data (sometimes code) from a retiring app to long-term storage because you must/need to keep it.

**Why keep**

- legal/regulatory retention (SOX financial 7 yrs
- HIPAA documentation 6 yrs
- tax)
- LEGAL HOLD (lawsuit/investigation: must not delete, overrides deletion schedules)
- business needs
- code for audits/rebuilds.

**Security**

- encrypt + manage keys for full retention (lose key = lose data)
- restrict + log access
- integrity via hashes
- keep readable (standard formats like CSV, PDF/A, or keep the tools)
- test restores.
- Backup vs archive: backup = COPY for RECOVERY, short-term, overwritten. Archive = ORIGINAL MOVED for long-term RETENTION, years, removed from live system.

**On the exam**

- keep 7 yrs after retirement = archive (encrypted, access-controlled). Lawsuit pending even though retention ended = legal hold, do not delete.

**Traps**

- offline archive still needs encryption/access control/integrity. Keeping everything forever is wrong too.

**Quick check:** Billing archive kept 7 yrs; sued 2 yrs later over that period. What happens to the data?

**Answer:** Correct: legal hold, do not delete, preserve for court. Added: hold lasts until legal releases it, even past year 7; protect integrity (hashes, logged access) so it is accepted as evidence.

</details>

<a name="t-2-6-6"></a>
**Data disposition**

Decide what to retain, how long, and how to destroy the rest.

> On the exam: What it is: deciding what happens to data when an app is retired: keep, move, archive or destroy.
Driven by: retention policy, legal holds (which override deletion), regulations, and dependencies on the data.
Scenario cue: 'data is under legal hold but the retention period ended' → keep it until the hold is lifted.

<details><summary>Lesson (13 Oct 2026)</summary>

**Data disposition**

- Data disposition = the DECISION for each data type at retirement: retain/archive, migrate, or destroy. (Destruction = the method.)

**Inputs**

- data retention policy/schedule (each data type + how long)
- data classification (how carefully to destroy)
- legal (retention laws, legal holds, privacy laws)
- data OWNER decides, legal/security advise.
- Privacy: GDPR data minimization + STORAGE LIMITATION (no longer than needed); keeping just in case = violation and bigger breach impact; right to erasure.
- Cover EVERY copy: backups, test/dev, exports, logs, caches, spreadsheets; use a data inventory/data map.

**On the exam**

- deciding what to keep/how long/destroy = disposition. Who decides retention = data owner per retention policy + legal.

**Traps**

- keep everything forever is wrong. Deleting prod DB while copies remain in backups/test = incomplete.

**Quick check:** Retiring marketing app with 10 yrs of customer emails/purchases; schedule says 2 yrs; IT manager wants to archive all 10 yrs just in case. What is wrong, what instead?

**Answer:** Correct: follow the schedule per data type; destroy beyond it, including all copies. Clarified: keep only the most recent 2 yrs; the older 8 yrs destroyed NOW. Name: storage limitation/data minimization; check legal holds first.

</details>

<a name="t-2-6-7"></a>
**Data destruction (NIST SP 800-88)** (review)

Clear (overwrite), purge (degauss, crypto-erase), destroy (shred, incinerate).

> On the exam: Clear stops simple recovery tools, purge stops lab recovery, destroy makes media unusable. For SSDs, overwriting is unreliable: use crypto-erase or physical destruction.

<details><summary>Lesson (13 Oct 2026)</summary>

**Data destruction (NIST SP 800-88)**

- NIST SP 800-88 = Guidelines for Media Sanitization. Sanitization = make data on media unrecoverable.
- Delete/format only removes pointers; leftover data = DATA REMANENCE.
- Order: CLEAR -> PURGE -> DESTROY.
- CLEAR: vs simple software recovery; overwrite (zeros/random) or factory reset; media REUSED INSIDE the org, not highly sensitive.
- PURGE: vs LAB recovery; degaussing (magnetic only, usually ruins HDD), cryptographic erase, drive secure erase; media LEAVES the org or data sensitive.
- DESTROY: shred, disintegrate, pulverize, incinerate, melt; most sensitive data, damaged media, or other methods cannot be verified; never reused.
- SSD: wear leveling means overwriting is unreliable; use crypto/secure erase or destroy. Degaussing does nothing to SSD/flash.
- Proof: certificate of sanitization/destruction (what, how, who, when) + verify.

**Traps**

- degaussing an SSD
- formatting/deleting is not sanitization.

**Quick check:** Match: 1 magnetic laptop drives returned to leasing co; 2 top-secret drives retired; 3 workstation to another employee same team.

**Answer:** Purge, Destroy, Clear. All correct.

</details>

<a name="t-2-6-8"></a>
**Crypto-shredding**

Destroying the encryption keys makes encrypted data unrecoverable; useful in the cloud.

> On the exam: What it is: encrypt data, then securely destroy the keys; without keys the data is useless.
When to use: cloud or shared storage where you can't physically destroy the disks, and SSDs where overwriting is unreliable.
Trap: only works if no copies of the keys remain (backups, escrow).

<details><summary>Lesson (13 Oct 2026)</summary>

**Crypto-shredding**

- Crypto-shredding (cryptographic erase) = destroy the ENCRYPTION KEYS so the encrypted data is permanently unreadable. A PURGE method in NIST 800-88.

**Why (cloud)**

- you do not own physical disks
- data copied across replicas/backups/snapshots
- deleting one key makes every copy unreadable.

**How**

- encrypt from the start with keys you control (KMS
- HSM = tamper-resistant key hardware)
- delete EVERY key copy
- ciphertext can stay.

**Requirements**

- strong encryption (AES-256)
- every key copy destroyed incl. backups/escrow
- encrypted from the beginning (unencrypted exports/logs/caches not covered)
- separate keys per tenant/app/dataset.
- Enables fast right-to-erasure (per-customer key).

**On the exam**

- dispose of data in public cloud without physical access = crypto-shredding.

**Traps**

- fails if any key copy survives or data was ever stored unencrypted. It is purge, not clear.

**Quick check:** Keys deleted from KMS but backed up in a separate vault; company declares data destroyed. Correct?

**Answer:** Correct: not destroyed; vault key backup can still decrypt; delete those too. Also check for unencrypted copies and record proof.

</details>

<a name="t-2-6-9"></a>
**Dependencies**

Check what other systems rely on the app before shutting it down.

> On the exam: Map integrations first. Shutting down an API can break other systems or leave data flowing nowhere.

<details><summary>Lesson (13 Oct 2026)</summary>

**Dependencies**

- Before retiring, find what relies on the app and what it relies on; skipping this breaks systems or leaves security gaps.
- UPSTREAM (what depends on the app): systems calling its API, data feeds, its authentication, reports off its DB.
- DOWNSTREAM (what the app depends on): DBs, shared services, service accounts, libraries, third-party APIs; clean up or confirm still needed.
- Hidden: shared authentication; shared databases; scheduled jobs/integrations; SECURITY functions others rely on (logging, encryption, access checks); hard-coded URLs/IPs.
- Find: CMDB + architecture diagrams; network traffic analysis; logs; interview owners; scream test/brownout (approved, reversible).

**Security angle**

- broken dependencies push unsafe workarounds (hard-coded creds, rushed firewall rules, keeping old app running = orphaned).

**On the exam**

- FIRST before shutdown = identify dependencies. Another system lost access controls after retirement = unidentified security dependency.

**Trap**

- checking only the app servers misses other systems that depend on it.

**Quick check:** Retiring old customer DB app next week; newer mobile app still pulls loyalty points via its API. What first?

**Answer:** Correct: remove the dependency, move the data, check all upstream/downstream, then retire. Refined: this is UPSTREAM; migrate loyalty data + API to a supported system, repoint and test the mobile app, postpone retirement until done.

</details>

<a name="t-2-6-10"></a>
**Sun-setting criteria**

Conditions that signal software should be retired or replaced: new threats whose risk can't be reduced enough, contract ends and upkeep is too costly, end of warranty, end of product or vendor support, incompatible with new systems.

> On the exam: Scenario cue: 'vendor support ended and a new flaw can't be fixed' → meets sun-setting criteria; plan retirement.

<details><summary>Lesson (13 Oct 2026)</summary>

**Sun-setting criteria**

- Sun-setting = planned gradual retirement. Criteria = conditions that signal retire/replace; written into the EOL policy.

**Criteria**

- unacceptable security risk (cannot reduce to acceptable level)
- end of vendor/product support (EOS) or vendor gone
- end of warranty
- cost (contract ends, upkeep more than replacing)
- incompatibility (new systems, OS, security tools e.g. no MFA/modern TLS)
- compliance (cannot meet new rules)
- business need ended.

**Who decides**

- business owner, security advises.
- Core question: can we keep risk acceptable at acceptable cost? If not, sun-set.

**On the exam**

- vulns can no longer be mitigated to acceptable level = sun-set. Cannot support MFA = incompatibility.

**Traps**

- it still works is not a reason to keep it
- age alone is not a criterion.

**Quick check:** Old app on EOS OS, cannot integrate with new MFA, needs expensive specialist contractor. Three criteria?

**Answer:** Correct: end of support, incompatibility, cost. All three.

</details>

<a name="t-2-6-11"></a>
**Sun-setting process**

Steps to retire software: notify users, migrate or archive data, remove access and credentials, revoke certificates, uninstall, sanitize media, update documentation and asset records.

> On the exam: Trap: retiring software includes its data and its accounts, not just uninstalling it.

<details><summary>Lesson (13 Oct 2026)</summary>

**Sun-setting process**

- Step-by-step retirement procedure; ties all of 2.6 together.
- 1 Approval + plan (business owner). 2 Identify dependencies. 3 Notify users/stakeholders (date + replacement). 4 Decide data disposition (check legal holds). 5 Migrate/archive data (encrypted). 6 Remove access + credentials (accounts, secrets, REVOKE certs, firewall, DNS). 7 Shut down + uninstall. 8 Sanitize media (800-88 / crypto-shred). 9 Cancel licenses/contracts (vendor deletion proof). 10 Update docs/records (inventory, CMDB, diagrams, risk register; keep evidence).

**Why order**

- data before destruction
- dependencies before shutdown
- ACCESS STAYS until data is out (you need the accounts to extract it)
- records last.

**On the exam**

- FIRST = approval/planning + dependencies. LAST = update documentation/asset inventory.

**Traps**

- sanitizing/cancelling before data migrated = data loss. Ending at server turned off = incomplete.

**Quick check:** Order: A revoke certs/disable service accounts; B notify users; C update asset inventory; D archive data for legal retention; E sanitize media.

**Answer:** My answer: B A D E C. Correct: B D A E C. Swapped A and D: archive BEFORE removing access, because the service accounts/certs may be needed to extract the data. Marked shaky.

</details>

## 2.7 Security reporting

<a name="t-2-7-1"></a>
**Reports and dashboards**

Present security status to the right audience (technical vs executive).

> On the exam: What it's for: show security status to the right audience. Executives need risk, trends and business impact; engineers need specific findings and how to fix them.
Scenario cue: 'the board doesn't understand the technical report' → summarize in business risk terms on a dashboard.

<details><summary>Lesson (15 Oct 2026)</summary>

**Reports and dashboards**

- Show security status to the people who need it, in the form that fits each audience.
- Report = point-in-time document with explanation/recommendations. Dashboard = live/refreshed screen of key numbers.
- EXECUTIVES/BOARD (decide, fund): business risk in plain language (financial, legal, reputational), trends, progress vs OKRs/KRIs, top risks + decisions needed; short; no CVE lists.
- MANAGERS/PRODUCT OWNERS (plan): open vulns by severity/app, SLA compliance, expiring risk acceptances, backlog progress.
- DEVELOPERS/ENGINEERS (fix): detailed findings (file, line, CWE, repro, fix) inside their tools.
- AUDITORS/COMPLIANCE (verify): evidence, control status, test results, signed approvals, traceability (RTM).
- Good reporting: accurate, consistent, actionable, timely, PROTECTED (reports list weaknesses = attacker shopping list).

**On the exam**

- report to the board = summarized business risk + trends
- developers = detailed technical in workflow.

**Traps**

- one report for everyone is wrong
- vuln reports are sensitive.

**Hook**

- board = big picture in dollars
- managers = what is late
- developers = which line to fix
- auditors = proof.

**Quick check:** Same 80-page scanner output to devs and board: what is wrong, what should the board get?

**Answer:** Correct: tailor to the audience; devs get what to fix; board gets non-technical summarized risk vs tolerance.

</details>

<a name="t-2-7-2"></a>
**Feedback loops**

Feed findings from testing and incidents back into requirements and design.

> On the exam: What it's for: lessons from testing, incidents and operations go back into requirements, standards and training, so the same mistakes stop.
Scenario cue: 'pentests find the same flaw every release' → missing feedback loop; add a coding standard, training and an automated test.

<details><summary>Lesson (15 Oct 2026)</summary>

**Feedback loops**

- Send what you LEARN from testing, incidents, operations BACK to requirements, design, coding so the same mistakes stop.

**Sources**

- testing (SAST, DAST, pen test, code review)
- incidents + root cause analysis
- bug bounty/customer reports
- operations/monitoring
- audits.

**Destinations**

- REQUIREMENTS (new security reqs)
- DESIGN (update threat model, patterns)
- CODING (rules, banned functions, new SAST rules)
- TRAINING (actual mistakes)
- bug bar/quality gates
- METRICS (is the class going down?).

**Example**

- pen test finds IDOR in 3 apps -> root cause no standard authz pattern -> requirement + reusable access-check library + review checklist + SAST rule + training -> IDOR near zero.
- Links: PDCA Act; SSDF RV root causes; NIST 800-61 post-incident lessons learned.

**On the exam**

- same vuln type keeps appearing = root cause analysis + feed lessons back to requirements, design, training, tools.

**Trap**

- fixing each bug is not best when it repeats
- fix the PROCESS.

**Hook**

- do not just mop the floor
- fix the leak.

**Quick check:** XSS found 3 releases in a row; devs fix each fast. What to do; which phases?

**Answer:** Correct core: root cause analysis. Missing phases: requirements (output encoding), design (auto-escaping framework, threat model), coding (standard, review checklist, SAST rule), training, measure.

</details>

<a name="t-2-7-3"></a>
**Risk register**

Central list of risks, owners, ratings and responses.

> On the exam: What it is: the central list of risks with owner, likelihood, impact, chosen response and status.
Scenario cue: 'how do you make sure every identified risk has a decision and an owner?' → risk register.
Also: it shows auditors that risks were formally accepted, not ignored.

<details><summary>Lesson (15 Oct 2026)</summary>

**Risk register**

- Risk register = CENTRAL list of all known risks with owner, rating, response, status; the risk to-do list management reviews.

**Fields**

- ID + description
- asset
- threat + vulnerability
- likelihood + impact
- inherent rating
- existing controls
- residual rating
- response (mitigate/accept/transfer/avoid)
- RISK OWNER (named, usually business owner)
- action plan + due date
- status + REVIEW DATE.

**Why**

- single source of truth
- accountability
- prioritization
- tracks accepted risks and expiry
- audit evidence.
- LIVING document; updated from testing, threat models, incidents; reviewed regularly.

**Related**

- POA&M = federal weaknesses-to-fix list for one system. Vulnerability list = raw technical findings
- register = business-level risks with owners/decisions.

**On the exam**

- central doc of risks/owners/ratings/responses = risk register
- owner = business owner
- revisit accepted risks = review dates.

**Traps**

- not one-time
- security maintains/facilitates, business owns.

**Hook**

- the risk to-do list with a name next to every line.

**Quick check:** Risk list with no owners or review dates; accepted risks 3 years old. Missing fields and why?

**Answer:** Review date (revisit, esp. accepted) + owner (accountable, who approved). Correct.

</details>

## 2.8 Integrated risk management

<a name="t-2-8-1"></a>
**ISO/IEC 27001 / 27002**

ISMS requirements / security control guidance.

> On the exam: 27001 is certifiable (requirements for an ISMS); 27002 is control guidance and is not certifiable.

<details><summary>Lesson (14 Oct 2026)</summary>

**ISO/IEC 27001 / 27002**

- ISMS = Information Security Management System: the whole system for managing security (policies, risk process, roles, controls, reviews). Not software.
- 27001 = REQUIREMENTS: what an ISMS must include (leadership, risk assessment, risk treatment plan, internal audits, management review, continual improvement). CERTIFIABLE by accredited auditor. Uses PDCA. Annex A = 93 controls (2022) in 4 themes: organizational, people, physical, technological. Output: STATEMENT OF APPLICABILITY (SoA) = which Annex A controls used/excluded and why.
- 27002 = GUIDANCE explaining each control; NOT certifiable.
- vs 27034: 27001/27002 = whole org; 27034 = application security.

**On the exam**

- certifiable ISMS standard = 27001. Control implementation guidance = 27002. Lists applicable controls + justifies exclusions = SoA.

**Traps**

- no 27002 certification. 27001 is a management system (process), not just tech controls.

**Hook**

- 27001 = 1 certificate
- 27002 = 2 explain.

**Quick check:** Customer wants a certificate from an accredited auditor; which standard, and which document shows chosen controls?

**Answer:** 27001 + Statement of Applicability. Correct (briefly said 27002 first: 27002 is the guidance book, the SoA is your own document).

</details>

<a name="t-2-8-2"></a>
**ISO/IEC 27005**

Information security risk management.

> On the exam: What it is: ISO's guidance on information security risk management (context, assessment, treatment, acceptance, communication, monitoring).
Scenario cue: 'which ISO standard guides the risk process for an ISO 27001 program?' → 27005.
Don't confuse: 27001 = ISMS requirements; 27002 = controls; 27005 = risk; 27034 = application security; 27036 = suppliers.

<details><summary>Lesson (14 Oct 2026)</summary>

**ISO/IEC 27005**

- 27005 = information security RISK MANAGEMENT guidance; the how-to for the risk part of 27001.

**Process**

- context establishment (scope, criteria, appetite) -> risk assessment (identification, analysis, evaluation/prioritize) -> risk treatment (modify/mitigate, retain/accept, avoid, share/transfer) -> risk acceptance (management signs residual) -> communication & consultation -> monitoring & review.

**Approaches**

- asset-based (start from what you own) or event-based (start from scenarios).
- Guidance only: NOT certifiable; no forced method (qualitative or quantitative).

**On the exam**

- ISO guidance on infosec risk management = 27005
- 27001 requires risk assessment, 27005 explains how.

**Traps**

- 27005 not certifiable. ISO 31000 = general risk management (any risk). NIST SP 800-30 = US equivalent for risk assessment.

**Hook**

- 1 certifies, 2 explains the controls, 5 handles the risk.

**Quick check:** Preparing for 27001; which standard explains the risk assessment method; certifiable?

**Answer:** 27005; not certifiable, only 27001 is. Correct (first voice transcription garbled it).

</details>

<a name="t-2-8-3"></a>
**ISO/IEC 15408 (Common Criteria)** (review)

Product security evaluation; EAL1-7 assurance levels, protection profiles.

> On the exam: Key terms: Target of Evaluation (TOE), Security Target (ST), Protection Profile (PP). EAL measures how thoroughly it was evaluated, not how secure it is.

<details><summary>Lesson (14 Oct 2026)</summary>

**ISO/IEC 15408 (Common Criteria)**

- Common Criteria (CC) = international standard to evaluate/certify ONE PRODUCT's security (firewall, OS, smart card) via independent labs; governments recognize results.
- vs 27001: 27001 certifies an ORGANIZATION's management system; CC certifies a PRODUCT.
- TOE = Target of Evaluation: the exact product/version/config evaluated.
- PROTECTION PROFILE (PP) = reusable requirements for a TYPE of product, written by CUSTOMERS/government; implementation-independent (what is needed). Analogy: tenant's wish list for any apartment.
- SECURITY TARGET (ST) = VENDOR's document for its specific product's security claims, often claiming PP conformance; lab evaluates AGAINST the ST. Analogy: landlord's listing.
- EAL 1-7 = depth of evaluation (ASSURANCE): 1 functionally tested; 2 structurally tested; 3 methodically tested and checked; 4 methodically designed, tested and reviewed (most common commercial); 5 semi-formally designed and tested; 6 semi-formally verified design and tested; 7 formally verified design and tested.
- TRAP: EAL = confidence that the product does what it claims, NOT more features/more secure.
- CCRA = mutual recognition between member countries.

**On the exam**

- specific IT product evaluation = CC/15408
- customer requirements for product category = PP
- vendor claims = ST
- product evaluated = TOE.

**Hook**

- PP = Purchaser's wish list
- ST = Seller's claims
- EAL = how hard the lab checked.

**Quick check:** Agency lists requirements for all smart card readers; vendor documents how its reader meets them. Name each; what does EAL4 tell?

**Answer:** I named 15408 (the whole standard) and EAL4 description right but not what it tells. Answer: agency doc = PP, vendor doc = ST; EAL4 = level of CONFIDENCE claims are true, not more features. Re-taught with apartment analogy; re-check hospital infusion pump requirements = PP, correct. Marked shaky.

</details>

<a name="t-2-8-4"></a>
**PCI DSS and PCI Secure Software Standard** (review)

Requirements for systems and software handling payment card data.

> On the exam: Applies to anyone storing, processing or transmitting card data. Never store the CVV after authorization. PCI DSS is a contract standard, not a law.

<details><summary>Lesson (14 Oct 2026)</summary>

**PCI DSS and PCI Secure Software Standard**

- PCI SSC (Visa, Mastercard, Amex, Discover, JCB) writes card-data rules: industry CONTRACT, not law (fines, lose card processing).
- CHD = cardholder data: PAN (card number), name, expiry, service code. PAN CAN be stored if protected.
- SAD = sensitive authentication data: full stripe, CVV2, PIN: NEVER stored after authorization, even encrypted.
- CDE = every system storing/processing/transmitting card data + connected systems.
- PCI DSS (v4.0/4.0.1): any org handling card data (merchants, service providers); 12 requirements; Req 6 = secure systems & software (dev training, review custom code, protect public web apps with WAF or assessment, patch critical fast).
- PCI Secure Software Standard (Software Security Framework): VENDORS selling payment software; evaluates the product; replaced PA-DSS.

**Scope reduction**

- TOKENIZATION (processor vaults PAN, you store a useless token
- charge returning customers with token
- systems with only tokens out of scope)
- segmentation (isolate CDE
- still stores PAN)
- outsourcing.

**On the exam**

- retailer accepting cards = PCI DSS
- vendor product = PCI Secure Software Standard
- CVV after auth = never
- reduce scope = tokenization/segmentation.

**Hook**

- token = coat-check ticket. DSS = the store
- Secure Software = the vendor.

**Quick check:** Online shop wants to STOP storing card numbers but charge returning customers. Technique and why?

**Answer:** My answer: tokenization or segmentation, mixed in the CVV rule. Answer: TOKENIZATION; processor vaults PAN, shop keeps token, database out of scope. Segmentation still stores PAN. Never-store-after-auth rule is for CVV2/SAD, not PAN. Marked shaky.

</details>

<a name="t-2-8-5"></a>
**NIST SP 800-53**

Catalog of security and privacy controls.

> On the exam: What it is: NIST's large catalog of security and privacy controls in families (AC = access control, AU = audit, CM = configuration management, SA = system acquisition, SR = supply chain).
Scenario cue: 'which document provides the controls to select during the RMF Select step?' → SP 800-53.
Don't confuse: 800-37 = the RMF process; 800-53 = the controls; 800-30 = how to assess risk.

<details><summary>Lesson (14 Oct 2026)</summary>

**NIST SP 800-53**

- 800-53 (Rev 5) = CATALOG of security and privacy controls; the menu the US federal government picks from. Control = any safeguard (technical, process, physical).
- 20 families with 2-letter codes: AC access control, AU audit, CM configuration mgmt, IA identification & authentication, IR incident response, RA risk assessment, SA system & services acquisition (secure development), SC system & comms protection, SI system & info integrity, SR supply chain (new Rev 5), PT PII processing (new Rev 5). e.g. AC-2 account mgmt, IA-2 MFA.
- 800-53B = Low/Moderate/High control BASELINES; tailor with justification.
- Used by: federal agencies (FISMA); cloud providers for government (FedRAMP); voluntary elsewhere.

**Fit**

- 800-53 = WHAT controls
- 800-37 RMF = PROCESS
- FIPS 199 = rate system L/M/H
- 800-30 = risk assessment.

**Chain**

- FIPS 199 rating -> 800-53B baseline -> tailor -> RMF.

**Don't confuse**

- ISO 27001 Annex A (93 controls, international, certifiable) vs 800-53 (1,000+ with enhancements, US federal, no certificate).

**Hook**

- 800-53 = the control menu.

**Quick check:** Cloud provider selling to federal agencies: which publication has the controls, how decide which set?

**Answer:** My answer: 800-53 control book; 800-37 decides. Mostly right. Complete: FIPS 199 rates L/M/H -> 800-53B baseline -> tailor, via FedRAMP; RMF process 800-37.

</details>

<a name="t-2-8-6"></a>
**NIST SP 800-37 (RMF)** (review)

Categorize, select, implement, assess, authorize, monitor.

> On the exam: Used for US federal systems. An Authorizing Official grants authority to operate; continuous monitoring follows.

<details><summary>Lesson (14 Oct 2026)</summary>

**NIST SP 800-37 (RMF)**

- RMF = federal step-by-step process for managing system security risk. 800-53 = menu; RMF = how you order/cook/inspect/keep eating safely.
- 7 steps (Rev 2): PREPARE (roles, strategy, assets) -> CATEGORIZE (L/M/H via FIPS 199) -> SELECT (800-53 baseline, tailor) -> IMPLEMENT (put in place, document) -> ASSESS (independent assessor tests controls) -> AUTHORIZE (senior official accepts residual risk) -> MONITOR (continuous monitoring).

**Mnemonic**

- People Can Sometimes Inspect And Approve Mistakes.
- AO = Authorizing Official: senior official who accepts residual risk.
- ATO = Authorization to Operate: formal approval to go live.
- POA&M = Plan of Action and Milestones: known weaknesses, who fixes, by when.

**On the exam**

- who accepts residual risk = AO
- formal approval = ATO
- tracks weaknesses = POA&M
- after Implement = Assess.

**Traps**

- Assess before Authorize. Assessor tests
- AO decides.

**Hook**

- Step = Authorize. Person = AO. Permission slip = ATO. To-do list = POA&M.

**Quick check:** Independent team tests controls; senior official allows go-live if 2 weaknesses fixed in 90 days. Name team step, official step, approval, tracking doc.

**Answer:** My answer: Assess correct; called official step the ATO; approval = plan of action authorization; POA&M correct. Answer: Assess / Authorize / ATO / POA&M. Marked shaky.

</details>

<a name="t-2-8-7"></a>
**NIST SP 800-30** (review)

Guide for conducting risk assessments.

> On the exam: What it is: NIST's guide to doing a risk assessment: identify threat sources and events, vulnerabilities, likelihood, impact, then determine risk.
Scenario cue: 'which NIST publication explains how to conduct a risk assessment?' → 800-30.

<details><summary>Lesson (14 Oct 2026)</summary>

**NIST SP 800-30**

- 800-30 = NIST guide for conducting RISK ASSESSMENTS; US counterpart to ISO 27005.

**Process**

- Prepare (purpose, scope, assumptions, risk model) -> Conduct -> Communicate -> Maintain.
- Conduct: threat sources, threat events, vulnerabilities + predisposing conditions, LIKELIHOOD, IMPACT, risk = likelihood x impact.
- Tiers: 1 organization, 2 mission/business process, 3 information system.
- Used inside RMF (Prepare, Categorize, Select, Monitor) whenever risk must be measured.

**Trio**

- 800-30 = MEASURE risk
- 800-53 = control MENU
- 800-37 = full PROCESS (RMF).
- Read what the question asks: how likely/how bad = 30; which controls = 53; categorize/authorize/ATO/monitor = 37.

**Trap**

- 800-30 assesses risk
- does not choose controls or authorize systems.
- RISK = LIKELIHOOD x IMPACT.

**Quick check:** How likely is ransomware on benefits system and how badly would it hurt: which NIST pub, which two factors?

**Answer:** My answer: 800-37; factors determine risk + identify threat (wrong). Answer: 800-30; likelihood x impact. Re-check (choose controls=53, estimate likelihood/impact=30, AO grants ATO=37) all correct. Marked shaky.

</details>

<a name="t-2-8-8"></a>
**NIST Cybersecurity Framework**

Govern, identify, protect, detect, respond, recover.

> On the exam: What it is: voluntary, high-level framework for managing cybersecurity risk. Functions: Govern, Identify, Protect, Detect, Respond, Recover. Uses profiles (current vs target) and tiers.
Scenario cue: 'an organization wants a common, non-technical way to describe and improve its cybersecurity posture' → NIST CSF.
Don't confuse: CSF = what outcomes; 800-53 = detailed controls.

<details><summary>Lesson (14 Oct 2026)</summary>

**NIST Cybersecurity Framework**

- CSF 2.0 (2024) = VOLUNTARY high-level framework for any organization; describes OUTCOMES, not exact controls; maps to 800-53, ISO 27001.
- 6 Functions: GOVERN (new in 2.0, center: strategy, roles, policy, risk appetite, oversight), IDENTIFY (assets, risks, supply chain), PROTECT (access control, training, data security), DETECT (monitoring, anomalies), RESPOND (contain, communicate), RECOVER (restore, learn). G-I-P-D-R-R.
- Parts: Core (Functions -> Categories -> Subcategories); Profiles (Current vs Target = gap analysis); Implementation Tiers 1 Partial, 2 Risk Informed, 3 Repeatable, 4 Adaptive.

**On the exam**

- added in 2.0 = Govern
- current vs target = profiles/gap
- restoring = Recover
- containing = Respond.

**Traps**

- tiers are not required maturity levels (pick what fits risk)
- CSF is voluntary outcomes, not a control catalog.

**Hook**

- CSF = the map
- 800-53 = the toolbox.

**Quick check:** Ransomware: isolate servers / restore from clean backups / board updates risk appetite + oversight: functions?

**Answer:** Respond, (restore) = RECOVER, Govern. Correct; use exact function name Recover.

</details>

<a name="t-2-8-9"></a>
**OWASP**

Open community: Top 10, ASVS, SAMM, testing guides, cheat sheets.

> On the exam: What it is: the Open Worldwide Application Security Project, a free community. Key projects: Top 10 (awareness), ASVS (verification requirements), SAMM (maturity), WSTG (testing guide), Cheat Sheets, Dependency-Check (SCA), ZAP (DAST tool), Top 10 for LLMs, API Top 10, MASVS (mobile).
Scenario cue: match the need to the project: requirements → ASVS, maturity → SAMM, testing → WSTG.

<details><summary>Lesson (14 Oct 2026)</summary>

**OWASP**

- OWASP = Open Worldwide Application Security Project: non-profit open community; FREE resources; not a company/law/certifier.
- Top 10 = 10 most critical web app risks (AWARENESS); 2021 current, 2025 update released; #1 Broken Access Control, Cryptographic Failures, Injection.
- ASVS = Application Security Verification Standard: testable requirements, 3 levels: L1 basic/low-risk (largely outside testing); L2 most apps with sensitive data (recommended); L3 critical (banking, healthcare, military).
- Testing Guide (WSTG) = how to test web apps. Cheat Sheet Series = short developer how-tos. SAMM = maturity model.
- Others: Top 10 for LLM Applications, Mobile Top 10, API Security Top 10, ZAP (free DAST), Dependency-Check.

**On the exam**

- awareness list = Top 10
- leveled verification requirements = ASVS
- how to test = Testing Guide
- dev guides = Cheat Sheets.

**Trap**

- Top 10 is not a compliance standard/full checklist.

**Hook**

- Top 10 = warning sign
- ASVS = inspection checklist.

**Quick check:** Bank wants detailed testable requirements to verify online banking app: which resource, which level?

**Answer:** ASVS, Level 3. Correct.

</details>

<a name="t-2-8-10"></a>
**SAFECode**

Industry group publishing secure development practices.

> On the exam: What it is: Software Assurance Forum for Excellence in Code, an industry nonprofit publishing practical secure development practices, e.g., 'Fundamental Practices for Secure Software Development'.
Scenario cue: 'industry-proven secure development practices from major software vendors' → SAFECode.

<details><summary>Lesson (14 Oct 2026)</summary>

**SAFECode**

- SAFECode = Software Assurance Forum for Excellence in Code: non-profit INDUSTRY group of major software VENDORS (Microsoft, Adobe, SAP, Symantec) sharing secure development practices that work internally.
- vs OWASP: OWASP = open community, anyone contributes, web app risks/tools. SAFECode = big vendors pooling real-world experience, whole-lifecycle practices.
- Publishes: Fundamental Practices for Secure Software Development; third-party component risk guidance; tactical threat modeling; security champions; free training.
- Wound down operations in 2025; still referenced and in the outline.

**On the exam**

- industry consortium of vendors sharing proven practices = SAFECode.

**Trap**

- neither OWASP nor SAFECode certifies anything
- the difference is WHO is behind it.

**Hook**

- SAFECode = big vendors' shared playbook
- OWASP = open community toolbox.

**Quick check:** Paper from major software companies on internal practices: OWASP or SAFECode? One difference?

**Answer:** SAFECode correct. Difference given (does not certify) applies to both; real difference = vendors consortium vs open community.

</details>

<a name="t-2-8-11"></a>
**OWASP SAMM**

Prescriptive maturity model: governance, design, implementation, verification, operations.

> On the exam: What it is: OWASP Software Assurance Maturity Model. Five business functions: Governance, Design, Implementation, Verification, Operations, each with practices scored at maturity levels 1-3.
Scenario cue: 'measure our current maturity and build a roadmap to improve' → SAMM.
Don't confuse: SAMM is prescriptive (what you should do); BSIMM is descriptive (what others do).

<details><summary>Lesson (14 Oct 2026)</summary>

**OWASP SAMM**

- SAMM = Software Assurance Maturity Model (OWASP, free): measure software security program maturity and plan improvement.
- Maturity model = scale from ad hoc to optimized (belt colors).
- v2: 5 Business Functions: GOVERNANCE (strategy, policy, compliance, education), DESIGN (threat assessment, security requirements, architecture), IMPLEMENTATION (secure build, secure deployment, defect mgmt), VERIFICATION (architecture assessment, requirements testing, security testing), OPERATIONS (incident, environment, operational mgmt). 3 practices each = 15. Levels 1-3 (0 = not done).

**Mnemonic**

- Good Developers Implement Verified Operations.

**Use**

- assess current -> set target -> roadmap -> repeat (gap analysis for software security).
- PRESCRIPTIVE = tells you WHAT TO DO. Free, open, flexible (any org, any methodology), technology-agnostic.

**On the exam**

- open prescriptive maturity model / build a roadmap = SAMM.

**Traps**

- not a certification
- not a vulnerability list. SAMM prescriptive vs BSIMM descriptive.

**Hook**

- SAMM = Self-improvement plan
- prescription.

**Quick check:** Score current practices, set targets, phased plan from step-by-step guidance: which model, why prescriptive?

**Answer:** SAMM (self-improvement plan); prescriptive because it tells you what to do. Correct; name the model explicitly on exam.

</details>

<a name="t-2-8-12"></a>
**BSIMM**

Descriptive model: measures what real organizations actually do. SAMM tells you what to do; BSIMM shows what others do.

> On the exam: Use it to benchmark against peers. Trap: BSIMM describes; it doesn't prescribe what you should do.

<details><summary>Lesson (14 Oct 2026)</summary>

**BSIMM**

- BSIMM = Building Security In Maturity Model: built by STUDYING real organizations (100+) and recording which software security activities they actually perform. Published by Black Duck (ex-Synopsys; created by Cigital).
- DESCRIPTIVE = describes what others do; does not tell you what to do.

**Analogy**

- SAMM = personal trainer with a plan
- BSIMM = survey of what other gym members do.

**Structure**

- 4 domains: Governance, Intelligence, SSDL Touchpoints, Deployment
- 12 practices (3 each)
- 100+ activities with how common each is.
- SSDL = secure software development lifecycle.

**Use**

- BENCHMARKING vs industry or sector
- scorecard.

**On the exam**

- descriptive, real-world observation / benchmark against peers = BSIMM
- prescriptive guidance = SAMM.

**Trap**

- BSIMM says how COMMON an activity is, not that it is required or best.

**Hook**

- SAMM = Should (prescriptive)
- BSIMM = Benchmark (descriptive).

**Quick check:** Bank CISO: how do we compare to other financial institutions? Model + prescriptive/descriptive?

**Answer:** BSIMM, descriptive, benchmark. Correct.

</details>

<a name="t-2-8-13"></a>
**Intellectual property**

Copyright (expression), patent (invention), trademark (brand), trade secret (kept confidential).

> On the exam: Code is protected by copyright automatically; a novel algorithm may be patented; secret source code is a trade secret protected by NDAs.

<details><summary>Lesson (14 Oct 2026)</summary>

**Intellectual property**

- IP = legal protection for creations of the mind; decides who owns what and what others can copy.
- COPYRIGHT = the EXPRESSION (written code, docs, UI art); not the idea; automatic; long (US life+70 / 95 for company works).
- PATENT = the INVENTION (new, useful, non-obvious algorithm/process); must apply; PUBLIC DISCLOSURE; ~20 years; protects the idea itself.
- TRADEMARK = the BRAND (names, logos, slogans); forever if used/renewed; TM claimed, (R) registered.
- TRADE SECRET = kept CONFIDENTIAL (recipes, algorithms, customer lists); NDAs, access control, need-to-know; no registration/time limit; lost if leaked or legitimately reverse-engineered.
- NDA = non-disclosure agreement.

**Security links**

- trade secrets need reasonable security measures
- obfuscation/anti-reverse-engineering
- IP assignment agreements for developers
- piracy = copyright violation.

**Trap**

- patent requires disclosure
- to keep it secret use trade secret.

**Hook**

- copyright = words
- patent = invention
- trademark = brand
- trade secret = vault.

**Quick check:** Unique fraud algorithm, never want competitors to learn it: patent or trade secret?

**Answer:** Trade secret; patent requires public disclosure. Correct.

</details>

<a name="t-2-8-14"></a>
**Software licensing**

Proprietary vs open source; permissive (MIT, Apache) vs copyleft (GPL) obligations.

> On the exam: Copyleft licenses can require releasing your own source if you distribute derived software. SCA tools flag this legal risk.

<details><summary>Lesson (14 Oct 2026)</summary>

**Software licensing**

- License = legal permission for how to use, copy, change, share software.
- PROPRIETARY: vendor owns code, no source; right to use with conditions; EULA.
- OPEN SOURCE: public source but MUST follow terms.
- PERMISSIVE (MIT, Apache 2.0, BSD): use in closed commercial products; keep copyright notice/license text; Apache 2.0 adds patent grant.
- COPYLEFT (GPL, AGPL): if you DISTRIBUTE, whole combined program must be released under GPL incl. your source (viral). AGPL: network/SaaS use counts. LGPL: weaker, can link without opening whole program.

**Why care**

- legal risk (forced source release/lawsuit)
- SBOM lists components + licenses
- SCA (Software Composition Analysis) finds components, vulns, licenses
- approved license list.

**On the exam**

- commercial closed-source with attribution = permissive
- derivatives same license = copyleft
- SaaS must share = AGPL
- tool for components/licenses = SCA.

**Traps**

- open source is not no obligations
- GPL triggered by DISTRIBUTION (internal use usually fine
- AGPL exception).

**Hook**

- permissive = just give credit
- copyleft = share alike.

**Quick check:** Closed-source app sold to customers; MIT lib and GPL lib: which is a problem?

**Answer:** GPL: distribution would force releasing the whole app source. MIT fine with notice. Correct.

</details>

<a name="t-2-8-15"></a>
**Breach notification**

Laws requiring timely notice of breaches, e.g., GDPR's 72 hours to the regulator.

> On the exam: What it is: laws requiring you to notify regulators and affected people after a breach. GDPR: regulator within 72 hours of becoming aware. US: state laws plus sector rules (e.g., HIPAA).
Why it matters for software: you need logging and data inventory good enough to know what data was affected and when.
Scenario cue: 'the company can't tell which records were stolen' → logging and data classification gaps.

<details><summary>Lesson (14 Oct 2026)</summary>

**Breach notification**

- Laws requiring notice to regulators/people when personal data is breached, within deadlines.
- Breach = personal data accessed, disclosed, changed, destroyed without authorization (attack, mistake, lost laptop).
- GDPR: CONTROLLER notifies SUPERVISORY AUTHORITY within 72 HOURS of AWARENESS (unless unlikely to result in risk); individuals without undue delay if HIGH risk. Processor tells controller without undue delay.
- HIPAA: individuals within 60 days of discovery; HHS: 500+ within 60 days, &lt;500 annual report; media if 500+ in one state.
- US states: all 50 have laws; varied deadlines.
- SEC: material incident within 4 business days of materiality determination (8-K).
- ENCRYPTION SAFE HARBOR: properly encrypted + key not compromised = usually no notification.

**Notice contents**

- what happened, data involved, actions, what people should do, contacts.
- Developers: logging/monitoring to detect and scope; encryption at rest; IR plan includes notification steps.

**Traps**

- 72 hours is for the regulator
- clock starts at AWARENESS.

**Hook**

- GDPR 72h regulator
- HIPAA 60 days people
- SEC 4 business days
- encrypted + key safe = usually no notice.

**Quick check:** EU e-commerce discovers Monday 9 AM theft of unencrypted names/addresses: who, deadline?

**Answer:** Controller notifies regulator (supervisory authority) within 72h. Correct. Added: deadline Thursday 9 AM; customers without undue delay if high risk (likely).

</details>

<a name="t-2-8-16"></a>
**Risk assessment vs analysis**

Assessment identifies risks; analysis rates their likelihood and impact.

> On the exam: Process order: identify risks → analyze them (likelihood and impact) → evaluate (compare to risk appetite, prioritize) → treat (mitigate, accept, transfer, avoid) → monitor.
Scenario cue: 'which step compares risk levels to the organization's tolerance?' → evaluation.
The whole process together is risk assessment.

<details><summary>Lesson (14 Oct 2026)</summary>

**Risk assessment vs analysis**

- Risk ASSESSMENT = whole process: IDENTIFICATION (find assets, threats, vulns) -> ANALYSIS (rate likelihood + impact) -> EVALUATION (compare to acceptance criteria, prioritize).
- Risk ANALYSIS = just the rating step; qualitative or quantitative.
- Risk TREATMENT/response = act: mitigate, accept, transfer, avoid.
- Risk MANAGEMENT = whole lifecycle (assessment + treatment + monitoring + communication).
- Nesting: management > assessment > analysis.

**Analogy**

- symptoms (identify), tests (analyze), decide what to treat first (evaluate), medicine (treat), ongoing care (manage).

**On the exam**

- identifying assets/threats/vulns = identification
- likelihood + impact = analysis
- compare to criteria = evaluation
- mitigate/transfer/accept/avoid = treatment.

**Trap**

- assessment does not fix anything.

**Hook**

- Assess = find + rate + rank. Analyze = just rate. Treat = act.

**Quick check:** List apps + threats / rate 1-5 / buy cyber insurance: label each.

**Answer:** Identification, analysis, treatment. Correct.

</details>

<a name="t-2-8-17"></a>
**Qualitative vs quantitative risk**

High/medium/low judgments vs dollar values.

> On the exam: Qualitative is faster and more common; quantitative supports cost-benefit decisions about controls.

<details><summary>Lesson (14 Oct 2026)</summary>

**Qualitative vs quantitative risk**

- Two ways to do risk ANALYSIS.
- QUALITATIVE: words/scales (High/Med/Low, 1-5) by expert judgment; risk matrix/heat map; interviews, workshops, surveys, DELPHI technique (anonymous expert rounds to consensus, avoids groupthink). Fast, cheap, no hard data needed, easy; but subjective, hard to compare to control cost.
- QUANTITATIVE: dollar values + numeric probabilities; e.g. expected $120k/year (SLE, ARO, ALE); objective-looking, enables COST-BENEFIT; slow, expensive, needs reliable data, intangibles hard to price, false precision.
- Semi-quantitative/hybrid: ratings mapped to numeric ranges.

**When**

- qualitative = quick prioritization, little data, intangibles
- quantitative = budget justification, control cost comparison.

**On the exam**

- H/M/L expert judgment = qualitative
- dollar values/annual loss = quantitative
- anonymous rounds = Delphi
- justify to CFO = quantitative.

**Trap**

- quantitative is not automatically better.

**Hook**

- Qualitative = Quality words
- Quantitative = Quantity ($).

**Quick check:** CFO wants annual loss in dollars to decide on $80k firewall: which approach?

**Answer:** Quantitative. Correct; key reason = cost-benefit comparison of control cost vs expected annual loss.

</details>

<a name="t-2-8-18"></a>
**SLE, ARO, ALE** (review)

SLE = asset value x exposure factor. ALE = SLE x ARO (annual rate of occurrence).

> On the exam: Example: asset $100k, EF 40% → SLE $40k; ARO 0.5 → ALE $20k. A control is worth it if its yearly cost is less than the ALE it removes.

<details><summary>Lesson (14 Oct 2026)</summary>

**SLE, ARO, ALE**

- AV = Asset Value ($). EF = Exposure Factor = % of value lost in ONE incident (decimal). ARO = Annualized Rate of Occurrence = times per year (twice/yr = 2; once every 4 yrs = 0.25).
- SLE (Single Loss Expectancy) = AV x EF = cost of ONE incident.
- ALE (Annualized Loss Expectancy) = SLE x ARO = expected loss PER YEAR.

**Example**

- $500k x 0.4 = $200k SLE
- x 0.25 = $50k ALE.
- ALE is compared to control costs (control costing more per year than ALE prevented usually not worth it).

**Traps**

- SLE vs ALE
- ARO fraction (once in 10 yrs = 0.1)
- EF as decimal (25% = 0.25)
- full AV as SLE only if EF 100%.

**Mental math**

- 50% halve
- 25% divide by 4
- 10% move decimal
- 20% = 10% doubled.

**Hook**

- AV x EF = SLE
- SLE x ARO = ALE.

**Quick check:** Server $80k, 25% loss, 3x/yr: SLE, ALE?

**Answer:** Formulas right; numbers 40k/120k wrong (used 50%). Correct: SLE $20k, ALE $60k. Re-check laptops $200k, 10%, once in 2 yrs: $20k / $10k correct. Marked shaky.

</details>

<a name="t-2-8-19"></a>
**Risk responses** (review)

Mitigate, accept, transfer (insurance, contract), avoid.

> On the exam: Transfer moves financial impact, not accountability. Avoid means stopping the risky activity. Acceptance must be documented by the risk owner.

<details><summary>Lesson (14 Oct 2026)</summary>

**Risk responses**

- MITIGATE (reduce) [ISO: modify]: add controls to lower likelihood/impact (patch, MFA, validation, encryption, WAF); most common.
- TRANSFER (share): shift FINANCIAL impact (cyber insurance, outsourcing with liability, indemnity clauses). Cannot transfer ACCOUNTABILITY.
- ACCEPT (retain): consciously live with it; within appetite or fix costs more than loss; FORMAL: documented, named owner, business owner signs, review/expiry date. Ignoring is not acceptance.
- AVOID: STOP the activity (do not launch, stop collecting data, retire system); removes risk, loses benefit.
- Rejection/denial = pretending it does not exist; always wrong.
- Business owner decides, security advises.

**Test**

- is the activity still happening? Yes with controls = mitigate
- stopped = avoid.

**On the exam**

- insurance = transfer
- encryption/MFA = mitigate
- do not launch = avoid
- owner signs, no action = accept
- ignores = rejection.

**Traps**

- accountability stays after transfer
- residual risk always remains.

**Hook**

- M-A-T-A. Mitigate = add a lock
- avoid = do not own the thing.

**Quick check:** Stop storing SSNs / processor takes liability / owner signs to leave low-risk bug: responses?

**Answer:** My answer: mitigate, transfer, accept. #1 should be AVOID (activity stopped). 2/3. Marked shaky.

</details>

<a name="t-2-8-20"></a>
**Inherent vs residual risk**

Before controls vs what remains after controls.

> On the exam: Inherent risk: before any controls. Residual risk: what remains after controls. Total risk minus control effect = residual.
Scenario cue: 'after controls are applied, what does senior management formally accept?' → residual risk.
Trap: residual risk is never zero.

<details><summary>Lesson (14 Oct 2026)</summary>

**Inherent vs residual risk**

- INHERENT risk = before any controls (raw).
- RESIDUAL risk = what remains AFTER controls; never zero.
- Inherent - effect of controls = residual. Older: total risk = threats x vulnerabilities x asset value; residual = total - countermeasures; difference = controls gap.
- Residual compared to risk appetite: within = business owner formally ACCEPTS (risk acceptance; AO ATO); too high = more controls or transfer/avoid.
- Inherent risk helps prioritize (payment, login get most controls).

**On the exam**

- before controls = inherent
- after = residual
- management accepts = residual
- controls never eliminate risk completely.

**Trap**

- management accepts RESIDUAL, not inherent.

**Hook**

- inherent = in the raw
- residual = the residue left over.

**Quick check:** Critical before security work, Low after encryption/MFA/DLP: names, which does owner sign?

**Answer:** Inherent, residual; owner signs residual. Correct.

</details>

<a name="t-2-8-21"></a>
**Risk appetite and tolerance**

How much risk the organization is willing to take on.

> On the exam: Appetite is the overall amount of risk pursued; tolerance is the acceptable variation for a specific risk.

<details><summary>Lesson (14 Oct 2026)</summary>

**Risk appetite and tolerance**

- RISK APPETITE = overall amount/type of risk the org is willing to pursue/accept; broad, strategic; set by BOARD/senior leadership; CSF 2.0 Govern. e.g. low appetite for customer data risk.
- RISK TOLERANCE = acceptable variation around appetite; specific, MEASURABLE limits for a risk/objective. e.g. max 4h downtime/month.
- KRIs set at tolerance thresholds.
- RISK CAPACITY = maximum risk before failing; appetite below capacity.
- Decisions: residual &lt;= appetite/tolerance = accept; > = treat further.

**On the exam**

- broad willingness = appetite
- measurable deviation = tolerance
- sets appetite = board/senior mgmt
- max survivable = capacity.

**Trap**

- security does not set appetite
- it advises.

**Hook**

- appetite = how hungry
- tolerance = how much extra you can stomach
- capacity = the point you would be sick.

**Quick check:** Cautious approach to patient safety risk / portal down max 30 min per quarter: appetite or tolerance?

**Answer:** Appetite, tolerance. Correct.

</details>

<a name="t-2-8-22"></a>
**Technical vs business risk**

Technical risk is the flaw's effect on the system; business risk is financial, legal, or reputational. Explain risk to management in business terms.

> On the exam: A developer says 'SQL injection, CVSS 9.8'; management needs 'the customer database could be stolen, leading to fines and lost trust'.

<details><summary>Lesson (14 Oct 2026)</summary>

**Technical vs business risk**

- TECHNICAL risk = flaw's effect on the SYSTEM in technical terms (SQLi reads users table; CVSS 9.8 RCE); audience = people who FIX it.
- BUSINESS risk = effect on the ORGANIZATION: FINANCIAL (revenue, fines, recovery), LEGAL/REGULATORY (lawsuits, GDPR/PCI, notification), REPUTATIONAL (trust, press, brand), OPERATIONAL (downtime); audience = executives/board/business owners who DECIDE and FUND.

**Why**

- management acts on dollars, not CVEs
- owners decide responses/accept residual. Ties to quantitative ALE, criticality, board metrics.

**On the exam**

- present to senior management = business terms
- effect on system = technical
- revenue/compliance/reputation = business.

**Trap**

- technically severe can be low business risk (isolated test) and vice versa (payment system).

**Hook**

- technical = what breaks
- business = what it costs. Dollars, not CVEs.

**Quick check:** Rewrite "authentication bypass CVSS 9.1 in portal session handler" for the CFO.

**Answer:** My answer: can cause severe customer data leakage. Good direction; stronger with $ estimate, GDPR fines, reputation, and the fix cost next to it.

</details>

<a name="t-2-8-23"></a>
**CMMI** (review)

Capability Maturity Model Integration (from SEI). Five levels: 1 Initial (chaotic), 2 Managed (project-level), 3 Defined (organization-wide standard), 4 Quantitatively Managed (measured), 5 Optimizing (continuous improvement).

> On the exam: Scenario cue: 'processes are documented and used across the whole organization' → Level 3. 'Processes are measured and controlled with metrics' → Level 4.

<details><summary>Lesson (14 Oct 2026)</summary>

**CMMI**

- CMMI = Capability Maturity Model Integration (SEI Carnegie Mellon; now CMMI Institute / ISACA): process maturity.
- 1 INITIAL = chaotic, ad hoc, heroes. 2 MANAGED = planned/tracked at PROJECT level, each project its own way. 3 DEFINED = ORGANIZATION-WIDE standard documented processes. 4 QUANTITATIVELY MANAGED = measured/controlled with data/statistics. 5 OPTIMIZING = continuous improvement.

**Mnemonic**

- I Must Define Quality Optimally.

**Ladder**

- chaos -> each team organized its own way -> everyone same rulebook -> rulebook measured with numbers -> numbers used to keep improving.
- CMMI = general process maturity; SAMM/BSIMM = software security maturity. CMMC = DoD cybersecurity certification (different).

**Why security**

- mature processes = security built into standard process.

**Traps**

- Managed (2) = project
- Defined (3) = organization. Six Sigma named = cross out CMMI/PDCA.

**Hook**

- 2 = each project its own rules
- 3 = whole company one rulebook.

**Quick check:** Projects follow own documented plans + track progress, teams differ; CTO wants one company-wide process. Current/target?

**Answer:** My answer: 4 then 3. Answer: now 2 (Managed), target 3 (Defined). No metrics mentioned so not 4. Marked shaky.

</details>

<a name="t-2-8-24"></a>
**Threat, vulnerability, risk, exploit**

Threat: what could cause harm (attacker, flood). Vulnerability: a weakness. Exploit: the method of using it. Risk: likelihood × impact of a threat exploiting a vulnerability.

> On the exam: Scenario cue: 'unpatched server' → vulnerability. 'Ransomware group' → threat agent. 'Chance of losing data because of it' → risk.

<details><summary>Lesson (14 Oct 2026)</summary>

**Threat, vulnerability, risk, exploit**

- THREAT = anything that could cause harm (WHO/WHAT): hacker, insider, ransomware gang, flood, outage, mistake. Threat agent/actor = the specific one.
- VULNERABILITY = WEAKNESS (the HOLE): unpatched server, SQLi, weak password policy, unlocked room, untrained staff.
- EXPLOIT = METHOD/TOOL to take advantage (HOW): crafted SQLi string, malware abusing a flaw, phishing email.
- RISK = LIKELIHOOD x IMPACT of a threat exploiting a vulnerability.
- ASSET = what you protect. CONTROL/countermeasure = reduces risk.
- Sentence: a threat uses an exploit against a vulnerability to harm an asset; risk = how likely and how bad; controls reduce it.
- House: TV asset; burglar threat; unlocked window vulnerability; climbing in exploit; burglary likelihood x loss risk; lock/alarm control.
- No vuln or no threat = no risk; reduce by fixing vulns or reducing exposure.

**Traps**

- hacker = threat, not vulnerability
- unpatched server = vulnerability, not threat. Zero-day = vuln unknown to vendor
- zero-day exploit = attack code.

**Hook**

- threat = who
- vulnerability = hole
- exploit = how
- risk = how likely x how bad.

**Quick check:** Ransomware gang / unpatched VPN / public script / 30% chance of $1M breach: label.

**Answer:** Threat, vulnerability, exploit, risk. Correct.

</details>

<a name="t-2-8-25"></a>
**Countermeasure cost-benefit** (review)

Value of a control = ALE before − ALE after − annual cost of the control.

> On the exam: Scenario cue: 'a control costs more per year than the loss it prevents' → not justified; accept or find a cheaper control.

<details><summary>Lesson (14 Oct 2026)</summary>

**Countermeasure cost-benefit**

- VALUE OF CONTROL = ALE before - ALE after - annual cost of the control (ACS).
- Positive = worth it; negative = costs more than it saves; zero = break even.
- TWO STEPS: 1) saving = ALE before - ALE after; 2) value = saving - annual cost.

**Example**

- WAF 100k - 20k - 30k = +50k worth it. Not worth: 10k - 2k - 15k = -7k.
- Annual cost includes: purchase spread over life, licenses, implementation, staff time, maintenance, training, performance/productivity impact.
- May still be required despite negative math: legal/compliance (PCI), reputation, human safety.

**Traps**

- compare with ALE not SLE (both per year). ALE after is what is LEFT, not what is cut.

**Hook**

- saved minus spent.

**Quick check:** ALE 200k -> 50k with DLP costing 60k/yr: value, worth it?

**Answer:** My answer: not worth it (compared cost to the 50k left over). Answer: 200k-50k=150k saved; 150k-60k=+90k worth it. Re-check 80k->30k, 70k cost: not worth it, saving 50k correct; value -20k. Marked shaky.

</details>

<a name="t-2-8-26"></a>
**Compliance**

Meeting the requirements of laws, regulations, contracts and internal policies, and proving it with evidence (audits, reports).

> On the exam: Trap: compliance is the minimum. Being compliant doesn't mean being secure, but being non-compliant brings fines and legal risk.

<details><summary>Lesson (14 Oct 2026)</summary>

**Compliance**

- Compliance = meeting requirements of laws, regulations, contracts, internal policies AND PROVING IT WITH EVIDENCE.

**Sources**

- laws (GDPR, HIPAA, SOX)
- industry standards/contracts (PCI DSS, customer clauses, SLAs)
- chosen certifications (ISO 27001, SOC 2)
- internal policies.
- Two halves: doing it + proving it (audit reports, logs, screenshots, signed policies, training records, test results). No proof = not done.
- Checked by: internal audits, external audits (ISO cert audit, PCI QSA, SOC 2), self-assessments (PCI SAQ), continuous compliance monitoring.
- SOC 2 = audit report on service provider controls: security, availability, processing integrity, confidentiality, privacy.
- COMPLIANCE IS NOT SECURITY: compliant but insecure; secure but non-compliant. Compliance = minimum floor; audit = point-in-time snapshot.
- In SDLC: compliance requirements -> security requirements in Requirements phase; RTM = evidence; audit logs built in.

**On the exam**

- passes audit but breached = compliance is not security
- auditors need evidence.

**Hook (user's)**

- DO MORE, BE SECURE. Compliance = we can prove we met the rules
- security = we are actually safe.

**Quick check:** Passed PCI audit in Jan, breached in March via uncovered plugin: compliant? secure? lesson?

**Answer:** Correct: compliance is the minimum, not security; do more, be secure. Added: compliant yes (at audit), secure no; audit = point-in-time, security continuous.

</details>

<a name="t-2-8-27"></a>
**OCTAVE**

Operationally Critical Threat, Asset and Vulnerability Evaluation (Carnegie Mellon/SEI): a self-directed, risk-based assessment run by the organization's own staff, focused on critical assets and operational risk.

> On the exam: Scenario cue: 'internal teams assess their own organizational risk without outside consultants' → OCTAVE.
Don't confuse: OCTAVE = organizational risk; STRIDE/PASTA = application threat modeling.

<details><summary>Lesson (14 Oct 2026)</summary>

**OCTAVE**

- OCTAVE = Operationally Critical Threat, Asset and Vulnerability Evaluation (SEI Carnegie Mellon): risk assessment METHOD.
- SELF-DIRECTED: run by the org's OWN cross-functional analysis team (business + IT), not consultants.
- Focus: CRITICAL ASSETS + OPERATIONAL risk; mostly qualitative; business-driven.

**Phases**

- 1 build asset-based threat profiles (organizational view)
- 2 identify infrastructure vulnerabilities (technological view)
- 3 develop security strategy and plans.

**Variants**

- OCTAVE-S = small orgs
- OCTAVE ALLEGRO = streamlined, INFORMATION ASSETS (most used).
- vs 800-30 (federal guide), ISO 27005 (international guidance): OCTAVE = specific self-directed method.

**On the exam**

- self-directed by own staff = OCTAVE
- critical assets + operational risk = OCTAVE
- streamlined info assets = Allegro
- small orgs = OCTAVE-S.

**Trap**

- not a control catalog or compliance standard.

**Hook**

- an octave is played by YOU, with your own hands.

**Quick check:** Own cross-functional team, critical operational assets, no consultants: method + streamlined info-asset variant?

**Answer:** OCTAVE + Allegro. Correct (voice transcription garbled).

</details>

<a name="t-2-8-28"></a>
**FIPS standards to recognize** (review)

US Federal Information Processing Standards: FIPS 140-2/140-3 (crypto module validation, Levels 1-4), FIPS 197 (AES), FIPS 180 (SHA hashes), FIPS 186 (digital signatures), FIPS 199 (security categorization), FIPS 200 (minimum security requirements), FIPS 201 (PIV smart cards).

> On the exam: Scenario cue: 'US agency requires a validated encryption module' → FIPS 140-3. FIPS 140 Level 1 = software-level basics; Level 4 = strongest physical tamper response.

<details><summary>Lesson (14 Oct 2026)</summary>

**FIPS standards to recognize**

- FIPS = Federal Information Processing Standards (NIST); MANDATORY for US federal systems (most SPs are guidance). Recognition only.
- 140-2/140-3 = CRYPTOGRAPHIC MODULE validation (140-3 current). Levels: 1 basic (approved algorithms, software); 2 TAMPER-EVIDENT + role-based auth; 3 TAMPER-RESISTANT, wipes keys on tamper, identity-based auth (HSMs); 4 highest, environmental attacks, any penetration.
- 197 = AES. 180 = SHA hashes (202 = SHA-3). 186 = digital signatures (DSA, RSA, ECDSA). 199 = security CATEGORIZATION L/M/H for C, I, A (RMF Categorize). 200 = MINIMUM security requirements (points to 800-53). 201 = PIV smart cards.

**On the exam**

- validates crypto modules = 140
- tamper-evident vs resistant = Level 2 vs 3
- categorize = 199
- smart ID card = 201.

**Trap**

- 140 validates the MODULE, not the algorithm (AES = 197).

**Hook**

- 199 rates, 200 sets minimums, 140 checks the crypto box.

**Quick check:** Rate system L/M/H / HSM wipes keys if opened / government smart cards: FIPS numbers?

**Answer:** Skipped. Answers: 199; 140-3 Level 3; 201. Marked shaky until quizzed.

</details>

<a name="t-2-8-29"></a>
**Other NIST SPs to recognize** (review)

800-12 (security handbook), 800-34 (contingency planning), 800-41 (firewalls), 800-61 (incident handling), 800-63 (digital identity and authentication), 800-64 (security in the SDLC, withdrawn), 800-88 (media sanitization), 800-92 (log management), 800-95 (web services security), 800-115 (security testing), 800-160 (systems security engineering).

> On the exam: Scenario cue: match the topic to the number. 'Password and authenticator strength' → 800-63. 'Wiping drives' → 800-88. 'Log management' → 800-92.

<details><summary>Lesson (14 Oct 2026)</summary>

**Other NIST SPs to recognize**

- SPs = guidance (FIPS = mandatory). Known: 800-30 risk assessment, 800-37 RMF, 800-53 controls, 800-88 sanitization, 800-218 SSDF.
- 800-12 = intro/security handbook. 800-34 = CONTINGENCY planning (backups, DR, BCP). 800-41 = FIREWALLS. 800-61 = INCIDENT HANDLING (Preparation -> Detection & Analysis -> Containment, Eradication & Recovery -> Post-Incident Activity). 800-63 = DIGITAL IDENTITY (IAL, AAL, FAL; long passwords, no forced periodic changes, breached-password checks). 800-64 = security in SDLC (WITHDRAWN; replaced by 800-160/SSDF). 800-92 = LOG management. 800-95 = WEB SERVICES security (SOAP/XML). 800-115 = security TESTING (pen test, scanning). 800-160 = SYSTEMS SECURITY ENGINEERING.

**Hooks**

- 12 intro
- 34 keep going when things break
- 41 four walls one gate
- 61 emergency number
- 63 who is me
- 92 write it down
- 95 Windows 95 SOAP era
- 115 test and probe
- 160 big blueprint.

**Trap**

- 800-61 incidents vs 800-34 contingency/disruptions of any kind.

**Quick check:** Ransomware incident guidance / password + MFA rules / pen test: 800-numbers?

**Answer:** Skipped. Answers: 800-61; 800-63; 800-115. Marked shaky until quizzed.

</details>

<a name="t-2-8-30"></a>
**ISO standards to recognize** (review)

ISO/IEC 9126 and its successor 25010 (software quality models, SQuaRE series), 12207 (software lifecycle processes), 15288 (system lifecycle processes), 15408 (Common Criteria), 21827 (SSE-CMM, security engineering maturity), 27000 series (security management).

> On the exam: Scenario cue: 'standard defining software quality characteristics' → ISO 25010 (formerly 9126). 'Software lifecycle processes' → ISO 12207.

<details><summary>Lesson (14 Oct 2026)</summary>

**ISO standards to recognize**

- Known: 27001 certifiable ISMS; 27002 control guidance; 27005 risk; 27034 application security; 15408 Common Criteria.
- 9126 = older SOFTWARE QUALITY model (functionality, reliability, usability, efficiency, maintainability, portability). 25010 = SUCCESSOR, SQuaRE series (25000 family); adds SECURITY as its own quality characteristic (confidentiality, integrity, non-repudiation, accountability, authenticity).
- 12207 = SOFTWARE lifecycle processes. 15288 = SYSTEM lifecycle processes (hardware + software + people + processes).
- 21827 = SSE-CMM (Systems Security Engineering Capability Maturity Model).
- 27000 = overview and vocabulary for the series.

**Hooks**

- 9126 -> 25010 quality (25010 added security)
- 12 software, 15 system (software is part of a system)
- 21827 security maturity
- 27000 dictionary/27001 certificate/27002 control guide/27005 risk/27034 apps.

**Trap**

- 15288 (system lifecycle) vs 15408 (Common Criteria).

**Quick check:** Quality model with security as a characteristic / full software lifecycle processes?

**Answer:** Skipped. Answers: 25010; 12207. Marked shaky until quizzed.

</details>

<a name="t-2-8-31"></a>
**PA-DSS and PCI Secure Software Standard** (review)

PA-DSS was the PCI standard for payment application vendors; it was retired and replaced by the PCI Secure Software Standard and Secure SLC Standard.

> On the exam: Scenario cue: 'vendor builds payment software sold to merchants' → PCI Secure Software Standard (formerly PA-DSS). PCI DSS applies to the merchant's environment.

<details><summary>Lesson (14 Oct 2026)</summary>

**PA-DSS and PCI Secure Software Standard**

- PA-DSS = Payment Application DSS: old PCI standard for VENDORS selling payment apps (POS); RETIRED, validations expired Oct 2022.
- Replaced by PCI Software Security Framework (SSF): SECURE SOFTWARE STANDARD (evaluates the software PRODUCT; direct successor) + SECURE SLC STANDARD (evaluates the vendor's development PROCESS).

**Why**

- covers modern software (cloud, mobile, APIs) and adds process side.

**Fit**

- PCI DSS = merchant/service provider
- Secure Software = product
- Secure SLC = vendor process.

**Trap**

- PA-DSS is not PCI DSS (PA = Payment Application, vendor).

**Hook**

- PA = Payment App (retired). Heirs: Secure Software = product
- Secure SLC = process.

**Quick check:** POS software vendor: current standard for (1) product (2) development process?

**Answer:** I said PCI DSS. Answer: Secure Software Standard; Secure SLC Standard. Marked shaky.

</details>

## 2.9 Secure operation practices

<a name="t-2-9-1"></a>
**Change management**

Request, impact analysis, approval (change board), test, implement, rollback plan, document.

> On the exam: Prevents unauthorized or untested changes. Emergency changes are still documented and reviewed afterwards.

<details><summary>Lesson (15 Oct 2026)</summary>

**Change management**

- Change management = FORMAL process to request, review, approve, test, record production changes (ITIL: approve before production).

**Why**

- unauthorized/untested changes cause outages + incidents
- protects baseline (no drift)
- audit trail.

**Steps**

- RFC (request for change) -> impact analysis incl. SECURITY impact (attack surface, access, data flows, threat model) -> approval by CAB (Change Advisory Board) -> test in non-prod -> implement in change window -> ROLLBACK/BACKOUT plan ready BEFORE -> document, update CMDB/baseline/diagrams, close.

**Types**

- STANDARD = low-risk, pre-approved
- NORMAL = full process + CAB
- EMERGENCY = fast approval by ECAB/designated approver, documented + reviewed AFTERWARD, never skipped.

**On the exam**

- approves normal changes = CAB
- must exist before = rollback plan
- zero-day tonight = emergency change
- dev pushes straight to prod = violation.

**Traps**

- emergency still follows the process, faster
- change mgmt approves/controls, does not build releases.

**Hook**

- ask, assess, approve, test, do, undo-ready, document.

**Quick check:** Active exploit, fix ready 11 PM, CAB meets Monday: what to do?

**Answer:** Emergency change: quick ECAB approval, document and review afterward, never skipped. Correct.

</details>

<a name="t-2-9-2"></a>
**Incident response plan**

NIST SP 800-61: preparation; detection and analysis; containment, eradication, recovery; post-incident activity.

> On the exam: Written before an incident: roles, contacts, escalation, communication. Containment comes before eradication.

<details><summary>Lesson (15 Oct 2026)</summary>

**Incident response plan**

- IR plan = written plan to detect, handle, recover from incidents; created in SDL RELEASE, used in RESPONSE.
- Event = anything observable; incident = event that harms/threatens security.
- NIST SP 800-61 classic phases: 1 PREPARATION (CSIRT, plan, tools, logging, contacts, training, tabletop exercises); 2 DETECTION & ANALYSIS (confirm, scope, severity, prioritize; hardest); 3 CONTAINMENT (stop spread, preserve evidence), ERADICATION (remove cause), RECOVERY (restore from clean backups, monitor); 4 POST-INCIDENT ACTIVITY (lessons learned -> feedback loop).
- Rev 3 (2025) maps to CSF 2.0 functions; exam outline uses the classic four.

**Key**

- contain FIRST
- chain of custody for evidence
- communication plan (legal, PR, regulators, breach deadlines)
- test the plan.

**On the exam**

- first step after confirming = containment
- CSIRT formed = preparation
- lessons learned = improve process
- most important before = prepare.

**Traps**

- recovery before eradication reinfects
- 800-61 incidents vs 800-34 contingency.

**Hook**

- stop the bleeding, remove the bullet, heal, then learn.

**Quick check:** Ransomware on 3 servers; engineer wants to restore from backup immediately. What is wrong, what first?

**Answer:** Contain, eradicate, then restore; restoring first reinfects. Correct. (Also check backups are clean and save evidence.)

</details>

<a name="t-2-9-3"></a>
**Verification vs validation**

Verification: built the product right (meets spec). Validation: built the right product (meets user needs).

> On the exam: Verification: 'Are we building the product right?' Checks work products against specs: reviews, inspections, static analysis.
Validation: 'Are we building the right product?' Checks the product meets the user's real needs: UAT, acceptance tests.
Scenario cue: 'testing confirms the software meets the documented design' → verification. 'Customers confirm it does what they need' → validation.

<details><summary>Lesson (15 Oct 2026)</summary>

**Verification vs validation**

- VERIFICATION = did we build the product RIGHT? Meets the SPECIFICATION (requirements/design docs). Methods: code reviews, inspections, walkthroughs, SAST, unit/integration tests, RTM check. e.g. locks after 5 failed logins as specified.
- VALIDATION = did we build the RIGHT PRODUCT? Meets USERS' real needs in the real environment. Methods: UAT, beta, pilots, operational testing. e.g. lockout works but floods help desk / enables lockout DoS.

**Security**

- verification catches implementation mistakes
- validation catches requirement mistakes. Can pass verification and fail validation.
- SDL Verification phase = mostly verification; validation with users around release.

**On the exam**

- meets specs = verification
- meets user needs = validation
- UAT = validation
- code review vs design = verification.

**Hook**

- verification = built it right
- validation = built the right thing.

**Quick check:** Tester confirms password rules in spec / nurses find 2-min timeout unusable: label.

**Answer:** Verification, validation. Correct.

</details>

<a name="t-2-9-4"></a>
**Assessment and Authorization (A&A)**

Formerly certification and accreditation. Assess controls, then an authorizing official grants authority to operate.

> On the exam: What it is: assess the system's security controls, then a senior official (Authorizing Official) decides whether residual risk is acceptable and grants authority to operate (ATO).
Old terms: certification (technical assessment) and accreditation (management approval).
Scenario cue: 'a major change was made to an authorized system' → reassessment and reauthorization needed.

<details><summary>Lesson (15 Oct 2026)</summary>

**Assessment and Authorization (A&A)**

- A&A = test a system's controls, then a senior official formally approves operation (inside RMF).
- ASSESSMENT = INDEPENDENT ASSESSOR tests controls (implemented correctly, working as intended, desired outcome) -> Security Assessment Report (SAR).
- AUTHORIZATION = AUTHORIZING OFFICIAL reviews results + residual risk: ATO (often with POA&M), denial (DATO), or conditional/interim.

**Old names**

- CERTIFICATION = assessment (technical, Checking)
- ACCREDITATION = authorization (management, Approval). C&A -> A&A.

**Package**

- System Security Plan (SSP), SAR, POA&M.
- Not one-and-done: continuous monitoring; REAUTHORIZATION after significant changes (ties to change management); ongoing authorization.

**On the exam**

- technical evaluation = assessment/certification
- management decision = authorization/accreditation
- grants ATO = AO
- major change = reauthorization.

**Traps**

- assessor never authorizes, AO never tests (separation of duties)
- certification BEFORE accreditation.

**Hook**

- test, then trust.

**Quick check:** Certification and accreditation: modern names and who performs each?

**Answer:** Assessment (test), authorization (trust): correct. Who: independent assessor; Authorizing Official.

</details>

<a name="t-2-9-5"></a>
**Change vs configuration vs release management**

Change management: approves and controls changes. Configuration management: tracks what's installed and how it's configured (baselines, CMDB). Release management: plans, builds, tests and deploys approved changes into production as releases.

> On the exam: Scenario cue: 'who decides if a change can happen?' → change management. 'What versions are on each server?' → configuration management. 'How a set of changes gets packaged and rolled out' → release management.

<details><summary>Lesson (15 Oct 2026)</summary>

**Change vs configuration vs release management**

- CHANGE mgmt = GATEKEEPER: approves/controls changes (RFC, impact analysis, CAB, rollback). May we?
- CONFIGURATION mgmt = RECORD KEEPER: tracks what is installed + how configured; configuration items (CIs), CMDB, baselines, version control, configuration audits (catch drift). What do we have?
- RELEASE mgmt = DELIVERY: plans, builds, tests, deploys approved changes, often BUNDLED as a release (schedule, pipeline, release notes, only approved/tested code, code signing). Ship it.

**Flow**

- change approves -> release bundles/builds/deploys -> configuration records new version + baseline.

**Analogy**

- permit office (change), construction crew (release), blueprints on file (configuration).

**Clue words**

- version on servers/inventory/baseline/drift/CMDB = configuration
- approve/reject/CAB/RFC = change
- bundle/package/deploy/schedule/version X.Y goes out = release.

**Trap**

- change approves, does not deploy
- release deploys, does not approve.

**Quick check:** Which exact library version on every server / CAB rejects firewall port / bundle 12 fixes into v4.2 and deploy.

**Answer:** My answer: release, change, config (1 and 3 swapped). Correct: configuration, change, release. Re-check: config audit finds OpenSSL mismatch = configuration, correct. Marked shaky.

</details>

<a name="t-2-9-6"></a>
**Key performance indicators (KPIs) for security**

Measurable values showing whether security goals are met.

> On the exam: Examples: % of apps threat-modeled, % of builds passing security gates, mean time to remediate critical flaws, % of developers trained.
Trap: a KPI measures performance; a KRI warns of rising risk.

<details><summary>Lesson (15 Oct 2026)</summary>

**KPIs for security**

- Operational security KPIs = measurable values showing operational security goals are met (KPI = performance; KRI = risk building).
- MTTD = mean time to DETECT (lower = better monitoring). MTTR = mean time to respond/recover/remediate (check which R). Patch compliance % within SLA. Baseline compliance % (opposite of drift). Change success rate; % changes with security impact review. Vulnerability SLA compliance by severity. Incident trends (lagging). Uptime vs SLA.

**Rules from 2.5**

- SMART, results not activity, split by severity/criticality, right audience.

**On the exam**

- time to notice = MTTD; % matching hardened config = baseline compliance
- patching meeting goal = patch compliance.

**Trap**

- lower MTTD/MTTR better
- higher compliance % better.

**Hook**

- detect fast, respond fast, stay patched, stay on baseline.

**Quick check:** MTTD 30 days -> 4 days after SIEM: good? which IR phase?

**Answer:** Good, MTTD: correct. Phase = DETECTION AND ANALYSIS (user said response improved).

</details>

## 2.AI AI additions in the current outline

<a name="t-2-ai-1"></a>
**MLSecOps**

DevSecOps extended to machine learning pipelines and retraining loops.

> On the exam: What it is: applying DevSecOps to ML: securing training data pipelines, scanning models, versioning datasets and models, monitoring drift and attacks in production.
Scenario cue: 'models are retrained weekly with no security checks' → add MLSecOps controls to the retraining pipeline.

<details><summary>Lesson (15 Oct 2026)</summary>

**MLSecOps**

- MLSecOps = DevSecOps extended to MACHINE LEARNING: security in every step of building, training, deploying, retraining models.
- MLOps = collect data -> train -> evaluate -> deploy -> monitor -> retrain. Model = trained brain file = an asset.
- New attack surface: training data POISONING; model theft/tampering/leakage (memorization, membership inference, inversion); retraining loops pulling unvetted data; third-party models/datasets with backdoors.

**Controls**

- DATA provenance, validation, change control, poisoning detection
- TRAINING secure env + LINEAGE
- MODEL ARTIFACTS sign + hash, scan third-party models
- DEPLOYMENT endpoint access control, rate limiting, input validation
- MONITORING model drift + abuse
- RETRAINING gated with same checks, never auto-promote
- ML-BOM/AI-BOM.

**On the exam**

- DevSecOps for ML lifecycle = MLSecOps
- verify model unaltered = sign/hash
- auto-retrain on user data = poisoning risk, add validation + gates.

**Trap**

- securing only app code around a model is not enough.

**Hook**

- protect what it learns from, what it is, and how it re-learns.

**Quick check:** Fraud model retrains weekly incl. customer-flagged transactions: risk + control?

**Answer:** Data poisoning; validation + gates + cleaning new training data. Correct.

</details>

<a name="t-2-ai-2"></a>
**Governing AI coding assistants**

Ensure generated code passes the same security gates and doesn't add hallucinated vulnerabilities.

> On the exam: Key controls: approved tools only; never paste secrets or confidential code into public assistants; scan and review generated code like any untrusted code; check licenses of suggested code.
Scenario cue: 'developers paste proprietary code into a public AI chatbot' → data leakage risk; policy plus approved enterprise tool.

<details><summary>Lesson (15 Oct 2026)</summary>

**Governing AI coding assistants**

- Rules + controls so AI-written code is at least as safe as human code.
- CORE RULE: AI code passes the SAME gates (code review, SAST, SCA, tests, bug bar).

**Risks**

- insecure suggestions (string-built SQL, weak crypto, missing validation)
- HALLUCINATED PACKAGES (nonexistent names registered by attackers = SLOPSQUATTING)
- hallucinated APIs/logic
- DATA LEAKAGE (secrets/proprietary/customer data in prompts)
- license/IP (copyleft copied)
- over-trust = AUTOMATION BIAS.

**Controls**

- policy (approved tools, never paste secrets/customer data)
- enterprise settings (no training on your code, retention)
- human review, developer ACCOUNTABLE
- pipeline SAST + secret scanning + SCA flagging unknown/new/unverified packages
- dependency allow-lists/private mirror
- training
- labeling AI code.

**On the exam**

- AI code = same gates + human review
- nonexistent package = hallucinated dependency, verify before install
- API keys pasted into chat = data leakage.

**Traps**

- trusted AI tool, skip review = always wrong
- developer stays accountable.

**Hook**

- treat the AI like a fast junior developer: every line reviewed.

**Quick check:** AI suggests pip install fastjson-secure, published 2 days ago, little info: risk + pipeline action?

**Answer:** Hallucinated dependency; verify before installing (transcription said not verify). Pipeline SCA blocks new/unknown/non-allow-listed packages until verified. Correct.

</details>

<a name="t-2-ai-3"></a>
**OWASP Top 10 for LLM Applications**

Top risks such as prompt injection, sensitive info disclosure, excessive agency.

> On the exam: Know the big ones: prompt injection (first), sensitive information disclosure, supply chain, data poisoning, improper output handling, excessive agency.

<details><summary>Lesson (15 Oct 2026)</summary>

**OWASP Top 10 for LLM Applications**

- OWASP awareness list of top risks in LLM apps (2025). LLM = text AI; prompt = input; system prompt = hidden developer instructions; agent = LLM that takes actions via tools.
- 1 PROMPT INJECTION: DIRECT (user types it: ignore previous instructions) vs INDIRECT (hidden in content the AI reads: email, web page, doc). 2 SENSITIVE INFO DISCLOSURE. 3 SUPPLY CHAIN. 4 DATA AND MODEL POISONING. 5 IMPROPER OUTPUT HANDLING (trusting output -> XSS/SQLi; treat output as untrusted input). 6 EXCESSIVE AGENCY (too many permissions/tools, no human approval). 7 SYSTEM PROMPT LEAKAGE (no secrets in prompts). 8 VECTOR AND EMBEDDING WEAKNESSES (RAG: poisoned docs, cross-user retrieval). 9 MISINFORMATION (hallucination relied on). 10 UNBOUNDED CONSUMPTION (cost/DoS; rate limits, quotas).

**Defenses**

- least privilege for agents
- human approval for high-impact actions
- validate/encode output
- separate/label untrusted content
- no secrets in prompts
- access control on retrieval
- rate limits.

**Test direct vs indirect**

- who typed the malicious instruction? user = direct
- someone else hidden in content = indirect.
- Risk = excessive agency; fix = least privilege + human approval.

**Trap**

- prompt injection cannot be fully prevented by filtering
- limit what the LLM can do.

**Hook**

- do not trust what goes in, do not trust what comes out, do not give it the keys.

**Quick check:** AI email assistant reads/summarizes/sends; attacker email with hidden forward instruction; it forwards 50 emails. Two risks?

**Answer:** My answer: least privilege + direct prompt injection. Correct: INDIRECT prompt injection + EXCESSIVE AGENCY (least privilege is the fix, not the risk name). Marked shaky.

</details>

<a name="t-2-ai-4"></a>
**AI build-break criteria**

Fail the pipeline when bias or hallucination rates exceed thresholds.

> On the exam: What it is: a bug bar for AI: block deployment if model metrics (hallucination rate, bias, toxicity, jailbreak success) exceed agreed thresholds.
Scenario cue: 'how do we stop a worse model from being released automatically?' → AI build-break criteria in the pipeline.

<details><summary>Lesson (15 Oct 2026)</summary>

**AI build-break criteria**

- Bug bar applied to AI models: agreed thresholds that automatically FAIL the pipeline when model quality/safety is not good enough.

**Why**

- AI is probabilistic, so measure RATES and set limits.

**Criteria**

- hallucination rate
- bias/fairness (group differences)
- accuracy/performance (not below minimum or current production = no regression)
- safety/jailbreak resistance via red-team suites
- toxicity
- data leakage/PII
- robustness to adversarial inputs.

**How**

- thresholds agreed EARLY in Requirements (quotes = bug bar)
- automated evaluation suite on every new/retrained model
- quality gate compares
- any failure breaks the build, model not promoted
- exceptions need documented risk acceptance by business owner.
- Link: the MLSecOps gate stopping poisoned/degraded retrained models.

**On the exam**

- stop deployment when bias/hallucination too high = AI build-break criteria
- thresholds set in Requirements
- retrained model worse than production = fail.

**Trap**

- passing functional tests is not enough.

**Hook**

- a bug bar for models.

**Quick check:** Retrained loan model +1% accuracy but 15% age-group gap vs 5% limit: promote?

**Answer:** No, failed the gate (bias threshold). Correct; one failed criterion breaks the build even if accuracy improved.

</details>

<a name="t-2-ai-5"></a>
**Post-quantum cryptography roadmap**

Planning migration to quantum-resistant algorithms.

> On the exam: Threat: attackers harvest encrypted data now to decrypt later. Crypto agility makes migration feasible; NIST standards include ML-KEM and ML-DSA.

<details><summary>Lesson (15 Oct 2026)</summary>

**Post-quantum cryptography roadmap**

- PQC roadmap = plan to move to quantum-resistant algorithms before quantum computers can break today's crypto.
- SHOR'S algorithm BREAKS asymmetric: RSA, ECC, Diffie-Hellman. GROVER'S only WEAKENS symmetric/hashes (halves strength) -> use AES-256.
- HARVEST NOW, DECRYPT LATER: steal encrypted data today, decrypt later; long-lived secrets already at risk; migration takes years.
- NIST 2024: FIPS 203 ML-KEM (Kyber) key exchange; FIPS 204 ML-DSA (Dilithium) signatures; FIPS 205 SLH-DSA (SPHINCS+) hash-based signatures. RSA/ECC deprecated ~2030, disallowed 2035.

**Steps**

- 1 CRYPTO INVENTORY (CBOM) FIRST
- 2 prioritize long-lived sensitive data
- 3 CRYPTO AGILITY (swap via config)
- 4 HYBRID mode (classical + PQC)
- 5 test/migrate/monitor (larger keys/signatures)
- 6 vendor plans.

**On the exam**

- store now decrypt later = harvest now decrypt later
- first step = crypto inventory
- easy future changes = crypto agility
- quantum breaks asymmetric.

**Trap**

- wait until quantum computers exist = wrong.

**Hook**

- find it, make it swappable, swap it. Quantum breaks public-key, dents AES.

**Quick check:** Gov health agency: why migrate now, first step?

**Answer:** Harvest now decrypt later + long migration; first = find it (crypto inventory). Correct.

</details>
