import requests
from bs4 import BeautifulSoup

#In here, we will be using request way
def fetching_url():
    #Convert URL into XML
    html = requests.get("http://shakespeare.mit.edu/lll/full.html")
    #Create BS object
    bsobj = BeautifulSoup(html.content,"html.parser")
    #Check if we were able to get the data
    print(bsobj)

fetching_url()

