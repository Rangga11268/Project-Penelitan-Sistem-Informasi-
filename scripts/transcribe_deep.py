import subprocess
import os
import imageio_ffmpeg
import speech_recognition as sr
import wave
import contextlib

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
audio_in = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\yapp bu sipa bab 3'
full_wav = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\full_norm.wav'

print("Normalizing audio and converting to 16kHz mono WAV...")
# We use loudnorm filter to boost soft voices!
cmd = [
    ffmpeg_exe, '-y', '-i', audio_in,
    '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
    '-ar', '16000', '-ac', '1', full_wav
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"Normalized WAV created: {os.path.getsize(full_wav)} bytes")

# Get duration
with contextlib.closing(wave.open(full_wav, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
print(f"Total audio duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")

r = sr.Recognizer()
r.energy_threshold = 150  # Lower threshold for sensitivity
r.dynamic_energy_threshold = True

# We'll transcribe in 12-second chunks with 2-second overlap, or 15-second chunks
chunk_size = 15
step = 13
offset = 0

transcripts = []

with sr.AudioFile(full_wav) as source:
    while offset < duration:
        dur = min(chunk_size, duration - offset)
        if dur < 2:
            break
        # Read from source at offset
        source_chunk = r.record(source, duration=dur)
        # To handle seek, AudioFile advances sequentially.
        # So sequential 15s chunks without overlap first:
        try:
            text = r.recognize_google(source_chunk, language='id-ID')
            timestamp = f"[{int(offset//60):02d}:{int(offset%60):02d} - {int((offset+dur)//60):02d}:{int((offset+dur)%60):02d}]"
            res = f"{timestamp} {text}"
            print(res)
            transcripts.append(res)
        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"Error at {offset}: {e}")
        offset += dur

out_file = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\transcription_detailed.txt'
with open(out_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(transcripts))

print(f"Saved detailed transcript to {out_file}")
