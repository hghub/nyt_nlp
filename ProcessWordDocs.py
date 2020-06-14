
#specific to extracting information from word documents
import os
import zipfile

#useful tool for extracting information from XML
import re

import pandas as pd

#to pretty print our xml:
import xml.dom.minidom

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

s = "123123STRINGabcabc"
print(find_between( s, "123", "abc" ))
print(find_between_r( s, "123", "abc" ))


def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


#pip install docx2txt
#pip install openpyxl
import docx2txt
import io
#the sample word document is in the folder entitled "docs"
docs_list = os.listdir("F:/Haider/RC/DS/Ali bahi/NYTimes Nexis Uni/NYTimes Nexis Uni/alldocs/")

#for doc in docs_list:
 #   print(doc)


df = pd.DataFrame(columns=["FileName","Title","Date","Length","Highlight","Body"])

for doc in docs_list:
    
    if doc != '.ipynb_checkpoints':
        print(doc)
        #print(type(doc))
        text = docx2txt.process('F:/Haider/RC/DS/Ali bahi/NYTimes Nexis Uni/NYTimes Nexis Uni/alldocs/'+doc)
        
            

        #Prints output after converting
        #print ("After converting text is ",text)

        str_list = find_between(text,"Page ", "The New York Times").splitlines()   #Page 2 of 3
        title = list(filter(None, str_list))
        #print(title)
        if (' ' in title):
            title.remove(' ')
        title = list(set(title))
        title = title[0]
        #print(title)


        date = find_between(text,"The New York Times", "Copyright 2020")
        date = date.strip()
        #print(date)
        date = date[0:findnth(date,' ',2)]
        #print(date)

        #Length: 2199 words
        length = find_between(text,"Length:", "words").strip()
        #print(length)

        highlight = find_between(text,"Highlight:", "Body").strip()
        #print(highlight)

        body = find_between(text,"Body", "End of Document").strip()
        body = body.strip('\n')
        #print(len(body))
        #if (len(body) >= 32000):
            #body = body[0:32000]
        #body = text.split("Body",1)[1].strip('\n') #
        #print(body)


        #if (re.search("(\d)",doc.strip())):
        if (re.search("\(\d+\)",doc.strip()) is None):    
            new_row = {'FileName':doc, 'Title':title, 'Date':date, 'Length':length, 'Highlight':highlight, 'Body':body}
            #append row to the dataframe
            df = df.append(new_row, ignore_index=True)
        else:
            print(doc +" is duplicate")

#print(df.head())

df.to_excel('data.xlsx', encoding="utf-8-sig")
df.shape

#content = []

#for line in text.splitlines():
  #This will ignore empty/blank lines. 
  #if line != '':
    #Append to list
    #content.append(line)

#print (content)

#with open("Output.txt", "w") as text_file:
    #text_file.write("abc")
