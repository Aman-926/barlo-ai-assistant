import tkinter as tk
from PIL import Image, ImageTk

from weather import get_weather, get_weather_description


# -----------------------------
# Get weather data
# -----------------------------

weather = get_weather(43.10, -75.23)

temperature = weather["temperature_2m"]
feels_like = weather["apparent_temperature"]
condition = get_weather_description(weather["weather_code"])


# -----------------------------
# Create main Barlo window
# -----------------------------

root = tk.Tk()

root.title("Barlo")
root.geometry("500x700")
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


# -----------------------------
# Ask Barlo
# -----------------------------

question_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)

question_entry.pack(pady=10)


def ask_barlo():
    question = question_entry.get()

    if "weather" in question.lower():
        response = (
            f"It's currently {temperature}°F and {condition}. "
            f"It feels like {feels_like}°F outside."
        )
    else:
        response = "I can only answer weather questions right now."

    response_label.config(text=response)


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