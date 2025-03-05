import requests
from bs4 import BeautifulSoup
from scrapper.config import SCRAPPER_CONFIG

def get_lic_stock_price():
    """Fetch the lic stock price from money control"""
    try:
        response=requests.get(SCRAPPER_CONFIG["url"],headers=SCRAPPER_CONFIG["headers"])
        if response.status_code==200:
            soup = BeautifulSoup(response.text,"html.parser")
            price_div = soup.find("div",class="inprice1 nsecp")  #this is the div name of html element displaying the price

            if price_div:
                stock_price=price_div["data-numberanimate-value"]
                return float(stock_price)
    except Exception as e:
        print(f"Error obtaining the value of stock_price. Exception is {e}")
    return None
    
