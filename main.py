from pytube import YouTube, Playlist

blankline = '_' * 70 + '\n \n' #Some decoration !
dlpath = r'C:\Users\Your Username\Downloads' #Choose a download folder

#Defining the download function
def dl(thevideo):
    print('Video titled [' + thevideo.title + '] started downloading')
    if Format == 'v' or Format == 'V':
        thevideo.streams.filter(subtype='mp4', progressive=True).order_by('resolution').last().download(dlpath)
    if Format == 'a' or Format == 'A':
        thevideo.streams.filter(only_audio=True, subtype='webm').order_by('bitrate').last().download(dlpath)
    print('Video titled [' + thevideo.title + '] has been downloaded')

#Some inputs
Type = input('What yo want to download ? [v] for video and [p] for playlist : ')
Format = input(blankline + 'What format you want to download ? [v] for video and [a] for audio : ')
url = input(blankline + 'Write the link : ')

#Download starts
print(blankline + 'Download in progress, please wait...')
if Type == 'v' or Type == 'V':
    video = YouTube(url)
    dl(video)
if Type == 'p' or Type == 'P':
    playlist = Playlist(url)
    for video in playlist.videos:
        dl(video)
print(blankline + 'Done !')