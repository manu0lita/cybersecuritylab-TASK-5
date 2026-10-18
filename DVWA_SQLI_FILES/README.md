# DVWA SQL Injection Capstone - Starter Kit

> **Status:** Starter kit/template. Replace every `[FILL IN]` marker and add your own screenshots and actual outputs before final submission. This repository deliberately does not invent test results.

## Project
**Web Application Penetration Testing and Incident Response Using DVWA**

A time-efficient capstone focused on a controlled SQL injection demonstration against your own local DVWA instance, defensible mitigation recommendations, and a small incident-detection exercise using web logs.

## Safety and scope
- Authorized target: DVWA running on your own Kali VM, ideally bound to `127.0.0.1:4280`.
- Do not scan or test any public website or any system you do not own or have explicit permission to assess.
- Use DVWA's intentionally vulnerable training module only.
- Keep evidence free of real personal data, secrets, credentials, and unrelated host information.
- Do not publish the full raw log if it contains sensitive data; redact first.

## Fast path
1. Read `docs/01_project_plan.md`.
2. Verify/start DVWA using `docs/02_environment_setup.md`.
3. Follow `docs/03_sqli_lab_checklist.md` and capture the evidence as you go.
4. Use `scripts/detect_sqli_logs.py` to scan a local Apache access-log export for suspicious request indicators. The script reads files only; it sends no traffic.
5. Fill in `docs/04_incident_response.md` with the actual event, detection, containment, and verification steps.
6. Use `report/Capstone_Report_Draft.md` and `report/Capstone_Report.pdf` as templates.
7. Rehearse `docs/05_12_minute_video_script.md` while recording the actual lab, not only slides.

## Official DVWA setup (if your existing instance is not running)
The official project provides its own Docker Compose configuration and maps the app to `127.0.0.1:4280` by default. From a Kali terminal with internet access:

```bash
git clone https://github.com/digininja/DVWA.git
cd DVWA
docker compose up -d
docker compose ps
curl -I --max-time 5 http://127.0.0.1:4280
```

Open `http://127.0.0.1:4280`. Follow the app's database setup page if prompted. The normal DVWA login is `admin` / `password` unless changed. Never change the published port binding to all interfaces for convenience; keep the intentionally vulnerable app local.

If the folder already exists, `cd` into that existing `DVWA` directory rather than cloning over it.

## Evidence naming
Use filenames like `E01_dvwa_home.png`, `E02_sqli_baseline.png`, `E03_sqli_quote_test.png`, `E04_sqli_boolean_test.png`, `E05_access_log_detection.png`, `E06_remediation_retest.png`. Save screenshots in `evidence/`. The screenshots currently included in this kit are not populated; add your own.

## Contents
- `docs/`: scope, environment, SQLi test checklist, incident response, timed talk track.
- `diagrams/network_diagram.mmd`: editable Mermaid network diagram.
- `diagrams/network_diagram.png`: rendered diagram for report/presentation.
- `scripts/detect_sqli_logs.py`: offline access-log indicator scanner.
- `scripts/sample_access.log`: clearly marked synthetic sample log for testing the detector only, not real evidence.
- `report/Capstone_Report_Draft.md`: editable report content.
- `report/Capstone_Report.pdf`: formatted report template with evidence placeholders.
- `evidence/EVIDENCE_REGISTER.csv`: evidence tracker.

## References
- DVWA official repository and compose file: https://github.com/digininja/DVWA
- OWASP Web Security Testing Guide - SQL Injection: https://owasp.org/www-project-web-security-testing-guide/
- OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
