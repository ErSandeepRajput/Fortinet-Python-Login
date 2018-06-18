import requests
import re
import time

req = requests.get("http://www.google.com")
url = str(req.url)

info = {}

info["username"] = "" #username
info["password"] = "" #password

if "fgtauth" in url:
	magic = re.search("http.*\?", url).group()
	magic = url.replace(magic,"")
	info["magic"] = magic
	rsp = requests.post(url, data = info, timeout = (1, 1))
	print rsp.url
	print "http://192.168.6.5:1000/logout?" + magic

	while True:
		rsp = requests.get(str(rsp.url))
		time.sleep(555)
		print rsp.url

