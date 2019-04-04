# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:48:36 2018

@author: devar
"""


from requests import get
import pandas as pd
import json

company = [500002,500043,533272,538521,505526,524743,540190,539009,531592,500174,524590,513693,531206,511728,530243,539938,539594,532416,531512,509084,517258,590057,532689,538596,541986,542145,532435,511672,539593,531962,531359,526231,532159,522091,531518,532354,530665, 541179]

company_name = []
stock_data = []


#x = company[5]
x = 539009
url ="https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w?scripcode="+str(x)+"&flag=1M&fromdate=&todate=&seriesid="
try:
    r = get(url)
    data = json.loads(r.text)
    z = json.loads(data["Data"])
    company_name.append(x)
    
    
    
    dates = []
    value = []
    
    
    for x in z:
        dates.append(x["dttm"])
        value.append(float(x["vale1"]))
    
    stock_data.append(value)
except Exception as e:
    print(e)

bse_company = pd.DataFrame({'company_name': company_name,
                              'stock_data': stock_data})
