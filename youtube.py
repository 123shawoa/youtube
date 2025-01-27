import tkinter
import customtkinter
from yt_dlp import YoutubeDL
from tkinter import messagebox

def on_progress(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        progress.set(float(d['_percent_str'].strip('%')))
        percentis.configure(text = f"{percentage.strip('%')[:-1].replace('.','')}%")
        app.update_idletasks()
        
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
        'progress_hooks': [on_progress]
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

# Callback function for download progress

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

#progress
percentis = customtkinter.CTkLabel(app, text="")
percentis.pack(padx=10, pady =10)

#Progress percentage
progress = customtkinter.CTkProgressBar(app, width=400, height=10)
progress.pack(padx = 10, pady = 10)
progress.set(0)


#Submit the url
download_button = customtkinter.CTkButton(app, text="Download", command=startDownload)
download_button.pack(padx = 10, pady = 10)

#run app
app.mainloop()