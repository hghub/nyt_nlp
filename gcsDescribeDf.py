
import pandas as pd
import pandas_gbq
import os
#from google.cloud.bigquery.client import Client

xls = pd.ExcelFile('dataFromGCS.xlsx')
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(df.head(3))



print(df.describe(include='all'))