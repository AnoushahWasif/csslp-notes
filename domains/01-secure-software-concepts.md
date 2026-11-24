# Domain 1: Secure Software Concepts

Exam weight: 12%

## 1.1 Core concepts

<a name="t-1-1-1"></a>
**Confidentiality**

Preventing unauthorized disclosure. Controls: encryption, masking, access control.

<a name="t-1-1-2"></a>
**Symmetric vs asymmetric encryption**

Symmetric uses one shared key and is fast (AES). Asymmetric uses a public/private key pair (RSA, ECC) for key exchange and signatures.

<a name="t-1-1-3"></a>
**Integrity**

Assurance that data and code are not altered without authorization.

<a name="t-1-1-4"></a>
**Hashing**

One-way, fixed-length digest (SHA-256) that reveals any change. Passwords get salted, slow hashes.

<a name="t-1-1-5"></a>
**Digital signatures**

A hash signed with the sender's private key. Gives integrity, authenticity and nonrepudiation, not confidentiality.

<a name="t-1-1-6"></a>
**Code signing**

Signing binaries so users can verify the publisher and that code wasn't tampered with.

<a name="t-1-1-7"></a>
**Reliability**

Software works as intended under expected conditions. ISC2 treats it as part of integrity.

<a name="t-1-1-8"></a>
**Authenticity**

Proof that data or code really comes from the claimed source.

<a name="t-1-1-9"></a>
**Availability**

Timely, reliable access for authorized users.

<a name="t-1-1-10"></a>
**Redundancy, replication, clustering**

Duplicate components or data so one failure doesn't stop service. Clusters can be active-active or active-passive.

<a name="t-1-1-11"></a>
**Scalability**

Handling growth: vertical (bigger machine) or horizontal (more machines).

<a name="t-1-1-12"></a>
**Resiliency**

Withstanding and recovering from faults and attacks.

> On the exam: Goes beyond availability: the system keeps working in a degraded state during an attack or failure, then recovers. Scenario cue: 'keeps operating even when a component fails' points to resiliency.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Resiliency is software's ability to keep working when things go wrong (attacks, errors, bad input, failed components) and to recover quickly. It may run in a reduced (degraded) mode, but it doesn't collapse.

ISC2's three qualities of secure software:

- **Reliable:** works correctly under normal conditions
- **Resilient:** withstands abnormal conditions and attacks
- **Recoverable:** returns to normal after failure

**Don't confuse**

- **Availability:** up and reachable when needed
- **Reliability:** correct results under expected conditions
- **Resiliency:** survives unexpected conditions and keeps going
- **Redundancy:** a technique (spare servers, copies) used to achieve resiliency, not the goal itself

**How developers build it**

- Input validation and error handling so bad input can't crash the app
- Graceful degradation: one feature fails, the rest keeps working
- Timeouts, retries, circuit breakers
- Isolation so one component can't bring down others
- Rate limiting and throttling against DoS
- Redundancy, failover, no single point of failure
- Backups and tested recovery; fault injection and chaos testing to prove it

**Example**

Payment provider goes down. Not resilient: whole site crashes. Resilient: browsing works, checkout says payment is temporarily unavailable, orders are saved and retried, site recovers automatically.

**On the exam**

- 'Continues to operate during attack or failure' or 'degrades gracefully' → resiliency
- **Trap:** staying up must never mean failing open. If login is down, deny logins; never let everyone in.
- **Trap:** adding servers doesn't fix an app that crashes on bad input. Resiliency starts in the code.

**Quick check:** Under heavy load, an app disables 'recommended products' but keeps search and checkout running. Which concept?

**Answer:** **Graceful degradation**, a key technique for resiliency. Pick 'graceful degradation' if it's an option; otherwise resiliency.

</details>

<a name="t-1-1-13"></a>
**Authentication**

Verifying identity using something you know, have, or are (plus location/behavior).

> On the exam: Always happens before authorization. If the system can't confirm who someone is, it's an authentication problem; if it can't limit what they do, it's authorization.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Verifying that someone (or something) really is who they claim to be: 'prove it'.

**Factors**

- Something you **know**: password, PIN
- Something you **have**: phone, token, smart card, certificate
- Something you **are**: fingerprint, face, iris
- Extras: somewhere you are, something you do

**Not just users**

Services authenticate to APIs (tokens, keys, mutual TLS), apps to databases (service accounts), servers to clients (TLS certificates).

**Building it securely**

- Authenticate on the **server**; client checks can be bypassed
- Salted slow hashes (bcrypt, Argon2); never plaintext or reversible encryption
- TLS for credentials in transit
- Rate limiting, lockout, CAPTCHA against guessing
- Generic error messages
- Secure side doors: password reset, remember-me, recovery
- Reuse a proven identity provider instead of building your own
- **Re-authenticate before sensitive actions** (change password, email, payment)

**Example**

Strong login + MFA, but 'forgot password' only asks for date of birth. Attackers use the weak recovery path. Authentication is only as strong as its weakest path.

**On the exam**

- Pretending to be someone else → spoofing → threatens authentication (S in STRIDE)
- API accepts requests from anyone → missing service authentication
- **Trap:** authentication = who you are; authorization = what you may do
- **Trap:** best answer usually adds a different factor type (MFA), not a longer password

**Telling them apart**

- 'Is this really the person?' → authentication
- 'Is this person allowed to do it?' → authorization

**Quick check:** Strong login, but users can change their account email with no further checks; an attacker with a stolen session cookie takes over accounts. What control was missing?

**Answer:** **Re-authentication (step-up authentication)** before sensitive actions. Not authorization: the owner IS allowed to change their email; the app never confirmed it was really the owner.

</details>

<a name="t-1-1-14"></a>
**Multi-factor authentication (MFA)**

Two or more different factor types. Two passwords is not MFA.

> On the exam: Factors must be different types. Password + PIN is still one factor (both knowledge); password + code from a phone is MFA. Best answer when a scenario involves stolen or phished passwords.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Requiring two or more **different types** of factors (know / have / are).

**The rule the exam tests**

- Password + security question = ONE factor (both know) ❌
- Password + PIN = ONE factor ❌
- Password + phone code = TWO (know + have) ✅
- Smart card + PIN = TWO (have + know) ✅
- Fingerprint + password = TWO (are + know) ✅

**Why it matters**

Passwords get phished, guessed, reused and leaked. With MFA a stolen password alone isn't enough. Best answer for phishing, credential theft and credential stuffing.

**Strongest to weakest second factors**

- **FIDO2 hardware keys / passkeys:** phishing-resistant
- Authenticator app codes (TOTP) and push (risk: MFA fatigue)
- SMS codes: weakest (SIM swapping, interception)

**Building it in**

- Require for admins, remote access, sensitive actions
- Step-up MFA before risky actions
- Secure enrollment and recovery (recovery must be as strong as MFA)
- Risk-based (adaptive) MFA for unusual logins
- Rate-limit and expire codes

**On the exam**

- Phishing / stolen / reused passwords → MFA
- Most phishing-resistant → FIDO2 / passkeys
- **Trap:** two items from the same category isn't MFA
- **Trap:** strong MFA + weak recovery is still weak

**Quick check:** Password, then mother's maiden name. Is this MFA?

**Answer:** **No.** Both are something you know, so it's single-factor. Security questions are often guessable from social media; as a 'fix' they're usually a distractor.

</details>

<a name="t-1-1-15"></a>
**Identity and access management (IAM)**

Managing the identity lifecycle: creation, roles, changes, removal.

> On the exam: Covers the whole account lifecycle. Accounts left active after someone leaves (orphaned accounts) are an IAM failure in deprovisioning.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Processes and tools managing digital identities and access across their **whole lifecycle**.

**The lifecycle**

- **Joiner (provisioning):** create account with only the access the role needs
- **Mover (change):** add new access AND remove old
- **Review:** periodically confirm access is still needed (recertification)
- **Leaver (deprovisioning):** disable everything immediately

**What goes wrong**

- Joiner: copying a colleague's access → too much from day one
- Mover: old access kept → **privilege creep**
- Leaver: accounts left active → **orphaned accounts** (top audit finding)
- No reviews → nobody notices

**Non-human identities**

Service accounts, API keys, bots: need owners, least privilege, rotated credentials, no interactive login.

**Building blocks**

- Directory (AD, LDAP)
- Authentication services (SSO, MFA, IdP)
- Authorization models (RBAC, ABAC)
- Privileged access management (PAM): checkout passwords, session recording, just-in-time access
- Automation driven by HR records

**For software**

Apps should use central IAM, not their own user lists, or offboarding misses them.

**On the exam**

- Former employee still logs in → leaver failure
- Moved departments, kept old access → privilege creep (mover failure)
- Detect unneeded access → access reviews
- **Trap:** best fix for orphaned accounts is automated HR-driven deprovisioning, not 'audit more'

**Quick check:** A custom app keeps its own user/password list separate from the directory. What's the risk and the better design?

**Answer:** Risk: **orphaned accounts** when people leave (disabled in the directory, still active in the app), plus separate passwords and weaker policies. Better: use central **SSO via the IdP (SAML/OIDC)** and read **roles from directory groups** at login.

</details>

<a name="t-1-1-16"></a>
**Single sign-on (SSO)**

One login for many systems. Convenient, but one stolen credential opens everything.

> On the exam: Improves usability and cuts password reuse, but the identity provider becomes a single point of failure and a high-value target, so protect it with MFA and monitoring.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Log in once to a central identity provider, then access many apps without logging in again.

**How it works**

- Open an app (service provider)
- App redirects to the **identity provider (IdP)**
- Authenticate once (ideally with MFA)
- IdP sends a **signed token/assertion** ('this is Ali, in these groups')
- App validates and trusts it; other apps reuse the session

**Benefits**

- Fewer passwords → less reuse and help desk resets (psychological acceptability)
- Central MFA and policy; **disable once, cut off all apps**
- Apps never handle passwords (economy of mechanism, component reuse)
- Central login logging

**Risks**

- **Single point of compromise:** one stolen login opens everything → MFA on the IdP
- **Single point of failure:** IdP down = nobody logs in → redundancy
- **Token validation:** check signature, expiry, audience
- Session length on shared machines → timeouts, single logout

**SSO vs federation**

SSO: one login, many apps, usually one org. Federation: trust across organizations.

**On the exam**

- Too many passwords, reuse → SSO
- One phished SSO login opened ten apps → add MFA on the IdP
- App accepts unsigned tokens → broken token validation
- **Trap:** keep SSO and add MFA, don't drop SSO

**Quick check:** Company adopts SSO for 30 apps. Most important control on the IdP?

**Answer:** **MFA.** A stolen SSO password alone can no longer unlock all 30 apps. (Password reuse on outside sites without MFA is a separate problem.)

</details>

<a name="t-1-1-17"></a>
**Federated identity**

Trusting identities across organizations. SAML, OAuth 2.0 (authorization), OpenID Connect (authentication on top of OAuth).

> On the exam: Trap: plain OAuth 2.0 is for authorization (delegated access), not proving identity. For authentication pick SAML or OpenID Connect. SAML = XML assertions, typical in enterprise web SSO.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

One organization trusts identities verified by **another organization**. Log in with an identity you already have.

Examples: 'Sign in with Google', company account into a partner portal, university logins across universities.

**Roles**

- **Identity provider (IdP):** verifies you, issues proof
- **Service provider / relying party:** app that trusts the proof
- **Trust relationship:** set up in advance (metadata, signing certificates)

**The three protocols**

- **SAML 2.0:** XML assertions; enterprise web SSO and federation; **authentication**
- **OAuth 2.0:** **authorization** / delegated access ('let this app read my calendar') without sharing your password; access tokens; doesn't prove identity
- **OpenID Connect (OIDC):** identity layer on top of OAuth 2.0; adds an **ID token** (JWT); **authentication** for modern web/mobile

Memory trick: OAuth = Authori**z**ation; OIDC = **ID**entity; SAML = older XML enterprise authentication.

**Benefits**

No extra passwords; home org keeps control (disable once, partner access ends); partners never see passwords.

**Risks and controls**

- IdP trusted completely → choose carefully, MFA
- Validate token **signature, issuer, audience, expiry**
- Share only needed attributes
- Account linking by unverified email → takeover risk
- OAuth **scopes**: request the minimum; users can revoke

**On the exam**

- Third-party app needs access without the password → **OAuth 2.0**
- Modern app authenticates users via external provider → **OIDC**
- Enterprise XML SSO between companies → **SAML**
- **Trap:** 'which is for authentication?' → not plain OAuth
- SSO = within an org; federation = across orgs

**Quick check:** A fitness app wants to post workout summaries to the user's social media. Which protocol, and what should it avoid asking for?

**Answer:** **OAuth 2.0** (delegated authorization). It must **never ask for the user's social media password**; the user approves access and the app gets a limited token. It should also request only the minimum **scope** (post updates, not read messages or contacts).

</details>

<a name="t-1-1-18"></a>
**Biometrics**

FRR / Type I = rejecting a valid user. FAR / Type II = accepting an impostor (worse). CER/EER is where they're equal; lower is better.

> On the exam: For high-security systems, keep FAR low (keep impostors out) even if FRR rises. To compare two devices, pick the one with the lower CER.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Authentication with something you are, measured by a sensor.

**How it works**

- **Enrollment:** trait saved as a **template** (math summary, not the image)
- **Verification:** new scan compared to template using a **threshold** for 'close enough'

**The error rates**

- **FRR = Type I:** legitimate user rejected (annoying, not a breach)
- **FAR = Type II:** impostor accepted (security breach, more dangerous)
- **CER / EER:** setting where FAR = FRR

Memory trick: **R**ejection is **Type I**; **A**cceptance of an **A**ttacker is **Type II**.

**Tuning the threshold**

- Stricter → FAR down, FRR up
- Looser → FRR down, FAR up

You can't minimize both; it depends on what you protect.

**On the exam**

- Compare devices → **lower CER** is more accurate
- High-security area → tune for **low FAR**, accept more false rejections
- Consumer convenience → lower FRR, combine with another factor
- **Trap:** don't guess from the acronym; FAR = impostor accepted

**Quick check:** Server room fingerprint scanners often reject employees. Which rate is high, which type, and should you loosen the threshold?

**Answer:** **FRR, Type I.** Don't loosen it: a server room needs low FAR. Ease usability with better sensors, re-enrollment, or a card as a backup factor.

</details>

<a name="t-1-1-19"></a>
**Authorization**

Deciding what an authenticated subject may do: access controls, permissions, entitlements.

> On the exam: Must be checked server-side on every request. Users reaching other users' records by changing an ID in the URL (IDOR) is an authorization failure, OWASP's number one risk.

<a name="t-1-1-20"></a>
**Accountability**

Tracing actions to a specific identity, through auditing and logging.

> On the exam: Needs unique user IDs. Shared accounts destroy accountability, so the fix in a 'shared admin login' scenario is individual accounts plus logging.

<a name="t-1-1-21"></a>
**Auditing and logging**

Record who, what, when, where, and outcome. Protect logs from tampering and keep clocks synced.

> On the exam: Logging records events; auditing reviews them. Send logs to a separate, append-only store so an attacker or admin can't erase their tracks.

<details><summary>Lesson (06 Oct 2026)</summary>

**What they are**

- **Logging:** automatically recording events as they happen (who, what, when, where, outcome)
- **Auditing:** reviewing those records to check compliance, detect misuse and investigate incidents

Logging creates the evidence; auditing examines it. Together they provide **accountability**.

**What a good log entry contains**

- **Who:** user or service ID
- **What:** the action (login, delete, permission change)
- **When:** timestamp from a synchronized clock
- **Where:** source IP, device, component
- **Outcome:** success or failure

**What to log**

- Logins and logouts, success **and failure**
- Access to sensitive data
- Privilege and permission changes, account creation/deletion
- Admin actions and configuration changes
- Security errors: failed validation, access denied

**What NOT to log**

- Passwords, keys, tokens, session IDs
- Full card numbers and unnecessary personal data

Logs are often less protected than the database, so secrets in logs become a leak.

**Protecting logs**

- **Centralize** them (send to a separate log server or SIEM) so a compromised server can't erase its tracks
- **Append-only / write-once** storage; hash or sign logs to prove integrity
- **Restrict access** and log who reads or changes logs
- **Synchronize clocks (NTP)** so events can be correlated
- **Encode log input** to prevent log injection (fake entries)
- Set **retention** per policy and law

**Making them useful**

Logs nobody reviews are useless: use alerts, dashboards and regular audits.

**On the exam**

- Attacker deleted logs to hide activity → logs should be forwarded to a central protected store
- Can't correlate events across servers → clocks not synchronized
- Passwords found in log files → sensitive data logged; fix logging, rotate credentials
- **Trap:** logging is detective, not preventive
- **Trap:** shared accounts make logs useless for accountability

**Quick check:** After a breach, investigators find the attacker cleared the web server's local log files, and nobody noticed for weeks. What went wrong, and what's the fix?

**Answer:** Problems: logs stored **locally** where the attacker could reach them (no integrity protection), and **no central copy or alerting**. Fix: forward logs in real time to a **central, append-only log server / SIEM** that admins on the web server can't modify; protect integrity (hashing/WORM storage), synchronize clocks, and alert on suspicious events like log clearing.

</details>

<a name="t-1-1-22"></a>
**Nonrepudiation**

The sender can't deny an action. Digital signatures and blockchain ledgers provide it.

> On the exam: Trap: HMAC and other symmetric methods do not give nonrepudiation, because both parties share the key. Only asymmetric digital signatures do.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Proof that someone performed an action or sent a message, so strong that they **can't credibly deny it** later.

**Two directions**

- **Nonrepudiation of origin:** the sender can't deny sending
- **Nonrepudiation of receipt/delivery:** the receiver can't deny receiving

**What provides it**

- **Digital signatures:** the sender signs with their **private key**; only they hold it, so only they could have signed. This is the main answer.
- Supported by: **PKI/certificates** binding the key to a real identity, **trusted timestamps**, and **tamper-proof audit logs** with unique user IDs

**What does NOT provide it**

- **Symmetric encryption, MACs and HMAC:** both sides share the same key, so either could have produced the message
- Plain hashes: anyone can compute them
- Logs from **shared accounts**: can't prove which person acted

**The chain of properties**

A digital signature gives **integrity** (unchanged) + **authenticity** (from the claimed sender) + **nonrepudiation** (sender can't deny). It does NOT give confidentiality; add encryption for that.

**Requirements for it to hold**

- The private key must stay private (HSM, smart card); a shared or stolen key breaks nonrepudiation
- Certificate must be valid and not revoked at signing time
- Unique identities and protected logs

**STRIDE link**

**Repudiation** threat (R in STRIDE) is countered by nonrepudiation controls: signatures and secure audit logging.

**On the exam**

- Customer denies placing a large order → needed digital signature and/or secure audit logs tied to a unique identity
- Which provides nonrepudiation: HMAC, AES, SHA-256, digital signature? → **digital signature**
- **Trap:** HMAC gives integrity and authenticity between the two parties, **not** nonrepudiation

**Quick check:** Two banks exchange payment instructions protected with HMAC using a shared key. Bank A later denies sending one instruction. Can Bank B prove Bank A sent it? Why?

**Answer:** **No.** HMAC uses a **shared secret key**, so both Bank A and Bank B could have created the code. Bank A can claim Bank B forged it. For nonrepudiation, Bank A must **digitally sign** with its **private key**, which only Bank A holds.

</details>

<a name="t-1-1-23"></a>
**Governance, risk and compliance (GRC)**

Aligning security with laws (regulatory), contracts (legal), and industry standards like PCI DSS.

> On the exam: Governance sets direction and roles, risk management decides what to protect, compliance proves you meet external rules. Being compliant doesn't mean being secure.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Three connected disciplines that make sure security is directed, prioritized and provable.

- **Governance:** how leadership **directs and controls** security: strategy, policies, roles, accountability, oversight. Answers 'who decides and who's responsible?'
- **Risk management:** identifying, assessing and treating risks so resources go where they matter most. Answers 'what could go wrong and what do we do about it?'
- **Compliance:** meeting the requirements of laws, regulations, contracts and internal policies, and **proving it** with evidence. Answers 'are we following the rules, and can we show it?'

**How they fit together**

Governance sets direction and appetite for risk → risk management decides what to protect and how → compliance checks and proves the rules are met → results feed back to governance.

**Sources of compliance requirements**

- **Regulatory:** laws (GDPR, HIPAA, SOX)
- **Contractual / industry:** PCI DSS, customer contracts
- **Internal:** company policies and standards

**For software**

- Requirements from laws and policies become **security requirements** early in the SDLC
- Evidence (logs, test results, sign-offs) must be produced to prove compliance
- Senior management is ultimately **accountable** (governance), even when work is delegated

**On the exam**

- **Trap:** compliance ≠ security. Compliant organizations still get breached; compliance is the minimum
- Security efforts fail because no leader supports them → **governance** problem
- Deciding which threats to address first with a limited budget → **risk management**
- Proving to auditors that controls exist and work → **compliance**
- Ultimate responsibility for security → **senior management / board**

**Quick check:** A company passed its PCI DSS audit last month, then suffered a breach through a system that wasn't in the audit scope. Which GRC idea does this show?

**Answer:** **Compliance.** Passing the PCI DSS audit shows they met the standard's minimum requirements at that point in time; it doesn't guarantee they're secure. The breach came through an area outside the audit scope, a risk that **risk management** should have identified. Compliance is the floor, not the goal.

</details>

<a name="t-1-1-24"></a>
**AAA: authentication, authorization, accounting**

The three access control functions: prove who you are, decide what you can do, record what you did.

> On the exam: Protocols: RADIUS (UDP, encrypts only the password, combines authentication and authorization) vs TACACS+ (TCP, encrypts the whole payload, separates the three A's, preferred for admin access to network devices).
Scenario cue: 'which provides per-command authorization and full encryption for device admins?' → TACACS+.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

The three core functions of access control, usually provided together by a central server:

- **Authentication:** who are you? (prove identity)
- **Authorization:** what may you do? (permissions)
- **Accounting:** what did you do? (record usage and actions, for audit, billing, investigation)

Accounting here = tracking and logging, not money. It supports **accountability**.

**Why centralize AAA**

Instead of every router, VPN or Wi-Fi access point keeping its own user list, they all ask one AAA server. One place to add, change or remove access; consistent policy; central logs.

**The two protocols**

- **RADIUS:** UDP; **combines** authentication and authorization; encrypts **only the password**; common for network access (Wi-Fi with 802.1X, VPN, ISPs)
- **TACACS+:** TCP; **separates** all three A's; encrypts the **entire payload**; supports **per-command authorization**; preferred for **admin access to network devices**
- **Diameter:** newer successor to RADIUS (mobile/telecom networks)

Memory trick: TACACS+ has a **plus**: plus full encryption, plus separated A's, plus per-command control.

**For software**

Apps implement the same three functions: authenticate users, authorize every action server-side, and **account** by logging security-relevant actions with the user's identity and time.

**On the exam**

- Need to authorize individual admin commands on routers → **TACACS+**
- Wi-Fi/VPN network access for many users → **RADIUS**
- Which protocol encrypts the whole session? → **TACACS+**
- 'Accounting' in AAA → tracking user activity (supports accountability and nonrepudiation)
- **Trap:** RADIUS does NOT encrypt everything, only the password

**Quick check:** A company wants network admins to log in to routers centrally, with each command individually authorized and the whole session encrypted. RADIUS or TACACS+?

**Answer:** **TACACS+.** It separates authentication, authorization and accounting (so it can authorize each command), uses TCP, and encrypts the whole message. RADIUS combines authentication and authorization and only encrypts the password.

</details>

<a name="t-1-1-25"></a>
**Identification vs authentication**

Identification is claiming an identity (typing a username); authentication is proving it (password, token).

> On the exam: Order: identification → authentication → authorization → accountability.
Scenario cue: 'users share one account' → identification fails, so accountability is impossible.

<details><summary>Lesson (06 Oct 2026)</summary>

**What they are**

- **Identification:** claiming who you are (username, badge). Proves nothing.
- **Authentication:** proving the claim (password, fingerprint, code).

**The sequence**

- 1. Identification: 'I am Ali'
- 2. Authentication: 'here's proof'
- 3. Authorization: 'Ali may view but not delete'
- 4. Accountability: 'Ali deleted report #7 at 14:02'

Each step depends on the one before.

**Why it matters for software**

- Every user needs a **unique ID**. Shared accounts break identification, so logs can't show who did what: accountability is lost even if authentication works.
- Identifiers aren't secrets; security must come from authentication.
- Don't reveal which part was wrong: say 'Invalid username or password', not 'User not found'.

**Example**

Nurses share one login per ward. Strong password, but nobody can tell who changed a record. Identification failure destroyed accountability.

**On the exam**

- 'Users share an account' → identification problem → loss of accountability. Fix: individual accounts + logging.
- Typing a username = identification; entering a code = authentication.
- **Trap:** strong password policy doesn't fix shared accounts.

**Quick check:** Login page says 'This email is not registered' for unknown emails. What's the problem?

**Answer:** **Username enumeration**, a form of **information disclosure** at the identification step. Attackers build a list of real accounts to target. Fix: generic 'Invalid email or password'.

</details>

<a name="t-1-1-26"></a>
**Kerberos**

Ticket-based authentication: the Key Distribution Center (Authentication Service + Ticket Granting Service) issues a ticket-granting ticket, then service tickets.

> On the exam: Strengths: passwords never sent over the network; mutual authentication; SSO in Windows domains.
Weaknesses: KDC is a single point of failure; clocks must be synced (tickets expire); stolen tickets can be replayed (pass-the-ticket).

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

A **ticket-based authentication protocol** (Windows Active Directory). Prove your identity once, then use **tickets** to reach services. Your password never travels across the network.

**The parts**

- **KDC (Key Distribution Center):** the trusted third party, made of:
- **AS (Authentication Service):** checks who you are
- **TGS (Ticket Granting Service):** issues tickets for specific services
- **TGT (Ticket Granting Ticket):** your 'day pass' proving you already authenticated
- **Service ticket:** a pass for one specific service

**The flow**

- 1. Log in: the **AS** verifies you and issues a **TGT**
- 2. Need a service: show the TGT to the **TGS**, get a **service ticket**
- 3. Present the service ticket to the service, which trusts the KDC
- 4. Tickets **expire** (about 10 hours); timestamps prevent reuse

Analogy: show ID once at the theme park entrance (AS) and get a wristband (TGT); show the wristband at each ride for a ride token (service ticket).

**Strengths**

- Passwords never sent over the network
- SSO within the domain
- **Mutual authentication**
- Timestamps and expiry limit replay

**Weaknesses (heavily tested)**

- **KDC = single point of failure** (down → nobody authenticates) **and single point of compromise** (breached → forged 'golden tickets' for anything)
- **Clocks must be synchronized** (about 5 minutes) → NTP matters
- Stolen tickets reusable until expiry (pass-the-ticket)
- Weak passwords can be cracked offline
- Built for internal networks; internet apps use SAML/OIDC

**On the exam**

- Auth fails after a clock drifted → **time synchronization**
- Main weakness → **KDC single point of failure/compromise**
- Issues service tickets → **TGS**; received at first login → **TGT**
- **Trap:** Kerberos uses **symmetric** cryptography, not public-key

**Quick check:** An organization runs a single KDC with no backup. What two risks does this create, and what's the fix?

**Answer:** 1. **Single point of failure** (availability): KDC down → nobody can log in anywhere. Fix: **multiple redundant KDCs** (replicas) with failover.
2. **Single point of compromise** (security): KDC breached → attacker can forge tickets for everything (golden ticket). Fix: **harden and protect the KDC**: restrict admin access, isolate it, monitor it, protect its master keys.
Redundancy fixes the first; it doesn't fix the second.

</details>

<a name="t-1-1-27"></a>
**Hashing vs encryption vs encoding**

Hashing: one-way, for integrity and password storage. Encryption: reversible with a key, for confidentiality. Encoding: reversible without a key (Base64), for format only.

> On the exam: Trap: Base64 is not encryption and gives no security.
Scenario cue: 'store passwords so even admins can't recover them' → salted slow hash, not encryption.

<details><summary>Lesson (06 Oct 2026)</summary>

**The core difference**

- **Hashing:** one-way; can't be reversed. Purpose: **integrity** and **password storage**.
- **Encryption:** two-way **with a key**. Purpose: **confidentiality**.
- **Encoding:** two-way **without any key**. Purpose: **format/compatibility only**. No security at all.

**Hashing**

- Turns any input into a fixed-length digest (SHA-256)
- Same input → same hash; tiny change → completely different hash
- Uses: verifying files weren't altered, password storage, digital signatures (the hash gets signed)
- Passwords: add a unique **salt** and use a **slow** algorithm (bcrypt, scrypt, Argon2, PBKDF2)
- Avoid MD5 and SHA-1 (collisions)

**How password checking works with hashes**

- Sign-up: store hash(password + salt)
- Login: hash what the user typed with the same salt and **compare the two hashes**
- Match → correct password. The system never needs, or can recover, the original
- Breached database → attacker gets hashes, not passwords; salts + slow hashing make cracking expensive

**Encryption**

- **Symmetric** (one shared key, fast): AES
- **Asymmetric** (public/private pair): RSA, ECC
- Use when you need the original data back: card numbers for refunds, files to share, data in transit (TLS)

**Encoding**

- Base64, URL encoding, HTML encoding, Unicode/UTF-8
- Anyone can reverse it with no key
- **HTML/output encoding is a security technique against XSS** (makes browsers treat input as text), but it doesn't hide data

**Quick decision guide**

- Never need the original, only to compare or verify? → **hash**
- Need the original back, but only authorized parties? → **encrypt**
- Just need data to fit a format? → **encode**

**On the exam**

- Store passwords so even admins can't recover them → **salted slow hash**, never encryption
- Developer 'protected' API keys with Base64 → not protection; anyone can decode it
- Verify a downloaded file wasn't altered → compare its **hash**
- **Trap:** encrypting passwords is wrong (reversible); hashing card numbers you need later is wrong (can't get them back)
- **Trap:** Base64 is not encryption

**Quick check:** An app must store (1) user passwords, (2) customer card numbers it needs later for refunds, and (3) a binary image inside a JSON message. Hashing, encryption or encoding for each?

**Answer:** 1. Passwords → **hashing** (salted, slow: bcrypt/Argon2). At login, hash what the user typed and **compare** it with the stored hash; the original is never needed. Encrypting passwords is wrong: whoever gets the key can decrypt every password.
2. Card numbers needed later for refunds → **encryption** (e.g., AES-256), because you must get the original back; or **tokenization**.
3. Binary image in JSON → **encoding** (Base64). Formatting only, no security.

</details>

<a name="t-1-1-28"></a>
**Software assurance**

Confidence that software is free of vulnerabilities (built in or inserted) and works as intended.

> On the exam: CSSLP view: secure software is reliable (works as expected), resilient (withstands attack) and recoverable (restores after failure).
Scenario cue: 'what does software assurance aim for?' → justified confidence in all three.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

**Justified confidence** that software is free from vulnerabilities (whether accidentally built in or deliberately inserted) and functions as intended.

Key word: **justified**. Confidence must be backed by **evidence** (test results, reviews, threat models, audits), not hope or vendor claims.

**The three qualities (ISC2)**

- **Reliable:** functions as expected under normal conditions
- **Resilient:** withstands attack and abnormal conditions
- **Recoverable:** restores itself after failure or compromise

**Where the evidence comes from**

- Security requirements and threat models
- Secure code reviews, SAST, DAST, pentests
- Traceability (every requirement tested)
- Independent assessments and certifications (Common Criteria, FIPS)
- Secure supply chain (SBOM, signed components)

**The evidence must match the claim**

- Functional tests → proves it works (reliable)
- Security tests, pentests, fuzzing, code review → proves it resists attack (resilient)
- Failover and recovery tests → proves it recovers (recoverable)

Having evidence isn't enough; it must be the right evidence for all three.

**Two kinds of threat it covers**

- **Unintentional:** flaws from mistakes (bugs, design flaws)
- **Intentional:** malicious code inserted by insiders or supply chain attackers (backdoors, logic bombs)

**On the exam**

- 'Justified confidence that software is free of vulnerabilities and works as intended' → software assurance
- Vendor says 'trust us, it's secure' → not assurance; ask for evidence
- **Trap:** passing functional tests ≠ assurance; it doesn't prove resistance to attack

**Quick check:** A vendor shows their app passed all its functional tests. Does this give software assurance? Why or why not?

**Answer:** **No, not on its own.** The evidence is real, but it's the **wrong kind**. Functional tests prove the app does what it should with normal input (reliability). Assurance also needs evidence it **resists attack** (resilience) and **recovers** (recoverability): security testing, pentests, code review, threat models. Ask: 'Does this evidence prove the claim I care about?'

</details>

<a name="t-1-1-29"></a>
**Quality vs security**

Quality means software meets requirements and works correctly; security means it resists misuse and attack.

> On the exam: Trap: high-quality software isn't automatically secure, but most vulnerabilities are quality defects. Security is a subset of quality concerns that also covers abuse cases.

<details><summary>Lesson (06 Oct 2026)</summary>

**The difference**

- **Quality:** software meets its requirements and works correctly for normal users under expected conditions ('does it do what it should?')
- **Security:** software resists misuse and attack, and doesn't do what it **shouldn't**, even under hostile conditions ('can it be made to do something bad?')

**How they relate**

- Many vulnerabilities **are** quality defects (buffer overflows, missing input checks), so better quality usually means fewer vulnerabilities
- But high quality ≠ secure. Software can pass every functional test and still be easy to attack, because functional tests use **normal** input; attackers use **abnormal** input
- Security adds **negative requirements**: things that must NOT happen (users must not see others' data)

**Practical consequences**

- Security testing must include **misuse/abuse cases**, malicious input, fuzzing and pentests, not just functional tests
- Security defects should be tracked in the same bug system, with security severity
- 'Secure software is a subset of quality software': you need quality as a foundation, plus security-specific work

**On the exam**

- 'App passed all functional/QA tests, so it's secure' → **false**
- Many security bugs are quality bugs → improving code quality reduces vulnerabilities
- **Trap:** a high-quality product can still be insecure

**Quick check:** A QA team reports zero functional defects after testing. The manager says the app is ready because it's 'secure and high quality'. Is that justified?

**Answer:** **No.** Zero functional defects shows **quality** (it meets requirements under normal use), not **security**. Nobody tested what happens with malicious input or attacks. Security needs its own testing: misuse/abuse cases, SAST/DAST, pentests.

</details>

<a name="t-1-1-30"></a>
**Holistic security**

Security across people, processes and technology, and across every layer: network, host, application, data.

> On the exam: Scenario cue: 'a strong firewall but the app has SQL injection' → security must be holistic; one strong layer can't make up for a weak one.
Related: defense in depth, weakest link.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Security that covers **everything together**, not just one piece. Attackers go for the weakest spot, so every area needs protection.

**Two dimensions**

**1. People, process, technology**

- **People:** training, awareness, clear roles (developers, testers, admins, users)
- **Process:** secure SDLC, change management, code review, incident response
- **Technology:** firewalls, encryption, authentication, scanners

A great tool fails if people misuse it or no process ensures it's used.

**2. All layers of the stack**

- **Network:** firewalls, segmentation, IDS/IPS
- **Host / OS:** hardening, patching, anti-malware
- **Application:** secure coding, input validation, authorization
- **Data:** encryption, classification, access control, backups

**Why it matters**

- Most attacks today hit the **application layer**, which network defenses can't see well (a firewall allows normal web traffic, including SQL injection)
- Security must also span the **whole lifecycle**: requirements through disposal

**Related principles**

- **Defense in depth:** multiple layers so one failure isn't fatal
- **Weakest link:** overall security equals the weakest area

**On the exam**

- Strong network security but a vulnerable application → not holistic
- Great tools, untrained staff, no process → people/process gap
- **Trap:** buying more security technology rarely fixes a people or process problem

**Quick check:** A company spends heavily on next-generation firewalls and IDS, but attackers steal data through SQL injection in the web app. Developers never had secure coding training. What principle was missed, and how do you fix it?

**Answer:** It isn't holistic: the company secured the **network/technology** layer but ignored the **application** layer (SQL injection) and **people/process** (no secure coding training, no code review or security testing). Fix: secure every layer: secure coding standards and training, code review and SAST/DAST, input validation and parameterized queries, plus the firewall.

</details>

<a name="t-1-1-31"></a>
**Biometric types and considerations**

Physiological (fingerprint, iris, face) vs behavioral (voice, typing rhythm, signature). Also enrollment time, throughput and acceptance.

> On the exam: Privacy: biometric data can't be changed if stolen, so store templates, never raw images, and protect them strongly.
Trap: biometrics are best as one factor in MFA, not alone for high security.

<details><summary>Lesson (06 Oct 2026)</summary>

**Two families**

- **Physiological:** fingerprint, face, iris, retina, palm/hand geometry, veins. More accurate and stable.
- **Behavioral:** voice, signature, keystroke dynamics, gait. More variable (mood, illness), higher error rates.

**Accuracy (roughly high → low)**

Iris/retina → fingerprint/palm → face → voice/signature. Retina is very accurate but feels invasive (psychological acceptability).

**Selection factors**

- Accuracy (FAR, FRR, CER)
- Throughput (speed per person)
- Enrollment time
- User acceptance
- Spoofing resistance: fake fingers, photos, masks, recordings → needs **liveness detection**

**The privacy issue**

**Biometrics can't be changed.** A leaked password can be reset; a leaked fingerprint is compromised for life.

- Store **templates, never raw images**; encrypt them
- Match on the device where possible (secure element)
- Treat as highly sensitive personal data (GDPR, state laws, consent)
- Use as one factor in MFA for high security

**On the exam**

- Most accurate → iris/retina; most accepted → fingerprint/face
- Photo fooled face scanner → missing liveness detection
- Why is a biometric breach worse? → can't be revoked or reissued
- Behavioral biometrics → expect higher FRR

**Quick check:** A developer wants to store raw fingerprint images centrally 'in case we need them later'. What problems should you raise?

**Answer:** Privacy breach of highly sensitive data; biometrics **can't be reissued** if leaked; violates **data minimization** (store templates only); a central raw store is a **high-value target**.

</details>

<a name="t-1-1-32"></a>
**Iron triangle constraints**

Every project is limited by scope (resources), schedule (time) and budget (cost). Security competes for all three.

> On the exam: Why security gets skipped: deadlines and budgets push it out, and it's added as an afterthought.
Scenario cue: 'security was cut to meet the release date' → iron triangle pressure; the answer is building security in from requirements so it's planned, not bolted on.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Every project is limited by three constraints that pull against each other:

- **Scope** (what's built, including resources and people)
- **Schedule** (time)
- **Budget** (cost)

Change one and the others are affected. Quality (and security) sits in the middle and suffers when the triangle is squeezed.

**Why it matters for security**

- Security needs time, money and skilled people, so it competes with features and deadlines
- Under pressure, security is the first thing cut or postponed ('we'll fix it after launch')
- This leads to **security as an afterthought**: bolted on late, costly and weak

**The defender's disadvantage**

Defenders must protect everything, all the time, within constraints; attackers need only **one** weakness and have no deadlines or rules.

**How to handle it**

- **Build security in from requirements** so it's part of scope and the plan, not an extra
- Fix issues early (much cheaper than in production)
- **Break/build criteria (bug bar):** objective rules that stop release with critical flaws
- Automate security testing in CI/CD to save time
- If security is cut, the **business owner formally accepts the risk**

**On the exam**

- 'Security testing was skipped to meet the release date' → iron triangle pressure; answer: plan security from the start, bug bar, risk acceptance
- **Trap:** the best answer is rarely 'delay everything'; it's planning security into scope, time and budget early

**Quick check:** A team is behind schedule and the manager proposes skipping security testing to hit the launch date. What concept is this, and what should have been done to prevent it?

**Answer:** **Build security into requirements and the plan from the start**, so it's part of the scope, schedule and budget rather than an optional extra cut at the end. Practically: define security requirements and acceptance criteria up front, use a bug bar (break/build criteria) so release can't happen with critical issues, automate security tests in the pipeline to save time, and if risk is accepted to meet the date, the business owner signs off formally.

</details>

<a name="t-1-1-33"></a>
**Security vs usability**

Stronger controls often make software harder to use; too much friction makes users bypass them.

> On the exam: Goal: balance them (psychological acceptability). Example: SSO or passwordless reduces friction while keeping security.
Trap: the exam rarely wants 'remove the control'; it wants a control that's both secure and usable.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

Stronger security controls often make software harder to use. Too much friction and users **bypass** the controls, so real security drops.

The related design principle is **psychological acceptability**: security mechanisms should be easy to use and not get in the way, or people will avoid them.

**Classic examples of friction backfiring**

- Complex passwords changed every 30 days → written on sticky notes or reused with a number added
- Constant security prompts → users click 'Allow' without reading (alert fatigue)
- Slow VPN or blocked tools → staff use personal email or unapproved apps (shadow IT)
- Long lockouts after a few typos → help desk overload, insecure reset shortcuts

**How to balance them**

- **SSO:** one strong login instead of many passwords
- **Passwordless / passkeys / biometrics:** strong and easy
- **Risk-based (adaptive) authentication:** extra checks only when something is unusual
- **Secure defaults:** users get security without configuring anything
- **Clear, helpful messages** instead of jargon
- Modern password guidance (NIST 800-63B): length over complexity, no forced periodic changes without reason, check breached-password lists
- Involve users in design and usability testing

**On the exam**

- Users bypass a control because it's too hard → **psychological acceptability** violated
- Best answer usually **keeps the security goal** but makes it easier (SSO, MFA app, passkeys), not 'remove the control'
- **Trap:** the most restrictive control isn't automatically the most secure if people work around it

**Quick check:** A company forces 16-character complex passwords changed every 30 days. An audit finds passwords on sticky notes under keyboards. Which principle was violated, and what's a better approach?

**Answer:** It violates **psychological acceptability** (security vs usability): the control is so painful that users work around it, which makes security worse. Better: longer passphrases with no forced 30-day changes (NIST 800-63B), a password manager, **SSO** to cut the number of passwords, and **MFA** for strength.

</details>

<a name="t-1-1-34"></a>
**Security profile**

The set of security properties software must have across all lifecycle phases: confidentiality, integrity, availability, authentication, authorization, accountability, plus design principles.

> On the exam: Key idea: a gap in any phase (e.g., confidentiality required but never designed) undoes the effort in the others.
Scenario cue: 'requirement captured, but no design control exists' → security must carry through every phase.

<details><summary>Lesson (06 Oct 2026)</summary>

**What it is**

The complete set of security properties software must have, carried through **every phase** of the lifecycle. A software's 'security DNA'.

**What's in the profile**

- **Core concepts:** confidentiality, integrity, availability, authentication, authorization, accountability (and nonrepudiation)
- **Design principles:** least privilege, separation of duties, defense in depth, fail secure, economy of mechanism, complete mediation, open design, least common mechanism, psychological acceptability, weakest link, leveraging existing components

**The key idea**

Each property must appear in **every phase**:

- **Requirements:** captured ('card data must be kept confidential')
- **Design:** a control chosen (field-level encryption)
- **Implementation:** built correctly
- **Testing:** verified
- **Deployment/operations:** configured and monitored
- **Disposal:** data destroyed securely

A gap in **any one phase** can make all the other work useless.

**How to keep the chain unbroken**

- **Requirements traceability matrix (RTM):** links each requirement → design → code → test
- Design reviews and threat modeling against the requirements
- Security test cases derived from requirements

**On the exam**

- 'Requirement existed but was never designed or tested' → broken chain; fix with **traceability**
- **Trap:** capturing a requirement isn't the same as delivering it

**Quick check:** A project's requirements say 'customer data must be kept confidential.' The design documents contain no encryption, and the app ships storing data in plaintext. Which phase broke the chain, and what practice would have caught it?

**Answer:** The **design** phase broke the chain: a confidentiality requirement existed but no encryption was designed, so developers never built it. Fix: **traceability**. Map each security requirement to a design control, code and a test case (requirements traceability matrix), and run a design review against the requirements before coding.

</details>

## 1.2 Security design principles

<a name="t-1-2-1"></a>
**Saltzer and Schroeder**

The 1975 paper most of these design principles come from.

> On the exam: The exam tests the principles through scenarios, not the paper. For each principle, learn what a violation looks like.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Jerome Saltzer and Michael Schroeder wrote 'The Protection of Information in Computer Systems' (1975). It listed the design principles for building secure systems that are still the foundation of secure design today. Most CSSLP design principles come from it.

**The original 8 principles**

- **Economy of mechanism:** keep the design small and simple
- **Fail-safe defaults:** deny by default; access only when explicitly granted
- **Complete mediation:** check every access, every time
- **Open design:** security must not depend on keeping the design secret
- **Separation of privilege:** require more than one condition or key to grant access (two-key systems)
- **Least privilege:** give only the rights needed for the task
- **Least common mechanism:** minimize mechanisms shared between users
- **Psychological acceptability:** security must be easy to use correctly

**Two extra ideas they noted (less exact for computers)**

- **Work factor:** compare the cost of breaking a control with the attacker's resources
- **Compromise recording:** record when a compromise happens (logging), even if you can't prevent it

**How CSSLP names them today**

- Fail-safe defaults → **fail secure** / default deny
- Separation of privilege → **separation of duties**, **dual control**, multi-factor
- Added later: **defense in depth**, **weakest link**, **component reuse (leveraging existing components)**, **no single point of failure**, **Zero Trust**

**On the exam**

- You won't be asked about the paper itself much; you'll get **scenarios** asking which principle is followed or violated
- 'Access denied unless explicitly allowed' → fail-safe defaults / fail secure
- 'Two keys or conditions needed' → separation of privilege
- **Trap:** 'fail-safe' in Saltzer and Schroeder means **default deny**, not the physical-safety meaning (doors unlocking in a fire). Read the context.

**Quick check:** A new app's access rules start with 'deny everything,' and users get access only when an admin explicitly grants it. Which original Saltzer and Schroeder principle is this?

**Answer:** **Fail-safe defaults.** Access is denied unless explicitly granted, so mistakes and failures result in 'no access' rather than 'open access'. In CSSLP wording this is the **fail secure** / default-deny idea.

</details>

<a name="t-1-2-2"></a>
**Least privilege**

Give only the minimum rights needed, for the minimum time.

> On the exam: Very often the correct answer for service accounts, database connections and app permissions. Classic violation: the web app connects to the database as an admin account.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Give every user, process and program **only the minimum rights needed** to do its job, and only for as long as needed. Nothing extra 'just in case'.

**Why it matters**

It limits the **blast radius**: if an account or program is compromised or makes a mistake, the damage is limited to what that account could do.

**Where it applies in software**

- **Users:** normal users aren't admins; admin rights only for admin staff
- **Service accounts:** the app's database account can read/write its own tables, not drop databases
- **Processes:** web servers run as unprivileged users, not root/SYSTEM
- **APIs and tokens:** OAuth scopes and API keys limited to needed actions
- **Developers:** no direct production access by default
- **Code:** modules and plugins get only the permissions they need
- **Time:** just-in-time access for admin tasks that expires automatically

**Common violations**

- App connects to the database as an admin account (sa, root)
- Everyone in the team gets admin 'to save time'
- Services run as SYSTEM/root
- Long-lived broad API keys

**Related ideas**

- **Need-to-know:** limits which data you see within your clearance (next topic)
- **Run-time privileges:** elevate only when needed, then drop
- **Privilege creep:** gradual violation of least privilege over time

**On the exam**

- One of the most common right answers for service accounts, database connections and permissions
- 'SQL injection let the attacker drop all tables' → app account had too much privilege
- **Trap:** least privilege limits damage; it doesn't prevent the attack itself (still fix the injection)

**Quick check:** A web app connects to its database using the database administrator account. An attacker uses SQL injection and deletes every table. Which principle was violated, and what's the fix?

**Answer:** **Least privilege** is violated: the app only needs to read, insert and update specific tables, but it has full admin rights. Fix: a dedicated database account with only the permissions the app needs (no DROP, no admin), so a SQL injection can't destroy or take over the whole database.

</details>

<a name="t-1-2-3"></a>
**Need-to-know**

Even with clearance, access only data required for the task.

> On the exam: Applies within a clearance level: a doctor sees only their own patients' records, not every record in the hospital.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Even if you have the right **clearance or role**, you get access to specific information **only if you need it for your current task**.

**Least privilege vs need-to-know**

- **Least privilege:** limits **what actions/rights** you have (read, write, admin)
- **Need-to-know:** limits **which specific data** you can see, within your level
- Example: a doctor is cleared to read medical records (privilege), but only for **their own patients** (need-to-know)
- Military: Secret clearance doesn't mean access to every Secret document, only those needed for your mission

**In software**

- Row-level or record-level access: support agents see only their assigned customers' tickets
- Data filtered by department, region or case
- Fields masked unless needed (last 4 card digits)
- ABAC rules using attributes like 'assigned to' or 'department'
- **Break-glass access:** emergency override for urgent cases, always logged and reviewed afterwards

**Why it matters**

- Limits insider snooping (celebrity records, ex-partners' data)
- Limits damage if an account is compromised
- Supports privacy laws (HIPAA minimum necessary rule, GDPR data minimization)

**On the exam**

- 'Employee with valid access viewed records they had no business reason to see' → **need-to-know** violated
- **Trap:** clearance alone doesn't grant access; need-to-know must also be met

**Quick check:** A doctor uses her valid login to look up the medical record of a celebrity admitted to another ward. She isn't treating him. Which principle was violated, and how could the system prevent it?

**Answer:** **Need-to-know.** Her clearance and role (least privilege for a doctor) allow viewing patient records in general, but she has no business need to see a celebrity patient she isn't treating. Fix: restrict access to patients under her care, with break-glass emergency access that's logged and reviewed.

</details>

<a name="t-1-2-4"></a>
**Run-time privileges**

Elevate only when needed and drop privileges right after.

> On the exam: Example: a server starts as root to bind port 443, then switches to an unprivileged user. Limits damage if it's exploited after startup.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Run with **normal (low) privileges** most of the time, **raise privileges only at the moment** a task really needs them, and **drop them immediately** afterwards.

It's least privilege applied over **time**: not just 'how much access' but 'for how long'.

**Classic examples**

- A web server starts as root to open port 80/443 (privileged ports), then switches to an unprivileged user like 'www-data'
- Admin uses a normal account daily and elevates (sudo, Windows UAC) only for admin tasks
- An installer needs admin rights to install, but the installed app runs as a normal user
- **Just-in-time (JIT) access:** admin rights granted for a short window, then revoked automatically

**Why it matters**

- Most of the time the program runs with little power, so an exploit during normal operation gets little power too
- Reduces the window when high privilege can be abused

**Design tips**

- Keep **privileged code small and separate** from the rest (privilege separation)
- Drop privileges as early as possible, permanently if they're never needed again
- Never run the whole app as root/admin for one task that needs it

**On the exam**

- 'Service runs as root the whole time because it needed root once at startup' → violates run-time privilege management / least privilege
- 'Admins use their admin account for email and browsing' → should use a normal account and elevate only when needed
- **Trap:** the answer is rarely 'give it full privileges but monitor it'; it's 'elevate briefly, then drop'

**Quick check:** A service needs root only to open port 443 at startup, but it runs as root for its whole lifetime. An attacker exploits a bug hours later and gains root. What should the design have done?

**Answer:** Use **run-time privileges**: start with root only to bind port 443 (or use a privileged helper / OS capability for just that step), then **immediately drop to an unprivileged user** for the rest of its life. Even better: let a reverse proxy or the OS (capabilities, socket activation) handle the privileged port so the app never runs as root.

</details>

<a name="t-1-2-5"></a>
**Zero Trust**

Never trust by network location; always verify every request.

> On the exam: Core ideas: verify explicitly, least privilege, assume breach, micro-segmentation. Scenario cue: 'internal traffic is trusted by default' violates Zero Trust.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

**'Never trust, always verify.'** No user, device or system is trusted just because of **where it is** (inside the corporate network or VPN). Every request is authenticated, authorized and checked, every time.

**Why it replaced the old model**

- Old model: **castle and moat**. Strong perimeter firewall; anything inside is trusted.
- Problem: once an attacker gets inside (phishing, a compromised server), they can move freely (**lateral movement**). Also, with cloud, remote work and mobile, there's no clear 'inside' anymore.

**Core principles**

- **Verify explicitly:** authenticate and authorize every request using identity, device health, location and other signals
- **Least privilege access:** just enough, just in time
- **Assume breach:** design as if attackers are already inside; limit blast radius and monitor everything

**How it's built**

- Strong identity for users AND services (MFA, mutual TLS, signed tokens)
- **Micro-segmentation:** small network zones; services only reach what they need
- Device posture checks (patched, managed device)
- Continuous monitoring and re-evaluation (not just at login)
- Encryption everywhere, including internal traffic
- NIST SP 800-207 is the Zero Trust Architecture reference

**In software design**

- Internal APIs require authentication too
- Never assume a request is safe because it came from an internal IP
- Validate input from internal services like any other input

**On the exam**

- 'Internal traffic is trusted by default' → violates **Zero Trust**
- 'Attacker moved freely after breaching one server' → lack of segmentation and Zero Trust
- **Trap:** a VPN alone isn't Zero Trust; it grants broad network access once connected
- Related: complete mediation (check every access) is a building block of Zero Trust

**Quick check:** An attacker compromises a company's public web server. Because internal services accept any request coming from inside the network, the attacker reaches the payment database without further checks. Which principle was violated, and what would fix it?

**Answer:** It violates **Zero Trust**: the services trusted each other just because they were on the internal network (implicit trust from location). The attacker moved laterally from one compromised service to the payment database. Fix: **authenticate and authorize every service-to-service call** (mutual TLS, tokens), **micro-segment** the network so the web service can't reach the payment DB directly, apply least privilege per service, and monitor traffic.

</details>

<a name="t-1-2-6"></a>
**Separation (segregation) of duties**

No single person can complete a critical task alone.

> On the exam: Prevents fraud and mistakes by one person. Classic SDLC example: a developer must not approve their own code or deploy it to production.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Split a critical task into parts so that **no single person can complete it alone**. Committing fraud or a serious error then requires **collusion** (two or more people working together), which is much less likely.

**Classic examples**

- Finance: one person creates a vendor, another approves payments to it
- Purchasing: one person orders, another receives, another pays
- Software:
- Developer writes code; **someone else reviews/approves** it
- Developer doesn't **deploy their own code** to production
- Security admin who grants access doesn't also audit access logs
- The person who requests access doesn't approve it

**Why it matters**

- Prevents **fraud** (one person can't both steal and hide it)
- Catches **errors** (a second person sees mistakes)
- Stops a single insider from planting backdoors or logic bombs

**How to implement in software**

- **Role design:** create roles so conflicting rights can't be held together (static SoD in RBAC)
- **Dynamic SoD:** a user may hold both roles but can't use both on the same transaction
- Workflow approvals (maker-checker / four-eyes principle)
- Branch protection: required reviews from someone other than the author
- Separate dev, test and production access

**Supporting controls**

- **Job rotation:** reveals hidden fraud when someone else takes over
- **Mandatory vacation:** same idea; fraud often requires constant presence

**On the exam**

- 'Developer can write, approve and deploy own code' → **separation of duties** violated
- 'Same person creates and approves payments' → SoD violated
- **Trap:** SoD reduces risk but can be beaten by **collusion**; job rotation and monitoring help detect it

**Quick check:** A developer can write code, approve her own pull request, and deploy it to production by herself. Which principle is violated, and how do you fix it?

**Answer:** **Separation of duties** is violated: one developer can write, approve and deploy her own code, so a mistake or deliberate backdoor goes straight to production. Fix: require a **different person to review and approve** each change (protected branches), and have deployment done by a separate person or an automated pipeline she can't bypass.

</details>

<a name="t-1-2-7"></a>
**Multi-party control / dual control**

Two or more people must act together (e.g., two keys to approve).

> On the exam: Abuse requires collusion between people. Dual control is about acting together (two people, two keys, at the same time).

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

A sensitive action requires **two or more authorized people acting together, at the same time**, to complete it. One person alone can't do it.

**Classic examples**

- Bank vault opened only with two keys held by two different people
- Nuclear launch requiring two officers turning keys simultaneously
- Two admins approving a production database deletion together
- Two key custodians needed to activate a master key in an HSM
- Large payments needing two signatures

**Dual control vs separation of duties**

- **Separation of duties:** **different people do different steps** of a process (one writes, another approves, another deploys); spread across time
- **Dual control / multi-party:** **multiple people perform the same action together** (both must turn the key now)
- Both prevent one person acting alone; both can be defeated by **collusion**

**M-of-N control**

- A more flexible form: any **M out of N** authorized people must cooperate (e.g., 3 of 5 key holders)
- Keeps things working if some holders are unavailable, while still needing a group

**In software**

- Approval workflows needing two approvers before high-risk actions
- Break-glass / emergency admin access requiring a second person
- HSM and key ceremonies needing multiple custodians

**On the exam**

- 'Two people must be present to perform the action' → **dual control**
- 'Different people handle different steps' → **separation of duties**
- 'Any 3 of 5 administrators must approve' → **M-of-N control**
- **Trap:** dual control is about acting **together**; split knowledge (next topic) is about each person **knowing only part** of a secret

**Quick check:** To restore the company's master encryption key, two security officers must each log in with their own credentials and approve the restore at the same time. What control is this, and how is it different from separation of duties?

**Answer:** **Dual control (multi-party control).** Two authorized people must act **together, at the same time**, to complete the action, so neither can do it alone. It's different from separation of duties, where different people do **different steps** of a process one after another.

</details>

<a name="t-1-2-8"></a>
**Split knowledge and secret sharing**

Each person holds only part of a secret (e.g., Shamir's secret sharing).

> On the exam: Each person knows only part of the secret, like half a safe combination. Split knowledge is about knowing; dual control is about doing. Master keys often use both.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

A secret (like a master encryption key) is divided so that **each person knows only part of it**. Nobody has enough information alone to use or rebuild the secret.

**Split knowledge vs dual control**

- **Split knowledge:** about **knowing**. Each person holds only a piece of the secret.
- **Dual control:** about **doing**. Several people must act together.
- They're often **used together**: two custodians each hold half the key AND must both be present to load it.
- Memory trick: split **knowledge** = what's in your head; dual **control** = what's in your hands.

**Simple split**

- Key divided into parts (e.g., two halves, or XOR shares). **All parts** are needed.
- Risk: if one holder is unavailable or loses their part, the key can't be rebuilt.

**Secret sharing (Shamir's secret sharing)**

- Mathematically splits a secret into **N shares** so that any **M (threshold)** can rebuild it, but fewer than M reveal **nothing**
- Example: 3-of-5 → any 3 custodians can recover; 2 learn nothing
- Gives security (needs a group) **and** availability (works if some are absent)

**Where it's used**

- Master keys and root CA keys
- HSM key ceremonies
- Backup/recovery keys for encrypted systems
- Cryptocurrency wallet recovery

**On the exam**

- 'Each administrator knows only half the password/key' → **split knowledge**
- 'Any 3 of 5 shares can recover the key' → **secret sharing** (M-of-N)
- 'Both must be present to act' → **dual control**
- **Trap:** a simple split where ALL parts are needed risks losing the key; threshold sharing fixes that

**Quick check:** A company's master key is divided among 5 custodians using Shamir's secret sharing, so any 3 can rebuild it. What principle does this apply, and what are its two benefits over giving the whole key to one person?

**Answer:** **Split knowledge** (with secret sharing): no single person knows the whole key, so one stolen or rogue custodian can't recover it. Using **Shamir's secret sharing (3-of-5)** means any 3 custodians together can rebuild it, so it still works if 2 are unavailable. Combined with requiring them to act together, it's also **dual/multi-party control**.

</details>

<a name="t-1-2-9"></a>
**Defense in depth**

Layered controls so one failure isn't fatal. Includes geographic and technical (vendor) diversity.

> On the exam: The answer when one control alone could be bypassed: e.g., input validation plus parameterized queries plus a WAF. Diversity means two vendors' firewalls so one exploit can't beat both.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Use **multiple, independent layers** of security controls so that if one layer fails or is bypassed, others still protect the asset. No single control is trusted to stop everything.

Analogy: a castle with a moat, walls, gates, guards and a locked keep, not just one wall.

**Layers in a typical web app**

- **Perimeter:** firewall, WAF, DDoS protection
- **Network:** segmentation, IDS/IPS
- **Host:** hardening, patching, anti-malware
- **Application:** authentication, authorization, input validation, output encoding, parameterized queries
- **Data:** encryption, masking, least-privilege database accounts, backups
- **People/process:** training, code review, monitoring, incident response

**Diversity of defense**

Layers are stronger when they're **different**, so one flaw can't defeat them all:

- **Technical (vendor) diversity:** e.g., firewalls from two different vendors
- **Geographic diversity:** systems and backups in different locations
- **Control type diversity:** mix preventive, detective and corrective controls

**Why it matters**

- Every control has gaps; layers cover each other's gaps
- Slows attackers down and gives more chances to **detect** them
- Limits damage when one layer fails

**On the exam**

- 'Company relies only on a firewall/WAF' → lacks **defense in depth**
- 'Even if X is bypassed, Y still protects the data' → defense in depth
- 'Firewalls from two different vendors' → **diversity of defense**
- **Trap:** adding the same control twice isn't real depth; layers should be independent
- Related: **weakest link** (topic 12) and **holistic security** (1.1)

**Quick check:** A company protects its web app only with a web application firewall (WAF). Attackers find a payload the WAF misses and use SQL injection to steal data. Which principle was missing, and what layers would you add?

**Answer:** **Defense in depth.** Relying only on the WAF is a single layer; when it was bypassed, nothing else stopped the injection. Add layers: **input validation**, **parameterized queries** (the real fix), a **least-privilege database account**, **encryption** of sensitive data, and **logging/monitoring** to detect attacks.

</details>

<a name="t-1-2-10"></a>
**Fail secure vs fail safe**

Fail secure defaults to a locked, deny-access state on error. Fail safe prioritizes human safety (e.g., doors unlock in a fire). For software, the exam usually wants deny on failure.

> On the exam: If authentication or authorization code throws an error, the result must be deny. Exception handlers that default to allow violate this.

<details><summary>Lesson (07 Oct 2026)</summary>

**The two terms**

- **Fail secure (fail closed):** on failure, the system goes into a state that **protects security**: deny access, lock down, keep data protected.
- **Fail safe (fail open):** on failure, the system goes into a state that **protects people/life safety**, even if security is weakened.

**The classic physical example**

A building's electronic doors during a power cut or fire:

- **Fail safe:** doors **unlock** so people can escape (life safety wins)
- **Fail secure:** doors **stay locked** (a bank vault or server cage)
- Human life always comes first; that's why fire exits fail safe.

**In software (what the exam usually wants)**

Software should almost always **fail secure**:

- Authentication or authorization error → **deny** access
- Exception during a permission check → deny, never default to allow
- Firewall crashes → block traffic rather than pass everything
- Crypto failure → stop, don't send data unencrypted
- Error messages → generic, no stack traces

**Watch the wording (Saltzer and Schroeder)**

'Fail-safe **defaults**' in Saltzer and Schroeder means **default deny**, which is the same idea as fail secure. Context tells you which meaning is used:

- About **access/permissions** → deny (secure)
- About **people's physical safety** → open/unlock (safe)

**Code pattern to avoid**

- try { check permission } catch { allow = true } ← fails open
- Correct: start with allow = false; only set true after a successful check

**Link to resiliency**

Resilient systems keep non-sensitive features running (graceful degradation) but **never** fail open on security checks.

**On the exam**

- 'Authorization service is down, so the app lets all users in' → violates **fail secure**
- 'Doors unlock during a fire alarm' → **fail safe** (correct for life safety)
- **Trap:** in software scenarios about access, pick the answer that **denies** on failure

**Quick check:** An app checks permissions with a separate authorization service. When that service is unreachable, the app's error handler grants access so users aren't blocked. What principle is violated, and what should happen instead?

**Answer:** It **fails open**, violating **fail secure** (fail-safe defaults). When the authorization service is unreachable, the safe default for software is **deny**: block access to protected features, show a 'temporarily unavailable' message, log the error and alert. Availability is kept for features that don't need authorization (graceful degradation), but never by letting everyone in.

</details>

<a name="t-1-2-11"></a>
**No single point of failure / failover**

Remove components whose failure stops everything; switch automatically to a backup.

> On the exam: Fix with redundancy and automatic failover, and test the failover regularly. A single database server behind many web servers is a classic SPOF.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

A **single point of failure (SPOF)** is any one component whose failure stops the whole system. Good design removes SPOFs using **redundancy** and **failover**.

**Common SPOFs**

- One database server, one web server, one load balancer
- One network link or internet provider
- One power supply or data center
- One identity provider or KDC (from 1.1)
- One key person who alone knows how something works
- One encryption key with no backup or recovery process

**How to remove them**

- **Redundancy:** duplicate components (servers, disks via RAID, network links, power)
- **Failover:** automatic switch to the backup when the primary fails
- **Active-active:** all copies serve traffic at once (load balanced)
- **Active-passive:** standby takes over only when the primary fails
- **Replication:** keep data copies in sync across servers or sites
- **Geographic diversity:** copies in different locations/zones
- **Test failover regularly**: untested failover often fails when needed

**Security angle**

- Availability is part of CIA
- Redundant components must be **equally secure**; an unpatched backup server is a weak link
- Failover must fail **secure** (backup site enforces the same access controls)
- Single point of failure (availability) vs single point of **compromise** (security), as with Kerberos KDCs

**On the exam**

- 'One server failure took the whole app offline' → SPOF; fix with redundancy + failover
- **Trap:** backups ≠ failover. Backups restore data after downtime; failover keeps the service running
- **Trap:** redundancy that shares the same power, network or location still has a SPOF

**Quick check:** An online store runs on several web servers but only one database server, all in one data center with a single power feed. The database's power supply fails and the store goes offline for six hours. What's the problem, and how should it be fixed?

**Answer:** The **single database server** (and its single power supply) is a single point of failure. Fix: **redundancy with automatic failover**: a replicated standby database (or cluster) on separate hardware/power, ideally in another zone, with regular failover testing. Backups alone aren't enough; they restore data but don't keep the service running.

</details>

<a name="t-1-2-12"></a>
**Economy of mechanism**

Keep designs simple. Less complexity means fewer flaws and less attack surface.

> On the exam: Simple designs are easier to review and test. If choosing between complex custom security code and one well-tested mechanism, choose the simpler one.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

A system is **only as strong as its weakest component**. Attackers don't attack your strongest control; they look for the **easiest way in**.

Analogy: a chain breaks at its weakest link, no matter how strong the other links are.

**Common weak links**

- **People:** phishing and social engineering bypass technical controls
- **Forgotten or legacy systems:** old APIs, test servers, unpatched backup servers
- **Side doors:** password reset, account recovery, admin panels, debug endpoints
- **Third parties:** vendors and suppliers with access to your systems
- **Default configurations:** default passwords left unchanged
- **Unprotected copies of data:** backups, logs, test databases with real data

**How to strengthen the weakest link**

- Find all entry points: **attack surface analysis** and asset inventory
- **Threat modeling** looks at every path, not just the main one
- Retire or secure legacy and forgotten components
- Apply the **same security standard** to every path into the system
- Train people; add MFA to reduce social engineering impact
- **Defense in depth** so one weak link doesn't expose everything

**Why it matters**

Spending heavily on one strong control while leaving another path weak wastes money; attackers simply go around.

**On the exam**

- 'Main login is strong, but the password reset/old API/test server is weak' → **weakest link**
- 'Attackers bypassed technical controls by tricking an employee' → people are the weakest link
- **Trap:** the answer is rarely 'make the strong control stronger'; it's 'fix the weakest path'
- Related: defense in depth, holistic security, attack surface reduction

**Quick check:** A company's main web login uses MFA and strict lockouts. Attackers instead use an old, forgotten v1 API that still accepts requests without authentication, and steal customer data. What principle does this show, and what should the company do?

**Answer:** **Weakest link.** The old, forgotten v1 API with no authentication was the easiest path, so attackers ignored the strong main login. Fix: **inventory and retire** old APIs (or bring them up to the same security standard), reduce the attack surface, and include every entry point in threat modeling and testing.

</details>

<a name="t-1-2-13"></a>
**Complete mediation**

Check authorization on every access, not just the first. Watch cached credentials and long-lived sessions.

> On the exam: Classic violation: permissions checked only at login and cached, so a user whose access is revoked keeps it. Fix: check on each request, use short-lived tokens.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

**Keep the design as small and simple as possible.** Fewer components, fewer lines of code, fewer features and fewer paths mean fewer places for bugs and vulnerabilities to hide. Often summarized as **KISS: Keep It Simple, Stupid**.

**Why simplicity = security**

- Complex code has more bugs, and some bugs are vulnerabilities
- Simple designs are easier to **review, test and verify**
- Fewer features and interfaces = smaller **attack surface**
- Easier to understand means fewer configuration mistakes

**How to apply it**

- Remove unused features, code, services and accounts
- Use **one well-tested security mechanism** rather than many custom ones (e.g., one central authentication service)
- Avoid writing custom security code (crypto, authentication) when a proven one exists
- Keep security-critical code (like the trusted computing base) **small** so it can be verified
- Prefer clear, simple logic over clever, complicated logic
- Reduce dependencies you don't need

**Common violations**

- Huge custom authentication or crypto code
- Multiple different login systems in one product
- Features added 'in case someone needs them'
- Overly complex permission rules nobody fully understands

**On the exam**

- 'Complex custom security code vs one simple proven mechanism' → choose the simple one (**economy of mechanism**)
- 'Removing unused features reduces risk' → economy of mechanism + attack surface reduction
- **Trap:** more features or more controls isn't automatically more secure; complexity can create weaknesses
- Related: component reuse, open design, attack surface reduction

**Quick check:** A team has built 40,000 lines of custom authentication code with dozens of special cases. A reviewer says it's too complex to verify. Which principle is violated, and what's a better approach?

**Answer:** **Economy of mechanism** is violated: 40,000 lines of custom authentication code is complex, hard to review and likely to hide flaws. Better: **replace it with a proven, standard identity provider or library** (SSO/OIDC), keeping the design small and simple. This also follows **component reuse** and **open design**.

</details>

<a name="t-1-2-14"></a>
**Open design / Kerckhoffs's principle**

Security shouldn't depend on hiding the design; only the key is secret. The opposite is security through obscurity.

> On the exam: Hidden URLs, secret proprietary algorithms or relying on attackers not knowing the design are obscurity. Prefer public, peer-reviewed algorithms with secret keys.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

**Check authorization on every access to every resource, every time.** Never assume that because access was allowed once, it's still allowed now.

**Why it matters**

Permissions change: users get fired, roles change, accounts get compromised. If the system remembers an old 'yes', it keeps granting access that should be gone.

**Common violations**

- Checking permissions **only at login**, then trusting the session for hours
- **Caching** authorization results for too long
- Checking access on the **page/menu** but not on the underlying API call
- Hidden URLs assumed to be safe ('nobody knows this link')
- Trusting client-side checks (hidden buttons) instead of server-side checks
- Long-lived tokens that can't be revoked

**How to apply it**

- Authorize **every request on the server**, at the resource level
- Use **short-lived tokens** and refresh them; support revocation
- If caching, keep it short and invalidate it when permissions change
- End active sessions when an account is disabled or a role changes
- Check object ownership on every access (prevents IDOR)

**Link to other ideas**

- The **reference monitor** concept: mediates all access, always invoked
- A building block of **Zero Trust** (verify every request)
- Related to **TOCTOU** (time of check vs time of use) problems

**On the exam**

- 'Fired employee still had access for hours because permissions were cached at login' → **complete mediation** violated
- 'Admin page hidden from menu, but the URL works if typed directly' → complete mediation (missing server-side check)
- **Trap:** performance is often the excuse for caching; the secure answer still checks every time or keeps caches very short

**Quick check:** An app checks a user's permissions at login and caches them for the 12-hour session. A manager is fired and her admin rights are removed at 9 AM, but she keeps using admin functions until 5 PM. Which principle is violated, and what's the fix?

**Answer:** **Complete mediation** is violated: permissions were checked once at login and cached for 12 hours, so revoking access had no effect until the session ended. Fix: **check authorization on every request** against current permissions (or use short-lived tokens/caches with immediate revocation), and terminate active sessions when access is revoked.

</details>

<a name="t-1-2-15"></a>
**Least common mechanism**

Minimize mechanisms shared between users or processes. Isolate and compartmentalize.

> On the exam: Shared mechanisms (a shared temp folder, shared service account) can leak data between users. Use separate instances per user or tenant.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

**Security must not depend on keeping the design or algorithm secret.** Assume attackers know exactly how the system works; only the **keys/secrets** should be secret.

**Kerckhoffs's principle**

A cryptographic system should stay secure even if **everything about it except the key** is public. (Auguste Kerckhoffs, 1883.) Claude Shannon put it as: 'the enemy knows the system.'

**The opposite: security through obscurity**

Relying on secrecy of the design itself:

- Secret, home-made encryption algorithms
- Hidden URLs or admin pages as the only protection
- Hard-coded keys or passwords buried in the code
- Non-standard ports as the only defense
- Assuming nobody will reverse-engineer the app

Problem: secrets in the design **leak** (reverse engineering, insiders, leaked source code), and once leaked, everything breaks at once and can't easily be changed.

**Why open design works**

- Public, peer-reviewed algorithms (AES, RSA, SHA-256) have been tested by thousands of experts
- If a **key** leaks, you just replace the key; if a secret **design** leaks, you must redesign
- Encourages using standards over custom inventions

**Nuance**

Obscurity can be an **extra layer** (e.g., hiding server version banners) but never the **main** protection.

**On the exam**

- 'Company uses its own secret encryption algorithm' → violates **open design**; use standard algorithms
- 'Admin page protected only by an unguessable URL' → security through obscurity
- 'Security relies on the key, not the algorithm' → **Kerckhoffs's principle**
- **Trap:** open design doesn't mean publishing your keys or passwords; only the design is public

**Quick check:** A company's mobile app protects data with a secret, home-made encryption algorithm, and the key is hidden inside the app's code. An attacker decompiles the app and decrypts data from every user. What principle was violated, and what's the fix?

**Answer:** It violates **open design** (relies on **security through obscurity**). Once the app was decompiled, the secret algorithm and the key hidden in it were exposed, so every device is broken at once. Fix: use a **standard, public, peer-reviewed algorithm (e.g., AES-GCM)**, keep only the **key** secret, and never embed keys in client apps; use per-device keys and a secure keystore.

</details>

<a name="t-1-2-16"></a>
**Psychological acceptability**

Security must be usable or people will bypass it. Examples: passwordless login, sensible password rules, CAPTCHA.

> On the exam: If users write passwords on sticky notes because the rules are too strict, the control failed this principle. Security that's easy to use gets used.

<details><summary>Lesson (07 Oct 2026)</summary>

**In plain words**

**Don't make different people share the same 'thing' if they don't have to.** Every shared thing is a doorway from one person's stuff to another's.

**Analogy: the shared fridge**

- Five flatmates share one fridge. Anyone can see, take, or spoil anyone else's food. If one person leaves the door open, **everyone's** food goes bad.
- Give each flatmate their own small fridge: nobody can touch anyone else's food, and one person's mistake only affects them.
- The shared fridge = a **common mechanism**. Separate fridges = **isolation**.

**Least privilege vs least common mechanism**

- **Least privilege** is about the **key you're given**: what you're allowed to do
- **Least common mechanism** is about the **room you're in**: what you share with others
- A hotel with one shared master key for all guests breaks least privilege; a hotel where every guest sleeps in the same big room breaks least common mechanism

**What it is (formal)**

**Minimize mechanisms that are shared between multiple users or processes**, especially when those users have different trust levels. Every shared mechanism is a possible path for data to leak, or for one user to interfere with another.

**Why sharing is risky**

- Shared resources can leak information between users
- One user can tamper with or overload something others depend on
- Shared mechanisms can create **covert channels**
- A flaw in the shared mechanism affects **everyone** at once

**Software examples**

- One shared temp folder for all users → per-user folders
- One service account for many apps → one account per app
- One cache for all customers → per-customer cache keys
- Global variables shared between sessions → per-session storage

**How to spot it on the exam**

Ask: 'Did the problem happen because two users or apps were **sharing the same thing**?' If yes → least common mechanism. Fix = **isolate** (separate per user/tenant/app).

**On the exam**

- 'One customer could see another's data through a shared cache/temp folder' → **least common mechanism**
- 'All apps use the same service account' → least common mechanism (and least privilege)
- **Trap:** sharing saves money (multitenancy), so the answer is strong isolation, not 'never share anything'

**Quick check:** A multi-tenant SaaS app writes every customer's uploaded files into one shared temp folder. One customer guesses file names and downloads another customer's invoices. Which principle is violated, and what's the fix?

**Answer:** **Least common mechanism** is violated: all tenants share one temp folder (a common mechanism), so data written by one customer was reachable by another. Fix: give each tenant (or session) its **own isolated storage** with its own permissions, e.g., separate per-tenant directories or buckets, random unguessable file names, and automatic cleanup.

</details>

<a name="t-1-2-17"></a>
**Component reuse / leveraging existing components**

Reuse proven libraries and common controls, but you inherit their vulnerabilities.

> On the exam: Saves time and reduces errors, but you inherit the component's flaws (Log4Shell). Track reused components and patch them.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is (review from 1.1 'Security vs usability')**

Security mechanisms must be **easy to use correctly** and not get in users' way. If security is too hard, people **bypass** it, and real security drops.

From Saltzer and Schroeder (one of the original 8 principles).

**Signs it's being violated**

- Users write passwords on sticky notes
- Staff use personal email or unapproved tools (shadow IT)
- Users click 'Allow' on every prompt without reading (alert fatigue)
- People share accounts because getting access takes weeks
- Security steps are skipped 'just this once'

**How to design for it**

- Make the secure way the **easy way** (secure defaults)
- SSO, passkeys, biometrics, authenticator apps
- Risk-based checks: extra friction only when risk is high
- Clear, plain-language messages and instructions
- Fast, simple processes for requesting access
- Test with real users (usability testing)

**The CSSLP mindset**

The best answer usually **keeps the security goal** and makes it easier, rather than removing the control.

**On the exam**

- 'Users bypass a control because it's too hard' → **psychological acceptability**
- **Trap:** the most restrictive control isn't the most secure if people work around it

**Quick check:** A banking app asks users to answer 20 security questions at login and change their password every week. Many users stop using the app or reuse simple passwords. Which principle is violated, and what's a better design?

**Answer:** **Psychological acceptability** is violated: 20 security questions and a weekly password change make the process so painful that users bypass it (reusing weak passwords, writing them down, abandoning the app). Better: **MFA with an authenticator app or passkeys**, SSO where possible, no forced periodic changes, and a simple, secure recovery flow.

</details>

<a name="t-1-2-18"></a>
**Weakest link**

A system is only as strong as its weakest component.

> On the exam: Attackers take the easiest path, often people (social engineering) or a forgotten legacy interface, not the strongest control.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

**Leveraging existing components:** reuse proven, well-tested components (libraries, frameworks, security services) instead of building everything from scratch.

**Why it's good for security**

- Proven components have been reviewed and tested by many people
- Fewer new lines of your own code = fewer new bugs (economy of mechanism)
- Faster, cheaper, more consistent
- Example: use the company SSO/identity provider, a standard crypto library, an approved logging framework

**The catch: you inherit their weaknesses**

- A flaw in a popular library affects **everyone** who uses it (Log4Shell in Log4j, 2021, hit thousands of companies)
- Abandoned or unmaintained components stop getting fixes
- Malicious or counterfeit packages (supply chain attacks, typosquatting)
- License obligations (e.g., GPL)

**How to reuse safely**

- Choose **trusted, maintained** components from official sources
- Keep an **inventory / SBOM** (software bill of materials) of what you use
- Use **SCA (software composition analysis)** tools to detect known vulnerabilities and license issues
- **Patch and update** promptly when advisories appear
- Verify integrity (signatures, hashes)
- Prefer the organization's **approved** components

**On the exam**

- 'Use the existing, tested authentication service instead of writing a new one' → **component reuse** (and economy of mechanism)
- 'A widely used library vulnerability affected the app' → inherited risk; fix with SBOM, SCA, patching
- **Trap:** reuse isn't 'set and forget'; reused components must be tracked and maintained

**Quick check:** A team reused a popular open-source logging library instead of writing their own, which was a good decision. Two years later, a critical flaw (like Log4Shell) is announced in it, and the team doesn't even know which apps use it. What did they do right, what went wrong, and what's the fix?

**Answer:** Reuse is right (it follows **leveraging existing components** and economy of mechanism), but the team failed to **manage** the reused component: they didn't track it or patch it. Fix: keep an **SBOM** / inventory of components, use **SCA** tools to flag known vulnerabilities, monitor advisories, and **patch promptly** (Log4j → upgrade immediately).

</details>

## 1.AI AI additions in the current outline

<a name="t-1-ai-1"></a>
**Data poisoning**

Attacker corrupts training data to change model behavior.

> On the exam: Defenses: verify where training data comes from, validate it, detect anomalies, and restrict who can modify datasets.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

An attacker **corrupts the data a machine learning model learns from**, so the model learns the wrong behavior. It attacks **integrity** at the source.

Analogy: teaching a child from a textbook where someone secretly changed some answers. The child learns the wrong answers confidently.

**Types**

- **Availability poisoning:** lots of bad data to make the model generally worse
- **Targeted / backdoor poisoning:** the model works normally, except when it sees a specific trigger (e.g., a certain word, sticker or pattern), then it does what the attacker wants

**How poisoned data gets in**

- Training on **public or user-submitted data** (reviews, feedback, web scrapes)
- **Retraining loops** that learn from live user input
- Compromised datasets or third-party data suppliers (supply chain)
- Insiders with write access to training data

**Real-world style examples**

- A spam filter retrained on user 'not spam' clicks; attackers mark their spam as 'not spam'
- A chatbot that learns from users being taught offensive language
- Malware detector trained on samples where attackers slipped in labeled-as-safe malware

**Defenses**

- **Data provenance:** know where every dataset came from (trusted sources)
- **Validate and clean** training data; detect outliers and anomalies
- **Restrict write access** to datasets (least privilege)
- Don't automatically retrain on unverified user input
- Keep **versioned datasets** to roll back
- Test models against known-good evaluation sets before release; red-team for triggers
- Monitor deployed models for unusual behavior

**On the exam**

- 'Attacker manipulated training data to change model behavior' → **data poisoning** (integrity)
- 'Model behaves normally except with a specific trigger' → **backdoor** poisoning
- **Trap:** it happens at **training time**; tricking a finished model with crafted inputs is a different attack (adversarial/evasion, in Domain 6)

**Quick check:** A fraud-detection model is retrained every night using customer feedback. Attackers submit thousands of fake 'this was legitimate' reports for transactions with a specific pattern. Weeks later, the model approves fraud with that pattern. What attack is this, and how could it be prevented?

**Answer:** **Data poisoning** (a backdoor/targeted poisoning attack). The attacker corrupted training data so the model learned to approve fraud with that pattern. Defenses: **don't train directly on unverified public feedback**; validate and filter training data (anomaly detection), track **data provenance**, restrict who can add training data, test the model against known fraud before deployment, and monitor for drift.

</details>

<a name="t-1-ai-2"></a>
**Model inversion / membership inference**

Reconstructing training data, or learning whether a record was in it, from model outputs.

> On the exam: Defenses: return less detail (no confidence scores), rate-limit queries, use differential privacy during training.

<details><summary>Lesson (07 Oct 2026)</summary>

**The big idea**

A trained model can **leak information about the private data it was trained on**, just through its answers. These attacks target **confidentiality and privacy**.

**Model inversion**

- The attacker queries the model repeatedly and uses the outputs (especially **confidence scores**) to **reconstruct** what the training data looked like
- Example: rebuilding a recognizable image of a person's face from a face-recognition model, given only their name
- Question it answers: **'What did the training data contain?'**

**Membership inference**

- The attacker figures out **whether a specific person's record was in the training data**
- Models are often **more confident** on data they were trained on, which gives it away
- Example: if a model was trained only on patients with a disease, proving someone's record was in the training set reveals they have the disease
- Question it answers: **'Was this specific record used in training?'**

**Why it happens**

- **Overfitting:** the model memorizes training examples instead of learning general patterns
- **Detailed outputs:** returning exact confidence scores gives attackers lots of signal
- **Unlimited queries:** attackers can probe the model thousands of times

**Defenses**

- **Limit output detail:** return only the label/decision, not precise confidence scores
- **Rate-limit and monitor queries** to spot probing
- **Differential privacy** during training (adds mathematical noise so no single record can be detected)
- Reduce overfitting (regularization, more diverse data)
- **Data minimization:** don't train on sensitive data you don't need
- Access control on the model API

**On the exam**

- 'Attacker reconstructs training data from model outputs' → **model inversion**
- 'Attacker determines whether a person's record was in the training set' → **membership inference**
- Both are **privacy/confidentiality** attacks; key defense ideas: less output detail, rate limiting, **differential privacy**
- **Trap:** these don't need access to the training database at all, just the model's answers

**Quick check:** A hospital publishes an API for a model trained only on cancer patients' records. An attacker submits a known person's details and notices the model is unusually confident, concluding that person was in the training data and therefore has cancer. Which attack is this, and what defenses would help?

**Answer:** **Membership inference.** By watching how confident the model is, the attacker learns whether a specific person's record was in the training data, which reveals they have the disease (a privacy/confidentiality breach). Defenses: **return only the result, not detailed confidence scores**, **rate-limit and monitor queries**, train with **differential privacy**, and reduce overfitting.

</details>

<a name="t-1-ai-3"></a>
**Training data memorization**

Models can leak proprietary code or PII they memorized during training.

> On the exam: What happens: a model trained on code or customer data can repeat parts of it word for word when prompted.
Scenario cue: an internal coding assistant suggests another team's API key, or a chatbot reveals a customer's address.
Defense: remove secrets and PII before training, filter outputs, and limit who can query the model.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

AI models, especially large language models, can **memorize exact pieces of their training data** and later **repeat them word for word** in answers. If the training data contained secrets or personal data, the model can leak them to anyone who asks the right way.

**How it differs from model inversion / membership inference**

- **Inversion/inference:** attacker **deduces** information from patterns in outputs (confidence scores)
- **Memorization:** the model **directly outputs** the original text (an API key, an email address, a paragraph of code)

**What can leak**

- Passwords, API keys and secrets in training code
- Personal data (names, phone numbers, addresses, medical details)
- Proprietary source code or confidential documents
- Copyrighted text

**Risky situations**

- Training a coding assistant on internal repositories that contain hard-coded secrets
- Fine-tuning a chatbot on customer support tickets with personal details
- Employees pasting confidential data into public AI tools that may use it for training

**Defenses**

- **Clean training data first:** scan for and remove secrets and PII (secret scanners, PII detection, de-identification)
- **Data minimization:** don't train on sensitive data you don't need
- **Output filtering:** detect and block secrets/PII in responses
- **Access control:** only people allowed to see the original data should use a model trained on it
- **Deduplicate** training data (repeated text is memorized more easily)
- Differential privacy during training
- Policy: no confidential data in public AI tools
- If a secret leaks: **rotate it immediately**

**On the exam**

- 'AI assistant suggested another team's password/API key' → **training data memorization**
- Best preventive control → **remove secrets/PII from training data before training**
- **Trap:** output filtering helps, but cleaning the training data is the root fix

**Quick check:** A company trains an internal coding assistant on all its source code repositories. A developer asks it for help and it suggests code containing another team's real production API key. What's this called, and what should the company do?

**Answer:** **Training data memorization.** The model memorized secrets (API keys) from the internal code it was trained on and repeated them to other users. Fixes: **rotate the exposed keys immediately**; **scan and remove secrets and PII from training data** before training; add **output filtering** for secrets; limit who can use the model to those allowed to see the source data; and keep secrets out of source code in the first place (use a vault).

</details>

<a name="t-1-ai-4"></a>
**Non-deterministic outputs**

AI outputs are probabilistic, so security can't assume the same input gives the same result.

> On the exam: Testing must be statistical, since one passing run proves little. Validate AI output with deterministic checks before acting on it.

<details><summary>Lesson (07 Oct 2026)</summary>

**What it is**

Traditional software is **deterministic**: same input → same output, every time. AI models (especially LLMs) are often **non-deterministic**: the **same input can produce different outputs** on different runs. Answers are generated based on probabilities, not fixed rules.

**Why it matters for security**

- **Testing is harder:** one passing test proves little; the next run might fail
- A model may refuse a harmful request 99 times and comply on the 100th
- Results can't always be **reproduced**, which complicates debugging and incident investigation
- You can't fully predict or guarantee behavior, so you can't trust outputs blindly
- Outputs can include **hallucinations** (confident but false answers)

**How to handle it**

- **Statistical testing:** run tests many times, on large evaluation sets, and measure rates (e.g., 'fails less than 0.1%')
- **Red-teaming:** repeatedly try to make the model misbehave
- **Deterministic guardrails around the AI:** normal code checks AI output before it's used (validation, allow-lists, policy checks)
- Never let AI output **directly** trigger sensitive actions (payments, deletions, refunds) without checks or human approval
- **Log prompts and outputs** for monitoring and investigation
- Treat AI output as **untrusted input**
- Settings like lower 'temperature' reduce randomness but don't eliminate it

**On the exam**

- 'AI passed a test once, so it's safe' → wrong; outputs are **non-deterministic**, test statistically
- Best design → wrap AI output in **deterministic validation** before acting on it
- **Trap:** you can't prove an AI is safe with a single test run

**Quick check:** A company tests its customer-service chatbot once by asking 'Can I get a refund after 90 days?' It answers correctly ('No'), so they launch. A week later it tells some customers 'Yes, of course,' and the company is forced to honor those refunds. Why wasn't one test enough, and how should they have designed and tested it?

**Answer:** Testing once and seeing the right answer **doesn't prove** it's safe, because outputs are **non-deterministic**: the same question can get a different answer next time. Fix: test **statistically** (run each case many times across a large test set, measure the failure rate), and add a **deterministic guardrail**: the app checks every AI answer against the actual refund policy before showing it, or never lets the AI promise refunds on its own.

</details>
