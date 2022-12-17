import urllib.request
webUrl = urllib.request.urlopen('https://realpython.com/lessons/the-get-request/')
print('resultcode' + str(webUrl.getcode()))