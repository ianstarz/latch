# Latch - Scrapy

This README outlines the details of collaborating on this Twisted application.
A short introduction of this app could easily go here.

## Prerequisites for Windows

You will need the following things properly installed on your computer.

* [Python 2.7](https://www.python.org)
* [Scrapy](http://scrapy.org/)
* [Pywin32](http://sourceforge.net/projects/pywin32/)

* GOTCHA: Make sure Pywin32 matches processor bit and python version
* GOTCHA: Running scrapy may complain about missing the service_identity module, use `pip install service_identity`

## Installation for Windows

* Install Python, and register it into command line via adding the windows variable PATH to the Python installation directory, eg C:\Python27\;C:\Python27\Scripts\;
* `pip` in command line to double check Pip is installed, otherwise download and install (https://pip.pypa.io/en/latest/installing.html)
* `pip install scrapy`