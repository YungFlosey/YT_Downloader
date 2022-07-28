import pytube
from pytube import YouTube, Playlist


def download_high_res(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)
    
def download_low_res(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_lowest_resolution()
    ys.download(path)

def download_audio(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    ys.download(path)

def download_playlist(url, path):
    p = Playlist(url)
    for video in p.videos:
        ps = video.streams.first()
        ps.download(path)


def download(url, path, vh=False, vl=False, a=False):
    if vh == True:
        download_high_res(url, path)
    if vl == True:
        download_low_res(url, path)
    if a == True:
        download_audio(url, path)





