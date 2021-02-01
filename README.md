<h1 align="center">YouTube Videos Downloader</h1>
<p align="center">
A simple Python program to download YouTube videos and playlists (in mp4/mp3 format).
</p>

## Getting Started :
### Libraries :
This program is based on :
* PyTube (Loading YouTube videos)
* PyDub (Converting audio files to mp3)
* FFmpeg (Combining video and audio files)

You can simply execute the requirements installer to 
automatically install all the necessary libraries, or you can 
install them manually using this command :
```
pip install pytube pydub ffmpeg-python
```

### Edits :
Open the `main.py` file and change the `dlpath` to your downloads directory.

Run this command (in Python console) :
```
import os, pytube; print(os.path.dirname(pytube.__file__))
```

Go to the directory you get, open `request.py`, search for :
``
base_headers = {"User-Agent": "Mozilla/5.0"}
``
and change it to :
``
base_headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
``

Now you are ready !
## Usage :
1. Run the main file.
2. Type `V` or `v` for video, and `P` or `p` for playlist.
3. Type `V` or `v` to for mp4 video format, and `A` or `a` for mp3 audio format.
4. Type the url of the video/playlist and wait for the video(s) to get loaded.

If you are downloading a single video, a list of all available
 resolutions will appear then you will have to choose one of 
 them by typing it as a number (e.g. `1080`).
