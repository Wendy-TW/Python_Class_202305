import requests
url4="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
#  Ubike open api

response = requests.request('GET', url4)
# reponse object 實體接收 data  attribute 可讀/    2.  property read only  3.  Method 呼叫方法
if response.ok:
    print("ok")
   
if response.status_code==200:
    print("connect successfully")
    all_text=response.text
    print(type(all_text))
else:  print(f"fail code:{response.status_code}")

