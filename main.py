from yt_dlp import YoutubeDL
from tkinter import *
from tkinter import ttk



def download_def(url):
    ytdl = YoutubeDL()
    info = ytdl(url)
    print(info["title"])
    


root = Tk()
root.title("Asha's Simple YouTube downloader")

mainFrame = ttk.Frame(root, padding="3 3 12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainFrame, text="Enter your YouTube video below").grid(row=0, column=1, columnspan=3)

url = StringVar()
ttk.Entry(mainFrame, takefocus=True, textvariable=url).grid(row=1, column=1, columnspan=2)
ttk.Button(mainFrame, text="download", command=lambda: download_def(url)).grid(row=1, column=3)
root.mainloop() # you need this line for the gui to actually run