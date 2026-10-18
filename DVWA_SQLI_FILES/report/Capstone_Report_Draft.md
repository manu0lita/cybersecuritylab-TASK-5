# Web Application Penetration Testing and Incident Response Using DVWA

**Capstone report - draft template**  
**Author:** [FILL IN]  
**Institution / internship:** [FILL IN]  
**Assessment date:** [FILL IN]  
**Target:** DVWA local lab at [VERIFIED URL]  
**Report status:** Draft; actual test evidence still required

> **Important integrity note:** This report is a starter template. Do not submit it unchanged. Replace bracketed fields and attach your own request/response screenshots, terminal output, and logs. No SQL injection result is asserted until your lab test confirms it.

## Executive Summary
This project uses the Damn Vulnerable Web Application (DVWA), an intentionally vulnerable web application, to practice a controlled SQL injection assessment and a basic incident-response simulation. The testing scope is limited to the project owner's local DVWA environment. The planned assessment records baseline behavior, evaluates a controlled input-validation test, compares Boolean-condition responses, reviews local web logs, and recommends parameterized queries and defensive monitoring.

**Actual result:** [FILL IN after testing: confirmed / not confirmed / inconclusive].  
**Primary finding:** SQL injection in [parameter/module - fill in only if validated].  
**Evidence:** [E02-E05 filenames].  
**Key remediation:** Parameterized queries/prepared statements, least-privilege database account, safe error handling, and regression tests.

## 1. Objectives and Scope
### Objectives
- Apply a repeatable methodology to one SQL injection test case.
- Preserve actual evidence and distinguish facts from interpretation.
- Explain potential impact and recommend mitigations.
- Detect a simulated SQLi-like request in local web logs and document the response lifecycle.

### In scope
- DVWA running in the user's own local/isolated environment.
- The DVWA SQL Injection module, initially at Low security for the controlled demonstration.
- Locally generated access logs and the offline pattern detector in this repository.

### Out of scope
- Any public website or third-party target.
- Destructive queries, data modification, credential/hash dumping, persistence, denial of service, and testing unrelated services.

## 2. Environment and Architecture
**Host / VM:** [FILL IN]  
**OS/version:** [FILL IN]  
**DVWA version/image:** [FILL IN]  
**Local target URL:** [VERIFY]  
**Bound interface/port:** [FILL IN]  
**Database:** [FILL IN if known]  
**Tools:** Kali Linux, Firefox, DVWA, optional Burp Suite Community, Docker Compose/logs, Python 3, Git.

Add `../diagrams/network_diagram.png` to the submitted report or recreate it using `../diagrams/network_diagram.mmd`. Attach your verified environment output as E01.

## 3. Methodology
1. Confirm target ownership, local URL, security level, and network isolation.
2. Verify only the local DVWA endpoint using `curl -I --max-time 5 http://127.0.0.1:4280` and `nmap -sT -sV -p 4280 127.0.0.1`; save the actual output.
3. Record normal baseline behavior with input `1`.
4. Make one controlled syntax probe with `1'` and capture the actual response.
5. Compare Boolean conditions (`1' OR '1'='1` and `1' AND '1'='2`) in the DVWA field.
6. Stop after the limited demonstration; do not dump hashes or modify data.
7. Review logs around the exact test time. Run the offline detector and manually validate flags.
8. Recommend mitigation and document retest status honestly.

Reference methodology: OWASP Web Security Testing Guide. See References.

## 4. Findings
### F-01: SQL injection test in DVWA SQL Injection module
- **Status:** [CONFIRMED / NOT CONFIRMED / INCONCLUSIVE]
- **Severity:** [PROVISIONAL rating and rationale - don't guess]
- **Affected module/parameter:** [FILL IN]
- **Evidence IDs:** [E02, E03, E04]
- **Prerequisites/security level:** [FILL IN]

**Observation:** [Write exactly what the application returned for baseline, quote test, true condition, and false condition.]

**Technical explanation:** SQL injection can occur when an application concatenates user-controlled input into SQL syntax rather than binding it as data. A successful issue may permit unauthorized records to be read or changed, depending on the query and database privileges. Do not claim impacts that were not demonstrated or supported by the application design.

**Impact assessment:** [State only the impact supported by the observed result. Separate demonstrated impact from possible worst-case impact.]

**Reproduction summary:** In the locally scoped DVWA SQL Injection module at Low security, submit baseline input `1`, then the controlled quote probe `1'`, then compare the responses to `1' OR '1'='1` and `1' AND '1'='2`. Store screenshots and relevant HTTP requests/responses, redacting cookies and tokens.

**Mitigation:** Use parameterized queries/prepared statements. Apply allow-list validation when the input is expected to be a known identifier. Use a database account with only necessary permissions, prevent verbose SQL errors from reaching users, log suspicious failures, and add regression tests.

**Retest:** [FILL IN; if you did not change the application source and verify a fix, write “Not performed; mitigation recommended.”]

## 5. Incident Detection and Response Simulation
- **Incident ID:** IR-01
- **Scenario:** Controlled SQLi-like request to local DVWA.
- **Detection source:** [REAL access log / container output / clearly labelled synthetic sample]
- **Detection timestamp:** [FILL IN]
- **Indicator found:** [FILL IN]
- **Detection output:** [ATTACH screenshot/output]

### Response timeline
| Phase | Action | Evidence/status |
|---|---|---|
| Detect | Flag a suspicious request pattern in the local log | [FILL IN] |
| Triage | Correlate with the controlled browser test time and source | [FILL IN] |
| Contain | Restrict local access or stop the DVWA container after preserving evidence | [FILL IN] |
| Eradicate | Recommend or apply parameterized-query remediation; do not claim a fix unless applied | [FILL IN] |
| Recover | Restart/verify service and perform safe retest if a fix was applied | [FILL IN] |
| Lessons learned | Logging, least privilege, prepared statements, generic errors, regression tests | [FILL IN] |

The bundled `scripts/sample_access.log` is synthetic and must never be represented as captured target traffic.

## 6. Limitations
- DVWA is a deliberately vulnerable training target, not a production system.
- The project focuses on one vulnerability class due to time constraints.
- The included log detector uses simple string patterns and can produce false positives and false negatives; it is not a SIEM or a substitute for manual investigation.
- Findings are limited to behavior actually observed in the test environment.

## 7. Conclusion
[Summarize the actual test result, whether the behavior supported the finding, how evidence was preserved, and which mitigation or retest was completed. Avoid claiming a confirmed finding or successful remediation without supporting evidence.]

## References
1. OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
2. OWASP SQL Injection testing page: https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Injection/05-SQL_Injection/
3. OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
4. Official DVWA repository: https://github.com/digininja/DVWA
5. Tutorial used for background (bWAPP, not DVWA): https://www.youtube.com/watch?v=ZaLWQ89b5f8

## Appendix A: Evidence Index
Use `../evidence/EVIDENCE_REGISTER.csv` and add the exact file paths and notes. Include actual screenshots for E01-E06. The supplied initial DVWA homepage screenshot is not proof that SQL injection was tested.
