import code
import json
import requests
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

MAX_RETRIES = 100

def get_proxy_server():

	for i in range(0,MAX_RETRIES):
		try:
			gimme_proxy = requests.get("http://gimmeproxy.com/api/getProxy?get=true&maxCheckPeriod=3600&port=8080&minSpeed=50")
			print gimme_proxy.status_code
			assert gimme_proxy.status_code == 200

		except:
			print "proxy server status code:", gimme_proxy.status_code
			if i == MAX_RETRIES - 1:
				sys.exit("Error getting proxy")
			time.sleep(5)
			continue

		break

	proxy = json.loads(gimme_proxy.content)
	proxy_server = str(proxy['ip'] + ":" + proxy['port'])

	print gimme_proxy.content

	return proxy_server


def start_webdriver(proxy_server):

	options = Options()
	options.add_argument('--proxy-server={0}'.format(proxy_server))
	options.add_extension("./uBlock-Origin_v1.14.24.crx");

	driver = webdriver.Chrome(executable_path='./chromedriver', port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=options)

	print "Chrome driver instantiated with proxy server {0}".format(proxy_server)

	return driver


def main():

	BASE_URL = "https://www.whatismyip.com/"

	driver = start_webdriver(get_proxy_server())

	driver.get(BASE_URL)

	# for debug purposes
	code.interact(local=dict(globals(), **locals()))

if __name__ == "__main__":
	main()
