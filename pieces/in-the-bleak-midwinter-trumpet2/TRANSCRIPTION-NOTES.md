# In The Bleak Mid-Winter: Trumpet 2 in B♭ transcription notes

## Source
- `images/in-the-bleak-midwinter_trumpet2-in-Bb_page-1.jpg`: one phone photo of the printed part, taken at a slight angle.
- The heading on the page reads: "Trumpet 2 in B♭ / In The Bleak Mid-Winter / Chamber Orchestra / GUSTAV HOLST / arr. for orchestra by JCR © 2004/6".
- A ScoreExchange download stamp at the foot of the page is left out of the edition.

## Files
- `in-the-bleak-midwinter-trumpet2.mscz`: MuseScore 4 (4.7.7) score, single staff, concert pitch off.
- `in-the-bleak-midwinter-trumpet2.musicxml`: exported from the .mscz.
- `parts/in-the-bleak-midwinter-trumpet2.pdf`: 1 page, US Letter. Its 8 systems break at the same bars as the original (printed bars 1, 10, 17, 38, 47, 54, 61, 67).

## Score facts
- **Instrument:** B♭ trumpet. The page says so ("Trumpet 2 in B♭").
- **Key:** written G major (1 sharp), so the concert key is F major.
- **Time signature:** common time (C) throughout.
- **Tempo:** ♩ = 92, "Sostenuto molto". "molto rit." starts at bar 69 and its dashed line runs to the end.
- **Bars:** 73 physical bars, numbered 0–72 to match the printed bar numbers (see the first point under "Uncertain or worth checking").
- **Rehearsal marks:** given in printed numbering.
  - [1] at bar 4, after the opening 4-bar rest.
  - [2] at bar 22, a 16-bar rest covering bars 22–37.
  - [3] at bar 38, a 2-bar rest covering bars 38–39.
  - [4] at bar 40.
  - [5] at bar 57.
- **Repeats:** none. Double barlines follow bars 3, 19, 21, 37, 39 and 56, and a final barline follows bar 72.
- **Dynamics:** only mf at bar 4. No other dynamics are printed.

## Method
- Each system was straightened (the photo is tilted and slightly curved) by fitting the staff lines. I then read every bar by eye, using zoomed crops.
- `work/build.py` writes the MusicXML and asserts that every bar adds up to exactly 4/4. All 73 bars pass.
- MuseScore imported the MusicXML. A post-processing step set the title frame, multi-bar rests, the bar-number offset, spacing and the dashed "molto rit." line.
- I rendered the PDF at 200 dpi and compared it with the straightened photo system by system, side by side. No note differences remain.

## Uncertain or worth checking
- **Bar numbering:** on the page, system 2 is numbered 10, but system 1 holds a 4-bar rest plus 6 bars, which would make it 11. Every later system number (17, 38, 47, 54, 61, 67) agrees with the 10.
  - So the part numbers its first bar as 0. That could be because the full score counts an upbeat or extra bar, or because the multi-bar rest should really read "3".
  - I kept the "4" exactly as printed, and offset the first bar so the displayed numbers match the page. If the rest should really be 3 bars, delete one bar at the start and remove the offset.
- **Bar 56:** reads as G5 (half), then F♯5 (eighth), D5 D5 (16ths), D5 D5 (eighths). The repeated D5s were checked with a zoomed crop and all sit on the D line.
- **Bar 55:** a run of eighths, G4 F♯4 G4 A4 | B4 C5, then D5 (quarter). Clearly printed.
- **Slurs:** I read the F♯4→G4 arcs in bars 18, 20, 54 and 71 and the G4→F♯4 arcs in bars 14 and 66 as slurs, because they join different pitches.
- **F naturals:** bars 12, 48 and 65 have a printed natural on F4, as on the page.
- **Shadows:** a hand or phone shadow covers parts of systems 3–8, but every note was still readable.
