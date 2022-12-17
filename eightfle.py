import requests

url = raw_input('enter something')
req = requests(url)
try:
    response = urlopen(req)
except (URLError, e):
    if hasattr(e, 'reason'):
        print ('We failed to reach a server.')
        print ('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print ('The server couldn\'t fulfill the request.')
        print ('Error code: ', e.code)
    else:
        print ('URL is good!')