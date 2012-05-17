#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def getMNC(cell):
	''' get Mobile Network Code ( http://en.wikipedia.org/wiki/Mobile_Network_Code ) '''
	opera = requests.session()
	values = { 'msisdn':cell }	# remember about prefix
	content = opera.post('http://download.t-mobile.pl/updir/updir.cgi', values).content
	return re.search('<b>Kod sieci:</b></td><td>[0-9]+ ([0-9]+)</td>', content).group(1)
