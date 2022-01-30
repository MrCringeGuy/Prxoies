from urllib.request import Request, urlopen
import time
import datetime

url = input('[+] URL To Go To (INCLUDE HTTP/S): ')
proxies = {
    'https':'191.103.219.225:48612'
}

while True:
    try:
        h = urlopen(url, proxies=proxies)
        break
    except:
        print('['+time.strftime('%Y/%m/%d %H:%M:%S')+'] '+'ERROR. Trying again in a few seconds...')
        time.sleep(3)
