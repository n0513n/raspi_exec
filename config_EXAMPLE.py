#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
To enable importing, save this file as "config.py" after
setting the required variables and optional settings below.
"""

# Default command to execute
CMD = []

# GPIO port to keep watch
PORT = 40

# Custom commands to execute
CMD_CHECK = []
CMD_START = []

# Seconds to recheck condition
RECHECK = 0

# Seconds to wait every turn
WAIT = 0.25

# Initial boolean state
DEFAULT = False

# Main display; do not edit
SCREEN = "DISPLAY=:0"