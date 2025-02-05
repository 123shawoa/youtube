import tkinter
import customtkinter
from yt_dlp import YoutubeDL
from tkinter import messagebox
import re

def on_progress(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']  # Example: '\x1b[0;94m  0.0\x1b[0m%'
        # Remove ANSI escape sequences
        cleaned_percentage = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', percentage)
        cleaned_percentage = cleaned_percentage.strip().replace('%', '')

        try:
            progress_value = float(cleaned_percentage)
            progress.set(progress_value / 100)  # Normalize to 0-1 for the progress bar
            percentis.configure(text=f"{int(progress_value)}%")  # Display as integer percent
            app.update_idletasks()
        except ValueError as e:
            print(f"Error converting percentage: {e}")


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