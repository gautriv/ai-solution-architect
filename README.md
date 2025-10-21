# AI Systems & Automation Architect — 365-Day Gamified Syllabus

A complete end-to-end daily learning companion that guides you from zero to AI Systems & Automation Architect in 12 months (4 gamified seasons). Each day includes:
- A clear task (2-hour maximum)
- Links to the exact course, video, or tool
- Anti-boredom "Warm-up Win" activity
- XP and streak tracking
- Notes and reflection prompts
- Certification checkpoints and capstones

## Features

- 365-day syllabus structured by 4 seasons
- XP, streaks, badges, and certification milestones
- Daily view with task completion, notes, and warm-up tracking
- Progress dashboard with stats and upcoming milestones
- Lightweight architecture: Flask + SQLite, deploy anywhere

## Tech Stack

- Flask 3, Jinja templates, Bootstrap via CDN
- SQLite via Flask-SQLAlchemy
- Single-file run, zero external services

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask --app app.py --debug run
```

Open http://127.0.0.1:5000/

## Resetting Progress

If you want to reset progress, delete the `instance/progress.db` file and reload the app.

## Deployment

- **GitHub Codespaces**: Push this repo and open a dev container
- **Render/Heroku/Fly.io**: Standard Flask deployment
- **Railway**: One-click Flask template, then upload this repo

## Learning Path

### Season 1: The Connector (Months 1-3)
Make.com, Airtable, basic APIs, Python-as-a-step

### Season 2: The Builder (Months 4-6)
ServiceNow CSA + enterprise workflows

### Season 3: The Architect (Months 7-9)
LangChain, Responsible AI, Decision dashboards

### Season 4: The Governor (Months 10-12)
Full capstone: human-in-the-loop AI system

## License

MIT
