# Review list

Terms I marked as shaky (52). Go through these before each practice test.

## Domain 2, 2.6 Decommission applications

- **[Data destruction (NIST SP 800-88)](domains/02-secure-software-lifecycle-management.md#t-2-6-7)**: Clear (overwrite), purge (degauss, crypto-erase), destroy (shred, incinerate).

## Domain 2, 2.8 Integrated risk management

- **[ISO/IEC 15408 (Common Criteria)](domains/02-secure-software-lifecycle-management.md#t-2-8-3)**: Product security evaluation; EAL1-7 assurance levels, protection profiles.
- **[PCI DSS and PCI Secure Software Standard](domains/02-secure-software-lifecycle-management.md#t-2-8-4)**: Requirements for systems and software handling payment card data.
- **[NIST SP 800-37 (RMF)](domains/02-secure-software-lifecycle-management.md#t-2-8-6)**: Categorize, select, implement, assess, authorize, monitor.
- **[NIST SP 800-30](domains/02-secure-software-lifecycle-management.md#t-2-8-7)**: Guide for conducting risk assessments.
- **[SLE, ARO, ALE](domains/02-secure-software-lifecycle-management.md#t-2-8-18)**: SLE = asset value x exposure factor. ALE = SLE x ARO (annual rate of occurrence).
- **[Risk responses](domains/02-secure-software-lifecycle-management.md#t-2-8-19)**: Mitigate, accept, transfer (insurance, contract), avoid.
- **[CMMI](domains/02-secure-software-lifecycle-management.md#t-2-8-23)**: Capability Maturity Model Integration (from SEI). Five levels: 1 Initial (chaotic), 2 Managed (project-level), 3 Defined (organization-wide standard), 4 Quantitatively Managed (measured), 5 Optimizing (continuous improvement).
- **[Countermeasure cost-benefit](domains/02-secure-software-lifecycle-management.md#t-2-8-25)**: Value of a control = ALE before − ALE after − annual cost of the control.
- **[FIPS standards to recognize](domains/02-secure-software-lifecycle-management.md#t-2-8-28)**: US Federal Information Processing Standards: FIPS 140-2/140-3 (crypto module validation, Levels 1-4), FIPS 197 (AES), FIPS 180 (SHA hashes), FIPS 186 (digital signatures), FIPS 199 (security categorization), FIPS 200 (minimum security requirements), FIPS 201 (PIV smart cards).
- **[Other NIST SPs to recognize](domains/02-secure-software-lifecycle-management.md#t-2-8-29)**: 800-12 (security handbook), 800-34 (contingency planning), 800-41 (firewalls), 800-61 (incident handling), 800-63 (digital identity and authentication), 800-64 (security in the SDLC, withdrawn), 800-88 (media sanitization), 800-92 (log management), 800-95 (web services security), 800-115 (security testing), 800-160 (systems security engineering).
- **[ISO standards to recognize](domains/02-secure-software-lifecycle-management.md#t-2-8-30)**: ISO/IEC 9126 and its successor 25010 (software quality models, SQuaRE series), 12207 (software lifecycle processes), 15288 (system lifecycle processes), 15408 (Common Criteria), 21827 (SSE-CMM, security engineering maturity), 27000 series (security management).
- **[PA-DSS and PCI Secure Software Standard](domains/02-secure-software-lifecycle-management.md#t-2-8-31)**: PA-DSS was the PCI standard for payment application vendors; it was retired and replaced by the PCI Secure Software Standard and Secure SLC Standard.

## Domain 3, 3.6 Misuse and abuse cases

- **[Misuse case](domains/03-secure-software-requirements.md#t-3-6-1)**: How an actor could misuse the system, intentionally or by accident.
- **[Mitigating control identification](domains/03-secure-software-requirements.md#t-3-6-3)**: Each misuse case leads to a security requirement or control.

## Domain 4, 4.1 Security architecture

- **[Industrial IoT / OT](domains/04-secure-software-architecture-and-design.md#t-4-1-24)**: ICS, SCADA, PLCs, automotive, robotics, medical devices; safety and availability come first.

## Domain 4, 4.2 Secure interface design

- **[API design](domains/04-secure-software-architecture-and-design.md#t-4-2-5)**: Authentication, authorization per call, rate limiting, input validation, versioning.

## Domain 4, 4.3 Reusable technologies

- **[Firewalls](domains/04-secure-software-architecture-and-design.md#t-4-3-3)**: Packet filter, stateful, application-level, web application firewall (WAF).
- **[Data loss prevention (DLP)](domains/04-secure-software-architecture-and-design.md#t-4-3-4)**: Detects and blocks sensitive data leaving, at rest, in motion, in use.
- **[Infrastructure as code (IaC)](domains/04-secure-software-architecture-and-design.md#t-4-3-7)**: Infrastructure in templates; scan for misconfigurations, prevent drift.
- **[Trusted Platform Module (TPM)](domains/04-secure-software-architecture-and-design.md#t-4-3-8)**: Chip for key storage, measured boot, sealed storage.
- **[Trusted Computing Base (TCB)](domains/04-secure-software-architecture-and-design.md#t-4-3-9)**: All hardware, firmware and software enforcing the security policy.
- **[Polyinstantiation](domains/04-secure-software-architecture-and-design.md#t-4-3-13)**: Different versions of a record at different classification levels to stop inference.
- **[Digital certificates in detail](domains/04-secure-software-architecture-and-design.md#t-4-3-19)**: An X.509 certificate binds a public key to an identity, signed by a CA. Contains subject, issuer, public key, validity dates, serial number, extensions.
- **[Trusted computing concepts together](domains/04-secure-software-architecture-and-design.md#t-4-3-24)**: Ring protection (privilege levels), trust boundary/security perimeter (where trust changes), TCB (everything enforcing the policy), reference monitor (concept that mediates all access), security kernel (its implementation).
- **[Security-oriented operating systems](domains/04-secure-software-architecture-and-design.md#t-4-3-26)**: Operating systems with built-in mandatory access control and hardening, such as SELinux, AppArmor or trusted OS variants.

## Domain 4, 4.6 Security properties and constraints

- **[Non-functional trade-offs](domains/04-secure-software-architecture-and-design.md#t-4-6-1)**: E.g., encryption vs performance, logging vs privacy.
- **[Biba](domains/04-secure-software-architecture-and-design.md#t-4-6-3)**: Integrity model: no read down, no write up.
- **[State machine, information flow, noninterference, lattice](domains/04-secure-software-architecture-and-design.md#t-4-6-7)**: State machine: system is secure if it starts secure and every transition keeps it secure. Information flow: controls how data moves between levels. Noninterference: actions at a high level can't be observed by low levels (stops covert channels). Lattice: defines upper and lower bounds of access between levels.

## Domain 4, 4.7 Secure operational architecture

- **[CI/CD architecture](domains/04-secure-software-architecture-and-design.md#t-4-7-3)**: Separate environments, protected pipeline, least-privilege deployment.

## Domain 5, 5.1 Secure coding practices

- **[Algorithm selection](domains/05-secure-software-implementation.md#t-5-1-22)**: Use AES-GCM, SHA-256+, RSA 2048+/ECC. Avoid DES, RC4, MD5, SHA-1, ECB mode.
- **[Spoofing](domains/05-secure-software-implementation.md#t-5-1-45)**: Pretending to be another user, system or source (IP, email, DNS, caller ID).

## Domain 5, 5.2 Analyze code for security risks

- **[SAST](domains/05-secure-software-implementation.md#t-5-2-5)**: Static analysis of source or binaries without running it. White-box, early, fast, but more false positives.
- **[Manual code review](domains/05-secure-software-implementation.md#t-5-2-7)**: Finds business logic and design flaws tools miss; peer review.

## Domain 5, 5.3 Implement security controls

- **[Anti-malware](domains/05-secure-software-implementation.md#t-5-3-3)**: Signature- and behavior-based detection.

## Domain 5, 5.5 Evaluate and integrate components

- **[Software composition analysis (SCA)](domains/05-secure-software-implementation.md#t-5-5-3)**: Inventories third-party and open source components; flags known vulnerabilities and license issues.
- **[Dependency confusion / typosquatting](domains/05-secure-software-implementation.md#t-5-5-4)**: Attackers publish lookalike or same-named packages to get them installed.

## Domain 5, 5.AI AI additions in the current outline

- **[Constraining AI agents](domains/05-secure-software-implementation.md#t-5-ai-4)**: Declarative boundaries limiting what autonomous agents can do.

## Domain 6, 6.1 Security testing strategy and plan

- **[OWASP WSTG and ASVS](domains/06-secure-software-testing.md#t-6-1-5)**: Web testing guide; verification standard with levels 1-3.
- **[Known environment (white-box)](domains/06-secure-software-testing.md#t-6-1-8)**: Tester has full knowledge of code and design.
- **[Vulnerability disclosure program](domains/06-secure-software-testing.md#t-6-1-16)**: Public process to report flaws, with coordinated disclosure and safe harbor.

## Domain 6, 6.2 Security test cases

- **[Generation-based fuzzing](domains/06-secure-software-testing.md#t-6-2-8)**: Builds inputs from a specification or grammar; smarter, needs more setup.
- **[Fault injection](domains/06-secure-software-testing.md#t-6-2-12)**: Deliberately introducing errors to see whether the system fails securely.
- **[Boundary value and equivalence testing](domains/06-secure-software-testing.md#t-6-2-22)**: Test at the edges of input ranges and one value per input class.

## Domain 6, 6.4 Undocumented functionality

- **[Undocumented features](domains/06-secure-software-testing.md#t-6-4-1)**: Backdoors, debug code, hidden admin functions, maintenance hooks, Easter eggs.
- **[Finding them](domains/06-secure-software-testing.md#t-6-4-2)**: Code review, binary analysis, comparing behavior to the requirements matrix.

## Domain 6, 6.AI AI additions in the current outline

- **[Agent scope testing](domains/06-secure-software-testing.md#t-6-ai-4)**: Verify AI agents can't run commands outside their allowed scope.
- **[Token limit stress testing](domains/06-secure-software-testing.md#t-6-ai-5)**: Check behavior when inputs hit or exceed model limits.
- **[NIST AI RMF](domains/06-secure-software-testing.md#t-6-ai-6)**: AI Risk Management Framework: Govern, Map, Measure, Manage.

## Domain 7, 7.1 Operational risk analysis

- **[System integration risk](domains/07-secure-software-deployment-operations-maintenance.md#t-7-1-4)**: New software changes the risk of connected systems.
- **[Implementation and cutover (changeover) strategies](domains/07-secure-software-deployment-operations-maintenance.md#t-7-1-5)**: Ways to move from an old system to a new one: direct/big bang (switch at once), parallel (run both together), phased (module by module), pilot (one group or site first).

## Domain 7, 7.2 Configuration and version control

- **[Configuration management database (CMDB)](domains/07-secure-software-deployment-operations-maintenance.md#t-7-2-4)**: Record of configuration items and relationships.
