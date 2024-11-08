#main
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import moviepy.editor as mp
import speech_recognition as sr
import cv2
import sqlite3
from moviepy.editor import VideoFileClip, TextClip

class VideoCaptionGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Caption Generator")

        self.label = tk.Label(master, text="Select Video File:",font=("Times New Roman",14))
        self.label.pack()

        self.select_button = tk.Button(master, text="Select", command=self.select_video)
        self.select_button.pack()

        self.convert_button = tk.Button(master, text="Generate Captions", command=self.generate_captions)
        self.convert_button.pack()


    def select_video(self):
        self.video_file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

    def video_to_audio(self):
        video_clip = mp.VideoFileClip(self.video_file_path)
        audio_path = "audio_from_video.wav"
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        return audio_path

    def audio_to_text(self, audio_path):
        try:
            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source, duration=None)
                text = recognizer.recognize_google(audio_data)
            return text
        except Exception as e:
            print("Error during audio-to-text conversation:", e)
            return ""

    def generate_captions(self):
        if hasattr(self, 'video_file_path'):
            threading.Thread(target=self.process_video).start()
        else:
            print("Please select a video file first.")

    def process_video(self):
        audio_path = self.video_to_audio()
        text = self.audio_to_text(audio_path)
        if text:
            print("Transcribed Text:", text)
            self.display_video_with_captions(text)
        else:
            print("No caption generated .Please check the audio file.")

    def display_video_with_captions(self, captions):
        cap = cv2.VideoCapture(self.video_file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.putText(frame, captions, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Video with Captions', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()





def create_table():
    conn = sqlite3.connect('login_credentials.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def register():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('login_credentials.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    conn.close()

def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('login_credentials.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        open_video_generator()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def open_video_generator():
    root.withdraw()  # Hide login window
    root_video = tk.Toplevel()  # Create new window for video caption generator
    #root.geometry("900x900")
    root_video.geometry("800x800")
    root_video.configure(bg="lightblue")
    app_video = VideoCaptionGeneratorApp(root_video)
   # app = VideoCaptionGeneratorApp(root)
# Create the Tkinter application window
root = tk.Tk()

root.title("Login System")
root.geometry("400x400")
root.configure(bg="lightblue")

create_table()

# Username label and entry
label_username = tk.Label(root, text="Username:",font=("Times New Roman", 12, "bold"))
label_username.grid(row=0, column=0,padx=5, pady=5, sticky="e")
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1,padx=5, pady=5, sticky="we")
#root.grid_columnconfigure(1, weight=1)

# Password label and entry  
label_password = tk.Label(root, text="Password:",font=("Times New Roman", 12, "bold"))
label_password.grid(row=1, column=0,padx=5,  pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1 ,padx=5,pady=5, sticky="we")
#root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(1, weight=1)  
# Login button
button_login = tk.Button(root, text="Login", command=login,font=("Times New Roman", 12, "bold"))
button_login.grid(row=2, column=0, columnspan=2, pady=10)

# Register button
button_register = tk.Button(root, text="Register", command=register,font=("Times New Roman", 12, "bold"))
button_register.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()





