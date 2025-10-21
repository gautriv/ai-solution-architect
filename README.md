# AI Systems & Automation Architect — 365-Day Gamified Syllabus (Flask App)

A complete end‑to‑end **daily learning companion** that guides you from **zero** to **AI Systems & Automation Architect** in 12 months (4 gamified seasons). Each day you get:
- a clear task (2h max),
- links to the exact course/video/tool,
- anti-boredom "Warm-up Win",
- XP & streak tracking,
- notes & reflection prompts,
- certification checkpoints & capstones.

## ✨ Features
- 365-day syllabus (auto-generated, structured by **4 Seasons**).
- **XP, streaks, badges**, and boss fights (certification weeks).
- Daily view with **Mark Complete**, add notes, and record **Warm-up Win**.
- Progress dashboard with stats and upcoming milestones.
- Lightweight: **Flask + SQLite**, deploy anywhere.

## 🧱 Tech Stack
- Flask 3, Jinja templates, Bootstrap via CDN
- SQLite via Flask-SQLAlchemy
- Single-file run, zero external services

## 🚀 Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask --app app.py --debug run
```

Open http://127.0.0.1:5000/

## 🔧 Resetting progress
If you want to reset progress, delete the `instance/progress.db` file and reload the app.

## 🌐 Deploy
- **GitHub Codespaces**: push this repo and open a dev container.
- **Render/Heroku/Fly.io**: standard Flask deployment.
- **Railway**: one-click Flask template, then upload this repo.

## 🏆 Seasons
- **S1: The Connector (Months 1–3)** — Make.com, Airtable, basic APIs, Python-as-a-step
- **S2: The Builder (Months 4–6)** — ServiceNow CSA + enterprise workflows
- **S3: The Architect (Months 7–9)** — LangChain, Responsible AI, Decision dashboards
- **S4: The Governor (Months 10–12)** — Full capstone: human‑in‑the‑loop AI system

## 📜 License
MIT
