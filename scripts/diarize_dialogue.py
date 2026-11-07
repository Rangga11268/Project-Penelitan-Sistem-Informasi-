import wave
import numpy as np
import scipy.signal
import speech_recognition as sr
import os

wav_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\full_norm.wav'

with wave.open(wav_path, 'r') as f:
    sr_rate = f.getframerate()
    audio = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16)

window = sr_rate * 1 # 1s
n_windows = len(audio) // window

def estimate_pitch_1s(chunk, sr_rate):
    corr = scipy.signal.correlate(chunk, chunk, mode='full')
    corr = corr[len(corr)//2:]
    min_lag = int(sr_rate / 350)
    max_lag = int(sr_rate / 70)
    if max_lag >= len(corr):
        return 0
    peak = min_lag + np.argmax(corr[min_lag:max_lag])
    return sr_rate / peak

# Classify each second: 'User' (male, pitch < 160) or 'Bu Syifa' (female, pitch >= 170) or 'Silence/Ambiguous'
speaker_sec = []
for i in range(n_windows):
    chunk = audio[i*window : (i+1)*window]
    rms = np.sqrt(np.mean(chunk.astype(np.float32)**2))
    if rms < 400:
        speaker_sec.append('Silence')
    else:
        p = estimate_pitch_1s(chunk, sr_rate)
        if p >= 175:
            speaker_sec.append('Bu Syifa')
        elif 70 <= p <= 155:
            speaker_sec.append('User')
        else:
            speaker_sec.append('User' if p < 165 else 'Bu Syifa')

# Now group consecutive seconds of the same speaker
segments = []
curr_spk = speaker_sec[0]
start_t = 0

for t in range(1, len(speaker_sec)):
    spk = speaker_sec[t]
    if spk != curr_spk:
        if curr_spk != 'Silence' and (t - start_t) >= 2: # At least 2 seconds
            segments.append((start_t, t, curr_spk))
        curr_spk = spk
        start_t = t

if curr_spk != 'Silence' and (len(speaker_sec) - start_t) >= 2:
    segments.append((start_t, len(speaker_sec), curr_spk))

print(f"Total speech segments detected: {len(segments)}")

# Let's transcribe and print out the dialogue
r = sr.Recognizer()
dialogue = []

for start_t, end_t, spk in segments:
    # Extract audio chunk
    start_frame = int(start_t * sr_rate)
    end_frame = int(end_t * sr_rate)
    chunk = audio[start_frame:end_frame]
    
    # Save temp wav
    temp_wav = "temp_turn.wav"
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
        
    if text:
        ts = f"[{int(start_t//60):02d}:{int(start_t%60):02d} - {int(end_t//60):02d}:{int(end_t%60):02d}]"
        line = f"{ts} **{spk}**: {text}"
        print(line)
        dialogue.append(line)

with open(r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\dialogue_diarized.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(dialogue))

print("Dialogue diarization complete!")
