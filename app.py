print("Starting the Flask application...")

from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    submitted = False

    if request.method == 'POST':
        submitted = True

        last_date = request.form.get('last_date')
        cycle_length = int(request.form.get('cycle_length', 28))

        last_date = datetime.strptime(last_date, "%Y-%m-%d")

        next_period = last_date + timedelta(days=cycle_length)
        ovulation = next_period - timedelta(days=14)
        fertile_start = ovulation - timedelta(days=2)
        fertile_end = ovulation + timedelta(days=2)

        today = datetime.today()
        days_since_last = (today - last_date).days
        cycle_day = days_since_last % cycle_length

        if cycle_day <= 5:
            phase = "🩸 Period Phase – Take Rest"
        elif cycle_day <= 13:
            phase = "🌱 Follicular Phase – Productive Time"
        elif cycle_day == 14:
            phase = "🌸 Ovulation Phase – High Energy"
        else:
            phase = "🌙 Luteal Phase – Self Care Mode"

        if "Period" in phase:
            tip = "Drink warm water and rest well 💗"
        elif "Ovulation" in phase:
            tip = "You may feel energetic today ✨"
        elif "Follicular" in phase:
            tip = "Good time to start new tasks 🌟"
        else:
            tip = "Practice self-care and avoid stress 🌸"

        result = f"""
        Next Period Date: {next_period.date()} <br>
        Ovulation Date: {ovulation.date()} <br>
        Fertile Window: {fertile_start.date()} to {fertile_end.date()} <br><br>
        Current Phase: {phase} <br>
        Health Tip: {tip}
        """

    return render_template('index.html', result=result, submitted=submitted)


# ---------------- SYMPTOMS PAGE ----------------
@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    tips = None

    advice = {
        "Cramps": [
            "Use warm heating pad 💗",
            "Drink herbal tea ☕",
            "Light stretching 🧘‍♀️"
        ],
        "Mood Swings": [
            "Deep breathing 🌿",
            "Calming music 🎵",
            "Talk to a friend 💞"
        ],
        "Headache": [
            "Drink water 💧",
            "Rest in dark room 🌙",
            "Reduce screen time 📵"
        ],
        "Bloating": [
            "Avoid salty food 🥗",
            "Go for light walk 🚶‍♀️",
            "Drink warm lemon water 🍋"
        ]
    }

    if request.method == 'POST':
        selected = request.form.getlist('symptoms')

        if selected:
            all_tips = []
            for symptom in selected:
                all_tips.append(f"<b>{symptom}:</b>")
                for tip in advice[symptom]:
                    all_tips.append("• " + tip)
                all_tips.append("<br>")

            tips = "<br>".join(all_tips)
        else:
            tips = "No symptoms selected."

    return render_template("symptoms.html", tips=tips)


# ---------------- PRODUCT STOCK PAGE ----------------
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    message = None

    if request.method == 'POST':
        products = request.form.getlist('products')

        required_items = [
            "Sanitary Pads",
            "Tampons",
            "Pain Relief Tablets",
            "Heating Pad",
            "Herbal Tea",
            "period panties"
        ]

        missing = [item for item in required_items if item not in products]

        if missing:
            message = "⚠ Low Stock! Missing: " + ", ".join(missing)
        else:
            message = "✅ All Essential Products Available!"

    return render_template("stock.html", message=message)


# ---------------- DAY PLANNER PAGE ----------------
@app.route('/dayplanner')
def dayplanner():

    schedule = {
        "Morning 🌅": [
            "Drink warm water",
            "Light stretching",
            "Healthy breakfast",
            "Avoid caffeine"
        ],
        "Afternoon ☀": [
            "Take rest breaks",
            "Drink enough water",
            "Eat light lunch",
            "Avoid stress"
        ],
        "Evening 🌆": [
            "Short walk",
            "Heating pad if needed",
            "Relaxing music"
        ],
        "Night 🌙": [
            "Warm shower",
            "Herbal tea",
            "Sleep early"
        ]
    }

    return render_template("dayplanner.html", schedule=schedule)


if __name__ == '__main__':
    app.run(debug=True)
