import tkinter
import customtkinter
from yt_dlp import YoutubeDL
from tkinter import messagebox

def startDownload():
    yt_dlp_link = link.get()
    if not yt_dlp_link.strip():
        messagebox.showerror("Error", "Cannot be empty")
        return
    try:
        #Configuration for Youtube DL
        ydl_opts = {
            'format': 'best[height = 1080]',
            'outtmpl': '%(title)s.%(ext)s',
        }
        #Download the video
        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([yt_dlp_link])
            messagebox.showinfo("Success", "Downloaded successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# System setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady =10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable = url_var)
link.pack()

#Download button
download = customtkinter.CTkButton(app, text="Download", command= startDownload)
download.pack(padx=10, pady =10)

# Run app
app.mainloop()