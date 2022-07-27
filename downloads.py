import pytube
from pytube import YouTube


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

       