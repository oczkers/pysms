#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def sendSMS(cell, text):
	opera = requests.session(headers=headers)
	return opera.get('https://bramka.play.pl').content
