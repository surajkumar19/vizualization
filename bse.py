# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:48:36 2018

@author: devar
"""


from requests import get
import pandas as pd
import json
import numpy as np
import seaborn as sns
import ast


# =============================================================================
# 
# company = [500002, 500043,533272,538521,505526,524743,540190,539009,531592,500174,524590,513693,531206,511728,530243,539938,539594,532416,531512,509084,517258,590057,532689,538596,541986,542145,532435,511672,539593,531962,531359,526231,532159,522091,531518,532354,530665, 541179]
# 
# company_name = []
# stock_data = []
# 
# 
# for com in company:
#     print(com)
# 
#     
#     url ="https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?scripcode="+str(com)+"&flag=1M&fromdate=&todate=&seriesid="
#     try:
#         r = get(url)
#         data = json.loads(r.text)
#         z = json.loads(data["Data"])
#         
#         
#         
#         
#         dates = []
#         value = []
#         
#         
#         for x in z:
#             dates.append(x["dttm"])
#             value.append(float(x["vale1"]))
#         company_name.append(com)
#         stock_data.append(value)
#     except Exception as e:
#         print(e)
# 
# bse_company = pd.DataFrame({'company_name': company_name,'stock_data': stock_data})
# 
# bse_company.to_csv('bse_company_data.csv')
# =============================================================================


bse_company = pd.read_csv("bse_company_data.csv")
#bse_company = pd.DataFrame(bse_company)
    
new_com_name = []
new_stock=[]




for i in range(len(bse_company)):
    lis = ast.literal_eval(bse_company["stock_data"][i])
    if len(lis)>=20:
        new_com_name.append(bse_company["company_name"][i])
        new_stock.append(lis[:20])

bse_company_new = pd.DataFrame({'company_name': new_com_name,'stock_data': new_stock})


#np.corrcoef(result["imdb"][x], result["votes"][x])[0][1]

corr = []
for x in range(len(bse_company_new)):
    temp = []
    for y in range(len(bse_company_new)):
        temp.append(np.corrcoef(bse_company_new["stock_data"][x], bse_company_new["stock_data"][y])[0][1])
    corr.append(temp)
        
        

 
# Create a dataset (fake)
df = pd.DataFrame(corr, columns=bse_company_new["company_name"])              
#sns.heatmap(df, cmap="RdYlGn")
sns.heatmap(df, cmap="RdYlGn",vmin=-1, vmax=1)
sns.plt.show()        
        
        
        
        
        
        
        
        
        
        
        
        