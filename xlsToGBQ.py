
import pandas as pd
import pandas_gbq
import os
#from google.cloud.bigquery.client import Client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'F:\Haider\RC\DS\gcp key\storage-api-project-762431441781-11e093e0a1ac.json'

xls = pd.ExcelFile('dataFromGCS.xlsx')
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head(3))

df.columns = ['FileName_String','Title_string','Date_date','Length_int64','Highlight_string','Body_string','SentimentScore_float64','SentimentMagnitude_float64']


table_id = 'my_dataset.new_table'

df.to_gbq(table_id)

df.describe(include='all')