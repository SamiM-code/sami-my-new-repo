import urllib.request
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def fetch_url(givenUrl):

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.parse.urlencode(headers)
    data = data.encode('utf-8')
    #data = data.encode('utf-8')  # data should be bytes
    #createRequest = urllib.request.Request(givenUrl, data)
    response = urllib.request.urlopen(givenUrl, data)

    #data = urllib.parse.urlencode(values)
    #req = urllib.request.Request(url, data)
    #response = urllib.request.urlopen(req)


    #html = urlopen(createRequest)
    bsobj = BeautifulSoup(response.read(),"html.parser")
    print(bsobj)

    #req = urllib.request.Request(
    #givenUrl,
    #data=None,
    #headers={
    #    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    #}
    #)

    #f = urllib.request.urlopen(givenUrl)
    #print(f.read().decode('utf-8'))

#fetch_url('https://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html')
#fetch_url('http://shakespeare.mit.edu/lll/full.html')
#fetch_url('http://www.sectorspdr.com/sectorspdr/')
fetch_url('https://www.whatismybrowser.com/detect/what-is-my-user-agent')