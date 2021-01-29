import os
import ffmpeg
from pytube.helpers import safe_filename
from pydub import AudioSegment
from pytube import YouTube, Playlist

blankline = '_' * 70 + '\n \n'   # Some decoration !
dlpath = r'C:\Users\Your Username\Downloads'  # Choose a download folder

# Coverts downloaded audio files from there original format .webm to .mp3
def convertaudio(var):
    webmaudio = os.path.join(dlpath, safe_filename(var.title) + '.webm')
    mp3audio = os.path.join(dlpath, safe_filename(var.title) + '.mp3')
    AudioSegment.from_file(webmaudio, "webm").export(mp3audio, format="mp3")
    os.remove(webmaudio)

#Defining the download function
def dl(var):

    if Format == 'v' or Format == 'V':

        listed_stream = var.streams.filter(only_video=True, subtype="webm").order_by("resolution")
        listed_stream = str(listed_stream).replace("[", "").replace("]", "")

        streams_reso = list(listed_stream.split(", "))
        streams_reso[:] = [text.replace(text[:text.find("res=") + 5], "")
                               .replace(text[text.find(" fps=") - 2:], "") for text in streams_reso]

        streams_itag = list(listed_stream.split(", "))
        streams_itag[:] = [text.replace(text[:text.find("itag=") + 6], "")
                               .replace(text[text.find("mime_type=") - 2:], "") for text in streams_itag]

        print(blankline + "Here's the available resolutions :\n")
        for text in streams_reso:
            print(text)

        chosen_reso = input("Choose a reso [e.g. 1440]: ")
        chosen_itag = streams_itag[streams_reso.index(str(chosen_reso))]

        print('Video titled [' + var.title + '] started downloading')

        if int(chosen_reso) > 720:
            var.streams.get_by_itag(chosen_itag).download(dlpath)
            var.streams.filter(only_audio=True, subtype="mp4").order_by("bitrate").last().download(dlpath)

            filepath = os.path.join(dlpath, safe_filename(var.title))

            video_stream = ffmpeg.input(filepath + ".webm")
            audio_stream = ffmpeg.input(filepath + ".mp4")

            ffmpeg.output(audio_stream, video_stream, filepath + " - HD.mp4").run()

            os.remove(filepath + ".webm")
            os.remove(filepath + ".mp4")

        else:
            var = var.streams.filter(progressive=True, mime_type="video/mp4").get_by_resolution(chosen_reso + "p")
            var.download(dlpath)

        print('Video titled [' + var.title + '] has been downloaded')

    if Format == 'a' or Format == 'A':
        print('Video titled [' + var.title + '] started downloading')
        var.streams.filter(only_audio=True, subtype='webm').order_by('bitrate').last().download(dlpath)
        print('Video titled [' + var.title + '] has been downloaded')

#Some inputs
Type = input('What yo want to download ? [v] for video and [p] for playlist : ')
Format = input(blankline + 'What format you want to download ? [v] for video and [a] for audio : ')
url = input(blankline + 'Write the link : ')

#Download starts
print(blankline + 'Loading in progress, please wait...')
if Type == 'v' or Type == 'V':
    video = YouTube(url)
    dl(video)
if Type == 'p' or Type == 'P':
    playlist = Playlist(url)
    for video in playlist.videos:
        dl(video)
print(blankline + 'Done !')