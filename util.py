# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:38:08 2015

@author: xujingping, simin
"""

import pandas as pd


def list2csv(li,filename):
    li1=[]
    li2=[]
    for item in li:
        li1.append(item[0])
        li2.append(item[1])
    df=pd.DataFrame({'user_id':li1, 'item_id':li2})
    df.to_csv(filename,index=False)
      

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
    
    
def extract_itemfeature(user_file,filename="feature_item.csv"):
    #load data
    raw_data=pd.read_table(user_file)
    #buy_numbers
    buy    =raw_data[raw_data['behavior_type']==4]
    target_item = pd.read_table('tianchi_mobile_recommend_train_item.csv',sep=',')
    #buy_numbers
    buy_target_item=pd.merge(target_item, buy, how='inner', on='item_id', left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True) 
    item_buy_num = buy_target_item['item_id'].value_counts()
    item_buy_num.to_csv(filename)   

	
def extract_userfeature(train_file,feature_file="feature_user.csv"):
    """
      Input:
          user_file:
      Output:file  
    """
    
    #load data      
    feature_user=pd.read_csv(feature_file)
    train_data=pd.read_csv(train_file)

    #购买量
    feature_user=user_buynums(train_data,feature_user)
    #购物车量
    feature_user=user_cartnums(train_data,feature_user)
    #收藏量
    feature_user=user_shoucangnums(train_data,feature_user)
    #点击量
    feature_user=user_clicknums(train_data,feature_user) 
    #点击购买比
    pass
    #收藏购买比
    pass
    #购物车购买比
    pass

    #保存
    feature_user.to_csv(feature_file,index=False)
    
    
    
def merge_feature(userfeature_file="feature_user.csv",itemfeature_file="feature_item.csv",useritemfeature_file="feature_useritem.csv",feature_file="featues_train.csv"):
    #load data
    user_feature=pd.read_csv(userfeature_file)
    item_feature=pd.read_csv(itemfeature_file)
    useritem_feature=pd.read_csv(useritemfeature_file)
    #merge
    useritem_feature=pd.merge(useritem_feature,user_feature)
    useritem_feature=pd.merge(useritem_feature,item_feature)
    
    #save 
    useritem_feature.to_cvs(feature_file)  
    
def cut_traindata(traindata_file,date_cut,pre_traindata,post_traindata):
    #load data
    traindata=pd.read_csv(traindata_file)
    pre=traindata[traindata.date<date_cut]
    post=traindata[traindata.date>=date_cut]
    pre.to_csv(pre_traindata)
    post.to_csv(post_traindata)
    
    
    
"""
Defined the subfunction in this section 

"""
def sample_user(user_file,sample_user):
    df=pd.read_csv(user_file)
    user_id=df.user_id.unique()
    li=user_id.tolist()
    df=pd.DataFrame({'user_id':li})
    df.to_csv(sample_user,index=False)    
    
def sample_item(item_file,sample_item):
    df=pd.read_csv(item_file)
    user_id=df.item_id.unique()
    li=user_id.tolist()
    df=pd.DataFrame({'item_id':li})
    df.to_csv(sample_user,index=False)    
    
    

##############################################################################
####提取特征的子函数############

##user features ##  
def user_buynums(user_data,feature_user):
    item_buy=user_data.loc[:,['user_id','behavior_type']]
    item_buy=item_buy[item_buy.behavior_type==4]
    item_buy.behavior_type=1
    item_buy=item_buy.groupby("user_id").sum()
    item_buy['user_id']=item_buy.index
    item_buy['buy_nums']=item_buy.behavior_type
#    item_buy=item_buy.loc[:,['user_id','buy_num']]
    del item_buy['behavior_type']
    feature_user=pd.merge(feature_user,item_buy,how='outer',on=None) 
    feature_user.fillna(0)
    return feature_user
    
def user_cartnums(user_data,feature_user):
    item_buy=user_data.loc[:,['user_id','behavior_type']]
    item_buy=item_buy[item_buy.behavior_type==3]
    item_buy.behavior_type=1
    item_buy=item_buy.groupby("user_id").sum()
    item_buy['user_id']=item_buy.index
    item_buy['cart_nums']=item_buy.behavior_type
#    item_buy=item_buy.loc[:,['user_id','buy_num']]
    del item_buy['behavior_type']
    feature_user=pd.merge(feature_user,item_buy,how='outer',on=None) 
    feature_user.fillna(0)
    return feature_user
    
def user_clicknums(user_data,feature_user):
    item_buy=user_data.loc[:,['user_id','behavior_type']]
    item_buy=item_buy[item_buy.behavior_type==1]
    item_buy.behavior_type=1
    item_buy=item_buy.groupby("user_id").sum()
    item_buy['user_id']=item_buy.index
    item_buy['click_nums']=item_buy.behavior_type
#    item_buy=item_buy.loc[:,['user_id','buy_num']]
    del item_buy['behavior_type']
    feature_user=pd.merge(feature_user,item_buy,how='outer',on=None) 
    feature_user.fillna(0)
    return feature_user
    
def user_shoucangnums(user_data,feature_user):
    item_buy=user_data.loc[:,['user_id','behavior_type']]
    item_buy=item_buy[item_buy.behavior_type==2]
    item_buy.behavior_type=1
    item_buy=item_buy.groupby("user_id").sum()
    item_buy['user_id']=item_buy.index
    item_buy['shoucang_nums']=item_buy.behavior_type
#    item_buy=item_buy.loc[:,['user_id','buy_num']]
    del item_buy['behavior_type']
    feature_user=pd.merge(feature_user,item_buy,how='outer',on=None) 
    feature_user.fillna(0)
    return feature_user

# 提取ylabel
def extract_ylabel(user_id_file,item_id_file,train_data_file,lable_file):
    user_id=pd.read_csv(user_id_file)
    item_id=pd.read_csv(item_id_file)
    train_data=pd.read_csv(train_data_file)
    train_data=train_data[train_data.behavior_type==4]
    label=train_data.loc[:,['user_id','item_id']]
    ylabel=pd.merge(user_id,item_id)
    ylabel=pd.merge(ylabel,label)
    #save 
    ylabel.to_csv(lable_file)
    #merge
    
def item_buynums(item_feature,item_data):

    return item_feature
    
##############################################################################
#test code    
if __name__=="__main__":
    sample_user('tianchi_mobile_recommend_train_user.csv','feature_user.csv')
    extract_userfeature('train_data.csv')
   # sample_user('train_data.csv','feature_user.csv')
    
    #test evaluate_model
   # print evaluate_model("test_label.csv","predict_label.csv")
   # sample_item('tianchi_mobile_recommend_train_item.csv','item_feature.csv')

    
    #
    
    