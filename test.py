import requests

SESSION = "3m_euCelChS8wJ-u6N4aXc1zaVYpP3HvGBWfFAiD.mbcprd01a000007"
GATEWAY = "83319066d98520c427a532c0b3064cef"

print(requests.get("https://myeducation.gov.bc.ca/aspen/portalStudentDetail.do?navkey=myInfo.details.detail", cookies={
    "JSESSIONID":SESSION, 
    "deploymentId": "aspen",
    "ApplicationGatewayAffinity": GATEWAY,
    "ApplicationGatewayAffinityCORS": GATEWAY
    }).text)