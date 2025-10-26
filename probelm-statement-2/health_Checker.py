import requests
URL = "https://accuknox.com"
try:
    r = requests.get(URL, timeout=5)
    print(f"Checking URL: {URL}")
    print(f"Status Code: {r.status_code}")
    print("Application is UP" if r.status_code == 200 else "Application is DOWN")
except requests.RequestException as e:
    print(f"Checking URL: {URL}")
    print("Application is DOWN")
    print(f"Error: {e}")
