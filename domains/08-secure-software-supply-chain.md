# Domain 8: Secure Software Supply Chain

Exam weight: 10%

## 8.1 Supply chain risk management

<a name="t-8-1-1"></a>
**ISO/IEC 27036**

Information security for supplier relationships.

> On the exam: What it is: the ISO standard for information security in supplier relationships, covering the whole lifecycle: planning, selecting suppliers, contracting, managing, and ending the relationship. Part 4 covers cloud services.
Scenario cue: 'which ISO standard guides managing security with suppliers across the relationship?' → ISO/IEC 27036.
Don't confuse: 27001 = your own ISMS; 27034 = application security; 27036 = suppliers; ISO 28000 = physical supply chain security.

<a name="t-8-1-2"></a>
**NIST SP 800-161**

Cybersecurity supply chain risk management (C-SCRM).

> On the exam: What it is: NIST's guidance on cybersecurity supply chain risk management (C-SCRM) for organizations: identifying, assessing and mitigating risks from suppliers, products and services across their lifecycle, at organization, mission and system levels.
Scenario cue: 'which NIST publication focuses on supply chain risk management?' → SP 800-161.
Don't confuse: 800-218 (SSDF) = how to build software securely; 800-161 = how to manage supplier and supply chain risk; 800-53 SR family = supply chain controls.

<a name="t-8-1-3"></a>
**Component identification and selection**

Choose components based on security, support and reputation.

> On the exam: What it means: choose components using criteria: security history, active maintenance, community size, license, origin, support.
Scenario cue: 'two libraries do the same job; one is abandoned with open CVEs' → choose the maintained one.

<a name="t-8-1-4"></a>
**Component risk assessment**

Mitigate or accept each component's risk.

> On the exam: What it means: evaluate each component's risk, then decide: mitigate (patch, wrap, isolate), accept (documented), or replace.
Scenario cue: 'a needed library has a vulnerability with no patch' → mitigate with compensating controls or replace; document acceptance if neither is possible.

<a name="t-8-1-5"></a>
**SBOM**

Software bill of materials: list of all components and versions. Formats: SPDX, CycloneDX.

> On the exam: Lets you instantly answer 'are we affected by this new CVE?'. Often required in US government contracts.

<a name="t-8-1-6"></a>
**VEX**

States whether a known vulnerability in a component actually affects the product.

> On the exam: What it is: Vulnerability Exploitability eXchange, a statement saying whether a known vulnerability in a component actually affects your product (affected, not affected, fixed, under investigation).
Scenario cue: 'customers panic about a CVE in a library you include but never call' → publish a VEX saying 'not affected'.

<a name="t-8-1-7"></a>
**Transitive dependencies**

Dependencies of your dependencies; often where hidden risk lives.

> On the exam: What it is: indirect dependencies, the libraries your libraries use. Most open-source code in an app is transitive.
Scenario cue: 'vulnerable library not in our dependency list but in production' → it came in transitively; SCA must scan the full tree.

<a name="t-8-1-8"></a>
**Monitoring for changes and vulnerabilities**

Continuously watch components for new CVEs and updates.

> On the exam: What it means: components that were safe when shipped become vulnerable later, so keep watching CVE feeds against your SBOM and watch for ownership or maintainer changes.
Scenario cue: 'a popular package got a new maintainer who added malicious code' → monitor for changes, pin versions.

## 8.2 Third-party software security

<a name="t-8-2-1"></a>
**Certifications**

ISO 27001, SOC 2 (Type I = design at a point in time, Type II = effectiveness over a period), FedRAMP, Common Criteria, FIPS 140.

> On the exam: Type II is stronger evidence than Type I. Certifications show process quality, not bug-free software.

<a name="t-8-2-2"></a>
**Cloud Controls Matrix (CCM)**

Cloud Security Alliance's cloud control framework; CAIQ questionnaire, STAR registry.

> On the exam: What it is: the Cloud Security Alliance's framework of cloud security controls, mapped to other standards. CAIQ is its questionnaire; STAR is the public registry where providers publish assessments.
Scenario cue: 'standard way to assess a cloud provider's controls' → CSA CCM/CAIQ.

<a name="t-8-2-3"></a>
**Origin and support**

Who builds it, where, how it's maintained, and how long it's supported.

> On the exam: What it means: know who makes the software, where, who owns the company, how long it will be supported and how fast it fixes issues.
Scenario cue: 'critical library maintained by one anonymous volunteer' → origin and support risk.

<a name="t-8-2-4"></a>
**SSAE 18 and SOC reports**

SSAE 18 is the US auditing standard for service organization audits (ISAE 3402 is the international version). SOC 1: controls affecting customers' financial reporting. SOC 2: Trust Services Criteria: security, availability, processing integrity, confidentiality, privacy (detailed, restricted). SOC 3: public summary of SOC 2.

> On the exam: Type I: controls designed properly at a point in time. Type II: controls operated effectively over a period (usually 6-12 months), stronger evidence.
Scenario cue: 'assess a SaaS provider's security controls over time' → SOC 2 Type II.

## 8.3 Pedigree and provenance

<a name="t-8-3-1"></a>
**Pedigree vs provenance**

Pedigree = the component's history and lineage. Provenance = its origin and chain of custody.

> On the exam: Pedigree: the component's history: where it came from, what it's derived from, how it changed. Provenance: verifiable record of origin and chain of custody: who built it, from what source, how, and who handled it since.
Scenario cue: 'prove this binary was built from this exact source by our pipeline' → provenance (e.g., SLSA attestation).

<a name="t-8-3-2"></a>
**Secure transfer**

Chain of custody, authenticity and integrity when software moves between parties.

> On the exam: What it means: when software moves between parties, protect integrity and authenticity: encrypted channels, signed packages, hash verification, documented chain of custody.
Scenario cue: 'a downloaded installer's hash doesn't match the published hash' → don't install; it may be tampered.

<a name="t-8-3-3"></a>
**System interconnections**

Formal agreements (ISA, MOU) for connected systems.

> On the exam: What it means: connecting your systems with a supplier's requires formal agreements: ISA (Interconnection Security Agreement: technical security details) and MOU/MOA (responsibilities).
Scenario cue: 'a vendor's network connects to ours without documented controls' → need an ISA.

<a name="t-8-3-4"></a>
**Code repository security**

Access control, MFA, branch protection, signed commits.

> On the exam: Controls: MFA for all contributors, least-privilege access, protected branches, required code reviews, signed commits, secret scanning, audit logs.
Scenario cue: 'attacker with a stolen developer password pushed malicious code' → MFA and required reviews would stop it.

<a name="t-8-3-5"></a>
**Build environment security**

Isolated, hardened, hermetic builds; SLSA levels.

> On the exam: Controls: isolated, hardened, ephemeral build servers; no manual access; dependencies from trusted sources; signed outputs; provenance records. SLSA levels describe increasing build integrity.
Scenario cue: 'SolarWinds-style attack inserting code during build' → build environment security.

<a name="t-8-3-6"></a>
**Hashed and signed components**

Verify hashes and signatures before using components.

> On the exam: A hash proves integrity only if you got it from a trusted channel; a signature also proves origin.

<a name="t-8-3-7"></a>
**Right to audit**

Contract clause allowing you to audit the supplier.

> On the exam: What it is: a contract clause letting you (or an auditor you choose) inspect the supplier's security practices.
Rule: negotiate it before signing; it's very hard to add later.

<a name="t-8-3-8"></a>
**Export controls**

Laws restricting export of certain software and technology, especially strong cryptography: US EAR (Commerce Department) and ITAR (defense items); the Wassenaar Arrangement coordinates controls among many countries.

> On the exam: Scenario cue: 'shipping encryption software to another country' → check export control requirements before delivery.

<a name="t-8-3-9"></a>
**Authenticity and anti-counterfeiting**

Making sure software is genuine and from the real publisher: buy from authorized sources, verify code signatures, license checks, product registration, application allow-listing.

> On the exam: Scenario cue: 'cheap software from an unofficial reseller' → counterfeit risk; may contain malware.

<a name="t-8-3-10"></a>
**Supply chain goals**

Conformance (built to requirements and standards), trustworthiness (no vulnerabilities, accidental or malicious), authenticity (genuine, not counterfeit or pirated). Meeting all three gives predictable execution.

> On the exam: Scenario cue: 'software matches its spec but contains an implanted backdoor' → trustworthiness failed.

<a name="t-8-3-11"></a>
**Supply chain threats**

Product and data threats: tampering, malicious code insertion, counterfeiting, piracy, data theft. Process threats: bypassing legitimate channels, insecure code transfer, export violations, misconfiguration. People threats: malicious insiders, poorly trained staff.

> On the exam: Scenario cue: 'malicious code inserted into a vendor's update' → supply chain tampering.

<a name="t-8-3-12"></a>
**Termination access controls**

Remove developers' and suppliers' access to code, repositories and systems as soon as they leave or change roles, and when software is handed over to another party.

> On the exam: Why: disgruntled former staff can plant logic bombs or backdoors.
Scenario cue: 'a contractor whose contract ended still has repository access' → termination access control failure.

<a name="t-8-3-13"></a>
**Custom code extension checks**

When acquired software is customized or extended, the new code must go through threat modeling, code review, integration testing and secure storage with need-to-know access.

> On the exam: Scenario cue: 'secure COTS product, but an in-house plugin added SQL injection' → custom extensions weren't reviewed.

## 8.4 Supplier security in acquisition

<a name="t-8-4-1"></a>
**Auditing supplier compliance**

Verify suppliers follow secure development practices.

> On the exam: What it means: verify the supplier really follows secure development practices, through audits, evidence (SSDF attestation, test reports) or third-party reports, not just their claims.

<a name="t-8-4-2"></a>
**Vulnerability and incident notification**

Supplier must report, coordinate and respond to issues.

> On the exam: What it means: the contract requires the supplier to tell you about vulnerabilities and incidents within set timeframes, coordinate fixes and disclosure, and report progress.
Scenario cue: 'you learned about the vendor's breach from the news' → missing notification clause.

<a name="t-8-4-3"></a>
**Maintenance and support**

Community vs commercial support; licensing terms.

> On the exam: What it means: how the product will be maintained: patch frequency, support hours, response times, end-of-life notice. Community open source has no guaranteed support; commercial support is contractual.
Scenario cue: 'critical system relies on an open-source tool with no support contract' → consider commercial support or internal ownership.

<a name="t-8-4-4"></a>
**Security track record**

Past vulnerabilities and how quickly they were handled.

> On the exam: What it means: check the supplier's history: past breaches, number and severity of vulnerabilities, how quickly and openly they fixed them.

<a name="t-8-4-5"></a>
**Scope of testing**

Who tests what under the shared responsibility model.

> On the exam: What it means: agree who tests what. In the cloud's shared responsibility model, the provider tests its infrastructure; you test your apps and configurations. Get permission before pentesting a provider.
Scenario cue: 'can we pentest our SaaS provider?' → only within their rules and contract.

<a name="t-8-4-6"></a>
**SIEM log integration**

Supplier's product must send usable logs to your SIEM.

> On the exam: What it means: the supplier's product must produce logs you can send to your SIEM, in a usable format.
Scenario cue: 'a SaaS app gives no access to audit logs' → monitoring blind spot; require log access in the contract.

<a name="t-8-4-7"></a>
**Acquisition phases**

Planning, contracting, monitoring and acceptance, follow-on.

> On the exam: Phases: 1) Planning: define needs and security requirements, assess risk. 2) Contracting: put security requirements in the RFP and contract, evaluate bidders. 3) Monitoring and acceptance: verify delivery meets requirements, acceptance testing. 4) Follow-on: maintenance, support, patches, and finally retirement.
Scenario cue: 'when should security requirements be defined in buying software?' → planning, before vendors are asked to bid.

<a name="t-8-4-8"></a>
**Make, buy or outsource**

Make: build in-house (full control, higher cost). Buy: commercial off-the-shelf software (COTS) (faster, less control, vendor dependency). Outsource: a third party builds or runs it.

> On the exam: Security angle: buying or outsourcing transfers the work, never the accountability. Requirements must be in contracts.

<a name="t-8-4-9"></a>
**Outsourcing risks and controls**

Risks: less visibility, IP loss, insecure coding, foreign jurisdiction, subcontractors, insider threats at the vendor.

> On the exam: Controls: security requirements and SLAs in the contract, right to audit, code reviews and testing of delivered code, code escrow, background checks, NDAs, limit access to data.
Scenario cue: 'offshore team builds the app' → verify code independently before acceptance.

<a name="t-8-4-10"></a>
**CAPEX vs OPEX**

CAPEX (capital expenditure): up-front purchase of long-term assets (servers, perpetual licenses). OPEX (operational expenditure): ongoing costs (subscriptions, cloud, support, staff).

> On the exam: Scenario cue: 'moving from on-premises servers to the cloud' → shifts cost from CAPEX to OPEX.

<a name="t-8-4-11"></a>
**ROI, ROSI and TCO**

ROI: (gain − cost) / cost. ROSI: return on security investment = (risk reduction (ALE saved) − cost of control) / cost of control. TCO: total cost of ownership over the whole life: purchase, implementation, training, maintenance, support, retirement.

> On the exam: Scenario cue: 'justify a security tool to management' → show ROSI in business terms.
Trap: compare options by TCO, not purchase price.

<a name="t-8-4-12"></a>
**COTS security considerations**

Commercial off-the-shelf software: you usually can't see or change the code.

> On the exam: Controls: vendor assessment, certifications (Common Criteria), SOC reports, pentests of the deployed product, secure configuration, patch SLAs, escrow, and isolating it if risk is high.

<a name="t-8-4-13"></a>
**Supplier pre-qualification**

Assess a supplier before choosing them: organization (financial history, conflicts of interest, foreign ownership/control/influence (FOCI), compliance, SLAs, past performance), people (security skills and training), processes (secure development lifecycle, vulnerability and patch track record).

> On the exam: Scenario cue: 'a foreign government has influence over the vendor' → FOCI risk.

<a name="t-8-4-14"></a>
**Acquisition models**

Direct purchase, OEM licensing (software bundled with hardware), partnering/alliances, outsourcing (including offshoring), and managed services.

> On the exam: Security: each model shifts work, never accountability. Offshoring adds jurisdiction and export issues.

<a name="t-8-4-15"></a>
**Supplier claims verification**

Never just trust supplier claims: check vulnerability history, verify features by testing (black-box testing if no source), use independent third parties. Get vendor permission before testing software you don't own.

> On the exam: Trap: reverse engineering vendor code without permission can break the license and the law.

<a name="t-8-4-16"></a>
**COTS, GOTS and MOTS**

COTS: commercial off-the-shelf. GOTS: government off-the-shelf (built for government). MOTS: modified off-the-shelf (COTS customized for you).

> On the exam: Security: modifications need the same reviews as custom code and may void vendor support.

<a name="t-8-4-17"></a>
**Managed services and SLAs**

Moving operations to a provider (managed security, hosting). SLAs define measurable service levels and penalties.

> On the exam: Scenario cue: 'provider repeatedly misses response times' → enforce SLA penalties; SLAs need measurable metrics.

## 8.5 Contractual requirements

<a name="t-8-5-1"></a>
**Intellectual property ownership**

Who owns custom code and derivatives.

> On the exam: What it means: the contract must state who owns custom code, modifications and derived work. Without it, the developer or vendor may own it.
Scenario cue: 'after an outsourced project, the vendor claims ownership of the code' → missing IP clause.

<a name="t-8-5-2"></a>
**Code escrow**

Source code held by a third party, released if the vendor fails or stops support.

> On the exam: What it is: the vendor's source code is held by a neutral third party and released to you if the vendor goes bankrupt, stops supporting the product or breaches the contract.
Scenario cue: 'critical app from a small vendor that might go out of business' → code escrow.

<a name="t-8-5-3"></a>
**Liability and indemnification**

Who pays when something goes wrong.

> On the exam: Liability: who pays when something goes wrong, and limits on it. Indemnification: one party protects the other from certain claims (e.g., IP infringement).
Scenario cue: 'vendor caps liability at the license fee' → limits how much risk you actually transfer.

<a name="t-8-5-4"></a>
**Warranty**

Vendor guarantees about quality or fitness.

> On the exam: What it is: the vendor's promise about quality or performance for a period. Many software licenses disclaim warranties ('as is'), especially open source.

<a name="t-8-5-5"></a>
**EULA**

End-user license agreement: usage terms and restrictions.

> On the exam: What it is: the End-User License Agreement, the terms for using the software: allowed use, number of users, no reverse engineering, no transfer, liability limits.
Scenario cue: 'a security team wants to reverse engineer vendor software to check it' → may be forbidden by the EULA; get permission.

<a name="t-8-5-6"></a>
**SLA and NDA**

Service commitments; confidentiality obligations.

> On the exam: An SLA carries remedies or penalties; an NDA protects confidential information shared with the vendor.

<a name="t-8-5-7"></a>
**Software licensing models**

Perpetual (buy once), subscription (pay periodically), per user or per device, concurrent users, site license, open source (permissive or copyleft).

> On the exam: Compliance: track licenses (software asset management); unlicensed or over-deployed software causes legal and financial penalties.
Scenario cue: 'audit shows more installations than licenses' → license compliance violation.

<a name="t-8-5-8"></a>
**Maintenance and support agreements**

Contract terms covering updates, patches, bug fixes, support hours, response times, and how long the product will be supported.

> On the exam: Scenario cue: 'vendor takes months to patch a critical flaw' → contract lacked patch timelines and penalties.

<a name="t-8-5-9"></a>
**Types of intellectual property**

Copyright (protects code as expression, automatic), patent (protects a novel invention, must be filed, time-limited), trademark (brand names and logos), trade secret (protected by keeping it secret, e.g., NDAs; lost once disclosed).

> On the exam: Scenario cue: 'protect a proprietary algorithm without public disclosure' → trade secret. 'Protect the product name' → trademark.

<a name="t-8-5-10"></a>
**Open source licenses**

Permissive (MIT, BSD, Apache: few obligations, Apache includes a patent grant), weak copyleft (LGPL: share changes to the library only), strong copyleft (GPL: distributed derivative works must be open source; AGPL also covers network use). Also freeware, shareware, Creative Commons for content.

> On the exam: Scenario cue: 'commercial product links a GPL library and is distributed' → may have to release its source; legal review needed.

## 8.AI AI additions in the current outline

<a name="t-8-ai-1"></a>
**AI-BOM**

AI bill of materials: model weights, training datasets, ML libraries.

> On the exam: What it is: an AI bill of materials listing models, versions, weights, training datasets, fine-tuning data and ML libraries.
Scenario cue: 'a popular dataset was found to be poisoned; are we affected?' → an AI-BOM answers it quickly.

<a name="t-8-ai-2"></a>
**Model poisoning and backdoors**

Malicious behavior hidden in pre-trained models.

> On the exam: What it is: malicious behavior hidden in a model, triggered by a specific input (backdoor), or introduced through poisoned training data.
Defense: get models from trusted sources, verify hashes and signatures, scan model files (some formats like pickle can run code when loaded), test behavior.

<a name="t-8-ai-3"></a>
**Selecting open-source models**

Security and bias criteria before adopting a model.

> On the exam: Criteria: trusted source and provenance, license terms, documentation (model cards), known bias and safety evaluations, maintenance, safe file format.
