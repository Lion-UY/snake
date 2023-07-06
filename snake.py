import curses
import time
import random

def get_key() -> int:
    lstkey = -2
    key = -2
    while key != -1:
        lstkey = key
        key = stdscr.getch()
    return lstkey

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(True)

map_size = (10, 10)
dire = 'Right' # 'Up' 'Down' 'Left' 'Right'
snake = [(3, 5), (3, 4), (3, 3)]

#generate apple
apple_x = random.randint(0,10)
apple_y = random.randint(0,10)
apple = [(apple_x,apple_y)]
if apple in snake:
    apple_x = random.randint(0,10)
    apple_y = random.randint(0,10)

#control the snake
if key == "a" 


while True:
    key = chr(get_key())
    if key in "asdw":
        turn(key)
        status = do_move()
        if status == 'crash':
            gameover()
    pretty_print()
    time.sleep(0.5)