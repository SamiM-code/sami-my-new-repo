import requests
from bs4 import BeautifulSoup

def fetching_url():
    #u means unicode
    url = u'https://twitter.com/search?q='
    query = u'trump'
    #combine URL + search query
    html = requests.get(url+query)
    bsobj = BeautifulSoup(html.text,'html.parser')

    #Print the json object..
    #print(bsobj)

    #To look for special signs
    #%40 = @
    #%32 = #
    
    #instead of printing the json object, let's get just tweet texts, and put them into a list
    tweets = [p.text for p in bsobj.findAll('p', class_='tweet-text')]
    print(tweets)

fetching_url()
