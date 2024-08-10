from pynput import mouse
from time import time
from tkinter import *




tickrate = 60
WIDTH = 800
RWIDTH = 38
RWSPACE = 2
RHEIGHT = 23
RHSPACE = 2

delta = 0.15
MAXLINES = 16


BACKGROUND_COLOR = "#000000"
MISS_COLOR = "#ff3030"
PERFECT_COLOR = "#0070ff"
OK_COLOR = "#d0d000"
BAD_INPUT_COLOR = "#ff9000"


def importCfg():
    global RWIDTH, RWSPACE, RHEIGHT, RHSPACE
    global delta, MAXLINES
    global MISS_COLOR, PERFECT_COLOR, OK_COLOR, BAD_INPUT_COLOR, BACKGROUND_COLOR
    f = open("settings.cfg")
    for line in f.readlines():
        cur_line = line.split("=")
        param = cur_line[0].rstrip()
        value = cur_line[1].lstrip().rstrip()
        match param:
            case "Rectangle Width":
                RWIDTH = int(value)
            case "Rectangle Height":
                RHEIGHT = int(value)
            case "Rectangle Width Gap":
                RWSPACE = int(value)
            case "Rectangle Height Gap":
                RHSPACE = int(value)
            case "Scroll Reset Time":
                delta = float(value)
            case "Max Lines":
                MAXLINES = int(value)
            case "Window Width":
                WIDTH = int(value)
            case "Background Color":
                BACKGROUND_COLOR = value
            case "Pefrect Input Color":
                PERFECT_COLOR = value
            case "Miss Input Color":
                MISS_COLOR = value
            case "Ok Input Color":
                OK_COLOR = value
            case "Bad Input Clor":
                BAD_INPUT_COLOR = value
                
    
HEIGHT = (RHEIGHT + RHSPACE) * (MAXLINES + 2)

def calculateCoords(line, pos):
    x1 = pos * (RWIDTH + RWSPACE) + RWSPACE
    x2 = x1 + RWIDTH
    y1 = line * (RHEIGHT + RHSPACE) + RHSPACE
    y2 = y1 + RHEIGHT
    return (x1, y1, x2, y2)

last_scroll = time()
first_scroll = time()
tick_time = time()

counter = 0


cur_line = 0


rectangles = [[] for i in range(MAXLINES + 1)]
def on_scroll(event):
    global counter, last_scroll, first_scroll, tick_time, canv, cur_line, rectangles
    cur_time = time()
    
    cur_ticks = 0
    while cur_time > tick_time:
        tick_time += 1 / tickrate
        cur_ticks += 1
    
    if cur_time-last_scroll < delta:
        counter += 1
    else:
        counter = 1
        first_scroll = time()
        cur_line += 1
        if cur_line > MAXLINES:
            cur_line -= MAXLINES
        clear_line = cur_line + 2
        if clear_line > MAXLINES:
            clear_line -= MAXLINES
        for elem in rectangles[clear_line]:
            canv.delete(elem)
        rectangles[clear_line] = []
    prev_scroll = last_scroll
    last_scroll = cur_time
    if counter > 1:
        cur_color = "black"
        if cur_ticks <= 1:
            #print ("MISS", end = ' ')
            cur_color = MISS_COLOR #red
        elif cur_ticks == 2:
            #print("PRF", end = '  ')
            cur_color = PERFECT_COLOR #light blue
        elif cur_ticks == 3:
            #print(cur_ticks - 1, end = "    ")
            cur_color = OK_COLOR #yellow
        else:
            #print(cur_ticks - 1, end = "    ")
            cur_color = BAD_INPUT_COLOR #orange
        #print(round(1 / (last_scroll - prev_scroll), 1), "cps", end = ' ')
        #print(round(counter / (last_scroll - first_scroll), 1), "current scroll average")

        
        x1, y1, x2, y2 = calculateCoords(cur_line, counter - 1)
        rectangles[cur_line].append(canv.create_rectangle(x1, y1, x2, y2, fill=cur_color, outline=cur_color))
        canv.update()

importCfg()
root = Tk()


canv = Canvas(root, width = WIDTH, height=HEIGHT, bg = BACKGROUND_COLOR)
canv.pack()



canv.bind("<MouseWheel>", on_scroll)

root.mainloop()





