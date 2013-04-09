#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests
from operator import play


def getMNC(cell):
    """Returns Mobile Network Code.
     (http://en.wikipedia.org/wiki/Mobile_Network_Code)
     """
    opera = requests.Session()
    data = {'msisdn': cell}    # remember about prefix
    content = opera.post('http://download.t-mobile.pl/updir/updir.cgi', data).content
    return re.search('<b>Kod sieci:</b></td><td>[0-9]+ ([0-9]+)</td>', content).group(1)


def sendSMS(cell):
    """Sends SMS."""
    mnc = getMNC(cell)
    if mnc == '06':
        network = play
    return network.sendSMS(cell, 'test')    # login?
