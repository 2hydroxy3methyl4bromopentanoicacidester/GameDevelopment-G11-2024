import requests, os

# SharePoint site and Lists.asmx endpoint
site_url = "https://portal.mpsd.ca/_vti_bin/Lists.asmx"

# SOAP request envelope
soap_envelope = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetListCollection xmlns="http://schemas.microsoft.com/sharepoint/soap/" />
  </soap:Body>
</soap:Envelope>"""

# Define the headers including the SOAPAction
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://schemas.microsoft.com/sharepoint/soap/GetListCollection',
    'Cookie': f'FedAuth={os.environ["FedAuth"]}',
}

# Send the SOAP request
response = requests.post(site_url, data=soap_envelope, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Output the raw XML response
    print(response.text)
else:
    print(f"Error: {response.status_code}")
