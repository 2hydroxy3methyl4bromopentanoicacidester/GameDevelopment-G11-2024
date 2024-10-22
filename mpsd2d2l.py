import requests, base64, os

FEDAUTH = os.environ.get("FedAuth")

initialSamlURL = "https://sd75.onlinelearningbc.com/d2l/lp/auth/saml/initiate-login?entityId=https%3a%2f%2fsts.windows.net%2fa11cb0cc-27e5-4187-a8c9-82384c872f52%2f"


def GetFedAuth(username, password):
    req = requests.get("https://portal.mpsd.ca/my/Pages/Hub.aspx#/=", headers={"Authorization": base64.b64encode(
        bytes(":".join([username, password]), 'utf-8')
            ).decode('utf-8')})
    return req

dummyheaders = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://sd75.onlinelearningbc.com/d2l/login",
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}


def InitializeSaml():
    request = requests.get(initialSamlURL, allow_redirects=False)
    # print(request)
    # print(request.headers)
    return request.headers["location"]

def SamlStage2(url): # url = InitializeSaml() retrn value
    req = requests.get(url, allow_redirects=False)
    return req

def Saml():
    return requests.get(initialSamlURL, cookies={"FedAuth": FEDAUTH}, allow_redirects=True)
# def SamlLogin():

# print(GetFedAuth(USERNAME, PASSWORD).headers)
# print(SamlStage2(InitializeSaml()).headers)
def CheckHome(samlreq):
    return requests.get("https://sd75.onlinelearningbc.com/d2l/home", cookies=samlreq.cookies)
# response = Saml()
# for header in response.cookies:
#     print(header)

samlreq = Saml()
homereq = CheckHome(samlreq)
print(samlreq)
print(samlreq.url)
print(samlreq.text)
print(homereq)
print(homereq.url)
print(homereq.headers)
print(len(homereq.cookies))
for cookie in homereq.cookies:
    print(cookie)
# print(InitializeSaml())