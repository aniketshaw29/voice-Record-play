#pip install numpy
#pip install sounddevice

import sounddevice as sd
import numpy as np

def record_audio(filename, duration, fs, channels):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    np.save(filename, recording)

filename = "recording.npy"
duration = 5 # in seconds
fs = 44100 # sample rate in Hz
channels = 2 # number of channels

record_audio(filename, duration, fs, channels)
