from moviepy.editor import VideoFileClip

clip = VideoFileClip("input/Shia LaBeouf.mp4").subclip((0, 59), (1, 2))
clip.write_videofile("output/example1.mp4")