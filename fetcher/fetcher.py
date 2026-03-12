import time
import json
from kafka import KafkaProducer
from newsapi import NewsApiClient
import yfinance as yf

producer = KafkaProducer(bootstrap_servers='localhost:9092')
newsapi = NewsApiClient(api_key = "b915d1832ed040a9bbb3ee44ddadab3b") #API key for NewsAPI

while True:
    articles = newsapi.get_everything(q="economy",language="en",pageSize=10)
    sp500 = yf.Ticker("^GSPC")
    ftse100 = yf.Ticker("^FTSE")
    sp500_price = sp500.fast_info['last_price']
    ftse100_price = ftse100.fast_info['last_price']

    producer.send("news",json.dumps(articles).encode('utf-8'))
    stock_data = { 
        "sp500":sp500_price,
        "ftse100":ftse100_price
    }
    producer.send("stock",json.dumps(stock_data).encode('utf-8'))
    time.sleep(300)
