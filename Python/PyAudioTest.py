import pyaudio
import numpy
import wave
import sys

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)

stream.stop_stream()
stream.close()

p.terminate()

