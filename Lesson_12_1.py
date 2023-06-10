import steamlit as st
import pandas as pd

codeFrame=pd.read_csv('個股日成交資訊.csv',  usecols=['證券代號','證券名稱', '成交金額'])
codeSeries=codeFrame['證券代號'].astype(str) + codeFrame['證券名稱']


with st.sidebar:
    st.multiselect("請選擇股票:",codeSeries)