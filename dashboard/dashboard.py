import streamlit as st
import pandas as pd
import psycopg2
import time

st.title("Financial News Tracker")
conn = psycopg2.connect(host="localhost",port="5432",dbname="economicpulse",user="saif",password="password123")
cursor = conn.cursor()

def get_sentiment_label(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return"negative"
    else:
        return "neutral"
    
news_df = pd.read_sql("SELECT * FROM news", conn)
stocks_df = pd.read_sql("SELECT * FROM stocks", conn)
news_df['sentiment_label'] = news_df['sentiment_score'].apply(get_sentiment_label)
st.subheader("latest news")
st.dataframe(news_df)
st.subheader("stock prices")
st.dataframe(stocks_df)

st.subheader("News Impact (negative,neutral,postive)")
st.bar_chart(news_df['sentiment_label'].value_counts())


time.sleep(30)
st.rerun()

