import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
import random
import os

mixer.init()

# -------------------- VARIABLES --------------------

playlist = []
current_index = 0
paused = False
repeat_mode = False
dark_mode = True

# -------------------- WINDOW --------------------

root = tk.Tk()
root.title("🎵 Premium Music Player")
root.geometry("1000x700")
root.configure(bg="#ffffff")

# -------------------- THEME --------------------

def toggle_theme():
    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        bg = "#ffffff"
        fg = "#d32f2f"
    else:
        bg = "#202020"
        fg = "#ffffff"

    root.configure(bg=bg)

    for w in root.winfo_children():
        try:
            w.configure(bg=bg, fg=fg)
        except:
            pass

# -------------------- ALBUM COVER --------------------

cover_frame = tk.Frame(root)
cover_frame.pack(pady=10)

img = Image.new("RGB", (250,250), "lightgray")
img = ImageTk.PhotoImage(img)

cover_label = tk.Label(cover_frame, image=img)
cover_label.pack()

# -------------------- SONG INFO --------------------

song_label = tk.Label(
    root,
    text="No Song Selected",
    font=("Segoe UI",20,"bold"),
    fg="#d32f2f"
)
song_label.pack()

duration_label = tk.Label(
    root,
    text="00:00 / 00:00",
    font=("Segoe UI",12)
)
duration_label.pack()

# -------------------- PLAYLIST --------------------

playlist_box = tk.Listbox(
    root,
    width=80,
    height=10,
    font=("Segoe UI",11)
)
playlist_box.pack(pady=10)

# -------------------- FUNCTIONS --------------------

def add_songs():
    global playlist

    files = filedialog.askopenfilenames(
        filetypes=[("MP3 Files","*.mp3")]
    )

    for file in files:
        playlist.append(file)
        playlist_box.insert(tk.END, os.path.basename(file))

def load_song(index):

    global current_index

    current_index = index

    song = playlist[index]

    mixer.music.load(song)

    song_label.config(
        text=os.path.basename(song)
    )

    audio = MP3(song)

    total_seconds = int(audio.info.length)

    mins = total_seconds // 60
    secs = total_seconds % 60

    duration_label.config(
        text=f"00:00 / {mins:02}:{secs:02}"
    )

def play_song():

    selected = playlist_box.curselection()

    if selected:
        load_song(selected[0])

    mixer.music.play()

    update_progress()

def pause_song():
    mixer.music.pause()

def resume_song():
    mixer.music.unpause()

def stop_song():
    mixer.music.stop()

def next_song():

    global current_index

    current_index += 1

    if current_index >= len(playlist):
        current_index = 0

    load_song(current_index)
    mixer.music.play()

def previous_song():

    global current_index

    current_index -= 1

    if current_index < 0:
        current_index = len(playlist)-1

    load_song(current_index)
    mixer.music.play()

def shuffle_song():

    global current_index

    current_index = random.randint(
        0,
        len(playlist)-1
    )

    load_song(current_index)
    mixer.music.play()

def toggle_repeat():

    global repeat_mode

    repeat_mode = not repeat_mode

    if repeat_mode:
        repeat_btn.config(text="Repeat ON")
    else:
        repeat_btn.config(text="Repeat OFF")

# -------------------- VOLUME --------------------

def set_volume(v):
    mixer.music.set_volume(float(v)/100)

volume = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    command=set_volume,
    label="Volume"
)

volume.set(70)
volume.pack()

# -------------------- PROGRESS BAR --------------------

progress = ttk.Scale(
    root,
    from_=0,
    to=100,
    length=500
)

progress.pack(pady=10)

def update_progress():

    if mixer.music.get_busy():

        position = mixer.music.get_pos()/1000

        progress.set(position)

        root.after(
            1000,
            update_progress
        )

# -------------------- VISUALIZER --------------------

canvas = tk.Canvas(
    root,
    width=500,
    height=100,
    bg="black"
)

canvas.pack(pady=10)

bars = []

for i in range(30):

    x = i * 18

    bar = canvas.create_rectangle(
        x,
        100,
        x+12,
        50,
        fill="red"
    )

    bars.append(bar)

def animate():

    for bar in bars:

        h = random.randint(20,100)

        x1,y1,x2,y2 = canvas.coords(bar)

        canvas.coords(
            bar,
            x1,
            100-h,
            x2,
            100
        )

    root.after(120, animate)

animate()

# -------------------- BUTTONS --------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

btn_style = {
    "font":("Segoe UI",11,"bold"),
    "bg":"#d32f2f",
    "fg":"white",
    "width":12
}

tk.Button(
    button_frame,
    text="Add Songs",
    command=add_songs,
    **btn_style
).grid(row=0,column=0,padx=5)

tk.Button(
    button_frame,
    text="Previous",
    command=previous_song,
    **btn_style
).grid(row=0,column=1,padx=5)

tk.Button(
    button_frame,
    text="Play",
    command=play_song,
    **btn_style
).grid(row=0,column=2,padx=5)

tk.Button(
    button_frame,
    text="Pause",
    command=pause_song,
    **btn_style
).grid(row=0,column=3,padx=5)

tk.Button(
    button_frame,
    text="Resume",
    command=resume_song,
    **btn_style
).grid(row=0,column=4,padx=5)

tk.Button(
    button_frame,
    text="Next",
    command=next_song,
    **btn_style
).grid(row=0,column=5,padx=5)

repeat_btn = tk.Button(
    button_frame,
    text="Repeat OFF",
    command=toggle_repeat,
    **btn_style
)

repeat_btn.grid(row=1,column=0,pady=10)

tk.Button(
    button_frame,
    text="Shuffle",
    command=shuffle_song,
    **btn_style
).grid(row=1,column=1)

tk.Button(
    button_frame,
    text="Theme",
    command=toggle_theme,
    **btn_style
).grid(row=1,column=2)

root.mainloop()