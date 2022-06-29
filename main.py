# ███████████████████████████████████████████████ SETTING UP THE PROGRAM ███████████████████████████████████████████████
import os
from pytube import YouTube, Playlist
from pytube.helpers import safe_filename


# ═══════════════════════════════════════════[ Texts used in this program ]═════════════════════════════════════════════
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
loading_msg = "Loading, please wait...\n"
done_msg = "DONE !"
exit_msg = "Type Q to exit or R to download another video : "
exit_command = "R"


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def startdl(var):
    print(f"╔═ Video titled [{var.title.upper()[:50]}] started downloading")


def finished_original_download():
    print("╟──── Downloaded original file(s)")


def startConverting():
    print("╟──── Converting file(s) to the proper format")


def finishConverting():
    print("╟──── Converting file(s) is done")


def finishdl(var):
    print(f"╚═ Video titled [{var.title.upper()[:50]}] has been downloaded\n")


# ════════════════════════[ Defining the function that download and convert a video to mp3]════════════════════════════
def vid_to_aud(var):
    startdl(var)

    audiofile = var.streams.filter(only_audio=True).order_by("abr").last()
    audiofile.download(filename_prefix="original ")
    finished_original_download()

    startConverting()
    options = '-v error -hide_banner -nostats'
    os.system(f'ffmpeg -i "original {audiofile.default_filename}" "{safe_filename(audiofile.title)}.mp3" {options}')
    os.remove(f'original {audiofile.default_filename}')
    finishConverting()

    finishdl(var)


# ════════════════════════[ Defining the function that download all videos from a playlist]════════════════════════════
# Download videos from a playlist
def dl_from_pl(var, video_index):
    if the_format == "v" or the_format == "V":
        startdl(var)
        var.streams.filter(subtype="mp4", progressive=True).order_by("resolution").last().download(filename_prefix=f"{video_index}) ")
        finishdl(var)
    elif the_format == "a" or the_format == "A":
        vid_to_aud(var)


# ════════════════════════════[ Defining the function that download videos individually]════════════════════════════════
def dl_a_vid(var):

    # If the selected format is video, then run this
    if the_format == "v" or the_format == "V":

        # Make a set of all available video resolutions
        all_streams = var.streams
        video_resolutions = []
        for stream in all_streams.filter(type="video").order_by("resolution"):
            if stream.resolution not in video_resolutions:
                video_resolutions.append(stream.resolution)

        # Display all available video resolutions
        print("\n" + blankline + "Here's all the available video resolutions :")
        print(*video_resolutions, sep=',    ')

        # Choose one of the available resolutions
        chosen_reso = input("Choose a resolution (e.g. 1080p) :")
        print(blankline)

        # Filter the streams according to the chosen resolution
        video_streams = all_streams.filter(type="video", progressive=True, resolution=chosen_reso)

        # If the stream is progressive, GREAT! Let's download it
        if video_streams:
            startdl(var)
            video_streams[0].download()
            finishdl(var)

        # If not then download the audio and video files separately and combine them
        else:
            startdl(var)

            # Download the video part
            videoFile = all_streams.filter(only_video=True, resolution=chosen_reso).order_by("filesize_approx").first()
            videoFile.download(filename_prefix="videofile ")
            # Download the audio part
            audioFile = all_streams.filter(only_audio=True).order_by("abr").first()
            audioFile.download(filename_prefix="audiofile ")
            finished_original_download()

            # Use FFMPEG to combine the video with the audio and output them as a single mp4 file
            startConverting()

            video_title = safe_filename(videoFile.title)
            input_file_video = f"videofile {videoFile.default_filename}"
            input_file_audio = f"audiofile {audioFile.default_filename}"
            options = '-v error -hide_banner -nostats'
            os.system(f'ffmpeg -i "{input_file_video}" -i "{input_file_audio}" -c copy "{video_title}.mp4" {options}')
            os.remove(input_file_video)
            os.remove(input_file_audio)

            finishConverting()

            finishdl(var)

    # If the selected format is audio, then run this
    elif the_format == "a" or the_format == "A":
        vid_to_aud(var)


# █████████████████████████████████████ THE USER INTERACTS WITH THE FOLLOWING CODE █████████████████████████████████████
while exit_command in ("R", "r"):
    clear()
    print(welcomeText)
    url = input(blankline + link_msg)  # Write the url of the video/playlist
    the_format = input(blankline + vid_aud_msg)  # Which file format (mp4/mp3)
    print(blankline + loading_msg)

    if "playlist?list" in url:
        # Load playlist data
        playlist = Playlist(url)
        for video_index, video in enumerate(playlist.videos):
            dl_from_pl(video, video_index)
    else:
        # Load video data
        video = YouTube(url)
        dl_a_vid(video)

    print(blankline + done_msg)

    exit_command = input(exit_msg)
