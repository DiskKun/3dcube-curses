import math
import curses
import time
from curses import wrapper
stdscr=curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
c="█"
vectors={} 
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)
    def defineVectors():
        global vectors
        vectors={
        
        "1":[-10, -10, -10],
               
        "2":[-10, -10, 10],
       
        "3":[-10, 10, -10],
       
        "4":[-10, 10, 10],
       
        "5":[10, -10, -10],
       
        "6":[10, -10, 10],
       
        "7":[10, 10, -10],
       
        "8":[10, 10, 10]
       
        }
        global linepoints
        linepoints = {
            "1":[0, 0],
            "2":[0, 0],
            "3":[0, 0],
            "4":[0, 0],
            "5":[0, 0],
            "6":[0, 0],
            "7":[0, 0],
            "8":[0, 0]
        }

    ax=0
    ay=0
    az=0
    ex=False
    ey=False
    ez=False
    defineVectors()
    i=1
    while True:
        for key in vectors:
            # X
            rotatedy=math.cos(math.radians(ax))*vectors[key][1]-math.sin(math.radians(ax))*vectors[key][2]
            rotatedz=math.sin(math.radians(ax))*vectors[key][1]+math.cos(math.radians(ax))*vectors[key][2]
            # Y
            prerotz = rotatedz
            rotatedx=math.cos(math.radians(ay))*vectors[key][0]+math.sin(math.radians(ay))*prerotz
            rotatedz=-math.sin(math.radians(ay))*vectors[key][0]+math.cos(math.radians(ay))*prerotz
            # Z
            prerotx = rotatedx
            preroty = rotatedy
            rotatedx=math.cos(math.radians(az))*rotatedx-math.sin(math.radians(az))*preroty
            rotatedy=math.sin(math.radians(az))*prerotx+math.cos(math.radians(az))*preroty
            
            linepoints[key][0] = rotatedx
            linepoints[key][1] = rotatedy
            if key == "1":
                stdscr.addch(int(rotatedy+20), int(rotatedx+20), c, curses.color_pair(1))
            else:   
                stdscr.addch(int(rotatedy+20), int(rotatedx+20), c)
        drawLine(linepoints["1"][0]+20, linepoints["1"][1]+20, linepoints["2"][0]+20, linepoints["2"][1]+20)
        drawLine(linepoints["2"][0]+20, linepoints["2"][1]+20, linepoints["4"][0]+20, linepoints["4"][1]+20)
        drawLine(linepoints["3"][0]+20, linepoints["3"][1]+20, linepoints["4"][0]+20, linepoints["4"][1]+20)
        drawLine(linepoints["3"][0]+20, linepoints["3"][1]+20, linepoints["1"][0]+20, linepoints["1"][1]+20)
        drawLine(linepoints["8"][0]+20, linepoints["8"][1]+20, linepoints["6"][0]+20, linepoints["6"][1]+20)
        drawLine(linepoints["5"][0]+20, linepoints["5"][1]+20, linepoints["6"][0]+20, linepoints["6"][1]+20)
        drawLine(linepoints["5"][0]+20, linepoints["5"][1]+20, linepoints["7"][0]+20, linepoints["7"][1]+20)
        drawLine(linepoints["7"][0]+20, linepoints["7"][1]+20, linepoints["8"][0]+20, linepoints["8"][1]+20)
        drawLine(linepoints["1"][0]+20, linepoints["1"][1]+20, linepoints["5"][0]+20, linepoints["5"][1]+20)
        drawLine(linepoints["6"][0]+20, linepoints["6"][1]+20, linepoints["2"][0]+20, linepoints["2"][1]+20)
        drawLine(linepoints["7"][0]+20, linepoints["7"][1]+20, linepoints["3"][0]+20, linepoints["3"][1]+20)
        drawLine(linepoints["4"][0]+20, linepoints["4"][1]+20, linepoints["8"][0]+20, linepoints["8"][1]+20)
        stdscr.refresh()
        time.sleep(.01)
        keyin = stdscr.getch()
        if keyin==120:
            if ex==False:
                ex=True
            else:
                ex=False
        elif keyin==121:
            if ey==False:
                ey=True
            else:
                ey=False
        elif keyin==122:
            if ez==False:
                ez=True
            else:
                ez=False
        elif keyin==32:
            ay, ax, az = 0, 0, 0
        if ex==True:
            ax+=i
        if ey==True:
            ay+=i
        if ez==True:
            az+=i
        stdscr.clear()
        stdscr.addstr(40, 0, str(ax)+" "+str(ay)+" "+str(az))

def drawLine(x1, y1, x2, y2):
    if x1-x2==0:
        y=y2 if y1>y2 else y1
        for t in range(int(round(abs(y1-y2)))):
            stdscr.addstr(int(round(t+y)), int(round(x1)), c)
    elif x1<x2:
        m=(y2-y1)/(x2-x1)
        for t in range(int(round(x2-x1))):
            stdscr.addstr(int(round(m*t+y1)), int(round(t+x1)), str(c))           
    else:
        m=(y1-y2)/(x1-x2)
        for t in range(int(round(x1-x2))):
            stdscr.addstr(int(round(m*t+y2)), int(round(t+x2)), str(c))
 
def terminate():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
wrapper(main)

