#!/usr/bin/python


#Import Relavent Libraries
import curses               #For CL GUI
import bluetooth            #Communicate over Bluetooth
import time                 #For getting current time
import RPi.GPIO as GPIO     #Get GPIO pins for Pins


GPIO.setmode(GPIO.BOARD)    #Set GPIO Pins to board


#Import Device names and hardware IDs
keyDat = open('keyDat.txt','r')     #Open the device file in read only mode
devices = {}                        #Place holder dictionary for device names and hardware IDs (keys and values)

for line in keyDat:                 #The following for loop sets name:ID pairs in the devices dict
        (key, val)= line.split()
        devices[key]= val


keyDat.close()                      #Close keydat file

names = list(devices.keys())        #Create an ordered list of names
ids = list(devices.values())        #Create an ordered list of IDs 

'''
#CL GUI definition
def main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    while True:
    # Clear screen
        stdscr.clear()

        NumDevices=len(names)
        stdscr.addstr(1,1,str("In/Out Board"))
        stdscr.addstr(2,1,str("Last checked on " + time.strftime("%a, %d %b %Y %H:%M:%S local time.", time.localtime())))
        for jj in range (0,NumDevices):
            result = bluetooth.lookup_name(ids[jj], timeout=5)
            if (result != None):
                stdscr.addstr(jj+3,1,str("%s is: in" %names[jj]),curses.color_pair(2))
            else:
                stdscr.addstr(jj+3,1,str("%s is: out" %names[jj]),curses.color_pair(1))
        stdscr.refresh()
        stdscr.getkey()
#        time.sleep(30)
curses.wrapper(main)
'''

while True:
        NumDevices=len(names)
        printlist=["fill"]*NumDevices
        print("In/Out Board \n Last checked on " + time.strftime("%a, %d %b %Y %H:%M:%S local time.", time.localtime()))
        for jj in range (0,NumDevices):
            result = bluetooth.lookup_name(ids[jj], timeout=5)
            if (result != None):
                printlist[jj]=("%s is: in" %(names[jj]))
            else:
                printlist[jj]=("%s is: out" %(names[jj]))
        
        for ii in printlist:
            print ii

        print "\r \r \r \r"






