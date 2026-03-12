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
        TIMESTAMP    TIMESTAMP DEFAULT NOW(),
        
               
        
               
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stocks (
        
        ID         SERIAL PRIMARY KEY,
        TICKER     TEXT,
        PRICE      FLOAT,
        TIMESTAMP  TIMESTAMP DEFAULT NOW(),
        
               
        
               
    )
""")
conn.commit()
for message in consumer:
    data = json.loads(message.value)

    if message.topic == "news":
        print(f"Processing News update: {message.value}")
    elif message.topic == "stocks":
        print(f"Processing Stock update: {message.value}")

