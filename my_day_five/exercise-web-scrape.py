from urllib.request import urlopen
from bs4 import BeautifulSoup

#Here we will be using urllib
def fetching_url():
    #Convert URL into XML
    html = urlopen("http://shakespeare.mit.edu/lll/full.html")
    #Create BS object
    bsobj = BeautifulSoup(html.read(),"html.parser")
    #Check if we were able to get the data
    #print(bsobj)
    #Return the first header element
    print(bsobj.h3)
    
    #Print all header 3 elements, will return a list
    #h3 = bsobj.findAll("h3")
    #print(h3)
    
    #Loop through the list and clear h3 tags, just print the text
    #for tag in h3:
    #    print(tag.get_text())

    #Look for something
    #nameList = bsobj.findAll(text="DUMAIN")
    #print(nameList)
    #print(len(nameList))

    #Let's grab a all headers and name="section 1.1.9"
    new_object = bsobj.find("a",{"name":"1.1.9"})
    print(new_object.get_text())

fetching_url()

