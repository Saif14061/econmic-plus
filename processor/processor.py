from kafka import KafkaConsumer
import json
from textblob import TextBlob
import psycopg2

consumer = KafkaConsumer("news","stocks",bootstrap_servers='localhost:9092')

conn = psycopg2.connect(host="localhost",port="5432",dbname="economicpulse",user="saif",password="password123")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS News (
        
        ID           SERIAL PRIMARY KEY,
        HEADLINE     TEXT,
        SOURCE       TEXT,
        SENTIMENT_SCORE FLOAT,
        TIMESTAMP    TIMESTAMP DEFAULT NOW()
        
               
        
               
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stocks (
        
        ID         SERIAL PRIMARY KEY,
        TICKER     TEXT,
        PRICE      FLOAT,
        TIMESTAMP  TIMESTAMP DEFAULT NOW()
        
               
        
               
               
    )
""")
conn.commit()
for message in consumer:
    data = json.loads(message.value)

    if message.topic == "news":
        articles_list = data["articles"]
        for article in articles_list:
            headline = article["title"]
            source = article["source"]["name"]
            sentiment_score = TextBlob(headline).sentiment.polarity
            cursor.execute("""
            INSERT INTO news (headline, source, sentiment_score)
            VALUES (%s, %s,%s)
            """, (headline,source,sentiment_score))
            conn.commit()
    elif message.topic == "stocks":
            print(data)
            cursor.execute("""
            INSERT INTO stocks (ticker,price)
            VALUES (%s, %s)
            """, ("S&P500",data["sp500"]))
            conn.commit()
            cursor.execute("""
            INSERT INTO stocks (ticker,price)
            VALUES (%s, %s)
            """, ("FTSE100",data["ftse100"]))
            conn.commit()
           
           
