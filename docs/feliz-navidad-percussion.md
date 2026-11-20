# Feliz Navidad: hand-clap percussion

Adds the separate snare track requested in
[issue #12](https://github.com/dsikar/xmas-repertoire/issues/12), with the later
[page cut for #14](feliz-navidad-duration.md) applied.

## Editable tracks and playback

`pieces/feliz-navidad-trumpet2/feliz-navidad-trumpet2-bb.mscz` and its matching
MusicXML contain **Trumpet 2 in B♭** and a separate one-line **Hand claps (snare)**
part. Each can be edited or muted independently in MuseScore.

The sound is acoustic snare, General MIDI note **38** on channel **10**, using
MuseScore Basic. The claps retain their inherited `f` dynamic with 65% percussion
instrument volume. The snare follows the hand-clap notation rather than adding
a drum groove.

The current edition retains bars **1–50**. Its clap passages are **10–18 and
27–40**, including the single claps followed by rests in bars 17 and 18.
The percussion follows the one-bar repeat signs and alternate endings and
rests everywhere else. Bars 51–96 were removed at Daniel's request.

The trumpet keeps its printed cross noteheads, text cues, and repeat signs,
with clap playback disabled. MusicXML uses silent `<cue/>` notes; MuseScore may
make imported cues smaller. Use the native project for the original full-size
cue layout. Genuine trumpet notes, dynamics, tempo, transposition and slurs in
the retained bars are preserved. Chord-symbol playback is disabled in the native
project and suppressed by the exporter. The shortened trumpet-only PDF has
been regenerated separately from the two-staff full score.

[Play / download the mixed MP3](../pieces/feliz-navidad-trumpet2/audio/feliz-navidad-trumpet2-bb.mp3)

## Regeneration and checks

```sh
python3 scripts/render-audio.py --piece feliz-navidad-trumpet2
```

The script preserves the instrumental tracks, disables the metronome, and
encodes a 192 kbit/s MP3 after applying −6 dB gain. Keep edits synchronized
between the native score and MusicXML. See [audio generation](audio-generation.md)
for prerequisites and diagnostic exports.

Both current score formats play **117 ordinary trumpet attacks and 170 snare
hits** over **57 played bars**. The pitches, onsets and velocities match the
retained portion of the previous edition exactly. No clap attacks remain on
the trumpet channel and no chord accompaniment notes are added. The four
remaining grace notes are preserved in both scores; MuseScore's MIDI diagnostics
omit those ornaments.

The full MP3 decodes without errors and lasts **106.636 seconds**, with peak
**0.495** of full scale. See [the duration checks](feliz-navidad-duration.md)
for the score-page boundary and ending verification.

**Full human listening sign-off remains pending.** Check the trumpet/snare
transitions at bars 10, 19, 27 and 41, the alternate endings, and the new ending
at bar 50. Automated checks do not replace that listening step.
