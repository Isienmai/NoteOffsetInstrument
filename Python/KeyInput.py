import keyboard

currentNote = 30
buttonsDown = []

def OnKeyPressed(keyboardEvent):
  global currentNote
  global buttonsDown
  
  if keyboardEvent.name not in buttonsDown:
    buttonsDown.append(keyboardEvent.name)
  else:
    return
    
  if keyboardEvent.name == 'q':
    currentNote = currentNote + 1
  elif keyboardEvent.name == 'a':
    currentNote = currentNote - 1
  elif keyboardEvent.name == 'w':
    currentNote = currentNote + 2
  elif keyboardEvent.name == 's':
    currentNote = currentNote - 2
  elif keyboardEvent.name == 'e':
    currentNote = currentNote + 3
  elif keyboardEvent.name == 'd':
    currentNote = currentNote - 3
  elif keyboardEvent.name == 'r':
    currentNote = currentNote + 4
  elif keyboardEvent.name == 'f':
    currentNote = currentNote - 4
  elif keyboardEvent.name == 't':
    currentNote = currentNote + 5
  elif keyboardEvent.name == 'g':
    currentNote = currentNote - 5
  elif keyboardEvent.name == 'y':
    currentNote = currentNote + 6
  elif keyboardEvent.name == 'h':
    currentNote = currentNote - 6
  elif keyboardEvent.name == 'space':
    currentNote = currentNote
  
  if currentNote < 0:
    currentNote = 0
  if currentNote > 100:
    currentNote = 100

def OnKeyReleased(keyboardEvent):
  global buttonsDown
  
  if keyboardEvent.name in buttonsDown:
    buttonsDown.remove(keyboardEvent.name)

def BindKeyboardInput():
  keyboard.on_press(OnKeyPressed)
  keyboard.on_release(OnKeyReleased)