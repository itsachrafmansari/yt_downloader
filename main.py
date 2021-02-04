import eel
from pytube import YouTube

eel.init('GUI files')

@eel.expose
def playlist_dl(x):
    print(x)

@eel.expose
def video_dl(x):
    print(x)
    vid = YouTube(x)
    strm = str(vid.streams.get_lowest_resolution())
    print(strm)

eel.start('gui.html')