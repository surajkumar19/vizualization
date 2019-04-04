# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:59:49 2018

@author: devar
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, metrics 
from pandas import DataFrame
import statsmodels.api as sm


# =============================================================================
# 

data =  pd.read_csv("movie_100_years_1.csv")
data_votes = data[data['votes'] >= 1000 ]
final =  pd.DataFrame(data_votes.groupby('year')['imdb'].apply(list))
final_2 =  pd.DataFrame(data_votes.groupby('year')['votes'].apply(list))
final = pd.concat([final, final_2], axis=1, sort=False)
final.reset_index(level=0, inplace=True)


mean = []
for x in final["imdb"]:
    mean.append(np.mean(x))


result = pd.concat([final, pd.DataFrame({'mean': mean})], axis=1, sort=False)
result["Gain"] = (result['mean'].pct_change())
result["Gain"][0] = 0


max_gain_year_index = result["Gain"].idxmax()


result["year"][:-1]
result["year"][-1:]

# =============================================================================

# =============================================================================
# X_train, X_test, y_train, y_test = list(result["year"][:-1]), list(result["Gain"][:-1]), list(result["year"][-1:]), list(result["Gain"][-1:])
# 
# reg = linear_model.LinearRegression() 
#   
# # train the model using the training sets 
# reg.fit(X_train, y_train) 
#   
# # regression coefficients 
# print('Coefficients: \n', reg.coef_) 
#   
# # variance score: 1 means perfect prediction 
# print('Variance score: {}'.format(reg.score(X_test, y_test))) 
# 
# =============================================================================
# =============================================================================




Stock_Market = {'Year': list(result["year"][:-1]),'mean': list(result["mean"][:-1]) }       
                

df = DataFrame(Stock_Market,columns=['Year','mean'])


X = df[['Year']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['mean']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# prediction with sklearn
New_Interest_Rate = list(result["year"][-1:])[0]
New_Unemployment_Rate =  list(result["Gain"][-1:])[0]
print ('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate]]))


# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

# =============================================================================

corr = []

for x in range(len(result)):
    corr.append(np.corrcoef(result["imdb"][x], result["votes"][x])[0][1])    

corr_df = pd.DataFrame({'corr': corr})
corr_df["corr_gain"] = (corr_df['corr'].pct_change())


