# 1. Project Plan

## Project title
**Web Application Penetration Testing and Incident Response Using DVWA**

## Objective
Assess a deliberately vulnerable local web application for SQL injection, demonstrate impact using limited dummy data, document supporting evidence, recommend mitigations, and simulate detection and response using application/web-server logs.

## Scope and authorization
- In scope: the DVWA instance running on the user's own Kali VM at `http://127.0.0.1:4280` (confirm actual URL before testing).
- Out of scope: public websites, unrelated devices, other VMs/services, denial-of-service, persistence, destructive database actions, and real credential collection.
- Environment: isolated local lab; retain loopback-only binding where possible.
- Data: DVWA sample data only. Do not access/export password hashes or secrets for this project.

## Success criteria
1. Record a normal baseline request and response.
2. Test the SQL Injection module at Low security using a harmless input and a controlled boolean test.
3. Capture actual request/response evidence and explain what it proves (and does not prove).
4. Document a reproducible finding with impact, severity rationale, and remediation.
5. Run the local log detector against actual access logs if available; otherwise label any sample log as synthetic and do not claim it came from the target.
6. Complete an incident timeline covering detection, containment, eradication/remediation, recovery, and lessons learned.
7. Submit a report PDF, GitHub repository, and 12-minute demonstration video.

## Tools
- Kali Linux, Firefox, DVWA
- Burp Suite Community (optional, for viewing the HTTP request; don't change payloads outside the lab)
- Docker Compose (if DVWA uses the official container setup)
- `curl`, `ip`, `ss`, and Docker CLI for environment verification
- Python 3 for offline log inspection
- Git/GitHub for versioned notes and scripts

## Time-boxed timeline (adjust to the deadline)
| Time box | Task | Output |
|---|---|---|
| 20 min | Verify DVWA and set scope | E01, environment notes |
| 35 min | Baseline + controlled SQLi test | E02-E04 |
| 20 min | Export/review logs and run detector | E05, detection notes |
| 25 min | Remediation research and retest plan | mitigation section |
| 40 min | Fill report and evidence register | report draft |
| 20 min | Record/rehearse final presentation | 12-minute video |

## Risk statement
DVWA is intentionally vulnerable. Run it only in a local or isolated lab, do not bind it to all interfaces or expose it to the Internet, and stop the test if the target differs from the defined scope.
