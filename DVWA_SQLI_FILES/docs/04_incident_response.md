# 4. Incident Response Simulation Worksheet

## Scenario
A test request against the local DVWA SQL Injection module contains SQL metacharacters and a boolean condition. The objective is to detect the request in a web log and rehearse a basic incident-response workflow. This is a controlled tabletop/simulation, not evidence of a real-world compromise.

## Detection source
Preferred: the actual DVWA container's Apache access log. If unavailable, use the synthetic `scripts/sample_access.log` only to demonstrate the detector and explicitly label the result **synthetic**.

### Find the real container and inspect logs
From the directory containing DVWA's `compose.yml`:

```bash
docker compose ps
docker compose logs --tail=100 dvwa
```

If `docker compose logs` doesn't contain request details, find the web container name with `docker ps` and inspect the Apache access log path configured in that image. Do not assume every image stores logs in the same location.

To save only an appropriate local excerpt, use a file you can review and redact:

```bash
# Example only: replace the container name and path with the real values.
docker logs --since 15m <dvwa-container> > ../dvwa-container.log 2>&1
```

`docker logs` captures container stdout/stderr; it might not contain Apache access logs if the container writes them to files. Document what source you actually used.

## Run the offline detector
```bash
python3 scripts/detect_sqli_logs.py scripts/sample_access.log
```

The bundled sample log is synthetic and is just a sanity test for the script. To analyze a real log, first copy a reviewed/redacted local access log to `evidence/actual_access.log` and run:

```bash
python3 scripts/detect_sqli_logs.py evidence/actual_access.log
```

## Record the incident lifecycle
1. **Detect:** record timestamp, source log, request path, client address as recorded in the lab, and why the request is suspicious.
2. **Triage:** correlate the log entry with your controlled test timestamp and browser evidence. Distinguish your own test activity from an unknown actor.
3. **Contain:** in a real environment, restrict access to the affected app or place it in maintenance; for this local lab, stopping the DVWA container is an acceptable simulated containment demonstration.
4. **Eradicate/remediate:** for the project, document the actual code-level fix required: parameterized queries / prepared statements. Do not claim to have patched DVWA's vulnerable source unless you truly did so.
5. **Recover:** restart the app after lab changes and perform the safe retest. For the local vulnerable training image, the practical containment is to stop it when not testing; remediation should be demonstrated in a safe sample or documented when source modification isn't part of the exercise.
6. **Lessons learned:** recommend least-privilege database access, nonverbose error messages, centralized logging, alerting, and a repeatable regression test.

## Post-incident record
- Incident ID: `IR-01`
- Classification: `Simulated web attack - SQL injection probe`
- Start/end time: `[FILL IN]`
- Detection method and log source: `[FILL IN]`
- Relevant evidence IDs: `[FILL IN]`
- Containment action performed: `[FILL IN]`
- Remediation recommendation: `[FILL IN]`
- Verification/retest result: `[FILL IN]`
- Residual limitations: `[FILL IN]`
