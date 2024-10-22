import requests, threading, time

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Length": "44",
    "Content-Type": "application/json",
    "Origin": "https://downforeveryoneorjustme.com",
    "Priority": "u=1, i",
    "Referer": "https://downforeveryoneorjustme.com/bing",
    "Sec-CH-UA": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "same-origin",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.3"
}

def reportBing():
    print(requests.post("https://downforeveryoneorjustme.com/api/report-problem", data={"problem_category_id":"22","service_id":22}, headers=headers).text)

print("spawning threads")
for i in range(1):
    threading.Thread(target=reportBing).start()
print("spawned threads")