import requests
from bs4 import BeautifulSoup
import re

def get_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17',
        'From': 'uncle@sam.com'  # This is another valid field
    }

    r = requests.get(url, headers=headers)
    bsobj = BeautifulSoup(r.text, "html.parser")

    #PRINTING WORKS
    # This will print header list: MONTH, OPTIONS,ETC
    thead = bsobj.findAll('th', {'class':re.compile('cme*'),'scope':'col'})

    #Let's try to add these values into list
    headerLine = []
    for title in thead:
        headerLine.append(title.get_text())

    #Let's create multi-dimensional array using lists inside a list
    dataArray = []
    dataArray.append(headerLine)

    component_codes = ['ESU7','ESZ7','ESH8','ESM8','ESU8','ESZ8']
    component_codes_translated = {'ESU7':'SEP 2017', 'ESZ7':'DEC 2017', 'ESH8':'MAR 2018', 'ESM8':'JUN 2018', 'ESU8':'SEP 2018', 'ESZ8':'DEC 2018'}

    for yearCode in component_codes:
        #Reset perYearValues list after each loop
        perYearValues = []
        td = bsobj.findAll('td', {"id": re.compile("quotesFuturesProductTable1_{}_*".format(yearCode))})
        for item in td:
            #print(item.get_text())
            perYearValues.append(item.get_text())
        #Accommodate the fact that "options" and "charts" have empty values
        perYearValues.insert(0,'')
        perYearValues.insert(0, '')
        #Translate yearCode back to human readable format
        perYearValues.insert(0,component_codes_translated[yearCode])
        # Add one year values into dataArray as a new list
        dataArray.append(list(perYearValues))

    #PRINT IN LIST FORMAT
    #Print the dataArray, accommodate the fact that the two first columns are empty from the data
    for index,item in enumerate(dataArray):
        print(item)

    print("")

    #PRINT IN HUMAN READABLE FORMAT
    for year in dataArray:
        for item in year:
            print("{0:<20}".format(item),end="")
        print("\n")

#get_url('https://www.whatismybrowser.com/detect/what-is-my-user-agent')
get_url('https://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html')