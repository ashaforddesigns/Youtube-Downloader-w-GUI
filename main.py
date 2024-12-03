from yt_dlp import YoutubeDL
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

ytdl = YoutubeDL()

#get download folder regardlesss of os, os.path.join appends the user path with "Downloads" therefore giving me their downloads folder
downloadsLocation = os.path.join(os.path.expanduser("~"), "Downloads")

 
def download_def(url):
    getURL = url.get()
    ytdl.download([getURL])



def browse():
    file_path = filedialog.asksaveasfilename()



root = Tk()
root.title("Asha's Simple YouTube downloader")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainFrame, text="Enter your YouTube video below").grid(row=0, column=1, columnspan=3)

url = StringVar()
ttk.Entry(mainFrame, takefocus=True, textvariable=url).grid(row=1, column=1, columnspan=2)
ttk.Button(mainFrame, text="download", command=lambda: download_def(url)).grid(row=1, column=3, sticky=(W))

ttk.Label(mainFrame, text="Your video will automatically download to your downloads folder unless you hit the 'Save as...' below").grid(row=2, column=1, columnspan=4)
ttk.Button(mainFrame, text="Save as...", command=lambda: browse()).grid(row=3, column=4)


root.mainloop() # you need this line for the gui to actually run