import requests 
import pandas as pd

url = 'https://full-stack-bookstore-mern-backend.vercel.app/api/books'

def main():
    res = requests.get(url)

    data = res.json()

    df = pd.DataFrame(data)

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
  
