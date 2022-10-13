from moviepy.editor import VideoFileClip, clips_array, vfx

clip1 = VideoFileClip("input/pep8 song.mp4")
clip1 = clip1.subclip((1, 15), (1, 40))
clip1 = clip1.margin(10)
clip2 = clip1.fx(vfx.mirror_x)
clip3 = clip1.fx(vfx.mirror_y)
clip4 = clip1.resize(0.60)

final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])

final_clip.resize(width=480).write_videofile("output/mtv.mp4")
