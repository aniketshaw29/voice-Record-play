import sounddevice as sd
import numpy as np

filename = "recording.npy"
fs = 44100 

recording = np.load(filename)
sd.play(recording, fs)
sd.wait()
