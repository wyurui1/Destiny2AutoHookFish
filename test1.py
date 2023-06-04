import keyboard
import pyautogui
import time
from io import BytesIO
from PIL import ImageGrab
from easyocr import easyocr

if __name__ == '__main__':
  is_running = False
  restart_key = 'j'
  pause_key = 'p'
  exit_key = 'k'
  reader = easyocr.Reader(['ch_sim'])

  def on_key_press(event):
    global is_running

    if event.name == restart_key and not is_running:
      is_running = True
      print('start!')
    elif event.name == pause_key and is_running:
      is_running = False
      print('stop!')
    elif event.name == exit_key:
      keyboard.unhook_all()
      exit(0)

  keyboard.on_press(on_key_press)

  while True:
    while is_running:
      screen  = BytesIO()
      img = ImageGrab.grab()
      time.sleep(0.03)
      img.crop([870, 710, 1120, 760]).save(screen, format='PNG')
      
      result = reader.readtext(screen.getvalue())
      img.close()
      screen.close()

      for line in result:
        text = line[1]
        if text:
          pyautogui.keyDown('f')
          time.sleep(1)
          pyautogui.keyUp('f')
        break
      pass

    while not is_running:
      event = keyboard.read_event()
      if event.name == restart_key:
        is_running = True
        break
