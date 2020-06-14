
import pandas as pd
from google.cloud import storage
import os
#from google.cloud.bigquery.client import Client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'F:\Haider\RC\DS\gcp key\storage-api-project-762431441781-11e093e0a1ac.json'
storage_client = storage.Client()
xls = pd.ExcelFile('gs://ds_bucket_nyt/data-full.xlsx')
df = xls.parse('Sheet1', index_col=None, na_values=['NA'])

#df['Sentiment'] = []
sentiment_score_list = []
sentiment_magnitude_list = []

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

for index, row in df.iterrows():
    #print(row['c1'], row['c2'])
    # The text to analyze
    text = row['Body']#u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    sentiment_score_list.append(sentiment.score)
    sentiment_magnitude_list.append(sentiment.magnitude)
    #df[index]['Sentiment'] = sentiment.score


#df.drop(columns=['Unnamed: 0'])

df['SentimentScore'] = sentiment_score_list
df['SentimentMagnitude'] = sentiment_magnitude_list

df.to_excel('dataFromGCS.xlsx', encoding="utf-8-sig")
df.shape
