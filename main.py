# ███████████████████████████████████████████████ SETTING UP THE PROGRAM ███████████████████████████████████████████████
import os
import ffmpeg
from pytube import YouTube, Playlist
from pytube.helpers import safe_filename


# ═══════════════════════════════════════════[ Texts used in this program ]═════════════════════════════════════════════
dlpath = r"C:\Users\YOUR_USERNAME\Downloads"  # Choose a download folder
blankline = "_" * 70 + "\n"  # Some decoration !
welcomeText = '''
           ▄█████████████████████▄
          ██████████  ▀████████████
          ██████████     ▀█████████
          ██████████     ▄█████████
          ██████████  ▄████████████
           ▀█████████████████████▀

      YOUTUBE VIDEO/PLAYLIST DOWNLOADER
'''
vid_aud_msg = "V for video, or A for audio : "
link_msg = "Write the link : "
avreso_msg = "Here's all the available video resolutions :"
choose_reso_msg = "Choose a resolution [e.g. 1080p]: "
loading_msg = "Loading, please wait..."
done_msg = "Done !"


# ════════════════════════════════════[ Defining some functions to be used later ]══════════════════════════════════════
# Indicates that a video started downloading
def startdl(var):
    print("Video titled [" + var.title.upper()[:50] + "] started downloading")


# Indicates that a video finished downloading
def finishdl(var):
    print("Video titled [" + var.title.upper()[:50] + "] has been downloaded")


# Download a video as an audio file
def vid_to_aud(var):
    startdl(var)
    audioFile = var.streams.filter(only_audio=True).order_by("abr").last()
    audioFile.download(dlpath, filename_prefix="[Audio] ")
    path2audio = os.path.join(dlpath, "audiofile " + safe_filename(audioFile.title))
    audioInput = ffmpeg.input(path2audio + audioFile.subtype)
    ffmpeg.output(audioInput, path2audio + ".mp3").run()
    os.remove(path2audio + audioFile.subtype)
    finishdl(var)


# Download videos from a playlist
def dl_from_pl(var):
    if the_format == "v" or the_format == "V":
        startdl(var)
        var.streams.filter(subtype="mp4", progressive=True).order_by("resolution").last().download(dlpath)
        finishdl(var)
    elif the_format == "a" or the_format == "A":
        vid_to_aud(var)


# ════════════════════════════[ Defining the function that download videos individually]════════════════════════════════
def dl_a_vid(var):

    # If the selected format is video, then run this
    if the_format == "v" or the_format == "V":

        # Display a list of all available video resolutions
        all_streams = var.streams
        video_resolutions = []
        for stream in all_streams:
            reso = stream.resolution
            if reso and reso not in video_resolutions:
                video_resolutions.append(reso)

        print("\n" + blankline + avreso_msg)
        print(*video_resolutions, sep=',    ')

        # Choose one of the available resolutions (e.g. 1080p)
        chosen_reso = input(choose_reso_msg)

        # Indicates the start of the download process
        startdl(var)

        # Filter the streams according to the chosen resolution
        video_streams = all_streams.filter(type="video", resolution=chosen_reso)

        # If the stream is progressive, GREAT! Let's download it
        done = False
        for stream in video_streams:
            if stream.is_progressive:
                stream.download(dlpath)
                done = True
                break

        # If not then download the audio and video files separately and combine them
        if not done:
            # Download the video part
            videoFile = video_streams.order_by("filesize_approx").first()
            videoFile.download(dlpath, filename_prefix="videofile ")

            # Download the audio part
            audioFile = all_streams.filter(only_audio=True).order_by("abr").last()
            audioFile.download(dlpath, filename_prefix="audiofile ")

            # Here's the path to the two downloaded files, and the name of the final file
            videoTitle = safe_filename(videoFile.title)
            path2video = os.path.join(dlpath, "videofile " + videoTitle + videoFile.subtype)
            path2audio = os.path.join(dlpath, "audiofile " + videoTitle + audioFile.subtype)
            path2final = os.path.join(dlpath, videoTitle + ".mp4")

            # Use FFMPEG to combine the video with the audio and output them as a single mp4 file
            videoInput = ffmpeg.input(path2video)
            audioInput = ffmpeg.input(path2audio)
            ffmpeg.output(videoInput, audioInput, path2final).run()

            # Remove each of the video and audio file, leaving only the finished mp4 file
            os.remove(path2video)
            os.remove(path2audio)

        # Indicates the finish of the download process
        finishdl(var)

    # If the selected format is audio, then run this
    elif the_format == "a" or the_format == "A":
        vid_to_aud(var)


# █████████████████████████████████████ THE USER INTERACTS WITH THE FOLLOWING CODE █████████████████████████████████████
print(welcomeText)
url = input(blankline + link_msg)  # Write the url of the video/playlist
the_format = input(blankline + vid_aud_msg)  # Which file format (mp4/mp3)
print(blankline + loading_msg)

if "playlist?list" in url:
    # Load playlist data
    playlist = Playlist(url)
    for video in playlist.videos:
        dl_from_pl(video)
else:
    # Load video data
    video = YouTube(url)
    dl_a_vid(video)

print(blankline, done_msg, "\n", "█" * 70)

input("Press enter to exit")
