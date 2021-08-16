

import pandas as pd
import numpy as np
import math

df = pd.read_csv("C://Users//admin//Desktop//Sample file//sample.csv")
df_new=pd.DataFrame()

print(df)


def impute(df):
    
    

    for i in df:
        loop=df[i].isnull().sum() / df[i].nunique()
        loop=math.ceil(loop)
        nan_cnt=(df[i].isnull().sum())-1
        item=df[i].unique()
        item=item.tolist()
        if pd.isnull(item[-1]):
            item.pop()
        l=[]

        for r in range(loop):
            for a in item:
                if len(l)<=nan_cnt:
                    l.append(a)
                else:
                    break

        item.extend(l)
        df_new[i]=item
impute(df)



print(df_new)


