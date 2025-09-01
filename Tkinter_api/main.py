from tkinter import *
import requests
import os

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()  # good practice for errors
    data = response.json()
    quote = data["quote"]
    # Update the canvas text
    canvas.itemconfig(quote_text, text=quote)


# ---------------- SETUP ---------------- #
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Get the folder where this script is located
BASE_DIR = os.path.dirname(__file__)

# ---------------- CANVAS ---------------- #
canvas = Canvas(width=300, height=414)

# Load background image safely
bg_path = os.path.join(BASE_DIR, "background.png")
background_img = PhotoImage(file=bg_path)
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(
    150, 207,
    text="Click Kanye for a quote!",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

# ---------------- BUTTON ---------------- #
kanye_path = os.path.join(BASE_DIR, "kanye.png")
kanye_img = PhotoImage(file=kanye_path)

kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# ---------------- MAINLOOP ---------------- #
window.mainloop()
