import os
import requests

def get_user_profile_by_email(email):
    # Define the SOAP request
    soap_envelope = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <GetUserProfileByName xmlns="http://microsoft.com/sharepoint/soap/">
          <AccountName>{email}</AccountName>
        </GetUserProfileByName>
      </soap:Body>
    </soap:Envelope>"""

    # Set the endpoint URL
    url = "https://portal.mpsd.ca/_vti_bin/UserProfileService.asmx"

    # Set the headers
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://microsoft.com/webservices/SharePointPortalServer/UserProfileService/GetUserProfileByName",
        "Cookie": f"FedAuth={os.environ["FedAuth"]}"
    }

    # Prepare the cookies for authentication
    # cookies = {
    #     "FedAuth": os.environ["FedAuth"]
    # }

    # Send the POST request
    response = requests.post(url, data=soap_envelope, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text  # Return the SOAP response
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    email_to_lookup = "1429203@learn75.ca"  # Replace with the actual email
    try:
        user_profile = get_user_profile_by_email(email_to_lookup)
        print(user_profile)  # Print the SOAP response
    except Exception as e:
        print(e)
