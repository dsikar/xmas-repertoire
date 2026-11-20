#!/usr/bin/env python3
"""Render repertoire MusicXML through MuseScore's bundled instrument sounds."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sources = sorted((ROOT / 'pieces').glob('*/*.musicxml'))
    parser.add_argument('--piece', choices=[p.parent.name for p in sources],
                        help='Render only this piece (default: all pieces)')
    parser.add_argument('--musescore', default='musescore', help='MuseScore Studio executable')
    parser.add_argument('--ffmpeg', default='ffmpeg', help='FFmpeg executable with libmp3lame')
    parser.add_argument('--diagnostics', type=Path, help='Keep WAVs, MIDI, imported scores and logs here')
    args = parser.parse_args()
    executable = shutil.which(args.musescore)
    if not executable:
        parser.error(f'MuseScore executable not found: {args.musescore}')
    encoder = shutil.which(args.ffmpeg)
    if not encoder:
        parser.error(f'FFmpeg executable not found: {args.ffmpeg}')
    with tempfile.TemporaryDirectory(prefix='.xmas-audio-', dir=ROOT) as temporary:
        # Isolate settings so local metronome/profile preferences cannot leak
        # into exports, and leave the user's MuseScore preferences untouched.
        config = Path(temporary) / 'config'
        settings = config / 'MuseScore' / 'MuseScore4.ini'
        settings.parent.mkdir(parents=True)
        settings.write_text('[application]\nhasCompletedFirstLaunchSetup=true\n'
                            'playback\\metronomeEnabled=false\n')
        env = dict(os.environ, XDG_CONFIG_HOME=str(config),
                   QT_QPA_PLATFORM=os.environ.get('QT_QPA_PLATFORM', 'offscreen'))
        diagnostics = args.diagnostics.resolve() if args.diagnostics else Path(temporary)
        diagnostics.mkdir(parents=True, exist_ok=True)
        for source in sources:
            if args.piece and source.parent.name != args.piece:
                continue
            destination = source.parent / 'audio' / (source.stem + '.mp3')
            destination.parent.mkdir(exist_ok=True)
            # Export atomically, leaving an existing recording intact on failure.
            rendered = diagnostics / (source.stem + '.mp3')
            # MuseScore enables chord-symbol accompaniment on MusicXML import.
            # Preserve the notated instrumental tracks; omit harmony symbols in
            # the temporary playback copy; keep all notes and score sources intact.
            playback = diagnostics / (source.stem + '.musicxml')
            tree = ET.parse(source)
            for measure in tree.findall('./part/measure'):
                for harmony in measure.findall('harmony'):
                    measure.remove(harmony)
            tree.write(playback, encoding='utf-8', xml_declaration=True)
            wav = diagnostics / (source.stem + '.wav')
            job = diagnostics / (source.stem + '.json')
            job.write_text(json.dumps([{'in': str(playback), 'out': [
                str(wav), str(diagnostics / (source.stem + '.mid')),
                str(diagnostics / (source.stem + '.mscx'))]}], indent=2) + '\n')
            command = [executable, '--sound-profile', 'MuseScore Basic', '-j', str(job)]
            print(f'Rendering {source.relative_to(ROOT)}', flush=True)
            with (diagnostics / (source.stem + '.log')).open('w') as log:
                subprocess.run(command, env=env, stdout=log, stderr=subprocess.STDOUT,
                               check=True, timeout=600)
            # MuseScore exports float WAV. Apply constant gain before the one
            # lossy encode; -6 dB preserves dynamics and leaves MP3 peak headroom.
            with (diagnostics / (source.stem + '-encode.log')).open('w') as log:
                subprocess.run([encoder, '-nostdin', '-y', '-v', 'error', '-i',
                                str(wav), '-af', 'volume=-6dB', '-c:a', 'libmp3lame',
                                '-b:a', '192k', str(rendered)], stdout=log,
                               stderr=subprocess.STDOUT, check=True, timeout=120)
            if not rendered.is_file() or rendered.stat().st_size < 1024:
                raise RuntimeError(f'Missing or empty audio export: {rendered}')
            shutil.copyfile(rendered, destination.with_suffix('.mp3.tmp'))
            destination.with_suffix('.mp3.tmp').replace(destination)
            print(f'  -> {destination.relative_to(ROOT)}', flush=True)


if __name__ == '__main__':
    main()
