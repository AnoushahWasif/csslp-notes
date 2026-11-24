# Glossary

Short definitions and lists to memorise, grouped by section.

## 1.1 Core concepts

### AAA protocols

- **802.1X** (Port-based network access control): Common with RADIUS for Wi-Fi and wired network login.
- **Diameter** (Successor to RADIUS): Used in mobile/telecom networks.
- **RADIUS** (Remote Authentication Dial-In User Service): UDP; combines authentication + authorization; encrypts only the password. Wi-Fi (802.1X), VPN.
- **TACACS+** (Terminal Access Controller Access-Control System Plus): TCP; separates all three A's; encrypts the whole payload; per-command authorization. Admin access to network devices.

### Authentication & MFA

- **Adaptive / risk-based authentication** (Extra checks only when something is unusual): New device, new country, impossible travel.
- **FIDO2 / Passkeys** (Fast IDentity Online 2): Hardware keys or device passkeys. Most phishing-resistant MFA.
- **MFA / 2FA** (Multi-Factor / Two-Factor Authentication): Two or more DIFFERENT factor types.
- **MFA fatigue** (Spamming push approvals): Attacker floods push requests until the user taps approve.
- **OTP / TOTP** (One-Time Password / Time-based One-Time Password): Short-lived codes, e.g., from an authenticator app.
- **SIM swapping** (Attacker moves your phone number to their SIM): Why SMS is the weakest second factor.
- **Step-up (re-)authentication** (Asking for proof again before a sensitive action): E.g., before changing email or password. Protects against stolen sessions.
- **Username enumeration** (Learning which accounts exist): Caused by errors like 'user not found'. A form of information disclosure. Fix: generic messages.

### Biometrics

- **CER / EER** (Crossover Error Rate / Equal Error Rate): Point where FAR = FRR. Used to COMPARE devices: lower = more accurate. Not how you set a high-security threshold.
- **FAR** (False Acceptance Rate = Type II error): Impostor accepted. Security breach; more dangerous.
- **FRR** (False Rejection Rate = Type I error): Legitimate user rejected. Annoying, not a breach.
- **Liveness detection** (Checking a real person is present): Stops photos, masks, fake fingers, recordings.
- **Physiological vs behavioral** (What you are vs what you do): Fingerprint, iris, face vs voice, signature, typing, gait (more variable).
- **Template** (Mathematical summary of a biometric): Store templates, never raw images.
- **Threshold rule** (Set by what you protect): High security → keep FAR low (strict). Convenience → lower FRR.
- **Throughput** (How many people per minute): A selection factor, with enrollment time and user acceptance.

### Crypto, hashing & encoding

- **AES** (Advanced Encryption Standard): Symmetric (one shared key), fast. Standard choice for data encryption.
- **Base64** (Encoding scheme): Turns binary into text. Anyone can decode it: NOT security.
- **bcrypt, scrypt, Argon2, PBKDF2** (Slow password-hashing algorithms): Deliberately slow to make brute force expensive. Use for passwords.
- **DES / 3DES** (Data Encryption Standard / Triple DES): Old symmetric ciphers. Avoid.
- **Digital signature** (Hash signed with the sender's private key): Verified with the public key. Provides nonrepudiation.
- **ECC** (Elliptic Curve Cryptography): Asymmetric, same strength as RSA with shorter keys. Good for mobile/low-power.
- **Hash vs encrypt vs encode** (Compare only vs need original back vs format only): Passwords → hash. Card numbers for refunds → encrypt. Binary in JSON → encode.
- **HMAC** (Hash-based Message Authentication Code): A MAC built from a hash function + shared key. Still no nonrepudiation (both sides hold the key).
- **HSM** (Hardware Security Module): Tamper-resistant device that stores keys and does crypto; keys can't be exported.
- **MAC** (Message Authentication Code): Checksum made with a shared secret key. Integrity + authenticity between two parties. No nonrepudiation.
- **MD5 / SHA-1** (Message Digest 5 / Secure Hash Algorithm 1): Broken hashes (collisions). Don't use.
- **Output encoding** (Converting output so browsers treat it as text): Main defense against XSS. Doesn't hide data.
- **PKI / CA** (Public Key Infrastructure / Certificate Authority): System of certificates binding public keys to identities; the CA signs them.
- **RSA** (Rivest-Shamir-Adleman): Asymmetric (public/private key pair). Key exchange and signatures.
- **Salt** (Unique random value added before hashing): Makes identical passwords hash differently; defeats rainbow tables. Not secret, must be unique.
- **SHA-256** (Secure Hash Algorithm, 256-bit): Current standard hash for integrity checks.
- **Symmetric vs asymmetric** (One shared key vs public/private key pair): Symmetric = fast bulk encryption. Asymmetric = key exchange, signatures.
- **TLS** (Transport Layer Security): Encrypts data in transit (HTTPS). Use 1.2 or 1.3.
- **XSS** (Cross-Site Scripting): Attacker's script runs in other users' browsers. Defense: output encoding + input validation.

### Governance, assurance & quality

- **Bug bar** (Break/build criteria): Objective rules blocking release with critical flaws.
- **Common Criteria** (ISO/IEC 15408): Product security evaluation. EAL (Evaluation Assurance Level) 1-7 = how thoroughly evaluated, not how secure.
- **FIPS 140-3** (Federal Information Processing Standard 140-3): US validation of cryptographic modules.
- **GDPR / HIPAA / SOX** (General Data Protection Regulation / Health Insurance Portability and Accountability Act / Sarbanes-Oxley Act): EU personal data / US health data / US public company financial reporting.
- **PCI DSS** (Payment Card Industry Data Security Standard): Contractual industry standard for card data. Compliance ≠ security.
- **Risk acceptance** (Business owner formally accepts residual risk): Release decisions are business decisions, made with security's risk information.
- **RTM** (Requirements Traceability Matrix): Links requirement → design → code → test. Catches broken security profile chains.
- **SAST / DAST** (Static / Dynamic Application Security Testing): Scan code without running it / test the running app from outside.
- **SBOM** (Software Bill of Materials): List of all components in the software.
- **Software assurance** (JUSTIFIED confidence): Evidence it's free of vulnerabilities and works as intended. Evidence must match the claim.

### Identity, SSO & federation

- **Access recertification** (Periodic access review): Managers/data owners confirm access is still needed.
- **AD / LDAP** (Active Directory / Lightweight Directory Access Protocol): Directory where identities live / protocol to query directories.
- **Federated identity** (Trust across organizations): Use an identity from one organization in another's apps.
- **IAM** (Identity and Access Management): Managing identities and access across their whole lifecycle.
- **IdP** (Identity Provider): Verifies the user and issues the token/assertion (e.g., Microsoft Entra ID, Okta, Google).
- **JWT** (JSON Web Token): Signed token format used by OIDC and APIs. Validate signature and expiry; reject 'alg: none'.
- **OAuth 2.0** (Open Authorization): Delegated AUTHORIZATION: lets an app access something without your password. Not authentication on its own.
- **OIDC** (OpenID Connect): Identity layer on OAuth 2.0; adds an ID token. AUTHENTICATION for modern web/mobile apps.
- **Orphaned account** (Active account of someone who left): Leaver-process failure. Fix: automated HR-driven deprovisioning.
- **PAM** (Privileged Access Management): Extra control for admin accounts: password checkout, session recording, just-in-time access.
- **Privilege creep** (Access piling up over time): Mover-process failure. Fix: remove old access on role change + reviews.
- **RBAC / ABAC** (Role-Based / Attribute-Based Access Control): Access by job role / by attributes like time, location, department.
- **SAML 2.0** (Security Assertion Markup Language): XML assertions. Enterprise web SSO and federation. Authentication.
- **Scope (OAuth)** (Permissions an app requests): Request the minimum (least privilege).
- **SP / RP** (Service Provider / Relying Party): The app that trusts the IdP's token.
- **SSO** (Single Sign-On): Log in once, use many apps. Single point of compromise → add MFA at the IdP.

### Kerberos

- **AS** (Authentication Service): Part of the KDC that verifies you and issues the TGT.
- **Golden ticket** (Forged ticket after KDC compromise): Grants access to anything. Why the KDC must be hardened.
- **KDC** (Key Distribution Center): Trusted third party = AS + TGS. Single point of failure AND of compromise.
- **Kerberos** (Ticket-based authentication protocol): Used by Windows AD. Passwords never cross the network. Symmetric crypto.
- **NTP** (Network Time Protocol): Keeps clocks in sync. Kerberos fails if clocks differ by more than about 5 minutes.
- **Pass-the-ticket** (Reusing a stolen ticket): Works until the ticket expires.
- **Service ticket** (Pass for one specific service): Presented to the service you want to use.
- **TGS** (Ticket Granting Service): Part of the KDC that issues service tickets.
- **TGT** (Ticket Granting Ticket): Your 'day pass' after first login; shown to the TGS.

### Lists to memorize

- **AAA** (Authentication, Authorization, Accounting): Who are you, what may you do, what did you do. Accounting = tracking/logging, not money.
- **Access control sequence** (Identification → Authentication → Authorization → Accountability): Claim → prove → permit → record. Each depends on the one before.
- **Authentication factors** (Know, Have, Are (+ Where, Do)): Password/PIN; phone/token/smart card; fingerprint/face; location; behavior. MFA needs different types.
- **CIA triad** (Confidentiality, Integrity, Availability): The three core security goals.
- **Compliance sources** (Regulatory, Contractual/industry, Internal): Laws (GDPR, HIPAA, SOX); PCI DSS, contracts; company policies.
- **Digital signature gives** (Integrity, Authenticity, Nonrepudiation): NOT confidentiality; add encryption for that.
- **GRC** (Governance, Risk management, Compliance): Direct and control; decide what to protect; meet rules and prove it.
- **Holistic security: dimension 1** (People, Process, Technology): Training and roles; secure SDLC, reviews, change management; tools.
- **Holistic security: dimension 2** (Network, Host/OS, Application, Data): Every layer of the stack needs protection.
- **Identity lifecycle** (Joiner → Mover → Review → Leaver): Provision, change (remove old access), recertify, deprovision immediately.
- **Iron triangle** (Scope, Schedule, Budget): Scope includes resources/people. Quality and security sit in the middle and suffer when it's squeezed.
- **Log entry contents** (Who, What, When, Where, Outcome): User ID, action, synced timestamp, source, success/failure.
- **Secure software qualities (ISC2)** (Reliable, Resilient, Recoverable): Works under normal conditions; withstands attack; restores after failure.
- **Security profile** (Core concepts + design principles, carried through every phase): Core: confidentiality, integrity, availability, authentication, authorization, accountability, nonrepudiation. Phases: requirements, design, implementation, testing, deployment/operations, disposal.
- **Software assurance threats** (Unintentional, Intentional): Mistakes (bugs, design flaws) vs inserted malicious code (backdoors, logic bombs).
- **Token validation checks** (Signature, Issuer, Audience, Expiry): Apps must verify all four before trusting an SSO/federation token.

### Logging & accountability

- **Detective control** (Finds problems after they happen): Logging and auditing are detective, not preventive.
- **Log injection** (Inserting fake log lines through input): Prevent by encoding data before logging.
- **Nonrepudiation** (Can't deny an action): Origin (can't deny sending) and receipt (can't deny receiving). Digital signatures.
- **SIEM** (Security Information and Event Management): Collects and correlates logs, alerts in real time.
- **STRIDE: R** (Repudiation): Threat countered by nonrepudiation: signatures + secure logs.
- **WORM** (Write Once, Read Many): Append-only storage that protects logs from tampering.

### Resilience

- **Circuit breaker** (Stop calling a failing service): Prevents one failure from hanging the whole app.
- **DoS / DDoS** (Denial of Service / Distributed DoS): Overwhelming a system. Defend with rate limiting, throttling, scaling.
- **Fail secure (fail closed)** (Deny access on failure): Staying up must never mean letting everyone in.
- **Graceful degradation** (Non-essential features fail; core keeps working): Key resiliency technique.
- **SPOF** (Single Point of Failure): One component whose failure stops everything. Fix: redundancy and failover.

### Usability

- **Alert fatigue** (Too many prompts → users click Allow): Usability failure that weakens security.
- **NIST SP 800-63B** (Digital identity guidelines): Length over complexity, no forced periodic changes without cause, check breached-password lists.
- **Psychological acceptability** (Security must be usable): If it's too hard, users bypass it.
- **Shadow IT** (Unapproved tools used by staff): Often caused by security that's too restrictive.

## 1.2 Design principles + AI additions

### AI additions

- **Backdoor poisoning** (Targeted poisoning): Model works normally except with a trigger.
- **Data poisoning** (Corrupting training data): Integrity attack at training time.
- **Differential privacy** (Adding noise during training so no single record can be detected): Main defense for inversion/inference.
- **Guardrail** (Deterministic guardrail): Code checks AI output before it's used.
- **Hallucination**: Confident but false AI output.
- **LLM** (Large Language Model): Main AI model type behind chatbots.
- **Membership inference** (Was this record in the training data?): Models are more confident on training data.
- **Model inversion** (Reconstructing training data from outputs): Uses outputs/confidence scores to rebuild training data.
- **Non-deterministic outputs** (Same input, different outputs): Test statistically; wrap in deterministic validation.
- **Overfitting** (Model memorizes examples instead of patterns): Makes memorization and inference easier.
- **Red-teaming** (Adversarial testing): People repeatedly trying to make a system misbehave.
- **Temperature** (Setting controlling randomness): Lower = less random, but never fully deterministic.
- **Training data memorization** (Model repeats training data word for word): Root fix: clean secrets/PII from training data; rotate leaked secrets.

### Lists to memorize

- **Diversity of defense** (Technical (vendor), Geographic, Control type): Layers are stronger when they differ.
- **Least privilege vs least common mechanism** (What you can do vs what you share): Least privilege = the key you're given. Least common mechanism = the room you share.
- **Least privilege vs need-to-know** (Rights vs data): Least privilege = what actions. Need-to-know = which specific data.
- **Original 8 principles** (Economy of mechanism, Fail-safe defaults, Complete mediation, Open design, Separation of privilege, Least privilege, Least common mechanism, Psychological acceptability): Plus two extras: work factor, compromise recording.
- **Saltzer and Schroeder** ('The Protection of Information in Computer Systems'): 1975 paper listing the original 8 design principles.
- **SoD vs dual control vs split knowledge** (Steps vs together vs knowing): Separation of duties: different people, different steps (time). Dual control: several people, same action, at once. Split knowledge: each knows only part of a secret.
- **Zero Trust principles** (Verify explicitly, Least privilege access, Assume breach): From NIST SP 800-207.

### Principles

- **Complete mediation** (Check authorization on every access, every time): Not just at login; no long caches.
- **Component reuse** (Reuse proven components (leveraging existing components)): You inherit their flaws; track and patch them.
- **Covert channel** (Risk created by shared mechanisms): Hidden ways to pass information.
- **Defense in depth** (Multiple layers of controls): Independent layers cover each other's gaps.
- **Dual control / multi-party control** (Two+ people must act together, at the same time): Two keys turned at once.
- **Economy of mechanism** (Keep designs small and simple (KISS)): Simplicity is easier to verify; smaller attack surface.
- **Fail secure vs fail safe** (Fail closed (deny) vs fail open (protect people, e.g., doors unlock in fire)): Software should fail secure on access checks.
- **Fail-safe defaults** (Deny unless explicitly allowed): In Saltzer and Schroeder this = default deny (same idea as fail secure).
- **Failover** (Automatic switch to a backup): Active-active: all serve traffic. Active-passive: standby takes over.
- **Four-eyes** (Maker-checker / four-eyes principle): Approval by a second person.
- **JIT** (Just-in-time access): Admin rights granted for a short window, removed automatically.
- **Job rotation / mandatory vacation** (Supporting controls for SoD): Help detect fraud hidden by one person.
- **Lateral movement** (Attacker moving from one system to others): What Zero Trust and segmentation prevent.
- **Least common mechanism** (Minimize mechanisms shared between users): Shared temp folders, shared service accounts, shared caches. Fix: isolation.
- **Least privilege** (Only the access needed): Minimum rights, minimum time. Limits blast radius.
- **Log4Shell** (Log4j vulnerability): 2021 flaw in the Log4j logging library; classic inherited-risk example.
- **M-of-N control** (Any M of N authorized people): e.g., any 3 of 5.
- **Micro-segmentation** (Small network zones): Each service reaches only what it needs.
- **Need-to-know** (Access to specific data only if your task needs it): Clearance alone isn't enough.
- **Open design / Kerckhoffs's principle** (Only the key is secret): Security must not depend on a secret design.
- **Psychological acceptability** (Security must be easy to use correctly): If it's too hard, people bypass it.
- **Run-time privileges** (Elevate briefly, then drop): Least privilege over time (sudo, UAC, JIT access).
- **SBOM** (Software Bill of Materials): List of all components and versions in software.
- **SCA** (Software Composition Analysis): Finds known vulnerabilities and license issues in third-party components.
- **Security through obscurity** (Relying on secrecy of the design): Secret algorithms, hidden URLs. Opposite of open design.
- **Shamir's secret sharing** (Threshold scheme splitting a secret into N shares): Any M shares rebuild it; fewer reveal nothing. Security + availability.
- **SoD (separation of duties)** (No one person completes a critical task alone): Fraud then needs collusion.
- **Split knowledge** (Each person knows only part of a secret): No one person has the whole secret.
- **SPOF** (Single Point of Failure): Fix with redundancy and failover. Backups ≠ failover.
- **Static vs dynamic SoD** (Two ways to enforce SoD): Static: conflicting roles can't be held together. Dynamic: may hold both, can't use both on the same transaction.
- **Weakest link** (System is only as strong as its weakest part): Attackers take the easiest path.
- **Zero Trust** (Never trust, always verify): No trust based on network location. NIST SP 800-207.

## 2.1 Development methodologies

### Existing software

- **Anti-reversing**: Obfuscation, anti-debugging, tamper checks, code signing.
- **RE tools** (Disassembler / decompiler / debugger): Machine code → assembly / compiled code → readable code / run step by step.
- **Re-engineering**: Rebuilding/migrating existing software. Redo threat model; full testing; old assumptions break.
- **Reverse engineering**: Understanding a finished product without source. Malware analysis vs IP theft. Defense: no secrets in client code.

### Lists to memorize

- **CI vs CD vs CD** (Continuous Integration / Delivery / Deployment): CI: merge + auto test often. Delivery: always releasable, HUMAN approves. Deployment: auto to production, NO approval.
- **NIST lifecycle** (NIST system lifecycle (5 phases)): Initiation (categorize), Development/Acquisition (select controls), Implementation/Assessment (assess + ATO), Operations/Maintenance (monitor), Disposal (sanitize).
- **SDL phases** (Microsoft SDL phases): Training, Requirements, Design, Implementation, Verification, Release, Response.
- **SDLC phases** (Software Development Lifecycle): Requirements, design, development, testing, deployment, operations & maintenance, disposal.
- **Security in Agile** (Stories, Done, Automate, Champions): Security stories (incl. abuse stories), security in the Definition of Done, Automated security tests, security Champions.
- **Spiral loop** (Spiral quadrants): Objectives → risk analysis (prototype) → develop & test → plan next loop.
- **TDD cycle** (Red → Green → Refactor): Write failing test → make it pass → clean up.
- **V-model pairs**: Requirements ↔ acceptance; system design ↔ system test; architecture ↔ integration test; module design ↔ unit test.

### Models

- **Abuse story** (Abuse / evil user story): Feature written from the attacker's view: 'As an attacker, I want...'
- **Agile / Scrum** (Agile framework): Short sprints, changing requirements, frequent releases.
- **DoD** (Definition of Done): Checklist an item must pass to count as finished. Put security checks in it.
- **Iterative model** (Iterative): Repeated cycles, each producing a working version. Redo threat model every iteration.
- **Iterative vs incremental**: Iterative refines the whole; incremental delivers piece by piece.
- **Kanban**: Visual board, cards, columns, WIP limits, continuous pull. Make security visible as cards/column rules.
- **Lean**: Eliminate waste, deliver value. Late-found flaws = waste (rework).
- **Pair programming**: Driver types, navigator reviews. = continuous code review.
- **Prototyping**: Quick rough model to clarify requirements. Throwaway vs evolutionary. Risk: demo becomes product.
- **RAD** (Rapid Application Development): Speed via prototypes, reuse and heavy user involvement.
- **Scrum roles**: Product Owner (priorities), Scrum Master (coach), Development Team.
- **Spiral** (Risk-driven model): Iterative with formal risk analysis at the start of every cycle. Large, high-risk, unclear requirements. Barry Boehm.
- **Sprint** (Scrum iteration): Fixed time-box (1-4 weeks) producing a working increment.
- **TDD** (Test-Driven Development): Tests written before code. Security tests first + regression protection.
- **V-model** (Verification and Validation model): Each build phase paired with a test phase; tests planned early, run later. Safety-critical/regulated.
- **Waterfall** (Sequential model): Linear, phase by phase. Stable requirements, heavy documentation. Security: phase gates.
- **WIP limits** (Work-In-Progress limits): Caps on cards per column.
- **XP** (Extreme Programming): Pair programming (continuous review), TDD, continuous integration, refactoring, collective ownership.

### Modern delivery & programs

- **ATO** (Authorization To Operate): Senior official accepts residual risk before go-live.
- **Categorization** (FIPS 199 categorization): Impact level low/moderate/high for C, I, A; done in NIST initiation.
- **Defect cost curve** (Cost of fixing defects): Later = costlier (production often 10-100x design). Do early activities.
- **DevOps**: Development + Operations; automation, CI/CD, shared responsibility.
- **DevSecOps**: Security built into DevOps and automated in the pipeline; everyone's job.
- **FSR** (Final Security Review): Last SDL gate before release: all activities done, bug bar met.
- **Microsoft SDL** (Security Development Lifecycle): Microsoft's process; training first; threat modeling in design; FSR + response plan at release.
- **Pipeline** (CI/CD pipeline): Automated build, test, scan and deploy flow. Itself a high-value target.
- **Security as code**: Security policies and configs written as version-controlled code.
- **Security champions**: Developers in each team with extra security training/time; scale security; don't replace the security team.
- **Shift left**: Move security activities earlier in the lifecycle.
- **Touchpoints** (Gary McGraw's model): Seven security activities attached to existing development artifacts.

## 2.2 Security standards and awareness

### Don't confuse

- **Attest vs assertion** (SSDF attestation / SAML assertion): Attest = company swears in writing. Assertion = system tells another system who the user is.
- **Background words** (SOX, SBOM, SAST, SOAP, PCI DSS): SOX = US financial-reporting law. SBOM = software ingredient list. SAST = scans code without running it. SOAP = envelope-style message format. PCI DSS = card payment rules.
- **Framework vs standard** (Flexible vs Strict): Framework = adapt it (SSDF, SAMM). Standard = MUST (PCI DSS). After choosing a framework: gap analysis next.
- **Owner vs custodian** (Decides vs does): Data owner decides classification/access; custodian (DBA) implements. Business owner accepts residual risk; security advises.
- **SAML vs XACML vs SPML** (Who you are / what you may do / account exists): Key card picture: SPML gives the card, SAML shows whose card it is, XACML decides which doors it opens.
- **Socratic method** (Questioning): Ask questions (often negative form) so the person reaches the conclusion; not policy or escalation.

### Frameworks & standards

- **COBIT** (ISACA IT governance framework): IT controls checklist with the board at the top. Aligns IT with business goals; auditors evaluate IT controls with it.
- **COSO** (Treadway internal control framework): Company-wide internal control, financial reporting, fraud. Used for SOX; paired with COBIT for IT controls.
- **ISO/IEC 27034** (Application security standard): International (IS-O and O-NF share the O). Process-based; no coding rules. ONF = org library, ANF = one app's subset, ASC = control + proof.
- **ITIL** (IT service management): IT's daily to-do list. Incident = restore; Problem = root cause; Change = approve before production. Org certification = ISO 20000.
- **NIST SSDF** (NIST SP 800-218): US (N = National). Secure dev practices for any SDLC; outcome-based. Federal suppliers ATTEST (EO 14028). No certification. 800-218A = AI add-on.
- **OASIS** (Standards organization): Not a framework. SAML = SAMe Login (assertion). XACML = Access Control rules (PDP decides, PEP enforces). SPML = Provisioning. WS-Security = protects SOAP messages.
- **Secure coding standard** (e.g., SEI CERT): Mandatory rules per language. Banned functions (strcpy, gets, sprintf). Enforce via SAST/linters + review. OWASP Top 10/CWE/CVE are NOT coding standards.
- **Six Sigma** (Statistical quality method): 3.4 defects per million. Belts = experts. If Six Sigma is named, only DMAIC/DMADV count.

### Lists to memorize

- **Awareness / Training / Education** (What / How / Why): Awareness = everyone (posters, phishing tests). Training = your role, hands-on. Education = deep why, future problems.
- **COBIT domains** (EDM + APO, BAI, DSS, MEA): EDM = governance (board). APO, BAI, DSS, MEA = management (IT). Capability levels 0-5.
- **COSO components** (CRIME): Control environment (tone at the top), Risk assessment (incl. fraud), Information & communication, Monitoring, Existing control activities (approvals, SoD). Objectives (NOT components): operations, reporting, compliance.
- **DMAIC vs DMADV** (Six Sigma methods): DMAIC = Improve EXISTING (Define, Measure, Analyze = root cause, Improve, Control). DMADV = Design NEW (Define, Measure, Analyze, Design, Verify).
- **Governance documents** (Policy, Standard, Procedure, Guideline): Policy = intent. Standard = specific + mandatory. Procedure = numbered steps. Guideline = optional.
- **PDCA** (Plan, Do, Check, Act (Deming)): Plan = goals/controls, Do = implement, Check = LOOK (measure, audit), Act = FIX. Pick what the subject is doing now.
- **SSDF groups** (PO, PS, PW, RV): Prepare (before: roles, training, tools), Produce (during: design, threat model, code review, SAST), Protect (padlock: sign, hash, archive, SBOM, repo access), Respond (after release: reports, fix, root cause).

## 2.3 Strategy and roadmap

### Don't confuse

- **Gate vs bug bar** (Checkpoint vs criteria): The gate is the checkpoint; the bug bar is the criteria it applies.
- **Milestone vs gate** (Review vs block): Milestone only reviews; a gate blocks. 'Can't move forward until...' = gate.
- **Who approves an exception** (Gate exceptions): Bypass only with documented risk acceptance by the accountable business owner (security advises), with conditions and expiry. Not the person in a hurry.

### Lists to memorize

- **2.3 in one line** (Where / Must pass / The rule): Milestone = WHERE we stop and review. Gate = MUST PASS to continue. Bug bar = THE RULE the gate uses.
- **Gate outcomes** (Gate decisions): Go / No-go / Go with conditions (documented exception).
- **Typical checkpoints** (Security checkpoints by phase): Requirements (security reqs + bug bar), Design (threat model), Implementation (code review, SAST), Testing (DAST, pen test), Release (FSR + incident response plan).

### Strategy and roadmap

- **Automated gate** (Automated quality gate): CI/CD pipeline fails the build when criteria aren't met (e.g., high SAST finding). Fits Agile/DevSecOps.
- **Bug bar** (Break/build criteria): Pre-agreed severity rules for what breaks the build/blocks release (e.g., Critical/High = must fix). Microsoft SDL term. Set in REQUIREMENTS, applied at gates and the FSR.
- **CVSS**: Common Vulnerability Scoring System: severity score 0-10.
- **Gate** (Control gate / quality gate): Checkpoint with teeth: can't move to the next phase until exit criteria are met. Also phase/stage/quality gate.
- **Milestone** (Security milestones / checkpoints): Planned points where security is reviewed. Benefits: early (cheap) fixes, visibility, audit evidence, accountability.

## 2.4 Security documentation

### Documents

- **Baseline** (Security baseline): Minimum mandatory configuration for a system type (the floor). Sources: CIS Benchmarks, DISA STIGs. Built via golden images/IaC.
- **Drift** (Configuration drift): Systems slowly stop matching the baseline. Fix: scan against the baseline and RESTORE the systems. Never change the baseline to match drift (baseline changes only via change control).
- **Guideline**: 'Should', 'encouraged', 'where practical', 'may choose' = optional advice.
- **Policy**: Management intent (what/why), signed by senior management, NO technology named, rarely changes. Types: organizational, issue-specific, system-specific.
- **Procedure**: Mandatory numbered steps (how). Most detailed. A runbook is an operations procedure.
- **Standard**: 'Must' + specific, measurable tech rule (TLS 1.2+, AES-256). Test: can a tool check it? Yes = standard; no = policy.

### Don't confuse

- **Standard vs baseline** (One rule vs full config): Standard = one specific rule. Baseline = full set of settings for a system type. Both mandatory.

### Lifecycle documents

- **Lifecycle docs** (Docs by SDLC phase): Requirements: RTM. Design: threat model, DFDs. Implementation: code review, SAST. Testing: test plan, pen test report. Release: FSR, risk acceptance, SBOM, secure install guide. Ops: runbooks, IR plan. Retirement: decommission plan.
- **RTM** (Requirements Traceability Matrix): Links each requirement to design, code and test; proves nothing was dropped; shows missing test cases.
- **Runbook**: Step-by-step guide operations staff follow for routine tasks/incidents (e.g., certificate renewal).
- **Threat model**: Living document; update whenever the design changes (e.g., new feature).

### Lists to memorize

- **Hierarchy** (Document hierarchy): Policy (top) → Standards + Baselines → Procedures. Guidelines alongside as advice. Lower docs support the ones above.
- **Mandatory?** (Mandatory vs optional): Mandatory: policy, standard, baseline, procedure. Optional: guideline ONLY.
- **Which changes most** (Change frequency): Least → most: Policy → Standard → Procedure. More detail = changes more often. Top is stable, bottom moves.

## 2.5 Security metrics

### Don't confuse

- **Criticality vs classification** (System importance vs data sensitivity): Criticality = how much business needs the system. Classification = how sensitive the data is.
- **Defect vs vulnerability** (Bug vs exploitable bug): Every vulnerability is a defect; not every defect is a vulnerability.

### Good metrics

- **Goodhart's law** (Metric gaming): When a measure becomes a target, people game it. Defense: pair metrics, audit.
- **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound): Checklist for good metrics. Also consistent, cheap to collect, actionable, fit the audience.
- **Vanity metric** (Looks good, drives no decision): Counts activity not results (scans run, firewall rules). Busy is not better.

### Measures

- **Cyclomatic complexity** (McCabe complexity): Number of independent paths (each if/loop/case +1). >10 risky. = minimum test cases for all paths. Risk indicator: vulns more LIKELY, not proven.
- **MTTR** (Mean time to remediate): Average days from discovery to VERIFIED fix. Shrinks window of exposure. Split by severity, compare to SLA. Counts only FIXED bugs: also track age of open vulns + % within SLA.
- **Vulnerability density** (Vulns per KLOC): Count / thousands of lines of code. Fair comparison across app sizes. Rises when DETECTION improves (new SAST tool), not necessarily worse code.
- **Window of exposure** (Time a flaw stays exploitable): Time attackers have to exploit a flaw; lower MTTR shrinks it.

### Metric types

- **KPI** (Key Performance Indicator): How well we are DOING against a goal; past results. Cues: performance, target, achieved, efficiency.
- **KRI** (Key Risk Indicator): How much DANGER is building; early warning before an incident. Cues: threshold, exposure, trending up, tolerance. Same data can feed both: read what it is USED FOR.
- **OKR** (Objectives and Key Results): Objective = goal in words, no numbers. Key results = 2-5 measurable OUTCOMES with deadline (not activities). KPI = dashboard; OKR = GPS destination.

### Prioritizing

- **Criticality level** (Business importance rating): How much the business needs an asset (Critical/High/Medium/Low) from a BIA; business owner decides. Fix order = CVSS severity + asset criticality + exposure.
- **CVSS** (Common Vulnerability Scoring System): 0-10 TECHNICAL severity (9.0-10 Critical). Does not know business value.

### Timing

- **Lagging indicator** (Measures outcome): The security outcome itself, after the fact: breaches, incidents, losses. Rear-view mirror. Outcome = lagging, cause = leading; ignore verb tense.
- **Leading indicator** (Predicts outcome): Cause that predicts future results so you can act before: % devs trained, % threat-modeled, % code scanned. Windshield.

## 2.6 Decommission applications

### Cleanup

- **CMDB** (Configuration management database): List of IT components and how they connect; used to find everything tied to the app.
- **Credential removal** (Accounts, secrets, certs, DNS, firewall): Remove service accounts, keys, connection strings; REVOKE certificates; remove firewall rules, DNS, jobs. Shutting the server does not remove accounts on OTHER systems.
- **License/SLA cancellation** (End contracts and services): Cancel AFTER data is out. Cancellation does not delete data at the vendor: require deletion + certificate of destruction; revoke vendor access.
- **Subdomain takeover** (Dangling DNS record): Old DNS still points to a released cloud address; attacker claims it and hosts content on your domain.

### Data

- **Archive** (Long-term retention): Original data MOVED for years (legal/business). Encrypt, restrict, hash, keep readable, test restores.
- **Data disposition** (Keep, migrate or destroy decision): Data owner decides per retention schedule, classification, law. Cover EVERY copy (backups, test, exports, logs).
- **Legal hold** (Do not delete): Lawsuit/investigation: preserve data even past retention; overrides deletion schedules until legal releases it.
- **Storage limitation** (GDPR data minimization): Do not keep personal data longer than needed; keeping just in case is a violation. Right to erasure.

### Destruction

- **Crypto-shredding** (Cryptographic erase): Destroy ALL key copies so encrypted data is unreadable; purge method; ideal for cloud. Fails if any key copy or unencrypted copy remains.
- **Data remanence** (Leftover data): Data that remains after delete/format (only pointers removed).
- **Degaussing** (Magnetic erase): Purge for MAGNETIC media only (HDD, tape); useless on SSD/flash.
- **NIST SP 800-88** (Media sanitization): CLEAR (overwrite; reuse inside org) -> PURGE (degauss, crypto erase, secure erase; leaves org / lab recovery) -> DESTROY (shred, incinerate; most sensitive).

### Don't confuse

- **Backup vs archive** (Recovery copy vs retention): Backup = COPY for RECOVERY, short-term. Archive = ORIGINAL moved for long-term RETENTION.

### Process

- **Dependencies** (Upstream / downstream): Upstream = what depends ON the app; downstream = what the app uses. Identify before shutdown; watch hidden security functions. Scream test = controlled brownout.
- **Sun-setting criteria** (When to retire): Unacceptable risk, EOS/vendor gone, end of warranty, cost, incompatibility (no MFA/TLS), compliance, need ended. Not age alone; not it still works.
- **Sun-setting process** (Retirement steps): Approve -> dependencies -> notify -> disposition -> migrate/archive -> remove access -> shut down -> sanitize -> cancel contracts -> update records (LAST).

### Retirement basics

- **Compensating control** (Alternative safeguard): Used when the normal control (e.g. patching) is not possible: isolation, WAF, restricted access, monitoring.
- **EOL** (End of Life): Product officially finished (not sold/developed). EOL policy = how the org retires software safely; plan from Requirements/Design.
- **EOS** (End of Support): Vendor stops PATCHES (often after EOL). The date that matters for security. Best: upgrade; else compensating controls + extended support + documented risk acceptance with expiry.
- **Orphaned system** (Forgotten, unowned system): Replaced but never shut down: unpatched, unmonitored, often with live connections an attacker can pivot through.

## 2.7 Security reporting

### Improvement

- **Feedback loop** (Lessons go backward): Findings/incidents -> root cause -> requirements, design/threat model, coding rules/SAST, training, bug bar, metrics. Fix the leak, not just the floor.
- **Root cause analysis** (Why it happened): Best answer when the same bug type repeats.

### Reporting

- **Audience tailoring** (Right view for each audience): Board = business risk, trends, decisions (dollars, no CVEs); managers = SLA, what is late, expiring acceptances; developers = file/line/fix in their tools; auditors = evidence.
- **Report sensitivity** (Protect vuln reports): Vulnerability reports list your weaknesses; restrict access.
- **Report vs dashboard** (Point-in-time vs live view): Report = periodic document with explanation; dashboard = refreshed at-a-glance numbers.

### Risk tracking

- **Register vs vuln list vs POA&M** (Don't confuse): Vuln list = raw findings; register = business risks with owners; POA&M = federal per-system weakness fix list.
- **Risk register** (Central risk list): Risk, asset, likelihood/impact, inherent/residual, response, OWNER, action, due date, REVIEW DATE. Living; business owns, security maintains.

## 2.8 Integrated risk management

### Community and models

- **CMMI** (Process maturity): 1 Initial, 2 Managed (project), 3 Defined (org), 4 Quantitatively managed, 5 Optimizing.
- **OCTAVE** (Self-directed risk assessment): Own staff, critical assets, operational risk. OCTAVE-S small; Allegro streamlined info assets.
- **OWASP** (Open community): Top 10 = awareness; ASVS L1/L2/L3 = testable requirements (L3 critical); WSTG; Cheat Sheets.
- **SAFECode** (Vendor consortium): Big software vendors sharing proven secure dev practices.
- **SAMM vs BSIMM** (Prescriptive vs descriptive): SAMM = Should (what to do, roadmap). BSIMM = Benchmark (what others actually do).

### ISO

- **Common Criteria** (ISO/IEC 15408): Certifies ONE PRODUCT. TOE = product evaluated; PP = purchaser wish list; ST = seller claims; EAL 1-7 = confidence (4 most common), not features.
- **ISO 27001** (ISMS requirements): The ONLY certifiable one; PDCA; Annex A 93 controls (organizational, people, physical, technological).
- **ISO 27002 / 27005** (Control guidance / risk management): 27002 explains controls; 27005 = infosec risk how-to. Neither certifiable.
- **Other ISO** (Recognize): 9126 -> 25010 software quality (adds security); 12207 software lifecycle; 15288 system lifecycle; 21827 SSE-CMM; 27000 vocabulary.
- **Statement of Applicability** (SoA): Your document listing which Annex A controls you use/exclude and why.

### Legal

- **Breach notification** (Deadlines): GDPR 72h to regulator from awareness; HIPAA 60 days; SEC 4 business days; encryption safe harbor.
- **Compliance** (Meet rules + prove it): Evidence; point-in-time; compliance is not security. Do more, be secure.
- **IP types** (Copyright, patent, trademark, trade secret): Words; invention (disclosed, ~20 yrs); brand; vault (only while secret).
- **Licensing** (Permissive vs copyleft): MIT/Apache/BSD = give credit; GPL = share alike on distribution; AGPL = network use counts; SCA finds licenses.

### NIST

- **FIPS** (Mandatory federal standards): 140 crypto modules (L2 tamper-evident, L3 tamper-resistant); 197 AES; 180 SHA; 186 signatures; 199 categorize; 200 minimums; 201 PIV.
- **NIST 800-30** (Risk assessment guide): Risk = likelihood x impact. Measure.
- **NIST 800-37 RMF** (Risk Management Framework): Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. AO grants ATO; POA&M tracks fixes.
- **NIST 800-53** (Control catalog): 20 families; 800-53B Low/Mod/High baselines. Menu.
- **NIST CSF 2.0** (Cybersecurity Framework): Voluntary outcomes: Govern (new), Identify, Protect, Detect, Respond, Recover. Profiles (current/target), Tiers 1-4.
- **Other NIST SPs** (Recognize): 12 intro; 34 contingency; 41 firewalls; 61 incidents; 63 digital identity; 64 SDLC (withdrawn); 92 logs; 95 web services; 115 testing; 160 systems engineering.

### PCI

- **PCI DSS** (Card data security standard): Contract not law; any org handling card data. CVV/SAD never stored after auth. Tokenization removes PAN from scope.
- **PCI Secure Software / Secure SLC** (Replaced PA-DSS (2022)): Secure Software = the vendor PRODUCT; Secure SLC = the vendor DEV PROCESS.

### Risk

- **Appetite / tolerance / capacity** (How much risk): Appetite = broad (board); tolerance = measurable limits; capacity = breaking point.
- **Assessment vs analysis** (Whole vs part): Assessment = identify + analyze + evaluate. Analysis = rate likelihood/impact. Treatment = act.
- **Control value** (Cost-benefit): ALE before - ALE after - annual cost. Saving first, then subtract cost.
- **Inherent vs residual** (Before vs after controls): Management accepts RESIDUAL.
- **Qualitative vs quantitative** (Words vs dollars): H/M/L, Delphi vs SLE/ARO/ALE, cost-benefit.
- **Risk responses** (M-A-T-A): Mitigate (add a lock), Accept (signed), Transfer (cost only, not accountability), Avoid (stop the activity). Rejection always wrong.
- **SLE / ALE** (Risk math): SLE = AV x EF; ALE = SLE x ARO (once in 4 yrs = 0.25).
- **Technical vs business risk** (What breaks vs what it costs): Talk to the board in dollars, not CVEs.
- **Threat / vuln / exploit / risk** (Who / hole / how / so what): Hacker = threat; unpatched server = vulnerability; script = exploit; likelihood x impact = risk.

## 2.9 Secure operation practices

### Authorization

- **A&A** (Assessment and Authorization): Assessment (formerly certification) = independent assessor tests -> SAR. Authorization (formerly accreditation) = AO grants ATO/denial. Package: SSP, SAR, POA&M. Reauthorize after major change. Test, then trust.

### Don't confuse

- **Change vs config vs release** (Permit office / blueprints / construction crew): Approve/reject/CAB = change; version on servers/drift/CMDB = configuration; bundle/deploy/version goes out = release.
- **Verification vs validation** (Built it right vs built the right thing): Verification = meets the spec (reviews, SAST, tests, RTM). Validation = meets real user needs (UAT, pilots).

### Incident response

- **CSIRT / tabletop** (Team / practice): CSIRT = incident response team (Preparation). Tabletop = discussion drill of the plan.
- **Event vs incident** (Observable vs harmful): Event = anything observable; incident = harms or threatens security.
- **NIST 800-61 phases** (Incident handling): Preparation -> Detection & Analysis -> Containment, Eradication, Recovery -> Post-incident (lessons learned). Contain FIRST; recovery before eradication reinfects; chain of custody.

### Operations

- **Change management** (Gatekeeper): RFC -> impact (incl. security) -> CAB approval -> test -> implement -> rollback plan ready BEFORE -> document. Standard (pre-approved), normal (CAB), emergency (ECAB fast, documented after, never skipped).
- **Configuration management** (Record keeper): CIs, CMDB, baselines, version control, configuration audits catch drift. What do we have?
- **Release management** (Delivery): Bundle, build, test, deploy approved changes as releases; only approved/tested code; code signing.

### Operations KPIs

- **Compliance KPIs** (Patch / baseline / SLA): % patched within SLA, % matching baseline, % vulns fixed on time, change success rate. Higher is better.
- **MTTD / MTTR** (Detect / respond-recover): Lower is better. MTTD improves Detection & Analysis.

## AI additions (Domain 2)

### AI dev

- **AI coding assistants** (Governance): Same gates as all code + human review; developer accountable; no secrets in prompts; enterprise tools; secret scanning; SCA + allow-lists.
- **Automation bias** (Over-trust): Reviewing AI output less carefully because it looks polished.
- **Hallucinated dependency** (Slopsquatting): AI invents a package name; attacker registers it. Block new/unknown packages until verified.

### AI gates

- **AI build-break criteria** (Bug bar for models): Thresholds for hallucination, bias, accuracy regression, jailbreak resistance, toxicity, leakage; set in Requirements; any failure breaks the build.

### AI pipeline

- **Data poisoning** (Tampered training data): Auto-retraining on user data = risk; validate, clean, gate.
- **MLSecOps** (DevSecOps for ML): Protect data (provenance, validation, poisoning), training (lineage), model (sign/hash, scan third-party), deployment (access, rate limit), monitoring (drift), retraining (gated). ML-BOM.

### LLM Top 10

- **Excessive agency** (LLM06): Agent has too many permissions/acts without approval. Fix = least privilege + human approval.
- **Improper output handling** (LLM05): Trusting LLM output -> XSS/SQLi. Treat output as untrusted input.
- **Other LLM risks** (Recognize): Sensitive info disclosure, supply chain, data/model poisoning, system prompt leakage (no secrets in prompts), vector/embedding (RAG), misinformation, unbounded consumption (rate limits).
- **Prompt injection** (LLM01): Direct = user types it. Indirect = hidden in content the AI reads (email, web page). Who typed it?

### Post-quantum

- **Harvest now, decrypt later** (Why PQC is urgent): Encrypted data stolen today, decrypted when quantum arrives.
- **PQC roadmap** (Steps): Crypto inventory/CBOM FIRST -> prioritize -> crypto agility -> hybrid -> test/migrate -> vendors.
- **PQC standards** (NIST 2024): FIPS 203 ML-KEM (key exchange); 204 ML-DSA (signatures); 205 SLH-DSA (hash signatures).
- **Shor vs Grover** (What quantum breaks): Shor breaks RSA/ECC/DH. Grover weakens AES/hashes -> use AES-256.

## 3.1 Software security requirements

### Continuity

- **MTD vs MTTR** (Don't confuse): MTD = Maximum Tolerable Downtime (a limit). MTTR = mean time to recover (an average measured).
- **RPO / RTO / MTD** (Continuity): RPO = data loss looking back (backup frequency). RTO = time to restore. MTD = max survivable. RTO &lt;= MTD; RTO + WRT &lt;= MTD.

### Finding requirements

- **Elicitation** (Draw out requirements): Brainstorming (unstructured), interviews (deep, slow), surveys (many, shallow), data classification, use/misuse cases, JAD, prototypes.
- **PNE** (Protection needs elicitation): Assets, threats, protection needs WITH stakeholders; brainstorming, surveys (questionnaires + interviews), policy decomposition, data classification, use/misuse cases.

### Other types

- **Configuration parameters** (Secrets handling): No hardcoding; vault; externalized; separate per environment; secure defaults; rotate after leak.
- **Other requirement types** (Six to remember): Sequencing/timing, international (encoding, export controls, local laws), procurement (contract clauses), deployment environment, archiving, anti-piracy.
- **Race condition / TOCTOU** (Sequencing and timing): Two operations collide; check-then-use changes in between. Fix: atomic transactions, timeouts.

### Requirement types

- **Functional** (What it does): Features you can watch happen, incl. security features (MFA, lockout, audit log). Use cases, user stories.
- **Non-functional** (How well): Qualities: security, performance, operational, continuity, deployment. Must be measurable.

### Writing requirements

- **Policy decomposition** (Trunk to leaves): Policy -> objectives -> specific, testable requirements. Pick the MOST SPECIFIC option.
- **Security user story + acceptance criteria** (Agile security reqs): As a..I want..so that + Given/When/Then pass/fail criteria incl. negative cases. Evil/abuser story = attacker view.
- **Subject-object matrix** (Access control matrix): Subjects (who acts) x objects (what is acted on) x CRUD. Every cell = test incl. negative.

## 3.2 Compliance requirements

### Breach notification

- **SB 1386** (First US breach law): California 2003; now all 50 states. Believed-to-be accessed is enough; encryption safe harbor; resident state law applies.

### Challenges

- **Compliance challenges** (Conflict, change, country, vague): Legal decides conflicts; monitor changes; map to common controls / meet the strictest; decompose vague laws into testable requirements with traceability.

### Industry

- **Defense** (ITAR / CMMC): ITAR = export of defense tech/data, US persons only. CMMC = DoD contractor cyber levels 1-3 (NIST 800-171, CUI). Not CMMI.
- **Financial** (SOX / GLBA): SOX = public company financial REPORTING accuracy. GLBA = financial CUSTOMER privacy: Privacy Rule (notice, opt out), Safeguards Rule (written program), pretexting.
- **Healthcare** (HIPAA / HITECH): PHI; Privacy + Security Rules. HITECH: bigger fines, breach notification, business associates directly liable.

### International

- **International** (Recognize): GDPR (2018, replaced 1995 Directive; 20M euro or 4%); UK DPA 2018; UK Computer Misuse Act = UK CFAA; Basel II/III bank capital + operational risk; PIPEDA Canada private sector; data localization.

### Requirement sources

- **Jurisdiction** (Whose rules apply): Follows the people and their data (GDPR applies to a US shop with EU customers; US state breach law of the RESIDENT).
- **Regulatory vs industry vs company** (Who enforces): Regulatory = law, government fines (GDPR, HIPAA, SOX, GLBA, FISMA, CCPA). Industry = contracts (PCI DSS). Company-wide = internal approved tools/standards/frameworks/protocols.

### US laws

- **Duty laws vs CFAA** (Inspector vs cop): Most laws put duties on the company; CFAA punishes the attacker (break-in, former employee logging in).
- **Other US laws** (Recognize): FISMA federal agencies only; COPPA children under 13 parental consent; FERPA student records; CFAA hacking is a crime; DMCA no bypassing copy protection.

## 3.3 Data classification

### Data types

- **PII / PHI / public** (Who you are / health + who / public is not permission): Direct vs indirect identifiers (ZIP+DOB+gender); PHI = health + identifier (HIPAA); public personal data still regulated (GDPR); aggregation risk.
- **Structured vs unstructured** (Spreadsheet vs junk drawer): Structured = tables; unstructured = docs, email, chat, images (hardest; data discovery, DLP). Semi-structured = JSON, XML, logs.

### Labels

- **Commercial labels** (Can People See Public?): Confidential (company secrets) > Private (about people) > Sensitive/Internal > Public. Confidential is LOWEST in government, HIGHEST in commercial.
- **FIPS 199** (Impact labels): Low/Moderate/High for C, I, A; overall = high-water mark (highest).
- **Government labels** (Top Secret Spies Carry Umbrellas): Top Secret = exceptionally grave; Secret = serious; Confidential = damage; Unclassified (CUI).

### Lifecycle

- **Data lifecycle** (Can Someone Use Shared Archived Data?): Create (classify here), Store, Use, Share, Archive, Destroy.
- **Data remanence** (Data's ghost): Deleted files, freed memory, swap, temp/logs/crash dumps, SSDs, cloud snapshots. Clear memory, no secrets in logs/dumps, encrypt, 800-88, every copy.
- **Data states** (Parked / driving / hood open): At rest (AES, full-disk), in transit (TLS), in use (memory; hardest; clear memory, confidential computing).

### Roles

- **Data dictionary** (Data's ID card): Catalog of fields: meaning, format, rules, location, owner, classification, retention. Metadata, not logs. First step to find PII.
- **Owner / custodian / steward** (Data roles): Owner decides (classification, access, accountable, business). Custodian protects (IT: backups, permissions, encryption). Steward perfects (quality, proper use).

## 3.4 Privacy requirements

### Cross-border

- **Residency / sovereignty / localization** (Where it sleeps / whose rules / cannot leave): Sovereignty can follow the controlling company (US CLOUD Act). Transfers: adequacy, SCCs, BCRs, EU-US Data Privacy Framework (2023; Schrems II killed Privacy Shield 2020).

### De-identification

- **De-identification toolbox** (Mask, blur, drop, blend, fuzz): Masking (static/dynamic), generalization, suppression, k-anonymity (k-1 lookalikes; l-diversity fixes), differential privacy (noise, math guarantee).
- **Pseudonymization vs anonymization** (Nickname vs no name ever): Pseudonymized = reversible with separate key, STILL personal data (tokenization). Anonymized = irreversible, GDPR no longer applies. Removing names is not anonymization.

### Marketing

- **Opt-in vs opt-out** (Closed door vs open door): GDPR = active opt-in (no pre-ticked boxes). CAN-SPAM = opt-out + unsubscribe in 10 business days. Sync preferences everywhere; no dark patterns.
- **Third-party sharing** (Disclose, consent, contract): Privacy notice; consent or CCPA Do Not Sell or Share; DPA with processors; share minimal fields.

### Principles

- **Minimization** (Take only what you need): Fewer fields, less precision, less time. Every field needs a reason. Data not collected cannot be breached.
- **Principle vs process** (Don't confuse): Minimization/purpose/PbD = principles; PIA/DPIA = process that checks them.
- **Purpose limitation + consent** (Use it only as promised): No reuse for new purposes without new basis. Consent: freely given, specific, informed, active opt-in, withdrawable. 6 GDPR bases.

### Process

- **PbD + DPIA** (Bake it in, taste-test): Cavoukian 7 principles, privacy by default. DPIA mandatory for high risk (biometrics, monitoring, profiling), BEFORE processing.

### Rights

- **User rights** (See, fix, delete, take, pause, stop): Access (DSAR, 1 month), rectification, erasure (not absolute), portability, restriction, objection (absolute for marketing), automated decisions. VERIFY IDENTITY via what is on file.

### Storage

- **Retention** (Not too short, not too long, every copy): Minimum (legal) and maximum (storage limitation); automatic purge incl. backups; legal hold overrides; record deletion.

## Access, misuse cases, traceability, vendors, AI (3.5-3.AI)

### 3.5 Access

- **Joiner / Mover / Leaver** (User provisioning): Joiner = only what is needed (RBAC); Mover = swap, do not stack; Leaver = cut everything fast (automate from HR). Deprovisioning.
- **Recertification** (Access reviews): Periodic confirmation access is still needed; safety net for JML; rubber-stamping is a weakness. Fixes privilege creep.
- **Service accounts** (Non-human accounts): Least privilege, no interactive login, vault + rotation, named owner.

### 3.6 Misuse

- **Attack tree** (Attacker's family tree): Goal at root, ways as branches; OR = any path, AND = all steps.
- **Misuse vs abuse case** (Oops or evil vs evil only): Misuse = accidental or intentional; abuse = malicious, attacker view. Output = security REQUIREMENT (not a patch).

### 3.7 Traceability

- **Gold plating vs scope creep** (Devs add vs requirements grow): Both = features with no requirement = untested attack surface.
- **SRTM / bidirectional** (Forward vs backward): Forward (req → test) = nothing missing. Backward (feature → req) = nothing extra.

### 3.8 Vendors

- **SOC reports** (Photo vs video): SOC 2 Type I = design at a point; Type II = worked over 6-12 months (stronger). SOC 1 = financial; SOC 3 = public summary. Also ISO 27001, FedRAMP, SIG/CAIQ, attestations.
- **Vendor contracts** (Before signing): Secure SDLC, patch SLA, breach notice to you, right to audit, data handling + DPA, SBOM, flow-down.

### 3.AI

- **AI requirements** (Agency, thresholds, creep, abuse): Least privilege + human approval; numeric hallucination/bias limits; function creep = use beyond approved purpose (DPIA for new use); abuse cases for jailbreak/prompt injection.

## Security architecture (4.1)

### Architectures

- **N-tier / P2P / queues / ESB** (Architectures): Never trust the client. P2P = no central trust. Queues: sign, encrypt, replay protection (timestamp/nonce). ESB = control point + single point of failure.

### Cloud

- **CASB / CSPM / containers** (Cloud security tools): CASB: visibility (shadow IT), compliance, data security, threat protection. CSPM: misconfiguration scanning. Containers share host kernel.
- **Cloud models** (SaaS/PaaS/IaaS; public/private/hybrid/community): Customer responsibility grows to IaaS. Shared responsibility: data, accounts, access always the customer.
- **NIST cloud characteristics** (Our Big Rubber Raft Moves): On-demand self-service, Broad network access, Resource pooling, Rapid elasticity, Measured service (SP 800-145).

### Controls

- **Control categories** (Administrative / technical / physical): Could you kick it? = physical. On a screen = technical. Rule/document = administrative.
- **Control types** (Deter, prevent, detect, correct, recover, compensate): Can they still get in? Yes = deterrent; no = preventive. Corrective fixes damage; recovery restores operations.

### Devices

- **IoT / embedded** (Devices): RFID read from distance; NFC near. Default passwords (Mirai); segmentation; secure boot; signed updates.

### Frameworks

- **SABSA / Zachman / TOGAF** (Frameworks): SABSA = business-driven security architecture, 6 layers. Zachman = grid of What/How/Where/Who/When/Why. TOGAF = enterprise method with ADM cycle.

### Hardware

- **Firmware / secure element** (Below the OS): Firmware rootkits survive OS reinstall; secure boot, signed updates. Secure element/TPM/HSM keep keys inside.
- **Side channels + speculative execution** (Listening through the wall): Timing, power, EM (TEMPEST), cache; constant-time code. Meltdown = apps vs kernel; Spectre = all CPUs, hard to fix; microcode + OS patches.

### Legacy

- **Mainframe / middleware / WSDL** (Legacy + integration): ESM = RACF; middleware sees everything; SOAP = letter, WSDL = manual, UDDI = phone book; XXE.

### Mobile

- **Mobile** (MASVS, pinning, keystore, BYOD): Keystore for tokens; certificate pinning; MASVS; MDM (remote wipe); containerization = selective wipe; location = sensitive, opt-in.

### OT

- **OT / ICS** (SCADA = control room, PLC = hand on one machine): Availability + safety first; segmentation, compensating controls; Modbus no auth; Stuxnet.

### Web

- **SOAP vs REST, mTLS** (Web services): SOAP = message-level (WS-Security); REST = TLS + OAuth/JWT. mTLS = both sides show certificates.
- **XSS vs CSRF, SOP, CORS** (Browser attacks): XSS = their script on your page. CSRF = your browser, their request. SOP = wall, CORS = gate (* = misconfig).

### Wireless

- **Wi-Fi + Bluetooth** (WEP &lt; WPA &lt; WPA2 &lt; WPA3): WEP broken. Bluejacking = joke (messages), bluesnarfing = snatch (data), bluebugging = boss (control).

## Secure interface design (4.2)

### API

- **BOLA / IDOR** (#1 OWASP API Top 10): Logged in is not allowed-to-see-this; object-level authorization on every call. Also excessive data exposure, rate limits, zombie APIs.
- **Secure messaging** (Encrypt / sign / nonce): Encrypt = cannot read; sign = cannot fake (signature = nonrepudiation, HMAC = no); nonce/timestamp = cannot reuse; message-level survives every hop.
- **Sessions vs tokens** (Coat ticket vs ID card): Cookies Secure/HttpOnly/SameSite; new session ID at login (fixation); JWT: verify signature, reject alg none, short expiry, signed not encrypted, hard to revoke.

### Browser

- **Origin / SOP / CORS** (Scheme + host + port): All three must match; SOP blocks reading; CORS lists exceptions; * on private data or reflecting origin = misconfig.

### Interfaces

- **Admin interfaces** (Master key room): MFA, network-restricted (no public internet), least privilege, PAM (vault, just-in-time, session recording), log every admin action.
- **Log interfaces** (Camera footage): TLS to SIEM fast; append-only/WORM; admins cannot delete (separation of duties); no secrets; log injection; NTP.
- **Out-of-band management** (Staff-only corridor): Separate management channel (network, console, iDRAC/iLO); works during DDoS; must itself be secured.
- **Upstream/downstream** (Separate keys per connection): No shared master key; vault + rotate; minimize data; validate upstream; mTLS.

## Reusable technologies (4.3)

### Backups

- **Backups** (Book / page / bookmark): Full fastest restore; incremental fastest backup, chain restore; differential = full + latest. 3-2-1(-1-0); offline/immutable vs ransomware; test restores.

### Databases

- **Databases** (Puzzle / detective / cover story): Parameterized queries, least-privilege DB user, TDE, DAM. Aggregation = collect; inference = deduce; polyinstantiation = cover story (denial leaks).

### Identity

- **LDAP + credentials** (Phone book; 389 plain, 636 protected): Anonymous bind, LDAP injection, cleartext simple bind. NIST 800-63B, breached lists, no forced changes, MFA, credential stuffing, FIDO2/passkeys.

### Network

- **DLP** (Librarian / exit guard / watching hands): At rest = discover; in motion = network; in use = endpoint (USB, copy). Blind to encrypted traffic.
- **Firewalls** (Envelope / conversation / letter): Stateless packet filter, stateful (state table), application-level proxy, NGFW, WAF (virtual patching, not a fix).
- **Proxies** (Forward = users out; reverse = servers in): Reverse proxy hides servers, terminates TLS, hosts WAF.

### PKI

- **CRL / OCSP / stapling** (List / phone call / fresh letter): Revocation checks; OCSP may fail open; DV &lt; OV &lt; EV.
- **PKI roles** (CA = passport office, RA = clerk): RA verifies, CA signs; root CA offline in HSM; intermediates issue; chain of trust to trust store.
- **X.509 certificate** (ID card for a public key): Subject, issuer, PUBLIC key (never private), serial, validity, SAN, key usage, basic constraints. CSR to request.

### Runtimes

- **DAC vs MAC** (Owner decides vs must follow the law): SELinux (NSA, labels) and AppArmor (path profiles) enforce MAC; contains compromise.
- **Managed vs unmanaged** (Memory babysitter): Unmanaged C/C++: ASLR, DEP/NX, stack canaries; memory-safe languages; CAS = permissions by code origin; type safety.

### Trusted computing

- **Trusted computing** (Bank picture): TPM (EK, SRK, PCRs, measured boot, sealed storage, attestation); TCB + security perimeter; reference monitor NEAT; security kernel; rings 0 king / 3 citizens.

### Virtualization

- **Hypervisors + virtualization** (Type 1 foundation, Type 2 renting a room): VM escape, VM sprawl, snapshots hold memory, inter-VM blind spots, noisy neighbor. Containers share kernel.
- **IaC** (Restore from code): Templates reviewed + scanned (policy as code); drift → re-apply template; immutable infrastructure.

## Threat modeling (4.4)

### Methods

- **hTMM / VAST / Trike** (Other methods): hTMM (SEI) = Security Cards + PnG + STRIDE; VAST = scalable agile; Trike = requirements model.
- **PASTA** (7 stages, risk-centric): Do Dogs Always Think Very Angry Rabbits: objectives, scope, decomposition, threats, vulnerabilities, attack modeling, risk/impact.
- **STRIDE** (Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation): Authn, integrity, nonrepudiation, confidentiality, availability, authorization. Process = all; store/flow = TIDe; entity = SiR.

### Process

- **DFD shapes** (Rectangle, circle, parallel lines, arrow, dashed line): External entity, process, data store, data flow, trust boundary. Threats cluster at trust boundary crossings. Level 0 = context.
- **Entry / exit / privileged** (Doors in, doors out, power buttons): Entry = forms, APIs, uploads; exit = errors, logs (info disclosure); privileged = admin, password reset.
- **Threat modeling steps** (Shostack's 4 questions): Objectives → decompose (DFD) → identify (STRIDE) → rank (DREAD/CVSS) → mitigate → validate; design phase; living document.

### Ranking

- **CVSS** (Base, temporal/threat, environmental): FIRST; 0–10: Low &lt;4, Medium 4–6.9, High 7–8.9, Critical 9+. Environmental = your asset criticality.
- **DREAD** (Damage, Reproducibility, Exploitability, Affected users, Discoverability): Average 1–10; subjective; discoverability = obscurity.

### Threats

- **Attack surface + RASQ** (Brick up unused doors): Reduce: disable services/ports, remove debug/test, least privilege. RASQ = relative, lower = smaller.
- **Catalogs** (CWE / CVE / CAPEC / ATT&CK): Weakness type / specific bug / attack pattern / attacker playbook.
- **Threat intel + agents** (STIX message, TAXII taxi): Strategic, tactical (TTPs), operational, technical (IOCs). Agents: script kiddies, hacktivists, crime, nation-state/APT, insiders (often negligent), competitors.

## Security models and properties (4.6)

### Concepts

- **Covert channels** (Morse code through the wall): Timing (CPU busy/idle) vs storage (disk fill/empty).
- **Non-functional trade-offs** (People climb out the window): Security vs speed/usability/cost; too heavy = workarounds (shadow IT).
- **State machine / info flow / noninterference / lattice** (Building blocks): Every transition secure (traffic light); where data may move (pipes); high invisible to low; ordered levels.
- **Trusted path vs secure state** (Hotline vs self-locking building): Ctrl+Alt+Del = trusted path; fail into a safe condition = secure state.

### Models

- **2-step method** (Direction + why): Up/down + read/write; leak secrets = BLP, pollute data = Biba.
- **Bell-LaPadula** (Lips sealed (confidentiality)): No read up, no write down. Military secrets.
- **Biba** (Clean water (integrity)): No read down, no write up. Mirror of BLP.
- **Brewer-Nash** (Chinese Wall): Conflict of interest; access depends on what you have seen.
- **Clark-Wilson** (Business integrity): Approved programs (well-formed transactions) + separation of duties.
- **Graham-Denning / HRU / Take-Grant** (Permission management): Creating, granting, transferring, removing rights.

## Secure coding practices (5.1)

### Access

- **Access control + trust** (DAC Decision, MAC Must, RBAC Role, ABAC Attributes): Declarative vs imperative; NDAC, resource-based, role hierarchies, static vs dynamic SoD; trusted subsystem / impersonation / delegation; function-level authz.
- **Hardware + privilege** (SKPP = thick walls; sandbox = playpen): SGX, SEV/TDX, TrustZone, NX, CET; privilege separation, drop privileges, secure startup.

### Attacks

- **Side channels + spoofing** (SPA one trace, DPA many; SPF guest list, DKIM key in mail, DMARC manager): Timing, power, EM, acoustic, cache, fault injection; IP/email/ARP/DNS spoofing (DNSSEC).

### Crypto

- **Algorithms + TLS** (GCM = Gets Confidentiality + Message integrity; ECB = Every Copy Betrays): AES-GCM/ChaCha20, RSA 2048+/ECC, SHA-256+; retire DES, 3DES, RC4, MD5, SHA-1; TLS 1.2/1.3, ECDHE, cert validation, HSTS.
- **DB encryption + scope** (TDE locks the cabinet, not the drawer): TDE = at rest only; field/app-level or tokenization vs SQLi; full-disk protects only powered-off devices.
- **DH, envelope, keys, cryptanalysis** (Crowded-room secret; fast box + sealed envelope): DH needs authentication; ECDHE forward secrecy; n(n-1)/2 symmetric keys; ciphertext-only → known → chosen-plaintext → chosen-ciphertext; birthday, downgrade.
- **Password storage + attacks** (Rainbow table = cheat sheet; salt changes the question): Argon2id/bcrypt/scrypt/PBKDF2 + unique salt (+ secret pepper); online vs offline attacks.
- **Protecting data compared** (Encoding is a costume, not a lock): Encryption, hashing, tokenization, masking, anonymization, pseudonymization, redaction; stego hides existence, watermark traces owner.
- **Salt / IV / nonce / pepper** (Salt seasons, IV varies, nonce once, pepper secret): Salt + IV not secret; nonce reuse in GCM catastrophic.

### Input/output

- **Errors, logging, redirects, files, deserialization** (Generic to user, details to logs): Fail secure; no secrets in logs; allow-list redirects; traversal/upload/zip slip; never deserialize untrusted data.
- **Input + output** (Validate IN, encode OUT): Server-side allow-list; canonicalize THEN validate; parameterized queries; context-aware output encoding.
- **Other injection** (Data and commands never share a seat): OS command (safe API, separate args), LDAP, XPath, XXE (disable external entities), NoSQL, SSTI, CRLF, log injection.

### Memory

- **Concurrency + resources + randomness** (Deadlock = narrow hallway; Math.random() = predictable coin): Locks, atomic ops, lock order + timeouts; ACID, serializable, optimistic vs pessimistic; release resources, ReDoS; CSPRNG.
- **Memory + languages** (2 liters into a 1-liter glass): Stack vs heap overflow; use-after-free; safe functions, canaries, ASLR, DEP, CET; compiled vs interpreted vs hybrid (decompile → obfuscate).

### Web

- **CSRF / IDOR / SSRF / clickjacking** (Your browser their request / is this yours? / server makes the call / invisible frame): Anti-CSRF tokens + SameSite; object-level authz; allow-list destinations, block 169.254.169.254; X-Frame-Options / frame-ancestors.
- **Sessions + cookies** (New ID at login): Random IDs, idle + absolute timeouts, server-side logout; Secure, HttpOnly, SameSite. Spraying = one password, many accounts.
- **XSS types** (Stored = Saved; reflected = mirror; DOM = browser only): Output encoding (main), CSP, HttpOnly. Where does the script live?

## Domain 5 beyond 5.1 (5.2–5.6, 5.AI)

### 5.2

- **Coverage, linting, malicious code, SAMATE** (Logic bomb = IF, time bomb = WHEN; SAMATE tests the testers): Coverage ≠ secure; backdoors, hidden accounts, high-entropy strings; NIST SAMATE + SARD (Juliet).
- **CWE vs CVE / Top 25** (CWE = disease, CVE = patient): CWE-89 type vs CVE-2021-44228 instance; CWE/SANS Top 25 = most dangerous weaknesses.
- **OWASP Top 10 (2021)** (A01 Broken Access Control is #1): A01 access control, A02 crypto failures, A03 injection (incl. XSS), A04 insecure design, A05 misconfiguration, A06 vulnerable components, A07 auth failures, A08 integrity failures, A09 logging failures, A10 SSRF. Awareness list; ASVS is the standard.
- **SAST / SCA / manual review** (SAST = your code, SCA = borrowed code, humans = logic): SAST exact line, false positives, no runtime; SCA CVEs + licenses + SBOM + reachability; manual review catches logic flaws and logic bombs.

### 5.3

- **Runtime controls** (Watchdog = dead man's switch; signature AV = wanted poster): Watchdogs restart hung processes (log restarts); FIM baseline hashes (Tripwire, PCI DSS); signature vs behavior-based AV, EDR, application allow-listing.

### 5.4

- **Risk strategy + exceptions** (Exception = permission slip with expiry, signed by owner): Mitigate/transfer/avoid/accept; prioritize by business impact; compensating controls; time-bound, owner-approved, risk register.

### 5.5

- **Components** (Trust contract = handshake written down): Systems-of-systems: risk at connections, validate every boundary; design by contract; dependency confusion (scoped names, private feed, pinning) vs typosquatting vs slopsquatting.

### 5.6

- **Build security** (/GS Guard the Stack, /DYNAMICBASE, /NXCOMPAT): Code signing + timestamping (HSM keys; signed ≠ safe); compiler switches + warnings as errors; reproducible builds = same cake; anti-reversing, packing, anti-debugging; DRM, node-locking, DMCA.

### 5.AI

- **AI in coding** (AI agent = intern with superpowers): Direct vs indirect prompt injection (LLM01); sanitize inputs, retrieved content = data; provenance + review of AI code; constrain agents: least privilege, allow-lists, human approval, kill switch (excessive agency LLM06).

## Secure Software Testing (Domain 6)

### 6.1

- **Box testing** (White = lights on, black = no map, gray = visitor's guide): White-box thorough but NOT the attacker view; black-box realistic; gray-box authenticated.
- **FHM + MOM** (Suspect, test, find accomplices, lock up; remove one of motive/opportunity/means): Gather info → hypothesize → confirm → generalize → eliminate.
- **Functional vs non-functional** (Does the lock work vs does it hold when everyone pushes): Security function testing ≠ security testing (lock vs every window).
- **Process** (QA = recipe, QC = tasting; strategy = how, plan = what/when/who): STLC with entry/exit criteria; UAT/OAT; test env mirrors prod, isolated; driver = fake boss, stub = fake helper.
- **Standards** (29119 rulebook · OSSTMM measuring tape · 800-115 review/find/validate): SEI = CERT; WSTG = how-to guide; ASVS = checklist L1–L3 (L2 for most apps).
- **VDP vs bug bounty** (Front door vs door + cash): Safe harbor, coordinated disclosure (~90 days), security.txt; ISO 29147 disclosure / 30111 handling.

### 6.2

- **Crypto validation + coverage** (FIPS: correct → tamper-evident → tamper-resistant → survives anything): CMVP modules, CAVP algorithms, KATs; statement &lt; branch &lt; condition &lt; MC/DC &lt; path.
- **Fuzzing** (Mutation scribbles on a real letter; generation writes new letters from the grammar): Generation = deeper but more setup; coverage-guided (AFL).
- **Resilience tests** (Load = rush hour, stress = stampede, break = bridge collapses; Chaos Monkey): Fault injection = technique (verifies fail secure); synthetic transactions = mystery shopper.
- **Scan vs pen test** (Finds unlocked doors vs walks through them): Phases: permission/RoE → recon → scan → exploit → post-exploit (lateral movement) → report/cleanup.
- **Scanning + teams** (Horizontal = neighbor's apartment, vertical = penthouse; red attacks, blue defends, purple mixes): Passive fingerprinting sends nothing; banner grabbing; credentialed scans; Wireshark, Metasploit, Ghidra.
- **Test design** (Equivalence = one per bucket; boundary = the edges (17, 18, 65, 66)): Regression (security regression per fixed bug), integration (top-down stubs, bottom-up drivers), continuous, misuse/abuse cases.
- **Tools compared** (SAST reads, DAST pokes, IAST watches inside, SCA checks ingredients): IAST tests in QA; RASP protects in prod.

### 6.3–6.4

- **Docs + hidden features** (Maintenance hook = forgotten staff entrance): Generic errors (account enumeration); find via code review, backward traceability, attack surface validation.

### 6.5–6.6

- **Results + defects** (False negative = silent burglar; severity = how bad, priority = how soon): Break/build criteria; error → defect → failure → vulnerability; bug = building, flaw = blueprint; verify before close.

### 6.7

- **Test data** (Static = blurred photocopy, dynamic = live screen that blurs): Synthetic first; prod data only sanitized + approved; aggregation → k-anonymity.

### 6.8

- **V&V** (Verification = blueprint, validation = customer need; acceptance = signature on the delivery note): IV&V (technical/managerial/financial independence); completion criteria; FIPS 140, Common Criteria EAL post-release.

### 6.AI

- **AI testing** (Poisoning = textbook, evasion = exam trick; Go Make More Money): Bias, drift, toxicity; mutation testing for AI tests; agent scope testing; token limits; AI RMF Govern/Map/Measure/Manage.

## Secure Deployment, Operations, Maintenance (Domain 7)

### 7.1

- **Operational risk + cutover** (Big bang jump, parallel = old bridge open, pilot = test kitchen, canary = warning bird): Env separation (no dev prod access), role training, legal compliance, integration risk (dedicated least-privileged accounts), acceptance sign-off.

### 7.11

- **Runtime protection** (WAF = gate guard, RASP = bodyguard in the room): ASLR shuffles rooms; DEP/NX no running in data rooms.

### 7.12

- **Continuity** (DRP = fix computers, BCP = keep shop open; hot/warm/cold; read → talk → act → alongside → pull the plug): BIA first; RPO how far back, RTO how fast, MTD breaking point; MTBF high, MTTR low; erasure coding.

### 7.13

- **Service levels** (SLI speedometer, SLO target, SLA limit with a fine): 99.9% ≈ 8.8 h/yr, 99.99% ≈ 53 min, 99.999% ≈ 5 min; SLO stricter than SLA.

### 7.2

- **Config + version control** (Baseline = recipe; fix the kitchen; CMDB = family tree; version control = time machine with fingerprints): Inventory (CIS 1), CIS Benchmarks/DISA STIGs, drift → restore, branch protection, signed commits, re-engineering preserves controls.

### 7.3

- **Release** (Protect the road, inspect trucks, check the seal, lock the warehouse): Ephemeral least-privilege runners, OIDC short-lived creds, toolchain gates, signed artifacts + admission control, immutable repo, release = ship it.

### 7.4

- **Keys + secrets** (Born, shipped, stored, used, renewed, backed up, retired, destroyed; HSM = vault room, KMS = safe-deposit service): Vaults, dynamic secrets, NIST 800-57, BYOK/HYOK, ACME cert automation, key escrow M-of-N.

### 7.5

- **Installation** (MSB = must be this secure to ride production): Secure boot chain of trust, least-privilege install, hardening, secure provisioning (golden images), secure defaults.

### 7.6

- **Approval to operate** (ATO = license, sign-off = signature, POA&M = repair list): AO accepts residual risk; SSP + SAR + POA&M; ATO/IATO/DATO; reauthorize on major change.

### 7.7

- **Monitoring** (IDS = smoke alarm, IPS = sprinkler; SIEM spots, SOAR handles): ISCM 800-137 six steps; logs/metrics/traces; HIDS vs NIDS; honeypot vs honeytoken; MTTD/MTTR.

### 7.8

- **Incident response** (Collect what's in the air before what's on paper; incident = fire, problem = why fires start): 800-61 phases; event → alert → incident; chain of custody; contain → eradicate → recover; 5 whys/fishbone; tabletop → full-scale.

### 7.9–7.10

- **Patches + vulns** (CVE = name tag, NVD = folder): Identify → assess → test → approve → deploy → verify + rollback; emergency still documented; CVSS + KEV + EPSS + asset value; SLAs.

### 7.AI

- **AI in operations** (EU AI Act: banned, strictly controlled, transparent, free): AIOps with human oversight; data vs concept drift; sandboxed model staging; AI code copyright + license contamination.
