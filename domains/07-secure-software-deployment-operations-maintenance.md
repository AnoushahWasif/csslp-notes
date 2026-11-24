# Domain 7: Secure Software Deployment, Operations, Maintenance

Exam weight: 11%

## 7.1 Operational risk analysis

<a name="t-7-1-1"></a>
**Deployment environments**

Development, QA/test, staging, production; keep them separated.

> On the exam: Developers shouldn't have production access (separation of duties), and production data doesn't belong in dev.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Separation of duties; system integration risk. Correct.

</details>

<a name="t-7-1-2"></a>
**Personnel training**

Administrators and users need different training.

> On the exam: What it means: administrators need training on secure configuration, operations and incident procedures; users need awareness of safe use and phishing.
Scenario cue: 'a breach happened because an admin left default settings' → admin training gap.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Separation of duties; system integration risk. Correct.

</details>

<a name="t-7-1-3"></a>
**Legal compliance**

Privacy laws, regulations, copyright and licensing in operation.

> On the exam: What it means: during operations the software must keep meeting laws and contracts: privacy laws, regulations, license terms, copyright.
Scenario cue: 'a new privacy law requires data deletion features' → operational compliance change.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Separation of duties; system integration risk. Correct.

</details>

<a name="t-7-1-4"></a>
**System integration risk** (review)

New software changes the risk of connected systems.

> On the exam: What it means: connecting the software to other systems in production can create new risks (new data flows, trust relationships, entry points).
Scenario cue: 'a new partner integration exposes internal APIs' → reassess risk before integrating.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Named system integration risk; fix (dedicated least-privileged account) not given. Shaky.

</details>

<a name="t-7-1-5"></a>
**Implementation and cutover (changeover) strategies** (review)

Ways to move from an old system to a new one: direct/big bang (switch at once), parallel (run both together), phased (module by module), pilot (one group or site first).

> On the exam: Risk: direct is cheapest but riskiest; parallel is safest but costly; pilot limits impact to one group.
Scenario cue: 'critical system, failure unacceptable, budget available' → parallel.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Hedged phased/parallel; answer parallel. Shaky.

</details>

<a name="t-7-1-6"></a>
**Software acceptance before deployment**

Formal sign-off that software meets functional and security requirements, with documentation, test results and risk acceptance complete, before release.

> On the exam: Includes: verifying security requirements are met, reviewing open findings against the bug bar, completeness of documentation, and approval to deploy.

<details><summary>Lesson (20 Nov 2026)</summary>

**Domain 7: Secure Deployment, Operations, Maintenance — 7.1 Operational risk analysis (6 topics)**

*Domain angle: keeping software secure after it's built — deploying, running, monitoring, patching, recovering. 7.1 angle: before go-live, ask what could go wrong in operation: environments, people, law, connected systems, and how you switch over.*

**1. Deployment environments**

**Development → test/QA → staging/pre-production (mirror of prod) → production.** Separate: different networks + credentials; **no real data outside production**; **developers don't have production access** (separation of duties, least privilege). Code is **promoted** by the pipeline; manage config with **IaC** — staging that **drifts** from prod makes its tests worthless.

**2. Personnel training**

Role-based: **administrators/operators** (secure config, patching, monitoring, incident procedures, privileged-access hygiene) · **users** (secure use, phishing, **reporting**) · **support/help desk** (resist **social engineering**, verify identity before resets). **Before go-live**, refreshers, **runbooks**. Untrained staff = top cause of misconfigurations/breaches.

**3. Legal compliance in operation**

Privacy laws (GDPR **72-hour** breach notification to the regulator) + **data residency** · retention/deletion · **licensing compliance** (open-source obligations, seats) · copyright · export controls · sector rules (PCI DSS, HIPAA) · **audit evidence** (logs). Laws change → keep monitoring (7.7).

**4. System integration risk**

New software changes the risk of connected systems: new trust relationships, data flows, bigger attack surface, **shared credentials**, compatibility compromises (enabling old TLS for a legacy system). Before deploying: update the **threat model**, **integration testing**, **interconnection agreements (ISA/MOU)**, **each integration gets its own least-privileged account**.

**5. Cutover (changeover) strategies**

- **Direct / big bang:** all at once — fastest, cheapest, **riskiest** (no fallback)
- **Parallel:** old + new side by side — **safest** (old keeps running → zero downtime risk), **most expensive**
- **Phased:** one module/region at a time — moderate risk, longer (switched modules can still fail users)
- **Pilot:** one group/site first — limits damage
- Modern: **blue-green** (two identical prod environments, switch traffic, instant rollback) · **canary** (small % of traffic first)
- Always: **rollback plan**; protect both systems in parallel; **decommission the old one securely** (2.6).

*Hook: big bang = jump in all at once; parallel = keep the old bridge open while testing the new one; phased = one room at a time; pilot = a test kitchen; canary = the bird that warns you first.*

**6. Software acceptance before deployment**

**Formal sign-off by the business owner / authorizing official** at a **go/no-go** decision: requirements met (traceability matrix) · test results reviewed · open vulns **within the bug bar** or risk-accepted · documentation complete (install, admin, user guides, **DRP/BCP**, runbooks) · training done. Ties to 6.8 + 7.6.

**On the exam**

- Zero downtime tolerance, cost no issue → **parallel** · fastest/cheapest, no fallback → **big bang**
- One branch first → **pilot** · one module at a time → **phased** · 5% of traffic first → **canary**
- Developers admin in prod → **environment separation / separation of duties** · staging ≠ prod → **drift**
- Help desk resets without verifying → **training** gap · CRM ↔ billing via shared admin → **system integration risk** → dedicated least-privileged accounts
- **Traps:** parallel is safest, not cheapest; acceptance is a business sign-off, not the testers'.

**Quick check + your answers**

1. Bank can't risk downtime, can afford cost → you said "phased or parallel" → **parallel** (commit to one; old system runs the whole time).

2. Developers have prod admin → **separation of duties** ✅

3. CRM ↔ billing via shared admin account → **system integration risk** ✅; fix not given → **dedicated least-privileged integration account**.

**Quick check:** (1) Bank can't risk any downtime, can afford cost: cutover? (2) Developers with prod admin: problem? (3) CRM ↔ billing via shared admin account: risk area + fix?

**Answer:** Separation of duties; system integration risk. Correct.

</details>

## 7.2 Configuration and version control

<a name="t-7-2-1"></a>
**Hardware inventory**

Know what you run before you can secure it.

> On the exam: What it is: a complete list of hardware (and software) assets, owners and locations.
Why: you can't patch, monitor or protect what you don't know exists.
Scenario cue: 'an unknown server was compromised' → incomplete asset inventory.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

<a name="t-7-2-2"></a>
**Baseline configuration**

Approved secure starting configuration, e.g., CIS Benchmarks or DISA STIGs.

> On the exam: What it is: the approved, secure starting configuration for a system type (e.g., CIS Benchmark, DISA STIG).
Use: build every system from it, scan regularly against it, treat deviations as findings needing change approval.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

<a name="t-7-2-3"></a>
**Configuration drift**

Systems slowly diverging from the baseline.

> On the exam: What it is: systems slowly moving away from the baseline through manual changes and quick fixes.
Detect: configuration scanning, comparing against IaC. Fix: redeploy from the baseline or template.
Scenario cue: 'servers built identically now have different settings' → configuration drift.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

<a name="t-7-2-4"></a>
**Configuration management database (CMDB)** (review)

Record of configuration items and relationships.

> On the exam: What it is: database recording configuration items (servers, apps, versions) and their relationships.
Use: impact analysis before changes, faster troubleshooting and incident response.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Said documentation; answer CMDB. Shaky.

</details>

<a name="t-7-2-5"></a>
**Version control**

Branch protection, required reviews, signed commits, history.

> On the exam: What it is: tracking every code change with who, when and why (Git). Supports rollback and accountability.
Controls: protected main branch, required reviews and approvals, signed commits, no secrets in repos.
Scenario cue: 'malicious code merged with no review' → missing branch protection.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

<a name="t-7-2-6"></a>
**Documentation practices**

Record changes, versions and configurations.

> On the exam: What it means: keep accurate records of configurations, versions, changes and procedures.
Why: speeds incident response and recovery, supports audits and knowledge transfer.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

<a name="t-7-2-7"></a>
**Re-engineering during maintenance**

Changing legacy software to improve maintainability or move it to new platforms.

> On the exam: Security angle: rerun threat modeling and full security testing; changes in environment can break old assumptions.

<details><summary>Lesson (20 Nov 2026)</summary>

**7.2 Configuration and version control (7 topics)**

*Angle: you can only secure what you know you have and know the state of — inventory, approved baselines, catching drift, tracking every change.*

**1. Hardware inventory**

Every asset (servers, laptops, network devices, IoT, **cloud resources**) with owner, location, OS/firmware, criticality. "You can't protect what you don't know you have" — **CIS Control 1** (hardware), Control 2 (software). **Automated discovery** catches **shadow IT** + rogue devices. Feeds vuln management (which assets a CVE affects) + **end-of-life** tracking.

**2. Baseline configuration**

Approved, documented **secure starting configuration** per system type. Sources: **CIS Benchmarks** · **DISA STIGs** (Security Technical Implementation Guides, US DoD) · vendor hardening guides. **Versioned**, changed only via **change management**, used for **golden images**. (Minimum security baseline → 7.5.)

**3. Configuration drift**

Systems slowly diverge from the baseline (manual hotfixes, one-off changes, uneven patches) → unknown weaknesses, inconsistency, failed audits. Detect: config compliance scanning, FIM, IaC drift detection. **Fix: restore the system to the baseline**; don't change the baseline to match drift (unless approved change). **Immutable infrastructure** prevents drift.

*Hook: baseline = the approved recipe; drift = each kitchen quietly changing it; fix the kitchen, not the recipe.*

**4. Configuration management database (CMDB)**

**Configuration items (CIs)** — servers, apps, databases, network devices, licenses — **and their relationships/dependencies**. Used for **change impact analysis** ("what breaks if I change this?"), **incident response**, **vulnerability management**. Must be accurate (automated discovery). ITIL concept.

*Hook: CMDB = the family tree of your systems. Clue: "what depends on what" → CMDB.*

**5. Version control**

Full history (who/what/when/why) → accountability + rollback. Repo controls: **branch protection** (no direct pushes to main) · **required reviews/approvals** (separation of duties) · **signed commits** (prove authorship) · **required status checks** (CI + scans pass) · least-privilege access + **MFA** · **secret scanning** · **tagged releases**. Config + IaC in version control too. (Repo protection again in 8.3.)

*Hook: version control = a time machine that also takes fingerprints.*

**6. Documentation practices**

Document configurations, **changes** (who/what/when/why/approver), versions/releases, architecture, runbooks. Keep current; **protect sensitive docs** (network diagrams = attacker's map); link changes to tickets (audit trail).

**7. Re-engineering during maintenance**

Refactor legacy structure or **migrate platforms** (COBOL → Java, on-prem → cloud) **without changing behavior**; often starts with **reverse engineering** (poorly documented). Security: **preserve existing controls** (authentication, logging, audit trails), **re-run threat modeling + security testing** (new platform = new risks), **regression tests**.

**On the exam**

- Unknown devices on the network → missing **hardware inventory** · CIS/DoD hardened config → **baseline** (CIS Benchmarks / DISA STIGs)
- 40 servers differ after manual fixes → **drift** → restore to baseline · which apps depend on this DB → **CMDB**
- Push straight to main, no review → **branch protection / required reviews** · prove authorship → **signed commits**
- Network diagrams on a public share → poor documentation protection · COBOL → Java dropped logging → **re-engineering** risk → preserve controls, re-test
- **Traps:** fix drift by restoring the system, not editing the baseline; re-engineering must not lose existing controls.

**Quick check + your answers**

1. 40 servers no longer match the hardening standard → **configuration drift**, restore to baseline ✅

2. Which apps depend on the DB server → you said documentation → **CMDB**.

3. Push straight to main with no review → **branch protection + required reviews** ✅ (signed commits = authorship, wouldn't stop an unreviewed push alone).

**Quick check:** (1) 40 servers differ from hardening standard after manual fixes: name + fix? (2) Which apps depend on this DB server: where to look? (3) Push straight to main with no review: missing control?

**Answer:** Drift → restore baseline; branch protection + required reviews. Correct.

</details>

## 7.3 Release software securely

<a name="t-7-3-1"></a>
**Secure CI/CD pipeline**

Least-privilege runners, protected secrets, approvals, isolated build agents.

> On the exam: What it is: a build-and-deploy pipeline protected as a critical system: least-privilege service accounts, secrets in a vault, isolated build agents, signed artifacts, approval gates, full logging.
Scenario cue: 'attackers modified the build script to insert a backdoor' → pipeline was not secured; this is a supply chain attack.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-3-2"></a>
**Application security toolchain**

SAST, DAST, SCA, secret scanning, container and IaC scanning in the pipeline.

> On the exam: What it is: the set of security tools in the pipeline: SAST (your code), SCA (dependencies), secret scanning, IaC scanning, container scanning, DAST/IAST (running app).
Trap: no single tool covers everything; combine them.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-3-3"></a>
**Build artifact verification**

Code signing and hashes prove the artifact is what was built.

> On the exam: What it is: checking that what you deploy is exactly what was built and approved, using code signatures and hashes (checksums), plus provenance records.
Scenario cue: 'how do you make sure the binary in production wasn't swapped?' → verify signature and hash before deploying.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-3-4"></a>
**Artifact repository**

Controlled, trusted storage for build outputs.

> On the exam: What it is: a controlled store for build outputs (packages, images). Only artifacts from here get promoted from test to production.
Controls: access control, immutability, scanning, signing.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-3-5"></a>
**Release management**

Planning, scheduling, packaging and controlling the move of approved changes into production.

> On the exam: Security points: only tested, approved, signed builds are released; release notes; rollback plan; separation of duties between those who write and those who release code.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

## 7.4 Store and manage security data

<a name="t-7-4-1"></a>
**Secrets management**

Vaults, never in code or repos; rotate regularly.

> On the exam: What it is: storing passwords, API keys and tokens in a dedicated vault (HashiCorp Vault, cloud secret managers), not in code, configs or repos. Access is controlled, logged and rotated.
Scenario cue: 'an API key was committed to GitHub' → revoke and rotate it immediately (deleting the commit isn't enough).

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-4-2"></a>
**Key lifecycle**

Generation, distribution, storage, use, rotation, revocation, destruction.

> On the exam: Stages: generation (strong random), distribution (secure channel), storage (HSM/KMS), use (only for its purpose), rotation (regularly), revocation (if compromised), archival, destruction.
Scenario cue: 'one key used for years to encrypt everything' → no rotation, no separation of key purposes.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-4-3"></a>
**HSM and KMS**

Hardware security modules and key management services protect keys.

> On the exam: HSM: tamper-resistant hardware that generates and stores keys and does crypto; keys can't be exported. KMS: managed service (often HSM-backed) to create, store and control keys, with logged access.
Scenario cue: 'protect the code signing private key' → HSM.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-4-4"></a>
**Certificate management**

Track expiration, renewal and revocation.

> On the exam: What it means: track all certificates, renew before expiry (automate), revoke compromised ones (CRL/OCSP), protect private keys.
Scenario cue: 'site went down because a certificate expired' → poor certificate lifecycle management.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-4-5"></a>
**Key escrow**

A trusted third party holds a copy of keys for recovery.

> On the exam: What it is: a trusted third party keeps copies of keys so data can be recovered if keys are lost or for legal access.
Risk: the escrow becomes a high-value target. Don't confuse with code escrow (source code held for the customer).

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

<a name="t-7-4-6"></a>
**Configuration data**

Protect config files that contain sensitive settings.

> On the exam: What it means: config files often contain connection strings and settings; encrypt sensitive values, restrict access, version-control them and keep secrets out of them.

<details><summary>Lesson (24 Nov 2026)</summary>

**7.3 Release software securely (5) + 7.4 Store and manage security data (6) — 11 topics**

**7.3 angle: the pipeline is the road from code to production — protect the road, check everything on it, keep a trusted warehouse at the end.**

**1. Secure CI/CD pipeline (7.3.1)**

**Least-privilege runners** (no admin, narrowly scoped tokens) · **isolated, ephemeral agents** (fresh per job, nothing persists) · **protected secrets**: vault, **masked in logs**, never in pipeline files, **scoped per environment**, **short-lived credentials (OIDC federation)** instead of long-lived keys · **approval gates** before production (separation of duties) · pipeline definition is code: reviewed, protected, restricted edit rights, every run logged · **untrusted PRs (forks) get no secrets**.

**2. Application security toolchain (7.3.2)**

SAST · SCA (+ licenses) · **secret scanning** (pre-commit + pipeline) · **IaC scanning** · **container image scanning** · DAST vs staging · SBOM generation · gates enforce the **bug bar** · results to the tracker · tune noise.

**3. Build artifact verification (7.3.3)**

**Hash** (integrity) + **signature** (origin); **verify before deploying, reject unsigned**. **Provenance attestations** (who built it, from which commit, on which builder — **SLSA**). Reproducible builds. Kubernetes: sign images (**cosign**) + **admission controllers** allow only signed images.

**4. Artifact repository (7.3.4)**

Single trusted store for build outputs + approved third-party packages (**Artifactory**, **Nexus**, registries; proxies public registries). **Immutable versions**, **only the pipeline publishes**, scanned, stored with signatures + metadata, retention policies. Deployments pull from your warehouse, not the internet.

**5. Release management (7.3.5)**

Plan, schedule, package, control the move of **approved** changes into prod: release notes, **semantic versioning (MAJOR.MINOR.PATCH)**, calendars + maintenance windows, go/no-go, **rollback plans**. Trio: **change = "may we?"** · **configuration = "what do we have?"** · **release = "ship it."**

*Hook: protect the road (pipeline), inspect every truck (toolchain), check the seal (signatures), keep a locked warehouse (artifact repository).*

**7.4 angle: keys and secrets are the crown jewels — where they live, how long, who can touch them.**

**6. Secrets management (7.4.1)**

Passwords, API keys, tokens, private keys, connection strings → **vault** (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault). **Never** in code, repos, plain config, images, logs, tickets. Identity-based least-privilege access, **audit**, **rotate** regularly + immediately after leaks, **dynamic secrets** (on request, short-lived), secret scanning.

**7. Key lifecycle (7.4.2)**

**Generation** (strong RNG, inside an HSM) → **distribution** (secure channel, **wrapped**) → **storage** (HSM/KMS) → **use** (intended purpose only; **key separation**) → **rotation** (end of **cryptoperiod**) → **backup/archival** (decrypt old data; escrow) → **revocation/suspension** (compromise) → **destruction** (**zeroization**; crypto-shredding). **NIST SP 800-57** = key management recommendations.

*Hook: born, shipped, stored, used, renewed, backed up, retired, destroyed.*

**8. HSM vs KMS (7.4.3)**

**HSM** = dedicated **tamper-resistant hardware**; generates/stores keys, crypto **inside**, keys never leave in plain form; **FIPS 140** validated (often L3); expensive; on-prem or cloud (CloudHSM); **root CA keys, payment keys (PCI)**. **KMS** = **managed cloud service** (AWS KMS, Azure Key Vault, Google Cloud KMS), usually HSM-backed; **APIs + IAM policies + automatic rotation + audit logs**; **envelope encryption** (KEK encrypts DEKs). **BYOK** (import your key) vs **HYOK** (key stays with you).

*Hook: HSM = your own vault room; KMS = the bank's safe-deposit service (with a vault room behind it).*

**9. Certificate management (7.4.4)**

**Inventory** (where, expiry, owner) · **monitor expiry + alert** · **automate renewal** (**ACME**, Let's Encrypt, cert-manager) · **revoke** compromised (CRL/OCSP) · protect private keys. Expired certs = **outages**; public TLS lifetimes shrinking (toward **47 days by 2029**) → automation essential.

**10. Key escrow (7.4.5)**

Copy of keys with a trusted third party (or internal) for **recovery** or **legal access**. Risk: single high-value target, insider abuse. Controls: **split knowledge**, **M-of-N** (any 3 of 5 officers), **dual control**, strict access + audit. ≠ **code escrow** (8.5, source code).

**11. Configuration data (7.4.6)**

Configs hold secrets, endpoints, feature flags, debug settings. Move secrets to a vault (**reference only**) · restrict permissions · encrypt sensitive values · separate per environment · version control **without secrets** · **validate at startup** · **debug off in prod** · changes via change management.

**On the exam**

- Long-lived cloud admin key in the pipeline → **short-lived OIDC credentials**, least privilege · fork PRs read secrets → block secrets for untrusted PRs
- Only signed images in the cluster → **artifact verification** (admission control) · overwritten release version → **immutable versions**
- Approved change now scheduled/packaged/deployed → **release management**
- API key in Git → **revoke + rotate**, vault, secret scanning (and remove from history)
- Tamper-resistant hardware, keys never leave → **HSM** · managed cloud keys + IAM + auto-rotation → **KMS**
- Keep old keys to decrypt archives → **archival** · outage from expired cert → **certificate management** (ACME automation)
- Any 3 of 5 officers to recover → **M-of-N**
- **Traps:** key escrow ≠ code escrow; rotating a leaked secret isn't enough without removing it and finding the cause.

**Quick check + your answers**

1. Cluster runs only pipeline-built, signed images → started with "certificate management", settled on **build artifact verification** ✅

2. Managed cloud service with APIs, IAM, auto-rotation → **KMS** ✅

3. Any 3 of 5 officers to recover an escrowed key → **M-of-N control** ✅

**Quick check:** (1) Cluster runs only pipeline-built, signed images: which practice? (2) Managed cloud service with APIs, IAM, auto-rotation: HSM or KMS? (3) Any 3 of 5 officers to recover an escrowed key: control?

**Answer:** Artifact verification; KMS; M-of-N. All correct.

</details>

## 7.5 Secure installation

<a name="t-7-5-1"></a>
**Secure boot**

Chain of trust verifying each boot stage's signature; protect key generation and access.

> On the exam: What it is: each boot stage verifies the next stage's signature before running it, starting from a hardware root of trust.
Why: stops bootkits and rootkits. Key generation, access and management for signing keys must be protected.
Scenario cue: 'malware modified the bootloader' → secure boot would have blocked it.

<a name="t-7-5-2"></a>
**Least privilege installation**

Run services with minimal rights, not as admin/root.

> On the exam: What it means: install and run services with the minimum rights needed, not as root/administrator, and remove any temporary elevated rights after installation.
Scenario cue: 'the web service runs as SYSTEM' → violates least privilege.

<a name="t-7-5-3"></a>
**Environment hardening**

Disable unused services and ports, remove defaults, patch, firewall.

> On the exam: What it is: reducing attack surface on the deployed system: remove unused services, ports and sample apps; change default credentials; apply patches; configure firewalls; follow CIS/STIG baselines.

<a name="t-7-5-4"></a>
**Secure provisioning**

Deliver credentials, configs and licenses securely; use IaC.

> On the exam: What it is: delivering systems with unique credentials, secure configurations and licensing, usually automated with IaC.
Scenario cue: 'every customer device ships with the same admin password' → insecure provisioning.

<a name="t-7-5-5"></a>
**Secure defaults**

Ship in the most secure configuration out of the box.

> On the exam: What it is: the product is secure out of the box: strongest settings on, unneeded features off, no default passwords, users must choose to weaken settings.
Why: most users never change defaults.
Scenario cue: 'debug mode enabled by default in production builds' → insecure default.

<a name="t-7-5-6"></a>
**Minimum security baseline (MSB)**

The most restrictive standard configuration that all systems must meet before going into production; supports hardening.

> On the exam: Scenario cue: 'every server must meet a defined lockdown level before deployment' → MSB.

## 7.6 Security approval to operate

<a name="t-7-6-1"></a>
**Authority to operate (ATO)**

Formal approval to run the system in production.

> On the exam: What it is: formal approval from a senior official (Authorizing Official) to put the system into production after reviewing security assessment results.
Scenario cue: 'which step comes before a federal system goes live?' → authorization (ATO).

<a name="t-7-6-2"></a>
**Risk acceptance and sign-off**

The right-level owner formally accepts residual risk.

> On the exam: What it means: someone with enough authority over the business risk formally accepts the residual risk in writing.
Trap: developers or security testers can't accept risk for the business; the owner/senior management does.

<a name="t-7-6-3"></a>
**POA&M**

Plan of action and milestones for open issues.

> On the exam: What it is: Plan of Action and Milestones, a list of known weaknesses with planned fixes, owners and deadlines, accepted at authorization time.
Scenario cue: 'how are weaknesses not fixed before go-live tracked?' → POA&M.

## 7.7 Continuous monitoring

<a name="t-7-7-1"></a>
**ISCM (NIST SP 800-137)**

Information security continuous monitoring.

> On the exam: What it is: Information Security Continuous Monitoring, ongoing awareness of security, vulnerabilities and threats to support risk decisions, instead of point-in-time checks.
Scenario cue: 'the system was assessed once three years ago' → move to continuous monitoring.

<a name="t-7-7-2"></a>
**Observable data**

Logs, events, telemetry, traces, metrics.

> On the exam: Types: logs (records of events), events (things that happened), telemetry (performance/health data), traces (a request's path across services), metrics (numbers over time).
Requirements: centralize, keep clocks synced (NTP), protect integrity, retain as required.

<a name="t-7-7-3"></a>
**IDS vs IPS**

Detects vs blocks; signature-based vs anomaly-based; host vs network.

> On the exam: Signature-based misses zero-days; anomaly-based catches new attacks but has more false positives. An IPS sits inline and can block, and can also cause outages.

<a name="t-7-7-4"></a>
**SIEM**

Collects and correlates logs from many sources to detect incidents.

> On the exam: What it is: Security Information and Event Management: collects logs from many sources, normalizes and correlates them, alerts on suspicious patterns, supports investigation and compliance reporting.
Scenario cue: 'detect an attack visible only by combining firewall, server and app logs' → SIEM correlation.

<a name="t-7-7-5"></a>
**SOAR**

Automates response playbooks.

> On the exam: What it is: Security Orchestration, Automation and Response: runs automated playbooks (block an IP, disable an account, open a ticket) when alerts fire.
Scenario cue: 'too many alerts, slow response' → SOAR automation.

<a name="t-7-7-6"></a>
**Regulation and privacy changes**

Monitor for new laws that change requirements.

> On the exam: What it means: monitor for new or changed laws and regulations that may require changes to software (e.g., new privacy rights, breach notification rules).

<a name="t-7-7-7"></a>
**Logging and monitoring essentials**

What to log: logins (success/failure), access to sensitive data, privilege changes, admin actions, security errors. What not to log: passwords, keys, full card numbers, unneeded PII.

> On the exam: Controls: synced time (NTP), central collection, integrity protection (append-only, hashing), retention policy, regular review with alerts.
Scenario cue: 'attackers deleted local logs' → logs should have been forwarded to a central, protected server.

<a name="t-7-7-8"></a>
**Honeypots and honeytokens**

Honeypot: a decoy system to attract and study attackers. Honeynet: a network of them. Honeytoken: fake data (fake credentials or records) that triggers an alert if used.

> On the exam: Trap: honeypots must be isolated, and enticement is fine but entrapment raises legal issues.

<a name="t-7-7-9"></a>
**Monitoring methods and metrics**

Ways to monitor: logs and audits, IDS/IPS, SIEM, performance monitoring, synthetic transactions. Metrics: incidents over time, time to detect and respond, availability, failed logins.

> On the exam: Syslog is the standard protocol for sending log messages to a central server.

## 7.8 Incident response

<a name="t-7-8-1"></a>
**Incident triage**

Confirm, classify and prioritize incidents.

> On the exam: What it is: quickly confirming whether an event is a real incident, classifying it, assessing impact and setting priority and escalation.
Scenario cue: 'many alerts arrive at once; what first?' → triage to focus on the most severe.

<a name="t-7-8-2"></a>
**Forensics**

Chain of custody, order of volatility, hash evidence to prove integrity.

> On the exam: Collect the most volatile evidence first (memory before disk). Don't reboot a compromised machine before capturing it.

<a name="t-7-8-3"></a>
**Remediation**

Contain, eradicate the cause, recover safely.

> On the exam: Order: containment (stop the spread, isolate systems) → eradication (remove malware, close the vulnerability) → recovery (restore from clean backups, monitor).
Trap: containment comes before eradication.

<a name="t-7-8-4"></a>
**Root cause analysis**

Find the underlying cause (5 whys, fishbone) so it doesn't recur.

> On the exam: What it is: finding the underlying reason an incident happened, not just the symptom. Methods: 5 whys, fishbone diagram.
Scenario cue: 'the same breach keeps happening after servers are cleaned' → root cause not fixed (e.g., an unpatched flaw in the code).

<a name="t-7-8-5"></a>
**Lessons learned**

Post-incident review feeding improvements back into the lifecycle.

> On the exam: What it is: a post-incident review of what happened, what worked and what didn't, and what to improve. Results go back into requirements, coding standards, training and the IR plan.

<a name="t-7-8-6"></a>
**Events, alerts, incidents**

Event: any observable occurrence. Alert: an event flagged as possibly important. Incident: an event that harms or threatens confidentiality, integrity or availability, or breaks policy.

> On the exam: Scenario cue: 'one failed login' → event. 'Thousands of failed logins against many accounts' → incident.

<a name="t-7-8-7"></a>
**Incident vs problem management**

Incident management restores normal service as fast as possible. Problem management finds and removes the root cause so incidents don't recur.

> On the exam: Scenario cue: 'the service is back up, but why does it keep failing?' → problem management.

<a name="t-7-8-8"></a>
**Incident response exercises**

Tabletop exercise (discussion through a scenario), walkthrough, simulation, and full live exercises; they test the plan, roles and communication.

> On the exam: Scenario cue: 'cheapest way to test the IR plan without disrupting systems' → tabletop exercise.

## 7.9 Patch management

<a name="t-7-9-1"></a>
**Patch process**

Identify, test, approve, deploy, verify, with a rollback plan.

> On the exam: Steps: identify patches, assess risk, test in non-production, approve via change management, deploy, verify, with a rollback plan.
Scenario cue: 'a patch applied directly to production broke the app' → skipped testing and change management.

<a name="t-7-9-2"></a>
**Emergency patching**

Expedited process for actively exploited vulnerabilities.

> On the exam: What it is: a fast-track process for critical, actively exploited flaws: expedited testing and approval, documented and reviewed afterwards.
Trap: emergency doesn't mean skipping change management entirely.

## 7.10 Vulnerability management

<a name="t-7-10-1"></a>
**CVE and NVD**

Public IDs for vulnerabilities and NIST's database of them.

> On the exam: CVE: a unique ID for a publicly known vulnerability (CVE-2021-44228). NVD: NIST's database adding CVSS scores, affected products and references.
Scenario cue: 'where do you find the severity score of a known CVE?' → NVD.

<a name="t-7-10-2"></a>
**Triage and tracking**

Prioritize by CVSS, exploitability (e.g., EPSS, CISA KEV) and asset value.

> On the exam: Process: discover → triage (validate, score) → prioritize → assign → fix → verify → close.
Prioritize with CVSS, plus exploitation data: CISA KEV (known exploited) and EPSS (probability of exploitation), plus asset value.
Scenario cue: 'medium CVSS but listed in KEV' → prioritize it, it's actively exploited.

<a name="t-7-10-3"></a>
**Remediation SLAs**

Deadlines by severity, e.g., critical within days.

> On the exam: What it is: fix deadlines by severity, e.g., critical 7 days, high 30, medium 90.
Measured by mean time to remediate; missed SLAs need risk acceptance or exceptions.

## 7.11 Runtime protection

<a name="t-7-11-1"></a>
**RASP**

Runtime application self-protection: inside the app, blocks attacks with app context.

> On the exam: What it is: Runtime Application Self-Protection, built into the app's runtime; sees exactly how input is used and blocks attacks in real time.
Strengths: app context, low false positives. Weaknesses: performance overhead, tied to the language/runtime.
Don't confuse: RASP is inside the app; a WAF is outside. IAST tests; RASP protects.

<a name="t-7-11-2"></a>
**WAF**

Web application firewall: outside the app, filters HTTP traffic.

> On the exam: What it is: Web Application Firewall, in front of the app; inspects HTTP traffic and blocks attack patterns (SQLi, XSS).
Use: virtual patching while a real fix is built.
Trap: a WAF is a compensating layer, not a replacement for fixing the code.

<a name="t-7-11-3"></a>
**ASLR**

Randomizes memory addresses so exploits can't predict locations.

> On the exam: What it is: Address Space Layout Randomization, loads code and data at random memory addresses each run, so attackers can't predict where to jump.
Scenario cue: 'exploits relying on fixed memory addresses stop working' → ASLR.

<a name="t-7-11-4"></a>
**DEP / NX**

Data execution prevention: memory marked as data can't be executed.

> On the exam: What it is: Data Execution Prevention / No-eXecute bit: memory areas for data (stack, heap) can't run as code.
Scenario cue: 'injected shellcode on the stack fails to execute' → DEP/NX.
Together with ASLR: DEP stops running injected code; ASLR stops reusing existing code at known addresses.

## 7.12 Continuity of operations

<a name="t-7-12-1"></a>
**Backup, archiving, retention**

Backups are for recovery; archives for long-term retention.

> On the exam: Backup: copy for recovery after loss or ransomware (3-2-1 rule: 3 copies, 2 media types, 1 offsite; plus offline/immutable). Archive: long-term retention of data no longer active. Retention: how long each must be kept.
Trap: an untested backup is not a backup; test restores regularly.

<a name="t-7-12-2"></a>
**DRP vs BCP**

Disaster recovery restores IT; business continuity keeps the business running.

> On the exam: DRP: restoring IT systems after a disaster (technical focus). BCP: keeping critical business functions running during and after a disruption (whole-business focus). DRP is part of BCP.
Scenario cue: 'how will staff process orders while the system is down?' → BCP.

<a name="t-7-12-3"></a>
**Business impact analysis (BIA)**

Identifies critical functions and drives recovery targets.

> On the exam: What it is: identifies critical business processes, impact of their loss over time, and dependencies. It sets MTD, RTO and RPO.
Scenario cue: 'first step in continuity planning' → BIA.

<a name="t-7-12-4"></a>
**RTO, RPO, MTD**

Time to restore, acceptable data loss, maximum tolerable downtime (RTO must be under MTD).

> On the exam: MTD: longest the business can survive the outage. RTO: target time to restore (must be less than MTD). RPO: maximum acceptable data loss in time, which sets backup frequency.
Scenario cue: 'can lose at most 15 minutes of data' → RPO 15 minutes; needs replication or very frequent backups.

<a name="t-7-12-5"></a>
**MTBF and MTTR**

Mean time between failures; mean time to repair.

> On the exam: MTBF: average time between failures (reliability; higher is better). MTTR: average time to repair (lower is better).
Availability improves when MTBF rises and MTTR falls.

<a name="t-7-12-6"></a>
**Hot, warm, cold sites**

Ready immediately / partly equipped / space only.

> On the exam: Hot site: fully equipped, data current, ready in minutes to hours (most expensive). Warm site: equipment but not current data, days. Cold site: space and power only, weeks (cheapest).
Scenario cue: 'RTO of 1 hour' → hot site (or active-active cloud).

<a name="t-7-12-7"></a>
**Resiliency**

Operational redundancy, erasure coding, survivability, DoS/DDoS protection.

> On the exam: Operational redundancy: duplicate systems and failover. Erasure coding: data split with parity so lost pieces can be rebuilt. Survivability: keep critical functions under attack. DoS protection: rate limiting, CDNs, scrubbing services, autoscaling.

<a name="t-7-12-8"></a>
**DR and BCP test types**

Checklist (review the plan), tabletop/structured walkthrough (talk through a scenario), simulation (practice without switching systems), parallel (bring up recovery site while production keeps running), full interruption (shut down production and fail over; most realistic and most risky).

> On the exam: Scenario cue: 'most thorough test, but could disrupt the business' → full interruption.

## 7.13 SLOs and SLAs

<a name="t-7-13-1"></a>
**SLI, SLO, SLA**

Measurement / internal target / contractual commitment with penalties.

> On the exam: SLI (indicator): the actual measurement, e.g., uptime %. SLO (objective): the internal target, e.g., 99.95%. SLA (agreement): the contractual promise with penalties, e.g., 99.9%.
Rule: set the SLO stricter than the SLA to leave a buffer.

<a name="t-7-13-2"></a>
**SLA contents**

Maintenance windows, performance, availability (nines), qualified personnel.

> On the exam: Include: availability target (e.g., 99.9% = about 8.8 hours of downtime per year), performance, maintenance windows, support response times, qualified staff, security duties (incident notification time, patch timelines), and penalties.

## 7.AI AI additions in the current outline

<a name="t-7-ai-1"></a>
**AIOps**

Using AI to monitor and self-heal infrastructure.

> On the exam: What it is: using AI to monitor operations, detect anomalies and fix issues automatically (self-healing).
Risk: automated actions need limits and human oversight so a wrong decision doesn't cause an outage.

<a name="t-7-ai-2"></a>
**Model drift**

Model accuracy degrading in production as real data changes.

> On the exam: What it is: model performance drops because real-world data changes from what it was trained on.
Controls: monitor accuracy and input distributions; retrain and revalidate; alert on sudden changes (which may also signal an attack).

<a name="t-7-ai-3"></a>
**Sandboxed staging for models**

Test updated model weights in isolation before deployment.

> On the exam: What it means: test new model versions in an isolated staging environment (behavior, safety, security) before production; keep the ability to roll back.

<a name="t-7-ai-4"></a>
**EU AI Act**

Risk-based EU regulation of AI systems.

> On the exam: What it is: EU law classifying AI systems by risk: unacceptable (banned), high-risk (strict requirements: risk management, data quality, logging, human oversight), limited (transparency duties), minimal.

<a name="t-7-ai-5"></a>
**AI-generated code legal risk**

Copyright and licensing questions around generated code.

> On the exam: What it means: AI-generated code may copy licensed code or have unclear copyright. Track provenance and scan for license matches.
