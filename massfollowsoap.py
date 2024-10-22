import requests

# SOAP Envelope to follow a user using SharePoint SocialDataService (older SharePoint versions)
soap_envelope = """
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <AddColleague xmlns="http://microsoft.com/webservices/SharePointPortalServer/SocialDataService">
      <accountName>{user_to_follow}</accountName>
    </AddColleague>
  </soap:Body>
</soap:Envelope>
"""

# Set the URL to your SharePoint's Social Data Service (change to your specific SharePoint server)
url = "http://portal.mpsd.ca/_vti_bin/SocialDataService.asmx"

# Headers for the SOAP request
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': '"http://microsoft.com/webservices/SharePointPortalServer/SocialDataService/AddColleague"'
}

# User to follow (replace with the actual user claims-based identifier or account name)
user_to_follow = "i:0e.t|adfs|1134503@learn75.ca"

# Format the SOAP envelope with the specific user information
formatted_envelope = soap_envelope.format(user_to_follow=user_to_follow)

# Make the SOAP request using the requests library
response = requests.post(url, data=formatted_envelope, headers=headers, auth=('username', 'password'))

# Print the response content (or handle it as needed)
print(response.text)
