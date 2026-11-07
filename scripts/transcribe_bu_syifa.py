import subprocess
import os
import imageio_ffmpeg
import speech_recognition as sr
import time

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
audio_in = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\yapp bu sipa bab 3'
full_wav = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\full_16k.wav'
output_txt = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\transcription_yapp_bu_sipa.txt'

print("Converting to 16kHz mono WAV...")
cmd = [ffmpeg_exe, '-y', '-i', audio_in, '-ar', '16000', '-ac', '1', full_wav]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"WAV created: {os.path.getsize(full_wav)} bytes")

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = True

chunk_duration = 20  # seconds
total_duration = 845 # ~14 min 5 sec

results = []
print("Starting chunk transcription...")

with sr.AudioFile(full_wav) as source:
    offset = 0
    while offset < total_duration:
        dur = min(chunk_duration, total_duration - offset)
        try:
            audio = r.record(source, duration=dur)
            text = r.recognize_google(audio, language='id-ID')
            timestamp = f"[{int(offset//60):02d}:{int(offset%60):02d} - {int((offset+dur)//60):02d}:{int((offset+dur)%60):02d}]"
            line = f"{timestamp} {text}"
            print(line)
            results.append(line)
        except sr.UnknownValueError:
            timestamp = f"[{int(offset//60):02d}:{int(offset%60):02d} - {int((offset+dur)//60):02d}:{int((offset+dur)%60):02d}]"
            line = f"{timestamp} [Hening / Tidak terdeteksi]"
            print(line)
            results.append(line)
        except Exception as e:
            print(f"Error at {offset}: {e}")
            time.sleep(1)
        offset += dur

with open(output_txt, 'w', encoding='utf-8') as f:
    f.write("\n".join(results))

print(f"\nFinished! Saved transcription to {output_txt}")

if os.path.exists(full_wav):
    os.remove(full_wav)
