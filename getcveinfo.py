import requests
import json
import pandas as pd

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
print(df.head(3))

#filtered_keys=['id','sourceidentifier']

        # Filter5ed list of dictionaries
#filtered_dict_list = [{k: v for k, v in item.items() if k in filtered_keys} for item in dictlist]

        # Convert filtered list of dictionaries to JSON string
#on_string = json.dumps(dictlist)
#print(json_string) 


                    
