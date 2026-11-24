# Domain 4: Secure Software Architecture and Design

Exam weight: 15%

## 4.1 Security architecture

<a name="t-4-1-1"></a>
**SABSA**

Business-driven security architecture framework; starts from business attributes, uses a layered matrix.

> On the exam: Six layers (contextual, conceptual, logical, physical, component, operational) with traceability from business requirement to control.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 1: Architecture frameworks (topics 1–3)**

**1. SABSA (Sherwood Applied Business Security Architecture)**

- **Security** architecture framework that starts from **business needs** (**business-driven**).
- Top-down **6 layers**: **Contextual** (business) → **Conceptual** → **Logical** → **Physical** → **Component** → **Operational**.
- Starts by defining **business attributes** (available, confidential, auditable) and traces every control back to them.

**2. Zachman and TOGAF (ENTERPRISE architecture)**

- **Zachman** = a **matrix/grid** classifying architecture descriptions; columns = **What, How, Where, Who, When, Why**. A classification scheme, not a process.
- **TOGAF** (The Open Group Architecture Framework) = a **process**: the **ADM (Architecture Development Method)**, a repeating cycle of phases.
- **SABSA aligns with both**, bringing security into enterprise architecture.

**3. Security chain of responsibility**

Who is accountable for security at **each layer and handoff** (owner, architect, developer, ops, vendor). Security fails in the **gaps** between people; every handoff needs a clear owner.

**On the exam**

- Business-driven, layered security architecture → **SABSA**
- Grid of What/How/Where/Who/When/Why → **Zachman**
- Enterprise architecture method with ADM → **TOGAF**
- **Trap:** Zachman/TOGAF = **enterprise**; SABSA = **security**.

**Hooks**

**SABSA = Security Architecture, Business Starts it. Zachman = a grid of 6 questions. TOGAF = the method with a cycle (ADM).**

**Quick check:** (1) Security architecture tracing controls to business attributes? (2) Grid of What/How/Where/Who/When/Why?

**Answer:** SABSA, Zachman. Correct.

</details>

<a name="t-4-1-2"></a>
**Zachman and TOGAF**

Enterprise architecture frameworks that SABSA aligns with.

> On the exam: Zachman is a classification grid (who, what, where, when, why, how); TOGAF is a process (the ADM).

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 1: Architecture frameworks (topics 1–3)**

**1. SABSA (Sherwood Applied Business Security Architecture)**

- **Security** architecture framework that starts from **business needs** (**business-driven**).
- Top-down **6 layers**: **Contextual** (business) → **Conceptual** → **Logical** → **Physical** → **Component** → **Operational**.
- Starts by defining **business attributes** (available, confidential, auditable) and traces every control back to them.

**2. Zachman and TOGAF (ENTERPRISE architecture)**

- **Zachman** = a **matrix/grid** classifying architecture descriptions; columns = **What, How, Where, Who, When, Why**. A classification scheme, not a process.
- **TOGAF** (The Open Group Architecture Framework) = a **process**: the **ADM (Architecture Development Method)**, a repeating cycle of phases.
- **SABSA aligns with both**, bringing security into enterprise architecture.

**3. Security chain of responsibility**

Who is accountable for security at **each layer and handoff** (owner, architect, developer, ops, vendor). Security fails in the **gaps** between people; every handoff needs a clear owner.

**On the exam**

- Business-driven, layered security architecture → **SABSA**
- Grid of What/How/Where/Who/When/Why → **Zachman**
- Enterprise architecture method with ADM → **TOGAF**
- **Trap:** Zachman/TOGAF = **enterprise**; SABSA = **security**.

**Hooks**

**SABSA = Security Architecture, Business Starts it. Zachman = a grid of 6 questions. TOGAF = the method with a cycle (ADM).**

**Quick check:** (1) Security architecture tracing controls to business attributes? (2) Grid of What/How/Where/Who/When/Why?

**Answer:** SABSA, Zachman. Correct.

</details>

<a name="t-4-1-3"></a>
**Security chain of responsibility**

Who is accountable for security at each layer and handoff.

> On the exam: What it is: clearly defined responsibility for security at every layer and handoff (business, architects, developers, operations, vendors).
Scenario cue: 'both teams assumed the other was validating input' → broken chain of responsibility.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 1: Architecture frameworks (topics 1–3)**

**1. SABSA (Sherwood Applied Business Security Architecture)**

- **Security** architecture framework that starts from **business needs** (**business-driven**).
- Top-down **6 layers**: **Contextual** (business) → **Conceptual** → **Logical** → **Physical** → **Component** → **Operational**.
- Starts by defining **business attributes** (available, confidential, auditable) and traces every control back to them.

**2. Zachman and TOGAF (ENTERPRISE architecture)**

- **Zachman** = a **matrix/grid** classifying architecture descriptions; columns = **What, How, Where, Who, When, Why**. A classification scheme, not a process.
- **TOGAF** (The Open Group Architecture Framework) = a **process**: the **ADM (Architecture Development Method)**, a repeating cycle of phases.
- **SABSA aligns with both**, bringing security into enterprise architecture.

**3. Security chain of responsibility**

Who is accountable for security at **each layer and handoff** (owner, architect, developer, ops, vendor). Security fails in the **gaps** between people; every handoff needs a clear owner.

**On the exam**

- Business-driven, layered security architecture → **SABSA**
- Grid of What/How/Where/Who/When/Why → **Zachman**
- Enterprise architecture method with ADM → **TOGAF**
- **Trap:** Zachman/TOGAF = **enterprise**; SABSA = **security**.

**Hooks**

**SABSA = Security Architecture, Business Starts it. Zachman = a grid of 6 questions. TOGAF = the method with a cycle (ADM).**

**Quick check:** (1) Security architecture tracing controls to business attributes? (2) Grid of What/How/Where/Who/When/Why?

**Answer:** SABSA, Zachman. Correct.

</details>

<a name="t-4-1-4"></a>
**Security control types**

Preventive, detective, corrective, deterrent, compensating, recovery.

> On the exam: Logging = detective; input validation = preventive; restore from backup = recovery; warning banner = deterrent; compensating = alternative when the main control isn't possible.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 2: Controls (topics 4–6), exam angle**

**4. Control TYPES (what the control does)**

- **Preventive:** STOPS it (locks, MFA, input validation, firewall rules)
- **Detective:** NOTICES it (logs, IDS, alerts, audits)
- **Corrective:** FIXES the immediate damage (antivirus quarantine, patch the exploited flaw, reset hacked password)
- **Recovery:** RESTORES normal operations (backups, DR, failover)
- **Deterrent:** DISCOURAGES (warning banners, "CCTV in use" signs, visible guards)
- **Compensating:** ALTERNATIVE when the normal control isn't possible (isolate unpatchable system)
- (Directive: tells people what to do: policies, "authorized staff only")

**Pairs the exam mixes:** sign = deterrent vs lock = preventive · quarantine malware = corrective vs restore from backup = recovery.

**5. Control CATEGORIES (how implemented)**

- **Administrative** (managerial): policies, training, background checks, procedures
- **Technical** (logical): encryption, MFA, firewalls, ACLs, **on-screen banners**
- **Physical:** locks, fences, guards, badge readers, **printed** door signs
- **Test:** could you kick it? → physical · on a screen/software → technical · document/rule → administrative
- Every control has a type AND a category: badge reader = preventive + physical; awareness training = preventive + administrative; IDS = detective + technical.

**6. Control prioritization**

Rank by **risk reduction, cost, feasibility**; biggest risks, best value first (cost-benefit, 2.8); **layer** them (defense in depth: prevent + detect + recover).

**On the exam**

- CCTV warning sign → **deterrent** (+ physical) · recording CCTV camera → **detective**
- Restore from backup after ransomware → **recovery** · antivirus removes malware → **corrective**
- Awareness training → **administrative** · login banner → **deterrent + technical**

**Hook**

**Deter = scare. Prevent = block. Detect = notice. Correct = fix. Recover = restore. Compensate = substitute.**

**Quick check:** Type + category: (1) login warning banner (2) nightly backups used to restore a crashed server.

**Answer:** Banner = deterrent, backups = recovery. Correct.

</details>

<a name="t-4-1-5"></a>
**Control categories**

Administrative, technical (logical), physical.

> On the exam: Administrative (managerial): policies, training, background checks. Technical (logical): encryption, firewalls, access control. Physical: locks, guards, cameras.
Scenario cue: 'security awareness training is which category?' → administrative.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 2: Controls (topics 4–6), exam angle**

**4. Control TYPES (what the control does)**

- **Preventive:** STOPS it (locks, MFA, input validation, firewall rules)
- **Detective:** NOTICES it (logs, IDS, alerts, audits)
- **Corrective:** FIXES the immediate damage (antivirus quarantine, patch the exploited flaw, reset hacked password)
- **Recovery:** RESTORES normal operations (backups, DR, failover)
- **Deterrent:** DISCOURAGES (warning banners, "CCTV in use" signs, visible guards)
- **Compensating:** ALTERNATIVE when the normal control isn't possible (isolate unpatchable system)
- (Directive: tells people what to do: policies, "authorized staff only")

**Pairs the exam mixes:** sign = deterrent vs lock = preventive · quarantine malware = corrective vs restore from backup = recovery.

**5. Control CATEGORIES (how implemented)**

- **Administrative** (managerial): policies, training, background checks, procedures
- **Technical** (logical): encryption, MFA, firewalls, ACLs, **on-screen banners**
- **Physical:** locks, fences, guards, badge readers, **printed** door signs
- **Test:** could you kick it? → physical · on a screen/software → technical · document/rule → administrative
- Every control has a type AND a category: badge reader = preventive + physical; awareness training = preventive + administrative; IDS = detective + technical.

**6. Control prioritization**

Rank by **risk reduction, cost, feasibility**; biggest risks, best value first (cost-benefit, 2.8); **layer** them (defense in depth: prevent + detect + recover).

**On the exam**

- CCTV warning sign → **deterrent** (+ physical) · recording CCTV camera → **detective**
- Restore from backup after ransomware → **recovery** · antivirus removes malware → **corrective**
- Awareness training → **administrative** · login banner → **deterrent + technical**

**Hook**

**Deter = scare. Prevent = block. Detect = notice. Correct = fix. Recover = restore. Compensate = substitute.**

**Quick check:** Type + category: (1) login warning banner (2) nightly backups used to restore a crashed server.

**Answer:** Banner called physical (it is TECHNICAL: on a screen; physical = could you kick it?). Backups = technical correct. Marked shaky.

</details>

<a name="t-4-1-6"></a>
**Control prioritization**

Rank controls by risk reduction, cost and feasibility.

> On the exam: How: rank by risk reduction, cost, feasibility and requirements (legal must-haves first).
Scenario cue: 'limited budget, several controls proposed' → the one that reduces the most risk for the cost, starting with legally required controls.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 2: Controls (topics 4–6), exam angle**

**4. Control TYPES (what the control does)**

- **Preventive:** STOPS it (locks, MFA, input validation, firewall rules)
- **Detective:** NOTICES it (logs, IDS, alerts, audits)
- **Corrective:** FIXES the immediate damage (antivirus quarantine, patch the exploited flaw, reset hacked password)
- **Recovery:** RESTORES normal operations (backups, DR, failover)
- **Deterrent:** DISCOURAGES (warning banners, "CCTV in use" signs, visible guards)
- **Compensating:** ALTERNATIVE when the normal control isn't possible (isolate unpatchable system)
- (Directive: tells people what to do: policies, "authorized staff only")

**Pairs the exam mixes:** sign = deterrent vs lock = preventive · quarantine malware = corrective vs restore from backup = recovery.

**5. Control CATEGORIES (how implemented)**

- **Administrative** (managerial): policies, training, background checks, procedures
- **Technical** (logical): encryption, MFA, firewalls, ACLs, **on-screen banners**
- **Physical:** locks, fences, guards, badge readers, **printed** door signs
- **Test:** could you kick it? → physical · on a screen/software → technical · document/rule → administrative
- Every control has a type AND a category: badge reader = preventive + physical; awareness training = preventive + administrative; IDS = detective + technical.

**6. Control prioritization**

Rank by **risk reduction, cost, feasibility**; biggest risks, best value first (cost-benefit, 2.8); **layer** them (defense in depth: prevent + detect + recover).

**On the exam**

- CCTV warning sign → **deterrent** (+ physical) · recording CCTV camera → **detective**
- Restore from backup after ransomware → **recovery** · antivirus removes malware → **corrective**
- Awareness training → **administrative** · login banner → **deterrent + technical**

**Hook**

**Deter = scare. Prevent = block. Detect = notice. Correct = fix. Recover = restore. Compensate = substitute.**

**Quick check:** Type + category: (1) login warning banner (2) nightly backups used to restore a crashed server.

**Answer:** Taught; not directly tested.

</details>

<a name="t-4-1-7"></a>
**Client-server and N-tier**

Separate presentation, business logic and data tiers; never trust the client.

> On the exam: Never let the front end talk directly to the database; enforce validation and access checks on the server.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 3: Architectures (topics 7–10)**

**7. Client-server and N-tier**

- Tiers: **presentation** (UI) → **business logic** (app server) → **data** (DB), each in its own network zone.
- **#1 rule: NEVER TRUST THE CLIENT.** Hidden fields, JavaScript validation, prices can be changed. Validate and authorize on the **server**.

**8. Peer-to-peer (P2P)**

- **No central server**; every node is client + server (BitTorrent, some blockchains).
- **No central authority** for trust, identity, integrity; any peer may be malicious.
- Controls: **sign and hash** content, authenticate peers, limit peer actions.

**9. Message queuing (RabbitMQ, Kafka, cloud queues)**

- Apps send messages to a **queue**; others pick them up later (**asynchronous**).
- Secure for: **integrity** (sign), **confidentiality** (encrypt), **replay protection** (timestamp / unique ID / nonce), **access control** (who publishes/reads).
- **Encryption alone does NOT stop replay** (attacker resends the encrypted copy as-is).

**10. SOA and enterprise service bus (ESB)**

- **SOA:** business built from **reusable services** called over a network (microservices = smaller modern cousin).
- **ESB:** a **central middleman** all services talk **through** (routes, translates, connects).
- ESB = **key control point** (authn, authz, logging, validation) AND **single point of failure / high-value target**.

**On the exam**

- Price validated only in browser JS → violates **never trust the client**
- No central authority, peer trust hard → **P2P**
- Captured queue message resent → **replay attack** → timestamps / unique IDs
- Central hub routing between enterprise services → **ESB**
- **Trap:** ESB = strong control point AND single point of failure.

**Hooks**

**N-tier = layers with locked doors between them. P2P = no boss, no one to vouch for anyone. ESB = the post office every service must go through.**

**Quick check:** (1) Shop accepts price sent from the browser: rule broken? (2) Captured "pay $500" queue message resent: attack + control?

**Answer:** Never trust the client; replay attack, replay protection (timestamp/nonce). Correct. Note: encryption alone does not stop replay.

</details>

<a name="t-4-1-8"></a>
**Peer-to-peer (P2P)**

No central authority, so trust and integrity are harder.

> On the exam: Each peer is both client and server, so every node must be authenticated and data integrity checked.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 3: Architectures (topics 7–10)**

**7. Client-server and N-tier**

- Tiers: **presentation** (UI) → **business logic** (app server) → **data** (DB), each in its own network zone.
- **#1 rule: NEVER TRUST THE CLIENT.** Hidden fields, JavaScript validation, prices can be changed. Validate and authorize on the **server**.

**8. Peer-to-peer (P2P)**

- **No central server**; every node is client + server (BitTorrent, some blockchains).
- **No central authority** for trust, identity, integrity; any peer may be malicious.
- Controls: **sign and hash** content, authenticate peers, limit peer actions.

**9. Message queuing (RabbitMQ, Kafka, cloud queues)**

- Apps send messages to a **queue**; others pick them up later (**asynchronous**).
- Secure for: **integrity** (sign), **confidentiality** (encrypt), **replay protection** (timestamp / unique ID / nonce), **access control** (who publishes/reads).
- **Encryption alone does NOT stop replay** (attacker resends the encrypted copy as-is).

**10. SOA and enterprise service bus (ESB)**

- **SOA:** business built from **reusable services** called over a network (microservices = smaller modern cousin).
- **ESB:** a **central middleman** all services talk **through** (routes, translates, connects).
- ESB = **key control point** (authn, authz, logging, validation) AND **single point of failure / high-value target**.

**On the exam**

- Price validated only in browser JS → violates **never trust the client**
- No central authority, peer trust hard → **P2P**
- Captured queue message resent → **replay attack** → timestamps / unique IDs
- Central hub routing between enterprise services → **ESB**
- **Trap:** ESB = strong control point AND single point of failure.

**Hooks**

**N-tier = layers with locked doors between them. P2P = no boss, no one to vouch for anyone. ESB = the post office every service must go through.**

**Quick check:** (1) Shop accepts price sent from the browser: rule broken? (2) Captured "pay $500" queue message resent: attack + control?

**Answer:** Never trust the client; replay attack, replay protection (timestamp/nonce). Correct. Note: encryption alone does not stop replay.

</details>

<a name="t-4-1-9"></a>
**Message queuing**

Secure messages for integrity, confidentiality and replay protection.

> On the exam: Sign or encrypt messages, authenticate producers and consumers, guard against replay and poison messages.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 3: Architectures (topics 7–10)**

**7. Client-server and N-tier**

- Tiers: **presentation** (UI) → **business logic** (app server) → **data** (DB), each in its own network zone.
- **#1 rule: NEVER TRUST THE CLIENT.** Hidden fields, JavaScript validation, prices can be changed. Validate and authorize on the **server**.

**8. Peer-to-peer (P2P)**

- **No central server**; every node is client + server (BitTorrent, some blockchains).
- **No central authority** for trust, identity, integrity; any peer may be malicious.
- Controls: **sign and hash** content, authenticate peers, limit peer actions.

**9. Message queuing (RabbitMQ, Kafka, cloud queues)**

- Apps send messages to a **queue**; others pick them up later (**asynchronous**).
- Secure for: **integrity** (sign), **confidentiality** (encrypt), **replay protection** (timestamp / unique ID / nonce), **access control** (who publishes/reads).
- **Encryption alone does NOT stop replay** (attacker resends the encrypted copy as-is).

**10. SOA and enterprise service bus (ESB)**

- **SOA:** business built from **reusable services** called over a network (microservices = smaller modern cousin).
- **ESB:** a **central middleman** all services talk **through** (routes, translates, connects).
- ESB = **key control point** (authn, authz, logging, validation) AND **single point of failure / high-value target**.

**On the exam**

- Price validated only in browser JS → violates **never trust the client**
- No central authority, peer trust hard → **P2P**
- Captured queue message resent → **replay attack** → timestamps / unique IDs
- Central hub routing between enterprise services → **ESB**
- **Trap:** ESB = strong control point AND single point of failure.

**Hooks**

**N-tier = layers with locked doors between them. P2P = no boss, no one to vouch for anyone. ESB = the post office every service must go through.**

**Quick check:** (1) Shop accepts price sent from the browser: rule broken? (2) Captured "pay $500" queue message resent: attack + control?

**Answer:** Never trust the client; replay attack, replay protection (timestamp/nonce). Correct. Note: encryption alone does not stop replay.

</details>

<a name="t-4-1-10"></a>
**SOA and enterprise service bus**

Services communicate through a central bus; the bus becomes a key control point.

> On the exam: A central place to enforce security policy, but also a single point of failure and a high-value target.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 3: Architectures (topics 7–10)**

**7. Client-server and N-tier**

- Tiers: **presentation** (UI) → **business logic** (app server) → **data** (DB), each in its own network zone.
- **#1 rule: NEVER TRUST THE CLIENT.** Hidden fields, JavaScript validation, prices can be changed. Validate and authorize on the **server**.

**8. Peer-to-peer (P2P)**

- **No central server**; every node is client + server (BitTorrent, some blockchains).
- **No central authority** for trust, identity, integrity; any peer may be malicious.
- Controls: **sign and hash** content, authenticate peers, limit peer actions.

**9. Message queuing (RabbitMQ, Kafka, cloud queues)**

- Apps send messages to a **queue**; others pick them up later (**asynchronous**).
- Secure for: **integrity** (sign), **confidentiality** (encrypt), **replay protection** (timestamp / unique ID / nonce), **access control** (who publishes/reads).
- **Encryption alone does NOT stop replay** (attacker resends the encrypted copy as-is).

**10. SOA and enterprise service bus (ESB)**

- **SOA:** business built from **reusable services** called over a network (microservices = smaller modern cousin).
- **ESB:** a **central middleman** all services talk **through** (routes, translates, connects).
- ESB = **key control point** (authn, authz, logging, validation) AND **single point of failure / high-value target**.

**On the exam**

- Price validated only in browser JS → violates **never trust the client**
- No central authority, peer trust hard → **P2P**
- Captured queue message resent → **replay attack** → timestamps / unique IDs
- Central hub routing between enterprise services → **ESB**
- **Trap:** ESB = strong control point AND single point of failure.

**Hooks**

**N-tier = layers with locked doors between them. P2P = no boss, no one to vouch for anyone. ESB = the post office every service must go through.**

**Quick check:** (1) Shop accepts price sent from the browser: rule broken? (2) Captured "pay $500" queue message resent: attack + control?

**Answer:** Never trust the client; replay attack, replay protection (timestamp/nonce). Correct. Note: encryption alone does not stop replay.

</details>

<a name="t-4-1-11"></a>
**SOAP vs REST web services**

SOAP uses WS-Security; REST relies on TLS, tokens (OAuth/JWT), and HTTP.

> On the exam: SOAP's WS-Security protects the message itself, end to end through intermediaries. REST over TLS protects only each hop.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 4: Web and apps (topics 11–13)**

**11. SOAP vs REST**

- **SOAP** = XML protocol with built-in standards: **WS-Security** signs/encrypts **parts of the message**; security travels **with the message**, end to end through intermediaries (**message-level**).
- **REST** = HTTP + JSON, no built-in standard; relies on **TLS** (transport), **OAuth 2.0 / JWT** tokens, HTTP features (**transport-level**).
- End-to-end protection through several intermediaries → **SOAP + WS-Security**.

**12. Microservices**

- **API gateway** = one front door for **outside** traffic (authentication, rate limiting, validation)
- **Service mesh** (Istio) = manages traffic **between** services
- **Mutual TLS (mTLS)** = **BOTH sides** present certificates; normal TLS = only the server does. Zero trust inside the network.
- **Per-service least privilege**; risk = bigger attack surface, many connections.

**13. Rich internet applications (RIA)**

Lots of logic in the browser (React/Angular SPAs; old Flash/Silverlight).

- **XSS:** attacker's **script runs on YOUR site's page** in users' browsers (e.g. `&lt;script>` in a comment), steals cookies/sessions. Fix: **output encoding**, input validation, CSP.
- **CSRF:** a **malicious OTHER site** tricks a logged-in user's **browser** into sending a request (browser auto-attaches cookies). Fix: **anti-CSRF tokens**, **SameSite cookies**.
- **Same-origin policy (SOP):** page from site A can't read site B's data (the wall).
- **CORS:** server allows specific other sites through the wall; **`*` = misconfiguration**.
- **RCE:** old plug-ins, unsafe deserialization.

**Test: whose code runs where?** Attacker's script on the site itself → XSS. Other site makes your browser send a request → CSRF.

**On the exam**

- Message-level end-to-end through intermediaries → **SOAP + WS-Security** · REST → **TLS + OAuth/JWT**
- Services authenticate each other with certificates → **mutual TLS**
- Script in a comment runs in others' browsers → **XSS**
- Hidden form on another site makes logged-in browser transfer money → **CSRF**
- API allows any origin (`*`) → **CORS misconfiguration**

**Hooks**

**XSS = their script on your page. CSRF = your browser, their request. SOP = the wall; CORS = the gate (don't leave it wide open). Mutual = both show ID.**

**Quick check:** (1) Malicious page submits transfer form to bank using logged-in session: XSS or CSRF? (2) Two microservices both prove identity with certificates: name?

**Answer:** Taught (known).

</details>

<a name="t-4-1-12"></a>
**Microservices**

API gateway, service mesh, mutual TLS between services, per-service least privilege.

> On the exam: Security concerns: many APIs (bigger attack surface), service-to-service authentication (mutual TLS, tokens), central API gateway for authentication and rate limiting, secrets per service, logging across services.
Scenario cue: 'any internal service can call any other' → add service mesh/mTLS and per-service authorization (Zero Trust).

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 4: Web and apps (topics 11–13)**

**11. SOAP vs REST**

- **SOAP** = XML protocol with built-in standards: **WS-Security** signs/encrypts **parts of the message**; security travels **with the message**, end to end through intermediaries (**message-level**).
- **REST** = HTTP + JSON, no built-in standard; relies on **TLS** (transport), **OAuth 2.0 / JWT** tokens, HTTP features (**transport-level**).
- End-to-end protection through several intermediaries → **SOAP + WS-Security**.

**12. Microservices**

- **API gateway** = one front door for **outside** traffic (authentication, rate limiting, validation)
- **Service mesh** (Istio) = manages traffic **between** services
- **Mutual TLS (mTLS)** = **BOTH sides** present certificates; normal TLS = only the server does. Zero trust inside the network.
- **Per-service least privilege**; risk = bigger attack surface, many connections.

**13. Rich internet applications (RIA)**

Lots of logic in the browser (React/Angular SPAs; old Flash/Silverlight).

- **XSS:** attacker's **script runs on YOUR site's page** in users' browsers (e.g. `&lt;script>` in a comment), steals cookies/sessions. Fix: **output encoding**, input validation, CSP.
- **CSRF:** a **malicious OTHER site** tricks a logged-in user's **browser** into sending a request (browser auto-attaches cookies). Fix: **anti-CSRF tokens**, **SameSite cookies**.
- **Same-origin policy (SOP):** page from site A can't read site B's data (the wall).
- **CORS:** server allows specific other sites through the wall; **`*` = misconfiguration**.
- **RCE:** old plug-ins, unsafe deserialization.

**Test: whose code runs where?** Attacker's script on the site itself → XSS. Other site makes your browser send a request → CSRF.

**On the exam**

- Message-level end-to-end through intermediaries → **SOAP + WS-Security** · REST → **TLS + OAuth/JWT**
- Services authenticate each other with certificates → **mutual TLS**
- Script in a comment runs in others' browsers → **XSS**
- Hidden form on another site makes logged-in browser transfer money → **CSRF**
- API allows any origin (`*`) → **CORS misconfiguration**

**Hooks**

**XSS = their script on your page. CSRF = your browser, their request. SOP = the wall; CORS = the gate (don't leave it wide open). Mutual = both show ID.**

**Quick check:** (1) Malicious page submits transfer form to bank using logged-in session: XSS or CSRF? (2) Two microservices both prove identity with certificates: name?

**Answer:** I said API gateway for both-sides-certificates (answer: MUTUAL TLS); re-check said "only server TLS" (that is normal TLS). Marked shaky.

</details>

<a name="t-4-1-13"></a>
**Rich internet applications**

Client-side threats: XSS, CSRF, same-origin policy, CORS misconfiguration, remote code execution.

> On the exam: Attackers can read and change client-side code, so never put secrets or security decisions there.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 4: Web and apps (topics 11–13)**

**11. SOAP vs REST**

- **SOAP** = XML protocol with built-in standards: **WS-Security** signs/encrypts **parts of the message**; security travels **with the message**, end to end through intermediaries (**message-level**).
- **REST** = HTTP + JSON, no built-in standard; relies on **TLS** (transport), **OAuth 2.0 / JWT** tokens, HTTP features (**transport-level**).
- End-to-end protection through several intermediaries → **SOAP + WS-Security**.

**12. Microservices**

- **API gateway** = one front door for **outside** traffic (authentication, rate limiting, validation)
- **Service mesh** (Istio) = manages traffic **between** services
- **Mutual TLS (mTLS)** = **BOTH sides** present certificates; normal TLS = only the server does. Zero trust inside the network.
- **Per-service least privilege**; risk = bigger attack surface, many connections.

**13. Rich internet applications (RIA)**

Lots of logic in the browser (React/Angular SPAs; old Flash/Silverlight).

- **XSS:** attacker's **script runs on YOUR site's page** in users' browsers (e.g. `&lt;script>` in a comment), steals cookies/sessions. Fix: **output encoding**, input validation, CSP.
- **CSRF:** a **malicious OTHER site** tricks a logged-in user's **browser** into sending a request (browser auto-attaches cookies). Fix: **anti-CSRF tokens**, **SameSite cookies**.
- **Same-origin policy (SOP):** page from site A can't read site B's data (the wall).
- **CORS:** server allows specific other sites through the wall; **`*` = misconfiguration**.
- **RCE:** old plug-ins, unsafe deserialization.

**Test: whose code runs where?** Attacker's script on the site itself → XSS. Other site makes your browser send a request → CSRF.

**On the exam**

- Message-level end-to-end through intermediaries → **SOAP + WS-Security** · REST → **TLS + OAuth/JWT**
- Services authenticate each other with certificates → **mutual TLS**
- Script in a comment runs in others' browsers → **XSS**
- Hidden form on another site makes logged-in browser transfer money → **CSRF**
- API allows any origin (`*`) → **CORS misconfiguration**

**Hooks**

**XSS = their script on your page. CSRF = your browser, their request. SOP = the wall; CORS = the gate (don't leave it wide open). Mutual = both show ID.**

**Quick check:** (1) Malicious page submits transfer form to bank using logged-in session: XSS or CSRF? (2) Two microservices both prove identity with certificates: name?

**Answer:** I said XSS for malicious-page form submit (answer: CSRF); re-check: script in forum comment = XSS, correct. Marked shaky.

</details>

<a name="t-4-1-14"></a>
**Pervasive / ubiquitous computing**

IoT, wireless, location-based, RFID, NFC, sensor and mesh networks.

> On the exam: What it is: computing everywhere: IoT, wearables, RFID/NFC tags, sensors, mesh and wireless networks.
Risks: weak default credentials, no updates, eavesdropping on wireless, physical tampering, location privacy.
Scenario cue: 'thousands of devices ship with the same default password' → require unique credentials per device.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 5: Devices (topics 14–15)**

**14. Pervasive / ubiquitous computing**

- Computing **everywhere** in small connected devices: **IoT**, wearables, wireless sensors, **mesh networks**, location-based services.
- **RFID**: tags read by radio **from a distance** (shop tags, badges, pet chips). Risks: **skimming**, **cloning**, eavesdropping.
- **NFC**: very **short-range** RFID (a few cm): tap-to-pay, pairing. Risks: eavesdropping, relay attacks.
- IoT is hard: little CPU/memory (weak/no encryption), **default passwords**, rarely patched, huge numbers. **Mirai** botnet = IoT cameras via default passwords.
- Controls: change defaults, **NETWORK SEGMENTATION** (own VLAN), signed updates, disable unused services. When a device can't protect itself, **wall it off**.

**15. Embedded software**

- Software built into hardware (car controllers, medical devices, routers, smart meters).
- **Secure boot:** checks firmware is **signed by the manufacturer** before running it.
- **Signed and verified updates**; **secure memory** for keys.
- Challenges: 10+ year lifespans, hard to update, limited resources, physical access.

**On the exam**

- Badge read from a distance and cloned → **RFID skimming/cloning**
- IoT camera botnet via default passwords → **default credentials** (change, segment)
- Device refuses unsigned firmware → **secure boot**
- **Trap:** for IoT, **segmentation** is key because devices can't secure themselves.

**Hooks**

**RFID = read from a distance. NFC = Near (a few cm). Secure boot = check the signature before you start. Can't protect itself → wall it off.**

**Quick check:** (1) Smart thermostats cannot run antivirus, rarely patched: which NETWORK control? (2) Pump checks firmware is manufacturer-signed at every start: name?

**Answer:** I answered NFC/RFID/IoT instead of the network control: NETWORK SEGMENTATION. Marked shaky.

</details>

<a name="t-4-1-15"></a>
**Embedded software**

Secure boot, secure memory, signed and verified updates.

> On the exam: Secure boot blocks unsigned firmware; anti-rollback prevents downgrading to a vulnerable version.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 5: Devices (topics 14–15)**

**14. Pervasive / ubiquitous computing**

- Computing **everywhere** in small connected devices: **IoT**, wearables, wireless sensors, **mesh networks**, location-based services.
- **RFID**: tags read by radio **from a distance** (shop tags, badges, pet chips). Risks: **skimming**, **cloning**, eavesdropping.
- **NFC**: very **short-range** RFID (a few cm): tap-to-pay, pairing. Risks: eavesdropping, relay attacks.
- IoT is hard: little CPU/memory (weak/no encryption), **default passwords**, rarely patched, huge numbers. **Mirai** botnet = IoT cameras via default passwords.
- Controls: change defaults, **NETWORK SEGMENTATION** (own VLAN), signed updates, disable unused services. When a device can't protect itself, **wall it off**.

**15. Embedded software**

- Software built into hardware (car controllers, medical devices, routers, smart meters).
- **Secure boot:** checks firmware is **signed by the manufacturer** before running it.
- **Signed and verified updates**; **secure memory** for keys.
- Challenges: 10+ year lifespans, hard to update, limited resources, physical access.

**On the exam**

- Badge read from a distance and cloned → **RFID skimming/cloning**
- IoT camera botnet via default passwords → **default credentials** (change, segment)
- Device refuses unsigned firmware → **secure boot**
- **Trap:** for IoT, **segmentation** is key because devices can't secure themselves.

**Hooks**

**RFID = read from a distance. NFC = Near (a few cm). Secure boot = check the signature before you start. Can't protect itself → wall it off.**

**Quick check:** (1) Smart thermostats cannot run antivirus, rarely patched: which NETWORK control? (2) Pump checks firmware is manufacturer-signed at every start: name?

**Answer:** Secure boot. Correct.

</details>

<a name="t-4-1-16"></a>
**Cloud service models**

SaaS, PaaS, IaaS; customer responsibility grows from SaaS to IaaS.

> On the exam: SaaS: you manage data and access. PaaS: plus your app. IaaS: plus the OS and network configuration.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 6: Cloud (topics 16–18)**

**16. Service models (who manages what)**

- **SaaS** (Gmail, Salesforce): provider runs everything; you manage **data, users, access settings**.
- **PaaS** (Heroku, Azure App Service): you manage **app + data + access**.
- **IaaS** (AWS EC2, Azure VMs): you manage **OS, network config, apps, data, access**.
- Your responsibility **grows** SaaS → PaaS → IaaS.

**17. Deployment models and multitenancy**

- **Public** (shared, provider-run) · **Private** (one org) · **Hybrid** (mix) · **Community** (orgs with common needs: hospitals, agencies).
- **Multitenancy:** many tenants share infrastructure; risk = **tenant isolation** failure (one customer sees another's data).

**18. Shared responsibility model**

- **Provider secures the cloud itself** (data centers, hardware, hypervisor); **customer secures what they put in it** (data, identities, access, configuration).
- **You can outsource the work, never the accountability for your data.** Public S3 bucket leak = **customer's** fault (misconfiguration).
- ALWAYS the customer's in every model: **data, accounts, access**.

**On the exam**

- Most customer control/responsibility → **IaaS**
- Several hospitals share a healthcare cloud → **community**
- Public bucket leaked data → **customer** (misconfiguration)
- One customer's data visible to another → **tenant isolation** failure
- **Trap:** moving to the cloud doesn't move accountability.

**Hook**

**The provider secures the house; you lock your own room.**

**Quick check:** (1) SaaS email account hacked via weak password: provider or customer? (2) Which model makes the customer patch the OS?

**Answer:** Customer; IaaS. Both correct.

</details>

<a name="t-4-1-17"></a>
**Cloud deployment models and multitenancy**

Public, private, hybrid, community; tenant isolation.

> On the exam: Public (shared provider), private (one organization), hybrid (mix), community (shared by orgs with common needs).
Multitenancy: many customers share infrastructure, so isolation failures can leak data between tenants.
Scenario cue: 'strict regulation, needs full control' → private; 'several hospitals share a platform' → community.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 6: Cloud (topics 16–18)**

**16. Service models (who manages what)**

- **SaaS** (Gmail, Salesforce): provider runs everything; you manage **data, users, access settings**.
- **PaaS** (Heroku, Azure App Service): you manage **app + data + access**.
- **IaaS** (AWS EC2, Azure VMs): you manage **OS, network config, apps, data, access**.
- Your responsibility **grows** SaaS → PaaS → IaaS.

**17. Deployment models and multitenancy**

- **Public** (shared, provider-run) · **Private** (one org) · **Hybrid** (mix) · **Community** (orgs with common needs: hospitals, agencies).
- **Multitenancy:** many tenants share infrastructure; risk = **tenant isolation** failure (one customer sees another's data).

**18. Shared responsibility model**

- **Provider secures the cloud itself** (data centers, hardware, hypervisor); **customer secures what they put in it** (data, identities, access, configuration).
- **You can outsource the work, never the accountability for your data.** Public S3 bucket leak = **customer's** fault (misconfiguration).
- ALWAYS the customer's in every model: **data, accounts, access**.

**On the exam**

- Most customer control/responsibility → **IaaS**
- Several hospitals share a healthcare cloud → **community**
- Public bucket leaked data → **customer** (misconfiguration)
- One customer's data visible to another → **tenant isolation** failure
- **Trap:** moving to the cloud doesn't move accountability.

**Hook**

**The provider secures the house; you lock your own room.**

**Quick check:** (1) SaaS email account hacked via weak password: provider or customer? (2) Which model makes the customer patch the OS?

**Answer:** Customer; IaaS. Both correct.

</details>

<a name="t-4-1-18"></a>
**Shared responsibility model**

Which security tasks belong to the provider vs the customer.

> On the exam: Rule: the provider secures the cloud itself; the customer secures what they put in it. In IaaS the customer handles OS, apps, data and identity; in SaaS mostly data and user access.
Scenario cue: 'a misconfigured public storage bucket leaks data' → customer's responsibility.
Trap: you can outsource the work but never the accountability for your data.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 6: Cloud (topics 16–18)**

**16. Service models (who manages what)**

- **SaaS** (Gmail, Salesforce): provider runs everything; you manage **data, users, access settings**.
- **PaaS** (Heroku, Azure App Service): you manage **app + data + access**.
- **IaaS** (AWS EC2, Azure VMs): you manage **OS, network config, apps, data, access**.
- Your responsibility **grows** SaaS → PaaS → IaaS.

**17. Deployment models and multitenancy**

- **Public** (shared, provider-run) · **Private** (one org) · **Hybrid** (mix) · **Community** (orgs with common needs: hospitals, agencies).
- **Multitenancy:** many tenants share infrastructure; risk = **tenant isolation** failure (one customer sees another's data).

**18. Shared responsibility model**

- **Provider secures the cloud itself** (data centers, hardware, hypervisor); **customer secures what they put in it** (data, identities, access, configuration).
- **You can outsource the work, never the accountability for your data.** Public S3 bucket leak = **customer's** fault (misconfiguration).
- ALWAYS the customer's in every model: **data, accounts, access**.

**On the exam**

- Most customer control/responsibility → **IaaS**
- Several hospitals share a healthcare cloud → **community**
- Public bucket leaked data → **customer** (misconfiguration)
- One customer's data visible to another → **tenant isolation** failure
- **Trap:** moving to the cloud doesn't move accountability.

**Hook**

**The provider secures the house; you lock your own room.**

**Quick check:** (1) SaaS email account hacked via weak password: provider or customer? (2) Which model makes the customer patch the OS?

**Answer:** Customer; IaaS. Both correct.

</details>

<a name="t-4-1-19"></a>
**Mobile applications**

Implicit data collection, permissions, secure local storage, OWASP MASVS.

> On the exam: Risks: lost or rooted devices, insecure local storage, apps collecting data without users noticing (implicit collection), insecure communication, reverse engineering.
Controls: platform keystore, TLS with certificate pinning, minimal permissions, no secrets in the app, OWASP MASVS testing.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 7: Mobile + side channels (topics 19–20)**

**19. Mobile applications**

- **Implicit data collection:** location, contacts, device IDs, usage collected without typing; privacy (minimization, consent).
- **Permissions:** only what's needed, only when needed.
- **Secure local storage:** tokens/secrets in the **platform keystore** (iOS Keychain, Android Keystore), never plain files.
- **TLS + certificate pinning** (app accepts only your server's certificate; blocks fake certs in MITM).
- **No secrets in app code** (reverse engineering).
- Standard: **OWASP MASVS** (mobile ASVS).

**20. Side-channel attacks**

Stealing secrets by **measuring physical side effects**, not breaking the crypto:

- **Timing** (check stops at first wrong character → guess char by char) · **power** · **electromagnetic emissions** · **cache behavior** (→ Spectre/Meltdown) · **sound**.
- Defenses: **constant-time code**, noise + shielding (**TEMPEST**), **hardware secure elements**.

**On the exam**

- Token in plain text file → **platform keystore**
- Accepts only its own server's certificate → **certificate pinning**
- Mobile verification standard → **OWASP MASVS**
- Login check faster when first chars right → **timing side channel** → **constant-time comparison**
- **Trap:** side channels attack how it physically runs, not the algorithm.

**Hooks**

**Side channel = listening through the wall, not picking the lock. MASVS = ASVS for Mobile.**

**Quick check:** (1) Attacker times password rejections to learn it char by char: attack + fix? (2) Where to store a mobile login token?

**Answer:** Timing side channel, constant-time comparison; platform keystore. Both correct.

</details>

<a name="t-4-1-20"></a>
**Side-channel attacks**

Leaking secrets via timing, power use, electromagnetic emissions, cache behavior.

> On the exam: What it is: learning secrets by measuring physical effects of computation: timing differences, power use, electromagnetic emissions, cache behavior, even sound.
Defense: constant-time code, noise and shielding, hardware secure elements.
Scenario cue: 'password check returns faster when the first characters are right' → timing side channel; use constant-time comparison.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 7: Mobile + side channels (topics 19–20)**

**19. Mobile applications**

- **Implicit data collection:** location, contacts, device IDs, usage collected without typing; privacy (minimization, consent).
- **Permissions:** only what's needed, only when needed.
- **Secure local storage:** tokens/secrets in the **platform keystore** (iOS Keychain, Android Keystore), never plain files.
- **TLS + certificate pinning** (app accepts only your server's certificate; blocks fake certs in MITM).
- **No secrets in app code** (reverse engineering).
- Standard: **OWASP MASVS** (mobile ASVS).

**20. Side-channel attacks**

Stealing secrets by **measuring physical side effects**, not breaking the crypto:

- **Timing** (check stops at first wrong character → guess char by char) · **power** · **electromagnetic emissions** · **cache behavior** (→ Spectre/Meltdown) · **sound**.
- Defenses: **constant-time code**, noise + shielding (**TEMPEST**), **hardware secure elements**.

**On the exam**

- Token in plain text file → **platform keystore**
- Accepts only its own server's certificate → **certificate pinning**
- Mobile verification standard → **OWASP MASVS**
- Login check faster when first chars right → **timing side channel** → **constant-time comparison**
- **Trap:** side channels attack how it physically runs, not the algorithm.

**Hooks**

**Side channel = listening through the wall, not picking the lock. MASVS = ASVS for Mobile.**

**Quick check:** (1) Attacker times password rejections to learn it char by char: attack + fix? (2) Where to store a mobile login token?

**Answer:** Timing side channel, constant-time comparison; platform keystore. Both correct.

</details>

<a name="t-4-1-21"></a>
**Speculative execution**

CPU flaws like Spectre and Meltdown; mitigated in hardware, microcode, OS and compilers.

> On the exam: What it is: CPUs guess ahead and execute instructions early; Spectre and Meltdown abuse this to read memory they shouldn't.
Defense: microcode, OS and compiler patches, process isolation (accepting some performance cost).
Scenario cue: 'one cloud VM can read another VM's memory through a CPU flaw' → speculative execution side channel.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 8: Hardware (topics 21–22)**

**21. Speculative execution: Spectre and Meltdown**

- CPUs **guess** and run code ahead (**speculative execution**); wrong guesses are discarded but **traces stay in the CPU cache**, read via a **cache timing side channel**.
- **Meltdown (2018):** breaks the wall between **user programs and the kernel** → read **kernel memory**; mainly Intel; fixed largely by OS patches (kernel page-table isolation).
- **Spectre (2018):** tricks **other programs** into leaking their own data; almost **all** CPUs; **hard to fully fix** (compiler, browser, microcode mitigations).
- Hardware flaw software can't fully fix; in the **cloud** one tenant may read another's memory (multitenancy).
- Defenses: **microcode + OS/hypervisor patches**, compiler mitigations, browser isolation (for browsers), **dedicated non-shared hardware** for sensitive workloads.

**22. Secure element, firmware, drivers**

- **Secure element:** tamper-resistant chip that stores keys and does crypto **inside** (SIM, payment chips). Related: **TPM** (PCs), **HSM** (data centers).
- **Firmware:** low-level software **stored on hardware** (BIOS/UEFI, controllers); runs **before** the OS, so malware there (**rootkit/bootkit**) **survives OS reinstalls**. Protect: **secure boot**, **signed firmware updates**, write protection; fix: reflash.
- **Drivers:** run with **kernel privileges** → vulnerable/malicious driver = full control. Only **signed drivers** from trusted vendors.

**On the exam**

- Leaks kernel memory to user programs → **Meltdown**
- Tricks other programs into leaking; nearly all CPUs → **Spectre**
- Malware survives OS reinstall → **firmware** rootkit/bootkit (not "hardware")
- Chip that never lets payment keys out → **secure element**
- **Trap:** speculative execution = hardware; fix = microcode + OS patches.

**Hooks**

**Meltdown = melts the wall between apps and kernel. Spectre = a ghost haunting every CPU. Firmware = below the OS, so wiping the OS doesn't remove it.**

**Quick check:** (1) One cloud VM reads another VM's memory via a CPU flaw: class + one defense? (2) Malware returns after reinstalling Windows: where is it hiding?

**Answer:** I said Meltdown + browser isolation/CPU framework (microcode). Class = speculative execution (Spectre-style for cross-VM); defenses microcode/OS/hypervisor patches, dedicated hardware. Accepted.

</details>

<a name="t-4-1-22"></a>
**Secure element, firmware, drivers**

Tamper-resistant chips for keys; firmware and drivers run with high privilege.

> On the exam: Secure element: tamper-resistant chip that stores keys and does crypto; keys never leave it (SIM, payment cards, phones).
Firmware and drivers run with high privilege, so they must be signed, updated securely and minimal.
Scenario cue: 'where to store a device's private key so malware can't extract it?' → secure element or TPM.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 8: Hardware (topics 21–22)**

**21. Speculative execution: Spectre and Meltdown**

- CPUs **guess** and run code ahead (**speculative execution**); wrong guesses are discarded but **traces stay in the CPU cache**, read via a **cache timing side channel**.
- **Meltdown (2018):** breaks the wall between **user programs and the kernel** → read **kernel memory**; mainly Intel; fixed largely by OS patches (kernel page-table isolation).
- **Spectre (2018):** tricks **other programs** into leaking their own data; almost **all** CPUs; **hard to fully fix** (compiler, browser, microcode mitigations).
- Hardware flaw software can't fully fix; in the **cloud** one tenant may read another's memory (multitenancy).
- Defenses: **microcode + OS/hypervisor patches**, compiler mitigations, browser isolation (for browsers), **dedicated non-shared hardware** for sensitive workloads.

**22. Secure element, firmware, drivers**

- **Secure element:** tamper-resistant chip that stores keys and does crypto **inside** (SIM, payment chips). Related: **TPM** (PCs), **HSM** (data centers).
- **Firmware:** low-level software **stored on hardware** (BIOS/UEFI, controllers); runs **before** the OS, so malware there (**rootkit/bootkit**) **survives OS reinstalls**. Protect: **secure boot**, **signed firmware updates**, write protection; fix: reflash.
- **Drivers:** run with **kernel privileges** → vulnerable/malicious driver = full control. Only **signed drivers** from trusted vendors.

**On the exam**

- Leaks kernel memory to user programs → **Meltdown**
- Tricks other programs into leaking; nearly all CPUs → **Spectre**
- Malware survives OS reinstall → **firmware** rootkit/bootkit (not "hardware")
- Chip that never lets payment keys out → **secure element**
- **Trap:** speculative execution = hardware; fix = microcode + OS patches.

**Hooks**

**Meltdown = melts the wall between apps and kernel. Spectre = a ghost haunting every CPU. Firmware = below the OS, so wiping the OS doesn't remove it.**

**Quick check:** (1) One cloud VM reads another VM's memory via a CPU flaw: class + one defense? (2) Malware returns after reinstalling Windows: where is it hiding?

**Answer:** I said "hardware"; exact answer FIRMWARE (BIOS/UEFI, runs before OS). Marked shaky.

</details>

<a name="t-4-1-23"></a>
**Cognitive computing**

AI, virtual reality, augmented reality.

> On the exam: What it is: AI and machine learning, natural language, virtual and augmented reality.
Risks: data poisoning, adversarial inputs, privacy of biometric and environmental data captured by VR/AR, opaque decisions.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 9: Cognitive computing + Industrial IoT (topics 23–24)**

**23. Cognitive computing**

- Systems that **imitate human thinking**: AI/ML, natural language (chatbots, voice), computer vision, **VR/AR**.
- Security: huge personal data (privacy, minimization, DPIA); AI attacks (poisoning, prompt injection, model theft, **adversarial inputs**); bias + hallucination (thresholds, human review); VR/AR collect very sensitive data (eye movement, body motion, room scans), fake overlays.

**24. Industrial IoT / OT (operational technology)**

- **OT** = computers controlling **physical things** (factories, power, water, pipelines). IT = data; OT = machines.
- **ICS** = umbrella term · **SCADA** = monitors/controls systems over **large areas** from a central control room · **PLC** = rugged computer **directly controlling one machine**.
- **Priorities reversed:** IT = confidentiality first; **OT = AVAILABILITY and SAFETY first** (can't shut down to patch; failures can hurt people).
- Hard: 20–30-year-old systems, hard to patch, protocols with **no authentication** (Modbus), once air-gapped now connected.
- Controls: **network segmentation** (OT apart from IT), strict access, monitoring, **compensating controls**, planned maintenance windows.
- **Stuxnet** (2010): damaged centrifuges by manipulating **PLCs**.

**On the exam**

- AI, NLP, vision, VR/AR → **cognitive computing**
- Central system monitoring a grid over a wide area → **SCADA**
- Device directly controlling a factory machine → **PLC**
- Top OT priority → **availability and safety**
- **Trap:** "patch immediately" often wrong for OT → compensating controls + maintenance windows.

**Hooks**

**SCADA = the control room watching the whole map. PLC = the hand on one machine. IT protects data; OT protects people and machines.**

**Quick check:** (1) 25-year-old water utility control system cannot be patched without cutting water to a city: best approach? (2) In OT, which goal comes first?

**Answer:** Compensating controls + monitoring (+ segmentation, maintenance windows); availability and safety. Both correct.

</details>

<a name="t-4-1-24"></a>
**Industrial IoT / OT** (review)

ICS, SCADA, PLCs, automotive, robotics, medical devices; safety and availability come first.

> On the exam: Safety and availability come before confidentiality. Patching is hard, so segmentation is the key control.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 9: Cognitive computing + Industrial IoT (topics 23–24)**

**23. Cognitive computing**

- Systems that **imitate human thinking**: AI/ML, natural language (chatbots, voice), computer vision, **VR/AR**.
- Security: huge personal data (privacy, minimization, DPIA); AI attacks (poisoning, prompt injection, model theft, **adversarial inputs**); bias + hallucination (thresholds, human review); VR/AR collect very sensitive data (eye movement, body motion, room scans), fake overlays.

**24. Industrial IoT / OT (operational technology)**

- **OT** = computers controlling **physical things** (factories, power, water, pipelines). IT = data; OT = machines.
- **ICS** = umbrella term · **SCADA** = monitors/controls systems over **large areas** from a central control room · **PLC** = rugged computer **directly controlling one machine**.
- **Priorities reversed:** IT = confidentiality first; **OT = AVAILABILITY and SAFETY first** (can't shut down to patch; failures can hurt people).
- Hard: 20–30-year-old systems, hard to patch, protocols with **no authentication** (Modbus), once air-gapped now connected.
- Controls: **network segmentation** (OT apart from IT), strict access, monitoring, **compensating controls**, planned maintenance windows.
- **Stuxnet** (2010): damaged centrifuges by manipulating **PLCs**.

**On the exam**

- AI, NLP, vision, VR/AR → **cognitive computing**
- Central system monitoring a grid over a wide area → **SCADA**
- Device directly controlling a factory machine → **PLC**
- Top OT priority → **availability and safety**
- **Trap:** "patch immediately" often wrong for OT → compensating controls + maintenance windows.

**Hooks**

**SCADA = the control room watching the whole map. PLC = the hand on one machine. IT protects data; OT protects people and machines.**

**Quick check:** (1) 25-year-old water utility control system cannot be patched without cutting water to a city: best approach? (2) In OT, which goal comes first?

**Answer:** Compensating controls + monitoring (+ segmentation, maintenance windows); availability and safety. Both correct.

</details>

<a name="t-4-1-25"></a>
**NIST cloud characteristics**

Five essential characteristics: on-demand self-service, broad network access, resource pooling (multitenancy), rapid elasticity, measured service.

> On the exam: Scenario cue: 'resources scale up and down automatically with demand' → rapid elasticity.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 10: Cloud part 2 (topics 25, 26, 34, 35)**

**25. NIST's 5 cloud characteristics (SP 800-145)**

1. **On-demand self-service** (create resources yourself, instantly)

2. **Broad network access** (from any device over the network)

3. **Resource pooling** (shared hardware = the idea behind multitenancy; "multitenancy" is NOT the official name)

4. **Rapid elasticity** (scale up/down quickly, automatically)

5. **Measured service** (pay for what you use)

**Mnemonic: "Our Big Rubber Raft Moves."**

**26. Cloud risks and CASB**

**CASB (Cloud Access Security Broker):** sits **between users and cloud services**, enforcing policy. 4 pillars: **visibility** (finds **shadow IT**), **compliance**, **data security** (DLP, encryption), **threat protection** (hacked accounts, unusual behavior). *A security guard at the door between your company and the cloud.*

**34. Cloud threats**

**Misconfiguration = #1 cause** (public buckets, open ports, broad permissions); insecure APIs; account hijacking (no MFA); insiders; lack of visibility. Fix: **CSPM** (auto-scan for misconfigurations), MFA, least privilege.

**35. Serverless and containers**

- **Serverless:** provider handles servers/OS; **you** own code, permissions, secrets. Risks: over-permissioned functions, **event injection**, vulnerable dependencies. Controls: least privilege per function, validate every event, vault.
- **Containers + Kubernetes:** risks: vulnerable base images, **running as root**, secrets baked into images, **container escape** (containers **share the host kernel** → less isolated than VMs). Controls: scan images, minimal base images, not root, K8s **RBAC + network policies**, secrets outside images.

**On the exam**

- Scale automatically → **rapid elasticity** · pay per use → **measured service**
- Discover unapproved cloud apps → **CASB** (shadow IT)
- Top cause of cloud breaches → **misconfiguration**
- Containers less isolated than VMs → **share the host kernel**
- **Trap:** serverless ≠ no security work.

**Quick check:** (1) Employees upload company files to personal Dropbox without IT knowing: which tool? (2) Name three NIST cloud characteristics.

**Answer:** Broad network, on-demand self-service correct; said multi-tenancy (official name: RESOURCE POOLING). Marked shaky.

</details>

<a name="t-4-1-26"></a>
**Cloud security risks and CASB**

Risks: misconfiguration, data location and jurisdiction, multitenancy, vendor lock-in, insecure APIs, account hijacking. A CASB (cloud access security broker) sits between users and cloud services to enforce policy, visibility and DLP.

> On the exam: Scenario cue: 'employees use unapproved cloud apps (shadow IT)' → CASB.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 10: Cloud part 2 (topics 25, 26, 34, 35)**

**25. NIST's 5 cloud characteristics (SP 800-145)**

1. **On-demand self-service** (create resources yourself, instantly)

2. **Broad network access** (from any device over the network)

3. **Resource pooling** (shared hardware = the idea behind multitenancy; "multitenancy" is NOT the official name)

4. **Rapid elasticity** (scale up/down quickly, automatically)

5. **Measured service** (pay for what you use)

**Mnemonic: "Our Big Rubber Raft Moves."**

**26. Cloud risks and CASB**

**CASB (Cloud Access Security Broker):** sits **between users and cloud services**, enforcing policy. 4 pillars: **visibility** (finds **shadow IT**), **compliance**, **data security** (DLP, encryption), **threat protection** (hacked accounts, unusual behavior). *A security guard at the door between your company and the cloud.*

**34. Cloud threats**

**Misconfiguration = #1 cause** (public buckets, open ports, broad permissions); insecure APIs; account hijacking (no MFA); insiders; lack of visibility. Fix: **CSPM** (auto-scan for misconfigurations), MFA, least privilege.

**35. Serverless and containers**

- **Serverless:** provider handles servers/OS; **you** own code, permissions, secrets. Risks: over-permissioned functions, **event injection**, vulnerable dependencies. Controls: least privilege per function, validate every event, vault.
- **Containers + Kubernetes:** risks: vulnerable base images, **running as root**, secrets baked into images, **container escape** (containers **share the host kernel** → less isolated than VMs). Controls: scan images, minimal base images, not root, K8s **RBAC + network policies**, secrets outside images.

**On the exam**

- Scale automatically → **rapid elasticity** · pay per use → **measured service**
- Discover unapproved cloud apps → **CASB** (shadow IT)
- Top cause of cloud breaches → **misconfiguration**
- Containers less isolated than VMs → **share the host kernel**
- **Trap:** serverless ≠ no security work.

**Quick check:** (1) Employees upload company files to personal Dropbox without IT knowing: which tool? (2) Name three NIST cloud characteristics.

**Answer:** CASB. Correct.

</details>

<a name="t-4-1-27"></a>
**Mainframe architecture**

Centralized, high-reliability systems often running legacy code and connected to modern web front ends.

> On the exam: Risks: legacy code with no modern security, insecure integrations, few skilled staff.
Scenario cue: 'a web front end now exposes a decades-old mainframe' → the interface must authenticate and validate, since the legacy system assumed a closed environment.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 11: Legacy and integration (topics 27–29)**

**27. Mainframe architecture**

- Huge reliable central computers (IBM Z) running banks, airlines, insurers, government; old code (**COBOL**).
- Strength: built-in access control via an **ESM (External Security Manager)**: **RACF**, ACF2, Top Secret.
- Risks: "security through obscurity" thinking; shrinking expert pool → misconfiguration; connecting to web/APIs; old protocols (unencrypted **TN3270**).
- Controls: encrypt connections, least privilege in the ESM, monitor/log, treat as critical.

**28. Middleware and queuing**

- Software **in the middle** connecting apps (message brokers, ESBs, API gateways, app servers).
- Sees **all traffic** → compromise exposes **every connected system**; high-value target + single point of failure.
- Controls: authenticate every connecting app, encrypt, validate messages, least privilege, patch.

**29. SOAP, WSDL, UDDI**

- **SOAP** = message format (XML) · **WSDL** (Web Services Description Language) = the **instruction manual** (operations, how to call) · **UDDI** (Universal Description, Discovery and Integration) = the **directory / phone book**.
- Public WSDL = **map for attackers** (don't expose unless needed); protect SOAP with **WS-Security**; watch **XXE** (XML External Entity: parser reads server files) and **XML bombs** (nested entities crash parser).

**On the exam**

- IBM Z with RACF → **mainframe ESM** · compromise exposes every connected app → **middleware**
- Describes operations + how to call → **WSDL** · directory to discover services → **UDDI**
- Crafted XML reads server files → **XXE** · **Trap:** public WSDL = attacker's map.

**Hook**

**SOAP = the letter. WSDL = the instruction manual. UDDI = the phone book.**

**Quick check:** (1) Which is the web service instruction manual: SOAP, WSDL or UDDI? (2) Why is middleware a valuable target?

**Answer:** WSDL; sees everything, compromise exposes all connected services. Both correct.

</details>

<a name="t-4-1-28"></a>
**Middleware and queuing**

Software connecting applications (message brokers, queues, application servers).

> On the exam: Controls: authenticate producers and consumers, encrypt and sign messages, validate message content, protect queues from tampering and flooding.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 11: Legacy and integration (topics 27–29)**

**27. Mainframe architecture**

- Huge reliable central computers (IBM Z) running banks, airlines, insurers, government; old code (**COBOL**).
- Strength: built-in access control via an **ESM (External Security Manager)**: **RACF**, ACF2, Top Secret.
- Risks: "security through obscurity" thinking; shrinking expert pool → misconfiguration; connecting to web/APIs; old protocols (unencrypted **TN3270**).
- Controls: encrypt connections, least privilege in the ESM, monitor/log, treat as critical.

**28. Middleware and queuing**

- Software **in the middle** connecting apps (message brokers, ESBs, API gateways, app servers).
- Sees **all traffic** → compromise exposes **every connected system**; high-value target + single point of failure.
- Controls: authenticate every connecting app, encrypt, validate messages, least privilege, patch.

**29. SOAP, WSDL, UDDI**

- **SOAP** = message format (XML) · **WSDL** (Web Services Description Language) = the **instruction manual** (operations, how to call) · **UDDI** (Universal Description, Discovery and Integration) = the **directory / phone book**.
- Public WSDL = **map for attackers** (don't expose unless needed); protect SOAP with **WS-Security**; watch **XXE** (XML External Entity: parser reads server files) and **XML bombs** (nested entities crash parser).

**On the exam**

- IBM Z with RACF → **mainframe ESM** · compromise exposes every connected app → **middleware**
- Describes operations + how to call → **WSDL** · directory to discover services → **UDDI**
- Crafted XML reads server files → **XXE** · **Trap:** public WSDL = attacker's map.

**Hook**

**SOAP = the letter. WSDL = the instruction manual. UDDI = the phone book.**

**Quick check:** (1) Which is the web service instruction manual: SOAP, WSDL or UDDI? (2) Why is middleware a valuable target?

**Answer:** WSDL; sees everything, compromise exposes all connected services. Both correct.

</details>

<a name="t-4-1-29"></a>
**Web services: SOAP, WSDL, UDDI**

SOAP is an XML messaging protocol; WSDL describes what a service offers; UDDI was a directory to find services.

> On the exam: Risks: WSDL reveals all operations (information disclosure), XML injection, XXE.
Controls: WS-Security (sign and encrypt messages), restrict WSDL access, validate XML against a schema.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 11: Legacy and integration (topics 27–29)**

**27. Mainframe architecture**

- Huge reliable central computers (IBM Z) running banks, airlines, insurers, government; old code (**COBOL**).
- Strength: built-in access control via an **ESM (External Security Manager)**: **RACF**, ACF2, Top Secret.
- Risks: "security through obscurity" thinking; shrinking expert pool → misconfiguration; connecting to web/APIs; old protocols (unencrypted **TN3270**).
- Controls: encrypt connections, least privilege in the ESM, monitor/log, treat as critical.

**28. Middleware and queuing**

- Software **in the middle** connecting apps (message brokers, ESBs, API gateways, app servers).
- Sees **all traffic** → compromise exposes **every connected system**; high-value target + single point of failure.
- Controls: authenticate every connecting app, encrypt, validate messages, least privilege, patch.

**29. SOAP, WSDL, UDDI**

- **SOAP** = message format (XML) · **WSDL** (Web Services Description Language) = the **instruction manual** (operations, how to call) · **UDDI** (Universal Description, Discovery and Integration) = the **directory / phone book**.
- Public WSDL = **map for attackers** (don't expose unless needed); protect SOAP with **WS-Security**; watch **XXE** (XML External Entity: parser reads server files) and **XML bombs** (nested entities crash parser).

**On the exam**

- IBM Z with RACF → **mainframe ESM** · compromise exposes every connected app → **middleware**
- Describes operations + how to call → **WSDL** · directory to discover services → **UDDI**
- Crafted XML reads server files → **XXE** · **Trap:** public WSDL = attacker's map.

**Hook**

**SOAP = the letter. WSDL = the instruction manual. UDDI = the phone book.**

**Quick check:** (1) Which is the web service instruction manual: SOAP, WSDL or UDDI? (2) Why is middleware a valuable target?

**Answer:** WSDL; sees everything, compromise exposes all connected services. Both correct.

</details>

<a name="t-4-1-30"></a>
**Mobile app threats**

Lost or stolen devices, jailbreaking/rooting and sideloading (installing apps outside official stores), mobile malware, insecure data storage, side-channel data leakage (logs, caches, keyboard caches, screenshots), client-side injection, weak transport security.

> On the exam: Scenario cue: 'app works on rooted phones and stores tokens in plain files' → detect root/jailbreak where appropriate and use the secure keystore.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 12: Mobile threats + wireless (topics 30–33)**

**30. Mobile app threats**

- **Reverse engineering** (decompile; fix: obfuscation, no secrets in code); **jailbroken/rooted** devices (fix: jailbreak/root detection); insecure storage; weak TLS; malicious lookalike apps; over-broad permissions.
- **OWASP Mobile Top 10** lists them; **MASVS** verifies.

**31. BYOD and MDM**

- **BYOD** = personal devices for work; company doesn't control the device.
- **MDM** = manage/secure devices: enforce passcode, require encryption, push/block apps, **remote wipe**.
- **Containerization** = separate encrypted **work container** → **selective wipe** of work data only (privacy, trust).
- **MAM** = manage just work apps; **COPE** = corporate-owned, personally enabled.

**32. Location-based services**

- GPS/Wi-Fi/cell location = **highly sensitive** (home, work, health visits, habits).
- Requirements: **opt-in consent**, minimization, reduce precision (city not GPS), protect history, watch **spoofing**.

**33. Wireless and Bluetooth**

- Wi-Fi worst → best: **WEP** (broken, never use) → **WPA** (weak) → **WPA2** (AES; KRACK) → **WPA3** (current best; SAE).
- **Bluejacking** = sends unwanted messages, harmless (**jack = joke**).
- **Bluesnarfing** = **steals data** (contacts, messages, files) (**snarf = snatch**).
- **Bluebugging** = **takes control** (calls, listening) (**bug = boss of the phone**).
- **Test: what happens to the victim?** Odd message → jacking; loses data → snarfing; loses control → bugging.
- Fix: Bluetooth off when unused, non-discoverable, patched.

**On the exam**

- Wipe only work data from a personal phone → **containerization (selective wipe)**
- Enforce encryption + remote wipe → **MDM**
- Broken, never use → **WEP** · strongest → **WPA3**
- Unwanted messages → **bluejacking** · stealing contacts → **bluesnarfing** · taking control → **bluebugging**

**Quick check:** (1) Attacker silently copies contacts and messages over Bluetooth: which attack? (2) Protect work data on personal phones without controlling personal photos: approach?

**Answer:** Taught.

</details>

<a name="t-4-1-31"></a>
**BYOD and MDM**

Bring Your Own Device lets staff use personal devices; Mobile Device Management enforces policies on them (encryption, PIN, remote wipe, app control, containerization).

> On the exam: Scenario cue: 'a lost personal phone holds company email' → MDM remote wipe of the corporate container.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 12: Mobile threats + wireless (topics 30–33)**

**30. Mobile app threats**

- **Reverse engineering** (decompile; fix: obfuscation, no secrets in code); **jailbroken/rooted** devices (fix: jailbreak/root detection); insecure storage; weak TLS; malicious lookalike apps; over-broad permissions.
- **OWASP Mobile Top 10** lists them; **MASVS** verifies.

**31. BYOD and MDM**

- **BYOD** = personal devices for work; company doesn't control the device.
- **MDM** = manage/secure devices: enforce passcode, require encryption, push/block apps, **remote wipe**.
- **Containerization** = separate encrypted **work container** → **selective wipe** of work data only (privacy, trust).
- **MAM** = manage just work apps; **COPE** = corporate-owned, personally enabled.

**32. Location-based services**

- GPS/Wi-Fi/cell location = **highly sensitive** (home, work, health visits, habits).
- Requirements: **opt-in consent**, minimization, reduce precision (city not GPS), protect history, watch **spoofing**.

**33. Wireless and Bluetooth**

- Wi-Fi worst → best: **WEP** (broken, never use) → **WPA** (weak) → **WPA2** (AES; KRACK) → **WPA3** (current best; SAE).
- **Bluejacking** = sends unwanted messages, harmless (**jack = joke**).
- **Bluesnarfing** = **steals data** (contacts, messages, files) (**snarf = snatch**).
- **Bluebugging** = **takes control** (calls, listening) (**bug = boss of the phone**).
- **Test: what happens to the victim?** Odd message → jacking; loses data → snarfing; loses control → bugging.
- Fix: Bluetooth off when unused, non-discoverable, patched.

**On the exam**

- Wipe only work data from a personal phone → **containerization (selective wipe)**
- Enforce encryption + remote wipe → **MDM**
- Broken, never use → **WEP** · strongest → **WPA3**
- Unwanted messages → **bluejacking** · stealing contacts → **bluesnarfing** · taking control → **bluebugging**

**Quick check:** (1) Attacker silently copies contacts and messages over Bluetooth: which attack? (2) Protect work data on personal phones without controlling personal photos: approach?

**Answer:** Containerization. Correct.

</details>

<a name="t-4-1-32"></a>
**Location-based services**

Apps using GPS, Wi-Fi or cell location.

> On the exam: Risks: tracking and privacy violations, location spoofing. Controls: explicit consent, minimal precision, protect stored location history.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 12: Mobile threats + wireless (topics 30–33)**

**30. Mobile app threats**

- **Reverse engineering** (decompile; fix: obfuscation, no secrets in code); **jailbroken/rooted** devices (fix: jailbreak/root detection); insecure storage; weak TLS; malicious lookalike apps; over-broad permissions.
- **OWASP Mobile Top 10** lists them; **MASVS** verifies.

**31. BYOD and MDM**

- **BYOD** = personal devices for work; company doesn't control the device.
- **MDM** = manage/secure devices: enforce passcode, require encryption, push/block apps, **remote wipe**.
- **Containerization** = separate encrypted **work container** → **selective wipe** of work data only (privacy, trust).
- **MAM** = manage just work apps; **COPE** = corporate-owned, personally enabled.

**32. Location-based services**

- GPS/Wi-Fi/cell location = **highly sensitive** (home, work, health visits, habits).
- Requirements: **opt-in consent**, minimization, reduce precision (city not GPS), protect history, watch **spoofing**.

**33. Wireless and Bluetooth**

- Wi-Fi worst → best: **WEP** (broken, never use) → **WPA** (weak) → **WPA2** (AES; KRACK) → **WPA3** (current best; SAE).
- **Bluejacking** = sends unwanted messages, harmless (**jack = joke**).
- **Bluesnarfing** = **steals data** (contacts, messages, files) (**snarf = snatch**).
- **Bluebugging** = **takes control** (calls, listening) (**bug = boss of the phone**).
- **Test: what happens to the victim?** Odd message → jacking; loses data → snarfing; loses control → bugging.
- Fix: Bluetooth off when unused, non-discoverable, patched.

**On the exam**

- Wipe only work data from a personal phone → **containerization (selective wipe)**
- Enforce encryption + remote wipe → **MDM**
- Broken, never use → **WEP** · strongest → **WPA3**
- Unwanted messages → **bluejacking** · stealing contacts → **bluesnarfing** · taking control → **bluebugging**

**Quick check:** (1) Attacker silently copies contacts and messages over Bluetooth: which attack? (2) Protect work data on personal phones without controlling personal photos: approach?

**Answer:** Taught.

</details>

<a name="t-4-1-33"></a>
**Wireless and Bluetooth security**

Wi-Fi: WEP is broken; use WPA2 or WPA3 (with enterprise authentication where possible). Bluetooth attacks: bluejacking (unsolicited messages), bluesnarfing (stealing data), bluebugging (taking control).

> On the exam: Scenario cue: 'device still uses WEP' → upgrade to WPA2/WPA3; WEP can be cracked in minutes.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 12: Mobile threats + wireless (topics 30–33)**

**30. Mobile app threats**

- **Reverse engineering** (decompile; fix: obfuscation, no secrets in code); **jailbroken/rooted** devices (fix: jailbreak/root detection); insecure storage; weak TLS; malicious lookalike apps; over-broad permissions.
- **OWASP Mobile Top 10** lists them; **MASVS** verifies.

**31. BYOD and MDM**

- **BYOD** = personal devices for work; company doesn't control the device.
- **MDM** = manage/secure devices: enforce passcode, require encryption, push/block apps, **remote wipe**.
- **Containerization** = separate encrypted **work container** → **selective wipe** of work data only (privacy, trust).
- **MAM** = manage just work apps; **COPE** = corporate-owned, personally enabled.

**32. Location-based services**

- GPS/Wi-Fi/cell location = **highly sensitive** (home, work, health visits, habits).
- Requirements: **opt-in consent**, minimization, reduce precision (city not GPS), protect history, watch **spoofing**.

**33. Wireless and Bluetooth**

- Wi-Fi worst → best: **WEP** (broken, never use) → **WPA** (weak) → **WPA2** (AES; KRACK) → **WPA3** (current best; SAE).
- **Bluejacking** = sends unwanted messages, harmless (**jack = joke**).
- **Bluesnarfing** = **steals data** (contacts, messages, files) (**snarf = snatch**).
- **Bluebugging** = **takes control** (calls, listening) (**bug = boss of the phone**).
- **Test: what happens to the victim?** Odd message → jacking; loses data → snarfing; loses control → bugging.
- Fix: Bluetooth off when unused, non-discoverable, patched.

**On the exam**

- Wipe only work data from a personal phone → **containerization (selective wipe)**
- Enforce encryption + remote wipe → **MDM**
- Broken, never use → **WEP** · strongest → **WPA3**
- Unwanted messages → **bluejacking** · stealing contacts → **bluesnarfing** · taking control → **bluebugging**

**Quick check:** (1) Attacker silently copies contacts and messages over Bluetooth: which attack? (2) Protect work data on personal phones without controlling personal photos: approach?

**Answer:** I said bluejacking for copying data (answer: BLUESNARFING = snatch). Marked shaky.

</details>

<a name="t-4-1-34"></a>
**Cloud threats**

Data breaches and loss, account or traffic hijacking, insecure APIs, malicious insiders at the provider, abuse of cloud resources (attackers renting compute), denial of service, shared technology vulnerabilities, insufficient due diligence.

> On the exam: Scenario cue: 'company moved to the cloud without assessing the provider' → insufficient due diligence.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 10: Cloud part 2 (topics 25, 26, 34, 35)**

**25. NIST's 5 cloud characteristics (SP 800-145)**

1. **On-demand self-service** (create resources yourself, instantly)

2. **Broad network access** (from any device over the network)

3. **Resource pooling** (shared hardware = the idea behind multitenancy; "multitenancy" is NOT the official name)

4. **Rapid elasticity** (scale up/down quickly, automatically)

5. **Measured service** (pay for what you use)

**Mnemonic: "Our Big Rubber Raft Moves."**

**26. Cloud risks and CASB**

**CASB (Cloud Access Security Broker):** sits **between users and cloud services**, enforcing policy. 4 pillars: **visibility** (finds **shadow IT**), **compliance**, **data security** (DLP, encryption), **threat protection** (hacked accounts, unusual behavior). *A security guard at the door between your company and the cloud.*

**34. Cloud threats**

**Misconfiguration = #1 cause** (public buckets, open ports, broad permissions); insecure APIs; account hijacking (no MFA); insiders; lack of visibility. Fix: **CSPM** (auto-scan for misconfigurations), MFA, least privilege.

**35. Serverless and containers**

- **Serverless:** provider handles servers/OS; **you** own code, permissions, secrets. Risks: over-permissioned functions, **event injection**, vulnerable dependencies. Controls: least privilege per function, validate every event, vault.
- **Containers + Kubernetes:** risks: vulnerable base images, **running as root**, secrets baked into images, **container escape** (containers **share the host kernel** → less isolated than VMs). Controls: scan images, minimal base images, not root, K8s **RBAC + network policies**, secrets outside images.

**On the exam**

- Scale automatically → **rapid elasticity** · pay per use → **measured service**
- Discover unapproved cloud apps → **CASB** (shadow IT)
- Top cause of cloud breaches → **misconfiguration**
- Containers less isolated than VMs → **share the host kernel**
- **Trap:** serverless ≠ no security work.

**Quick check:** (1) Employees upload company files to personal Dropbox without IT knowing: which tool? (2) Name three NIST cloud characteristics.

**Answer:** Taught (known).

</details>

<a name="t-4-1-35"></a>
**Serverless and container orchestration**

Serverless (functions as a service): no servers to manage, but each function needs least-privilege permissions, input validation and secrets management. Orchestration (Kubernetes): secure the API server, use role-based access, network policies, pod security, and secrets.

> On the exam: Scenario cue: 'every function shares one admin role' → violates least privilege; give each function its own minimal role.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.1 Lesson 10: Cloud part 2 (topics 25, 26, 34, 35)**

**25. NIST's 5 cloud characteristics (SP 800-145)**

1. **On-demand self-service** (create resources yourself, instantly)

2. **Broad network access** (from any device over the network)

3. **Resource pooling** (shared hardware = the idea behind multitenancy; "multitenancy" is NOT the official name)

4. **Rapid elasticity** (scale up/down quickly, automatically)

5. **Measured service** (pay for what you use)

**Mnemonic: "Our Big Rubber Raft Moves."**

**26. Cloud risks and CASB**

**CASB (Cloud Access Security Broker):** sits **between users and cloud services**, enforcing policy. 4 pillars: **visibility** (finds **shadow IT**), **compliance**, **data security** (DLP, encryption), **threat protection** (hacked accounts, unusual behavior). *A security guard at the door between your company and the cloud.*

**34. Cloud threats**

**Misconfiguration = #1 cause** (public buckets, open ports, broad permissions); insecure APIs; account hijacking (no MFA); insiders; lack of visibility. Fix: **CSPM** (auto-scan for misconfigurations), MFA, least privilege.

**35. Serverless and containers**

- **Serverless:** provider handles servers/OS; **you** own code, permissions, secrets. Risks: over-permissioned functions, **event injection**, vulnerable dependencies. Controls: least privilege per function, validate every event, vault.
- **Containers + Kubernetes:** risks: vulnerable base images, **running as root**, secrets baked into images, **container escape** (containers **share the host kernel** → less isolated than VMs). Controls: scan images, minimal base images, not root, K8s **RBAC + network policies**, secrets outside images.

**On the exam**

- Scale automatically → **rapid elasticity** · pay per use → **measured service**
- Discover unapproved cloud apps → **CASB** (shadow IT)
- Top cause of cloud breaches → **misconfiguration**
- Containers less isolated than VMs → **share the host kernel**
- **Trap:** serverless ≠ no security work.

**Quick check:** (1) Employees upload company files to personal Dropbox without IT knowing: which tool? (2) Name three NIST cloud characteristics.

**Answer:** Taught (known).

</details>

## 4.2 Secure interface design

<a name="t-4-2-1"></a>
**Security management interfaces**

Admin consoles need strong authentication and restricted access.

> On the exam: What it is: admin consoles and APIs used to configure the system.
Controls: separate from user interfaces, strong authentication with MFA, restricted to admin networks, full logging.
Scenario cue: 'the admin panel is reachable from the internet' → move it to a management network or VPN.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 1: Admin, out-of-band, log and dependency interfaces (topics 1–4)**

**Interface** = any point where something talks to your system (person, program, system). **Attack surface** = all the doors.

**1. Security management interfaces**

Admin consoles, config dashboards, cloud portals, DB admin tools, router panels. They can **change everything** → compromise = owning the system.

- **MFA always**; restrict reach (**management network, VPN, IP allow-list**; never public internet)
- **Least privilege + separation of duties**; named admin accounts, no shared "admin"
- **PAM (privileged access management):** vault admin passwords, **just-in-time** access, **session recording**
- **Log every admin action** where admins can't erase it; separate admin UI from user UI
- Exposed admin panels + **default credentials** start many breaches.

**2. Out-of-band management**

**In-band** = same network as users. **Out-of-band (OOB)** = separate dedicated channel (management network, serial console, iDRAC/iLO management cards).

- **Availability:** still reachable during DDoS or network failure.
- **Security:** attackers on the user network can't see it.
- OOB must itself be protected (strong auth, restricted, patched; iDRAC/iLO have had serious vulns).

*Hook: staff-only back door with its own corridor.*

**3. Log interfaces**

How logs are sent, stored, accessed (central log server / **SIEM** = collects and analyzes logs).

- Attackers **delete/alter logs**; anyone-can-write = **poisoning**.
- **TLS in transit**, push off the machine fast; **append-only / WORM** storage; hash/sign batches.
- Only security staff read; **nobody (esp. admins) can edit/delete** = **separation of duties**.
- **No secrets in logs.** **Log injection** (fake lines via user input, e.g. newline in username) → encode/validate before logging.
- **NTP time sync** to correlate events.

*Hook: logs = camera footage; send it off-site fast; don't let the suspect hold the tape.*

**4. Upstream / downstream dependencies**

**Upstream** = systems you receive from; **downstream** = systems you send to.

- **Separate credentials per connection** (no shared master key: one breach exposes all, can't revoke without breaking all)
- Keys in a **vault**, **rotated**; **minimize** data sent downstream
- **Validate upstream data** even from internal systems; **mTLS** where it matters

**On the exam**

- Admin console on internet, password only → restrict network + **MFA**
- Admin access during DDoS → **out-of-band**
- Logs deleted after breach → **central append-only (WORM)**, restricted delete
- Username used to insert fake log lines → **log injection**
- One API key for all partners → **separate credentials per connection**
- **Traps:** OOB isn't automatically safe; internal upstream data still needs validation.

**Quick check:** (1) Why should admins not be able to delete their own servers' logs? (2) One API key for 12 partner integrations; one partner breached: problem + better design?

**Answer:** Camera footage, must not be changed (= separation of duties: admin could hide misuse). One breach exposes all 12; separate credentials per connection. Both correct. (Earlier light-mode check: out-of-band during DDoS, correct.)

</details>

<a name="t-4-2-2"></a>
**Out-of-band management**

A separate channel or network for administration.

> On the exam: What it is: managing systems through a separate network or channel, not the production network (e.g., dedicated management VLAN, console servers).
Why it matters: an attacker on the production network can't reach admin interfaces, and admins can still connect during an outage.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 1: Admin, out-of-band, log and dependency interfaces (topics 1–4)**

**Interface** = any point where something talks to your system (person, program, system). **Attack surface** = all the doors.

**1. Security management interfaces**

Admin consoles, config dashboards, cloud portals, DB admin tools, router panels. They can **change everything** → compromise = owning the system.

- **MFA always**; restrict reach (**management network, VPN, IP allow-list**; never public internet)
- **Least privilege + separation of duties**; named admin accounts, no shared "admin"
- **PAM (privileged access management):** vault admin passwords, **just-in-time** access, **session recording**
- **Log every admin action** where admins can't erase it; separate admin UI from user UI
- Exposed admin panels + **default credentials** start many breaches.

**2. Out-of-band management**

**In-band** = same network as users. **Out-of-band (OOB)** = separate dedicated channel (management network, serial console, iDRAC/iLO management cards).

- **Availability:** still reachable during DDoS or network failure.
- **Security:** attackers on the user network can't see it.
- OOB must itself be protected (strong auth, restricted, patched; iDRAC/iLO have had serious vulns).

*Hook: staff-only back door with its own corridor.*

**3. Log interfaces**

How logs are sent, stored, accessed (central log server / **SIEM** = collects and analyzes logs).

- Attackers **delete/alter logs**; anyone-can-write = **poisoning**.
- **TLS in transit**, push off the machine fast; **append-only / WORM** storage; hash/sign batches.
- Only security staff read; **nobody (esp. admins) can edit/delete** = **separation of duties**.
- **No secrets in logs.** **Log injection** (fake lines via user input, e.g. newline in username) → encode/validate before logging.
- **NTP time sync** to correlate events.

*Hook: logs = camera footage; send it off-site fast; don't let the suspect hold the tape.*

**4. Upstream / downstream dependencies**

**Upstream** = systems you receive from; **downstream** = systems you send to.

- **Separate credentials per connection** (no shared master key: one breach exposes all, can't revoke without breaking all)
- Keys in a **vault**, **rotated**; **minimize** data sent downstream
- **Validate upstream data** even from internal systems; **mTLS** where it matters

**On the exam**

- Admin console on internet, password only → restrict network + **MFA**
- Admin access during DDoS → **out-of-band**
- Logs deleted after breach → **central append-only (WORM)**, restricted delete
- Username used to insert fake log lines → **log injection**
- One API key for all partners → **separate credentials per connection**
- **Traps:** OOB isn't automatically safe; internal upstream data still needs validation.

**Quick check:** (1) Why should admins not be able to delete their own servers' logs? (2) One API key for 12 partner integrations; one partner breached: problem + better design?

**Answer:** Camera footage, must not be changed (= separation of duties: admin could hide misuse). One breach exposes all 12; separate credentials per connection. Both correct. (Earlier light-mode check: out-of-band during DDoS, correct.)

</details>

<a name="t-4-2-3"></a>
**Log interfaces**

Protect how logs are sent and accessed.

> On the exam: What it is: how logs are sent, stored and read.
Controls: encrypt in transit (TLS), restrict access, append-only storage, protect integrity, avoid logging sensitive data.
Scenario cue: 'logs are sent in clear text to a central server' → use encrypted, authenticated log transport.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 1: Admin, out-of-band, log and dependency interfaces (topics 1–4)**

**Interface** = any point where something talks to your system (person, program, system). **Attack surface** = all the doors.

**1. Security management interfaces**

Admin consoles, config dashboards, cloud portals, DB admin tools, router panels. They can **change everything** → compromise = owning the system.

- **MFA always**; restrict reach (**management network, VPN, IP allow-list**; never public internet)
- **Least privilege + separation of duties**; named admin accounts, no shared "admin"
- **PAM (privileged access management):** vault admin passwords, **just-in-time** access, **session recording**
- **Log every admin action** where admins can't erase it; separate admin UI from user UI
- Exposed admin panels + **default credentials** start many breaches.

**2. Out-of-band management**

**In-band** = same network as users. **Out-of-band (OOB)** = separate dedicated channel (management network, serial console, iDRAC/iLO management cards).

- **Availability:** still reachable during DDoS or network failure.
- **Security:** attackers on the user network can't see it.
- OOB must itself be protected (strong auth, restricted, patched; iDRAC/iLO have had serious vulns).

*Hook: staff-only back door with its own corridor.*

**3. Log interfaces**

How logs are sent, stored, accessed (central log server / **SIEM** = collects and analyzes logs).

- Attackers **delete/alter logs**; anyone-can-write = **poisoning**.
- **TLS in transit**, push off the machine fast; **append-only / WORM** storage; hash/sign batches.
- Only security staff read; **nobody (esp. admins) can edit/delete** = **separation of duties**.
- **No secrets in logs.** **Log injection** (fake lines via user input, e.g. newline in username) → encode/validate before logging.
- **NTP time sync** to correlate events.

*Hook: logs = camera footage; send it off-site fast; don't let the suspect hold the tape.*

**4. Upstream / downstream dependencies**

**Upstream** = systems you receive from; **downstream** = systems you send to.

- **Separate credentials per connection** (no shared master key: one breach exposes all, can't revoke without breaking all)
- Keys in a **vault**, **rotated**; **minimize** data sent downstream
- **Validate upstream data** even from internal systems; **mTLS** where it matters

**On the exam**

- Admin console on internet, password only → restrict network + **MFA**
- Admin access during DDoS → **out-of-band**
- Logs deleted after breach → **central append-only (WORM)**, restricted delete
- Username used to insert fake log lines → **log injection**
- One API key for all partners → **separate credentials per connection**
- **Traps:** OOB isn't automatically safe; internal upstream data still needs validation.

**Quick check:** (1) Why should admins not be able to delete their own servers' logs? (2) One API key for 12 partner integrations; one partner breached: problem + better design?

**Answer:** Camera footage, must not be changed (= separation of duties: admin could hide misuse). One breach exposes all 12; separate credentials per connection. Both correct. (Earlier light-mode check: out-of-band during DDoS, correct.)

</details>

<a name="t-4-2-4"></a>
**Upstream/downstream dependencies**

How keys and data are shared between connected apps.

> On the exam: What it is: systems your app sends data to (downstream) or receives from (upstream), sharing data and sometimes keys.
Risks: trusting input from upstream without validation, reusing keys across systems, one compromised system affecting others.
Scenario cue: 'two apps share the same encryption key' → compromise of one breaks both; use separate keys.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 1: Admin, out-of-band, log and dependency interfaces (topics 1–4)**

**Interface** = any point where something talks to your system (person, program, system). **Attack surface** = all the doors.

**1. Security management interfaces**

Admin consoles, config dashboards, cloud portals, DB admin tools, router panels. They can **change everything** → compromise = owning the system.

- **MFA always**; restrict reach (**management network, VPN, IP allow-list**; never public internet)
- **Least privilege + separation of duties**; named admin accounts, no shared "admin"
- **PAM (privileged access management):** vault admin passwords, **just-in-time** access, **session recording**
- **Log every admin action** where admins can't erase it; separate admin UI from user UI
- Exposed admin panels + **default credentials** start many breaches.

**2. Out-of-band management**

**In-band** = same network as users. **Out-of-band (OOB)** = separate dedicated channel (management network, serial console, iDRAC/iLO management cards).

- **Availability:** still reachable during DDoS or network failure.
- **Security:** attackers on the user network can't see it.
- OOB must itself be protected (strong auth, restricted, patched; iDRAC/iLO have had serious vulns).

*Hook: staff-only back door with its own corridor.*

**3. Log interfaces**

How logs are sent, stored, accessed (central log server / **SIEM** = collects and analyzes logs).

- Attackers **delete/alter logs**; anyone-can-write = **poisoning**.
- **TLS in transit**, push off the machine fast; **append-only / WORM** storage; hash/sign batches.
- Only security staff read; **nobody (esp. admins) can edit/delete** = **separation of duties**.
- **No secrets in logs.** **Log injection** (fake lines via user input, e.g. newline in username) → encode/validate before logging.
- **NTP time sync** to correlate events.

*Hook: logs = camera footage; send it off-site fast; don't let the suspect hold the tape.*

**4. Upstream / downstream dependencies**

**Upstream** = systems you receive from; **downstream** = systems you send to.

- **Separate credentials per connection** (no shared master key: one breach exposes all, can't revoke without breaking all)
- Keys in a **vault**, **rotated**; **minimize** data sent downstream
- **Validate upstream data** even from internal systems; **mTLS** where it matters

**On the exam**

- Admin console on internet, password only → restrict network + **MFA**
- Admin access during DDoS → **out-of-band**
- Logs deleted after breach → **central append-only (WORM)**, restricted delete
- Username used to insert fake log lines → **log injection**
- One API key for all partners → **separate credentials per connection**
- **Traps:** OOB isn't automatically safe; internal upstream data still needs validation.

**Quick check:** (1) Why should admins not be able to delete their own servers' logs? (2) One API key for 12 partner integrations; one partner breached: problem + better design?

**Answer:** Camera footage, must not be changed (= separation of duties: admin could hide misuse). One breach exposes all 12; separate credentials per connection. Both correct. (Earlier light-mode check: out-of-band during DDoS, correct.)

</details>

<a name="t-4-2-5"></a>
**API design** (review)

Authentication, authorization per call, rate limiting, input validation, versioning.

> On the exam: Common flaws: broken object-level authorization, missing rate limits, excessive data exposure (OWASP API Top 10).

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 2: APIs, sessions, messages, browsers (topics 5–8)**

**5. API design (APIs = #1 way modern apps get attacked)**

- **Authenticate every caller** (OAuth 2.0/JWT, API keys + stronger, mTLS).
- **Authorize every call, on every object.** **BOLA (Broken Object Level Authorization) = #1 in OWASP API Security Top 10** (= IDOR): `/orders/1002` → `/orders/1003` shows someone else's. Checked "logged in?" not "is this yours?" Fix: **object-level authorization on every call**.
- **Validate all input**; **return only needed data** (excessive data exposure); **rate limiting/quotas**; **versioning** + **retire old versions** (shadow/zombie APIs); **API gateway**; **inventory every API**.

*Hook: "logged in" ≠ "allowed to see this."*

**6. Stateful vs stateless**

- **Stateful** = server remembers you (session + session ID cookie). **Stateless** = every request carries a **token** (JWT). REST = stateless.
- **Sessions:** hijacking → cookies **Secure**, **HttpOnly** (JS can't read; blocks XSS theft), **SameSite** (blocks CSRF). **Session fixation** → **new session ID at login**. Idle + absolute timeouts; destroy server session on logout; random long IDs.
- **JWT:** verify signature server-side, reject **`alg: none`**; short expiry + refresh tokens; **hard to revoke**; **signed ≠ encrypted** → anyone can READ it, no private data inside; store safely.

*Hook: stateful = coat ticket; stateless = ID card.*

**7. Secure messaging**

- **Encryption** (confidentiality) · **MAC/HMAC** (integrity + origin, shared key, NO nonrepudiation) · **digital signature** (nonrepudiation) · **timestamps/nonces** (no replay; encryption alone doesn't stop replay).
- **TLS = one hop; message-level** (WS-Security, sign + encrypt payload) protects through every hop.

*Hook: encrypt = can't read; sign = can't fake; nonce = can't reuse.*

**8. Same-origin policy and CORS**

- **Origin = scheme + host + port** (path doesn't matter; subdomain = different; port = different).
- **SOP:** can't READ another origin's responses (can often still SEND → why CSRF exists).
- **CORS:** server lists allowed origins (`Access-Control-Allow-Origin`); **preflight OPTIONS**.
- Misconfigs: `*` on private data; **reflecting any origin**; credentials + broad origins. CORS **loosens** SOP.

**On the exam**

- Change ID in API URL → others' data → **BOLA/IDOR** → object-level authz (NOT an HttpOnly issue: nothing is stolen)
- Old v1 API without new controls → **zombie/shadow API**
- Session ID unchanged after login → **session fixation** · cookie readable by JS → missing **HttpOnly**
- Stolen JWT works after logout → hard to revoke → short expiry
- Protected through intermediaries → **message-level**
- `https://app.com` vs `https://api.app.com` → **different origin** · private API with `*` → **CORS misconfig**

**Quick check:** (1) User changes /api/invoices/551 to 552 and sees another customer's invoice: flaw + fix? (2) https://bank.com vs https://bank.com:8443 same origin? (3) JWT holds home address 'because it's signed': what's wrong?

**Answer:** I said missing HttpOnly; answer BOLA/IDOR, fix object-level authorization on every call. Marked shaky.

</details>

<a name="t-4-2-6"></a>
**Stateful vs stateless protocols**

Stateless (REST) needs a token on every request; stateful needs secure session handling.

> On the exam: Stateful: server remembers each client's session (traditional web sessions), needs secure session management. Stateless: each request carries everything needed (REST with tokens), so tokens must be signed, short-lived and validated every time.
Scenario cue: 'stolen JWT works for days' → expiry too long, no revocation strategy.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 2: APIs, sessions, messages, browsers (topics 5–8)**

**5. API design (APIs = #1 way modern apps get attacked)**

- **Authenticate every caller** (OAuth 2.0/JWT, API keys + stronger, mTLS).
- **Authorize every call, on every object.** **BOLA (Broken Object Level Authorization) = #1 in OWASP API Security Top 10** (= IDOR): `/orders/1002` → `/orders/1003` shows someone else's. Checked "logged in?" not "is this yours?" Fix: **object-level authorization on every call**.
- **Validate all input**; **return only needed data** (excessive data exposure); **rate limiting/quotas**; **versioning** + **retire old versions** (shadow/zombie APIs); **API gateway**; **inventory every API**.

*Hook: "logged in" ≠ "allowed to see this."*

**6. Stateful vs stateless**

- **Stateful** = server remembers you (session + session ID cookie). **Stateless** = every request carries a **token** (JWT). REST = stateless.
- **Sessions:** hijacking → cookies **Secure**, **HttpOnly** (JS can't read; blocks XSS theft), **SameSite** (blocks CSRF). **Session fixation** → **new session ID at login**. Idle + absolute timeouts; destroy server session on logout; random long IDs.
- **JWT:** verify signature server-side, reject **`alg: none`**; short expiry + refresh tokens; **hard to revoke**; **signed ≠ encrypted** → anyone can READ it, no private data inside; store safely.

*Hook: stateful = coat ticket; stateless = ID card.*

**7. Secure messaging**

- **Encryption** (confidentiality) · **MAC/HMAC** (integrity + origin, shared key, NO nonrepudiation) · **digital signature** (nonrepudiation) · **timestamps/nonces** (no replay; encryption alone doesn't stop replay).
- **TLS = one hop; message-level** (WS-Security, sign + encrypt payload) protects through every hop.

*Hook: encrypt = can't read; sign = can't fake; nonce = can't reuse.*

**8. Same-origin policy and CORS**

- **Origin = scheme + host + port** (path doesn't matter; subdomain = different; port = different).
- **SOP:** can't READ another origin's responses (can often still SEND → why CSRF exists).
- **CORS:** server lists allowed origins (`Access-Control-Allow-Origin`); **preflight OPTIONS**.
- Misconfigs: `*` on private data; **reflecting any origin**; credentials + broad origins. CORS **loosens** SOP.

**On the exam**

- Change ID in API URL → others' data → **BOLA/IDOR** → object-level authz (NOT an HttpOnly issue: nothing is stolen)
- Old v1 API without new controls → **zombie/shadow API**
- Session ID unchanged after login → **session fixation** · cookie readable by JS → missing **HttpOnly**
- Stolen JWT works after logout → hard to revoke → short expiry
- Protected through intermediaries → **message-level**
- `https://app.com` vs `https://api.app.com` → **different origin** · private API with `*` → **CORS misconfig**

**Quick check:** (1) User changes /api/invoices/551 to 552 and sees another customer's invoice: flaw + fix? (2) https://bank.com vs https://bank.com:8443 same origin? (3) JWT holds home address 'because it's signed': what's wrong?

**Answer:** JWT: signed not encrypted, readable. Correct.

</details>

<a name="t-4-2-7"></a>
**Secure messaging**

Protecting messages end to end: encryption for confidentiality, signatures or MACs for integrity and origin, timestamps or nonces against replay.

> On the exam: Don't confuse: transport security (TLS) protects one hop; message-level security protects the message across intermediaries.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 2: APIs, sessions, messages, browsers (topics 5–8)**

**5. API design (APIs = #1 way modern apps get attacked)**

- **Authenticate every caller** (OAuth 2.0/JWT, API keys + stronger, mTLS).
- **Authorize every call, on every object.** **BOLA (Broken Object Level Authorization) = #1 in OWASP API Security Top 10** (= IDOR): `/orders/1002` → `/orders/1003` shows someone else's. Checked "logged in?" not "is this yours?" Fix: **object-level authorization on every call**.
- **Validate all input**; **return only needed data** (excessive data exposure); **rate limiting/quotas**; **versioning** + **retire old versions** (shadow/zombie APIs); **API gateway**; **inventory every API**.

*Hook: "logged in" ≠ "allowed to see this."*

**6. Stateful vs stateless**

- **Stateful** = server remembers you (session + session ID cookie). **Stateless** = every request carries a **token** (JWT). REST = stateless.
- **Sessions:** hijacking → cookies **Secure**, **HttpOnly** (JS can't read; blocks XSS theft), **SameSite** (blocks CSRF). **Session fixation** → **new session ID at login**. Idle + absolute timeouts; destroy server session on logout; random long IDs.
- **JWT:** verify signature server-side, reject **`alg: none`**; short expiry + refresh tokens; **hard to revoke**; **signed ≠ encrypted** → anyone can READ it, no private data inside; store safely.

*Hook: stateful = coat ticket; stateless = ID card.*

**7. Secure messaging**

- **Encryption** (confidentiality) · **MAC/HMAC** (integrity + origin, shared key, NO nonrepudiation) · **digital signature** (nonrepudiation) · **timestamps/nonces** (no replay; encryption alone doesn't stop replay).
- **TLS = one hop; message-level** (WS-Security, sign + encrypt payload) protects through every hop.

*Hook: encrypt = can't read; sign = can't fake; nonce = can't reuse.*

**8. Same-origin policy and CORS**

- **Origin = scheme + host + port** (path doesn't matter; subdomain = different; port = different).
- **SOP:** can't READ another origin's responses (can often still SEND → why CSRF exists).
- **CORS:** server lists allowed origins (`Access-Control-Allow-Origin`); **preflight OPTIONS**.
- Misconfigs: `*` on private data; **reflecting any origin**; credentials + broad origins. CORS **loosens** SOP.

**On the exam**

- Change ID in API URL → others' data → **BOLA/IDOR** → object-level authz (NOT an HttpOnly issue: nothing is stolen)
- Old v1 API without new controls → **zombie/shadow API**
- Session ID unchanged after login → **session fixation** · cookie readable by JS → missing **HttpOnly**
- Stolen JWT works after logout → hard to revoke → short expiry
- Protected through intermediaries → **message-level**
- `https://app.com` vs `https://api.app.com` → **different origin** · private API with `*` → **CORS misconfig**

**Quick check:** (1) User changes /api/invoices/551 to 552 and sees another customer's invoice: flaw + fix? (2) https://bank.com vs https://bank.com:8443 same origin? (3) JWT holds home address 'because it's signed': what's wrong?

**Answer:** Sign = can't fake; correct.

</details>

<a name="t-4-2-8"></a>
**Same-origin policy and CORS**

Browsers block scripts from one origin (scheme + host + port) reading data from another. CORS lets a server explicitly allow specific other origins.

> On the exam: Trap: 'Access-Control-Allow-Origin: *' with credentials, or reflecting any origin, opens data to any website.
Scenario cue: 'a malicious site reads the user's account data through the API' → CORS misconfiguration.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.2 Lesson 2: APIs, sessions, messages, browsers (topics 5–8)**

**5. API design (APIs = #1 way modern apps get attacked)**

- **Authenticate every caller** (OAuth 2.0/JWT, API keys + stronger, mTLS).
- **Authorize every call, on every object.** **BOLA (Broken Object Level Authorization) = #1 in OWASP API Security Top 10** (= IDOR): `/orders/1002` → `/orders/1003` shows someone else's. Checked "logged in?" not "is this yours?" Fix: **object-level authorization on every call**.
- **Validate all input**; **return only needed data** (excessive data exposure); **rate limiting/quotas**; **versioning** + **retire old versions** (shadow/zombie APIs); **API gateway**; **inventory every API**.

*Hook: "logged in" ≠ "allowed to see this."*

**6. Stateful vs stateless**

- **Stateful** = server remembers you (session + session ID cookie). **Stateless** = every request carries a **token** (JWT). REST = stateless.
- **Sessions:** hijacking → cookies **Secure**, **HttpOnly** (JS can't read; blocks XSS theft), **SameSite** (blocks CSRF). **Session fixation** → **new session ID at login**. Idle + absolute timeouts; destroy server session on logout; random long IDs.
- **JWT:** verify signature server-side, reject **`alg: none`**; short expiry + refresh tokens; **hard to revoke**; **signed ≠ encrypted** → anyone can READ it, no private data inside; store safely.

*Hook: stateful = coat ticket; stateless = ID card.*

**7. Secure messaging**

- **Encryption** (confidentiality) · **MAC/HMAC** (integrity + origin, shared key, NO nonrepudiation) · **digital signature** (nonrepudiation) · **timestamps/nonces** (no replay; encryption alone doesn't stop replay).
- **TLS = one hop; message-level** (WS-Security, sign + encrypt payload) protects through every hop.

*Hook: encrypt = can't read; sign = can't fake; nonce = can't reuse.*

**8. Same-origin policy and CORS**

- **Origin = scheme + host + port** (path doesn't matter; subdomain = different; port = different).
- **SOP:** can't READ another origin's responses (can often still SEND → why CSRF exists).
- **CORS:** server lists allowed origins (`Access-Control-Allow-Origin`); **preflight OPTIONS**.
- Misconfigs: `*` on private data; **reflecting any origin**; credentials + broad origins. CORS **loosens** SOP.

**On the exam**

- Change ID in API URL → others' data → **BOLA/IDOR** → object-level authz (NOT an HttpOnly issue: nothing is stolen)
- Old v1 API without new controls → **zombie/shadow API**
- Session ID unchanged after login → **session fixation** · cookie readable by JS → missing **HttpOnly**
- Stolen JWT works after logout → hard to revoke → short expiry
- Protected through intermediaries → **message-level**
- `https://app.com` vs `https://api.app.com` → **different origin** · private API with `*` → **CORS misconfig**

**Quick check:** (1) User changes /api/invoices/551 to 552 and sees another customer's invoice: flaw + fix? (2) https://bank.com vs https://bank.com:8443 same origin? (3) JWT holds home address 'because it's signed': what's wrong?

**Answer:** Different port = different origin. Correct.

</details>

## 4.3 Reusable technologies

<a name="t-4-3-1"></a>
**X.509 and PKI**

Certificates binding identity to public key; CA, RA, CRL and OCSP for revocation.

> On the exam: CA signs certificates; RA verifies identity. A CRL is a list that can be stale; OCSP checks in real time.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 1: PKI and digital certificates (topics 1 + 19)**

**Why PKI exists**

Asymmetric crypto: **public key** shared, **private key** secret. Problem: how do you know a public key really belongs to the bank? → a **digital certificate**: a trusted third party vouches the **public key belongs to this identity**.

**The PKI cast**

- **CA (Certificate Authority):** **issues and signs** certificates (DigiCert, Let's Encrypt).
  - **Root CA:** top of trust chain; **self-signed**; in OS/browser **trust store**; private key kept **OFFLINE**, often in an **HSM**.
  - **Intermediate (subordinate) CA:** signed by root; does day-to-day issuing; if compromised, only it is revoked.
- **RA (Registration Authority):** **checks identity**, then tells the CA to issue. **RA verifies; CA signs.**
- **Chain of trust:** site cert → intermediate CA → root CA (trust store).
- **Repository:** publishes certs + revocation info.

**What's inside an X.509 (v3) certificate**

Subject (who) · Issuer (which CA) · **subject's PUBLIC key** · serial number · validity (not before / not after) · signature algorithm + **CA's signature** · extensions: **SAN** (extra domain names), **key usage**, **basic constraints** (may it act as a CA? website cert = no).

**A certificate contains the PUBLIC key (that's its purpose), NEVER the private key.**

**Lifecycle**

Generate key pair (private stays with you) → **CSR** (certificate signing request) → RA verifies, CA signs → use → renew → **revoke** early if needed (private key stolen, name change).

**Revocation**

- **CRL:** CA publishes a **list** of revoked serials, **periodically** (big, can be stale).
- **OCSP:** browser **asks in real time** (good / revoked / unknown); downsides: delay, privacy leak, often **fails open** if down.
- **OCSP stapling:** the **website** attaches a fresh OCSP response to the TLS handshake (faster, private, reliable).

**Validation levels**

**DV** (controls the domain; Let's Encrypt) · **OV** (organization checked) · **EV** (strictest).

**Other**

- **Self-signed** cert: no CA vouching; OK for internal testing; browsers warn publicly (root certs are self-signed but pre-installed).
- **Certificate pinning** (4.1). **Private keys in HSM/vault**; stolen private key = impersonation until revoked → revoke + new key pair + new cert.

**On the exam**

- Verifies identity before issuing → **RA** · issues and signs → **CA**
- Real-time revocation check → **OCSP** · periodic list → **CRL** · site attaches status → **OCSP stapling**
- Extra domain names → **SAN** · root CA key → **offline in an HSM**
- **Traps:** certificate holds the PUBLIC key, never the private key; valid signature + dates ≠ trustworthy (could be revoked).

**Hooks**

**CA = passport office; RA = clerk checking your documents. Certificate = ID card showing your public key, stamped by the office. CRL = printed list of stolen passports; OCSP = phone call to check one now; stapling = you bring a fresh letter. Root CA = boss locked in the vault; intermediates = managers doing daily work.**

**Quick check:** (1) Web server private key stolen: what must happen to its certificate, how do browsers find out? (2) Who checks a requester's identity, who signs the certificate?

**Answer:** RA checks, CA signs (final answer). Correct.

</details>

<a name="t-4-3-2"></a>
**Forward vs reverse proxy**

Forward proxy serves clients; reverse proxy protects servers.

> On the exam: Forward proxy: sits in front of clients, controls and filters their outbound traffic (web filtering).
Reverse proxy: sits in front of servers, hides them, balances load, terminates TLS, can host a WAF.
Scenario cue: 'protect and hide internal web servers from the internet' → reverse proxy.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 2: Proxies, firewalls and DLP (topics 2, 3, 4)**

**2. Forward vs reverse proxy**

- **Forward proxy** = in front of **clients/users**; outbound traffic; filter sites, scan downloads, log, hide internal IPs (corporate web gateway).
- **Reverse proxy** = in front of **servers**; inbound traffic; hide real servers, **TLS termination**, load balancing, caching, often hosts the **WAF** (Nginx, Cloudflare, cloud LB).

*Hook: forward = protects users going out; reverse = protects servers taking traffic in.*

**3. Firewalls (by depth; L3 = IP, L4 = ports, L7 = application content)**

1. **Packet-filtering (stateless)** L3–4: each packet alone (IP, port, protocol); no memory; fast, easy to fool.

2. **Stateful inspection** L3–4 + **state table** of open connections → knows legit replies; the standard network firewall.

3. **Application-level (proxy)** L7: understands HTTP/FTP/DNS, inspects **content**, splits the connection; deepest, slower.

4. **NGFW**: stateful + app awareness + **IPS** + user identity.

5. **WAF** L7 for web apps: blocks **SQLi, XSS**, bots (OWASP Core Rule Set); in front of web apps / on reverse proxy. **Compensating layer, not a fix**: real SQLi fix = **parameterized queries**; WAF = **virtual patching** to buy time.

Clues: IP + port only → packet filter · tracks connections → **stateful** · inspects HTTP/FTP content as proxy → application-level · blocks SQLi/XSS → WAF.

**4. Data loss prevention (DLP)**

Find sensitive data and stop it leaving.

- **At rest** = **scan storage** to DISCOVER (file shares, DBs, buckets) — librarian finding files.
- **In motion (network)** = watch traffic leaving (email, uploads, transfers); block/encrypt — guard at the exit gate.
- **In use (ENDPOINT)** = agent on laptops: copy/paste, **USB**, printing, screenshots — supervisor watching your hands.
- Recognition: patterns (regex), keywords + classification labels, **fingerprinting**, exact data matching.
- Challenges: false positives/negatives; **can't see encrypted traffic** without TLS inspection.

**On the exam**

- Hides web servers + terminates TLS → **reverse proxy** · filters employees' browsing → **forward proxy**
- Remembers connections → **stateful** · SQLi protection before code fix → **WAF** (virtual patching)
- Emailing card numbers out → **DLP in motion** · find SSNs on shares → **DLP at rest** · copy to USB → **endpoint DLP**
- **Traps:** WAF ≠ secure code; DLP blind to encrypted traffic without decryption.

**Hooks**

**Firewalls: stateless = checks the envelope, stateful = remembers the conversation, application = reads the letter, WAF = reads web letters for web attacks. DLP = the bag check at the exit.**

**Quick check:** (1) SQLi flaw, fix takes 3 weeks: what protects meanwhile, why not permanent? (2) Firewall with a table of open connections? (3) Employee copies SSN spreadsheet to USB: which DLP?

**Answer:** Taught.

</details>

<a name="t-4-3-3"></a>
**Firewalls** (review)

Packet filter, stateful, application-level, web application firewall (WAF).

> On the exam: Packet filter: IP and port only. Stateful: tracks connections. WAF: understands HTTP and blocks attacks like SQLi and XSS.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 2: Proxies, firewalls and DLP (topics 2, 3, 4)**

**2. Forward vs reverse proxy**

- **Forward proxy** = in front of **clients/users**; outbound traffic; filter sites, scan downloads, log, hide internal IPs (corporate web gateway).
- **Reverse proxy** = in front of **servers**; inbound traffic; hide real servers, **TLS termination**, load balancing, caching, often hosts the **WAF** (Nginx, Cloudflare, cloud LB).

*Hook: forward = protects users going out; reverse = protects servers taking traffic in.*

**3. Firewalls (by depth; L3 = IP, L4 = ports, L7 = application content)**

1. **Packet-filtering (stateless)** L3–4: each packet alone (IP, port, protocol); no memory; fast, easy to fool.

2. **Stateful inspection** L3–4 + **state table** of open connections → knows legit replies; the standard network firewall.

3. **Application-level (proxy)** L7: understands HTTP/FTP/DNS, inspects **content**, splits the connection; deepest, slower.

4. **NGFW**: stateful + app awareness + **IPS** + user identity.

5. **WAF** L7 for web apps: blocks **SQLi, XSS**, bots (OWASP Core Rule Set); in front of web apps / on reverse proxy. **Compensating layer, not a fix**: real SQLi fix = **parameterized queries**; WAF = **virtual patching** to buy time.

Clues: IP + port only → packet filter · tracks connections → **stateful** · inspects HTTP/FTP content as proxy → application-level · blocks SQLi/XSS → WAF.

**4. Data loss prevention (DLP)**

Find sensitive data and stop it leaving.

- **At rest** = **scan storage** to DISCOVER (file shares, DBs, buckets) — librarian finding files.
- **In motion (network)** = watch traffic leaving (email, uploads, transfers); block/encrypt — guard at the exit gate.
- **In use (ENDPOINT)** = agent on laptops: copy/paste, **USB**, printing, screenshots — supervisor watching your hands.
- Recognition: patterns (regex), keywords + classification labels, **fingerprinting**, exact data matching.
- Challenges: false positives/negatives; **can't see encrypted traffic** without TLS inspection.

**On the exam**

- Hides web servers + terminates TLS → **reverse proxy** · filters employees' browsing → **forward proxy**
- Remembers connections → **stateful** · SQLi protection before code fix → **WAF** (virtual patching)
- Emailing card numbers out → **DLP in motion** · find SSNs on shares → **DLP at rest** · copy to USB → **endpoint DLP**
- **Traps:** WAF ≠ secure code; DLP blind to encrypted traffic without decryption.

**Hooks**

**Firewalls: stateless = checks the envelope, stateful = remembers the conversation, application = reads the letter, WAF = reads web letters for web attacks. DLP = the bag check at the exit.**

**Quick check:** (1) SQLi flaw, fix takes 3 weeks: what protects meanwhile, why not permanent? (2) Firewall with a table of open connections? (3) Employee copies SSN spreadsheet to USB: which DLP?

**Answer:** WAF + parameterized queries correct; state-table firewall answer lost (STATEFUL). Marked shaky.

</details>

<a name="t-4-3-4"></a>
**Data loss prevention (DLP)** (review)

Detects and blocks sensitive data leaving, at rest, in motion, in use.

> On the exam: What it is: tools that find sensitive data and stop it leaving: at rest (scanning storage), in motion (network, email), in use (endpoints: copy, print, USB).
Scenario cue: 'employees email customer lists to personal accounts' → network/email DLP.
Trap: DLP depends on data classification to know what's sensitive.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 2: Proxies, firewalls and DLP (topics 2, 3, 4)**

**2. Forward vs reverse proxy**

- **Forward proxy** = in front of **clients/users**; outbound traffic; filter sites, scan downloads, log, hide internal IPs (corporate web gateway).
- **Reverse proxy** = in front of **servers**; inbound traffic; hide real servers, **TLS termination**, load balancing, caching, often hosts the **WAF** (Nginx, Cloudflare, cloud LB).

*Hook: forward = protects users going out; reverse = protects servers taking traffic in.*

**3. Firewalls (by depth; L3 = IP, L4 = ports, L7 = application content)**

1. **Packet-filtering (stateless)** L3–4: each packet alone (IP, port, protocol); no memory; fast, easy to fool.

2. **Stateful inspection** L3–4 + **state table** of open connections → knows legit replies; the standard network firewall.

3. **Application-level (proxy)** L7: understands HTTP/FTP/DNS, inspects **content**, splits the connection; deepest, slower.

4. **NGFW**: stateful + app awareness + **IPS** + user identity.

5. **WAF** L7 for web apps: blocks **SQLi, XSS**, bots (OWASP Core Rule Set); in front of web apps / on reverse proxy. **Compensating layer, not a fix**: real SQLi fix = **parameterized queries**; WAF = **virtual patching** to buy time.

Clues: IP + port only → packet filter · tracks connections → **stateful** · inspects HTTP/FTP content as proxy → application-level · blocks SQLi/XSS → WAF.

**4. Data loss prevention (DLP)**

Find sensitive data and stop it leaving.

- **At rest** = **scan storage** to DISCOVER (file shares, DBs, buckets) — librarian finding files.
- **In motion (network)** = watch traffic leaving (email, uploads, transfers); block/encrypt — guard at the exit gate.
- **In use (ENDPOINT)** = agent on laptops: copy/paste, **USB**, printing, screenshots — supervisor watching your hands.
- Recognition: patterns (regex), keywords + classification labels, **fingerprinting**, exact data matching.
- Challenges: false positives/negatives; **can't see encrypted traffic** without TLS inspection.

**On the exam**

- Hides web servers + terminates TLS → **reverse proxy** · filters employees' browsing → **forward proxy**
- Remembers connections → **stateful** · SQLi protection before code fix → **WAF** (virtual patching)
- Emailing card numbers out → **DLP in motion** · find SSNs on shares → **DLP at rest** · copy to USB → **endpoint DLP**
- **Traps:** WAF ≠ secure code; DLP blind to encrypted traffic without decryption.

**Hooks**

**Firewalls: stateless = checks the envelope, stateful = remembers the conversation, application = reads the letter, WAF = reads web letters for web attacks. DLP = the bag check at the exit.**

**Quick check:** (1) SQLi flaw, fix takes 3 weeks: what protects meanwhile, why not permanent? (2) Firewall with a table of open connections? (3) Employee copies SSN spreadsheet to USB: which DLP?

**Answer:** I wavered rest/endpoint; USB = ENDPOINT DLP (in use). Marked shaky.

</details>

<a name="t-4-3-5"></a>
**Hypervisors**

Type 1 (bare metal) vs Type 2 (hosted); VM escape risk.

> On the exam: Type 1 (bare-metal): runs directly on hardware (ESXi, Hyper-V); smaller attack surface, used in data centers. Type 2 (hosted): runs on an OS (VirtualBox).
Risks: VM escape (attacker breaks out to the host), VM sprawl, insecure snapshots.
Scenario cue: 'which is more secure for production?' → Type 1.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 3: Virtualization and infrastructure (topics 5, 6, 20, 7)**

Layers of isolation, and what breaks through them.

**5. Hypervisors**

**Hypervisor (VMM)** creates/runs VMs.

- **Type 1 (bare metal):** directly on hardware, no host OS (ESXi, Hyper-V, Xen, KVM). **More secure + faster**; data centers/cloud.
- **Type 2 (hosted):** an app on a normal OS (VirtualBox, VMware Workstation, Parallels). **Less secure** (host OS compromise exposes all VMs); desktops/testing.
- **VM escape:** code in a VM breaks out to the hypervisor → other VMs/host; worst case in multitenant cloud.

*Hook: Type 1 = the foundation; Type 2 = renting a room in someone else's house.*

**6. Containers**

- **Share the host kernel** (VMs have their own OS) → one kernel flaw hits all (**container escape**).
- Image: **scan**, minimal base, **sign + verify**, trusted registries. Runtime: **not root**, read-only FS, drop capabilities, resource limits. No secrets in images.

*VM = separate house; container = apartment (shared foundation).*

**20. Virtualization security**

- **VM escape** · **VM sprawl** (forgotten, unpatched, ownerless VMs → inventory, owners, lifecycle policies)
- **Insecure snapshots:** whole VM state incl. **memory** (passwords, keys, decrypted data) → encrypt, restrict, delete old (remanence)
- **Hypervisor = high-value target** → patch, restrict + monitor admin access
- **Inter-VM traffic blind spots** (never crosses a physical network) → **virtual firewalls / microsegmentation**
- **Noisy neighbor** resource exhaustion (availability)

**7. Infrastructure as code (IaC)**

Infrastructure in templates (Terraform, CloudFormation, Ansible).

- Benefits: **repeatable** (baseline), **version-controlled + reviewed** (change mgmt), **scannable before deploy** (public bucket, open 22, `*` permissions) = **policy as code**.
- Risks: secrets in templates (vault + scanning); bad template spreads everywhere (review + gates); **configuration drift** (manual live change) → **drift detection + re-apply the template**; needed changes go **in the code** via review. **Immutable infrastructure** = replace, don't patch live.

**On the exam**

- On hardware, cloud → **Type 1** · app on desktop OS → **Type 2**
- Breaks out to host → **VM escape** · forgotten VMs → **VM sprawl**
- Snapshot has passwords from memory → **insecure snapshots**
- Inter-VM traffic unseen → microsegmentation · containers less isolated → **share kernel**
- Scan Terraform before deploy → **IaC scanning / policy as code**
- Live servers ≠ IaC → **drift** → re-apply template
- **Trap:** Type 2 is LESS secure.

**Hooks**

**Type 1 = foundation; Type 2 = renting a room. Snapshot = a photo of the whole VM incl. memory secrets. IaC drift → restore from the code, never edit the code to match the drift.**

**Quick check:** (1) Max isolation + performance for customer VMs: which hypervisor type? (2) Prod VM snapshots on a shared drive: risk? (3) Port 22 opened manually on a Terraform-managed server: name + fix?

**Answer:** Type 1, directly on hardware. Correct.

</details>

<a name="t-4-3-6"></a>
**Containers**

Lighter isolation sharing the host kernel; scan and sign images.

> On the exam: Containers share the host kernel, so isolation is weaker than VMs.
Controls: minimal, signed base images; scan images; don't run as root; read-only file systems; limit capabilities; keep secrets out of images.
Scenario cue: 'a container escape compromises the host' → running privileged containers.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 3: Virtualization and infrastructure (topics 5, 6, 20, 7)**

Layers of isolation, and what breaks through them.

**5. Hypervisors**

**Hypervisor (VMM)** creates/runs VMs.

- **Type 1 (bare metal):** directly on hardware, no host OS (ESXi, Hyper-V, Xen, KVM). **More secure + faster**; data centers/cloud.
- **Type 2 (hosted):** an app on a normal OS (VirtualBox, VMware Workstation, Parallels). **Less secure** (host OS compromise exposes all VMs); desktops/testing.
- **VM escape:** code in a VM breaks out to the hypervisor → other VMs/host; worst case in multitenant cloud.

*Hook: Type 1 = the foundation; Type 2 = renting a room in someone else's house.*

**6. Containers**

- **Share the host kernel** (VMs have their own OS) → one kernel flaw hits all (**container escape**).
- Image: **scan**, minimal base, **sign + verify**, trusted registries. Runtime: **not root**, read-only FS, drop capabilities, resource limits. No secrets in images.

*VM = separate house; container = apartment (shared foundation).*

**20. Virtualization security**

- **VM escape** · **VM sprawl** (forgotten, unpatched, ownerless VMs → inventory, owners, lifecycle policies)
- **Insecure snapshots:** whole VM state incl. **memory** (passwords, keys, decrypted data) → encrypt, restrict, delete old (remanence)
- **Hypervisor = high-value target** → patch, restrict + monitor admin access
- **Inter-VM traffic blind spots** (never crosses a physical network) → **virtual firewalls / microsegmentation**
- **Noisy neighbor** resource exhaustion (availability)

**7. Infrastructure as code (IaC)**

Infrastructure in templates (Terraform, CloudFormation, Ansible).

- Benefits: **repeatable** (baseline), **version-controlled + reviewed** (change mgmt), **scannable before deploy** (public bucket, open 22, `*` permissions) = **policy as code**.
- Risks: secrets in templates (vault + scanning); bad template spreads everywhere (review + gates); **configuration drift** (manual live change) → **drift detection + re-apply the template**; needed changes go **in the code** via review. **Immutable infrastructure** = replace, don't patch live.

**On the exam**

- On hardware, cloud → **Type 1** · app on desktop OS → **Type 2**
- Breaks out to host → **VM escape** · forgotten VMs → **VM sprawl**
- Snapshot has passwords from memory → **insecure snapshots**
- Inter-VM traffic unseen → microsegmentation · containers less isolated → **share kernel**
- Scan Terraform before deploy → **IaC scanning / policy as code**
- Live servers ≠ IaC → **drift** → re-apply template
- **Trap:** Type 2 is LESS secure.

**Hooks**

**Type 1 = foundation; Type 2 = renting a room. Snapshot = a photo of the whole VM incl. memory secrets. IaC drift → restore from the code, never edit the code to match the drift.**

**Quick check:** (1) Max isolation + performance for customer VMs: which hypervisor type? (2) Prod VM snapshots on a shared drive: risk? (3) Port 22 opened manually on a Terraform-managed server: name + fix?

**Answer:** Taught (known).

</details>

<a name="t-4-3-7"></a>
**Infrastructure as code (IaC)** (review)

Infrastructure in templates; scan for misconfigurations, prevent drift.

> On the exam: What it is: defining infrastructure in code (Terraform, CloudFormation).
Benefits: repeatable, reviewable, versioned environments, no manual drift. Risks: one bad template creates many misconfigured systems; secrets in templates.
Scenario cue: 'how to stop misconfigured cloud resources before they exist?' → scan IaC templates in the pipeline.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 3: Virtualization and infrastructure (topics 5, 6, 20, 7)**

Layers of isolation, and what breaks through them.

**5. Hypervisors**

**Hypervisor (VMM)** creates/runs VMs.

- **Type 1 (bare metal):** directly on hardware, no host OS (ESXi, Hyper-V, Xen, KVM). **More secure + faster**; data centers/cloud.
- **Type 2 (hosted):** an app on a normal OS (VirtualBox, VMware Workstation, Parallels). **Less secure** (host OS compromise exposes all VMs); desktops/testing.
- **VM escape:** code in a VM breaks out to the hypervisor → other VMs/host; worst case in multitenant cloud.

*Hook: Type 1 = the foundation; Type 2 = renting a room in someone else's house.*

**6. Containers**

- **Share the host kernel** (VMs have their own OS) → one kernel flaw hits all (**container escape**).
- Image: **scan**, minimal base, **sign + verify**, trusted registries. Runtime: **not root**, read-only FS, drop capabilities, resource limits. No secrets in images.

*VM = separate house; container = apartment (shared foundation).*

**20. Virtualization security**

- **VM escape** · **VM sprawl** (forgotten, unpatched, ownerless VMs → inventory, owners, lifecycle policies)
- **Insecure snapshots:** whole VM state incl. **memory** (passwords, keys, decrypted data) → encrypt, restrict, delete old (remanence)
- **Hypervisor = high-value target** → patch, restrict + monitor admin access
- **Inter-VM traffic blind spots** (never crosses a physical network) → **virtual firewalls / microsegmentation**
- **Noisy neighbor** resource exhaustion (availability)

**7. Infrastructure as code (IaC)**

Infrastructure in templates (Terraform, CloudFormation, Ansible).

- Benefits: **repeatable** (baseline), **version-controlled + reviewed** (change mgmt), **scannable before deploy** (public bucket, open 22, `*` permissions) = **policy as code**.
- Risks: secrets in templates (vault + scanning); bad template spreads everywhere (review + gates); **configuration drift** (manual live change) → **drift detection + re-apply the template**; needed changes go **in the code** via review. **Immutable infrastructure** = replace, don't patch live.

**On the exam**

- On hardware, cloud → **Type 1** · app on desktop OS → **Type 2**
- Breaks out to host → **VM escape** · forgotten VMs → **VM sprawl**
- Snapshot has passwords from memory → **insecure snapshots**
- Inter-VM traffic unseen → microsegmentation · containers less isolated → **share kernel**
- Scan Terraform before deploy → **IaC scanning / policy as code**
- Live servers ≠ IaC → **drift** → re-apply template
- **Trap:** Type 2 is LESS secure.

**Hooks**

**Type 1 = foundation; Type 2 = renting a room. Snapshot = a photo of the whole VM incl. memory secrets. IaC drift → restore from the code, never edit the code to match the drift.**

**Quick check:** (1) Max isolation + performance for customer VMs: which hypervisor type? (2) Prod VM snapshots on a shared drive: risk? (3) Port 22 opened manually on a Terraform-managed server: name + fix?

**Answer:** Skipped: CONFIGURATION DRIFT; re-apply the template, change port 22 in code via review. Marked shaky.

</details>

<a name="t-4-3-8"></a>
**Trusted Platform Module (TPM)** (review)

Chip for key storage, measured boot, sealed storage.

> On the exam: Measured boot records hashes of boot components; sealed storage releases keys only if the system state is trusted.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 4: Trusted computing (topics 8, 9, 10, 23, 24)**

Classic definition-and-property terms that nest together.

**The bank picture (simplest way to hold it)**

- **TCB** = everything security depends on (guards, vault, locks, alarm); any failure = bank unsafe.
- **Reference monitor** = the RULE that every person entering the vault passes the guard's check; no side doors.
- **Security kernel** = the actual guard following that rule.
- **Rings** = who can go where: manager (**Ring 0, kernel**) everywhere; customers (**Ring 3, apps**) stay in the lobby and must ASK a teller (**system call**).
- **TPM** = small safe welded into the foundation, holding keys + a logbook of what came in at opening (boot).

**8. TPM (Trusted Platform Module)**

Security chip on the motherboard/CPU; keys generated/kept inside, can't be copied out.

- **Endorsement key (EK)**: factory-burned, unique identity · **Storage root key (SRK)**: protects other keys
- **Measured boot**: each boot component hashed into **PCRs** (records what booted)
- **SEALED STORAGE**: data/keys released ONLY if boot measurements match (**BitLocker**)
- **Remote attestation**: prove to a server the machine booted cleanly
- Random number generation
- **Secure boot = gatekeeper (blocks unsigned). Measured boot = flight recorder (records for later checks).**
- **TPM** = cheap chip inside one device · **HSM** = dedicated appliance for many keys (root CA, payments)

**9. TCB (Trusted Computing Base)**

All hardware/firmware/software that **enforces the security policy** (CPU protections, kernel, TPM, authentication, access control). Compromise any part = whole system fails. **Keep it small** (economy of mechanism).

**Security perimeter** = boundary between TCB and everything untrusted.

**10. Reference monitor**

**Abstract concept**: every subject → object access must be checked. Properties: **tamper-proof**, **always invoked** (no bypass = complete mediation), **small enough to verify**.

**NEAT = Non-bypassable, Evaluable, Always invoked, Tamper-proof.**

**Security kernel** = the actual implementation of the reference monitor (inside the TCB).

**23. Ring protection**

- **Ring 0** = most privileged = **OS kernel** · Rings 1–2 = drivers/services (rarely used) · **Ring 3** = least = **user apps**.
- Outer rings can't touch inner memory/hardware directly; must use a **system call**.
- **Privilege escalation** = Ring 3 → Ring 0 (Meltdown broke this wall). Hypervisor = "**Ring −1**".
- **Lower ring number = more power.**

**24. Together**

TCB (edge = security perimeter) ⊃ security kernel (implements the reference monitor) · rings enforce privilege (kernel Ring 0, apps Ring 3) · TPM anchors trust in hardware (measured boot, attestation) · **trust boundary** = anywhere trust changes; every crossing needs checks (DFDs in 4.4).

**On the exam**

- Stores keys + records boot measurements for attestation → **TPM**
- Disk key released only if boot unchanged → **sealed storage**
- Blocks unsigned bootloaders → **secure boot** · records hashes → **measured boot**
- All components enforcing policy → **TCB** · boundary trusted/untrusted → **security perimeter**
- Mediates every access; tamper-proof, always invoked, verifiable → **reference monitor**
- Implementation of the reference monitor → **security kernel**
- Most privileged ring → **Ring 0** · user apps → **Ring 3**
- **Traps:** reference monitor = CONCEPT; security kernel = IMPLEMENTATION. Lower ring = more privilege.

**Hooks**

**TPM = tiny safe welded to the motherboard + boot flight recorder. TCB = everything you must trust; keep it small. Reference monitor = NEAT. Rings: 0 = king, 3 = citizens.**

**Quick check:** (1) Three properties of a reference monitor? (2) Disk key released only if TPM confirms boot unchanged: which feature? (3) Kernel ring vs app ring? Re-check: which ring has most privilege?

**Answer:** I first said "I don't know"; after bank re-teach described TPM as the tiny safe but did not name SEALED STORAGE. Marked shaky.

</details>

<a name="t-4-3-9"></a>
**Trusted Computing Base (TCB)** (review)

All hardware, firmware and software enforcing the security policy.

> On the exam: What it is: everything (hardware, firmware, kernel, security software) responsible for enforcing the security policy. If any part fails, security fails.
Key idea: keep the TCB as small as possible so it can be verified. The security perimeter separates the TCB from the rest.
Scenario cue: 'why minimize code running in kernel mode?' → smaller TCB is easier to trust.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 4: Trusted computing (topics 8, 9, 10, 23, 24)**

Classic definition-and-property terms that nest together.

**The bank picture (simplest way to hold it)**

- **TCB** = everything security depends on (guards, vault, locks, alarm); any failure = bank unsafe.
- **Reference monitor** = the RULE that every person entering the vault passes the guard's check; no side doors.
- **Security kernel** = the actual guard following that rule.
- **Rings** = who can go where: manager (**Ring 0, kernel**) everywhere; customers (**Ring 3, apps**) stay in the lobby and must ASK a teller (**system call**).
- **TPM** = small safe welded into the foundation, holding keys + a logbook of what came in at opening (boot).

**8. TPM (Trusted Platform Module)**

Security chip on the motherboard/CPU; keys generated/kept inside, can't be copied out.

- **Endorsement key (EK)**: factory-burned, unique identity · **Storage root key (SRK)**: protects other keys
- **Measured boot**: each boot component hashed into **PCRs** (records what booted)
- **SEALED STORAGE**: data/keys released ONLY if boot measurements match (**BitLocker**)
- **Remote attestation**: prove to a server the machine booted cleanly
- Random number generation
- **Secure boot = gatekeeper (blocks unsigned). Measured boot = flight recorder (records for later checks).**
- **TPM** = cheap chip inside one device · **HSM** = dedicated appliance for many keys (root CA, payments)

**9. TCB (Trusted Computing Base)**

All hardware/firmware/software that **enforces the security policy** (CPU protections, kernel, TPM, authentication, access control). Compromise any part = whole system fails. **Keep it small** (economy of mechanism).

**Security perimeter** = boundary between TCB and everything untrusted.

**10. Reference monitor**

**Abstract concept**: every subject → object access must be checked. Properties: **tamper-proof**, **always invoked** (no bypass = complete mediation), **small enough to verify**.

**NEAT = Non-bypassable, Evaluable, Always invoked, Tamper-proof.**

**Security kernel** = the actual implementation of the reference monitor (inside the TCB).

**23. Ring protection**

- **Ring 0** = most privileged = **OS kernel** · Rings 1–2 = drivers/services (rarely used) · **Ring 3** = least = **user apps**.
- Outer rings can't touch inner memory/hardware directly; must use a **system call**.
- **Privilege escalation** = Ring 3 → Ring 0 (Meltdown broke this wall). Hypervisor = "**Ring −1**".
- **Lower ring number = more power.**

**24. Together**

TCB (edge = security perimeter) ⊃ security kernel (implements the reference monitor) · rings enforce privilege (kernel Ring 0, apps Ring 3) · TPM anchors trust in hardware (measured boot, attestation) · **trust boundary** = anywhere trust changes; every crossing needs checks (DFDs in 4.4).

**On the exam**

- Stores keys + records boot measurements for attestation → **TPM**
- Disk key released only if boot unchanged → **sealed storage**
- Blocks unsigned bootloaders → **secure boot** · records hashes → **measured boot**
- All components enforcing policy → **TCB** · boundary trusted/untrusted → **security perimeter**
- Mediates every access; tamper-proof, always invoked, verifiable → **reference monitor**
- Implementation of the reference monitor → **security kernel**
- Most privileged ring → **Ring 0** · user apps → **Ring 3**
- **Traps:** reference monitor = CONCEPT; security kernel = IMPLEMENTATION. Lower ring = more privilege.

**Hooks**

**TPM = tiny safe welded to the motherboard + boot flight recorder. TCB = everything you must trust; keep it small. Reference monitor = NEAT. Rings: 0 = king, 3 = citizens.**

**Quick check:** (1) Three properties of a reference monitor? (2) Disk key released only if TPM confirms boot unchanged: which feature? (3) Kernel ring vs app ring? Re-check: which ring has most privilege?

**Answer:** Taught (bank picture); not tested. Marked shaky (new).

</details>

<a name="t-4-3-10"></a>
**Reference monitor**

Mediates all access; must be tamper-proof, always invoked, small enough to verify.

> On the exam: An abstract concept; the security kernel implements it. This is where complete mediation happens.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 4: Trusted computing (topics 8, 9, 10, 23, 24)**

Classic definition-and-property terms that nest together.

**The bank picture (simplest way to hold it)**

- **TCB** = everything security depends on (guards, vault, locks, alarm); any failure = bank unsafe.
- **Reference monitor** = the RULE that every person entering the vault passes the guard's check; no side doors.
- **Security kernel** = the actual guard following that rule.
- **Rings** = who can go where: manager (**Ring 0, kernel**) everywhere; customers (**Ring 3, apps**) stay in the lobby and must ASK a teller (**system call**).
- **TPM** = small safe welded into the foundation, holding keys + a logbook of what came in at opening (boot).

**8. TPM (Trusted Platform Module)**

Security chip on the motherboard/CPU; keys generated/kept inside, can't be copied out.

- **Endorsement key (EK)**: factory-burned, unique identity · **Storage root key (SRK)**: protects other keys
- **Measured boot**: each boot component hashed into **PCRs** (records what booted)
- **SEALED STORAGE**: data/keys released ONLY if boot measurements match (**BitLocker**)
- **Remote attestation**: prove to a server the machine booted cleanly
- Random number generation
- **Secure boot = gatekeeper (blocks unsigned). Measured boot = flight recorder (records for later checks).**
- **TPM** = cheap chip inside one device · **HSM** = dedicated appliance for many keys (root CA, payments)

**9. TCB (Trusted Computing Base)**

All hardware/firmware/software that **enforces the security policy** (CPU protections, kernel, TPM, authentication, access control). Compromise any part = whole system fails. **Keep it small** (economy of mechanism).

**Security perimeter** = boundary between TCB and everything untrusted.

**10. Reference monitor**

**Abstract concept**: every subject → object access must be checked. Properties: **tamper-proof**, **always invoked** (no bypass = complete mediation), **small enough to verify**.

**NEAT = Non-bypassable, Evaluable, Always invoked, Tamper-proof.**

**Security kernel** = the actual implementation of the reference monitor (inside the TCB).

**23. Ring protection**

- **Ring 0** = most privileged = **OS kernel** · Rings 1–2 = drivers/services (rarely used) · **Ring 3** = least = **user apps**.
- Outer rings can't touch inner memory/hardware directly; must use a **system call**.
- **Privilege escalation** = Ring 3 → Ring 0 (Meltdown broke this wall). Hypervisor = "**Ring −1**".
- **Lower ring number = more power.**

**24. Together**

TCB (edge = security perimeter) ⊃ security kernel (implements the reference monitor) · rings enforce privilege (kernel Ring 0, apps Ring 3) · TPM anchors trust in hardware (measured boot, attestation) · **trust boundary** = anywhere trust changes; every crossing needs checks (DFDs in 4.4).

**On the exam**

- Stores keys + records boot measurements for attestation → **TPM**
- Disk key released only if boot unchanged → **sealed storage**
- Blocks unsigned bootloaders → **secure boot** · records hashes → **measured boot**
- All components enforcing policy → **TCB** · boundary trusted/untrusted → **security perimeter**
- Mediates every access; tamper-proof, always invoked, verifiable → **reference monitor**
- Implementation of the reference monitor → **security kernel**
- Most privileged ring → **Ring 0** · user apps → **Ring 3**
- **Traps:** reference monitor = CONCEPT; security kernel = IMPLEMENTATION. Lower ring = more privilege.

**Hooks**

**TPM = tiny safe welded to the motherboard + boot flight recorder. TCB = everything you must trust; keep it small. Reference monitor = NEAT. Rings: 0 = king, 3 = citizens.**

**Quick check:** (1) Three properties of a reference monitor? (2) Disk key released only if TPM confirms boot unchanged: which feature? (3) Kernel ring vs app ring? Re-check: which ring has most privilege?

**Answer:** NEAT: Non-bypassable, Evaluable, Always invoked, Tamper-proof. Correct after re-teach.

</details>

<a name="t-4-3-11"></a>
**Database security**

Encryption (TDE, column), views to limit data, stored procedures, triggers, least privilege, encrypted connections.

> On the exam: Views and stored procedures limit what users see and do. The app's database account should never be a DBA.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 5: Databases (topics 11, 12, 13)**

Standard DB protection + two sneaky leaks (inference, aggregation) + their odd fix (polyinstantiation).

**11. Database security**

- **SQLi defense: parameterized queries / prepared statements** (input = data, never code). **Stored procedures** help only if they don't concatenate SQL inside; not automatically safe.
- **Least privilege DB accounts:** app is a limited user, **never DBA / `sa`**; no DROP.
- **Views** (hide columns/rows) · **row-level security** (own rows only).
- **Encryption:** at rest **TDE** (Transparent Data Encryption, whole files) + **column-level** (SSNs; even DBAs can't read); in transit TLS.
- Passwords = salted slow hashes.
- **Auditing + DAM (Database Activity Monitoring):** who queried what; alert on anomalies (full-table export at 3 AM).
- Hardening: remove default accounts/sample DBs, patch, DB behind app tier.
- **Separation of duties:** DBAs can't erase their own audit logs.

**12. Inference and aggregation (leaks without forbidden access)**

- **AGGREGATION = combining many low-sensitivity pieces into a high-sensitivity whole** ("collect"). Supply orders → troop size; public check-ins → routine + home. Controls: **classify the aggregate higher**, limit bulk queries/exports, need-to-know, monitor mass collection.
- **INFERENCE = deducing a secret from allowed information** ("deduce"). Average salary 9 people $80k → 10 people $82k → new hire = $100k. Controls: **minimum query set size**, **noise** (differential privacy), **cell suppression**, **polyinstantiation**.
- Aggregation = puzzle pieces (the sum); inference = detective work (the reasoning).

**13. Polyinstantiation**

- **Multiple versions of the same record**, one per **classification level**; low-clearance users see a **harmless cover version** instead of being refused.
- **WHY: "access denied" itself leaks information** (tells them something secret exists = an **inference**); a believable cover value gives nothing to infer from.
- Ship Enterprise: Top Secret = Weapons; Unclassified = Food supplies.
- Used in **multilevel security (MLS)** DBs (military/government); links to **Bell-LaPadula** (4.6). Prevents **inference** + key conflicts across levels.
- "Poly" = many, "instance" = copy.

**On the exam**

- App connects as `sa` → **least privilege** · prevent SQLi → **parameterized queries**
- Encrypt whole DB transparently → **TDE** · 3 AM full export alert → **DAM**
- Supply orders reveal troop movements → **aggregation** · salary from two averages → **inference**
- Refuse stats for groups &lt; 10 → **minimum query set size**
- Cover story instead of "access denied" → **polyinstantiation**
- **Traps:** stored procedures not automatically safe; aggregation = collect, inference = deduce; when asked WHY, name the specific threat (inference), not "attacks."

**Hooks**

**Aggregation = puzzle pieces. Inference = detective work. Polyinstantiation = a cover story: even "access denied" is a clue.**

**Quick check:** (1) Subtracting regional totals reveals one customer's spend: aggregation or inference? (2) Why does polyinstantiation show a fake value instead of 'access denied'? (3) Web app connects as sa: which principle violated?

**Answer:** Least privilege. Correct.

</details>

<a name="t-4-3-12"></a>
**Inference and aggregation**

Deducing sensitive data from allowed data, or combining harmless data into sensitive data.

> On the exam: Inference: deducing restricted information from data you're allowed to see. Aggregation: combining many low-sensitivity items into something sensitive.
Scenario cue: 'a user can't see salaries but can see department totals and headcounts' → inference.
Defenses: limit query results, polyinstantiation, add noise, classify aggregated data higher.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 5: Databases (topics 11, 12, 13)**

Standard DB protection + two sneaky leaks (inference, aggregation) + their odd fix (polyinstantiation).

**11. Database security**

- **SQLi defense: parameterized queries / prepared statements** (input = data, never code). **Stored procedures** help only if they don't concatenate SQL inside; not automatically safe.
- **Least privilege DB accounts:** app is a limited user, **never DBA / `sa`**; no DROP.
- **Views** (hide columns/rows) · **row-level security** (own rows only).
- **Encryption:** at rest **TDE** (Transparent Data Encryption, whole files) + **column-level** (SSNs; even DBAs can't read); in transit TLS.
- Passwords = salted slow hashes.
- **Auditing + DAM (Database Activity Monitoring):** who queried what; alert on anomalies (full-table export at 3 AM).
- Hardening: remove default accounts/sample DBs, patch, DB behind app tier.
- **Separation of duties:** DBAs can't erase their own audit logs.

**12. Inference and aggregation (leaks without forbidden access)**

- **AGGREGATION = combining many low-sensitivity pieces into a high-sensitivity whole** ("collect"). Supply orders → troop size; public check-ins → routine + home. Controls: **classify the aggregate higher**, limit bulk queries/exports, need-to-know, monitor mass collection.
- **INFERENCE = deducing a secret from allowed information** ("deduce"). Average salary 9 people $80k → 10 people $82k → new hire = $100k. Controls: **minimum query set size**, **noise** (differential privacy), **cell suppression**, **polyinstantiation**.
- Aggregation = puzzle pieces (the sum); inference = detective work (the reasoning).

**13. Polyinstantiation**

- **Multiple versions of the same record**, one per **classification level**; low-clearance users see a **harmless cover version** instead of being refused.
- **WHY: "access denied" itself leaks information** (tells them something secret exists = an **inference**); a believable cover value gives nothing to infer from.
- Ship Enterprise: Top Secret = Weapons; Unclassified = Food supplies.
- Used in **multilevel security (MLS)** DBs (military/government); links to **Bell-LaPadula** (4.6). Prevents **inference** + key conflicts across levels.
- "Poly" = many, "instance" = copy.

**On the exam**

- App connects as `sa` → **least privilege** · prevent SQLi → **parameterized queries**
- Encrypt whole DB transparently → **TDE** · 3 AM full export alert → **DAM**
- Supply orders reveal troop movements → **aggregation** · salary from two averages → **inference**
- Refuse stats for groups &lt; 10 → **minimum query set size**
- Cover story instead of "access denied" → **polyinstantiation**
- **Traps:** stored procedures not automatically safe; aggregation = collect, inference = deduce; when asked WHY, name the specific threat (inference), not "attacks."

**Hooks**

**Aggregation = puzzle pieces. Inference = detective work. Polyinstantiation = a cover story: even "access denied" is a clue.**

**Quick check:** (1) Subtracting regional totals reveals one customer's spend: aggregation or inference? (2) Why does polyinstantiation show a fake value instead of 'access denied'? (3) Web app connects as sa: which principle violated?

**Answer:** Inference. Correct.

</details>

<a name="t-4-3-13"></a>
**Polyinstantiation** (review)

Different versions of a record at different classification levels to stop inference.

> On the exam: Example: a low-clearance user sees 'cargo: food' while the real record says something classified.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 5: Databases (topics 11, 12, 13)**

Standard DB protection + two sneaky leaks (inference, aggregation) + their odd fix (polyinstantiation).

**11. Database security**

- **SQLi defense: parameterized queries / prepared statements** (input = data, never code). **Stored procedures** help only if they don't concatenate SQL inside; not automatically safe.
- **Least privilege DB accounts:** app is a limited user, **never DBA / `sa`**; no DROP.
- **Views** (hide columns/rows) · **row-level security** (own rows only).
- **Encryption:** at rest **TDE** (Transparent Data Encryption, whole files) + **column-level** (SSNs; even DBAs can't read); in transit TLS.
- Passwords = salted slow hashes.
- **Auditing + DAM (Database Activity Monitoring):** who queried what; alert on anomalies (full-table export at 3 AM).
- Hardening: remove default accounts/sample DBs, patch, DB behind app tier.
- **Separation of duties:** DBAs can't erase their own audit logs.

**12. Inference and aggregation (leaks without forbidden access)**

- **AGGREGATION = combining many low-sensitivity pieces into a high-sensitivity whole** ("collect"). Supply orders → troop size; public check-ins → routine + home. Controls: **classify the aggregate higher**, limit bulk queries/exports, need-to-know, monitor mass collection.
- **INFERENCE = deducing a secret from allowed information** ("deduce"). Average salary 9 people $80k → 10 people $82k → new hire = $100k. Controls: **minimum query set size**, **noise** (differential privacy), **cell suppression**, **polyinstantiation**.
- Aggregation = puzzle pieces (the sum); inference = detective work (the reasoning).

**13. Polyinstantiation**

- **Multiple versions of the same record**, one per **classification level**; low-clearance users see a **harmless cover version** instead of being refused.
- **WHY: "access denied" itself leaks information** (tells them something secret exists = an **inference**); a believable cover value gives nothing to infer from.
- Ship Enterprise: Top Secret = Weapons; Unclassified = Food supplies.
- Used in **multilevel security (MLS)** DBs (military/government); links to **Bell-LaPadula** (4.6). Prevents **inference** + key conflicts across levels.
- "Poly" = many, "instance" = copy.

**On the exam**

- App connects as `sa` → **least privilege** · prevent SQLi → **parameterized queries**
- Encrypt whole DB transparently → **TDE** · 3 AM full export alert → **DAM**
- Supply orders reveal troop movements → **aggregation** · salary from two averages → **inference**
- Refuse stats for groups &lt; 10 → **minimum query set size**
- Cover story instead of "access denied" → **polyinstantiation**
- **Traps:** stored procedures not automatically safe; aggregation = collect, inference = deduce; when asked WHY, name the specific threat (inference), not "attacks."

**Hooks**

**Aggregation = puzzle pieces. Inference = detective work. Polyinstantiation = a cover story: even "access denied" is a clue.**

**Quick check:** (1) Subtracting regional totals reveals one customer's spend: aggregation or inference? (2) Why does polyinstantiation show a fake value instead of 'access denied'? (3) Web app connects as sa: which principle violated?

**Answer:** I said "it prevents attacks" (too vague). Specific: access denied itself leaks that a secret exists = INFERENCE. Marked shaky.

</details>

<a name="t-4-3-14"></a>
**Managed runtimes**

Java VM (bytecode verifier, sandbox), .NET common language runtime, Python, PowerShell (execution policy).

> On the exam: Java VM and .NET CLR: bytecode verification, memory management (no manual pointers), sandboxing, permission models. Python and PowerShell: scripting power is also attack power (PowerShell execution policy, constrained language mode, logging).
Scenario cue: 'attackers use PowerShell for fileless attacks' → script block logging and constrained language mode.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 6: Runtimes and operating systems (topics 14, 15, 25, 16, 26)**

Who manages memory, and OS-level controls that contain damage.

**14. Managed runtimes**

Runtime manages memory/checks code (**JVM**, **.NET CLR**, Python, JS, Go).

- **Garbage collection** (no use-after-free/double-free) · **bounds checking** (exception instead of overflow) · **type checking** · sandboxing.
- But: runtime itself can be vulnerable (patch); **native code** via JNI / P/Invoke loses protections; **logic flaws** (SQLi, broken access control) still happen.

**15. Managed vs unmanaged code**

- **Managed** (Java, C#) vs **unmanaged/native** (**C, C++**: you manage memory) → **buffer overflows, use-after-free, integer overflows, format string bugs**.
- Defenses: **ASLR** (random memory layout), **DEP/NX** (data areas non-executable), **stack canaries** (detect overwrite of return address), safe functions (no `strcpy`/`gets`), SAST + fuzzing.
- **Memory-safe languages** (Rust, Go, Java, C#) recommended by governments: eliminate whole bug classes.

**25. Code access security (CAS) and type safety**

- **Type safety:** data only used as its correct type; prevents memory attacks; enforced by managed runtimes.
- **CAS (.NET, deprecated):** permissions for **code based on its origin/signer/zone**, not just who runs it (Java Security Manager similar, deprecated).

**16. OS controls**

Process isolation · normal-user/least privilege (UAC) · file permissions/ACLs · ASLR + DEP · sandboxing · patching, hardening, host firewall, logging.

**26. Security-oriented operating systems**

- **DAC (Discretionary):** the **owner decides** access (normal Windows/Linux permissions); malware running as you gets everything you can access.
- **MAC (Mandatory):** **system enforces a central policy** nobody can override (not root, not the owner).
- **SELinux** (NSA; Red Hat, Fedora, Android): labels processes/files; policy says what each process may touch (hacked web server still can't read `/etc/shadow`).
- **AppArmor** (Ubuntu, SUSE): simpler, **path-based profiles** per program.
- Trusted/high-assurance OSes (formally verified **seL4** microkernel) → small TCB / reference monitor ideas.
- **MAC CONTAINS a compromise.**

**On the exam**

- Bounds checking blocks overflows → **managed code** · C/C++ overflows → **unmanaged**
- Random memory addresses → **ASLR** · non-executable memory → **DEP/NX** · detects stack overwrite → **stack canaries**
- Permissions by where code came from → **CAS**
- Owner decides → **DAC** · central policy even root can't override → **MAC**
- NSA Linux MAC module → **SELinux** · path profiles, Ubuntu → **AppArmor**
- **Traps:** managed code still has logic flaws; native calls lose protections.

**Hooks**

**Managed = a babysitter for memory. ASLR = shuffling the rooms; DEP = no running in the data rooms; canary = the bird that warns you. Discretionary = owner's Decision; Mandatory = Must follow the law.**

**Quick check:** (1) Hacked web server on SELinux still can't read the password file: which model, why? (2) Which protection randomizes memory placement? (3) Why do governments recommend memory-safe languages?

**Answer:** Memory-safe languages eliminate memory bug classes. Correct.

</details>

<a name="t-4-3-15"></a>
**Managed vs unmanaged code**

Managed runtimes handle memory; unmanaged (C/C++) risks memory corruption.

> On the exam: Managed code (Java, C#) runs inside a runtime that handles memory, preventing most buffer overflows. Unmanaged code (C, C++) gives direct memory access, so overflows and use-after-free are possible.
Scenario cue: 'which language choice reduces memory corruption vulnerabilities?' → managed or memory-safe languages.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 6: Runtimes and operating systems (topics 14, 15, 25, 16, 26)**

Who manages memory, and OS-level controls that contain damage.

**14. Managed runtimes**

Runtime manages memory/checks code (**JVM**, **.NET CLR**, Python, JS, Go).

- **Garbage collection** (no use-after-free/double-free) · **bounds checking** (exception instead of overflow) · **type checking** · sandboxing.
- But: runtime itself can be vulnerable (patch); **native code** via JNI / P/Invoke loses protections; **logic flaws** (SQLi, broken access control) still happen.

**15. Managed vs unmanaged code**

- **Managed** (Java, C#) vs **unmanaged/native** (**C, C++**: you manage memory) → **buffer overflows, use-after-free, integer overflows, format string bugs**.
- Defenses: **ASLR** (random memory layout), **DEP/NX** (data areas non-executable), **stack canaries** (detect overwrite of return address), safe functions (no `strcpy`/`gets`), SAST + fuzzing.
- **Memory-safe languages** (Rust, Go, Java, C#) recommended by governments: eliminate whole bug classes.

**25. Code access security (CAS) and type safety**

- **Type safety:** data only used as its correct type; prevents memory attacks; enforced by managed runtimes.
- **CAS (.NET, deprecated):** permissions for **code based on its origin/signer/zone**, not just who runs it (Java Security Manager similar, deprecated).

**16. OS controls**

Process isolation · normal-user/least privilege (UAC) · file permissions/ACLs · ASLR + DEP · sandboxing · patching, hardening, host firewall, logging.

**26. Security-oriented operating systems**

- **DAC (Discretionary):** the **owner decides** access (normal Windows/Linux permissions); malware running as you gets everything you can access.
- **MAC (Mandatory):** **system enforces a central policy** nobody can override (not root, not the owner).
- **SELinux** (NSA; Red Hat, Fedora, Android): labels processes/files; policy says what each process may touch (hacked web server still can't read `/etc/shadow`).
- **AppArmor** (Ubuntu, SUSE): simpler, **path-based profiles** per program.
- Trusted/high-assurance OSes (formally verified **seL4** microkernel) → small TCB / reference monitor ideas.
- **MAC CONTAINS a compromise.**

**On the exam**

- Bounds checking blocks overflows → **managed code** · C/C++ overflows → **unmanaged**
- Random memory addresses → **ASLR** · non-executable memory → **DEP/NX** · detects stack overwrite → **stack canaries**
- Permissions by where code came from → **CAS**
- Owner decides → **DAC** · central policy even root can't override → **MAC**
- NSA Linux MAC module → **SELinux** · path profiles, Ubuntu → **AppArmor**
- **Traps:** managed code still has logic flaws; native calls lose protections.

**Hooks**

**Managed = a babysitter for memory. ASLR = shuffling the rooms; DEP = no running in the data rooms; canary = the bird that warns you. Discretionary = owner's Decision; Mandatory = Must follow the law.**

**Quick check:** (1) Hacked web server on SELinux still can't read the password file: which model, why? (2) Which protection randomizes memory placement? (3) Why do governments recommend memory-safe languages?

**Answer:** Correct.

</details>

<a name="t-4-3-16"></a>
**Operating system controls**

Access controls, process isolation, memory protection.

> On the exam: Examples: user and file permissions, process isolation, memory protection (ASLR, DEP), secure storage APIs, OS logging, mandatory access control (SELinux).
Scenario cue: 'a developer writes custom encryption storage instead of using the OS keystore' → reuse OS security services instead.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 6: Runtimes and operating systems (topics 14, 15, 25, 16, 26)**

Who manages memory, and OS-level controls that contain damage.

**14. Managed runtimes**

Runtime manages memory/checks code (**JVM**, **.NET CLR**, Python, JS, Go).

- **Garbage collection** (no use-after-free/double-free) · **bounds checking** (exception instead of overflow) · **type checking** · sandboxing.
- But: runtime itself can be vulnerable (patch); **native code** via JNI / P/Invoke loses protections; **logic flaws** (SQLi, broken access control) still happen.

**15. Managed vs unmanaged code**

- **Managed** (Java, C#) vs **unmanaged/native** (**C, C++**: you manage memory) → **buffer overflows, use-after-free, integer overflows, format string bugs**.
- Defenses: **ASLR** (random memory layout), **DEP/NX** (data areas non-executable), **stack canaries** (detect overwrite of return address), safe functions (no `strcpy`/`gets`), SAST + fuzzing.
- **Memory-safe languages** (Rust, Go, Java, C#) recommended by governments: eliminate whole bug classes.

**25. Code access security (CAS) and type safety**

- **Type safety:** data only used as its correct type; prevents memory attacks; enforced by managed runtimes.
- **CAS (.NET, deprecated):** permissions for **code based on its origin/signer/zone**, not just who runs it (Java Security Manager similar, deprecated).

**16. OS controls**

Process isolation · normal-user/least privilege (UAC) · file permissions/ACLs · ASLR + DEP · sandboxing · patching, hardening, host firewall, logging.

**26. Security-oriented operating systems**

- **DAC (Discretionary):** the **owner decides** access (normal Windows/Linux permissions); malware running as you gets everything you can access.
- **MAC (Mandatory):** **system enforces a central policy** nobody can override (not root, not the owner).
- **SELinux** (NSA; Red Hat, Fedora, Android): labels processes/files; policy says what each process may touch (hacked web server still can't read `/etc/shadow`).
- **AppArmor** (Ubuntu, SUSE): simpler, **path-based profiles** per program.
- Trusted/high-assurance OSes (formally verified **seL4** microkernel) → small TCB / reference monitor ideas.
- **MAC CONTAINS a compromise.**

**On the exam**

- Bounds checking blocks overflows → **managed code** · C/C++ overflows → **unmanaged**
- Random memory addresses → **ASLR** · non-executable memory → **DEP/NX** · detects stack overwrite → **stack canaries**
- Permissions by where code came from → **CAS**
- Owner decides → **DAC** · central policy even root can't override → **MAC**
- NSA Linux MAC module → **SELinux** · path profiles, Ubuntu → **AppArmor**
- **Traps:** managed code still has logic flaws; native calls lose protections.

**Hooks**

**Managed = a babysitter for memory. ASLR = shuffling the rooms; DEP = no running in the data rooms; canary = the bird that warns you. Discretionary = owner's Decision; Mandatory = Must follow the law.**

**Quick check:** (1) Hacked web server on SELinux still can't read the password file: which model, why? (2) Which protection randomizes memory placement? (3) Why do governments recommend memory-safe languages?

**Answer:** ASLR. Correct.

</details>

<a name="t-4-3-17"></a>
**Backup and restoration planning**

Full, incremental, differential; test restores; 3-2-1 rule; protect backups.

> On the exam: Incremental: fast backup, slow restore. Differential: slower backup, faster restore. An untested backup isn't a backup; keep offline or immutable copies against ransomware.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 7: Backups and retention (topics 17, 18)**

**17. Backup types**

- **Full:** everything every time. Fastest/simplest **restore**; slowest backup, most storage.
- **Incremental:** changes since the **last backup of any kind**. Fastest backup, smallest; **slowest restore** (last full + EVERY incremental since, in order; one missing link breaks it).
- **Differential:** changes since the **last FULL**; grows daily. Restore = **last full + latest differential** (2 sets). Middle ground.
- Example: full Sunday, crash Thursday → incremental = full + Mon + Tue + Wed; differential = full + Wed.
- **Archive bit:** full + incremental **clear** it; differential **doesn't** (so it re-copies everything since the full).
- **3-2-1:** 3 copies, 2 media types, 1 off-site. **3-2-1-1-0:** + 1 **offline/immutable**, 0 errors on test restores.
- **Ransomware hunts connected backups** → **offline (air-gapped) or immutable** copy lets you recover without paying. Always-connected off-site (synced cloud) can be encrypted too.
- Encrypt backups (protect keys); restrict + log access; **test restores**; frequency from **RPO**, restore speed vs **RTO**.

**18. Secure retention, retrieval and destruction**

- **Retention:** follow the schedule (legal minimum, privacy maximum); **legal hold** overrides; includes **backups** (old backups with deleted customers = GDPR issue).
- **Retrieval:** authorized, **logged**, **integrity checks** (hashes); legal evidence → **chain of custody**.
- **Destruction:** **NIST 800-88** (clear/purge/destroy) or **crypto-shredding**; **every copy** incl. backups; **certificate of destruction**.

**On the exam**

- Changes since last backup of any type → **incremental** · since last full → **differential**
- Fastest restore → **full** · fastest backup → **incremental** · last full + latest only → **differential**
- 3 copies / 2 media / 1 off-site → **3-2-1**
- Ransomware encrypted backups too → **offline / immutable** backups
- Untested backups → **test restores**
- **Trap:** incremental = fast backup, slow restore; differential = reverse.

**Hooks**

**Full = whole book nightly; incremental = only today's new page; differential = every page since the last full book. Incremental restore = every link in the chain; differential = the book + one bookmark. 3-2-1 = three copies, two media, one far away (+ one locked offline).**

**Quick check:** (1) Full Sunday + differential other days; server dies Friday morning: which backups to restore? (2) Ransomware encrypts servers AND the network-connected backup drive: what backup would have saved them?

**Answer:** Sunday full + Thursday differential: correct. Said 3-2-1 for ransomware: refined to OFFLINE/IMMUTABLE copy (3-2-1-1-0).

</details>

<a name="t-4-3-18"></a>
**Secure retention, retrieval, destruction**

Keep data only as long as required and destroy it properly.

> On the exam: What it is: keeping data only as long as needed, getting it back securely when required (with access control and logging), and destroying it properly at the end.
Scenario cue: 'old backups still contain customer data past retention' → retention must cover backups too.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 7: Backups and retention (topics 17, 18)**

**17. Backup types**

- **Full:** everything every time. Fastest/simplest **restore**; slowest backup, most storage.
- **Incremental:** changes since the **last backup of any kind**. Fastest backup, smallest; **slowest restore** (last full + EVERY incremental since, in order; one missing link breaks it).
- **Differential:** changes since the **last FULL**; grows daily. Restore = **last full + latest differential** (2 sets). Middle ground.
- Example: full Sunday, crash Thursday → incremental = full + Mon + Tue + Wed; differential = full + Wed.
- **Archive bit:** full + incremental **clear** it; differential **doesn't** (so it re-copies everything since the full).
- **3-2-1:** 3 copies, 2 media types, 1 off-site. **3-2-1-1-0:** + 1 **offline/immutable**, 0 errors on test restores.
- **Ransomware hunts connected backups** → **offline (air-gapped) or immutable** copy lets you recover without paying. Always-connected off-site (synced cloud) can be encrypted too.
- Encrypt backups (protect keys); restrict + log access; **test restores**; frequency from **RPO**, restore speed vs **RTO**.

**18. Secure retention, retrieval and destruction**

- **Retention:** follow the schedule (legal minimum, privacy maximum); **legal hold** overrides; includes **backups** (old backups with deleted customers = GDPR issue).
- **Retrieval:** authorized, **logged**, **integrity checks** (hashes); legal evidence → **chain of custody**.
- **Destruction:** **NIST 800-88** (clear/purge/destroy) or **crypto-shredding**; **every copy** incl. backups; **certificate of destruction**.

**On the exam**

- Changes since last backup of any type → **incremental** · since last full → **differential**
- Fastest restore → **full** · fastest backup → **incremental** · last full + latest only → **differential**
- 3 copies / 2 media / 1 off-site → **3-2-1**
- Ransomware encrypted backups too → **offline / immutable** backups
- Untested backups → **test restores**
- **Trap:** incremental = fast backup, slow restore; differential = reverse.

**Hooks**

**Full = whole book nightly; incremental = only today's new page; differential = every page since the last full book. Incremental restore = every link in the chain; differential = the book + one bookmark. 3-2-1 = three copies, two media, one far away (+ one locked offline).**

**Quick check:** (1) Full Sunday + differential other days; server dies Friday morning: which backups to restore? (2) Ransomware encrypts servers AND the network-connected backup drive: what backup would have saved them?

**Answer:** Taught.

</details>

<a name="t-4-3-19"></a>
**Digital certificates in detail** (review)

An X.509 certificate binds a public key to an identity, signed by a CA. Contains subject, issuer, public key, validity dates, serial number, extensions.

> On the exam: Chain of trust: root CA → intermediate CA → end-entity certificate. Self-signed certificates have no trusted third party. Certificate pinning makes an app accept only a specific certificate or key.
Scenario cue: 'browser warns the certificate isn't trusted' → issuer not in the trust store, expired, or name mismatch.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 1: PKI and digital certificates (topics 1 + 19)**

**Why PKI exists**

Asymmetric crypto: **public key** shared, **private key** secret. Problem: how do you know a public key really belongs to the bank? → a **digital certificate**: a trusted third party vouches the **public key belongs to this identity**.

**The PKI cast**

- **CA (Certificate Authority):** **issues and signs** certificates (DigiCert, Let's Encrypt).
  - **Root CA:** top of trust chain; **self-signed**; in OS/browser **trust store**; private key kept **OFFLINE**, often in an **HSM**.
  - **Intermediate (subordinate) CA:** signed by root; does day-to-day issuing; if compromised, only it is revoked.
- **RA (Registration Authority):** **checks identity**, then tells the CA to issue. **RA verifies; CA signs.**
- **Chain of trust:** site cert → intermediate CA → root CA (trust store).
- **Repository:** publishes certs + revocation info.

**What's inside an X.509 (v3) certificate**

Subject (who) · Issuer (which CA) · **subject's PUBLIC key** · serial number · validity (not before / not after) · signature algorithm + **CA's signature** · extensions: **SAN** (extra domain names), **key usage**, **basic constraints** (may it act as a CA? website cert = no).

**A certificate contains the PUBLIC key (that's its purpose), NEVER the private key.**

**Lifecycle**

Generate key pair (private stays with you) → **CSR** (certificate signing request) → RA verifies, CA signs → use → renew → **revoke** early if needed (private key stolen, name change).

**Revocation**

- **CRL:** CA publishes a **list** of revoked serials, **periodically** (big, can be stale).
- **OCSP:** browser **asks in real time** (good / revoked / unknown); downsides: delay, privacy leak, often **fails open** if down.
- **OCSP stapling:** the **website** attaches a fresh OCSP response to the TLS handshake (faster, private, reliable).

**Validation levels**

**DV** (controls the domain; Let's Encrypt) · **OV** (organization checked) · **EV** (strictest).

**Other**

- **Self-signed** cert: no CA vouching; OK for internal testing; browsers warn publicly (root certs are self-signed but pre-installed).
- **Certificate pinning** (4.1). **Private keys in HSM/vault**; stolen private key = impersonation until revoked → revoke + new key pair + new cert.

**On the exam**

- Verifies identity before issuing → **RA** · issues and signs → **CA**
- Real-time revocation check → **OCSP** · periodic list → **CRL** · site attaches status → **OCSP stapling**
- Extra domain names → **SAN** · root CA key → **offline in an HSM**
- **Traps:** certificate holds the PUBLIC key, never the private key; valid signature + dates ≠ trustworthy (could be revoked).

**Hooks**

**CA = passport office; RA = clerk checking your documents. Certificate = ID card showing your public key, stamped by the office. CRL = printed list of stolen passports; OCSP = phone call to check one now; stapling = you bring a fresh letter. Root CA = boss locked in the vault; intermediates = managers doing daily work.**

**Quick check:** (1) Web server private key stolen: what must happen to its certificate, how do browsers find out? (2) Who checks a requester's identity, who signs the certificate?

**Answer:** Revoke + CRL correct (also OCSP). Said certificates don't have the public key: WRONG, a certificate binds the PUBLIC key to an identity; never contains the private key. Marked shaky.

</details>

<a name="t-4-3-20"></a>
**Virtualization security**

Risks: VM escape, VM sprawl (forgotten VMs), insecure snapshots containing sensitive data, hypervisor vulnerabilities, shared resources between VMs.

> On the exam: Controls: patch hypervisors, isolate management interfaces, control and encrypt snapshots, track all VMs, segment VM networks.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 3: Virtualization and infrastructure (topics 5, 6, 20, 7)**

Layers of isolation, and what breaks through them.

**5. Hypervisors**

**Hypervisor (VMM)** creates/runs VMs.

- **Type 1 (bare metal):** directly on hardware, no host OS (ESXi, Hyper-V, Xen, KVM). **More secure + faster**; data centers/cloud.
- **Type 2 (hosted):** an app on a normal OS (VirtualBox, VMware Workstation, Parallels). **Less secure** (host OS compromise exposes all VMs); desktops/testing.
- **VM escape:** code in a VM breaks out to the hypervisor → other VMs/host; worst case in multitenant cloud.

*Hook: Type 1 = the foundation; Type 2 = renting a room in someone else's house.*

**6. Containers**

- **Share the host kernel** (VMs have their own OS) → one kernel flaw hits all (**container escape**).
- Image: **scan**, minimal base, **sign + verify**, trusted registries. Runtime: **not root**, read-only FS, drop capabilities, resource limits. No secrets in images.

*VM = separate house; container = apartment (shared foundation).*

**20. Virtualization security**

- **VM escape** · **VM sprawl** (forgotten, unpatched, ownerless VMs → inventory, owners, lifecycle policies)
- **Insecure snapshots:** whole VM state incl. **memory** (passwords, keys, decrypted data) → encrypt, restrict, delete old (remanence)
- **Hypervisor = high-value target** → patch, restrict + monitor admin access
- **Inter-VM traffic blind spots** (never crosses a physical network) → **virtual firewalls / microsegmentation**
- **Noisy neighbor** resource exhaustion (availability)

**7. Infrastructure as code (IaC)**

Infrastructure in templates (Terraform, CloudFormation, Ansible).

- Benefits: **repeatable** (baseline), **version-controlled + reviewed** (change mgmt), **scannable before deploy** (public bucket, open 22, `*` permissions) = **policy as code**.
- Risks: secrets in templates (vault + scanning); bad template spreads everywhere (review + gates); **configuration drift** (manual live change) → **drift detection + re-apply the template**; needed changes go **in the code** via review. **Immutable infrastructure** = replace, don't patch live.

**On the exam**

- On hardware, cloud → **Type 1** · app on desktop OS → **Type 2**
- Breaks out to host → **VM escape** · forgotten VMs → **VM sprawl**
- Snapshot has passwords from memory → **insecure snapshots**
- Inter-VM traffic unseen → microsegmentation · containers less isolated → **share kernel**
- Scan Terraform before deploy → **IaC scanning / policy as code**
- Live servers ≠ IaC → **drift** → re-apply template
- **Trap:** Type 2 is LESS secure.

**Hooks**

**Type 1 = foundation; Type 2 = renting a room. Snapshot = a photo of the whole VM incl. memory secrets. IaC drift → restore from the code, never edit the code to match the drift.**

**Quick check:** (1) Max isolation + performance for customer VMs: which hypervisor type? (2) Prod VM snapshots on a shared drive: risk? (3) Port 22 opened manually on a Terraform-managed server: name + fix?

**Answer:** Insecure snapshots. Correct.

</details>

<a name="t-4-3-21"></a>
**Directories and LDAP**

Directory services (Active Directory, LDAP) store identities and attributes. Metadirectories synchronize several directories into one; virtual directories present a single view without copying data.

> On the exam: Security: protect LDAP with TLS (LDAPS), least-privilege bind accounts, prevent LDAP injection.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 8: Identity infrastructure (topics 21, 22)**

**21. Directories and LDAP**

- **Directory** = central tree-structured database of identities/resources (users, groups, computers); apps ask it instead of keeping their own lists.
- **LDAP** = standard protocol to read/search directories. Entries named by a **Distinguished Name (DN)**: `cn=Ali,ou=Engineering,dc=company,dc=com`.
- **Active Directory** = most common directory (speaks LDAP, uses **Kerberos**).
- **Ports: LDAP 389 (unencrypted) · LDAPS 636 (TLS) · StartTLS upgrades 389.**
- Risks/controls: **simple bind sends passwords in clear text** over plain LDAP → anyone **sniffing** reads it → **LDAPS/StartTLS**; **anonymous bind** leaks usernames/org → disable; **LDAP injection** (`*)(uid=*` changes filter logic) → **escape/validate input** (encryption does NOT fix injection); over-privileged service accounts → least privilege (read-only, limited scope).
- Benefit: one place to manage identities; disabling a leaver cuts every connected app (JML).

**22. Credential and password management**

- **User passwords:** salted slow hashes (bcrypt, Argon2, scrypt), never encrypted.
- **NIST SP 800-63B:** length over complexity (≥8, allow long passphrases); **check breached-password lists**; **no forced periodic changes**; **no complex composition rules**.
- **MFA**; **rate limiting + lockout** vs brute force and **credential stuffing** (leaked pairs from other sites, password reuse); password managers; **FIDO2 / passkeys** = passwordless, **phishing-resistant**.
- **Machine secrets:** no hardcoding; vault; rotate (immediately after leak); separate per connection; no default creds; admin creds under PAM.

**On the exam**

- Query a central user directory → **LDAP** · LDAP over TLS, 636 → **LDAPS**
- Anyone can list usernames → **anonymous bind** · `*)(uid=*` in login → **LDAP injection**
- Leaked pairs from another site → **credential stuffing** → MFA + breached checks + rate limiting
- NIST on password changes → **no forced periodic changes** · phishing-resistant no-password → **FIDO2/passkeys**
- **Traps:** passwords hashed, never encrypted; port 389 unencrypted; risk of simple bind on 389 = cleartext sniffing (not injection).

**Hooks**

**Directory = company phone book; LDAP = how you look it up. 389 = plain, 636 = protected. Credential stuffing = trying stolen keys from one house on every other house.**

**Quick check:** (1) App uses port 389 with simple bind: risk + fix? (2) Leaked gaming-site credentials tried on a bank login: attack + two defenses?

**Answer:** Fix LDAPS correct; named the risk LDAP injection (actual: cleartext password sniffing; injection is a separate input problem).

</details>

<a name="t-4-3-22"></a>
**Credential and password management**

Managing passwords, keys, certificates and tokens: strong password policy, secure storage (salted hashes, vaults), rotation, no hardcoding, password managers, MFA, single sign-on.

> On the exam: Modern guidance (NIST 800-63B): favor length over complexity rules, check against breached password lists, avoid forced periodic changes unless compromise is suspected.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 8: Identity infrastructure (topics 21, 22)**

**21. Directories and LDAP**

- **Directory** = central tree-structured database of identities/resources (users, groups, computers); apps ask it instead of keeping their own lists.
- **LDAP** = standard protocol to read/search directories. Entries named by a **Distinguished Name (DN)**: `cn=Ali,ou=Engineering,dc=company,dc=com`.
- **Active Directory** = most common directory (speaks LDAP, uses **Kerberos**).
- **Ports: LDAP 389 (unencrypted) · LDAPS 636 (TLS) · StartTLS upgrades 389.**
- Risks/controls: **simple bind sends passwords in clear text** over plain LDAP → anyone **sniffing** reads it → **LDAPS/StartTLS**; **anonymous bind** leaks usernames/org → disable; **LDAP injection** (`*)(uid=*` changes filter logic) → **escape/validate input** (encryption does NOT fix injection); over-privileged service accounts → least privilege (read-only, limited scope).
- Benefit: one place to manage identities; disabling a leaver cuts every connected app (JML).

**22. Credential and password management**

- **User passwords:** salted slow hashes (bcrypt, Argon2, scrypt), never encrypted.
- **NIST SP 800-63B:** length over complexity (≥8, allow long passphrases); **check breached-password lists**; **no forced periodic changes**; **no complex composition rules**.
- **MFA**; **rate limiting + lockout** vs brute force and **credential stuffing** (leaked pairs from other sites, password reuse); password managers; **FIDO2 / passkeys** = passwordless, **phishing-resistant**.
- **Machine secrets:** no hardcoding; vault; rotate (immediately after leak); separate per connection; no default creds; admin creds under PAM.

**On the exam**

- Query a central user directory → **LDAP** · LDAP over TLS, 636 → **LDAPS**
- Anyone can list usernames → **anonymous bind** · `*)(uid=*` in login → **LDAP injection**
- Leaked pairs from another site → **credential stuffing** → MFA + breached checks + rate limiting
- NIST on password changes → **no forced periodic changes** · phishing-resistant no-password → **FIDO2/passkeys**
- **Traps:** passwords hashed, never encrypted; port 389 unencrypted; risk of simple bind on 389 = cleartext sniffing (not injection).

**Hooks**

**Directory = company phone book; LDAP = how you look it up. 389 = plain, 636 = protected. Credential stuffing = trying stolen keys from one house on every other house.**

**Quick check:** (1) App uses port 389 with simple bind: risk + fix? (2) Leaked gaming-site credentials tried on a bank login: attack + two defenses?

**Answer:** Credential stuffing; rate limiting + MFA. Correct.

</details>

<a name="t-4-3-23"></a>
**Ring protection**

CPU privilege levels shown as rings: Ring 0 (kernel, most privileged) to Ring 3 (user applications, least). Lower number = more privilege.

> On the exam: Scenario cue: 'malware that runs in Ring 0' → kernel-level rootkit, hardest to detect.
Rule: applications should run in Ring 3 (user mode).

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 4: Trusted computing (topics 8, 9, 10, 23, 24)**

Classic definition-and-property terms that nest together.

**The bank picture (simplest way to hold it)**

- **TCB** = everything security depends on (guards, vault, locks, alarm); any failure = bank unsafe.
- **Reference monitor** = the RULE that every person entering the vault passes the guard's check; no side doors.
- **Security kernel** = the actual guard following that rule.
- **Rings** = who can go where: manager (**Ring 0, kernel**) everywhere; customers (**Ring 3, apps**) stay in the lobby and must ASK a teller (**system call**).
- **TPM** = small safe welded into the foundation, holding keys + a logbook of what came in at opening (boot).

**8. TPM (Trusted Platform Module)**

Security chip on the motherboard/CPU; keys generated/kept inside, can't be copied out.

- **Endorsement key (EK)**: factory-burned, unique identity · **Storage root key (SRK)**: protects other keys
- **Measured boot**: each boot component hashed into **PCRs** (records what booted)
- **SEALED STORAGE**: data/keys released ONLY if boot measurements match (**BitLocker**)
- **Remote attestation**: prove to a server the machine booted cleanly
- Random number generation
- **Secure boot = gatekeeper (blocks unsigned). Measured boot = flight recorder (records for later checks).**
- **TPM** = cheap chip inside one device · **HSM** = dedicated appliance for many keys (root CA, payments)

**9. TCB (Trusted Computing Base)**

All hardware/firmware/software that **enforces the security policy** (CPU protections, kernel, TPM, authentication, access control). Compromise any part = whole system fails. **Keep it small** (economy of mechanism).

**Security perimeter** = boundary between TCB and everything untrusted.

**10. Reference monitor**

**Abstract concept**: every subject → object access must be checked. Properties: **tamper-proof**, **always invoked** (no bypass = complete mediation), **small enough to verify**.

**NEAT = Non-bypassable, Evaluable, Always invoked, Tamper-proof.**

**Security kernel** = the actual implementation of the reference monitor (inside the TCB).

**23. Ring protection**

- **Ring 0** = most privileged = **OS kernel** · Rings 1–2 = drivers/services (rarely used) · **Ring 3** = least = **user apps**.
- Outer rings can't touch inner memory/hardware directly; must use a **system call**.
- **Privilege escalation** = Ring 3 → Ring 0 (Meltdown broke this wall). Hypervisor = "**Ring −1**".
- **Lower ring number = more power.**

**24. Together**

TCB (edge = security perimeter) ⊃ security kernel (implements the reference monitor) · rings enforce privilege (kernel Ring 0, apps Ring 3) · TPM anchors trust in hardware (measured boot, attestation) · **trust boundary** = anywhere trust changes; every crossing needs checks (DFDs in 4.4).

**On the exam**

- Stores keys + records boot measurements for attestation → **TPM**
- Disk key released only if boot unchanged → **sealed storage**
- Blocks unsigned bootloaders → **secure boot** · records hashes → **measured boot**
- All components enforcing policy → **TCB** · boundary trusted/untrusted → **security perimeter**
- Mediates every access; tamper-proof, always invoked, verifiable → **reference monitor**
- Implementation of the reference monitor → **security kernel**
- Most privileged ring → **Ring 0** · user apps → **Ring 3**
- **Traps:** reference monitor = CONCEPT; security kernel = IMPLEMENTATION. Lower ring = more privilege.

**Hooks**

**TPM = tiny safe welded to the motherboard + boot flight recorder. TCB = everything you must trust; keep it small. Reference monitor = NEAT. Rings: 0 = king, 3 = citizens.**

**Quick check:** (1) Three properties of a reference monitor? (2) Disk key released only if TPM confirms boot unchanged: which feature? (3) Kernel ring vs app ring? Re-check: which ring has most privilege?

**Answer:** King (Ring 0) and citizens (Ring 3); re-check Ring 0 = most privilege. Correct.

</details>

<a name="t-4-3-24"></a>
**Trusted computing concepts together** (review)

Ring protection (privilege levels), trust boundary/security perimeter (where trust changes), TCB (everything enforcing the policy), reference monitor (concept that mediates all access), security kernel (its implementation).

> On the exam: Scenario cue: 'which concept must be tamper-proof, always invoked and verifiable?' → reference monitor.

<details><summary>Lesson (21 Oct 2026)</summary>

**4.3 Lesson 4: Trusted computing (topics 8, 9, 10, 23, 24)**

Classic definition-and-property terms that nest together.

**The bank picture (simplest way to hold it)**

- **TCB** = everything security depends on (guards, vault, locks, alarm); any failure = bank unsafe.
- **Reference monitor** = the RULE that every person entering the vault passes the guard's check; no side doors.
- **Security kernel** = the actual guard following that rule.
- **Rings** = who can go where: manager (**Ring 0, kernel**) everywhere; customers (**Ring 3, apps**) stay in the lobby and must ASK a teller (**system call**).
- **TPM** = small safe welded into the foundation, holding keys + a logbook of what came in at opening (boot).

**8. TPM (Trusted Platform Module)**

Security chip on the motherboard/CPU; keys generated/kept inside, can't be copied out.

- **Endorsement key (EK)**: factory-burned, unique identity · **Storage root key (SRK)**: protects other keys
- **Measured boot**: each boot component hashed into **PCRs** (records what booted)
- **SEALED STORAGE**: data/keys released ONLY if boot measurements match (**BitLocker**)
- **Remote attestation**: prove to a server the machine booted cleanly
- Random number generation
- **Secure boot = gatekeeper (blocks unsigned). Measured boot = flight recorder (records for later checks).**
- **TPM** = cheap chip inside one device · **HSM** = dedicated appliance for many keys (root CA, payments)

**9. TCB (Trusted Computing Base)**

All hardware/firmware/software that **enforces the security policy** (CPU protections, kernel, TPM, authentication, access control). Compromise any part = whole system fails. **Keep it small** (economy of mechanism).

**Security perimeter** = boundary between TCB and everything untrusted.

**10. Reference monitor**

**Abstract concept**: every subject → object access must be checked. Properties: **tamper-proof**, **always invoked** (no bypass = complete mediation), **small enough to verify**.

**NEAT = Non-bypassable, Evaluable, Always invoked, Tamper-proof.**

**Security kernel** = the actual implementation of the reference monitor (inside the TCB).

**23. Ring protection**

- **Ring 0** = most privileged = **OS kernel** · Rings 1–2 = drivers/services (rarely used) · **Ring 3** = least = **user apps**.
- Outer rings can't touch inner memory/hardware directly; must use a **system call**.
- **Privilege escalation** = Ring 3 → Ring 0 (Meltdown broke this wall). Hypervisor = "**Ring −1**".
- **Lower ring number = more power.**

**24. Together**

TCB (edge = security perimeter) ⊃ security kernel (implements the reference monitor) · rings enforce privilege (kernel Ring 0, apps Ring 3) · TPM anchors trust in hardware (measured boot, attestation) · **trust boundary** = anywhere trust changes; every crossing needs checks (DFDs in 4.4).

**On the exam**

- Stores keys + records boot measurements for attestation → **TPM**
- Disk key released only if boot unchanged → **sealed storage**
- Blocks unsigned bootloaders → **secure boot** · records hashes → **measured boot**
- All components enforcing policy → **TCB** · boundary trusted/untrusted → **security perimeter**
- Mediates every access; tamper-proof, always invoked, verifiable → **reference monitor**
- Implementation of the reference monitor → **security kernel**
- Most privileged ring → **Ring 0** · user apps → **Ring 3**
- **Traps:** reference monitor = CONCEPT; security kernel = IMPLEMENTATION. Lower ring = more privilege.

**Hooks**

**TPM = tiny safe welded to the motherboard + boot flight recorder. TCB = everything you must trust; keep it small. Reference monitor = NEAT. Rings: 0 = king, 3 = citizens.**

**Quick check:** (1) Three properties of a reference monitor? (2) Disk key released only if TPM confirms boot unchanged: which feature? (3) Kernel ring vs app ring? Re-check: which ring has most privilege?

**Answer:** Taught; marked shaky (new).

</details>

<a name="t-4-3-25"></a>
**Code access security and type safety**

Code access security (.NET) grants permissions based on the code's identity and origin, not just the user's. Type safety means code can only access memory in allowed, well-defined ways, preventing many memory errors.

> On the exam: Scenario cue: 'downloaded code should run with fewer permissions than local code' → code access security.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 6: Runtimes and operating systems (topics 14, 15, 25, 16, 26)**

Who manages memory, and OS-level controls that contain damage.

**14. Managed runtimes**

Runtime manages memory/checks code (**JVM**, **.NET CLR**, Python, JS, Go).

- **Garbage collection** (no use-after-free/double-free) · **bounds checking** (exception instead of overflow) · **type checking** · sandboxing.
- But: runtime itself can be vulnerable (patch); **native code** via JNI / P/Invoke loses protections; **logic flaws** (SQLi, broken access control) still happen.

**15. Managed vs unmanaged code**

- **Managed** (Java, C#) vs **unmanaged/native** (**C, C++**: you manage memory) → **buffer overflows, use-after-free, integer overflows, format string bugs**.
- Defenses: **ASLR** (random memory layout), **DEP/NX** (data areas non-executable), **stack canaries** (detect overwrite of return address), safe functions (no `strcpy`/`gets`), SAST + fuzzing.
- **Memory-safe languages** (Rust, Go, Java, C#) recommended by governments: eliminate whole bug classes.

**25. Code access security (CAS) and type safety**

- **Type safety:** data only used as its correct type; prevents memory attacks; enforced by managed runtimes.
- **CAS (.NET, deprecated):** permissions for **code based on its origin/signer/zone**, not just who runs it (Java Security Manager similar, deprecated).

**16. OS controls**

Process isolation · normal-user/least privilege (UAC) · file permissions/ACLs · ASLR + DEP · sandboxing · patching, hardening, host firewall, logging.

**26. Security-oriented operating systems**

- **DAC (Discretionary):** the **owner decides** access (normal Windows/Linux permissions); malware running as you gets everything you can access.
- **MAC (Mandatory):** **system enforces a central policy** nobody can override (not root, not the owner).
- **SELinux** (NSA; Red Hat, Fedora, Android): labels processes/files; policy says what each process may touch (hacked web server still can't read `/etc/shadow`).
- **AppArmor** (Ubuntu, SUSE): simpler, **path-based profiles** per program.
- Trusted/high-assurance OSes (formally verified **seL4** microkernel) → small TCB / reference monitor ideas.
- **MAC CONTAINS a compromise.**

**On the exam**

- Bounds checking blocks overflows → **managed code** · C/C++ overflows → **unmanaged**
- Random memory addresses → **ASLR** · non-executable memory → **DEP/NX** · detects stack overwrite → **stack canaries**
- Permissions by where code came from → **CAS**
- Owner decides → **DAC** · central policy even root can't override → **MAC**
- NSA Linux MAC module → **SELinux** · path profiles, Ubuntu → **AppArmor**
- **Traps:** managed code still has logic flaws; native calls lose protections.

**Hooks**

**Managed = a babysitter for memory. ASLR = shuffling the rooms; DEP = no running in the data rooms; canary = the bird that warns you. Discretionary = owner's Decision; Mandatory = Must follow the law.**

**Quick check:** (1) Hacked web server on SELinux still can't read the password file: which model, why? (2) Which protection randomizes memory placement? (3) Why do governments recommend memory-safe languages?

**Answer:** Taught.

</details>

<a name="t-4-3-26"></a>
**Security-oriented operating systems** (review)

Operating systems with built-in mandatory access control and hardening, such as SELinux, AppArmor or trusted OS variants.

> On the exam: Scenario cue: 'enforce MAC policies on a Linux server' → SELinux or AppArmor.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.3 Lesson 6: Runtimes and operating systems (topics 14, 15, 25, 16, 26)**

Who manages memory, and OS-level controls that contain damage.

**14. Managed runtimes**

Runtime manages memory/checks code (**JVM**, **.NET CLR**, Python, JS, Go).

- **Garbage collection** (no use-after-free/double-free) · **bounds checking** (exception instead of overflow) · **type checking** · sandboxing.
- But: runtime itself can be vulnerable (patch); **native code** via JNI / P/Invoke loses protections; **logic flaws** (SQLi, broken access control) still happen.

**15. Managed vs unmanaged code**

- **Managed** (Java, C#) vs **unmanaged/native** (**C, C++**: you manage memory) → **buffer overflows, use-after-free, integer overflows, format string bugs**.
- Defenses: **ASLR** (random memory layout), **DEP/NX** (data areas non-executable), **stack canaries** (detect overwrite of return address), safe functions (no `strcpy`/`gets`), SAST + fuzzing.
- **Memory-safe languages** (Rust, Go, Java, C#) recommended by governments: eliminate whole bug classes.

**25. Code access security (CAS) and type safety**

- **Type safety:** data only used as its correct type; prevents memory attacks; enforced by managed runtimes.
- **CAS (.NET, deprecated):** permissions for **code based on its origin/signer/zone**, not just who runs it (Java Security Manager similar, deprecated).

**16. OS controls**

Process isolation · normal-user/least privilege (UAC) · file permissions/ACLs · ASLR + DEP · sandboxing · patching, hardening, host firewall, logging.

**26. Security-oriented operating systems**

- **DAC (Discretionary):** the **owner decides** access (normal Windows/Linux permissions); malware running as you gets everything you can access.
- **MAC (Mandatory):** **system enforces a central policy** nobody can override (not root, not the owner).
- **SELinux** (NSA; Red Hat, Fedora, Android): labels processes/files; policy says what each process may touch (hacked web server still can't read `/etc/shadow`).
- **AppArmor** (Ubuntu, SUSE): simpler, **path-based profiles** per program.
- Trusted/high-assurance OSes (formally verified **seL4** microkernel) → small TCB / reference monitor ideas.
- **MAC CONTAINS a compromise.**

**On the exam**

- Bounds checking blocks overflows → **managed code** · C/C++ overflows → **unmanaged**
- Random memory addresses → **ASLR** · non-executable memory → **DEP/NX** · detects stack overwrite → **stack canaries**
- Permissions by where code came from → **CAS**
- Owner decides → **DAC** · central policy even root can't override → **MAC**
- NSA Linux MAC module → **SELinux** · path profiles, Ubuntu → **AppArmor**
- **Traps:** managed code still has logic flaws; native calls lose protections.

**Hooks**

**Managed = a babysitter for memory. ASLR = shuffling the rooms; DEP = no running in the data rooms; canary = the bird that warns you. Discretionary = owner's Decision; Mandatory = Must follow the law.**

**Quick check:** (1) Hacked web server on SELinux still can't read the password file: which model, why? (2) Which protection randomizes memory placement? (3) Why do governments recommend memory-safe languages?

**Answer:** I said discretionary with the MAC reason ("nobody overrides the law"): name is MANDATORY (MAC). Marked shaky.

</details>

## 4.4 Threat modeling

<a name="t-4-4-1"></a>
**Threat modeling steps**

Identify assets, decompose the app, identify threats, rate them, mitigate, validate.

> On the exam: Typical steps: 1) define scope and assets, 2) diagram the system (DFD) with trust boundaries, 3) identify threats (STRIDE), 4) rate them (CVSS/DREAD), 5) choose mitigations, 6) validate and update.
When: during design, and again whenever the design changes.
Scenario cue: 'what's the best time to threat model?' → design phase, before code is written.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 1: Steps, DFDs and trust boundaries (topics 1, 2, 13)**

Threat modeling = thinking like an attacker at design time.

**1. Threat modeling steps**

**Shostack's 4 questions:** What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?

**Detailed steps:** 1 identify **security objectives** → 2 **decompose/model** (DFDs, assets, trust boundaries, entry/exit points) → 3 **identify threats** (STRIDE) → 4 **rate/rank** (DREAD, CVSS, likelihood × impact) → 5 **mitigate** (or accept/transfer/avoid) → 6 **validate + iterate**.

- **When:** design phase (SDL Design; cheapest). **Living document**: update when design/threats change.
- **Who:** team (architects, devs, security, testers).

**2. DFDs and trust boundaries**

- **External entity = rectangle** (outside your control: user, partner, browser)
- **Process = circle** (code doing work)
- **Data store = two parallel lines** (DB, file, cache, log)
- **Data flow = arrow**
- **Trust boundary = dashed line** (where trust changes: internet → web server, web → DB, Ring 3 → Ring 0, company → partner API)
- **Threats cluster where data flows CROSS trust boundaries** → authn, authz, validation, encryption there.
- **Level 0** = context diagram (whole system as one bubble); **Level 1, 2…** = zoom in.

**13. Entry points, exit points, privileged functions**

- **Entry points:** UI forms, APIs, file uploads, URL params, cookies, headers, queues, open ports, config files, env vars → validate input.
- **Exit points:** web pages, API responses, **error messages**, **logs**, exports, emails → **information disclosure** (stack traces, PII in logs).
- **Privileged functions:** admin panels, role management, **password reset**, payments, config, export → closest scrutiny (MFA, re-auth, logging).
- Together = the **attack surface**.

**On the exam**

- First step → **identify security objectives** · main decomposition diagram → **DFD**
- Rectangle = external entity · circle = process · parallel lines = data store · dashed = trust boundary
- Threats concentrate → **trust boundary crossings**
- Login/API/upload → entry · error messages/logs → exit · password reset/admin → privileged
- Update the model → whenever the design changes
- **Trap:** threat modeling is a DESIGN-phase activity.

**Hooks**

**DFD shapes: Rectangle = outsider, Circle = worker, Parallel lines = storage shelf, Arrow = moving data, Dashed line = border control. Trust boundary = border crossing where you check passports.**

**Quick check:** (1) What does a dashed line in a DFD represent, why focus on it? (2) Classify: file upload form / detailed stack-trace error / reset-any-user's-password admin feature.

**Answer:** Trust boundary, threats cluster at crossings; entry, exit, privileged function. All correct.

</details>

<a name="t-4-4-2"></a>
**Data flow diagrams (DFD) and trust boundaries**

Show where data crosses between trust levels; threats cluster there.

> On the exam: DFD elements: external entity (user, other system), process, data store, data flow, trust boundary.
Trust boundary: where data moves between different trust levels (internet to web server, app to database). Threats concentrate at boundaries, so validate and authenticate there.
Scenario cue: 'where should input validation happen?' → where data crosses a trust boundary.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 1: Steps, DFDs and trust boundaries (topics 1, 2, 13)**

Threat modeling = thinking like an attacker at design time.

**1. Threat modeling steps**

**Shostack's 4 questions:** What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?

**Detailed steps:** 1 identify **security objectives** → 2 **decompose/model** (DFDs, assets, trust boundaries, entry/exit points) → 3 **identify threats** (STRIDE) → 4 **rate/rank** (DREAD, CVSS, likelihood × impact) → 5 **mitigate** (or accept/transfer/avoid) → 6 **validate + iterate**.

- **When:** design phase (SDL Design; cheapest). **Living document**: update when design/threats change.
- **Who:** team (architects, devs, security, testers).

**2. DFDs and trust boundaries**

- **External entity = rectangle** (outside your control: user, partner, browser)
- **Process = circle** (code doing work)
- **Data store = two parallel lines** (DB, file, cache, log)
- **Data flow = arrow**
- **Trust boundary = dashed line** (where trust changes: internet → web server, web → DB, Ring 3 → Ring 0, company → partner API)
- **Threats cluster where data flows CROSS trust boundaries** → authn, authz, validation, encryption there.
- **Level 0** = context diagram (whole system as one bubble); **Level 1, 2…** = zoom in.

**13. Entry points, exit points, privileged functions**

- **Entry points:** UI forms, APIs, file uploads, URL params, cookies, headers, queues, open ports, config files, env vars → validate input.
- **Exit points:** web pages, API responses, **error messages**, **logs**, exports, emails → **information disclosure** (stack traces, PII in logs).
- **Privileged functions:** admin panels, role management, **password reset**, payments, config, export → closest scrutiny (MFA, re-auth, logging).
- Together = the **attack surface**.

**On the exam**

- First step → **identify security objectives** · main decomposition diagram → **DFD**
- Rectangle = external entity · circle = process · parallel lines = data store · dashed = trust boundary
- Threats concentrate → **trust boundary crossings**
- Login/API/upload → entry · error messages/logs → exit · password reset/admin → privileged
- Update the model → whenever the design changes
- **Trap:** threat modeling is a DESIGN-phase activity.

**Hooks**

**DFD shapes: Rectangle = outsider, Circle = worker, Parallel lines = storage shelf, Arrow = moving data, Dashed line = border control. Trust boundary = border crossing where you check passports.**

**Quick check:** (1) What does a dashed line in a DFD represent, why focus on it? (2) Classify: file upload form / detailed stack-trace error / reset-any-user's-password admin feature.

**Answer:** Trust boundary, threats cluster at crossings; entry, exit, privileged function. All correct.

</details>

<a name="t-4-4-3"></a>
**STRIDE**

Spoofing (authN), Tampering (integrity), Repudiation (nonrepudiation), Information disclosure (confidentiality), Denial of service (availability), Elevation of privilege (authZ).

> On the exam: Spoofing → authentication. Tampering → integrity. Repudiation → nonrepudiation/logging. Information disclosure → confidentiality. Denial of service → availability. Elevation of privilege → authorization.
Scenario cue: 'attacker changes a price in a hidden form field' → Tampering. 'User denies placing an order and there are no logs' → Repudiation.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 2: STRIDE (topic 3)**

Microsoft's threat categories (step 3: identify threats). Each letter breaks one property.

| Letter | Threat | Attacker does | Property broken | Defense |

|---|---|---|---|---|

| S | Spoofing | pretends to be someone else | Authentication | MFA, strong authn, certificates |

| T | Tampering | changes data/code | Integrity | hashes, signatures/MACs, access control, validation |

| R | Repudiation | denies an action, you can't prove it | Nonrepudiation | secure audit logs, digital signatures |

| I | Information disclosure | sees data they shouldn't | Confidentiality | encryption, access control, minimal errors |

| D | Denial of service | makes it unavailable | Availability | rate limiting, redundancy, resource limits |

| E | Elevation of privilege | gets more power than allowed | Authorization | least privilege, authz checks, sandboxing |

**Plain-word pairs:** S = who are you? · T = is it unchanged? · R = can you prove it? · I = is it secret? · D = is it up? · E = are you allowed?

**STRIDE-per-element (with DFDs)**

- **External entity:** S, R ("sir")
- **Process:** all six
- **Data store:** T, I, D (+ R if it holds logs) ("tide")
- **Data flow:** T, I, D ("tide")

**Examples**

Stolen session cookie → S · price=100 → price=1 → T · "I never made that transfer," no logs → R · API error leaks others' emails → I · botnet crashes login → D · user exploits bug to become admin → E.

**On the exam**

- Match the action to the letter · tampering → integrity · repudiation → nonrepudiation (audit logs)
- Threats to a data flow → T, I, D
- **Trap:** stolen ADMIN credentials = **spoofing**; a normal user exploiting a bug to become admin = **elevation of privilege**.

**Hooks**

**Processes get everything; stores and flows get TIDe; outsiders get SiR.**

**Quick check:** STRIDE category: (1) employee deletes own audit entries, denies change (2) intercepted unencrypted traffic read (3) user edits hidden field to get admin role.

**Answer:** Repudiation; information disclosure (after considering spoofing); elevation of privilege. All correct.

</details>

<a name="t-4-4-4"></a>
**PASTA**

Process for Attack Simulation and Threat Analysis: seven stages, risk- and attacker-centric, tied to business impact.

> On the exam: Seven stages: define objectives, define technical scope, decompose the app, analyze threats, analyze vulnerabilities, model attacks, analyze risk and impact.
Strength: ties technical threats to business impact; attacker-centric and risk-centric.
Scenario cue: 'management wants threat modeling tied to business risk' → PASTA. 'Developers want a simple checklist per component' → STRIDE.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 3: PASTA + hTMM (topics 4, 5)**

**4. PASTA (Process for Attack Simulation and Threat Analysis)**

**7-stage, risk-centric** method: starts from the **business**, ends with **business risk**, simulates attacks. Attacker-centric (threat intelligence). Heaviest method → critical apps.

1. **Define business objectives** · 2. **Define technical scope** · 3. **Decompose the application** (DFDs, trust boundaries, entry points) · 4. **Threat analysis** (threat intel) · 5. **Vulnerability/weakness analysis** · 6. **Attack modeling/simulation** (**attack trees**) · 7. **Risk and impact analysis** (countermeasures)

**Mnemonic: "Do Dogs Always Think Very Angry Rabbits?"**

**5. hTMM (Hybrid Threat Modeling Method)**

From the **SEI (Carnegie Mellon)** (CMMI, OCTAVE). Combines:

1. **Security Cards** (prompt deck: motives, resources, methods, impacts) for structured brainstorming

2. **PnG (Persona non Grata)** = imagined attacker personas ("what would this person try?")

3. **STRIDE** to organize findings

Goals: **no false positives**, **consistent results**, **cost-effective**.

*hTMM = Hybrid = Cards + Characters + STRIDE.*

**Method comparison**

- **STRIDE** = threat **categories** (checklist), software/developer-focused
- **PASTA** = 7-stage **risk-centric** process, business impact
- **hTMM** = cards + personas + STRIDE
- **Trike** = risk-based, starts from a **requirements model** (who may do what to which asset)
- **VAST** = Visual, Agile, Simple; **scales** across enterprises / Agile-DevOps
- **OCTAVE** = organizational/operational, self-directed (2.8)
- **Attack trees** = goal at root, branches = ways (3.6)

**On the exam**

- Risk-centric 7 stages aligned with business → **PASTA** · Security Cards + PnG + STRIDE → **hTMM**
- Imagined attacker personas → **PnG** · PASTA stage using attack trees → **6 (attack modeling)**
- Scales for Agile across enterprise → **VAST**
- **Trap:** STRIDE is a category list, not a full risk process; business impact + stages = PASTA.

**Quick check:** (1) Bank wants method from business objectives through attack simulation to business risk? (2) Brainstorm with prompt cards + imagined attacker characters, organize with STRIDE?

**Answer:** PASTA; hTMM. Both correct.

</details>

<a name="t-4-4-5"></a>
**Hybrid Threat Modeling Method (hTMM)**

SEI method combining SQUARE, Security Cards and Persona non Grata.

> On the exam: What it is: SEI's method combining SQUARE (requirements), Security Cards (brainstorming) and Persona non Grata (attacker personas).
Goal: consistent results with fewer false positives and cost-effective threat identification.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 3: PASTA + hTMM (topics 4, 5)**

**4. PASTA (Process for Attack Simulation and Threat Analysis)**

**7-stage, risk-centric** method: starts from the **business**, ends with **business risk**, simulates attacks. Attacker-centric (threat intelligence). Heaviest method → critical apps.

1. **Define business objectives** · 2. **Define technical scope** · 3. **Decompose the application** (DFDs, trust boundaries, entry points) · 4. **Threat analysis** (threat intel) · 5. **Vulnerability/weakness analysis** · 6. **Attack modeling/simulation** (**attack trees**) · 7. **Risk and impact analysis** (countermeasures)

**Mnemonic: "Do Dogs Always Think Very Angry Rabbits?"**

**5. hTMM (Hybrid Threat Modeling Method)**

From the **SEI (Carnegie Mellon)** (CMMI, OCTAVE). Combines:

1. **Security Cards** (prompt deck: motives, resources, methods, impacts) for structured brainstorming

2. **PnG (Persona non Grata)** = imagined attacker personas ("what would this person try?")

3. **STRIDE** to organize findings

Goals: **no false positives**, **consistent results**, **cost-effective**.

*hTMM = Hybrid = Cards + Characters + STRIDE.*

**Method comparison**

- **STRIDE** = threat **categories** (checklist), software/developer-focused
- **PASTA** = 7-stage **risk-centric** process, business impact
- **hTMM** = cards + personas + STRIDE
- **Trike** = risk-based, starts from a **requirements model** (who may do what to which asset)
- **VAST** = Visual, Agile, Simple; **scales** across enterprises / Agile-DevOps
- **OCTAVE** = organizational/operational, self-directed (2.8)
- **Attack trees** = goal at root, branches = ways (3.6)

**On the exam**

- Risk-centric 7 stages aligned with business → **PASTA** · Security Cards + PnG + STRIDE → **hTMM**
- Imagined attacker personas → **PnG** · PASTA stage using attack trees → **6 (attack modeling)**
- Scales for Agile across enterprise → **VAST**
- **Trap:** STRIDE is a category list, not a full risk process; business impact + stages = PASTA.

**Quick check:** (1) Bank wants method from business objectives through attack simulation to business risk? (2) Brainstorm with prompt cards + imagined attacker characters, organize with STRIDE?

**Answer:** PASTA; hTMM. Both correct.

</details>

<a name="t-4-4-6"></a>
**DREAD**

Older rating scheme: damage, reproducibility, exploitability, affected users, discoverability.

> On the exam: Rates threats 1-10 on Damage, Reproducibility, Exploitability, Affected users, Discoverability.
Weakness: very subjective (different people give different scores); Microsoft stopped using it.
Scenario cue: 'which rating method is criticized as subjective?' → DREAD.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 4: Ranking threats: DREAD, CVSS, other methods (topics 6, 7, 11)**

**6. DREAD**

Score each threat 1–10 on 5 factors, then **average**:

- **D**amage potential (how bad?) · **R**eproducibility (how reliably repeated?) · **E**xploitability (how easy to launch?) · **A**ffected users (how many?) · **D**iscoverability (how easy to find?)
- Score = (D+R+E+A+D) ÷ 5; higher = fix sooner.
- Weaknesses: **subjective**; **discoverability** encourages **security through obscurity** (assumes attackers won't find it) → many always score it max; Microsoft moved away from DREAD.

*Hook: Damage? Repeat? Easy? Audience? Detect?*

**7. CVSS (Common Vulnerability Scoring System)**

Industry standard **0.0–10.0** for **known vulnerabilities**; maintained by **FIRST**; versions **3.1** and **4.0**; **NVD** publishes scores for **CVEs**.

- **Base:** built-in: exploitability (**attack vector** network/adjacent/local/physical, **attack complexity**, **privileges required**, **user interaction**), **impact** (C, I, A), **scope**.
- **Temporal (v3) / Threat (v4):** changes over time (public exploit? patch?).
- **Environmental:** adjusted for YOUR environment (asset criticality).
- **Severity:** None 0.0 · Low 0.1–3.9 · Medium 4.0–6.9 · **High 7.0–8.9** · **Critical 9.0–10.0**.
- CVSS base = technical severity, not business risk → environmental + criticality.
- **DREAD** = imagined threats at design time (subjective); **CVSS** = known vulnerabilities (standardized).

**11. Threat ranking methods**

Qualitative H/M/L + risk matrix (likelihood × impact) · quantitative (SLE/ALE) · probability × impact · DREAD · CVSS · **Delphi** · **bug bar** (must-fix threshold). Rank → mitigate highest first; record the rest in the **risk register**.

**On the exam**

- D/R/E/A/D factors → **DREAD** · main criticism → subjective (+ discoverability = obscurity)
- Standard 0–10 for published vulns → **CVSS** (FIRST) · 7.5 → **High** · 9.1 → **Critical**
- Adjust for how critical the system is → **environmental** · changes when exploit published → **temporal/threat**
- **Trap:** high CVSS ≠ automatically top business priority.

**Hooks**

**CVSS bands: Low &lt; 4, Medium 4–6.9, High 7–8.9, Critical 9+. Base = the bug itself; temporal/threat = the news about it; environmental = your house.**

**Quick check:** (1) CVSS 8.2 = which label? (2) Which DREAD factor encourages security through obscurity, why? (3) Which CVSS group adjusts for a server holding your most sensitive data?

**Answer:** High; discoverability (assumes attackers won't find it); environmental. All correct.

</details>

<a name="t-4-4-7"></a>
**CVSS**

Scores vulnerability severity 0-10 using base, temporal/threat and environmental metrics.

> On the exam: Base = built-in severity; environmental adjusts for your organization. CVSS measures severity, not risk.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 4: Ranking threats: DREAD, CVSS, other methods (topics 6, 7, 11)**

**6. DREAD**

Score each threat 1–10 on 5 factors, then **average**:

- **D**amage potential (how bad?) · **R**eproducibility (how reliably repeated?) · **E**xploitability (how easy to launch?) · **A**ffected users (how many?) · **D**iscoverability (how easy to find?)
- Score = (D+R+E+A+D) ÷ 5; higher = fix sooner.
- Weaknesses: **subjective**; **discoverability** encourages **security through obscurity** (assumes attackers won't find it) → many always score it max; Microsoft moved away from DREAD.

*Hook: Damage? Repeat? Easy? Audience? Detect?*

**7. CVSS (Common Vulnerability Scoring System)**

Industry standard **0.0–10.0** for **known vulnerabilities**; maintained by **FIRST**; versions **3.1** and **4.0**; **NVD** publishes scores for **CVEs**.

- **Base:** built-in: exploitability (**attack vector** network/adjacent/local/physical, **attack complexity**, **privileges required**, **user interaction**), **impact** (C, I, A), **scope**.
- **Temporal (v3) / Threat (v4):** changes over time (public exploit? patch?).
- **Environmental:** adjusted for YOUR environment (asset criticality).
- **Severity:** None 0.0 · Low 0.1–3.9 · Medium 4.0–6.9 · **High 7.0–8.9** · **Critical 9.0–10.0**.
- CVSS base = technical severity, not business risk → environmental + criticality.
- **DREAD** = imagined threats at design time (subjective); **CVSS** = known vulnerabilities (standardized).

**11. Threat ranking methods**

Qualitative H/M/L + risk matrix (likelihood × impact) · quantitative (SLE/ALE) · probability × impact · DREAD · CVSS · **Delphi** · **bug bar** (must-fix threshold). Rank → mitigate highest first; record the rest in the **risk register**.

**On the exam**

- D/R/E/A/D factors → **DREAD** · main criticism → subjective (+ discoverability = obscurity)
- Standard 0–10 for published vulns → **CVSS** (FIRST) · 7.5 → **High** · 9.1 → **Critical**
- Adjust for how critical the system is → **environmental** · changes when exploit published → **temporal/threat**
- **Trap:** high CVSS ≠ automatically top business priority.

**Hooks**

**CVSS bands: Low &lt; 4, Medium 4–6.9, High 7–8.9, Critical 9+. Base = the bug itself; temporal/threat = the news about it; environmental = your house.**

**Quick check:** (1) CVSS 8.2 = which label? (2) Which DREAD factor encourages security through obscurity, why? (3) Which CVSS group adjusts for a server holding your most sensitive data?

**Answer:** High; discoverability (assumes attackers won't find it); environmental. All correct.

</details>

<a name="t-4-4-8"></a>
**Common threats**

APTs, insiders, malware, third-party suppliers, hacktivists, nation-states.

> On the exam: Insiders already have legitimate access, so separation of duties and monitoring matter. APTs are stealthy, long-term and well-funded.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 5: Attack surface, threats and attackers (topics 8, 9, 10, 12, 14)**

**14. Threat agents (who)**

**Script kiddies** (low skill, ready-made tools, fun/bragging) · **hacktivists** (political/social) · **organized crime** (money: ransomware, fraud) · **nation-states / APTs** (espionage/sabotage; most resources; **APT = Advanced Persistent Threat**, patient, hidden for months; Stuxnet) · **insiders** (already have access; **malicious** or **negligent/accidental** — often the most common) · **competitors** (industrial espionage).

Design against REALISTIC attackers (blog vs defense contractor); PnG personas come from here.

**8. Common threats + catalogs**

Injection (SQL, command, LDAP) · broken authn · **broken access control** (BOLA/IDOR) · XSS/CSRF · misconfiguration · sensitive data exposure · **SSRF** (server tricked into calling internal URLs) · insecure deserialization · vulnerable components · malware/ransomware · phishing/social engineering · insider misuse · DoS.

- **OWASP Top 10** = web app risks (awareness)
- **CWE** (MITRE) = **TYPES of weakness** (CWE-89 SQLi); **CWE Top 25**
- **CVE** = **ONE specific vulnerability in ONE product** (CVE-2021-44228 Log4Shell); gets a CVSS score
- **CAPEC** (MITRE) = **attack patterns** (how weaknesses are exploited)
- **MITRE ATT&CK** = real attacker behavior: **tactics** (goal) + **techniques** (how)

*CWE = weakness type · CVE = this specific bug · CAPEC = attack pattern · ATT&CK = attacker's playbook. Type vs instance.*

**9. Attack surface evaluation**

Everything an attacker can reach: entry/exit points, services/ports, APIs, privileged functions, accounts, code handling untrusted data.

**Reduction:** disable unused features/services/ports; remove debug endpoints, samples, test accounts, default creds; least privilege; restrict reach (segmentation, authn); less code. Track across versions (gold plating = needless surface).

*Attack surface = all doors and windows; reduction = brick up the unused ones.*

**12. RASQ (Relative Attack Surface Quotient)**

Microsoft (Howard, Pincus, Wing): **counts + weights** attack opportunities (open sockets/ports, running services, SYSTEM/root services, enabled accounts, weak ACLs, dynamic pages). **Relative**: compare versions/configs, not "safe." **Lower = smaller surface.**

**10. Threat intelligence**

**Strategic** (exec trends) · **tactical** (**TTPs**, mapped to ATT&CK) · **operational** (specific campaigns) · **technical** (**IOCs**: malicious IPs, domains, file hashes).

Sources: **ISACs** (FS-ISAC), CERTs (CISA), vendors, **OSINT**. Standards: **STIX** = format/language; **TAXII** = transport. *STIX = the message, TAXII = the taxi.*

**On the exam**

- Skilled, funded, hidden for months → **APT/nation-state** · employee misconfigures bucket → **negligent insider**
- Weakness types → **CWE** · specific product flaw → **CVE** · attack patterns → **CAPEC** · tactics/techniques → **ATT&CK**
- Disable unused services/ports → **attack surface reduction** · compare versions → **RASQ** (relative, lower better)
- Malicious IPs/hashes → **IOCs (technical TI)** · format → **STIX** · exchange → **TAXII**
- **Traps:** CWE ≠ CVE; RASQ relative.

**Quick check:** (1) CWE vs CVE? (2) Release disabled 6 services, closed 4 ports, RASQ 40 → 28: meaning? (3) Feed of malicious IPs + file hashes: which TI type?

**Answer:** Weakness vs vulnerability (refined: type vs specific instance); attack surface reduced (relative); technical (IOCs). All correct.

</details>

<a name="t-4-4-9"></a>
**Attack surface evaluation**

List entry points and reduce them; fewer exposed features means less risk.

> On the exam: What it is: counting and reducing entry points: open ports, APIs, input fields, files, privileges, services.
Why it matters: every entry point is a way in. Reduce by turning off unused features, removing debug interfaces and requiring authentication.
Scenario cue: 'how to lower risk without changing core functions?' → reduce attack surface.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 5: Attack surface, threats and attackers (topics 8, 9, 10, 12, 14)**

**14. Threat agents (who)**

**Script kiddies** (low skill, ready-made tools, fun/bragging) · **hacktivists** (political/social) · **organized crime** (money: ransomware, fraud) · **nation-states / APTs** (espionage/sabotage; most resources; **APT = Advanced Persistent Threat**, patient, hidden for months; Stuxnet) · **insiders** (already have access; **malicious** or **negligent/accidental** — often the most common) · **competitors** (industrial espionage).

Design against REALISTIC attackers (blog vs defense contractor); PnG personas come from here.

**8. Common threats + catalogs**

Injection (SQL, command, LDAP) · broken authn · **broken access control** (BOLA/IDOR) · XSS/CSRF · misconfiguration · sensitive data exposure · **SSRF** (server tricked into calling internal URLs) · insecure deserialization · vulnerable components · malware/ransomware · phishing/social engineering · insider misuse · DoS.

- **OWASP Top 10** = web app risks (awareness)
- **CWE** (MITRE) = **TYPES of weakness** (CWE-89 SQLi); **CWE Top 25**
- **CVE** = **ONE specific vulnerability in ONE product** (CVE-2021-44228 Log4Shell); gets a CVSS score
- **CAPEC** (MITRE) = **attack patterns** (how weaknesses are exploited)
- **MITRE ATT&CK** = real attacker behavior: **tactics** (goal) + **techniques** (how)

*CWE = weakness type · CVE = this specific bug · CAPEC = attack pattern · ATT&CK = attacker's playbook. Type vs instance.*

**9. Attack surface evaluation**

Everything an attacker can reach: entry/exit points, services/ports, APIs, privileged functions, accounts, code handling untrusted data.

**Reduction:** disable unused features/services/ports; remove debug endpoints, samples, test accounts, default creds; least privilege; restrict reach (segmentation, authn); less code. Track across versions (gold plating = needless surface).

*Attack surface = all doors and windows; reduction = brick up the unused ones.*

**12. RASQ (Relative Attack Surface Quotient)**

Microsoft (Howard, Pincus, Wing): **counts + weights** attack opportunities (open sockets/ports, running services, SYSTEM/root services, enabled accounts, weak ACLs, dynamic pages). **Relative**: compare versions/configs, not "safe." **Lower = smaller surface.**

**10. Threat intelligence**

**Strategic** (exec trends) · **tactical** (**TTPs**, mapped to ATT&CK) · **operational** (specific campaigns) · **technical** (**IOCs**: malicious IPs, domains, file hashes).

Sources: **ISACs** (FS-ISAC), CERTs (CISA), vendors, **OSINT**. Standards: **STIX** = format/language; **TAXII** = transport. *STIX = the message, TAXII = the taxi.*

**On the exam**

- Skilled, funded, hidden for months → **APT/nation-state** · employee misconfigures bucket → **negligent insider**
- Weakness types → **CWE** · specific product flaw → **CVE** · attack patterns → **CAPEC** · tactics/techniques → **ATT&CK**
- Disable unused services/ports → **attack surface reduction** · compare versions → **RASQ** (relative, lower better)
- Malicious IPs/hashes → **IOCs (technical TI)** · format → **STIX** · exchange → **TAXII**
- **Traps:** CWE ≠ CVE; RASQ relative.

**Quick check:** (1) CWE vs CVE? (2) Release disabled 6 services, closed 4 ports, RASQ 40 → 28: meaning? (3) Feed of malicious IPs + file hashes: which TI type?

**Answer:** Weakness vs vulnerability (refined: type vs specific instance); attack surface reduced (relative); technical (IOCs). All correct.

</details>

<a name="t-4-4-10"></a>
**Threat intelligence**

Credible, relevant information on threats. MITRE ATT&CK (tactics), CAPEC (attack patterns).

> On the exam: Good intel is timely, relevant, accurate, actionable. ATT&CK = attacker behavior; CAPEC = attack patterns; CWE = weaknesses.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 5: Attack surface, threats and attackers (topics 8, 9, 10, 12, 14)**

**14. Threat agents (who)**

**Script kiddies** (low skill, ready-made tools, fun/bragging) · **hacktivists** (political/social) · **organized crime** (money: ransomware, fraud) · **nation-states / APTs** (espionage/sabotage; most resources; **APT = Advanced Persistent Threat**, patient, hidden for months; Stuxnet) · **insiders** (already have access; **malicious** or **negligent/accidental** — often the most common) · **competitors** (industrial espionage).

Design against REALISTIC attackers (blog vs defense contractor); PnG personas come from here.

**8. Common threats + catalogs**

Injection (SQL, command, LDAP) · broken authn · **broken access control** (BOLA/IDOR) · XSS/CSRF · misconfiguration · sensitive data exposure · **SSRF** (server tricked into calling internal URLs) · insecure deserialization · vulnerable components · malware/ransomware · phishing/social engineering · insider misuse · DoS.

- **OWASP Top 10** = web app risks (awareness)
- **CWE** (MITRE) = **TYPES of weakness** (CWE-89 SQLi); **CWE Top 25**
- **CVE** = **ONE specific vulnerability in ONE product** (CVE-2021-44228 Log4Shell); gets a CVSS score
- **CAPEC** (MITRE) = **attack patterns** (how weaknesses are exploited)
- **MITRE ATT&CK** = real attacker behavior: **tactics** (goal) + **techniques** (how)

*CWE = weakness type · CVE = this specific bug · CAPEC = attack pattern · ATT&CK = attacker's playbook. Type vs instance.*

**9. Attack surface evaluation**

Everything an attacker can reach: entry/exit points, services/ports, APIs, privileged functions, accounts, code handling untrusted data.

**Reduction:** disable unused features/services/ports; remove debug endpoints, samples, test accounts, default creds; least privilege; restrict reach (segmentation, authn); less code. Track across versions (gold plating = needless surface).

*Attack surface = all doors and windows; reduction = brick up the unused ones.*

**12. RASQ (Relative Attack Surface Quotient)**

Microsoft (Howard, Pincus, Wing): **counts + weights** attack opportunities (open sockets/ports, running services, SYSTEM/root services, enabled accounts, weak ACLs, dynamic pages). **Relative**: compare versions/configs, not "safe." **Lower = smaller surface.**

**10. Threat intelligence**

**Strategic** (exec trends) · **tactical** (**TTPs**, mapped to ATT&CK) · **operational** (specific campaigns) · **technical** (**IOCs**: malicious IPs, domains, file hashes).

Sources: **ISACs** (FS-ISAC), CERTs (CISA), vendors, **OSINT**. Standards: **STIX** = format/language; **TAXII** = transport. *STIX = the message, TAXII = the taxi.*

**On the exam**

- Skilled, funded, hidden for months → **APT/nation-state** · employee misconfigures bucket → **negligent insider**
- Weakness types → **CWE** · specific product flaw → **CVE** · attack patterns → **CAPEC** · tactics/techniques → **ATT&CK**
- Disable unused services/ports → **attack surface reduction** · compare versions → **RASQ** (relative, lower better)
- Malicious IPs/hashes → **IOCs (technical TI)** · format → **STIX** · exchange → **TAXII**
- **Traps:** CWE ≠ CVE; RASQ relative.

**Quick check:** (1) CWE vs CVE? (2) Release disabled 6 services, closed 4 ports, RASQ 40 → 28: meaning? (3) Feed of malicious IPs + file hashes: which TI type?

**Answer:** Weakness vs vulnerability (refined: type vs specific instance); attack surface reduced (relative); technical (IOCs). All correct.

</details>

<a name="t-4-4-11"></a>
**Threat ranking methods**

Delphi ranking: each expert ranks threats independently through a facilitator to avoid domination; quick but subjective. Average ranking: average the DREAD category scores. Probability × impact: rank by likelihood times business impact; most complete.

> On the exam: Scenario cue: 'stop strong personalities influencing ranking' → Delphi. 'Most complete picture of risk' → probability × impact.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 4: Ranking threats: DREAD, CVSS, other methods (topics 6, 7, 11)**

**6. DREAD**

Score each threat 1–10 on 5 factors, then **average**:

- **D**amage potential (how bad?) · **R**eproducibility (how reliably repeated?) · **E**xploitability (how easy to launch?) · **A**ffected users (how many?) · **D**iscoverability (how easy to find?)
- Score = (D+R+E+A+D) ÷ 5; higher = fix sooner.
- Weaknesses: **subjective**; **discoverability** encourages **security through obscurity** (assumes attackers won't find it) → many always score it max; Microsoft moved away from DREAD.

*Hook: Damage? Repeat? Easy? Audience? Detect?*

**7. CVSS (Common Vulnerability Scoring System)**

Industry standard **0.0–10.0** for **known vulnerabilities**; maintained by **FIRST**; versions **3.1** and **4.0**; **NVD** publishes scores for **CVEs**.

- **Base:** built-in: exploitability (**attack vector** network/adjacent/local/physical, **attack complexity**, **privileges required**, **user interaction**), **impact** (C, I, A), **scope**.
- **Temporal (v3) / Threat (v4):** changes over time (public exploit? patch?).
- **Environmental:** adjusted for YOUR environment (asset criticality).
- **Severity:** None 0.0 · Low 0.1–3.9 · Medium 4.0–6.9 · **High 7.0–8.9** · **Critical 9.0–10.0**.
- CVSS base = technical severity, not business risk → environmental + criticality.
- **DREAD** = imagined threats at design time (subjective); **CVSS** = known vulnerabilities (standardized).

**11. Threat ranking methods**

Qualitative H/M/L + risk matrix (likelihood × impact) · quantitative (SLE/ALE) · probability × impact · DREAD · CVSS · **Delphi** · **bug bar** (must-fix threshold). Rank → mitigate highest first; record the rest in the **risk register**.

**On the exam**

- D/R/E/A/D factors → **DREAD** · main criticism → subjective (+ discoverability = obscurity)
- Standard 0–10 for published vulns → **CVSS** (FIRST) · 7.5 → **High** · 9.1 → **Critical**
- Adjust for how critical the system is → **environmental** · changes when exploit published → **temporal/threat**
- **Trap:** high CVSS ≠ automatically top business priority.

**Hooks**

**CVSS bands: Low &lt; 4, Medium 4–6.9, High 7–8.9, Critical 9+. Base = the bug itself; temporal/threat = the news about it; environmental = your house.**

**Quick check:** (1) CVSS 8.2 = which label? (2) Which DREAD factor encourages security through obscurity, why? (3) Which CVSS group adjusts for a server holding your most sensitive data?

**Answer:** High; discoverability (assumes attackers won't find it); environmental. All correct.

</details>

<a name="t-4-4-12"></a>
**RASQ**

Relative Attack Surface Quotient (Microsoft): a number measuring how big the attack surface is, based on entry points, channels and their weights. Used to compare versions.

> On the exam: Scenario cue: 'measure whether the new release increased the attack surface' → RASQ comparison.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 5: Attack surface, threats and attackers (topics 8, 9, 10, 12, 14)**

**14. Threat agents (who)**

**Script kiddies** (low skill, ready-made tools, fun/bragging) · **hacktivists** (political/social) · **organized crime** (money: ransomware, fraud) · **nation-states / APTs** (espionage/sabotage; most resources; **APT = Advanced Persistent Threat**, patient, hidden for months; Stuxnet) · **insiders** (already have access; **malicious** or **negligent/accidental** — often the most common) · **competitors** (industrial espionage).

Design against REALISTIC attackers (blog vs defense contractor); PnG personas come from here.

**8. Common threats + catalogs**

Injection (SQL, command, LDAP) · broken authn · **broken access control** (BOLA/IDOR) · XSS/CSRF · misconfiguration · sensitive data exposure · **SSRF** (server tricked into calling internal URLs) · insecure deserialization · vulnerable components · malware/ransomware · phishing/social engineering · insider misuse · DoS.

- **OWASP Top 10** = web app risks (awareness)
- **CWE** (MITRE) = **TYPES of weakness** (CWE-89 SQLi); **CWE Top 25**
- **CVE** = **ONE specific vulnerability in ONE product** (CVE-2021-44228 Log4Shell); gets a CVSS score
- **CAPEC** (MITRE) = **attack patterns** (how weaknesses are exploited)
- **MITRE ATT&CK** = real attacker behavior: **tactics** (goal) + **techniques** (how)

*CWE = weakness type · CVE = this specific bug · CAPEC = attack pattern · ATT&CK = attacker's playbook. Type vs instance.*

**9. Attack surface evaluation**

Everything an attacker can reach: entry/exit points, services/ports, APIs, privileged functions, accounts, code handling untrusted data.

**Reduction:** disable unused features/services/ports; remove debug endpoints, samples, test accounts, default creds; least privilege; restrict reach (segmentation, authn); less code. Track across versions (gold plating = needless surface).

*Attack surface = all doors and windows; reduction = brick up the unused ones.*

**12. RASQ (Relative Attack Surface Quotient)**

Microsoft (Howard, Pincus, Wing): **counts + weights** attack opportunities (open sockets/ports, running services, SYSTEM/root services, enabled accounts, weak ACLs, dynamic pages). **Relative**: compare versions/configs, not "safe." **Lower = smaller surface.**

**10. Threat intelligence**

**Strategic** (exec trends) · **tactical** (**TTPs**, mapped to ATT&CK) · **operational** (specific campaigns) · **technical** (**IOCs**: malicious IPs, domains, file hashes).

Sources: **ISACs** (FS-ISAC), CERTs (CISA), vendors, **OSINT**. Standards: **STIX** = format/language; **TAXII** = transport. *STIX = the message, TAXII = the taxi.*

**On the exam**

- Skilled, funded, hidden for months → **APT/nation-state** · employee misconfigures bucket → **negligent insider**
- Weakness types → **CWE** · specific product flaw → **CVE** · attack patterns → **CAPEC** · tactics/techniques → **ATT&CK**
- Disable unused services/ports → **attack surface reduction** · compare versions → **RASQ** (relative, lower better)
- Malicious IPs/hashes → **IOCs (technical TI)** · format → **STIX** · exchange → **TAXII**
- **Traps:** CWE ≠ CVE; RASQ relative.

**Quick check:** (1) CWE vs CVE? (2) Release disabled 6 services, closed 4 ports, RASQ 40 → 28: meaning? (3) Feed of malicious IPs + file hashes: which TI type?

**Answer:** Weakness vs vulnerability (refined: type vs specific instance); attack surface reduced (relative); technical (IOCs). All correct.

</details>

<a name="t-4-4-13"></a>
**Entry points, exit points, privileged functions**

Threat modeling identifies entry points (where input enters), exit points (where data leaves, including errors and logs) and privileged functionality (admin features).

> On the exam: Trap: exit points matter too; error messages and logs can leak data.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 1: Steps, DFDs and trust boundaries (topics 1, 2, 13)**

Threat modeling = thinking like an attacker at design time.

**1. Threat modeling steps**

**Shostack's 4 questions:** What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?

**Detailed steps:** 1 identify **security objectives** → 2 **decompose/model** (DFDs, assets, trust boundaries, entry/exit points) → 3 **identify threats** (STRIDE) → 4 **rate/rank** (DREAD, CVSS, likelihood × impact) → 5 **mitigate** (or accept/transfer/avoid) → 6 **validate + iterate**.

- **When:** design phase (SDL Design; cheapest). **Living document**: update when design/threats change.
- **Who:** team (architects, devs, security, testers).

**2. DFDs and trust boundaries**

- **External entity = rectangle** (outside your control: user, partner, browser)
- **Process = circle** (code doing work)
- **Data store = two parallel lines** (DB, file, cache, log)
- **Data flow = arrow**
- **Trust boundary = dashed line** (where trust changes: internet → web server, web → DB, Ring 3 → Ring 0, company → partner API)
- **Threats cluster where data flows CROSS trust boundaries** → authn, authz, validation, encryption there.
- **Level 0** = context diagram (whole system as one bubble); **Level 1, 2…** = zoom in.

**13. Entry points, exit points, privileged functions**

- **Entry points:** UI forms, APIs, file uploads, URL params, cookies, headers, queues, open ports, config files, env vars → validate input.
- **Exit points:** web pages, API responses, **error messages**, **logs**, exports, emails → **information disclosure** (stack traces, PII in logs).
- **Privileged functions:** admin panels, role management, **password reset**, payments, config, export → closest scrutiny (MFA, re-auth, logging).
- Together = the **attack surface**.

**On the exam**

- First step → **identify security objectives** · main decomposition diagram → **DFD**
- Rectangle = external entity · circle = process · parallel lines = data store · dashed = trust boundary
- Threats concentrate → **trust boundary crossings**
- Login/API/upload → entry · error messages/logs → exit · password reset/admin → privileged
- Update the model → whenever the design changes
- **Trap:** threat modeling is a DESIGN-phase activity.

**Hooks**

**DFD shapes: Rectangle = outsider, Circle = worker, Parallel lines = storage shelf, Arrow = moving data, Dashed line = border control. Trust boundary = border crossing where you check passports.**

**Quick check:** (1) What does a dashed line in a DFD represent, why focus on it? (2) Classify: file upload form / detailed stack-trace error / reset-any-user's-password admin feature.

**Answer:** Trust boundary, threats cluster at crossings; entry, exit, privileged function. All correct.

</details>

<a name="t-4-4-14"></a>
**Threat agents**

Who attacks: script kiddies (low skill), insiders (legitimate access), hacktivists (ideology), organized crime (money), competitors (espionage), nation-states (APTs, high skill and resources).

> On the exam: Motive, opportunity and means must all be present for an attack. Controls reduce opportunity and means; you can't control motive.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.4 Lesson 5: Attack surface, threats and attackers (topics 8, 9, 10, 12, 14)**

**14. Threat agents (who)**

**Script kiddies** (low skill, ready-made tools, fun/bragging) · **hacktivists** (political/social) · **organized crime** (money: ransomware, fraud) · **nation-states / APTs** (espionage/sabotage; most resources; **APT = Advanced Persistent Threat**, patient, hidden for months; Stuxnet) · **insiders** (already have access; **malicious** or **negligent/accidental** — often the most common) · **competitors** (industrial espionage).

Design against REALISTIC attackers (blog vs defense contractor); PnG personas come from here.

**8. Common threats + catalogs**

Injection (SQL, command, LDAP) · broken authn · **broken access control** (BOLA/IDOR) · XSS/CSRF · misconfiguration · sensitive data exposure · **SSRF** (server tricked into calling internal URLs) · insecure deserialization · vulnerable components · malware/ransomware · phishing/social engineering · insider misuse · DoS.

- **OWASP Top 10** = web app risks (awareness)
- **CWE** (MITRE) = **TYPES of weakness** (CWE-89 SQLi); **CWE Top 25**
- **CVE** = **ONE specific vulnerability in ONE product** (CVE-2021-44228 Log4Shell); gets a CVSS score
- **CAPEC** (MITRE) = **attack patterns** (how weaknesses are exploited)
- **MITRE ATT&CK** = real attacker behavior: **tactics** (goal) + **techniques** (how)

*CWE = weakness type · CVE = this specific bug · CAPEC = attack pattern · ATT&CK = attacker's playbook. Type vs instance.*

**9. Attack surface evaluation**

Everything an attacker can reach: entry/exit points, services/ports, APIs, privileged functions, accounts, code handling untrusted data.

**Reduction:** disable unused features/services/ports; remove debug endpoints, samples, test accounts, default creds; least privilege; restrict reach (segmentation, authn); less code. Track across versions (gold plating = needless surface).

*Attack surface = all doors and windows; reduction = brick up the unused ones.*

**12. RASQ (Relative Attack Surface Quotient)**

Microsoft (Howard, Pincus, Wing): **counts + weights** attack opportunities (open sockets/ports, running services, SYSTEM/root services, enabled accounts, weak ACLs, dynamic pages). **Relative**: compare versions/configs, not "safe." **Lower = smaller surface.**

**10. Threat intelligence**

**Strategic** (exec trends) · **tactical** (**TTPs**, mapped to ATT&CK) · **operational** (specific campaigns) · **technical** (**IOCs**: malicious IPs, domains, file hashes).

Sources: **ISACs** (FS-ISAC), CERTs (CISA), vendors, **OSINT**. Standards: **STIX** = format/language; **TAXII** = transport. *STIX = the message, TAXII = the taxi.*

**On the exam**

- Skilled, funded, hidden for months → **APT/nation-state** · employee misconfigures bucket → **negligent insider**
- Weakness types → **CWE** · specific product flaw → **CVE** · attack patterns → **CAPEC** · tactics/techniques → **ATT&CK**
- Disable unused services/ports → **attack surface reduction** · compare versions → **RASQ** (relative, lower better)
- Malicious IPs/hashes → **IOCs (technical TI)** · format → **STIX** · exchange → **TAXII**
- **Traps:** CWE ≠ CVE; RASQ relative.

**Quick check:** (1) CWE vs CVE? (2) Release disabled 6 services, closed 4 ports, RASQ 40 → 28: meaning? (3) Feed of malicious IPs + file hashes: which TI type?

**Answer:** Weakness vs vulnerability (refined: type vs specific instance); attack surface reduced (relative); technical (IOCs). All correct.

</details>

## 4.5 Architectural risk assessment and design review

<a name="t-4-5-1"></a>
**Architectural risk analysis**

Review the design against requirements and the threat model before coding.

> On the exam: What it is: reviewing the architecture for security flaws before or during development: missing authentication between components, weak trust boundaries, single points of failure.
Why it matters: design flaws are expensive to fix later and tools usually can't find them.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.5 Architectural risk assessment and design review (both topics)**

The **design** stage is where flaws are **cheapest** to fix: check the design before code.

**1. Architectural risk analysis**

Examine the **planned architecture** (components, data flows, trust boundaries, tech) for **design-level** weaknesses and rate risk **before coding**.

- **Implementation bug** = coding mistake in good design (missed output escaping → XSS); SAST/code review find these.
- **Design flaw** = the plan itself is wrong (no authorization layer, plain-text password storage by design, shared admin account, trusting client prices). Perfect code can't fix it → re-architecture. Roughly **half** of security problems; **scanners can't find them**.
- Steps: gather **security requirements + threat model + DFDs** → map components, flows, boundaries, entry points → check every requirement has a design control and every threat a mitigation (design-stage RTM) → check **secure design principles** (least privilege, defense in depth, fail secure, economy of mechanism, complete mediation, separation of duties) → rate risks, decide responses (redesign, controls, accept).
- = SDL Design phase; "secure by design."

**2. Design reviews**

Formal review of the design by **peers and security experts**, often at a **control gate** before implementation.

- Types: **peer review**, **security design review**, **walkthroughs** ("what if…?").
- Look for: missing authn/authz at entry points; trust boundary crossings without validation; unencrypted sensitive flows; single points of failure / fail-open; over-privileged components, shared credentials; conflicts with requirements/policy.
- **Cheapest here:** design = change a diagram; testing = rework; production = incident + emergency patch + maybe re-architecture (cost grows ~10× per later phase).
- Output: findings, required changes, **go/no-go** at the gate; accepted risks → **risk register**.

**On the exam**

- Review architecture vs requirements + threat model before coding → **architectural risk analysis**
- Flaw better coding can't fix (no authz layer) → **design flaw** → redesign
- Cheapest phase to fix → **design** (or requirements)
- Peers + security experts walk through design at a gate → **design review**
- **Trap:** SAST/code review can't catch design flaws.

**Hooks**

**Bug = mistake building the blueprint. Flaw = mistake in the blueprint itself. Fix it on paper, not in production.**

**Quick check:** (1) Scanner finds nothing, but any logged-in user can call the admin API (no role check in the design): bug or flaw, what catches it? (2) Why design reviews before implementation?

**Answer:** Design flaw, caught by architectural review / design review; catch flaws before resources are spent building. Both correct.

</details>

<a name="t-4-5-2"></a>
**Design reviews**

Peer and security reviews; flaws are cheapest to fix here.

> On the exam: What it is: formal review of the design against security requirements, principles and the threat model, ideally by reviewers independent of the designers.
Scenario cue: 'what catches a missing authorization design before coding?' → security design review.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.5 Architectural risk assessment and design review (both topics)**

The **design** stage is where flaws are **cheapest** to fix: check the design before code.

**1. Architectural risk analysis**

Examine the **planned architecture** (components, data flows, trust boundaries, tech) for **design-level** weaknesses and rate risk **before coding**.

- **Implementation bug** = coding mistake in good design (missed output escaping → XSS); SAST/code review find these.
- **Design flaw** = the plan itself is wrong (no authorization layer, plain-text password storage by design, shared admin account, trusting client prices). Perfect code can't fix it → re-architecture. Roughly **half** of security problems; **scanners can't find them**.
- Steps: gather **security requirements + threat model + DFDs** → map components, flows, boundaries, entry points → check every requirement has a design control and every threat a mitigation (design-stage RTM) → check **secure design principles** (least privilege, defense in depth, fail secure, economy of mechanism, complete mediation, separation of duties) → rate risks, decide responses (redesign, controls, accept).
- = SDL Design phase; "secure by design."

**2. Design reviews**

Formal review of the design by **peers and security experts**, often at a **control gate** before implementation.

- Types: **peer review**, **security design review**, **walkthroughs** ("what if…?").
- Look for: missing authn/authz at entry points; trust boundary crossings without validation; unencrypted sensitive flows; single points of failure / fail-open; over-privileged components, shared credentials; conflicts with requirements/policy.
- **Cheapest here:** design = change a diagram; testing = rework; production = incident + emergency patch + maybe re-architecture (cost grows ~10× per later phase).
- Output: findings, required changes, **go/no-go** at the gate; accepted risks → **risk register**.

**On the exam**

- Review architecture vs requirements + threat model before coding → **architectural risk analysis**
- Flaw better coding can't fix (no authz layer) → **design flaw** → redesign
- Cheapest phase to fix → **design** (or requirements)
- Peers + security experts walk through design at a gate → **design review**
- **Trap:** SAST/code review can't catch design flaws.

**Hooks**

**Bug = mistake building the blueprint. Flaw = mistake in the blueprint itself. Fix it on paper, not in production.**

**Quick check:** (1) Scanner finds nothing, but any logged-in user can call the admin API (no role check in the design): bug or flaw, what catches it? (2) Why design reviews before implementation?

**Answer:** Design flaw, caught by architectural review / design review; catch flaws before resources are spent building. Both correct.

</details>

## 4.6 Security properties and constraints

<a name="t-4-6-1"></a>
**Non-functional trade-offs** (review)

E.g., encryption vs performance, logging vs privacy.

> On the exam: What it means: security must be balanced against other qualities (performance, usability, cost). Example: encrypting everything may slow the system; long sessions improve usability but weaken security.
Scenario cue: 'stakeholders reject strong security because it's too slow' → document the trade-off and choose controls that meet both, with risk accepted by the owner.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Picked covert channel twice (pre-test + quiz) for heavy-security workarounds; answer = BAD TRADE-OFF. Shaky.

</details>

<a name="t-4-6-2"></a>
**Bell-LaPadula**

Confidentiality model: no read up, no write down.

> On the exam: No read up (simple security property); no write down (star property) to stop leaks to lower levels. Used by military.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Pre-test said Biba; quiz: Secret can not save to Unclassified = BLP no write down, correct.

</details>

<a name="t-4-6-3"></a>
**Biba** (review)

Integrity model: no read down, no write up.

> On the exam: Rules: no read down (simple integrity), no write up (star integrity). Protects integrity: high-integrity data isn't contaminated by lower-integrity sources.
Scenario cue: 'a low-trust process must not modify system files' → Biba.
Memory trick: BLP = Lock (confidentiality); Biba = Bodyguard (integrity).

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Pre-test correct; quiz said BLP write down for low-integrity form writing to ledger (answer Biba no write up). Shaky.

</details>

<a name="t-4-6-4"></a>
**Clark-Wilson**

Integrity via well-formed transactions and separation of duties.

> On the exam: Key parts: constrained data items (CDIs) changed only through transformation procedures (TPs), with integrity verification procedures (IVPs) and separation of duties.
Scenario cue: 'users can modify accounting data only through approved application functions, never directly' → Clark-Wilson.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Correct (pre-test + quiz).

</details>

<a name="t-4-6-5"></a>
**Brewer-Nash (Chinese Wall)**

Prevents conflicts of interest.

> On the exam: Access changes based on what you've already seen, e.g., a consultant can't view a competitor's data.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Correct (pre-test + quiz).

</details>

<a name="t-4-6-6"></a>
**More security models**

Graham-Denning: rules for securely creating and deleting subjects and objects and granting rights. Harrison-Ruzzo-Ullman: how access rights can change, and whether a system can reach an unsafe state. Take-Grant: rights passed between subjects using take and grant operations.

> On the exam: Scenario cue: 'model defining how rights are securely created, deleted and transferred' → Graham-Denning.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Graham-Denning, HRU, Take-Grant. Correct.

</details>

<a name="t-4-6-7"></a>
**State machine, information flow, noninterference, lattice** (review)

State machine: system is secure if it starts secure and every transition keeps it secure. Information flow: controls how data moves between levels. Noninterference: actions at a high level can't be observed by low levels (stops covert channels). Lattice: defines upper and lower bounds of access between levels.

> On the exam: Scenario cue: 'a low-level user must not be able to infer anything from high-level activity' → noninterference.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Noninterference correct (pre-test); state machine vs information flow unsure. Shaky.

</details>

<a name="t-4-6-8"></a>
**Covert channels**

Hidden ways to leak information that the security policy doesn't control. Storage channels: signal through shared resources (file attributes, disk space). Timing channels: signal by changing how long operations take.

> On the exam: Defense: noninterference design, limiting shared resources, monitoring. Scenario cue: 'process leaks data by varying CPU load' → timing channel.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Timing (pre-test) + storage (quiz) correct.

</details>

<a name="t-4-6-9"></a>
**Trusted path and secure state**

Trusted path: a guaranteed direct channel between the user and the trusted system (e.g., Ctrl+Alt+Del login) so malware can't fake it. Secure state: the system always remains in a state that satisfies the security policy, including after failure.

> On the exam: Scenario cue: 'prevent fake login screens from capturing passwords' → trusted path.

<details><summary>Lesson (25 Oct 2026)</summary>

**4.6 Security properties and constraints (all 9 topics)**

**1. Non-functional trade-offs**

Security costs speed, usability, money. Balance by risk. **Too much security backfires**: MFA on every action + endless approvals → people climb out the window (shadow IT, unapproved apps). Slow heavy encryption everywhere → app too slow, customers lost.

*Hook: locking every door so tightly that people climb out the window.*

**2. Bell-LaPadula = CONFIDENTIALITY (military, secrets)**

- **No read UP** (simple security property): don't peek at higher secrets
- **No write DOWN** (star * property): don't spill secrets to lower levels

*Hook: Bell-LaPadula keeps its Lips sealed.*

**3. Biba = INTEGRITY (trustworthy data) — the mirror**

- **No read DOWN**: don't trust dirty low-integrity data
- **No write UP**: don't pollute high-integrity data

*Hook: clean water — don't drink from the dirty puddle below, don't pour mud into the clean tank above.*

| | Bell-LaPadula (secrets) | Biba (clean data) |

|---|---|---|

| Reading | No read UP | No read DOWN |

| Writing | No write DOWN | No write UP |

**2-step method:** (1) which direction (up/down) and read/write? (2) why block it: leak secrets = Bell-LaPadula; pollute data = Biba. **Clue words:** secret, classified, clearance, leak → BLP; integrity, trustworthy, corrupt, pollute → Biba.

**4. Clark-Wilson = business INTEGRITY**

Users can't touch data directly; only via **approved programs (well-formed transactions)**; **separation of duties** (enter vs approve). Bank ledger via the transfer app only.

**5. Brewer-Nash (Chinese Wall) = CONFLICT OF INTEREST**

Access changes based on **what you've already seen**: view Coca-Cola → blocked from Pepsi.

**6. More models (permission management)**

**Graham-Denning**, **Harrison-Ruzzo-Ullman (HRU)**, **Take-Grant**: how permissions are **created, granted, transferred, removed**.

**7. State machine, information flow, noninterference, lattice**

- **State machine:** always in a **secure state**; every **transition** leads to another secure state (traffic light: never "all green").
- **Information flow:** **where data may move** (never High → Low) (the pipes).
- **Noninterference:** high-level actions have **no visible effect** on what low-level users observe.
- **Lattice:** ordered levels/categories deciding who accesses what.

**8. Covert channels**

Hidden ways to leak info the system wasn't designed for.

- **Timing:** CPU busy/idle patterns · **Storage:** filling/emptying a disk area.

*Hook: a spy tapping Morse code through the wall.*

**9. Trusted path and secure state**

- **Trusted path:** guaranteed direct channel user ↔ real security system that nothing can fake (**Ctrl+Alt+Del** handled by the kernel). *Private hotline.*
- **Secure state:** system starts, runs and **fails into a safe condition** (fail secure). *Building locks itself when the power goes out.*

**On the exam**

- Secret user can't save to Unclassified → **BLP no write down** · low-integrity form can't write to ledger → **Biba no write up**
- Approved programs + separation of duties → **Clark-Wilson** · competitor wall → **Brewer-Nash**
- Granting/removing permissions → **Graham-Denning / HRU / Take-Grant**
- Every transition stays secure → **state machine** · data movement rules → **information flow**
- High activity invisible to low → **noninterference**
- Disk fill pattern → **covert storage** · CPU busy/idle → **covert timing**
- Ctrl+Alt+Del genuine login → **trusted path**
- Heavy security → workarounds → **bad trade-off** (not a covert channel)

**Quick check:** 4.6 pre-test (8) + quiz (9): BLP vs Biba directions, Clark-Wilson, Brewer-Nash, permission models, state machine, covert channels, trusted path, trade-offs.

**Answer:** Pre-test said secure state; quiz trusted path correct.

</details>

## 4.7 Secure operational architecture

<a name="t-4-7-1"></a>
**Deployment topology**

Network segmentation, DMZ, tiers separated by firewalls.

> On the exam: What it is: where components sit on the network and how they connect: DMZ for internet-facing servers, internal zones for app and database, firewalls between tiers.
Scenario cue: 'the database server is directly reachable from the internet' → poor deployment topology.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.7 Secure operational architecture (all 3 topics)**

How the system is laid out and run in production.

**1. Deployment topology**

- **Network segmentation:** zones with firewalls; a break-in doesn't spread.
- **DMZ:** buffer zone between internet and internal network for **internet-facing** servers (web, reverse proxy, email gateway). Classic: Internet → FW → DMZ (web) → FW → app tier → FW → DB tier.
- **Database never directly reachable from the internet**; only the app tier talks to it.
- **Default deny** (only specific traffic, e.g. web → app on 443).
- **Microsegmentation** down to workloads (K8s network policies) = zero trust (don't trust "inside").
- **Redundancy:** load balancers, multiple instances/zones.

*Hook: DMZ = the lobby; database = the vault in the basement.*

**2. Operational interfaces**

- **Jump box / bastion host:** single hardened, monitored, MFA server = only way into production.
- **Out-of-band** management; **PAM** (just-in-time, vaulted creds, session recording); protected monitoring/logging.
- **Never expose SSH (22), RDP (3389) or admin consoles to the internet.**

*Hook: bastion = the one guarded drawbridge.*

**3. CI/CD architecture**

- Pipeline holds **the keys to production** → compromise = malicious code to every customer = **supply chain attack**. **SolarWinds (2020):** build system compromised, backdoor shipped in a **signed** update.
- **Separate environments** (dev/test/staging/prod), different creds; devs no direct prod access.
- Protect the pipeline: strong auth, least privilege; **protected branches** + required review/approval (separation of duties); **secrets in a vault**; **hardened, short-lived build runners**.
- Security gates: SAST, SCA, secret scanning, DAST, **bug bar** gate.
- Integrity (SSDF PS): **sign artifacts** + verify before deploy; **SBOM**; **reproducible builds**; **SLSA** grades build protection (Domain 8).
- Least-privilege deploy credentials.
- **Why signing didn't stop SolarWinds:** malicious code added BEFORE signing → genuine signature. Signature proves WHO signed, not that the content is clean. Protected branches don't help either when the attacker changes code ON the build server (skips the repo) → protect the build system itself.

**On the exam**

- Internet-facing servers between two firewalls → **DMZ**
- DB with a public IP → topology flaw → internal tier behind app tier
- Single hardened monitored server to reach prod → **jump box / bastion**
- Malware in a signed update via the build system → **supply chain / CI/CD compromise**
- Dev pushes straight to prod → **separation of duties** violation → protected branches + approval
- **Trap:** signed ≠ clean.

**Hooks**

**DMZ = lobby; DB = basement vault. Bastion = guarded drawbridge. Pipeline = keys to production. Signature = wax seal: proves who sealed it, not that the letter is honest.**

**Quick check:** (1) Customer DB has a public IP and accepts internet connections: what's wrong, where should it sit? (2) Build server hacked, malicious code ships in a properly signed update: attack + why signing didn't stop it?

**Answer:** Behind the app tier, never public. Correct.

</details>

<a name="t-4-7-2"></a>
**Operational interfaces**

Secure admin and monitoring access.

> On the exam: What it is: interfaces used to run the system: monitoring, backup, deployment, admin. Secure them with a separate network, jump hosts (bastion), MFA and logging.
Scenario cue: 'admins connect to production servers directly from their laptops' → use a hardened jump host.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.7 Secure operational architecture (all 3 topics)**

How the system is laid out and run in production.

**1. Deployment topology**

- **Network segmentation:** zones with firewalls; a break-in doesn't spread.
- **DMZ:** buffer zone between internet and internal network for **internet-facing** servers (web, reverse proxy, email gateway). Classic: Internet → FW → DMZ (web) → FW → app tier → FW → DB tier.
- **Database never directly reachable from the internet**; only the app tier talks to it.
- **Default deny** (only specific traffic, e.g. web → app on 443).
- **Microsegmentation** down to workloads (K8s network policies) = zero trust (don't trust "inside").
- **Redundancy:** load balancers, multiple instances/zones.

*Hook: DMZ = the lobby; database = the vault in the basement.*

**2. Operational interfaces**

- **Jump box / bastion host:** single hardened, monitored, MFA server = only way into production.
- **Out-of-band** management; **PAM** (just-in-time, vaulted creds, session recording); protected monitoring/logging.
- **Never expose SSH (22), RDP (3389) or admin consoles to the internet.**

*Hook: bastion = the one guarded drawbridge.*

**3. CI/CD architecture**

- Pipeline holds **the keys to production** → compromise = malicious code to every customer = **supply chain attack**. **SolarWinds (2020):** build system compromised, backdoor shipped in a **signed** update.
- **Separate environments** (dev/test/staging/prod), different creds; devs no direct prod access.
- Protect the pipeline: strong auth, least privilege; **protected branches** + required review/approval (separation of duties); **secrets in a vault**; **hardened, short-lived build runners**.
- Security gates: SAST, SCA, secret scanning, DAST, **bug bar** gate.
- Integrity (SSDF PS): **sign artifacts** + verify before deploy; **SBOM**; **reproducible builds**; **SLSA** grades build protection (Domain 8).
- Least-privilege deploy credentials.
- **Why signing didn't stop SolarWinds:** malicious code added BEFORE signing → genuine signature. Signature proves WHO signed, not that the content is clean. Protected branches don't help either when the attacker changes code ON the build server (skips the repo) → protect the build system itself.

**On the exam**

- Internet-facing servers between two firewalls → **DMZ**
- DB with a public IP → topology flaw → internal tier behind app tier
- Single hardened monitored server to reach prod → **jump box / bastion**
- Malware in a signed update via the build system → **supply chain / CI/CD compromise**
- Dev pushes straight to prod → **separation of duties** violation → protected branches + approval
- **Trap:** signed ≠ clean.

**Hooks**

**DMZ = lobby; DB = basement vault. Bastion = guarded drawbridge. Pipeline = keys to production. Signature = wax seal: proves who sealed it, not that the letter is honest.**

**Quick check:** (1) Customer DB has a public IP and accepts internet connections: what's wrong, where should it sit? (2) Build server hacked, malicious code ships in a properly signed update: attack + why signing didn't stop it?

**Answer:** Taught.

</details>

<a name="t-4-7-3"></a>
**CI/CD architecture** (review)

Separate environments, protected pipeline, least-privilege deployment.

> On the exam: Design points: separate dev/test/prod; least-privilege build and deploy accounts; secrets in a vault; signed artifacts; approvals before production; logs of every deployment.
Scenario cue: 'any developer can push straight to production' → violates separation of duties; add approval gates.

<details><summary>Lesson (19 Oct 2026)</summary>

**4.7 Secure operational architecture (all 3 topics)**

How the system is laid out and run in production.

**1. Deployment topology**

- **Network segmentation:** zones with firewalls; a break-in doesn't spread.
- **DMZ:** buffer zone between internet and internal network for **internet-facing** servers (web, reverse proxy, email gateway). Classic: Internet → FW → DMZ (web) → FW → app tier → FW → DB tier.
- **Database never directly reachable from the internet**; only the app tier talks to it.
- **Default deny** (only specific traffic, e.g. web → app on 443).
- **Microsegmentation** down to workloads (K8s network policies) = zero trust (don't trust "inside").
- **Redundancy:** load balancers, multiple instances/zones.

*Hook: DMZ = the lobby; database = the vault in the basement.*

**2. Operational interfaces**

- **Jump box / bastion host:** single hardened, monitored, MFA server = only way into production.
- **Out-of-band** management; **PAM** (just-in-time, vaulted creds, session recording); protected monitoring/logging.
- **Never expose SSH (22), RDP (3389) or admin consoles to the internet.**

*Hook: bastion = the one guarded drawbridge.*

**3. CI/CD architecture**

- Pipeline holds **the keys to production** → compromise = malicious code to every customer = **supply chain attack**. **SolarWinds (2020):** build system compromised, backdoor shipped in a **signed** update.
- **Separate environments** (dev/test/staging/prod), different creds; devs no direct prod access.
- Protect the pipeline: strong auth, least privilege; **protected branches** + required review/approval (separation of duties); **secrets in a vault**; **hardened, short-lived build runners**.
- Security gates: SAST, SCA, secret scanning, DAST, **bug bar** gate.
- Integrity (SSDF PS): **sign artifacts** + verify before deploy; **SBOM**; **reproducible builds**; **SLSA** grades build protection (Domain 8).
- Least-privilege deploy credentials.
- **Why signing didn't stop SolarWinds:** malicious code added BEFORE signing → genuine signature. Signature proves WHO signed, not that the content is clean. Protected branches don't help either when the attacker changes code ON the build server (skips the repo) → protect the build system itself.

**On the exam**

- Internet-facing servers between two firewalls → **DMZ**
- DB with a public IP → topology flaw → internal tier behind app tier
- Single hardened monitored server to reach prod → **jump box / bastion**
- Malware in a signed update via the build system → **supply chain / CI/CD compromise**
- Dev pushes straight to prod → **separation of duties** violation → protected branches + approval
- **Trap:** signed ≠ clean.

**Hooks**

**DMZ = lobby; DB = basement vault. Bastion = guarded drawbridge. Pipeline = keys to production. Signature = wax seal: proves who sealed it, not that the letter is honest.**

**Quick check:** (1) Customer DB has a public IP and accepts internet connections: what's wrong, where should it sit? (2) Build server hacked, malicious code ships in a properly signed update: attack + why signing didn't stop it?

**Answer:** I named defenses (separation of duties, protected branches) instead of the attack: SUPPLY CHAIN / CI/CD compromise (SolarWinds); code added before signing so signature genuine; branches do not help when the build server itself is changed. Marked shaky.

</details>

## 4.AI AI additions in the current outline

<a name="t-4-ai-1"></a>
**Decoupling AI inference**

Keep core logic separate from unpredictable AI components.

> On the exam: What it means: treat the AI component as untrusted; validate its output before core logic acts on it, and never give it direct write access to critical data.
Scenario cue: 'model output is executed as a database query' → injection risk; insert validation between AI and core.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.AI: AI in secure architecture (all 4 topics)**

**1. Decoupling AI inference**

**Inference** = model producing an answer (training builds it, inference uses it). AI is **non-deterministic** (different/wrong outputs, hallucinations).

**Principle:** core logic + critical decisions in **deterministic code**; AI = separate, **untrusted** component whose output is **advice, not a command**.

- AI in its **own tier/service**, least privilege (can't reach DB/payments directly)
- **Validate output** against a strict **schema** + allowed values; never straight into SQL/shell/web page (**improper output handling**)
- **Guardrails** in (prompt-injection screening) and out (sensitive data, toxicity)
- **Fallbacks / circuit breakers** (fail secure)
- **Human in the loop** for high-impact decisions (excessive agency defense)

*Example: AI suggests refund → code checks policy limit → human approves >$50. AI suggests, your code decides.*

**2. Zero Trust for AI**

**Never trust, always verify** for AI infrastructure. **Vector database** = stores embeddings for **RAG**.

- **Per-user access control on retrieval** (else chatbot returns CEO salary doc = BOLA for AI); per-tenant separation; validate what's added (**poisoned docs** → indirect prompt injection)
- **AI/GPU clusters:** segmentation, strong authn, patching
- **Model endpoints:** authenticate every call, **rate limit** (model theft, unbounded consumption)
- **Model weights** = IP/trade secret: encrypt, restrict, **sign** (MLSecOps)
- Agents' tools: least privilege

*No free pass: verify every request, document, tool call.*

**3. AI-driven threat modeling**

AI helps defenders: suggests DFDs, proposes STRIDE threats, maps to ATT&CK/CAPEC, keeps the model updated (continuous).

Cautions: **hallucinates** (invents/misses threats) → **human review**; **data leakage** (architecture = attacker map) → approved enterprise tools only; **accountability stays with the team**.

*A brainstorming partner, not the judge.*

**4. Federated learning**

One shared model trained across many devices/orgs **without centralizing data**: local training → send **model updates (gradients/weights)**, not raw data → server **aggregates** → global model back. (Phone keyboards; hospitals.)

- Benefit: privacy + data minimization; helps localization.
- Risks: **poisoned updates** (malicious participant backdoors the model); **gradient leakage** (reconstruct private data from updates); compromised nodes.
- Controls: **authenticate participants**, **secure aggregation** (server can't see any single update), **differential privacy** (noise), **anomaly detection / robust aggregation**.

*The data stays home; only the lessons travel (check every lesson for poison).*

**On the exam**

- Keep core logic separate from AI → **decoupling** · AI SQL run directly → **improper output handling**
- Chatbot returns unauthorized docs → **per-user access control on vector DB** (zero trust for AI)
- AI proposes STRIDE threats → **AI-driven threat modeling** (human review)
- Train across hospitals without sharing records → **federated learning** · malicious updates → **poisoning** · server can't see individual updates → **secure aggregation**
- **Trap:** federated learning reduces but doesn't remove privacy risk.

**Quick check:** (1) RAG chatbot gives intern the confidential bonus spreadsheet: missing control? (2) Five hospitals train jointly without sharing records: approach + one risk? (3) App runs the AI's suggested SQL filter directly: principle violated?

**Answer:** Zero trust for AI (specific: per-user access control on vector DB retrieval); federated learning (risk: poisoned updates / gradient leakage); decoupling (improper output handling). All correct.

</details>

<a name="t-4-ai-2"></a>
**Zero Trust for AI**

Strict boundaries around vector databases and AI processing clusters.

> On the exam: What it means: vector databases and AI clusters authenticate and authorize every request, network-segmented, with retrieval limited to what the user may see.
Scenario cue: 'the AI assistant retrieves documents the user isn't allowed to read' → missing per-user authorization in retrieval.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.AI: AI in secure architecture (all 4 topics)**

**1. Decoupling AI inference**

**Inference** = model producing an answer (training builds it, inference uses it). AI is **non-deterministic** (different/wrong outputs, hallucinations).

**Principle:** core logic + critical decisions in **deterministic code**; AI = separate, **untrusted** component whose output is **advice, not a command**.

- AI in its **own tier/service**, least privilege (can't reach DB/payments directly)
- **Validate output** against a strict **schema** + allowed values; never straight into SQL/shell/web page (**improper output handling**)
- **Guardrails** in (prompt-injection screening) and out (sensitive data, toxicity)
- **Fallbacks / circuit breakers** (fail secure)
- **Human in the loop** for high-impact decisions (excessive agency defense)

*Example: AI suggests refund → code checks policy limit → human approves >$50. AI suggests, your code decides.*

**2. Zero Trust for AI**

**Never trust, always verify** for AI infrastructure. **Vector database** = stores embeddings for **RAG**.

- **Per-user access control on retrieval** (else chatbot returns CEO salary doc = BOLA for AI); per-tenant separation; validate what's added (**poisoned docs** → indirect prompt injection)
- **AI/GPU clusters:** segmentation, strong authn, patching
- **Model endpoints:** authenticate every call, **rate limit** (model theft, unbounded consumption)
- **Model weights** = IP/trade secret: encrypt, restrict, **sign** (MLSecOps)
- Agents' tools: least privilege

*No free pass: verify every request, document, tool call.*

**3. AI-driven threat modeling**

AI helps defenders: suggests DFDs, proposes STRIDE threats, maps to ATT&CK/CAPEC, keeps the model updated (continuous).

Cautions: **hallucinates** (invents/misses threats) → **human review**; **data leakage** (architecture = attacker map) → approved enterprise tools only; **accountability stays with the team**.

*A brainstorming partner, not the judge.*

**4. Federated learning**

One shared model trained across many devices/orgs **without centralizing data**: local training → send **model updates (gradients/weights)**, not raw data → server **aggregates** → global model back. (Phone keyboards; hospitals.)

- Benefit: privacy + data minimization; helps localization.
- Risks: **poisoned updates** (malicious participant backdoors the model); **gradient leakage** (reconstruct private data from updates); compromised nodes.
- Controls: **authenticate participants**, **secure aggregation** (server can't see any single update), **differential privacy** (noise), **anomaly detection / robust aggregation**.

*The data stays home; only the lessons travel (check every lesson for poison).*

**On the exam**

- Keep core logic separate from AI → **decoupling** · AI SQL run directly → **improper output handling**
- Chatbot returns unauthorized docs → **per-user access control on vector DB** (zero trust for AI)
- AI proposes STRIDE threats → **AI-driven threat modeling** (human review)
- Train across hospitals without sharing records → **federated learning** · malicious updates → **poisoning** · server can't see individual updates → **secure aggregation**
- **Trap:** federated learning reduces but doesn't remove privacy risk.

**Quick check:** (1) RAG chatbot gives intern the confidential bonus spreadsheet: missing control? (2) Five hospitals train jointly without sharing records: approach + one risk? (3) App runs the AI's suggested SQL filter directly: principle violated?

**Answer:** Zero trust for AI (specific: per-user access control on vector DB retrieval); federated learning (risk: poisoned updates / gradient leakage); decoupling (improper output handling). All correct.

</details>

<a name="t-4-ai-3"></a>
**AI-driven threat modeling**

Using AI to map evolving attack surfaces during design.

> On the exam: What it means: AI tools help generate threats and attack paths from architecture diagrams, keeping up with fast-changing systems.
Trap: the output still needs human review; AI can miss threats or invent false ones.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.AI: AI in secure architecture (all 4 topics)**

**1. Decoupling AI inference**

**Inference** = model producing an answer (training builds it, inference uses it). AI is **non-deterministic** (different/wrong outputs, hallucinations).

**Principle:** core logic + critical decisions in **deterministic code**; AI = separate, **untrusted** component whose output is **advice, not a command**.

- AI in its **own tier/service**, least privilege (can't reach DB/payments directly)
- **Validate output** against a strict **schema** + allowed values; never straight into SQL/shell/web page (**improper output handling**)
- **Guardrails** in (prompt-injection screening) and out (sensitive data, toxicity)
- **Fallbacks / circuit breakers** (fail secure)
- **Human in the loop** for high-impact decisions (excessive agency defense)

*Example: AI suggests refund → code checks policy limit → human approves >$50. AI suggests, your code decides.*

**2. Zero Trust for AI**

**Never trust, always verify** for AI infrastructure. **Vector database** = stores embeddings for **RAG**.

- **Per-user access control on retrieval** (else chatbot returns CEO salary doc = BOLA for AI); per-tenant separation; validate what's added (**poisoned docs** → indirect prompt injection)
- **AI/GPU clusters:** segmentation, strong authn, patching
- **Model endpoints:** authenticate every call, **rate limit** (model theft, unbounded consumption)
- **Model weights** = IP/trade secret: encrypt, restrict, **sign** (MLSecOps)
- Agents' tools: least privilege

*No free pass: verify every request, document, tool call.*

**3. AI-driven threat modeling**

AI helps defenders: suggests DFDs, proposes STRIDE threats, maps to ATT&CK/CAPEC, keeps the model updated (continuous).

Cautions: **hallucinates** (invents/misses threats) → **human review**; **data leakage** (architecture = attacker map) → approved enterprise tools only; **accountability stays with the team**.

*A brainstorming partner, not the judge.*

**4. Federated learning**

One shared model trained across many devices/orgs **without centralizing data**: local training → send **model updates (gradients/weights)**, not raw data → server **aggregates** → global model back. (Phone keyboards; hospitals.)

- Benefit: privacy + data minimization; helps localization.
- Risks: **poisoned updates** (malicious participant backdoors the model); **gradient leakage** (reconstruct private data from updates); compromised nodes.
- Controls: **authenticate participants**, **secure aggregation** (server can't see any single update), **differential privacy** (noise), **anomaly detection / robust aggregation**.

*The data stays home; only the lessons travel (check every lesson for poison).*

**On the exam**

- Keep core logic separate from AI → **decoupling** · AI SQL run directly → **improper output handling**
- Chatbot returns unauthorized docs → **per-user access control on vector DB** (zero trust for AI)
- AI proposes STRIDE threats → **AI-driven threat modeling** (human review)
- Train across hospitals without sharing records → **federated learning** · malicious updates → **poisoning** · server can't see individual updates → **secure aggregation**
- **Trap:** federated learning reduces but doesn't remove privacy risk.

**Quick check:** (1) RAG chatbot gives intern the confidential bonus spreadsheet: missing control? (2) Five hospitals train jointly without sharing records: approach + one risk? (3) App runs the AI's suggested SQL filter directly: principle violated?

**Answer:** Zero trust for AI (specific: per-user access control on vector DB retrieval); federated learning (risk: poisoned updates / gradient leakage); decoupling (improper output handling). All correct.

</details>

<a name="t-4-ai-4"></a>
**Federated learning**

Training across distributed nodes without centralizing data; secure those nodes.

> On the exam: What it is: training a shared model across many devices or organizations without moving the raw data to one place.
Risks: malicious participants send poisoned updates; updates may leak information. Defenses: secure aggregation, validating updates, differential privacy.

<details><summary>Lesson (23 Oct 2026)</summary>

**4.AI: AI in secure architecture (all 4 topics)**

**1. Decoupling AI inference**

**Inference** = model producing an answer (training builds it, inference uses it). AI is **non-deterministic** (different/wrong outputs, hallucinations).

**Principle:** core logic + critical decisions in **deterministic code**; AI = separate, **untrusted** component whose output is **advice, not a command**.

- AI in its **own tier/service**, least privilege (can't reach DB/payments directly)
- **Validate output** against a strict **schema** + allowed values; never straight into SQL/shell/web page (**improper output handling**)
- **Guardrails** in (prompt-injection screening) and out (sensitive data, toxicity)
- **Fallbacks / circuit breakers** (fail secure)
- **Human in the loop** for high-impact decisions (excessive agency defense)

*Example: AI suggests refund → code checks policy limit → human approves >$50. AI suggests, your code decides.*

**2. Zero Trust for AI**

**Never trust, always verify** for AI infrastructure. **Vector database** = stores embeddings for **RAG**.

- **Per-user access control on retrieval** (else chatbot returns CEO salary doc = BOLA for AI); per-tenant separation; validate what's added (**poisoned docs** → indirect prompt injection)
- **AI/GPU clusters:** segmentation, strong authn, patching
- **Model endpoints:** authenticate every call, **rate limit** (model theft, unbounded consumption)
- **Model weights** = IP/trade secret: encrypt, restrict, **sign** (MLSecOps)
- Agents' tools: least privilege

*No free pass: verify every request, document, tool call.*

**3. AI-driven threat modeling**

AI helps defenders: suggests DFDs, proposes STRIDE threats, maps to ATT&CK/CAPEC, keeps the model updated (continuous).

Cautions: **hallucinates** (invents/misses threats) → **human review**; **data leakage** (architecture = attacker map) → approved enterprise tools only; **accountability stays with the team**.

*A brainstorming partner, not the judge.*

**4. Federated learning**

One shared model trained across many devices/orgs **without centralizing data**: local training → send **model updates (gradients/weights)**, not raw data → server **aggregates** → global model back. (Phone keyboards; hospitals.)

- Benefit: privacy + data minimization; helps localization.
- Risks: **poisoned updates** (malicious participant backdoors the model); **gradient leakage** (reconstruct private data from updates); compromised nodes.
- Controls: **authenticate participants**, **secure aggregation** (server can't see any single update), **differential privacy** (noise), **anomaly detection / robust aggregation**.

*The data stays home; only the lessons travel (check every lesson for poison).*

**On the exam**

- Keep core logic separate from AI → **decoupling** · AI SQL run directly → **improper output handling**
- Chatbot returns unauthorized docs → **per-user access control on vector DB** (zero trust for AI)
- AI proposes STRIDE threats → **AI-driven threat modeling** (human review)
- Train across hospitals without sharing records → **federated learning** · malicious updates → **poisoning** · server can't see individual updates → **secure aggregation**
- **Trap:** federated learning reduces but doesn't remove privacy risk.

**Quick check:** (1) RAG chatbot gives intern the confidential bonus spreadsheet: missing control? (2) Five hospitals train jointly without sharing records: approach + one risk? (3) App runs the AI's suggested SQL filter directly: principle violated?

**Answer:** Zero trust for AI (specific: per-user access control on vector DB retrieval); federated learning (risk: poisoned updates / gradient leakage); decoupling (improper output handling). All correct.

</details>
