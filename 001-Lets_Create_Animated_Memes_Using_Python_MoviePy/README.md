# Let's Create Animated Memes Using Python MoviePy

Youtube link: https://www.youtube.com/watch?v=7L9EE1Llu_8
MoviePy: https://zulko.github.io/moviepy/index.html
Youtube-dl: https://youtube-dl.org/

## Note on bug in sample04c.py that was in display during the show

These two are the relevant lines:

> clip3 = CompositeVideoClip([clip2, subtitle])
> combined = concatenate_videoclips([clip1, clip3], method="compose")

clip3 will be a composite of clip2 and the subtitle. However, the resolution would change.

When you concatenate the clips with different resolutions, we need to use the "compose" method, so that the clips would be centered.

I am unsure why compositing a TextClip (the subtitle variable) would change the behavior so much that we need to use "compose" when concatenating.

## Video Assets

- Shia LaBeouf: https://www.youtube.com/watch?v=RFmlV1B0zw0
- The Pep8 Song: https://www.youtube.com/watch?v=hgI0p1zf31k
- Karaoke: https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Image assets

- The Brave Fighter of Sun Fighbird
- Lord of the Rings
- https://twitter.com/filmeditingpro/status/581877371038494720
- https://www.flexclip.com/learn/best-video-meme-maker.html
- Dragonball Fighter Z (Gogeta SSJ4 Intro)
- Yo Dawg Heard You
- https://www.reddit.com/r/Animemes/comments/u2ix81/congratulations_you_played_yourself/
- Bohemian Rhapsody
- Death Note
- Curb Your Enthusiasm
- doge