## Dependencies
This program is based on :
* [PyTube](https://github.com/pytube/pytube) (Downloading YouTube videos)
* [FFmpeg](https://www.ffmpeg.org/download.html) (Combining video and audio files, converting audio files to .mp3 and video files to .mp4)

<br/>

## Getting Started

1. Download and install [FFmpeg](https://www.ffmpeg.org/download.html) on your computer and make sure to add it to your system's PATH variable
2. Install pytube using the following command :
```bash
python -m pip install --upgrade pytube
```

Sometimes, the pypi release becomes slightly outdated. So you can install pytube from the source using this command :

```bash
python -m pip install git+https://github.com/pytube/pytube
```

<br/>

## Usage
1. Run the `main.py` file.
2. Type the url of the video/playlist.
3. Type `V` or `v` to for MP4 video format, and `A` or `a` for MP3 audio format.
4. Wait for the video(s) to get loaded.
5. If you're downloading a single video in MP4 mode, choose from the available resolutions (e.g. `1080p`). Else, your video will start downloading automatically.
6. Wait for the program to finish working, then hit Enter to exit.
7. Your downloaded files are within the same directory the `main.py` file is currently located.
