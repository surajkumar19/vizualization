# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:03:16 2018

@author: devar
"""

import pandas as pd
import seaborn as sns

# =============================================================================

data =  pd.read_csv("movie_100_years_1.csv")
data_votes = data[data['votes'] >= 10000 ]

# =============================================================================


# Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
sns_plot  = sns.jointplot(x=data_votes["imdb"], y=data_votes["votes"], kind='scatter')
sns_plot.savefig("output.svg")


# =============================================================================
# 
# sns.jointplot(x=data_votes["imdb"], y=data_votes["votes"], kind='hex')
# sns.jointplot(x=data_votes["imdb"], y=data_votes["votes"], kind='kde')
# # Then you can pass arguments to each type:
# sns.jointplot(x=data_votes["imdb"], y=data_votes["votes"], kind='scatter', s=200, color='m', edgecolor="skyblue", linewidth=2)
#  
# # Custom the color
# sns.set(style="white", color_codes=True)
# sns.jointplot(x=data_votes["imdb"], y=data_votes["votes"], kind='kde', color="skyblue")
# =============================================================================
