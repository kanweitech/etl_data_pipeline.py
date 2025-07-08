import requests 
import pandas as pd
from sqlalchemy import create_engine

url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'
header = {"Content-Type": "application/json", "Accept-Encoding": "deflate"}
def main():
    res = requests.get(url, headers=header)

    data = res.json()

    df = pd.json_normalize(data)

    transform = {
      'shape': df.shape,
      'columns': df.columns,
      'view_head': df.head(),
      'view_tail': df.tail(),
      'check_duplicates': df.duplicated()
    }
    for key, value in transform.items():
      print(f"{key}: {value}")
    

if __name__ == "__main__":
  main()
  
