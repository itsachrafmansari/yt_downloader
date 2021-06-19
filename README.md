## Dependencies
This program is based on :
* [PyTube](https://github.com/pytube/pytube) (Downloading YouTube videos)
* [FFmpeg](https://github.com/kkroening/ffmpeg-python) (Combining video and audio files, converting audio files to .mp3 and video files to .mp4)

<br/>

## Getting Started

1. You can simply execute the `requirements_installer.py` to automatically install all the necessary libraries, or you can install them from pypi manually using this command :
```bash
python -m pip install pytube
```

Sometime, the pypi release becomes slightly outdated. So you can install them from the source using this command :

```bash
python -m pip install git+https://github.com/pytube/pytube
```

<br/>

2. Then, open the `main.py` file and change the `dlpath` to your downloads directory :
> e.g. **C:\Users\Username\Downloads** for windows users.

> e.g. **/home/Username/Downloads** for linux users.

... and make sure the last character is not `\` or `/`.

<br/>

## Usage
1. Run the `main.py` file.
2. Type `V` or `v` to for MP4 video format, and `A` or `a` for MP3 audio format.
3. Type the url of the video/playlist and wait for the video(s) to get loaded.

If you are downloading a single video, a list of all available resolutions will appear then you will have to choose one of them by typing it (e.g. `1080p`).
Then just wait for the program to finish working.
