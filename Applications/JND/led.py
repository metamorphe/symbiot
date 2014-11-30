from Tkinter import *

# from http://stackoverflow.com/questions/141855/programmatically-lighten-a-color/141943#141943
def redistribute_rgb(r, g, b):
    threshold = 255.999
    m = max(r, g, b)
    if m <= threshold:
        return int(r), int(g), int(b)
    total = r + g + b
    if total >= 3 * threshold:
        return int(threshold), int(threshold), int(threshold)
    x = (3 * threshold - total) / (3 * m - total)
    gray = threshold - x * m
    return int(gray + x * r), int(gray + x * g), int(gray + x * b)

# from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


# converts to value from 0-125, actuates and returns new value to be set as self.value
def change(value):
    new_value = 255 * value / 1000
    w.create_oval(100, 200, 75, 175, outline="white", fill=rgb_to_hex(redistribute_rgb(255, 255, new_value)))
    return new_value


master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()
#(x0, y0, x1, y1)
w.create_oval(400, 200, 375, 175, outline="white", fill=rgb_to_hex(redistribute_rgb(255, 255, 0)))

mainloop()