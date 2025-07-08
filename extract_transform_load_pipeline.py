import requests 
import pandas as pd
from sqlalchemy import create_engine

# Extraction of data from a Rest API

url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'

header = {"Content-Type": "application/json", "Accept-Encoding": "deflate"}

res = requests.get(url, headers=header)

data = res.json()

df = pd.json_normalize(data)


# Transformation of the data(Cleaning, filtering, removal of duplicates and removal of inconsistent data)

print(df.shape)
print(df.columns)
print(df.head())
print(df.tail())
print(df.duplicated())

# Loading of data to a new source(database, data lake or etc)

#engine = create_engine('mssql+pyodbc://Servername/databasename?driver+SQL+Server+Native+Client+11.0')

#df.to_sql(name='Tablename', con=engine, index=False, if_exists='fail/replace/append')

#fail - if it's a new database
#replace - if you want to replace an already existing database
#append - if you want to increment the database
