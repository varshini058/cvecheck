import requests

url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?lastModStartDate=2024-05-08T13:00:00.000%2B01:00&lastModEndDate=2024-05-10T13:36:00.000%2B01:00"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
