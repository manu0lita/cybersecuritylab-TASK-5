# 2. Environment Setup and Verification

## Verify the currently running DVWA
Run these on Kali:

```bash
ip -br addr
docker --version
docker compose version
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}'
curl -I --max-time 5 http://127.0.0.1:4280
```

A `200`, `302`, or other HTTP response can indicate a service responds; a connection refusal usually means nothing is listening on that address/port. Record the actual result and timestamp.

## Start official DVWA Compose setup if it is not already running
Only do this if you do not have an existing DVWA directory/instance you need to preserve:

```bash
git clone https://github.com/digininja/DVWA.git
cd DVWA
docker compose up -d
docker compose ps
curl -I --max-time 5 http://127.0.0.1:4280
```

The official Compose file binds host access to `127.0.0.1:4280` by default. Keep that setting. Do not change it to `4280:80` or a bridged/public binding for this capstone.

If `git clone` fails, capture the error and stop rather than making broad network changes. If a `DVWA` folder already exists, `cd DVWA` there and inspect it instead of cloning a second copy.

## Login and configuration
1. Open `http://127.0.0.1:4280`.
2. Use the credentials configured for your own instance. Common default credentials are `admin` / `password` if unchanged.
3. If DVWA asks for initialization, use its setup page and click **Create / Reset Database** only in this disposable training lab.
4. Open **DVWA Security** and select **Low** for the initial controlled demo.
5. Capture a screenshot that shows the URL and DVWA page. Do not expose unrelated browser tabs or private data.

## Stop the lab after the exercise
From the DVWA project directory:

```bash
docker compose stop
```

Use `docker compose down` only if you want to remove the containers for this project. Do not remove the data volume unless you deliberately want to reset the lab.
