# xmas-repertoire

Christmas repertoire scores (MuseScore + PDF), with trumpet practice audio.

| Piece | MP3 | Duration | Playback tempo |
| --- | --- | --- | --- |
| Feliz Navidad | [Listen / download](pieces/feliz-navidad-trumpet2/audio/feliz-navidad-trumpet2-bb.mp3) | 1:47 | ♩ = 132 |
| Joy to the World | [Listen / download](pieces/joy-to-the-world-trumpet2/audio/joy-to-the-world-trumpet2.mp3) | 1:27 | ♩ = 120 (MuseScore default; no metronome mark in the source) |
| In the Bleak Mid-Winter | [Listen / download](pieces/in-the-bleak-midwinter-trumpet2/audio/in-the-bleak-midwinter-trumpet2.mp3) | 3:13 | ♩ = 92 |

The recordings play at sounding pitch for B♭ trumpet. Written rests are retained,
including about 10.43 seconds of silence at the start of *In the Bleak Mid-Winter*.
Feliz Navidad retains the first two MuseScore pages (bars 1–50), with a separate
snare track for the hand-clap passages. Joy to the World and In the Bleak
Mid-Winter each have a single Trumpet 2 track.
There is no count-in, metronome, or chord-symbol accompaniment.

Workflow: edit the `.mscz` in MuseScore, export the matching `.musicxml`, and
refresh the part PDF when notation changes. With MuseScore and FFmpeg installed,
regenerate all committed MP3s from the repository root:

```sh
python3 scripts/render-audio.py
```

Add `--piece feliz-navidad-trumpet2` to render only Feliz Navidad. Listen through
the result, then commit the score, MusicXML, PDF, and audio updates together.
See [audio generation and verification](docs/audio-generation.md) for tool
requirements and playback details.
