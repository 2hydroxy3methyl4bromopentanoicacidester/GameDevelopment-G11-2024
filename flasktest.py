from mitmproxy import http

TARGET_DOMAIN = "sd75.onlinelearningbc.com"

def response(flow: http.HTTPFlow) -> None:
    if TARGET_DOMAIN in flow.request.pretty_url:
        cookies = flow.response.headers.get_all("Set-Cookie")
        if cookies:
            print(f"Intercepted Cookies from {flow.request.pretty_url}:")
            for cookie in cookies:
                print(cookie)

def request(flow: http.HTTPFlow) -> None:
    if TARGET_DOMAIN in flow.request.pretty_url:
        request_cookies = flow.request.headers.get_all("Cookie")
        if request_cookies:
            print(f"Cookies sent with request to {flow.request.pretty_url}:")
            for cookie in request_cookies:
                print(cookie)
