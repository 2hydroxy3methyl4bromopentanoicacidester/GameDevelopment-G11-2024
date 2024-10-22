import os
import requests

def perform_search(query):
    # Define the SOAP request
    soap_envelope = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Query xmlns="urn:Microsoft.Search">
          <queryXml>{query}</queryXml>
        </Query>
      </soap:Body>
    </soap:Envelope>"""

    # Set the endpoint URL
    url = "https://portal.mpsd.ca/_vti_bin/Search.asmx"

    # Set the headers
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "urn:Microsoft.Search/Query"
    }

    # Prepare the cookies for authentication
    cookies = {
        "FedAuth": os.environ["FedAuth"]
    }

    # Send the POST request
    response = requests.post(url, data=soap_envelope, headers=headers, cookies=cookies)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text  # Return the SOAP response
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    search_query = "x"  # Modify the query as needed
    try:
        search_results = perform_search(search_query)
        print(search_results)  # Print the SOAP response
    except Exception as e:
        print(e)
