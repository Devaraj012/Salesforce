import pandas as pd
from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os

load_dotenv()

# Salesforce credentials
username = os.getenv('SP_USERNAME')
password = os.getenv('SP_PASSWORD')
security_token = os.getenv('SP_SECURITY_TOKEN')

sf = Salesforce(username=username, password=password, security_token=security_token)

soql_query = """
SELECT id, transaction_id__c, transaction_date__c, sales_person__c, template__c, cust_id__c, customer_name__c,
       product_code__c, product_description__c, reference__c, UOM__c, orders__c, shipped__c, pending__c,
       unit_price__c, total__c, cust_PO__c, delivery_date__c, age__c, due_date__c, tax__c, total_tax__c,
       total_sales__c, total_paid__c, balance__c, cost__c, margin__c, markup__c, billing__c, shipping__c,
       contact__c, transaction_notes__c, Bill_City__c, Bill_State__c, BillCountry__c, bill_zip__c,
       bill_addr1__c, bill_addr2__c, Ship_City__c, ship_state__c, ShipCountry__c, Ship_Zip__c, ship_addr1__c,
       ship_addr2__c, cont_city__c, cont_state__c, cont_zip__c, contcountry__c, cont_addr1__c, cont_addr2__c,
       curr_code__c, region__c
FROM Sales_Performance__c
"""

sf_data = sf.query_all(soql_query)

# Convert results to a pandas DataFrame for easier manipulation
df = pd.DataFrame(sf_data['records'])

if 'attributes' in df.columns:
    df = df.drop(columns=['attributes'])
    
df['transaction_date__c'] = pd.to_datetime(df['transaction_date__c']).dt.strftime('%m-%d-%Y')

column_mapping = {
    'Id':'#',
    'transaction_id__c': 'Tran#',
    'transaction_date__c': 'Tran Date',
    'Sales_Person__c': 'Sales Person',
    'template__c': 'Template',
    'Cust_Id__c': 'Cust.#',
    'Customer_Name__c': 'Customer Name',
    'product_code__c': 'Prod. Code',
    'product_description__c': 'Product Description',
    'reference__c': 'Reference',
    'UOM__c': 'UOM',
    'Orders__c': 'Order',
    'shipped__c': 'Shipped',
    'pending__c': 'Pending',
    'Unit_Price__c': 'Unit Price',
    'total__c': 'Total',
    'Cust_PO__c': 'Cust. PO #',
    'Delivery_Date__c': 'Delivery Date',
    'Age__c': 'Age',
    'due_date__c': 'Due Date',
    'Tax__c': 'Tax',
    'Total_tax__c': 'Total Tax',
    'Total_sales__c': 'Total Sales',
    'Total_paid__c': 'Total Paid',
    'Balance__c': 'Balance',
    'Cost__c': 'Cost',
    'Margin__c': 'Margin',
    'Markup__c': 'Markup',
    'Billing__c': 'Billing',
    'Shipping__c': 'Shipping',
    'Contact__c': 'Contact',
    'transaction_notes__c': 'Tran.Notes',
    'Bill_City__c': 'Bill City',
    'Bill_State__c': 'Bill State',
    'BillCountry__c': 'BillCountry',
    'Bill_Zip__c': 'Bill Zip',
    'Bill_Addr1__c': 'Bill Addr1',
    'Bill_Addr2__c': 'Bill Addr2',
    'Ship_City__c': 'Ship City',
    'Ship_State__c': 'Ship State',
    'ShipCountry__c': 'ShipCountry',
    'Ship_Zip__c': 'Ship Zip',
    'Ship_Addr1__c': 'Ship Addr1',
    'Ship_Addr2__c': 'Ship Addr2',
    'cont_city__c': 'Cont City',
    'cont_state__c': 'Cont State',
    'cont_zip__c': 'Cont Zip',
    'contcountry__c': 'ContCountry',
    'cont_addr1__c': 'ContAddr1',
    'cont_addr2__c': 'ContAddr2',
    'curr_code__c': 'Curr Code',
    'Region__c': 'Region'
}

df = df.rename(columns=column_mapping)

df.to_csv('sales_performance_data.csv', index=False)

print(" ✅ Data saved to 'sales_performance_data.csv'\n")


import requests

url = "https://greenestep.giftai.co.in/api/v1/csv/upload?d_type=none&"

payload = {'collection_id': '104',
'type': 'Replace',
'fieldMapped': 'Object'}

files=[
  ('csvFile',('task.csv',open(r'C:\Users\devar\Documents\Code\Salesforce\sales_performance_data.csv','rb'),'text/csv'))
]

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRldmFyYWpAaWJhY3VzdGVjaGxhYnMuaW4iLCJpZCI6NCwidHlwZSI6IkFETUlOIiwiaWF0IjoxNzQxMzM5MDc5LCJleHAiOjE3NDEzODIyNzl9.7-6a280xHmG6MDJs_G2-jWgqVcWLLNRg-k9aiKhSqsw'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)