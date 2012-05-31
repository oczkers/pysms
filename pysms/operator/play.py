#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def login(username, passwd):
	opera = requests.session()
	content = opera.get('https://logowanie.play.pl/p4webportal/SsoRequest').content
	SAMLRequest = re.search('value="(.*?)"', content).group(1)
	content = opera.post('https://logowanie.play.pl/p4-idp2/SSOrequest.do', {'SAMLRequest':SAMLRequest, 'target':'https://bramka.playmobile.pl'}).content
	random = re.search('name="random" value="(.+)"', content).group(1)
	content = opera.post('https://logowanie.play.pl/p4-idp2/Login.do', {'step':1, 'random':random, 'login':username, 'password':passwd}).content
	SAMLResponse = re.search('value="(.+?)"', content.replace('\r', '').replace('\n', '')).group(1)
	print SAMLResponse
	content = opera.post('https://logowanie.play.pl/p4webportal/SSOResponseConsumer', {'SAMLResponse':SAMLResponse, 'target':'https://bramka.playmobile.pl'}).content
	return content

def sendSMS(username, passwd, cell, text):
	opera = requests.session()
	return login(username, passwd)
	#content = opera.post('https://logowanie.play.pl/p4-idp2/SSOrequest.do', {'SAMLRequest':SAMLRequest}).content
	#return opera.get('https://logowanie.play.pl/p4-idp2/LoginForm.do').content
	#return opera.get('https://bramka.play.pl').content
