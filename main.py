import eel
from pytube import Playlist
import re
import requests as r
import wget

eel.init('GUI files')
dlpath = r'C:\Users\Achraf Mansari\Downloads'  # Choose a download folder

# ════════════════════════════════════[ Defining some functions to be used later ]══════════════════════════════════════
# Indicates that a video started downloading
def startdl(var):
    print('Video titled [' + var.title + '] started downloading')

# Indicates that a video finished downloading
def finishdl(var):
    print('Video titled [' + var.title + '] has been downloaded')


# ═══════════════════════════════════[ Download functions that respond to JS calls ]════════════════════════════════════
@eel.expose
def yt_playlist_dl(url):
    print("Loading...")
    playlist = Playlist(url)
    print("We're ready")
    for video in playlist.videos:
        startdl(video)
        video.streams.filter(subtype='mp4', progressive=True).order_by('resolution').last().download(dlpath)
        finishdl(video)
    print("Download finished")

@eel.expose
def yt_video_dl(x):
    print("youtube video url = " + x)

@eel.expose
def fb_video_dl(x,y):
    view_source = r.get(x).text
    if y == "sd":
        video_real_url = re.search('sd_src:"(.+?)"', view_source)[1]
    elif y == "hd":
        video_real_url = re.search('hd_src:"(.+?)"', view_source)[1]
    wget.download(video_real_url, dlpath)

@eel.expose
def ig_video_dl(x):
    view_source = r.get(x).text
    video_real_url = re.search('property="og:video:secure_url" content="(.+?)"', view_source)[1]
    wget.download(video_real_url, out=dlpath)

eel.start('gui.html')
