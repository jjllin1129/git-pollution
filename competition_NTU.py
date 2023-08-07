# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:16:38 2023

@author: USER
"""
import pandas as pd
"""
處理pollution資料
"""
#讀取資料
df_pollution = pd.read_csv(r'D:\程式競賽\pollution_data_1.csv',encoding = 'big5')
#取PM2.5資料
len_pollution=len(df_pollution)
data_pm25=[]
for i in range(len_pollution):
    if df_pollution.loc[i,"ItemName"]=="細懸浮微粒":
        data_pm25.append(df_pollution.loc[i,:])
df=pd.DataFrame(data_pm25)
#把NaN部分移除
data_pm25=df.dropna(axis=0)
#存檔
df_1=pd.DataFrame(data_pm25)
df_1.to_excel(r'D:\程式競賽\data_pm2_5.xlsx', index=False)
df_1.to_csv(r'D:\程式競賽\data_pm2_5.csv', index=False, encoding='big5')
# df_station=pd.read_csv(r'D:\程式競賽\station_ifo.csv')