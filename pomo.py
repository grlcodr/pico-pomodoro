import time
import prog
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

GREEN = display.create_pen(0, 255, 0)


while True:
    if button_a.read():
        prog.focus()
    elif button_b.read():
        prog.shortbreak()
    elif button_x.read():
        prog.longbreak()
    elif button_y.read():
        prog.reset()
    else:
        display.set_pen(GREEN)
        display.text("Press A to start", 10, 10, 240, 4)
        display.update()
        time.sleep(0.05)
