import os
import requests

# SOAP request body (SOAP 1.1 example)
soap_body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <authentication xmlns="http://schemas.microsoft.com/sharepoint/dsp">YOUR_AUTH_XML</authentication>
    <dataRoot allowRemoteDataAccess="false" xmlns="http://schemas.microsoft.com/sharepoint/dsp">
      <root>https://portal.mpsd.ca/sites/hello/FILES</root>
    </dataRoot>
    <request document="content" method="query" xmlns="http://schemas.microsoft.com/sharepoint/dsp" />
    <versions xmlns="http://schemas.microsoft.com/sharepoint/dsp">
      <version>1.0</version>
      <version>2.0</version>
    </versions>
  </soap:Header>
  <soap:Body>
    <queryRequest xmlns="http://schemas.microsoft.com/sharepoint/dsp">
      <dsQuery select="*" resultContent="both" columnMapping="element">
        <Query RowLimit="10">
          <Fields>
            <Field>Name</Field>
            <Field>Modified</Field>
          </Fields>
        </Query>
      </dsQuery>
      <ptQuery />
    </queryRequest>
  </soap:Body>
</soap:Envelope>"""

# SharePoint service URL
url = "https://portal.mpsd.ca/_vti_bin/DspSts.asmx"

# Headers for SOAP 1.1 request
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://schemas.microsoft.com/sharepoint/dsp/queryRequest"
}

# Extract authentication token (e.g., FedAuth) from environment variables
fedauth_token = "77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MGUudHxhZGZzfDE0MjkyMDNAbGVhcm43NS5jYSwwZS50fGFkZnN8MTQyOTIwM0BsZWFybjc1LmNhLDEzMzc0MTg0NzcyNjYyMTA4NCxUcnVlLEFrY0FOeU4wejdyczlUdWI2TE4vanZkeFVPQUttelpJTUE5M2h1UjhjeHlTa3VDZWVsTjJGWGtjTzFmQWtTcEprRGxwWVNkUEFsekVJUEl0eFplVytMS2ZFamJkT2tjdFFYL2NlUjRrRWgzTlNOZ0FxN1VOMXc2WXJwYkYzdVI5cHZUVGx6TGlyMkpvV0gyNmJDSnZScU1DRGl5VENsaG5zZVdsVjVqbW9Udm1xZXdWbFFtcXRZNktZb2YybnQrYnFhdTFQNHZEWnVQMXlHN24wTFVNZ0RTU2M0NGptMENxMW9ab0JQSE1ld3F0aFNUdCsvRklGVXNvWVNDamlvQ1kvclIyV3lrbE12M0dydlpOL2tuRytlcWZNbkJncUEwSHBiK0wvK20vRXdhejlRUGl6c1YvQUZGQ3pYVGI4UFpzVmRwNGwwWHhpbjhXT1NORXhQVmhJUT09LGh0dHBzOi8vcG9ydGFsLm1wc2QuY2EvPC9TUD4="#os.environ.get("FedAuth")

# Include FedAuth token in cookies if required
cookies = {
    "FedAuth": fedauth_token
}

# Send the request
response = requests.post(url, data=soap_body, headers=headers, cookies=cookies)

# Print response status and body
print("Status Code:", response.status_code)
print("Response Text:", response.text)
