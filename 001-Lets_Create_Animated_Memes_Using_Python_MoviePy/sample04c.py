from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, ImageClip

clip1 = VideoFileClip("input/Shia LaBeouf.mp4").subclip((0,59), (1, 2))
clip2 = VideoFileClip("input/Shia LaBeouf.mp4").subclip(15, 19)
subtitle = (TextClip("use pep8", font="Impact", fontsize=80, color="White")
            .set_duration(4)
            .set_position(("center", "bottom"))
)

clip2 = CompositeVideoClip([clip2, subtitle])

combined = concatenate_videoclips([clip1, clip2])

doge = ImageClip("input/dog2.png").set_duration(3)
composite = CompositeVideoClip([combined, subtitle, doge])

composite.write_gif("output/example3.gif")