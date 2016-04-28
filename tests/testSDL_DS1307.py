#!/usr/bin/env python
#
# RTC DS1307 Python Driver Code
# Update to use adafruit GPIO by bibi21000@gmail.com
#
# original code from :
# SwitchDoc Labs 07/10/2014
# Shovic V 1.0
# only works in 24 hour mode
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# imports

import sys
import time
import datetime

from RTC_SDL_DS1307.SDL_DS1307 import SDL_DS1307

# Main Program

print ""
print "Test SDL_DS130"
print ""
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

ds1307 = SDL_DS1307(1, 0x68)
ds1307.write_now()

# Main Loop - sleeps 10 minutes, then reads and prints values of all clocks


while True:

    currenttime = datetime.datetime.utcnow()

    deltatime = currenttime - starttime

    print ""
    print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")

    print "DS1307=\t\t%s" % ds1307.read_datetime()

    time.sleep(10.0)
