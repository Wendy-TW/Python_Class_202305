import requests
import pandas as pd
import streamlit as st
url4="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
#  Ubike open api

response = requests.request('GET', url4)
# reponse object 實體接收 data  attribute 可讀/    2.  property read only  3.  Method 呼叫方法
if response.ok:
    print("ok")
   
if response.status_code==200:
    print("connect successfully")
    all_data=response.json()
    print(type(all_data))
else:  print(f"fail code:{response.status_code}")


#class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)[source]
DF1= pd.DataFrame(data=all_data)

Series1=DF1['sna']
mask=DF1['sbi']<=3
Mask_DF=DF1[mask]
Mask_DF.to_csv('可借用車輛小於3站點.csv')

Mask_DF.to_excel('可借用車輛小於3站點.xlsx')  #pip install openpyxl

# 加入INPUT變數
min= 3 #int(input("請輸入要查詢的可借數量:"))
mask=DF1['sbi']<=min
min_DF1=DF1[mask]


#  from teacher
dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
mask = dataFrame['sbi'] <= 3
mask_dataFrame = dataFrame[mask]
st.dataframe(mask_dataFrame)

#C:\Users\User\Documents\GitHub\Python_Class_202305>streamlit run Lesson_8_1.py
#You can now view your Streamlit app in your browser.
#Local URL: http://localhost:8501
#Network URL: http://172.16.4.19:8501
 