import time
import jpegdec
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4

# setup display and JPEG encoder
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)
j = jpegdec.JPEG(display)

# create colours
BLACK = display.create_pen(0, 0, 0)
TANGERINE = display.create_pen(255, 142, 114)
TURQ = display.create_pen(80, 201, 206)
MAGENTA = display.create_pen(255, 0, 255)
PINK = display.create_pen(254, 206, 241)
# set font
display.set_font("bitmap8")


def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


def focus():
    clear()
    display.set_pen(TANGERINE)
    display.text("FOCUS", 85, 30, 240, 3)
    j.open_file("focus.jpeg")
    j.decode(0, 80, jpegdec.JPEG_SCALE_FULL)
    display.update()
    time.sleep(2)
    clear()


def shortbreak():
    clear()
    display.set_pen(TURQ)
    display.text("SHORT BREAK", 40, 25, 240, 3)
    j.open_file("shortbreak.jpeg")
    j.decode(0, 70, jpegdec.JPEG_SCALE_FULL)
    display.update()
    time.sleep(2)
    clear()


def longbreak():
    clear()
    display.set_pen(MAGENTA)
    display.text("LONG BREAK", 50, 25, 240, 3)
    j.open_file("longbreak.jpeg")
    j.decode(0, 65, jpegdec.JPEG_SCALE_FULL)
    display.update()
    time.sleep(2)
    clear()


def reset():
    clear()
    display.set_pen(BLACK)
    display.set_pen(PINK)
    display.text("RESETTING", 55, 30, 240, 3)
    display.text("TIMERS", 75, 60, 240, 3)
    j.open_file("reset.jpeg")
    j.decode(0, 100, jpegdec.JPEG_SCALE_FULL)
    display.update()
    time.sleep(5)
    clear()
