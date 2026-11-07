import speech_recognition as sr
import wave
import numpy as np

wav_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\revisi_bab3_04nov.wav'

with wave.open(wav_path, 'r') as f:
    sr_rate = f.getframerate()
    frames = f.getnframes()
    audio = np.frombuffer(f.readframes(frames), dtype=np.int16)
    dur = frames / sr_rate

r = sr.Recognizer()
r.energy_threshold = 200
r.dynamic_energy_threshold = False

# We'll slice in 7-second chunks with 2-second overlap (step = 5 seconds)
step = 6
chunk_size = 7
offset = 0

detailed_lines = []
print(f"Total duration: {dur:.1f}s. Scanning with step {step}s and chunk {chunk_size}s...")

while offset < dur:
    t_end = min(offset + chunk_size, dur)
    c_bytes = audio[int(offset * sr_rate) : int(t_end * sr_rate)].tobytes()
    
    with wave.open("temp_7s.wav", "w") as fw:
        fw.setnchannels(1)
        fw.setsampwidth(2)
        fw.setframerate(sr_rate)
        fw.writeframes(c_bytes)
        
    try:
        with sr.AudioFile("temp_7s.wav") as src:
            aud = r.record(src)
            text = r.recognize_google(aud, language='id-ID')
            ts = f"[{int(offset//60):02d}:{int(offset%60):02d} - {int(t_end//60):02d}:{int(t_end%60):02d}]"
            print(f"{ts}: {text}")
            detailed_lines.append(f"{ts}: {text}")
    except:
        pass
        
    offset += step

with open(r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\transcription_fine_04nov.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(detailed_lines))

print("Fine-grained transcription saved!")
