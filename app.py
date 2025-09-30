from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

# --- Your Personalized Data ---
LOVE_MESSAGES = [
    "You make every day an adventure. ❤️",
    "I appreciate how hard you work for our family.",
    "Thinking about that time we danced in the rain always makes me smile.",
    "Your laugh is my favorite sound in the world.",
    "Today's affirmation: I'm so lucky to be your partner."
]

@app.route('/')
def home():
    # 1. Get a random message from the list
    daily_message = random.choice(LOVE_MESSAGES)

    # 2. Get the current time/date
    current_time = datetime.datetime.now().strftime("%A, %B %d, %Y")

    # 3. Define the countdown target (Anniversary: February 24th)
    today = datetime.datetime.now()
    anniversary_this_year = datetime.datetime(today.year, 2, 24)
    if today > anniversary_this_year:
        # If today is after this year's anniversary, use next year's
        target_date = datetime.datetime(today.year + 1, 2, 24)
    else:
        target_date = anniversary_this_year
    # Calculate days left
    time_left = target_date - today
    days_left = time_left.days

    # Pass all data to the HTML template
    return render_template('index.html',
                           message=daily_message,
                           date=current_time,
                           countdown=days_left)

if __name__ == '__main__':
    # Set debug=True for easier development
    app.run(debug=True)