import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
auth=os.getenv('TOKEN')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNoYXJlX2RldnJhal9pYnRAZ3JlZW5lc3RlcC5jb20iLCJpZCI6MTgsInR5cGUiOiJBRE1JTiIsImlhdCI6MTc0NDM2MDg5MSwiZXhwIjoxNzQ0NDA0MDkxfQ.B5x3McWfRzixV6CleGiF-Ws4to8Sq4HgydBbgop2JaI',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {auth}'
}
Collections=[
  {
  "collection_description": "Salesforce",
  "collection_name": "Salesperformance",
  "collection_permission": "READ",
  "collection_type": "PUBLIC"
  }]

for collection in Collections:
  payload = json.dumps(collection)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)