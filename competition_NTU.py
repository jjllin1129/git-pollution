# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:16:38 2023

@author: USER
"""
import pandas as pd
df_pollution = pd.read_csv(r'D:\程式競賽\pollution_data_1.csv',encoding = 'big5')
len_pollution=len(df_pollution)
data_pm25=[]
for i in range(len_pollution):
    if df_pollution.loc[i,"ItemName"]=="細懸浮微粒":
        data_pm25.append(df_pollution.loc[i,:])
# df_station=pd.read_csv(r'D:\程式競賽\station_ifo.csv')