from flask import Flask, render_template
import random
import datetime
import os # Import the OS library
from dotenv import load_dotenv # Import the dotenv function

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Your Personalized Data ---
LOVE_MESSAGES = [
    "You make every day an adventure. ❤️🥰",
    "I appreciate how hard you work for US. 💪💕",
    "Thinking about that time we danced in the rain always makes me smile. 💃🌧️😊",
    "Your laugh is my favorite sound in the world. 😂💖",
    "I'm so lucky to be your partner. 🍀💑",
    "Every moment with you is a treasure. 🗝️💎",
    "You light up my life in ways you can't imagine. 💡✨",
    "Your kindness and strength inspire me every day. 🌸💪",
    "I love the way you look at me. 👀😍",
    "You are my best friend and soulmate. 👫💞",
    "I cherish every memory we've made together. 📸❤️",
    "Your smile brightens my darkest days. 😁🌞",
    "I fall in love with you all over again every time I see you. 😍🔁",
    "You make me a better person just by being you. 🌱💖",
    "I can't wait to see what the future holds for us. 🔮🤗",
    "You are my rock and my safe place. 🪨🏡",
    "Every day with you is my favorite day. 📅💝",
    "I love the way you make me feel special and loved. ✨💗",
    "You are my forever and always. ♾️💘",
    "I am grateful for your love and support every single day. 🙏❤️",
    "Our love story is my favorite. 📖💕",
    "You are the reason I believe in magic. 🪄💫",
    "I love the way you challenge me to be my best self. 🏆💪",
    "You are my sunshine on a cloudy day. 🌞☁️",
    "I am so proud to call you mine. 🥹💍",
    "You make my heart skip a beat. 💓🏃‍♂️",
    "I love the way you understand me like no one else does. 🧠💞",
    "You are my home and my adventure all in one. 🏡🌍",
    "I am thankful for every moment we share together. Allhamdulillah. 🤲💞",
    "You are my greatest blessing. 🥰🙏",
    "I love the way you make me laugh until my cheeks hurt. 😂😊",
    "You are my partner in crime and my soulmate. 🕵️‍♂️💑",
    "I am so lucky to have you by my side. 🍀🤗",
    "I love you more than words can express. 📝💖",
    "I love you the most!! 🥇💘",
    "You complete me in every way possible. 🧩❤️",
    "You are my heart's desire. 💖🔥",
    "I am so grateful for your love and companionship. 🙏👫",
    "Your hands fit perfectly in mine. 🤝💞",
    "I love the way you look at me with so much love in your eyes. 👀💗",
    "We were meant to be together. 👫✨",
    "YOU ARE MY EVERYTHING!! 🌎💖",
    "I love you to the moon and back, and then some. 🌙🔙💞",
    "You are the biggest gift in my life. 🎁❤️",
    "You make my life worth living. 🌱💓",
    "I love the way you make me feel like the most important person in the world. 👑💝",
    "I love the way you support and encourage me to chase my dreams. 🏃‍♀️🌟",
    "I love the way you care for me and our relationship. 🫶💑",
    "I love our deep conversations. 🗣️💬",
    "I love the way we can be silly together. 🤪😂",
    "You are my favorite Assalamualaikum and my hardest Allah Hafiz. 🕌💔",
    "I love you for all that you are, all that you have been, and all you're yet to be. 🥰⏳",
    "You are my today and all of my tomorrows. 📅♾️",
    "I love our sunday bruches. 🥞☕",
    "I love the way you make me feel at home no matter where we are. 🏠🌍",
    "I love the way you look at me when you think I'm not noticing. 👀🤫",
    "I love the way you always know how to make me smile. 😁💖",
    "I love your coffee! Its the best! ☕😍",
    "Your voice is my favorite sound. 🔊💘",
    "I love the way you say my name. 🗣️💞",
    "I love the way you hug me. 🤗💖",
    "I love the way you kiss me. 😘💋",
    "I love the way you hold my hand. 🤝💕",
    "I love the way you look at me. 👀💗",
    "I love the way you make me feel. 🥰💓",
    "I love the way you love me. 💞💖",
    "I love you more each day. 📆💘",
    "Being with you feels like home. 🏠💞",
    "I wanna travel the world with you, In Sha Allah. ✈️🌍",
    "You are my bestestttt friend and my soulmate. 👫💖",
    "I love how we can talk about anything and everything. 🗣️💬",
    "I love how you always know how to make me feel better. 😊💗",
    "I love how you make me feel beautiful inside and out. 💃💖",
    "I love how you always put us first. 🥇👫",
    "I really love you!! 🥰💘",
    "I really really love you!! 🥰💘",
    "I really really really love you!! 🥰💘",
    "I really really really really love you!! 🥰💘",
    "I really really really really really love you!! 🥰💘",
    "I really really really really really really love you!! 🥰💘",
    "I really really really really really really really love you!! 🥰💘",
    "I really really really really really really really really love you!! 🥰💘",
    "I really really really really really really really really really love you!! 🥰💘",
    "I really really really really really really really really really really love you!! 🥰💘",
    "I really really really really really really really really really really really love you!! 🥰💘",
    "I really really really really really really really really really really really really love you!! 🥰💘",
    "I love you to infinity and beyond!! ♾️🚀",
    "You are my once in a lifetime. 🕰️💞",
    "I love you more than ice cream!! 🍦💖",
    "I love you 3000!! 🦸‍♂️💗",
    "I love your smell. 👃💞",
    "Fid-duniya wal-akhirah! 🌍♾️",
    "This Duniya is temporary, but my love for you is eternal. 🕊️💖",
    "Allah united us for a reason. 🤲💞",
    "We are made for each other. 👫💖",
    "we are each other's answered prayer. 🤲💑",
    "We fit like jigsaw pieces 🧩💞",
    "Babbuucheee....have a wonderful day! 🥰🌞",
    "Booo I miss you already! 😢💗",
    "Come home soon, I can't wait to see you! 🏠🤗",
    "Come home already, I need a hug! 🏠🤗",
    "You know exactly when to bring me chocolate cake... 🍫🍰",
    "You are my favorite notification. 📱💖",
    "I need you like air. 🌬️💞",
    "You are my better half. 🧩💑",
    "You are my happily ever after. 🏰💖",
    "You are my dream come true. 🌠💗",
    "You are my heart and soul. ❤️👫",
    "You are my reason for being. 🥰🌍",
    "You are my one and only. 1️⃣💖",
    "You are my forever love. ♾️💘",
    "You are amazing just the way you are. 🌟💞",
    "You are my person. 👫💖",
    "You are perfection!! 💯😍",
    "Allah has made you with so much love and care. 🤲💗",
    "I am blessed to have you in my life. 🙏💞",
    "You are sooo handsome!! 😍🤴",
    "You are sooo cuteeeeee!! 🥰🐻",
    "You are my king. 👑💖",
    "You have such a beautiful soul. 🕊️💗",
    "You have such a beautiful heart. 💖💓",
    "Life is better with you in it.",
    "You make my heart smile.",
    "life is goooooooood, Allhamdulillah!!😊",
    "Just reminding you that you're my favorite person in the world.",
    "Have I told you today how much I love you? Because I do! 🥰❤️",
]

# --- UPDATED: P.S. Message List ---
PS_MESSAGES = [
    "P.S. Don't forget to take a break. Love you!",
    "P.S. Have a cup of coffee.",
    "P.S. Eat a snack if you're hungry! 🍎😊",
    "P.S. Don't forget to sip water and stay hydrated! 💧😊",
    "P.S. Please have your lunch on time! 🍽️😊",
    "P.S. Pray first, everything else will fall into place.❤️",
    "P.S. I love you! 🥰❤️",
    "P.S. Text me when you get a chance. 📱😊",
]

@app.route('/')
def home():
    # 1. Get a random message from the list
    daily_message = random.choice(LOVE_MESSAGES)

# 2. Get a random message from the P.S. list 
    random_ps_note = random.choice(PS_MESSAGES)

    # 3. Get the current time/date
    current_time = datetime.datetime.now().strftime("%A, %B %d, %Y")

    # 4. Define the countdown target (Anniversary: February 24th)
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
                           countdown=days_left,
                           ps_note=random_ps_note)

if __name__ == '__main__':
    HOST_IP = os.getenv('LOCAL_HOST_IP', '127.0.0.1')
    
    # Run the application using the retrieved IP address
    app.run(host=HOST_IP, debug=True)


