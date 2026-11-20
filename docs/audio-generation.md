# Practice audio

These MP3s were generated from the three tracked `.musicxml` files for
[issue #10](https://github.com/dsikar/xmas-repertoire/issues/10).

## Regenerate

Requirements:

- Python 3 (standard library only).
- MuseScore Studio **4.7.5**, build **3654226** (Linux AppImage
  `MuseScore-Studio-4.7.5.260831071-x86_64.AppImage`).
- The bundled **MuseScore Basic** profile and **MS Basic.sf3** soundfont
  (`share/mscore4portable-4.7/sound/MS Basic.sf3` inside that AppImage).
  The scores select B♭ trumpet / General MIDI program 57 (zero-based program 56).
- FFmpeg with `libmp3lame`; these exports used **FFmpeg n4.3.1**.

From the repository root:

```sh
python3 scripts/render-audio.py
```

If MuseScore or FFmpeg is not on `PATH`, supply executable paths:

```sh
python3 scripts/render-audio.py --musescore /path/to/MuseScore.AppImage --ffmpeg /path/to/ffmpeg
```

To keep temporary playback copies, floating-point WAVs, MIDI diagnostics,
imported MuseScore scores, job files, and export logs:

```sh
python3 scripts/render-audio.py --diagnostics "$PWD/audio-diagnostics"
```

Keep that diagnostics directory out of commits. When using the FFmpeg snap,
choose a diagnostics location under Documents: the snap has its own private
`/tmp`. Without `--diagnostics`, temporary files are created under the repository
and removed automatically.

The script imports each MusicXML into MuseScore, renders a 44.1 kHz stereo float
WAV, and encodes one **192 kbit/s stereo MP3** in the piece's `audio/` directory,
using the MusicXML filename stem. A constant **−6 dB** gain before encoding
preserves relative dynamics and provides headroom. Each output replaces its
previous MP3 only after successful rendering and encoding.

MuseScore settings are isolated for each run, with the metronome explicitly
disabled. The script removes harmony/chord-symbol elements from temporary
playback copies because MuseScore otherwise adds chord accompaniment on import.
The tracked MusicXML, MuseScore projects, notes, and PDFs are unchanged.

## Playback interpretation and limitations

- All three MusicXML files specify a chromatic transposition of −2 semitones.
  The recordings use that sounding pitch. Joy to the World's B♭ instrumentation
  remains the inference documented in its transcription notes.
- **Feliz Navidad:** ♩ = 132. Both repeated sections, alternate endings, and
  one-bar repeat signs are played. The 96 written bars expand to 109 played
  bars (436 quarter-note beats). The six unslashed grace notes are audible in
  the audio, although MuseScore's MIDI export omits them; MIDI alone cannot
  validate those ornaments.
- **Joy to the World:** no metronome mark is encoded. MuseScore uses ♩ = 120;
  this is a practice playback choice, not a recovered source marking.
- **In the Bleak Mid-Winter:** ♩ = 92. The opening four-bar rest and all later
  rests are included. Its 73 physical bars total 292 quarter-note beats.
- The plain-text **rall.** in Joy to the World and **molto rit.** in In the
  Bleak Mid-Winter do not create tempo changes on MusicXML import. These
  recordings keep their initial tempos to the end. A performed slowdown would
  require an editorial tempo curve; none has been invented here.
- Feliz Navidad's **Cup Mute** text does not select a dedicated cup-mute
  sample in this export. Its hand-clap cross noteheads remain pitched trumpet
  notes, as already documented in the transcription notes. These recordings
  are practice references, not a recreation of those timbres.

## Verification recorded on 20 November 2026

All MP3s decoded fully with FFmpeg without errors. Both source and encoded signal
levels were checked; the float WAV peaks were below full scale, and the decoded
MP3 peaks below leave headroom. Leading rests were retained and all recordings
include the final notes and a roughly three-second export tail.

| Piece | Decoded duration | Decoded peak (full scale = 1) | First audible sound | MIDI note attacks checked |
| --- | ---: | ---: | ---: | ---: |
| Feliz Navidad | 201.181 s | 0.540 | 0.684 s | 454 ordinary attacks, plus six ornaments checked in the WAV |
| Joy to the World | 87.000 s | 0.639 | 0.002 s | 118 |
| In the Bleak Mid-Winter | 193.434 s | 0.207 | 10.439 s | 148 |

Every ordinary MIDI note attack was matched against the MusicXML's pitch and
beat position after B♭ transposition, tied-note merging, and expansion of repeat
signs and alternate endings. The only onset shifts were MuseScore's expected
grace-note timing. No extra chord accompaniment notes remained. MIDI tempo
maps confirmed 132, 120, and 92 respectively; changing velocities in Feliz
Navidad and Joy to the World confirmed dynamic playback.

The sounding E4–F♯4–G4 contours around all three grace-note pairs in Feliz
Navidad were checked in the WAV using short-window autocorrelation. This
checks the audio independently of MuseScore's incomplete MIDI grace export.

To repeat the full decoder integrity check:

```sh
for recording in pieces/*/audio/*.mp3; do
    ffmpeg -nostdin -v error -i "$recording" -f null - || exit 1
done
```

**Manual listening sign-off is pending.** Automated note and signal checks do
not replace a full human listen-through. Before accepting issue #10, listen to
all three MP3s against their scores, including the two repeat sections and
alternate endings in Feliz Navidad, the long rests in the other pieces, and
each ending. Confirm that the documented constant tempos and timbre limitations
are suitable for practice.
