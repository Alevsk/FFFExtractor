#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
import zlib
import urllib2

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

    def makeRequest(self,data = None):
    	if data is None:
    		self.path = '/search/189386589649/likers'
    	else:
    		self.path = '/ajax/pagelet/generic.php/BrowseScrollingSetPagelet?data=' + data

    	self.conn.request("GET",self.path,headers=self.headers)
    	self.res = self.conn.getresponse()
    	print self.res.status, self.res.reason
    	#urllib2.quote()
	        
if __name__ == '__main__':

	'''
	You can get your facebook cookie using POSTMAN and the interceptor plugin
	'''
	cookie = 'your_facebook_cookie'
	fffext = FFFExtractor(cookie)
	fffext.makeRequest()