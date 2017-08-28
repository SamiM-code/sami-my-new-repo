import requests

def get_quote(ticker):
    #Arty got the URL from the markit.com developer documentation
    quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
    r = requests.get(quote_url + ticker)
    print(r.json())

get_quote("aapl")

