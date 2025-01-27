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
        'format': "best",
        'outtmpl': '%(title)s.%(ext)s',
        }
        #Download the video
        with YoutubeDL(ydl_opts) as yt_dlp_object:
            info = yt_dlp_object.extract_info(yt_dlp_link, download=True)
            title.configure(text = {info['title']})
            messagebox.showinfo("Success", "Downloaded successfully")
            finishLabel.configure(text ="Downloaded successfully")

    except Exception as e:
        finishLabel.configure(text = "Error: " + str(e), text_color = "red")
        messagebox.showerror("Error", str(e))
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress.set(percent)

    ydl_opts = {
    'format': "best",
    'outtmpl': '%(title)s.%(ext)s',
    'progress_hooks': [progress_hook],
    }
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


#Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady =10)

#Progress percentage
progress = customtkinter.CTkProgressBar(app, width=400, height=10, text="0%")
progress.set(0)
progress.pack(padx = 10, pady = 10)

#Submit the url
download_button = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx = 10, pady = 10)

#run app
app.mainloop()