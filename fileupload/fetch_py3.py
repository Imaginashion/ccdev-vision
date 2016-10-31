import requests, random
import datetime
import hmac
import hashlib
import base64
import urllib
import xml.etree.ElementTree as ET
from random import randint


def fetch_from_amazon(item_to_find):
	domain = "http://webservices.amazon.in/onca/xml?"
	AWSAccessKeyId = "AKIAIECZDULPDDS5O6DA"
	AssociateTag = "none0d9-21"
	Keywords = item_to_find #string from google vision
	time = str(datetime.datetime.utcnow().isoformat())
	time = time[:len(time)-7]+"Z"
	time = time.replace(":","%3A")
	#print time
	secret = b"2zMq7BgvakMJ+skAcX0cFPfbVbbj/PcnvLcAEL9X"
	next_string = "Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=All&Service=AWSECommerceService&Timestamp=" + time 
	Version="2011-08-01"
	request_param = "AWSAccessKeyId=" + AWSAccessKeyId + "&AssociateTag=" + AssociateTag + "&Keywords=" + Keywords + "&" + next_string + "&Version=" + Version 
	string_to_sign = "GET\nwebservices.amazon.in\n/onca/xml\n" + request_param
	#print("String_to_sign :" + string_to_sign)
	signature = hmac.new(secret, string_to_sign.encode('utf-8'), hashlib.sha256).digest()
	#print "Signature=" + urllib.quote(base64.b64encode(signature),safe='')
	request = domain + request_param + "&Signature=" + urllib.parse.quote(base64.b64encode(signature),safe='')
	response = requests.get(request)
	xml_str = ""
	for child in response:
		xml_str += child.decode("utf-8") 
		
	#print(xml_str)
	root = ET.fromstring(xml_str)
	count = 0
	prod_url = []
	img_url = []
	features = []
	color = []
	price = []
	title = []
	for child in root:
		#print child.tag
		if child.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Items':
			for item in child:
				if item.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Item':
					for x in item:
						#print x.tag, x.attrib
						if x.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}DetailPageURL':
							prod_url.append(x.text)
						elif x.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}MediumImage':
							for url in x:
								if url.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}URL':
									img_url.append(url.text)
						elif x.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ItemAttributes':
							feat = ''
							for att in  x:
								if att.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Color':
									color.append(att.text)
								elif att.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Feature':
									feat += '<br/>' + att.text
								elif att.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Title':
									title.append(att.text)
								elif att.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}ListPrice':
									for z in att:
										if z.tag == '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}FormattedPrice':
											price.append(z.text)
							features.append(feat)
	dictionary = {
		'title': title,
		'prod_url' : prod_url,
		'features' : features,
		'color' : color,
		'price' : price,
		'img_url' : img_url
	}
	listi = []
	x = 0
	for x in range(len(title)):
		obj = [title[x]]
		obj.append(prod_url[x])
		obj.append(features[x])
		try:
			obj.append(color[x])
		except Exception as e:
			cool = ['red','blue','green','metallic','grey','black']
			obj.append(cool[randint(1,5)])
		try:
			obj.append(img_url[x])
		except Exception as e:
			break	
		try:
			obj.append(price[x])
		except Exception as e:
			cost = 1000 + randint(1,1000)
			obj.append("INR " + str(cost))
		listi.append(obj)
		x += 1
	print(listi)
	return listi

#fetch_from_amazon('green-shirt-men')