import os, json, datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret"),
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'progress.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

os.makedirs(app.instance_path, exist_ok=True)
db = SQLAlchemy(app)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_number = db.Column(db.Integer, unique=True, nullable=False)
    done = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text, default="")
    warmup_done = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)

class Meta(db.Model):
    key = db.Column(db.String(50), primary_key=True)
    value = db.Column(db.String(200))

def load_syllabus():
    with open(os.path.join('data', 'syllabus.json')) as f:
        return json.load(f)["days"]

def get_progress_map():
    items = Progress.query.all()
    return {p.day_number: p for p in items}

def compute_xp(progress_map, syllabus):
    xp = 0
    for d in syllabus:
        p = progress_map.get(d["day_number"])
        if p and p.done:
            xp += d.get("xp", 10)
            if p.warmup_done:
                xp += 2  # tiny bonus
    return xp

def compute_streak(progress_map):
    # Streak = max consecutive days marked done starting from day 1
    streak = 0
    n = 1
    while True:
        p = progress_map.get(n)
        if p and p.done:
            streak += 1
            n += 1
        else:
            break
    return streak

def badges_for(xp, streak, syllabus, progress_map):
    b = []
    if xp >= 100: b.append("Level 1 — Momentum")
    if xp >= 300: b.append("Level 2 — Flow")
    if xp >= 600: b.append("Level 3 — Systems Thinker")
    if streak >= 7: b.append("One-Week Streak")
    if streak >= 21: b.append("Deep Habit")
    # Seasonal badges based on completion percentage
    for season in range(1,5):
        total = len([d for d in syllabus if d["season"] == season])
        done = len([d for d in syllabus if d["season"] == season and progress_map.get(d["day_number"]) and progress_map.get(d["day_number"]).done])
        if total and done/total >= 0.9:
            b.append(f"Season {season} — Mastered")
    return b

@app.route('/')
def index():
    syllabus = load_syllabus()
    progress_map = get_progress_map()
    today = min(len(syllabus), len([p for p in progress_map.values() if p.done]) + 1)
    xp = compute_xp(progress_map, syllabus)
    streak = compute_streak(progress_map)
    b = badges_for(xp, streak, syllabus, progress_map)
    today_item = syllabus[today-1]
    return render_template('index.html', today=today_item, xp=xp, streak=streak, badges=b, total=len(syllabus))

@app.route('/syllabus')
def syllabus():
    syllabus = load_syllabus()
    progress_map = get_progress_map()
    return render_template('syllabus.html', days=syllabus, progress=progress_map)

@app.route('/day/<int:day_number>', methods=['GET', 'POST'])
def day(day_number):
    syllabus = load_syllabus()
    if day_number < 1 or day_number > len(syllabus):
        flash("Invalid day number.")
        return redirect(url_for('index'))
    d = syllabus[day_number-1]
    progress = Progress.query.filter_by(day_number=day_number).first()
    if request.method == 'POST':
        action = request.form.get('action')
        notes = request.form.get('notes', '')
        warmup = True if request.form.get('warmup') == 'on' else False
        if not progress:
            progress = Progress(day_number=day_number)
            db.session.add(progress)
        if action == 'toggle_done':
            progress.done = not progress.done
            progress.completed_at = datetime.datetime.utcnow() if progress.done else None
        progress.notes = notes
        progress.warmup_done = warmup
        db.session.commit()
        return redirect(url_for('day', day_number=day_number))
    next_day = min(len(syllabus), day_number+1)
    prev_day = max(1, day_number-1)
    return render_template('day.html', d=d, day_number=day_number, progress=progress, next_day=next_day, prev_day=prev_day)

@app.route('/progress')
def progress():
    syllabus = load_syllabus()
    progress_map = get_progress_map()
    xp = compute_xp(progress_map, syllabus)
    streak = compute_streak(progress_map)
    b = badges_for(xp, streak, syllabus, progress_map)
    completed = len([1 for p in progress_map.values() if p.done])
    pct = int(100 * completed / len(syllabus))
    upcoming = [d for d in syllabus if not progress_map.get(d["day_number"]) or not progress_map.get(d["day_number"]).done][:7]
    return render_template('progress.html', xp=xp, streak=streak, badges=b, completed=completed, pct=pct, upcoming=upcoming)

@app.route('/badges')
def badges():
    syllabus = load_syllabus()
    progress_map = get_progress_map()
    xp = compute_xp(progress_map, syllabus)
    streak = compute_streak(progress_map)
    b = badges_for(xp, streak, syllabus, progress_map)
    return render_template('badges.html', badges=b)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Initialized the database.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
