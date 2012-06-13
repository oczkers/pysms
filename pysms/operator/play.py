#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

def login(username, passwd):
	opera = requests.session()
	content = opera.get('https://bramka.play.pl/composer/public/mmsCompose.do').content
	SAMLRequest = re.search('value="(.*?)"', content, re.MULTILINE|re.DOTALL).group(1)
	content = opera.post('https://logowanie.play.pl/p4-idp2/SSOrequest.do', {'SAMLRequest':SAMLRequest, 'target':'https://bramka.playmobile.pl'}).content
	random = re.search('name="random" value="(.+)"', content).group(1)
	content = opera.post('https://logowanie.play.pl/p4-idp2/Login.do', {'step':1, 'random':random, 'login':username, 'password':passwd}).content
	SAMLResponse = re.search('value="(.+?)"', content, re.MULTILINE|re.DOTALL).group(1)
	content = opera.post('https://bramka.play.pl/composer/samlLog?action=sso', {'SAMLResponse':SAMLResponse, 'target':'https://bramka.playmobile.pl'}).content
	content = opera.post('https://bramka.play.pl/composer/j_security_check', {'SAMLResponse':SAMLResponse}).content
	return opera

def sendSMS(username, passwd, cell, text):
	opera = login(username, passwd)
	content = opera.get('https://bramka.play.pl/composer/public/editableSmsCompose.do').content
	randForm = re.search('name="randForm" value="(.+)"', content).group(1)
	data = {'recipients':cell, 'content_in':text, 'czas':0, 'templateId':'', 'sendform':'on', 'composedMsg':'', 'randForm':randForm, 'old_signature':'', 'old_content':text, 'content_out':text}
	opera.post('https://bramka.play.pl/composer/public/editableSmsCompose.do', data).content
	data['SMS_SEND_CONFIRMED'] = 'Wyślij'
	content = opera.post('https://bramka.play.pl/composer/public/editableSmsCompose.do', data).content
	if 'Wiadomość została wysłana' in content:
		return True
	else:
		return False
