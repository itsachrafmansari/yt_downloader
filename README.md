## Dependencies
This program is based on :
* [PyTube](https://github.com/pytube/pytube) (Downloading YouTube videos)
* [FFmpeg](https://github.com/kkroening/ffmpeg-python) (Combining video and audio files, converting audio files to .mp3 and video files to .mp4)

<br/>

## Getting Started

1. You can simply execute the `requirements_installer.py` to automatically install all the necessary libraries, or you can install them from pypi manually using this command :
```bash
python -m pip install --upgrade pytube ffmpeg-python
```

Sometimes, the pypi release becomes slightly outdated. So you can install it from the source using this command :

```bash
python -m pip install git+https://github.com/pytube/pytube
```

<br/>

2. Then, open the `main.py` file and change the `dlpath` to your downloads directory (make sure the last character isn't `\` or `/`) :
>
>For example :
> 
>Windows : **C:\Users\Username\Downloads**<br/>
>Linux : **/home/Username/Downloads**<br/>
>Mac OS : **/Users/Username/Downloads**<br/>

<br/>

## Usage
1. Run the `main.py` file.
2. Type the url of the video/playlist.
3. Type `V` or `v` to for MP4 video format, and `A` or `a` for MP3 audio format.
4. Wait for the video(s) to get loaded.
5. Choose from the available resolutions (e.g. `1080p`), if you're downloading a single video in the MP4 mode.
6. Wait for the program to finish working, then hit Enter to exit.
