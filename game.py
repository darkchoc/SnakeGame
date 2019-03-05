'''
Original code and direction taken from : https://www.youtube.com/watch?v=rbasThWVb-c

Made changes to make game better

'''

import random
import curses
import time

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
sh = sh/2
sw = sw/3
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
timeout_val=100
w.timeout(timeout_val)

for y in [1,sh-2]:
        for x in range(1, sw-1):
                w.addch(y,x, curses.ACS_DIAMOND)
for x in [1, sw-2]:
        for y in range(1, sh-1):
                w.addch(y,x, curses.ACS_DIAMOND)

snk_x = sw/4
snk_y = sh/2

snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x+1]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
total = 0

while True:
        prev_key = key
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if prev_key == curses.KEY_DOWN and key ==curses.KEY_UP:
                key = curses.KEY_DOWN
        elif prev_key == curses.KEY_UP and key == curses.KEY_DOWN:
                key = curses.KEY_UP
        elif prev_key == curses.KEY_RIGHT and key == curses.KEY_LEFT:
                key = curses.KEY_RIGHT
        elif prev_key == curses.KEY_LEFT and key == curses.KEY_RIGHT:
                key = curses.KEY_LEFT

        if snake[0] in snake[1:]:
                w.addstr(0, sw/3, "Your score is: " + str(total))
                w.refresh()
                time.sleep(3)
                curses.endwin()
                quit()


        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
                new_head[0] += 1
        if key == curses.KEY_UP:
                new_head[0] -= 1
        if key == curses.KEY_RIGHT:
                new_head[1] += 1
        if key == curses.KEY_LEFT:
                new_head[1] -= 1

        if new_head[0] == 1:
                new_head[0] = sh-3
        if new_head[0] == sh-2:
                new_head[0] = 2
        if new_head[1] == 1:
                new_head[1] = sw-3
        if new_head[1] == sw-2:
                new_head[1] = 2

        snake.insert(0, new_head)

        if snake[0] == food:
                total = total + 1
                if total%5 == 0 and timeout_val > 20:
                        timeout_val -= 10
                        w.timeout(timeout_val)

                food = None
                while food is None:
                        nf = [
                                random.randint(2, sh-3),
                                random.randint(2, sw-3)
                        ]
                        food = nf if nf not in snake else None
                w.addch(food[0],food[1], curses.ACS_PI)
        else:
                tail = snake.pop()
                w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
