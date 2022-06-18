from pytube import YouTube
from moviepy.editor import VideoFileClip
import sys
import os

os.chdir(sys.path[0])

url = "https://youtu.be/vjIGSNMerlU"  # 請輸入YT網址
yt = YouTube(url)
print("We are downloading video...")

video = yt.streams
result = video.filter(progressive=False, subtype="mp4", res="360p")
print(result[0])

fname = "sss.mp4"

result[0].download(filename=fname)
print("Download finished...")

if os.path.isfile(fname):
    clip = VideoFileClip(fname)
else:
    exit()

new_file = "musll"
new_path = new_file + ".mp3"
new_path_mp444 = new_file + ".mp4"

# i = 0
# while os.path.isfile(new_path):
#     i += 1
#     new_path = new_file + str(i) + ".mp3"

# clip.audio.write_audiofile(new_path)
# print("Convert mp3 Success")
i = 0
while os.path.isfile(new_path_mp444):
    i += 1
    new_path_mp444 = new_file + str(i) + ".mp4"

clip.write_videofile(new_path_mp444)
print("Convert mp4 Success")
