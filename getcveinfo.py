import requests
import json

url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?lastModStartDate=2024-05-08T13:00:00.000%2B01:00&lastModEndDate=2024-05-10T13:36:00.000%2B01:00"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

nested_json = response.json()

# Function to filter nested JSON
def filter_nested_json(nested_json):
    filtered_data = []
    for item in nested_json['items']:
        filtered_item = {
            'id': item['nested']['id'],
            'sourceid': item['nested']['sourceIdentifier'],
            'publish' : item['nested']['published'], 
            'lastmod' : item['nested']['lastModified'],
            'status' : item['nested']['vulnStatus']
            # Add more keys as needed
        }
        filtered_data.append(filtered_item)
    return filtered_data

# Filter the nested JSON
filtered_json = filter_nested_json(nested_json)

# Print or do whatever you need with the filtered JSON
print(json.dumps(filtered_json, indent=4))

