import pyaudio
import numpy
import KeyInput
import AudioScale


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=AudioScale.BITRATE, output=1)

KeyInput.BindKeyboardInput()


while True:
  if len(KeyInput.buttonsDown) > 0:
    stream.write(AudioScale.GetNoteString(KeyInput.currentNote))



stream.stop_stream()
stream.close()

p.terminate()

