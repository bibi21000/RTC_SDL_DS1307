# -*- coding: utf-8 -*-
"""

RTC DS1307 Python Driver Code
Update to use adafruit GPIO by bibi21000@gmail.com

original code from :
SwitchDoc Labs 07/10/2014
Shovic V 1.0
only works in 24 hour mode

# The MIT License (MIT)
#
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

"""
from datetime import datetime
from bcd import int_to_bcd, bcd_to_int

DS1307_ADDRESS = 0x68

class SDL_DS1307(object):
    """Class for DS1307 RTC clock."""

    _REG_SECONDS = 0x00
    _REG_MINUTES = 0x01
    _REG_HOURS = 0x02
    _REG_DAY = 0x03
    _REG_DATE = 0x04
    _REG_MONTH = 0x05
    _REG_YEAR = 0x06
    _REG_CONTROL = 0x07

    def __init__(self, address=DS1307_ADDRESS, i2c=None, **kwargs):
        """Initialize the RTC DS1307."""
        # Setup I2C interface for the device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device( address, **kwargs )


    def _write(self, register, data):
        """Write data to bus"""
        #print "addr =0x%x register = 0x%x data = 0x%x %i " % (self._addr, register, data,bcd_to_int(data))
        self._device.write8( register, data )

    def _read(self, data):
        """Read data from bus"""
        returndata = self._device.readU8(data)
        #print "addr = 0x%x data = 0x%x %i returndata = 0x%x %i " % (self._addr, data, data, returndata, bcd_to_int(returndata))
        return returndata

    def _read_seconds(self):
        return bcd_to_int(self._read(self._REG_SECONDS))

    def _read_minutes(self):
        return bcd_to_int(self._read(self._REG_MINUTES))

    def _read_hours(self):
        d = self._read(self._REG_HOURS)
        if (d == 0x64):
            d = 0x40
        return bcd_to_int(d & 0x3F)

    def _read_day(self):
        return bcd_to_int(self._read(self._REG_DAY))

    def _read_date(self):
        return bcd_to_int(self._read(self._REG_DATE))


    def _read_month(self):
        return bcd_to_int(self._read(self._REG_MONTH))

    def _read_year(self):
        return bcd_to_int(self._read(self._REG_YEAR))

    def read_all(self):
        """Return a tuple such as (year, month, date, day, hours, minutes, seconds).
        """
        return (self._read_year(), self._read_month(), self._read_date(),
                self._read_day(), self._read_hours(), self._read_minutes(),
                self._read_seconds())

    def read_str(self):
        """Return a string such as 'YY-DD-MM HH-MM-SS'.
        """
        return '%02d-%02d-%02d %02d:%02d:%02d' % (self._read_year(),
                self._read_month(), self._read_date(), self._read_hours(),
                self._read_minutes(), self._read_seconds())

    def read_datetime(self, century=21, tzinfo=None):
        """Return the datetime.datetime object.
        """
        return datetime((century - 1) * 100 + self._read_year(),
                self._read_month(), self._read_date(), self._read_hours(),
                self._read_minutes(), self._read_seconds(), 0, tzinfo=tzinfo)

    def write_all(self, seconds=None, minutes=None, hours=None, day=None,
            date=None, month=None, year=None, save_as_24h=True):
        """Direct write un-none value.
        Range: seconds [0,59], minutes [0,59], hours [0,23],
               day [0,7], date [1-31], month [1-12], year [0-99].
        """
        if seconds is not None:
            if seconds < 0 or seconds > 59:
                raise ValueError('Seconds is out of range [0,59].')
            self._write(self._REG_SECONDS, int_to_bcd(seconds))

        if minutes is not None:
            if minutes < 0 or minutes > 59:
                raise ValueError('Minutes is out of range [0,59].')
            self._write(self._REG_MINUTES, int_to_bcd(minutes))

        if hours is not None:
            if hours < 0 or hours > 23:
                raise ValueError('Hours is out of range [0,23].')
            self._write(self._REG_HOURS, int_to_bcd(hours))  # not | 0x40 as in the orignal code

        if year is not None:
            if year < 0 or year > 99:
                raise ValueError('Years is out of range [0,99].')
            self._write(self._REG_YEAR, int_to_bcd(year))

        if month is not None:
            if month < 1 or month > 12:
                raise ValueError('Month is out of range [1,12].')
            self._write(self._REG_MONTH, int_to_bcd(month))

        if date is not None:
            if date < 1 or date > 31:
                raise ValueError('Date is out of range [1,31].')
            self._write(self._REG_DATE, int_to_bcd(date))

        if day is not None:
            if day < 1 or day > 7:
                raise ValueError('Day is out of range [1,7].')
            self._write(self._REG_DAY, int_to_bcd(day))

    def write_datetime(self, dt):
        """Write from a datetime.datetime object.
        """
        self.write_all(dt.second, dt.minute, dt.hour,
                dt.isoweekday(), dt.day, dt.month, dt.year % 100)

    def write_now(self):
        """Equal to DS1307.write_datetime(datetime.datetime.now()).
        """
        self.write_datetime(datetime.now())
