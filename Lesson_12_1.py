import streamlit as st
import pandas as pd
import yfinance as yf


codeFrame=pd.read_csv('個股日成交資訊.csv',  usecols=['證券代號','證券名稱', '成交金額'])
codeSeries=codeFrame['證券代號'].astype(str) + codeFrame['證券名稱']


with st.sidebar:
    selected_codes = st.multiselect("請選擇股票:",codeSeries,
                                    max_selections=4)

st.cache_data
def fetch_stock_dataframe(id):
    stock=yf.download(id,start='2023-01-01')
    return fetch_stock_dataframe


for code in selected_codes:
    code1=code[:4]+".TW"
    code_stock_dataFrame=fetch_stock_dataframe(code1)
    code_stock_DF_sorted=code_stock_dataFrame.sort_index(ascending=false)
    st.subheader(code)
    st.dataframe(code_stock_DF_sorted, width=1024)
    st.divider()
    st.write(code)