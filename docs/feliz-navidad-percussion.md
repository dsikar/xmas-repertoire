# Feliz Navidad: hand-clap percussion

Implements the score and audio changes for
[issue #12](https://github.com/dsikar/xmas-repertoire/issues/12).

## Editable tracks and playback

Open `pieces/feliz-navidad-trumpet2/feliz-navidad-trumpet2-bb.mscz` in MuseScore.
It contains the original **Trumpet 2 in B♭** part and a separate one-line
**Hand claps (snare)** percussion part. Each track can be edited or muted
independently in MuseScore. The matching MusicXML contains the same two parts.

The percussion uses an **acoustic snare**, General MIDI note **38** on channel
**10**, with the bundled MuseScore Basic soundfont. The clap passages retain their
inherited `f` dynamic; a 65% percussion instrument volume balances the snare
against the trumpet. Snare is the requested
substitute for clapping; this is not an added drum groove.

The original photos confirm hand-clap passages in **bars 10–18, 27–40, and
51–64**, including the single clap followed by rests in bars 17, 18, and 58.
The percussion follows exactly those rhythms, the one-bar repeat signs, and
the first and second endings. It rests everywhere else.

The trumpet part keeps its printed cross noteheads, text cues, and repeat
signs. In the native project only the clap notes' playback is disabled. In
MusicXML those notes use standard `<cue/>` elements, which MuseScore imports
as silent cues. MuseScore may make those imported cues smaller; use the native
project for the preserved original full-size layout. Genuine trumpet notes,
rests, dynamics, tempo, transposition, slurs, and the existing part PDF are
unchanged. Chord-symbol playback is disabled in the native project and remains
suppressed by the audio export script.

The existing MP3 now mixes trumpet and snare:

[Play / download Feliz Navidad](../pieces/feliz-navidad-trumpet2/audio/feliz-navidad-trumpet2-bb.mp3)

## Regeneration

```sh
python3 scripts/render-audio.py --piece feliz-navidad-trumpet2
```

The exporter preserves both instrumental parts, uses isolated settings with no
metronome, and encodes a 192 kbit/s MP3 with −6 dB gain before encoding. It does
not rebuild the percussion track: edits should be made in the two-part score
and kept in sync between `.mscz` and `.musicxml`. See
[audio generation](audio-generation.md) for prerequisites and diagnostic exports.

## Verification on 20 November 2026

- Both files contain two independently editable parts with 96 bars each. Every
  MusicXML part's bar sums to 4/4.
- The MusicXML trumpet part matches its previous version after removing only
  the added cue markers. The native trumpet staff matches its previous version
  after removing only the new playback-disable flags, preserving its layout.
- The 207 percussion events encoded in MusicXML expand to **249 snare hits** over the full
  repeat sequence. Every hit matches the original clap's beat exactly in both
  native-project and MusicXML MIDI exports. All percussion hits use note 38 on
  channel 10; no other percussion notes or extra accompaniment notes occur.
- Both MIDI exports contain **205 ordinary trumpet attacks**. Pitches and order
  match the original melody, with no clap attacks left on the trumpet channel.
  The native project's melodic attack times and velocities match the original
  native project exactly. MuseScore's existing MIDI grace-note omission remains;
  the six grace notes are retained in both scores and in audio playback.
- Both formats retain ♩ = 132 and both repeat sections. The MusicXML playback
  covers **109 played bars / 436 quarter-note beats**. The native MIDI exporter
  ends its track after the last sounding note rather than padding the final bar.
- The updated native full score was rendered and its first page inspected: the
  snare has a separate staff and the original trumpet cues remain visible.
  The existing two-page trumpet-only PDF was retained because its notation did
  not change.
- The complete MP3 decodes without errors: **201.181 seconds**, peak **0.537**
  of full scale, first sound at **0.684 seconds**, last sound at **199.079
  seconds**. The source 44.1 kHz stereo float WAV peaks below full scale.
  The first snare hit was checked for a broadband transient; the opening
  trumpet rest and final audio tail remain intact.

**Full human listening sign-off is pending.** Before accepting the ticket,
listen through the mixed MP3, especially the transitions at bars 10, 19, 27,
41, 51, 59, and 65 and the first repeat's alternate endings. Confirm that the
snare balance and articulation make suitable practice cues. Automated score,
MIDI, layout, and signal checks do not replace this listening step.
