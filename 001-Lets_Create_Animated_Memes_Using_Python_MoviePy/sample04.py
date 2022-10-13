from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

clip1 = VideoFileClip("input/Shia LaBeouf.mp4").subclip((0,59), (1, 2))
clip2 = VideoFileClip("input/Shia LaBeouf.mp4").subclip(15, 19)

combined = concatenate_videoclips([clip1, clip2])

subtitle = (TextClip("use pep8", font="Impact", fontsize=80, color="White")
            .set_duration(4)
            .set_position(("center", "bottom"))
)

composite = CompositeVideoClip([combined, subtitle])

composite.write_gif("output/example3.gif")