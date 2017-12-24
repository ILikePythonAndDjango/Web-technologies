# -*- coding: utf-8 -*-
import requests
from lxml import etree
response = requests.get("https://stepik.org/explore")
parser = etree.HTMLParser()
root = etree.fromstring(response.text, parser)
for element in root.iter("link"):
	if element.attrib["rel"] == 'stylesheet':
		print(element.attrib)
