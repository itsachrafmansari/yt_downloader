<h1 align="center">YouTube Videos Downloader</h1>
<p align="center">
A simple Python program to download YouTube videos and playlists (in mp4/mp3 format).
</p>

## Getting Started

This program is based on :
* [PyTube](https://github.com/pytube/pytube) (Downloading YouTube videos)
* [FFmpeg](https://github.com/kkroening/ffmpeg-python) (Combining video and audio files, converting audio files to .mp3 and video files to .mp4)

You can simply execute the `requirements_installer.py` to 
automatically install all the necessary libraries, or you can 
install them manually using this command :
```Bash
pip install pytube ffmpeg-python
```
Then, open the `main.py` file and change the `dlpath` to your downloads directory without any `\` or `/`from its end :
> e.g. **C:\Users\Username\Downloads** for windows users.

> e.g. **/home/Username/Downloads** for linux users.

## Usage
1. Run the main file.
2. Type `V` or `v` for video, and `P` or `p` for playlist.
3. Type `V` or `v` to for mp4 video format, and `A` or `a` for mp3 audio format.
4. Type the url of the video/playlist and wait for the video(s) to get loaded.

If you are downloading a single video, a list of all available
 resolutions will appear then you will have to choose one of 
 them by typing it (e.g. `1080p`).
