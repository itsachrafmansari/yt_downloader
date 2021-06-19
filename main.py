# ███████████████████████████████████████████████ SETTING UP THE PROGRAM ███████████████████████████████████████████████
import os
import ffmpeg
from pytube import YouTube, Playlist
from pytube.helpers import safe_filename


# ═══════════════════════════════════════════[ Texts used in this program ]═════════════════════════════════════════════
dlpath = r'C:\Users\YOUR_USERNAME\Downloads'  # Choose a download folder
blankline = '_' * 70 + '\n'  # Some decoration !
welcomeText = '''
           ▄█████████████████████▄
          ██████████  ▀████████████
          ██████████     ▀█████████
          ██████████     ▄█████████
          ██████████  ▄████████████
           ▀█████████████████████▀

      YOUTUBE VIDEO/PLAYLIST DOWNLOADER
'''
vid_aud = "V for video, or A for audio : "
link = "Write the link : "
avreso = "Here's the available resolutions :"
choose_reso = "Choose a reso [e.g. 1440p]: "
loading = "Loading, please wait..."
done = 'Done !'


# ════════════════════════════════════[ Defining some functions to be used later ]══════════════════════════════════════
# Indicates that a video started downloading
def startdl(var):
    print('Video titled [' + var.title.upper()[:50] + '] started downloading')


# Indicates that a video finished downloading
def finishdl(var):
    print('Video titled [' + var.title.upper()[:50] + '] has been downloaded')


# Download a video as an audio file
def vid_to_aud(var):
    startdl(var)
    var.streams.filter(only_audio=True, subtype='webm').order_by('bitrate').last().download(dlpath)
    filepath = os.path.join(dlpath, safe_filename(var.title))
    webmaudio = ffmpeg.input(filepath + '.webm')
    mp3audio = filepath + '.mp3'
    ffmpeg.output(webmaudio, mp3audio).run()
    os.remove(filepath + '.webm')
    finishdl(var)


# Download videos from a playlist
def dl_from_pl(var):
    if the_format == 'v' or the_format == 'V':
        startdl(var)
        var.streams.filter(subtype='mp4', progressive=True).order_by('resolution').last().download(dlpath)
        finishdl(var)
    elif the_format == 'a' or the_format == 'A':
        vid_to_aud(var)


# ════════════════════════════[ Defining the function that download videos individually]════════════════════════════════
def dl_a_vid(var):

    # If the selected format is video, then run this
    if the_format == 'v' or the_format == 'V':

        # Get all available resolutions
        listed_stream = var.streams.filter(only_video=True, subtype="webm").order_by("resolution")
        streams_reso = []

        # Display all available resolutions
        print(blankline + avreso)
        for elem in listed_stream:
            areso = str(elem)
            areso = areso.replace(areso[:areso.find("res=") + 5], "")
            areso = areso.replace(areso[areso.find("fps=") - 2:], "")
            if areso not in streams_reso:
                streams_reso.append(areso)
                print(areso)

        # Choose one of the available resolutions (e.g. 1440p)
        chosen_reso = input(choose_reso)

        # Indicates the start of the download process
        startdl(var)

        # If the selected resolution is higher than 720p (e.g. 1080p and higher) then run this
        if int(chosen_reso.replace("p", "")) > 720:

            var.streams.filter(progressive=False, mime_type="video/webm", resolution=chosen_reso).first().download(dlpath)
            var.streams.filter(only_audio=True, subtype="mp4").order_by("bitrate").last().download(dlpath)

            filepath = os.path.join(dlpath, safe_filename(var.title))

            video_stream = ffmpeg.input(filepath + ".webm")
            audio_stream = ffmpeg.input(filepath + ".mp4")

            final_file = filepath + " - HD.mp4"
            ffmpeg.output(audio_stream, video_stream, final_file).run()

            os.remove(filepath + ".webm")
            os.remove(filepath + ".mp4")
            os.rename(final_file, final_file.replace(" - HD", ""))

        # If the selected resolution is equal to or lower than 720p then run this
        else:

            # Check if you can normally (video and audio combined) download the video in .mp4 format
            reso = var.streams.filter(progressive=True, mime_type="video/mp4", resolution=chosen_reso)

            # If yes, then download the video in .mp4 format
            if reso:
                var.streams.filter(progressive=True, mime_type="video/mp4", resolution=chosen_reso).first().download(dlpath)

            # If no, then run this
            else:

                # check if you can normally (video and audio combined) download the video in .webm format
                reso = var.streams.filter(progressive=True, mime_type="video/webm", resolution=chosen_reso)

                # If yes, then download the video in .webm format and convert it to .mp4
                if reso:
                    var.streams.filter(progressive=True, mime_type="video/webm", resolution=chosen_reso).first().download(dlpath)
                    filepath = os.path.join(dlpath, safe_filename(var.title))
                    webmvideo = ffmpeg.input(filepath + ".webm")
                    ffmpeg.output(webmvideo, filepath + ".mp4")
                    os.remove(filepath + ".webm")

                # If no, then download video and audio separately, and combine them into a single .mp4 video file
                else:
                    var.streams.filter(progressive=False, mime_type="video/webm", resolution=chosen_reso).first().download(dlpath)
                    var.streams.filter(only_audio=True, subtype="mp4").order_by("bitrate").last().download(dlpath)

                    filepath = os.path.join(dlpath, safe_filename(var.title))

                    video_stream = ffmpeg.input(filepath + ".webm")
                    audio_stream = ffmpeg.input(filepath + ".mp4")
                    final_file = filepath + " - HD.mp4"
                    ffmpeg.output(audio_stream, video_stream, final_file).run()

                    os.remove(filepath + ".webm")
                    os.remove(filepath + ".mp4")
                    os.rename(final_file, final_file.replace(" - HD", ""))

        # Indicates the finish of the download process
        finishdl(var)

    # If the selected format is audio, then run this
    elif the_format == 'a' or the_format == 'A':
        vid_to_aud(var)


# █████████████████████████████████████ THE USER INTERACTS WITH THE FOLLOWING CODE █████████████████████████████████████
print(welcomeText)
url = input(blankline + link)  # Write the url of the video/playlist
the_format = input(blankline + vid_aud)  # Which file format (mp4/mp3)
print(blankline + loading)

if "playlist?list" in url:
    # Load playlist data
    playlist = Playlist(url)
    for video in playlist.videos:
        dl_from_pl(video)
else:
    # Load video data
    video = YouTube(url)
    dl_a_vid(video)

print(blankline, done, "\n", "█" * 70)

input('Press enter to exit')
