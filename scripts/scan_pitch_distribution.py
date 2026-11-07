import wave
import numpy as np
import scipy.signal

wav_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\RevisiAudio\full_norm.wav'

with wave.open(wav_path, 'r') as f:
    sr_rate = f.getframerate()
    audio = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16)

# Let's inspect energy and pitch across 1-second windows throughout the entire 14 minutes
window = sr_rate * 1 # 1 second
n_windows = len(audio) // window

print(f"Total 1s windows: {n_windows}")

# Let's collect pitch where energy is significant
pitches = []
times = []

for i in range(n_windows):
    chunk = audio[i*window : (i+1)*window]
    rms = np.sqrt(np.mean(chunk.astype(np.float32)**2))
    if rms > 500: # Active voice
        # Autocorrelation
        corr = scipy.signal.correlate(chunk, chunk, mode='full')
        corr = corr[len(corr)//2:]
        min_lag = int(sr_rate / 350) # up to 350 Hz
        max_lag = int(sr_rate / 70)  # down to 70 Hz
        if max_lag < len(corr):
            peak = min_lag + np.argmax(corr[min_lag:max_lag])
            p = sr_rate / peak
            pitches.append(p)
            times.append(i)

pitches = np.array(pitches)
times = np.array(times)

print(f"Voiced windows: {len(pitches)}")
print(f"Pitch percentiles: 10%={np.percentile(pitches, 10):.1f}, 50%={np.median(pitches):.1f}, 90%={np.percentile(pitches, 90):.1f}")
print(f"Pitch min={np.min(pitches):.1f}, max={np.max(pitches):.1f}")

# Histogram of pitches
hist, bin_edges = np.histogram(pitches, bins=20, range=(70, 350))
for b, h in zip(bin_edges, hist):
    print(f"{b:.1f} - {b+(bin_edges[1]-bin_edges[0]):.1f} Hz: {h} windows")
