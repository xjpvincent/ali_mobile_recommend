# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:38:08 2015

@author: xujingping
"""

import pandas as pd
import csv


def list2csv(li,filename):
    li1=[]
    li2=[]
    for item in li:
        li1.append(item[0])
        li2.append(item[1])
    df=pd.DataFrame({'user_id':li1, 'item_id':li2})
    df.to_csv(filename,index=False)

def loaddata():
    train_data=pd.read_csv("")
    test_data=pd.read_csv()
      

def data2lable(test_data_file,filename):
    test_data=pd.read_csv(test_data_file)
    test_data=test_data.set_index(['user_id' ,'item_id'])
    test_data=test_data[test_data.behavior_type==4]
    user_item=test_data.index.unique()
    list2csv(user_item,filename)
    return "success"

#mask behavior
def data2useritem(data_file,filename,behavior):
    test_data=pd.read_csv(data_file)
    test_data=test_data.set_index(['user_id' ,'item_id'])
    test_data=test_data[test_data.behavior_type==behavior]
    user_item=test_data.index.unique()
    list2csv(user_item,filename)
    return "success"
    
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
    

def exact_userfeature(user_file,feature_file):
    """
      Input:
          user_file:
      Output:file    
    """
    #load data
    user_data=pd.read_csv(user_file)
    feature_data=pd.read_csv(feature_file)
    #buy_numbers
    
    
    
    #save feature_data
    feature_data.to_csv(feature_file,index=False)    
    pass


    
def extract_userfeature(user_file  ,feature_file=none):
	  """
      Input:
          item_file:
      Output:file   
      """
	#load data
	raw_data=pd.read_table(user_file,sep=',')
	#buy_numbers
	buy    =raw_data[raw_data['behavior_type']==4]

	target_item = pd.read_table('tianchi_mobile_recommend_train_user_Item2BPredict.csv',sep=',')
	#buy_numbers
	buy_target_item=pd.merge(target_item, buy, how='inner', on='item_id', left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True)

	item_buy_num = buy_target_item['item_id'].value_counts() 
	item_buy_num.to_csv('feature_file_item.csv')    

	pass
	
def extract_userfeature(user_file  ,feature_file=none):
    """
      Input:
          user_file:
      Output:file   """
    #load data
    raw_data=pd.read_table(user_file,sep=',')
    #buy_numbers
    buy    =raw_data[raw_data['behavior_type']==4]

    user_buy_num=buy['user_id'].value_counts() 
    user_buy_num.to_csv('feature_file_user.csv')   
    pass
    
    
def merge_feature(user_feature,item_feature,useritem_feature,feature_file):
    
    pass
    
    
    
"""
Defined the subfunction in this section 
"""
def sample_user(user_file,sample_user):
    
    
def sample_item(item_file,sample_item):
    
    

#test code    
if __name__=="__main__":
    
    #test evaluate_model
    print evaluate_model("test_label.csv","predict_label.csv")
    
    
