# Feliz Navidad: retain the first two score pages

For [issue #14](https://github.com/dsikar/xmas-repertoire/issues/14), Daniel
specified: **remove pages 3 and 4 and regenerate the audio**.

In the four-page native score, page 3 began at **bar 51**. Both editable formats
now retain **bars 1–50** on both the trumpet and snare tracks. Bars 51–96 were
removed, and bar 50 has a final barline. The trailing page break was removed.
The native full score now renders as **two pages**. The trumpet-only PDF was
regenerated and now has **one page**. The retained notes and cue layout are
preserved, including the slur ending in bar 50 and its following rests.

## Playback and duration

The retained repeat sequence is:

**1–17 → 10–16 → 18–50**

This is **57 played bars / 228 quarter-note beats** at the unchanged **♩ = 132**.
The music lasts **103.636 seconds**; MuseScore adds its usual three-second audio
tail, giving an MP3 duration of **106.636 seconds (about 1:47)**. This is the
result of the specified page cut. The earlier estimated half-length of 1:40–1:41
differs because the retained pages contain 50 written bars and their marked
repeat. No tempo change or post-render audio truncation was used.

## Checks on 20 November 2026

- Both score formats contain exactly 50 bars per track, each MusicXML bar
  summing to 4/4. The final barlines agree and no notes from bars 51–96 remain.
- Native-project and MusicXML MIDI exports both contain **117 ordinary trumpet
  attacks and 170 snare hits**. Every retained attack's pitch, onset and velocity
  matches the corresponding portion of the previous edition exactly. No extra
  instruments or pitched clap doubling occur. The four grace notes at bars 22
  and 46 remain in the score and audio; MuseScore omits them from MIDI export.
- The native full-score PDF has two pages; the updated trumpet-only PDF has one.
- The regenerated MP3 fully decodes without errors: **106.636 seconds**, peak
  **0.495** of full scale, first sound at **0.684 seconds**, last sound at
  **103.630 seconds**. Opening rests, the new ending and its decay are retained.
- Joy to the World and In the Bleak Mid-Winter are unchanged.

The branch is `issue-14-feliz-playback-duration`. Regenerate using:

```sh
python3 scripts/render-audio.py --piece feliz-navidad-trumpet2
```

**Human listening sign-off is pending**, especially the retained alternate
endings and the new ending at bar 50.
