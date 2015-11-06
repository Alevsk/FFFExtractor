#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import zlib
import urllib2
import sys
import string
import json

class CONSTANTS:
	CURSOR = "cursor"
	PAGE_NUMBER = "page_number"

class FFFExtractor:

	def __init__(self, cookie):

		self.conn                       = httplib.HTTPSConnection("www.facebook.com")
		self.headers                    = {}
		self.headers['user-agent']      = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'
		self.headers['accept']          = '*/*'
		self.headers['referer']         = 'https//www.facebook.com/search/189386589649/likers'
		self.headers['accept-encoding'] = 'gzip, deflate, sdch'
		self.headers['accept-language'] = 'es-ES,es;q=0.8'
		self.headers['cookie']          = cookie
		self.counter                    = 1

	def makeRequest(self,data = None):

		print 'Request #' + str(self.counter)
		self.path = None
		
		if data is None:
			self.path = '/search/189386589649/likers'
		else:
			self.path = '/ajax/pagelet/generic.php/BrowseScrollingSetPagelet?data=' + '%7B%22typeahead_sid%22%3A%22%22%2C%22tr%22%3Anull%2C%22topic_id%22%3Anull%2C%22em%22%3Afalse%2C%22mr%22%3Afalse%2C%22view%22%3A%22list%22%2C%22display_params%22%3A%5B%5D%2C%22logger_source%22%3A%22www_main%22%2C%22encoded_query%22%3A%22%7B%5C%22bqf%5C%22%3A%5C%22likers(189386589649)%5C%22%2C%5C%22vertical%5C%22%3A%5C%22none%5C%22%2C%5C%22post_search_vertical%5C%22%3Anull%2C%5C%22intent_data%5C%22%3Anull%2C%5C%22query_analysis%5C%22%3Anull%7D%22%2C%22trending_source%22%3Anull%2C%22has_top_pagelet%22%3Anull%2C%22ref_path%22%3A%22%2Fsearch%2F189386589649%2Flikers%22%2C%22tl_log%22%3Afalse%2C%22encoded_title%22%3A%22WyJQZW9wbGUrd2hvK2xpa2UrIix7InRleHQiOiJVbml2ZXJzaWRhZCtQYW5hbWVyaWNhbmEiLCJ1aWQiOjE4OTM4NjU4OTY0OSwidHlwZSI6InBhZ2UifV0%22%2C%22is_trending%22%3Afalse%2C%22page_number%22%3A'+data['page_number']+'%2C%22browse_location%22%3A%22%22%2C%22filter_ids%22%3A%7B%22520053742%22%3A520053742%2C%221066595962%22%3A1066595962%2C%221406468036%22%3A1406468036%2C%22100000891774285%22%3A100000891774285%7D%2C%22callsite%22%3A%22browse_ui%3Ainit_result_set%22%2C%22cursor%22%3A%22'+data['code']+'%22%2C%22exclude_ids%22%3Anull%2C%22impression_id%22%3A%229d6ea2b2%22%2C%22ref%22%3A%22unknown%22%2C%22experience_type%22%3A%22grammar%22%2C%22story_id%22%3Anull%7D'
			self.path += '&__user=1078496755&__a=1&__dyn=7AmajEyl2qm9ongDxiWOGeFDzECiq2WiqAdy9VCC-K26m5-bzES2N6y8-bxu3fzoat1bxjx27W88xi5VJ1efKiVWz9EpwzxO2OE&__req=k&__rev=1951399'

		self.conn.request("GET",self.path,headers=self.headers)
		self.res = self.conn.getresponse()
		print self.res.status, self.res.reason
		self.counter += 1

		if self.res.status == 200 and self.res.reason == 'OK':
			
			self.data = self.res.read()
			self.decompress = zlib.decompress(self.data, 16+zlib.MAX_WBITS)
			return self.decompress.decode('utf-8')

		else:
			return -1

	def cursorParser(self,input):

		input = input.replace("for (;;);", "", 2)
		cursor = {'code':'','page_number':''}
		position = 0
		pageNumberPosition = 0

		try:
			json_object = json.loads(input)
		except ValueError, e:
			position = input.find(CONSTANTS.CURSOR)
			cursorStart = position + 9

		else:
			position = input.find("\"cursor\"")
			cursorStart = position + 10
			
		for i in range(cursorStart,len(input)):
			if input[i] == '"':
				pageNumberPosition = i + 16
				for i in range(pageNumberPosition,len(input)):
					if input[i] == ',':
						break
					else:
						cursor['page_number'] += input[i]
				break
			else:
				cursor['code'] += input[i]


		print cursor
		return cursor
			
	def fansParser(self,input):
		pass

	def getFans(self):
		data = None
		for i in range(1,9):
			response = self.makeRequest(data)
			# THREADS HERE
			# data contains the necesary information to build the request for the following pages
			data = self.cursorParser(response)
			# Thread thatPrint or store fans data
			self.fansParser(response)


if __name__ == '__main__':

	'''
	You can get your facebook cookie using POSTMAN and the interceptor plugin
	'''
	cookie = 'your_facebook_cookie'
	fffext = FFFExtractor(cookie)
	fffext.getFans()