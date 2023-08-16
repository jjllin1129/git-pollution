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
df_station=pd.read_csv(r'D:\程式競賽\station_ifo.csv')
#%%把縣市等資料合併到汙染的資料中
merged_df = df_pollution.merge(df_station[['StationName', 'Area', 'County']], left_on='SiteName', right_on='StationName', how='left')
merged_df=merged_df[['Area', 'County']]
df_pollution[['Area', 'County']]=merged_df
#%%取PM2.5資料
data_pm25=[]
for i in range(len(df_pollution)):
    if df_pollution.loc[i,"ItemName"]=="細懸浮微粒":
        data_pm25.append(df_pollution.loc[i,:])
df=pd.DataFrame(data_pm25)
#把NaN部分移除
df=df.dropna(axis=0)
#把x及外島部分移除
nox=[]
for j in range((len(df))):
    if "x" not in df.iloc[j,:].values:
        if "外島" not in df.iloc[j,-2]:
            nox.append(df.iloc[j,:])
#%%把資料依照站名跟月份(由小到大排列)
df_nox=pd.DataFrame(nox)
df_nox = df_nox.sort_values(by=['SiteName', 'MonitorDate'], ascending=[True, True])
#%%計算日平均
num = df_nox.columns[8:-2]  # 轉換從第8列開始的數據為int(因為值從columns=8開始)
df_nox[num] = df_nox[num].astype(int)# 原本是str用astype改變成int
df_nox["日平均"]= df_nox[num].mean(axis=1)
#%%計算年and月平均前置作業
# 將MonitorDate列轉換為日期時間類型
df_nox['MonitorDate'] = pd.to_datetime(df_nox['MonitorDate'])#先換成日期模式才能改
df_nox['月份'] = df_nox['MonitorDate'].dt.strftime('%m')# 添加月份列
#%%計算每月平均值
monthly_avg = df_nox.groupby(['Area','County','SiteName', '月份'])['日平均'].mean()#依循站名跟月份下去分類，並且對日平均那欄取平均
df_monthly=pd.DataFrame(monthly_avg).rename(columns={'日平均':'月平均'})#改變column名字，從日平均變成月平均
df_monthly = df_monthly.pivot_table(index=['SiteName','Area','County'], columns='月份', values='月平均')# 使用 pivot_table 函數將每個月的平均值分成不同欄位
# 將 pivot 後的資料框架重新命名欄位，加上 '月份'
df_monthly = df_monthly.add_prefix('月份')
df_monthly=df_monthly.reset_index()#用reset存下index的值
#%%計算每年平均值
yearly_avg = df_monthly.iloc[:,3:].mean(axis=1)
# df_yearly=df_monthly[['Area','County','SiteName']]
# df_yearly.loc[:,'年平均']=yearly_avg
df_yearly = df_monthly[['Area','County','SiteName']].assign(年平均=yearly_avg)#用assig()來取代上面的方法
#%%存檔(csv)
# df_nox.to_csv(r'D:\程式競賽\data_pm2_5.csv', index=False, encoding='big5')
df_monthly.to_csv(r'D:\程式競賽\pm2_5_monthly.csv', index=False, encoding='big5')
df_yearly.to_csv(r'D:\程式競賽\pm2_5_yearly.csv', index=False, encoding='big5')
