import tkinter
import customtkinter
from pytube import YouTube


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("720x480")
app.title("WYNA YOUTUBE DOWNLOADER")

def downloadaudio():
    try:
        #finishedlabel.configure(text="DOWNLOADING, PLEASE WAIT")
        ytLink= link.get()
        ytObject=YouTube(ytLink, on_progress_callback=on_progress)
        audio=ytObject.streams.get_audio_only(subtype="mp4")
        title.configure(text=ytObject.title, text_color="blue")
        audio.download(filename_prefix="wynayt")
    except:
        finishedlabel.configure(text="INVALID LINK", text_color="red")
    else:
        finishedlabel.configure(text="DOWNLOAD COMPLETE")






def downloadvideo():
    try:
        ytLink= link.get()
        ytObject=YouTube(ytLink,on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="blue")
        video.download(filename_prefix="wynayt")
    except:
        finishedlabel.configure(text="INVALID LINK", text_color="red")
    else:
        finishedlabel.configure(text="DOWNLOAD COMPLETE")



def on_progress(stream, bytes_remaining):
    finishedlabel.configure(text="DOWNLOADING, PLEASE WAIT")
    total_size= stream.filesize
    bytes_downloaded=total_size - bytes_remaining
    percentage_of_completion=bytes_downloaded/total_size*100
    per=str(int(percentage_of_completion))
    pPercentage.configure(text=per+"%")
    pPercentage.update()

    progressbar.set(float(percentage_of_completion) / 100)


title=customtkinter.CTkLabel(app, text="INSERT YOUTUBE LINK")
title.pack(padx=10, pady=10)


url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,corner_radius=7, textvariable=url_var)
link.pack()

finishedlabel=customtkinter.CTkLabel(app,text="NOW")
finishedlabel.pack()

audiobutton=customtkinter.CTkButton(app, text="DOWNLOAD AUDIO", command=downloadaudio, corner_radius=7)
audiobutton.pack(padx=10, pady=10)

videobutton=customtkinter.CTkButton(app, text="DOWNLOAD VIDEO", command=downloadvideo, corner_radius=7)
videobutton.pack(padx=15, pady=15)

pPercentage=customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressbar= customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10 )



app.mainloop()