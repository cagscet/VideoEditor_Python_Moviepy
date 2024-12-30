from moviepy import *

video_path = input("Please enter the video path: ")
video = VideoFileClip(video_path)

rotate_degrees = int(input("how many degrees the video be rotated ? "))
rotated_video = video.rotated(rotate_degrees)

rotated_video.write_videofile("rotated_video.mp4", codec="libx264")

print("The video has been rotated 180 degrees and saved!")


