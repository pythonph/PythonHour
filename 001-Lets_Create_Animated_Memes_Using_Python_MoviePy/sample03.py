from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("input/Shia LaBeouf.mp4").subclip((0,59), (1, 2))
clip2 = VideoFileClip("input/Shia LaBeouf.mp4").subclip(15, 19)

combined = concatenate_videoclips([clip1, clip2])
combined.write_gif("output/example2.gif")
