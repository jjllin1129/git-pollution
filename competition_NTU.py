# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:16:38 2023

@author: USER
"""
import pandas as pd
"""
處理pollution資料
"""
#%%讀取資料
df_pollution = pd.read_csv(r'D:\程式競賽\pollution_data_1.csv',encoding = 'big5')
#%%取PM2.5資料
data_pm25=[]
for i in range(len(df_pollution)):
    if df_pollution.loc[i,"ItemName"]=="細懸浮微粒":
        data_pm25.append(df_pollution.loc[i,:])
df=pd.DataFrame(data_pm25)
#把NaN部分移除
df=df.dropna(axis=0)
#把x部分移除
nox=[]
for j in range((len(df))):
    if "x" not in df.iloc[j,:].values:
        nox.append(df.iloc[j,:])
df_nox=pd.DataFrame(nox)
#%%計算每一行的總和
#先將計算範圍的數值轉換為整數
num = df_nox.columns[8:]  # 轉換從第8列開始的數據為int
df_nox[num] = df_nox[num].astype(int)
sum_row = df_nox[num].sum(axis=1)
df_nox["總和"]=sum_row
df_nox=df_nox.sort_values(by='MonitorDate', ascending=True)#排序由1/1~12/31
# #存檔(csv)
# df_nox.to_csv(r'D:\程式競賽\data_pm2_5.csv', index=False, encoding='big5')


