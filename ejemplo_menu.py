'''
----------------------------------
#Developed by                     |
@user: Dennis Masaya              |
#id: 201503413                    |
#e-mail: dennismasaya@gmail.com   |
#blog: dennismasaya.com           |
----------------------------------
This example demonstrates how to build a simple curses
application that displays a Menu, every option can be
selected and will take you to and empty screen that you
will be able to get out and return to the Main Menu by
pressing the [ESC] key.
'''

import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,21, '1. Play')             #paint option 1
    win.addstr(8,21, '2. Scoreboard')       #paint option 2
    win.addstr(9,21, '3. User Selection')   #paint option 3
    win.addstr(10,21, '4. Reports')         #paint option 4
    win.addstr(11,21, '5. Bulk Loading')    #paint option 5
    win.addstr(12,21, '6. Exit')            #paint option 6
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()


stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        paint_title(window, ' PLAY ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' BULK LOADING ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state