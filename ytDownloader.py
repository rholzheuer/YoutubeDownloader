from pytube import YouTube
from sys import argv

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    live_progress = (bytes_downloaded / total_size) * 100
    print(f'Downloading... {live_progress:.2f}% done', end='\r')

link = argv[1]
yt = YouTube(link, on_progress_callback=progress_function)

print("Title: ", yt.title)
print("Number of views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download("/Volumes/KINGSTON")