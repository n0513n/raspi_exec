#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple script used to listen for changes in
a specific GPIO portand send commands through
SSH to be executed by a remote server.
"""

from __future__ import print_function

import RPi.GPIO as GPIO

from os.path import isfile
from subprocess import Popen, check_output
from time import time, sleep

__git__ = 'https://github.com/n0513n/raspi_exec'

# Try and import from file
if isfile('config.py'):
    print('Importing settings from "config.py"...')
    from config import *

def start_script():
    '''
    Keep watching for changes in the specified port.
    '''
    # Identify if running for the first time
    started = False

    # Before is a BOOLEAN state by default turned off
    before = False

    # Make sure the CMD_CHECK condition has been matched first
    check = False

    # Store start timestamp for later
    tstamp = time()

    # Ignore warning for now
    GPIO.setwarnings(False)

    # Use physical pin numbering
    GPIO.setmode(GPIO.BOARD)

    # Set pin PORT to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Start watching for changes on specified port
    print("Listening on GPIO port "+str(PORT)+" every "+str(WAIT)+" seconds...")

    while True: # keep running

      try: # ignore errors

        if CMD_CHECK:

            cond1 = (started == False or RECHECK)
            cond2 = (time()-tstamp >= RECHECK)

            if cond1 or cond2:

                if check_command(CMD_CHECK) == False:
                    started = False
                    while not started:
                        send_command(CMD_START, bg=True); sleep(1)
                        started = check_command(CMD_CHECK)
                    send_command(CMD_FOCUS); sleep(0.25)
                    send_command(CMD_ABOVE); sleep(0.25)
                    send_command(CMD) if DEFAULT else None

                tstamp = time()
                started = True

        now = GPIO.input(PORT)

        if (now != before):
            send_command(CMD); sleep(0.25)

        before = now
        sleep(WAIT)

      except Exception as e:
        #raise # <-- uncomment line if bug-hunting!
        print(str(e))
        sleep(WAIT)

def check_command(cmd, bg=False, quiet=False):
    '''
    Checks command output and optionally performs action.
    '''
    output = send_command(cmd, bg=bg)

    if isinstance(output, bytes): # Python3
        output = output.decode('utf8', 'ignore')

    try:    output = int(output) # True or False
    except: output = str(output) # 0==False, 1>=True

    cond_false = isinstance(output, str) and output.startswith("False")
    cond_true  = isinstance(output, str) and output.startswith("True")

    cond0 = isinstance(output, int) and output == 0
    cond1 = isinstance(output, int) and output >= 1

    if cond_false or cond0:
        return False
    elif cond_true or cond1:
        return True
    return None

def send_command(cmd, bg=False):
    '''
    Executes command as a foreground process by default.
    '''
    print(str(int(time()))+' => '+str(cmd))
    return Popen(cmd) if bg else check_output(cmd)

if __name__ == '__main__':
    start_script()