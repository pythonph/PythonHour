# Did I miss a 06-09? No, I just want to name this to a nice number.

from moviepy.editor import *
from moviepy.video.tools.subtitles import *

clip = VideoFileClip("input/Song.mp4")

#line_render = lambda txt: TextClip(txt, font='Impact', fontsize=24, color='white')
def line_render(txt):
    return TextClip(txt, font='Impact', fontsize=24, color='white')

subtitle = SubtitlesClip("input/song.srt", line_render)

composite = CompositeVideoClip([clip, subtitle])
composite.to_videofile("output/fun.mp4")