import numpy
import math
import itertools
from scipy import interpolate
from operator import itemgetter


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


class Scale:

  def __init__(self, root, intervals):
    self.root = Note(root.index, 0)
    self.intervals = intervals

  def get(self, index):
    if index < 0:
      index = abs(index)
    intervals = itertools.cycle(self.intervals)
    note = self.root
    for i in range(index):
      note = note.transpose(next(intervals))
    return note


def sine(frequency, length):
  length = int(length * BITRATE)
  factor = float(frequency) * (math.pi * 2) / BITRATE
  return numpy.sin(numpy.arange(length) * factor)

def pluck1(note):
  return sine(note.frequency(), 1 / note.frequency())

def GetNoteString(noteIndex):
  global scale
  return pluck1(scale.get(noteIndex)).astype(numpy.float32).tostring()

scale = Scale(Note('C', 3), [2, 2, 1, 2, 2, 2, 1])