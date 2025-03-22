import pandas as pd
from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

load_dotenv()

# Credentials (Replace with your actual values)
username = os.getenv('SP_USERNAME')
password = os.getenv('SP_PASSWORD')
security_token = os.getenv('SP_SECURITY_TOKEN')

# Connect to Salesforce
sf = Salesforce(username=username,password=password,security_token=security_token)

# SOQL Query (Example: Retrieve all Accounts)
soql_query = "SELECT Id, CaseNumber, Subject, Status, Origin, CreatedDate, ClosedDate FROM Case"

# Execute Query
query_result = sf.query_all(soql_query)

# Create Pandas DataFrame
df = pd.DataFrame(query_result['records']).drop(columns='attributes')  # Remove extra metadata

# Explore Data (Optional)
print(df.head())

# Save to CSV
#df.to_csv("salesforce_Cases.csv", index=False)