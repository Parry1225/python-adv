import sys
import os

# pip install --upgrade pytube
# pip install --upgrade moviepy

from pytube import YouTube
from moviepy.editor import *

os.chdir(sys.path[0])

yt = YouTube("https://www.youtube.com/watch?v=C5zTO4nhXl4")
video = yt.streams.filter(progressive=False, subtype="mp4", res="360p")
video[0].download(filename="video.mp4")
print("Download finished...")

video = VideoFileClip("video.mp4")
song = video.audio
song = song.subclip(1, 4)  # 自訂秒數
song.write_audiofile("01.wav")
