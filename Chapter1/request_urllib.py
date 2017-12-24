# -*- coding: utf-8 -*-
#Example1:
'''
import urllib.request
url = "http://ya.ru/"
req = urllib.request.ulropen(url)
print(req.info())
print(req.read())
'''
#Example2:
'''
import urllib.parse
import urllib.request
url = "http://numbersapi.com/#random/math&json"
values = {}
headears = {"User-Agent":"python urllib",
			"Content-Type":"application/json"}
data = urllib.parse.urlencode(values)
byte_data = data.encode("ASCII")
req = urllib.request.Request(url, byte_data, headears)
response = urllib.request.urlopen(req)
print(response.info())
print(response.read())
'''
# Example on Python 2:
'''
import urllib
import urllib2
url = "http://api.site.come/method"
values = {"argument1":"value1",
		  "argument2":"value2"}
headers = {"User-Agent":"python urllib2"}
data = urllib.urlenconde(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
result = response.read()
'''