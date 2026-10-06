import tkinter as tk
from PIL import Image, ImageTk

from weather import get_weather, get_weather_description
from voice import record_audio, transcribe_audio


# -----------------------------
# Get weather data
# -----------------------------

weather = get_weather(43.10, -75.23)

temperature = weather["temperature"]
feels_like = weather["feels_like"]
condition = get_weather_description(weather["weather_code"])
high = weather["high"]
low = weather["low"]
precipitation = weather ["precipitation_chance"]


# -----------------------------
# Create main Barlo window
# -----------------------------

root = tk.Tk()

root.title("Barlo")
root.geometry("500x900")
root.resizable(False, False)


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="BARLO",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=(20, 10))


# -----------------------------
# Barlo image
# -----------------------------

barlo_image = Image.open("assets/barlo.jpeg")
barlo_image = barlo_image.resize((300, 300))

barlo_photo = ImageTk.PhotoImage(barlo_image)

barlo_label = tk.Label(
    root,
    image=barlo_photo
)

barlo_label.pack()


# -----------------------------
# Status
# -----------------------------

status_label = tk.Label(
    root,
    text="● ONLINE",
    font=("Arial", 11, "bold")
)

status_label.pack(pady=10)


# -----------------------------
# Weather
# -----------------------------

temperature_label = tk.Label(
    root,
    text=f"{temperature}°F",
    font=("Arial", 30, "bold")
)

temperature_label.pack()


condition_label = tk.Label(
    root,
    text=condition.title(),
    font=("Arial", 16)
)

condition_label.pack()


feels_like_label = tk.Label(
    root,
    text=f"Feels like {feels_like}°F",
    font=("Arial", 12)
)

feels_like_label.pack(pady=(5, 20))
forecast_label = tk.Label(
    root,
    text=f"High: {high}°F • Low: {low}°F • Rain: {precipitation}%",
    font=("Arial", 12)
)

forecast_label.pack(pady=(0, 20))


# -----------------------------
# Ask Barlo
# -----------------------------

question_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)

question_entry.pack(pady=10)


def listen_to_user():
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)

    question_entry.delete(0, tk.END)
    question_entry.insert(0, transcription)

    ask_barlo()


def ask_barlo():
    question = question_entry.get()

    if "weather" in question.lower():
        response = (
            f"It's currently {temperature}°F and {condition}. "
            f"It feels like {feels_like}°F. "
            f"Today's high is {high}°F with a low of {low}°F. "
            f"There's a {precipitation}% chance of precipitation."
        )
    else:
        response = "I can only answer weather questions right now."

    response_label.config(text=response)


listen_button = tk.Button(
    root,
    text="🎤 LISTEN",
    font=("Arial", 12, "bold"),
    command=listen_to_user
)

listen_button.pack(pady=5)


ask_button = tk.Button(
    root,
    text="ASK BARLO",
    font=("Arial", 12, "bold"),
    command=ask_barlo
)

ask_button.pack(pady=10)


# -----------------------------
# Barlo response
# -----------------------------

response_label = tk.Label(
    root,
    text="Ask me about the weather.",
    font=("Arial", 11),
    wraplength=420,
    justify="center"
)

response_label.pack(pady=15)


# -----------------------------
# Start application
# -----------------------------

root.mainloop()