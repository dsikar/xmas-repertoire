# Feliz Navidad (Kacey Musgraves version, arr. Daryl McKenzie): Trumpet 2 in B♭ transcription notes

## Source
- Two phone photos of the printed part: `trumpet2-page1.jpg` and `trumpet2-page2.jpg` (1536×2048 each).
- Page 1 covers bars 1–50 and page 2 covers bars 51–96, with 9 systems on each page.
- Heading on the page: "Feliz Navidad / Recorded by Kacey Musgraves / Composed by Jose Feliciano / Arranged by Daryl McKenzie / Trumpet 2 in B♭".

## Outputs
- `feliz-navidad-trumpet2-bb.mscz`: MuseScore 4 (4.7.7) score, single staff, B♭ Trumpet, concert pitch off.
- `feliz-navidad-trumpet2-bb.pdf`: 2 pages, US Letter. The system breaks match the original (9 + 9 systems).
- `feliz-navidad-trumpet2-bb.musicxml`: exported from the .mscz.
- `work/`: build scripts (`build.py` → MusicXML, `post.py` → .mscz layout and style, `make.sh`) and comparison images (`cmp_p*_s*.png`).

## Musical facts
- Written key: A major (3♯). Concert key: G major.
- Time signature: 4/4 throughout.
- Tempo/style: "Flamenco Rock ♩=132". Bar 1 also has "Cup Mute" and "Soli".
- 96 bars. Rehearsal marks: A 10, B 19, C 27, D 35, E 43, F 51, G 59, H 67, I 79, J 89.
- Repeats:
  - Bars 10–18: repeat with a 1st ending at bar 17 and a 2nd at bar 18.
  - Bars 79–88: repeat with a 1st ending at bars 85–86 and a 2nd at bars 87–88.
- One-bar repeat signs (%) and the "(4)" and "(8)" counts are kept exactly as printed. The part has no multi-bar rest numbers.

## Method
1. Zoomed and straightened crops of every system were read by eye. The notes were written into a small text format (`work/build.py`), which produces MusicXML.
2. `build.py` checks that every bar adds up to exactly 4/4. All 96 bars pass.
3. MuseScore imported the MusicXML. `post.py` then set the title frame, boxed texts, page style, tuplet bracket sides and spacing.
4. The PDF was rendered at 200 dpi and compared bar by bar with the photos, system by system, side by side. Differences were fixed and the comparison rerun.
5. No OMR tool was used. The photos are skewed and speckled, so OMR would add little beyond the manual comparison.

## Uncertain or hard-to-read spots
- **Bar 1:** the slur seems to start on the E5 eighth and end on the following E5. Its start point is not fully clear.
- **Bars 3, 25, 49, 95 (and the centre of most systems):** a band of paper speckle runs down the middle of both pages. The noteheads are still readable, but small marks there could be hidden.
- **Bar 7:** the B4 accidental is printed as a cautionary (♮) in parentheses and is reproduced that way.
- **Bars 22, 46, 92:** read as two 16th grace notes (F♯4 G♯4) without a slash.
- **Bar 73:** read as a tie between the C♯5 eighths (C♯5 dotted quarter, C♯5 8th tied to C♯5 8th, D5 8th, E5 marcato). The second C♯5 sits in the speckle band, so this could also be a slur.
- **Bar 77:** a speck in front of the first A4 eighth looks a little like a grace note. I treated it as dirt, to match bars 41 and 65.
- **Bars 87–88:** the photo is tilted and shaded here. The second C♯5 in bar 87 is partly covered by speckle, and the last eighth (G♯4) and bar 88's A4 half note were read from the tilted image.
- **Hairpins (bars 41, 65, 73, 77):** the start and end points are matched to the nearest note, so they are approximate.
- **Boxed texts:** their horizontal positions are approximate. "Solos- Guitar 1st X Accordian 2nd X" is attached at bar 81.

## Editorial choices
- The Sheet Music Plus purchase stamp and watermark are left out. The copyright notice is kept as the page footer.
- The spelling "Accordian" is kept as printed.
- Hand-clap bars retain their original cross noteheads and repeat signs in the Trumpet 2 part. These cues have trumpet playback disabled. A separate **Hand claps (snare)** percussion track now plays the rhythm using General MIDI acoustic snare (note 38, channel 10). The existing Trumpet 2 PDF is unchanged because its notation is unchanged.
- In MusicXML the trumpet clap notes are silent `<cue/>` notes; MuseScore may display imported cues smaller. The native `.mscz` preserves the original full-size cue layout. See [percussion playback and verification](../../docs/feliz-navidad-percussion.md).
- Chord symbols in section I (Bm7, E, A, F♯m, Bm, E, A, F♯m, A, F♯m) are written-pitch names, as printed.
- Small layout differences remain: slur curvature, tuplet bracket length, and exact spacing within each system. In bar 6 the slur from bar 6 to bar 8 passes over the triplet bracket. In the original the slur clears the bracket.
