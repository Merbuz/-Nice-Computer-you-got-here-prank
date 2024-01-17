from media import Media
from tkinter import Tk, Label
from screeninfo import get_monitors
import moviepy.editor as mp
from pytube import YouTube
import os

# Download video
YouTube('https://youtu.be/KpBnc9acOZg?si=ADZ1q0LGGdlREozB').streams.first().download('')

# Resize it to fullscreen
clip = mp.VideoFileClip("Nice computer!.mp4")
clip_resized = clip.resize(width=get_monitors()[0].width).write_videofile("Nice computer!.mp4", threads=8,fps=24)
media = Media('Nice computer!.mp4')

# Create Tkinter window
root = Tk()
root.attributes('-fullscreen', True)
root.frame = Label(root)
root.frame.pack(expand="true")

# Let's go motherfucker
media.Play(audio=0, video=0, audioDevice=None, videoFrame=root.frame)
root.after(5800, root.destroy)
root.mainloop()

# Have a good restart! :)
os.system("shutdown /r /t 00")


