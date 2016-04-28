# -*- coding: utf-8 -*-
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages, Extension

# Call setuptools setup function to install package.
setup(name              = 'RTC_SDL_DS1307',
      version           = '1.0.0',
      author            = 'bibi21000',
      author_email      = 'bibi21000@gmail.com',
      description       = 'Raspberry Pi Python Library for DS1307 RTC',
      license           = 'MIT',
      url               = 'https://github.com/bibi21000/RTC_SDL_DS1307',
      packages          = find_packages(),
      dependency_links  = [
                'https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5',
                'https://github.com/dafyddcrosby/python-bcd/tarball/master#egg=bcd',
      ],
      install_requires  = ['Adafruit-GPIO>=0.6.5','bcd'],
      )
