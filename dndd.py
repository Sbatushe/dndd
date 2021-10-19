import sys,os
import curses
import random

def draw_menu(stdscr):
    k = 0
    s = ""
    n = 0
    result = "?"
    nresult = 0
    
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Cancella (con backspace)
        if ((k == 263) or (k == 127)):
            s = ""
            result = "?"
        # Invio (lancia il dado)
        elif (k == 10):
            if (int(s)>0):
                nresult = random.randint(1,int(s))
                result = int(nresult)
            else:
                result = "Porco-D"
                s = ""

        # Funzionamento numeri
        n = k-48
        if ((n>=0) and (n<10)):
            s = s+str(n) 

        # Declaration of strings
        title = "Lancia un dado del Pordo-D"[:width-1]
        subtitle = "Scrivi il numero di facce e premi invio"[:width-1]
        keystr = "1D{} = {}".format(s,result)[:width-1]
        statusbarstr = "q -> esci, invio -> lancia, backspsace -> cancella | {}".format(k)[:width-1]
        if k == 0:
            keystr = ""[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
