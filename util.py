# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:38:08 2015

@author: xujingping, simin
"""

from __future__ import division  
import pandas as pd
import numpy as np
# import time as time
from pandas.tseries.offsets import Day,Hour
from pandas import DataFrame



def list2csv(li,filename):
    li1=[]
    li2=[]
    for item in li:
        li1.append(item[0])
        li2.append(item[1])
    df=pd.DataFrame({'user_id':li1, 'item_id':li2})
    df.to_csv(filename,index=False)
      

    
def evaluate_model(test_label_file,predict_label_file):   
    """
      Input:
          test_label_file:
          predict_label_file:
      Output:result[0]:正确率； result(1)：召回率； result[2]:F1    
    """
    result=[0,0,0]
    df1=pd.read_csv(test_label_file)
    df2=pd.read_csv(predict_label_file)
    df1=df1.set_index(['user_id','item_id'])
    df2=df2.set_index(['user_id','item_id'])
    result[0]=len(df1.index.intersection(df2.index))*1.0/len(df2.index)
    result[1]=len(df1.index.intersection(df2.index))*1.0/len(df1.index)
    result[2]=2.0*result[0]*result[1]/(result[0]+result[1])
    return result

#@author: simin lee
def user_buy_nums(train_x):
    user_buy_nums=train_x.loc[:,['user_id','behavior_type']]
    user_buy_nums=user_buy_nums[user_buy_nums.behavior_type==4]
    user_buy_nums=user_buy_nums.groupby("user_id",as_index=False).count()
    user_buy_nums.rename(columns={'behavior_type':'user_buy_nums'}, inplace=True)
    return user_buy_nums
def add_day(old_date,n=1):
    new_date=pd.to_datetime(old_date)+n*Day()
    return new_date.strftime('%Y-%m-%d %H')
def minus_hour(old_date,n=1):
    new_date=pd.to_datetime(old_date)-n*Hour()
    return new_date.strftime('%Y-%m-%d %H')
def get_target_buy(raw_data,target_date):
    target_date_end=add_day(target_date)
    target_buy=raw_data[raw_data['behavior_type']==4]
    target_buy=target_buy[target_buy.time<target_date_end]
    target_buy=target_buy[target_buy.time>=target_date]
    target_buy=target_buy.loc[:,['item_id','user_id']]
    return target_buy
def get_behavior_and_hit_at_certain_time(raw_data,target_buyed,new_time):
    behavior_nums=raw_data[raw_data['time']==new_time]
    behavior_nums=behavior_nums.drop_duplicates(cols=['item_id','user_id'])
    if (behavior_nums.shape[0]==0):
        return 0,0
    else:
        # hit=behavior_nums.user_id.isin(target_buy.user_id)&behavior_nums.item_id.isin(target_buy.item_id)
        behavior_nums=behavior_nums.set_index(['user_id','item_id'])
        hit=len(behavior_nums.index.intersection(target_buyed.index))
        return behavior_nums.shape[0],hit 
    
    
	
    
##############################################################################
#test code    
if __name__=="__main__":
     print 'Good luck'
    

    
    