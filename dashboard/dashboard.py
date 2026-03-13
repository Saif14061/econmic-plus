import streamlit as st
import pandas as pd
import psycopg2
import time
st.set_page_config(layout="wide", page_title="Financial News Tracker")

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
def color_sentiment(value):
    if value == "positive":
        return 'color:green'
    elif value == "negative":
        return 'color:red'
    else:
        return 'color:black'
    
news_df = pd.read_sql("SELECT * FROM news", conn)
stocks_df = pd.read_sql("SELECT * FROM stocks ORDER BY timestamp DESC LIMIT 2", conn)
news_df['sentiment_label'] = news_df['sentiment_score'].apply(get_sentiment_label)

col1,col2,col3 = st.columns(3)
col1.metric(label="S&P 500", value=stocks_df[stocks_df['ticker']=='S&P500']['price'].iloc[-1].round(2))
col2.metric(label="FTSE 100", value=stocks_df[stocks_df['ticker']=='FTSE100']['price'].iloc[-1].round(2))
col3.metric(label="Market Sentiment", value=news_df['sentiment_label'].mode()[0])

col4, col5 = st.columns(2)
with col4:
    st.dataframe(news_df.style.applymap(color_sentiment, subset=['sentiment_label']))
with col5:
    st.bar_chart(news_df['sentiment_label'].value_counts(), height=300, width=400)
st.subheader("stocks")
st.dataframe(stocks_df)

time.sleep(30)
st.rerun()

