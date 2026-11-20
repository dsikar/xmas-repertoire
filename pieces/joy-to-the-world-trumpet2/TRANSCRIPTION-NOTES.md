# Joy To The World: Trumpet 2 transcription notes

## Source
- `images/joy-to-the-world_trumpet2_page-1.jpg`: one phone photo (1536×2048) of the printed part.
- The heading on the page reads: "TRUMPET 2 / Joy To The World / For Audience & Orchestra / Arranged by TONY ROYSE / © AR Publications '74".
- A ScoreExchange download stamp at the foot of the page is left out of the edition.

## Files
- `joy-to-the-world-trumpet2.mscz`: MuseScore 4 (4.7.7) score, single staff, concert pitch off.
- `joy-to-the-world-trumpet2.musicxml`: exported from the .mscz.
- `parts/joy-to-the-world-trumpet2.pdf`: 1 page, US Letter. Its 8 systems break at the same bars as the original (1, 9, 29, 39, 49, 64, 71, 78).

## Score facts
- **Bars:** 84.
- **Time signature:** 2/4 throughout.
- **Tempo:** "Maestoso", with no metronome mark (none is printed). "rall." at bar 79.
- **Written key:** E major (4 sharps).
- **Transposition (inferred):** the page says only "TRUMPET 2" and does not name the pitch of the trumpet. The score uses a B♭ trumpet, which makes the concert key D major, the usual key for this carol. This is an inference. If the part is really for C trumpet, change the instrument in MuseScore; the written notes stay the same.
- **Rehearsal marks:** [1] at bar 9, [2] at bar 32, [3] at bar 55.
- **Repeats:** none. Double barlines follow bars 8, 31 and 54, and a final barline follows bar 84.
- **Multi-bar rests:** as printed. Bars 9–13 (5), 17–28 (12), 32–36 (5), 40–44 (5), 49–51 (3), 55–61 (7), and a one-bar rest at bar 75 shown with "1" as on the page.
- **Dynamics:** ff at bars 1, 52 and 76. f at bars 14, 29, 37, 45 and 62. A diminuendo hairpin at bar 8.

## Method
- I read zoomed crops of every system by eye, checking pitches against the staff-line positions.
- `work/build.py` writes the MusicXML and asserts that every bar adds up to exactly 2/4. All 84 bars pass.
- MuseScore imported the MusicXML. A post-processing step set the title frame, multi-bar rest style and spacing.
- I rendered the PDF at 200 dpi and compared it with the photo system by system, side by side. No note differences remain.
- No OMR tool was used. The page is clean enough that the bar-by-bar visual comparison is the check.

## Uncertain or worth checking
- **Instrument transposition:** inferred as B♭ (see above). This is the main open point.
- **Bar 37:** the pickup eighth reads as A4, unlike the F♯4 pickup in the parallel bar 14. Both are clearly printed; I flag it only because the two differ.
- **Bar 47:** the last two 16ths (E5 D♯5) have a short arc over them. I read it as a slur.
- **Bar 66:** the staccato dot sits under the last eighth (G♯4) only, as printed.
- **Bar 80:** the second quarter is D♯5 (on the D line, so sharp from the key signature), not C♯5. Checked with a zoomed crop.
- **Bars 70–77 and 78–84:** these are partly in shadow on the photo, but every note was still readable.
- **Pencil marking:** a handwritten mark (") 7" or similar) above bars 16–17 is not part of the printed music and is left out.
