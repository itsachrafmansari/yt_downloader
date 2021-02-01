# ███████████████████████████████████████████████ SETTING UP THE PROGRAM ███████████████████████████████████████████████
import os
import ffmpeg
from pytube.helpers import safe_filename
from pytube import YouTube, Playlist
from pydub import AudioSegment


# ═══════════════════════════════════════════[ Texts used in this program ]═════════════════════════════════════════════
dlpath = r'C:\Users\YOUR_USERNAME\Downloads'  # Choose a download folder
blankline = '_' * 70 + '\n'  # Some decoration !
vid_pl = "What yo want to download ? [v] for video and [p] for playlist : "
vid_aud = "What format you want to download ? [v] for video and [a] for audio : "
link = "Write the link : "
choose_reso = "Choose a reso [e.g. 1440]: "


# ════════════════════════════════════[ Defining some functions to be used later ]══════════════════════════════════════
# Indicates that a video started downloading
def startdl(var):
    print('Video titled [' + var.title + '] started downloading')

# Indicates that a video finished downloading
def finishdl(var):
    print('Video titled [' + var.title + '] has been downloaded')

# Download a video as an audio file
def vid_to_aud(var):
    startdl(var)
    var.streams.filter(only_audio=True, subtype='webm').order_by('bitrate').last().download(dlpath)
    webmaudio = os.path.join(dlpath, safe_filename(var.title) + '.webm')
    mp3audio = os.path.join(dlpath, safe_filename(var.title) + '.mp3')
    AudioSegment.from_file(webmaudio, "webm").export(mp3audio, format="mp3")
    os.remove(webmaudio)
    finishdl(var)

# Download videos from a playlist
def dl_from_pl(var):
    if the_format == 'v' or the_format == 'V':
        startdl(var)
        var.streams.filter(subtype='mp4', progressive=True).order_by('resolution').last().download(dlpath)
        finishdl(var)
    if the_format == 'a' or the_format == 'A':
        vid_to_aud(var)

# Download a single video
def dl_a_vid(var):

    if the_format == 'v' or the_format == 'V':

        # Display available resolutions and choose one of them
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

        chosen_reso = input(choose_reso)
        chosen_itag = streams_itag[streams_reso.index(str(chosen_reso))]

        if int(chosen_reso) > 720:
            startdl(var)

            var.streams .get_by_itag(chosen_itag).download(dlpath)
            var.streams.filter(only_audio=True, subtype="mp4").order_by("bitrate").last().download(dlpath)

            filepath = os.path.join(dlpath, safe_filename(var.title))

            video_stream = ffmpeg.input(filepath + ".webm")
            audio_stream = ffmpeg.input(filepath + ".mp4")

            ffmpeg.output(audio_stream, video_stream, filepath + " - HD.mp4").run()

            os.remove(filepath + ".webm")
            os.remove(filepath + ".mp4")

            finishdl(var)

        else:
            startdl(var)
            var = var.streams.filter(progressive=True, mime_type="video/mp4").get_by_resolution(chosen_reso + "p")
            var.download(dlpath)
            finishdl(var)

    if the_format == 'a' or the_format == 'A':
        vid_to_aud(var)


# █████████████████████████████████████ THE USER INTERACTS WITH THE FOLLOWING CODE █████████████████████████████████████

the_type = input(vid_pl)  # Define what to download (Video/Playlist)
the_format = input(blankline + vid_aud)  # Which file format (mp4/mp3)
url = input(blankline + link)  # Write the url of the video/playlist
print(blankline + 'Loading, please wait...')  # Load video/playlist data

if the_type == 'v' or the_type == 'V':
    video = YouTube(url)
    dl_a_vid(video)
if the_type == 'p' or the_type == 'P':
    playlist = Playlist(url)
    for video in playlist.videos:
        dl_from_pl(video)

print(blankline + 'Done !')