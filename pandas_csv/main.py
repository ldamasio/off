import pandas as pd
import requests
import json
import time


url='http://localhost:8002/api/create/'

df = pd.read_csv('off.csv', sep='\t', engine='python', on_bad_lines='skip')
for index in range(len(df)):
    code = df.iloc[index, 0] or "No data returned"
    product_name = df.iloc[index, 6] or "No data returned"
    quantity = df.iloc[index, 27] or "No data returned"
    brands = df.iloc[index, 31] or "No data returned"
    categories = df.iloc[index, 34] or "No data returned"
    labels = df.iloc[index, 36] or "No data returned"
    stores = df.iloc[index, 40] or "No data returned"
    ingredients_text = df.iloc[index, 58] or "No data returned"
    traces = df.iloc[index, 71] or "No data returned"
    serving_size = df.iloc[index, 28] or "No data returned"
    nutriscore_score = df.iloc[index, 289] or "No data returned"
    nutriscore_grade = df.iloc[index, 90] or "No data returned"
    data = {
      "code": str(code), 
      "product_name": str(product_name),
      "quantity": str(quantity),
      "brands": str(brands),
      "categories": str(categories),
      "labels": str(labels),
      "stores": str(stores),
      "ingredients_text": str(ingredients_text),
      "traces": str(traces),
      "serving_size": str(serving_size),
      "nutriscore_score": str(nutriscore_score),
      "nutriscore_grade": str(nutriscore_grade)
    }
    r = requests.post(
      url,
      data=json.dumps(data),
      headers={"Content-Type": "application/json"},
    )
    print(r.status_code, r.reason)
    time.sleep(0.3)



