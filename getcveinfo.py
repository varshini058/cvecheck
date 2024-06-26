import requests
import json
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?lastModStartDate=2024-05-08T13:00:00.000%2B01:00&lastModEndDate=2024-05-10T13:36:00.000%2B01:00"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

nested_json = response.json()

# Function to filter nested JSON
def filter_nested_json(nested_json):
    filtered_data = nested_json ['vulnerabilities']
    print(type(filtered_data))
    return filtered_data
    
# Filter the nested JSON
filtered_json = filter_nested_json(nested_json)

# Print or do whatever you need with the filtered JSON
jsonlist =json.dumps(filtered_json, indent=4)
dictlist =json.loads(jsonlist)
#print(dictlist)

idlist=[]
df = pd.DataFrame(columns=["id", "sourceIdentifier","published","published","lastModified","vulnStatus"])
for item in dictlist:
    #print(item)
    #print(item['cve'] ['id'])
    iddict = {"id":item['cve'] ['id'],"sourceIdentifier":item['cve'] ['sourceIdentifier'],"published": item['cve']['published'],"lastModified": item['cve']['lastModified'],"vulnStatus":item['cve']['vulnStatus']}
    idlist.append(iddict)
     
     
#print(idlist)    
df = pd.DataFrame(idlist)
#print(df.head(3))

//code to connect to mysql database and creating cve_summary table
engine = create_engine('mysql+mysqlconnector://[user]:[pass]@[host]:[port]/[schema]', echo=False)
df.to_sql(name='cve_summary', con=engine, if_exists = 'append', index=False)
                    
