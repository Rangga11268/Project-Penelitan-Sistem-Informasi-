import wave
import numpy as np
import scipy.signal
import speech_recognition as sr

wav_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\full_norm.wav'

with wave.open(wav_path, 'r') as f:
    sr_rate = f.getframerate()
    audio_data = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16)

def get_pitch(segment, sr_rate):
    # Autocorrelation based pitch estimation
    # segment is 1D numpy array
    if len(segment) < sr_rate * 0.05:
        return 0
    # Center clip
    corr = scipy.signal.correlate(segment, segment, mode='full')
    corr = corr[len(corr)//2:]
    
    # Pitch search range: 80 Hz (male low) to 300 Hz (female high)
    min_lag = int(sr_rate / 320)
    max_lag = int(sr_rate / 75)
    
    if max_lag >= len(corr):
        return 0
    
    peak_lag = min_lag + np.argmax(corr[min_lag:max_lag])
    pitch = sr_rate / peak_lag
    return pitch

# Check timestamps of the key parts from transcription
# Let's inspect intervals:
# 0:00 - 0:45
# 0:45 - 1:30
# 2:15 - 3:15
# 4:10 - 4:45
# 7:45 - 9:45
# 9:45 - 11:30
# 11:30 - 14:00

intervals = [
    (0, 15), (15, 30), (30, 45), (45, 60), (60, 75), (75, 90),
    (130, 150), (150, 170), (170, 195),
    (240, 270), (270, 300),
    (580, 605), (605, 630), (630, 660), (660, 690), (690, 720),
    (720, 750), (750, 780), (780, 810), (810, 840)
]

r = sr.Recognizer()

print("Analyzing speaker pitch and turns...")
for start_s, end_s in intervals:
    start_frame = int(start_s * sr_rate)
    end_frame = int(end_s * sr_rate)
    chunk = audio_data[start_frame:end_frame]
    
    # Calculate pitches across 100ms frames
    frame_len = int(sr_rate * 0.1)
    pitches = []
    for i in range(0, len(chunk) - frame_len, frame_len):
        f = chunk[i:i+frame_len]
        p = get_pitch(f, sr_rate)
        if 75 < p < 350:
            pitches.append(p)
            
    median_pitch = np.median(pitches) if len(pitches) > 0 else 0
    speaker = "Bu Syifa (Dosen)" if median_pitch > 165 else ("Mahasiswa (User)" if median_pitch > 80 else "Tak tentu")
    
    # Also transcribe
    with wave.open("temp_chunk.wav", "w") as fw:
        fw.setnchannels(1)
        fw.setsampwidth(2)
        fw.setframerate(sr_rate)
        fw.writeframes(chunk.tobytes())
        
    text = ""
    with sr.AudioFile("temp_chunk.wav") as src:
        try:
            a = r.record(src)
            text = r.recognize_google(a, language='id-ID')
        except:
            pass
            
    if text:
        ts = f"[{int(start_s//60):02d}:{int(start_s%60):02d} - {int(end_s//60):02d}:{int(end_s%60):02d}]"
        print(f"{ts} [Pitch: {median_pitch:.1f} Hz -> {speaker}]: {text}")
