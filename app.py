import pyttsx3 as p
import speech_recognition as sr
import time
from listen import listen
from web import *
from youtube import *
from news import *
import randfacts
from jokes import *
from weather import *
from word2number import w2n
import datetime
from playsound import playsound
from notes import *
import winshell
from sendemail import send_email
from apikeys import sendgrid_key, sender_email
from takepicture import take_picture
import tkinter as tk
from tkinter import messagebox
import threading

# Initialize the text-to-speech engine
engine = p.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "morning"
    elif 12 <= hour < 16:
        return "afternoon"
    else:
        return "evening"

today_date = datetime.datetime.now()
r = sr.Recognizer()

def convert_spoken_numbers(spoken_numbers):
    try:
        return str(w2n.word_to_num(spoken_numbers))
    except ValueError:
        return None

assistant_running = True


def run_voice_assistant():
    global assistant_running
    while assistant_running:
        while True:
            try:
                speak("Hello sir, good " + wishme() +  " I am your voice assistant. What can I do for you?")
                text2 = listen()
                if text2:
                    break  # Exit the loop if user input is recognized
                elif get_user_input():
                    text2 = get_user_input()
                    break
                else:
                    speak("I couldn't understand. Please repeat your command.")
            except sr.UnknownValueError:
                speak("I couldn't understand. Please repeat your command.")
        
        if any(keyword in text2 for keyword in ["information", "informations", "wikipedia"]):
            while True:
                try:
                    speak("You need information related to which topic?")
                    text2 = listen()
                    if text2:
                        break  # Exit the loop if user input is recognized
                    else:
                        speak("I couldn't understand. Please repeat your command.")
                except sr.UnknownValueError:
                    speak("I couldn't understand. Please repeat your command.")

            speak(f"Searching {text2} in Wikipedia.")
            print(f"Searching {text2} in Wikipedia.")
            assist = infow()
            assist.get_info(text2)
            time.sleep(3)
            speak("What else can I do for you?")


        
        elif any(keyword in text2 for keyword in ["play", "video", "music", "youtube"]):
            while True:
                try:
                    speak("you want me to play which video?")
                    text2 = listen()
                    if text2:
                        break  # Exit the loop if user input is recognized
                    else:
                        speak("I couldn't understand. Please repeat your command.")
                except sr.UnknownValueError:
                    speak("I couldn't understand. Please repeat your command.")
                               
            speak(f"Searching {text2} on Youtube.")
            print(f"Searching {text2} on Youtube.")
            assist = music()
            assist.play(text2)
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["news", "daily"]):
            print("Sure sir, Now I will read news for you.")
            speak("Sure sir, Now I will read news for you.")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["fact", "facts", "random", "stuff"]):
            speak("Sure sir, here is a random fact.")
            x = randfacts.get_fact()
            print(x)
            speak("Did you know that, " + x)
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["joke", "jokes"]):
            arr = joke()
            print(arr[0])
            speak(arr[0])
            print(arr[1])
            speak(arr[1])
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["temp", "temperature", "weather", "hot", "cold", "outside"]):
            temperature = str(temp())
            description = str(des())
            print(f"Sir today's temperature in Belgrade is {temperature} degrees Celsius, and the weather is {description}.")
            speak(f"Sir today's temperature in Belgrade is {temperature} degrees Celsius, and the weather is {description}.")
            time.sleep(3)
            speak("What else can I do for you?")
            
            
        elif any(keyword in text2 for keyword in ["time", "o'clock", "current", "date", "today"]):
            print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " and currently is " + today_date.strftime("%c"))
            speak("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " and currently is " + today_date.strftime("%c"))
            time.sleep(3)
            speak("What else can I do for you?")
        
        elif any(keyword in text2 for keyword in ["set", "alarm", "tomorrow", "wake"]):
            speak("Sure, please specify the alarm time in a spoken format, like 'two three five zero' for 23:50.")
            alarm_time_text = listen()
            print("Recognized text:", alarm_time_text)
            alarm_time_digits = convert_spoken_numbers(alarm_time_text)
            
            if alarm_time_digits and len(alarm_time_digits) == 4:
                alarm_hour = int(alarm_time_digits[:2])
                alarm_minute = int(alarm_time_digits[2:])
                if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                    speak(f"Setting alarm for {alarm_hour}:{alarm_minute}.")
                    while True:
                        now = datetime.datetime.now()
                        if alarm_hour == now.hour and alarm_minute == now.minute:
                            print("Playing")
                            playsound("crank.mp3")  # Play the alarm sound
                            break
                else:
                    speak("Invalid time format. Please specify the alarm time in a spoken format, like 'two three five zero' for 23:50.")
            else:
                speak("Sorry, I couldn't understand the time you provided.")
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["write", "note", "notes", "text"]):
            while True:
                try:
                    speak("Yes, please tell me the name of the file under you wish me to save it?")
                    notes_name = listen()
                    if notes_name:
                        break  # Exit the loop if user input is recognized
                    else:
                        speak("I couldn't understand. Please repeat your command.")
                except sr.UnknownValueError:
                    speak("I couldn't understand. Please repeat your command.")
            
            print(notes_name)
            speak("Yes, please tell me the notes you wish me to save for you.")
            write_note(notes_name)
            speak("The note has been saved.")
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["empty", "recycle", "bin", "delete"]):
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")
            time.sleep(3)
            speak("What else can I do for you?")

        elif any(keyword in text2 for keyword in ["send", "message", "email"]):
            speak("Please write the recipient's email address.")
            recipient_email = input("Write email address: ").lower()
            print(f"The recipient's email address is: {recipient_email}. Is that correct?")
            speak(f"The recipient's email address is: {recipient_email}. If that is correct, please confirm with 'yes'; if it is not, please say 'no'.")
            confirmation = listen().lower()
            if "yes" in confirmation:
                print(recipient_email)
                speak("Please tell me the subject of the email.")
                subject = listen()
                print(subject)
                speak("Please tell me the content of the email message.")
                body = listen()
                print(body)
                if send_email(sendgrid_key, sender_email, recipient_email, subject, body):
                    print("Email sent successfully!")
                else:
                    print("Failed to send email!")
            elif "no" in confirmation:
                speak("Please provide the recipient's email address again.")
            time.sleep(3)
            speak("What else can I do for you?")    

        elif any(keyword in text2 for keyword in ["camera", "picture", "photo", "selfie"]):
            if take_picture("img.jpg"):
                print("Picture saved successfully.")
                speak("Picture saved successfully.")
            else:
                print("Failed to take a picture.")
                speak("Failed to take a picture.")
            time.sleep(3)
            speak("What else can I do for you?")

        elif "close voice assistant" in text2:
            speak("Are you sure you want to close the voice assistant? Please say 'yes' or 'no'.")
            confirmation = listen().lower()
            if "yes" in confirmation:
                assistant_running = False
            elif "no" in confirmation:
                speak("I will continue listening for your commands.")

    speak("Voice assistant is closing. Goodbye!")
            
import tkinter as tk
import threading
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import tkinter.simpledialog as simpledialog

# Create a Tkinter window
app = tk.Tk()
app.geometry("870x1000")
app.title("Voice Assistant")

def get_user_input():
    user_input = user_input_entry.get()
    return user_input
# Function to start the voice assistant in a separate thread
def start_voice_assistant():
    global assistant_thread
    assistant_thread = threading.Thread(target=run_voice_assistant)
    assistant_thread.daemon = True
    assistant_thread.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Function to stop the voice assistant and close the Tkinter window
def stop_voice_assistant():
    global assistant_thread
    global assistant_running
    assistant_running = False
    assistant_thread.join()
    app.quit()
    

# Function to prompt the user for the recipient's email address
def get_recipient_email():
    recipient_email = simpledialog.askstring("Recipient's Email", "Enter the recipient's email address:")
    return recipient_email

# Function to handle sending emails
def send_email_wrapper():
    recipient_email = get_recipient_email()
    if recipient_email:
        speak("Please tell me the subject of the email.")
        subject = listen()
        print(subject)
        speak("Please tell me the content of the email message.")
        body = listen()
        print(body)
        if send_email(sendgrid_key, sender_email, recipient_email, subject, body):
            print("Email sent successfully!")
        else:
            print("Failed to send email!")

# Create an Entry widget for user input
user_input_entry = tk.Entry(app)
user_input_entry.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="w")
# Create "Start" button in green
start_button = tk.Button(
    app,
    text="Start Voice Assistant",
    command=start_voice_assistant,
    bg="green",  # Green background color
    fg="white",  # White text color
    padx=10,  # Increase horizontal padding
    pady=5,   # Increase vertical padding
)
start_button.grid(row=0, column=0, pady=10, padx=20, sticky="w")

# Create "Stop" button (initially disabled) in red
stop_button = tk.Button(
    app,
    text="Stop Voice Assistant",
    command=stop_voice_assistant,
    state=tk.DISABLED,
    bg="red",  # Red background color
    fg="white",  # White text color
    padx=10,  # Increase horizontal padding
    pady=5,   # Increase vertical padding
)
stop_button.grid(row=0, column=1, pady=10, padx=20, sticky="w")

# Create a frame for displaying available options
options_frame = tk.Frame(app)
options_frame.grid(row=1, column=0, columnspan=4, pady=20, padx=20)

# Define a list of options with colors and font styles
option_styles = [
    ("information", "blue", "Arial 18 bold"),
    ("video", "green", "Arial 18 italic"),
    ("news", "red", "Arial 18 underline"),
    ("random fact", "purple", "Arial 18"),
    ("joke", "orange", "Arial 18"),
    ("temperature", "blue", "Arial 18"),
    ("time", "green", "Arial 18"),
    ("alarm", "red", "Arial 18"),
    ("note", "purple", "Arial 18"),
    ("bin", "orange", "Arial 18"),
    ("email", "blue", "Arial 18"),
    ("camera", "green", "Arial 18")
]

# Create a dictionary to map image extensions to PhotoImage loaders
image_loaders = {
    ".jpg": ImageTk.PhotoImage,
    ".png": ImageTk.PhotoImage,
    ".jpeg": ImageTk.PhotoImage,
}

# Load images for each option using ImageTk and Image from PIL
option_images = {}
image_directory = "images"  # Specify your image directory here
for option_text, color, font_style in option_styles:
    for ext, image_loader in image_loaders.items():
        image_path = os.path.join(image_directory, f"{option_text}{ext}")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((100, 100), Image.LANCZOS)
            image = image_loader(image)
            option_images[option_text] = image
            break

# Create Label widgets for each option with colors and font styles
for i, (option_text, color, font_style) in enumerate(option_styles):
    label = tk.Label(options_frame, text=option_text, font=font_style, fg=color)
    label.grid(row=i // 4 * 2, column=i % 4 * 2, sticky="w", padx=40, pady=40)
    
    # Add an image below each label
    image_label = tk.Label(options_frame, image=option_images.get(option_text, None))
    image_label.grid(row=i // 4 * 2 + 1, column=i % 4 * 2, sticky="w", padx=40, pady=40)

# Configure the grid to expand columns and rows
for i in range(4):
    options_frame.columnconfigure(i * 2, weight=1)
    options_frame.rowconfigure(i // 2 * 2, weight=1)

# Function to handle window close event
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_voice_assistant()
        app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter main loop
app.mainloop()


