# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:38:08 2015

@author: xujingping, simin
"""

import pandas as pd
import numpy as np


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
    
    
def extract_itemfeature(train_data_file,item_file,feature_file="feature_user.csv"):
    train_data=pd.read_csv(train_data_file)
    item_data=pd.read_csv(item_file)
    feature_item=pd.DataFrame({'item_id':item_data.item_id.unique()})
    
    #
    feature_item=item_buynums(train_data,feature_item)
    
    
    #load data
        #保存
    feature_item.to_csv(feature_file,index=False)

  
	
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

def extract_useritemfeature(train_file="train_data.csv",feature_file="feature_useritem.csv"):
    #load data
    df=pd.read_csv(train_file)
    ui=df.groupby(['user_id','item_id']).sum()
    ui=ui.index.tolist()
    li_user=[]
    li_item=[]
    for tmp in ui:
        li_user.append(tmp[0])
        li_item.append(tmp[1])
    feature_useritem=pd.DataFrame({'user_id':li_user,'item_id':li_item})
    feature_useritem['key']=ui    
    #cart7
    ui=df.loc[:,['user_id','item_id','behavior_type']]   
    ui=ui[ui.behavior_type>1]
    
    f1=ui.groupby(['user_id','item_id']).mean()
    f1['key']=f1.index.tolist()    
    feature_useritem=pd.merge(feature_useritem,f1,how='outer',on='key')
    #save data
    feature_useritem.to_csv(feature_file,index=False)
    
    
def merge_feature(userfeature_file="feature_user.csv",itemfeature_file="feature_item.csv",label_file="train_label.csv",useritemfeature_file="feature_useritem.csv",feature_file="featues_train.csv"):
    #load data
    user_feature=pd.read_csv(userfeature_file)
    item_feature=pd.read_csv(itemfeature_file)
    useritem_feature=pd.read_csv(useritemfeature_file)
    train_label=pd.read_csv(label_file)
    #merge
    useritem_feature=pd.merge(useritem_feature,user_feature,how='outer',on='user_id')
    useritem_feature=pd.merge(useritem_feature,item_feature,how='outer',on='item_id')
    useritem_feature=pd.merge(useritem_feature,train_label,how='outer',on=['user_id','item_id'])
    #save 
    useritem_feature=useritem_feature.fillna(0)
    useritem_feature.to_cvs(feature_file,index=False)  
    
#cut the train data from date_cut    
def cut_traindata(traindata_file,date_cut,pre_traindata,post_traindata):
    #load data
    traindata=pd.read_csv(traindata_file)
    pre=traindata[traindata.time<date_cut]
    post=traindata[traindata.time>=date_cut]
    pre.to_csv(pre_traindata,index=False)
    post.to_csv(post_traindata,index=False)
    
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



def sample_ui(user_file,item_file,sample_user_item):
    df1=pd.read_csv(user_file)
    df2=pd.read_csv(item_file)
    user_id=df1.user_id.unique().tolist()
    del df1
    item_id=df2.item_id.unique().tolist()
    del df2
    user_id_extend=[]
    for i in range(len(item_id)):
        user_id_extend.extend(user_id)
    print 'user_id'

    item_id_extend=[]
    for i in range(len(user_id)):
        item_id_extend.extend(item_id)
        
    user_item=pd.DataFrame({'user_id':user_id_extend,'item_id':item_id_extend})       
    del user_item
    del user_id
    del item_id
    

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

##item features ##  
def item_buynums(user_data,feature_item):
    item_buy=user_data.loc[:,['item_id','behavior_type']]
    item_buy=item_buy[item_buy.behavior_type==4]
    item_buy.behavior_type=1
    item_buy=item_buy.groupby("item_id").sum()
    item_buy['item_id']=item_buy.index
    item_buy['buyed_nums']=item_buy.behavior_type
#    item_buy=item_buy.loc[:,['user_id','buy_num']]
    del item_buy['behavior_type']
    filter_item=pd.DataFrame({'item_id':feature_item.item_id})
    #filter
    item_buy=pd.merge(filter_item,item_buy,how='inner',on='item_id')
    feature_item=pd.merge(feature_item,item_buy,how='outer',on=None) 
    feature_item.fillna(0)
    return feature_item
# 提取ylabel
def extract_ylabel(train_data_file,item_id_file,lable_file):
    train_data=pd.read_csv(train_data_file)
    item_id=pd.read_csv(item_id_file)
    item_filter=pd.DataFrame({'item_id':item_id.item_id.unique()})
    train_data=train_data[train_data.behavior_type==4]
    ylabel=train_data.loc[:,['user_id','item_id']]    
    ylabel=pd.merge(ylabel,item_filter)
    ylabel['label']=np.ones(len(ylabel))
    #save 
    ylabel.to_csv(lable_file,index=False)
    #merge

    
##############################################################################
#test code    
if __name__=="__main__":
    
    #split the train data
    cut_traindata('tianchi_mobile_recommend_train_user.csv','2014-12-17','test_data.csv','test_data_lable.csv')
    cut_traindata('test_data.csv','2014-12-16','train_data.csv','train_label_data.csv')
    #extract user feature
    extract_userfeature(train_file='train_data.csv',feature_file="feature_user.csv")
    #extract item feature
    extract_itemfeature(train_data_file='train_data.csv',item_file='tianchi_mobile_recommend_train_item.csv',feature_file="feature_item.csv")
    #extract user_item feature
    extract_useritemfeature(train_file="train_data.csv",feature_file="feature_useritem.csv")
    #extract ylabel
    extract_ylabel('train_data.csv','tianchi_mobile_recommend_train_item.csv','train_label.csv')
    merge_feature(userfeature_file="feature_user.csv",itemfeature_file="feature_item.csv",label_file="train_label.csv",useritemfeature_file="feature_useritem.csv",feature_file="featues_train.csv")
    #extract user feature

    #sample_user('tianchi_mobile_recommend_train_user.csv','feature_user.csv')
   # extract_userfeature('train_data.csv')
   # sample_user('train_data.csv','feature_user.csv')
 
    
    #test evaluate_model
   # print evaluate_model("test_label.csv","predict_label.csv")
   # sample_item('tianchi_mobile_recommend_train_item.csv','item_feature.csv')

    
    