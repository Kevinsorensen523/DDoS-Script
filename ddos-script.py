import requests
from concurrent.futures import ThreadPoolExecutor

def send_post_request(url):
    """Function to send a POST request."""
    try:
        data = {'data': 'test'}  # Data to be sent
        response = requests.post(url, data=data)
        print(f"Status Code: {response.status_code}, URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    url = 'http://localhost:3000/submit'
    with ThreadPoolExecutor(max_workers=50) as executor:
        for _ in range(1000):  # Number of requests to send
            executor.submit(send_post_request, url)

if __name__ == "__main__":
    main()
