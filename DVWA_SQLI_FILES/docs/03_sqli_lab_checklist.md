# 3. Controlled SQL Injection Lab Checklist (DVWA)

This checklist is written for the **SQL Injection** module in your own DVWA instance. The supplied video transcript describes bWAPP's **search** parameter; DVWA's SQLi module is commonly a **User ID** input, so do not copy bWAPP's parameter names or column-count assumptions blindly.

## Before testing
- [ ] Target URL confirmed as local DVWA (`127.0.0.1` or another explicitly isolated address).
- [ ] Run a narrow, local-only verification scan and save the output:

```bash
curl -I --max-time 5 http://127.0.0.1:4280
nmap -sT -sV -p 4280 127.0.0.1
```

This checks only the local port assigned to the authorized DVWA lab; do not change the target to a public address or scan a broader network for this capstone.
- [ ] DVWA Security set to **Low** for this first demonstration.
- [ ] No public target or real data is in scope.
- [ ] Screenshot `E01_dvwa_home.png` captured.

## Test sequence
1. Open **SQL Injection** from DVWA's left menu.
2. **Baseline:** enter `1` and submit. Note the displayed record(s), response, and request URL. Capture `E02_sqli_baseline.png`.
3. **Syntax-error probe:** enter `1'` and submit. Record whether the page exposes a SQL error, returns a generic message, or behaves normally. Capture `E03_sqli_quote_test.png`. A SQL error is useful evidence, but an error alone does not prove full exploitability.
4. **Boolean test:** enter `1' OR '1'='1` and submit. Compare the number/content of returned records with the baseline. Capture `E04_sqli_boolean_test.png`.
5. **False-condition control:** enter `1' AND '1'='2` and submit. Compare against the true condition. Record exactly what the application returns; do not assume the outcome.
6. If using Burp, capture only the relevant local request and response; redact cookies/session IDs before publishing.
7. Stop after demonstrating the effect. Do not dump password hashes, enumerate unrelated schema, modify records, or run destructive payloads.

## Interpret results carefully
- If the true and false conditions produce meaningfully different results, that differential can support the SQLi finding.
- If the app shows an error, preserve the exact sanitized evidence.
- If the inputs are rejected or the outcomes do not differ, record that honestly and troubleshoot the DVWA security level/module. Do not claim the vulnerability was confirmed.

## Finding notes to fill
- Test date/time: `[FILL IN]`
- DVWA URL: `[FILL IN]`
- Security level: `[FILL IN]`
- Input/parameter: `[FILL IN]`
- Baseline result: `[FILL IN]`
- Quote test result: `[FILL IN]`
- True-condition result: `[FILL IN]`
- False-condition result: `[FILL IN]`
- Screenshots/evidence IDs: `[FILL IN]`
- Status: `Confirmed / Not confirmed / Inconclusive`
