import pyaudio
import numpy
import wave
import sys

import math
import itertools
from scipy import interpolate
from operator import itemgetter


CHUNK = 1024
BITRATE = 44100

class Note:

  NOTES = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

  def __init__(self, note, octave=4):
    self.octave = octave
    if isinstance(note, int):
      self.index = note
      self.note = Note.NOTES[note]
    elif isinstance(note, str):
      self.note = note.strip().lower()
      self.index = Note.NOTES.index(self.note)

  def transpose(self, halfsteps):
    octave_delta, note = divmod(self.index + halfsteps, 12)
    return Note(note, self.octave + octave_delta)

  def frequency(self):
    base_frequency = 16.35159783128741 * 2.0 ** (float(self.index) / 12.0)
    return base_frequency * (2.0 ** self.octave)

  def __float__(self):
    return self.frequency()


class Scale:

  def __init__(self, root, intervals):
    self.root = Note(root.index, 0)
    self.intervals = intervals

  def get(self, index):
    intervals = self.intervals
    if index < 0:
      index = abs(index)
      intervals = reversed(self.intervals)
    intervals = itertools.cycle(self.intervals)
    note = self.root
    for i in range(index):
      note = note.transpose(next(intervals))
    return note

  def index(self, note):
    intervals = itertools.cycle(self.intervals)
    index = 0
    x = self.root
    while x.octave != note.octave or x.note != note.note:
      x = x.transpose(next(intervals))
      index += 1
    return index

  def transpose(self, note, interval):
    return self.get(self.index(note) + interval)


def sine(frequency, length, rate):
  length = int(length * rate)
  factor = float(frequency) * (math.pi * 2) / rate
  return numpy.sin(numpy.arange(length) * factor)

def pluck1(note):
  return sine(note.frequency(), 0.1, BITRATE)


p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=BITRATE, output=1)

root = Note('A', 3)
scale = Scale(root, [2, 1, 2, 2, 1, 3, 1])

chunks = []
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(21)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(23)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))
chunks.append(pluck1(scale.get(25)))

chunk = numpy.concatenate(chunks) * 0.25

stream.write(chunk.astype(numpy.float32).tostring())

stream.stop_stream()
stream.close()

p.terminate()

