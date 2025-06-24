import requests

BASE_URL = "http://localhost:8000"

def get_customers():
    r = requests.get(f"{BASE_URL}/customers/")
    print(r.json())

if __name__ == "__main__":
    get_customers()