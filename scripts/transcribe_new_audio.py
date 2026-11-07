import subprocess
import os
import imageio_ffmpeg
import speech_recognition as sr
import wave
import contextlib
import numpy as np
import scipy.signal

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
audio_in = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\Revisi Bab 3 20261104-144937.m4a.mpeg'
wav_out = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\revisi_bab3_04nov.wav'

print("Normalizing audio and converting to 16kHz mono WAV...")
cmd = [
    ffmpeg_exe, '-y', '-i', audio_in,
    '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
    '-ar', '16000', '-ac', '1', wav_out
]
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"Normalized WAV created: {os.path.getsize(wav_out)} bytes")

with contextlib.closing(wave.open(wav_out, 'r')) as f:
    frames = f.getnframes()
    sr_rate = f.getframerate()
    audio_data = np.frombuffer(f.readframes(frames), dtype=np.int16)
    duration = frames / float(sr_rate)

print(f"Total audio duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")

def estimate_pitch(segment, sr_rate):
    if len(segment) < sr_rate * 0.05:
        return 0
    corr = scipy.signal.correlate(segment, segment, mode='full')
    corr = corr[len(corr)//2:]
    min_lag = int(sr_rate / 350)
    max_lag = int(sr_rate / 75)
    if max_lag >= len(corr):
        return 0
    peak = min_lag + np.argmax(corr[min_lag:max_lag])
    return sr_rate / peak

r = sr.Recognizer()
r.energy_threshold = 150
r.dynamic_energy_threshold = True

chunk_size = 12
offset = 0
dialogue = []

print("Transcribing in chunks with speaker identification...")

while offset < duration:
    dur = min(chunk_size, duration - offset)
    start_frame = int(offset * sr_rate)
    end_frame = int((offset + dur) * sr_rate)
    chunk = audio_data[start_frame:end_frame]
    
    # Calculate pitch in chunk
    frame_len = int(sr_rate * 0.1)
    pitches = []
    for i in range(0, len(chunk) - frame_len, frame_len):
        f_sub = chunk[i:i+frame_len]
        p = estimate_pitch(f_sub, sr_rate)
        if 75 < p < 350:
            pitches.append(p)
    med_p = np.median(pitches) if len(pitches) > 0 else 0
    speaker = "Bu Syifa (Dosen)" if med_p >= 165 else ("Mahasiswa (User)" if med_p > 75 else "Tak tentu")
    
    temp_wav = "temp_nov_chunk.wav"
    with wave.open(temp_wav, "w") as fw:
        fw.setnchannels(1)
        fw.setsampwidth(2)
        fw.setframerate(sr_rate)
        fw.writeframes(chunk.tobytes())
        
    text = ""
    with sr.AudioFile(temp_wav) as src:
        try:
            a = r.record(src)
            text = r.recognize_google(a, language='id-ID')
        except:
            pass
            
    if os.path.exists(temp_wav):
        os.remove(temp_wav)
        
    ts = f"[{int(offset//60):02d}:{int(offset%60):02d} - {int((offset+dur)//60):02d}:{int((offset+dur)%60):02d}]"
    if text:
        line = f"{ts} [{speaker} | {med_p:.1f} Hz]: {text}"
        print(line)
        dialogue.append(line)
    else:
        line = f"{ts} [{speaker} | {med_p:.1f} Hz]: [Hening / Tidak terdeteksi]"
        print(line)
        dialogue.append(line)
        
    offset += dur

out_txt = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\transcription_revisi_04nov.txt'
with open(out_txt, 'w', encoding='utf-8') as f:
    f.write("\n".join(dialogue))

print(f"Transcription complete! Saved to {out_txt}")
