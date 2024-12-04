import requests, os, xml.dom.minidom


soap_body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://schemas.microsoft.com/sharepoint/soap/">
    <soap:Body>
        <tns:SearchPrincipals>
            <tns:searchText>.</tns:searchText> <!-- Use '*' to return all users -->
            <tns:maxResults>1099999999</tns:maxResults> <!-- Maximum number of results to return -->
            <tns:principalType>All</tns:principalType> <!-- Search for all principal types -->
        </tns:SearchPrincipals>
    </soap:Body>
</soap:Envelope>
"""

uri = "https://portal.mpsd.ca/_vti_bin/People.asmx"
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://schemas.microsoft.com/sharepoint/soap/SearchPrincipals",
    "Cookie": f"FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MGUudHxhZGZzfDE0MjkyMDNAbGVhcm43NS5jYSwwZS50fGFkZnN8MTQyOTIwM0BsZWFybjc1LmNhLDEzMzc0MTg0NzcyNjYyMTA4NCxUcnVlLEFrY0FOeU4wejdyczlUdWI2TE4vanZkeFVPQUttelpJTUE5M2h1UjhjeHlTa3VDZWVsTjJGWGtjTzFmQWtTcEprRGxwWVNkUEFsekVJUEl0eFplVytMS2ZFamJkT2tjdFFYL2NlUjRrRWgzTlNOZ0FxN1VOMXc2WXJwYkYzdVI5cHZUVGx6TGlyMkpvV0gyNmJDSnZScU1DRGl5VENsaG5zZVdsVjVqbW9Udm1xZXdWbFFtcXRZNktZb2YybnQrYnFhdTFQNHZEWnVQMXlHN24wTFVNZ0RTU2M0NGptMENxMW9ab0JQSE1ld3F0aFNUdCsvRklGVXNvWVNDamlvQ1kvclIyV3lrbE12M0dydlpOL2tuRytlcWZNbkJncUEwSHBiK0wvK20vRXdhejlRUGl6c1YvQUZGQ3pYVGI4UFpzVmRwNGwwWHhpbjhXT1NORXhQVmhJUT09LGh0dHBzOi8vcG9ydGFsLm1wc2QuY2EvPC9TUD4="
}

response = requests.post(uri, data=soap_body, headers=headers)

def Update(message, impl, args, oncomplete=None):
    print(message)
    t = threading.Thread(target=impl, args=args)
    t.start()
    val = t.join()
    print(oncomplete or "Done " + str(message))
    return val


print(response.status_code)
with open("output_users_SHAREPOINT.xml", "w") as write:
    #print("parsing")
    dom = Update("Parsing", xml.dom.minidom.parseString, (response.text))
    #print("parsed. prettifying")
    pretty_xml_as_string = Update("Prettifying", dom.toprettyxml, ())
    print("formatted. writing to file.")
    write.write(pretty_xml_as_string)
    print("success.")
