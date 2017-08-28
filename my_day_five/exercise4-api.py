import requests

def company_search(ticker):
    lookup_url = "http://www.sectorspdr.com/sectorspdr/"\
                 "IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol="
    r = requests.get(lookup_url + ticker)
    print(r.text)

company_search("xlf")
