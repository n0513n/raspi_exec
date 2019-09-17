#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Remote address as in "user@IP"
REMOTE = "raspi@192.168.50.100"

# Remote path to video file
VIDEO  = "/home/raspi/organon/video.mp4"

# Main display; do not edit
SCREEN = "DISPLAY=:0"

# Default command to execute
CMD = ['ssh', REMOTE, SCREEN, 'xdotool', 'key', 'v']

# Custom commands to execute
CMD_CHECK = ['ssh', REMOTE, 'check-mpv']
CMD_START = ['ssh', REMOTE, SCREEN, 'mpv', VIDEO, '--fs', '--osd-level=0', '--sub-visibility=no', '--loop 0']
CMD_FOCUS = ['ssh', REMOTE, SCREEN, 'wmctrl', '-a', 'mpv']
CMD_ABOVE = ['ssh', REMOTE, SCREEN, 'wmctrl', '-r', 'mpv', '-b', 'toggle,above']

# GPIO port to keep watch
PORT = 40

# Seconds to recheck condition
RECHECK = 0

# Seconds to wait every turn
WAIT = 0.1

# Initial boolean state
DEFAULT = False