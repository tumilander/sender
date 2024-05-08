import requests
import argparse
import threading
import signal
import sys
import random
import time

requests.packages.urllib3.disable_warnings()

## add agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
   
]

# add random headers
random_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Cache-Control": "max-age=0",
}

def load_proxies(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

def send_requests(url, num_requests, use_proxies=False, proxies=None):
    for _ in range(num_requests):
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            headers.update(random_headers)
            if use_proxies:
                proxy = random.choice(proxies)
                response = requests.get(url, headers=headers, proxies={"http": proxy}, verify=False)
            else:
                response = requests.get(url, headers=headers, verify=False)
            print(response.status_code)
            time.sleep(random.uniform(0.1, 0.5))  # waiting requests(random)
        except Exception as e:
            print(f"An error occurred: {e}")

def handler(signum, frame):
    print("\nCtrl+C pressed. Exiting...")##testing
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Send multiple requests to a target URL")
    parser.add_argument("-u", "--url", help="Target URL", required=True)
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=10)
    parser.add_argument("-n", "--requests", help="Number of requests per thread", type=int, default=10)
    parser.add_argument("--use-proxy", help="Use proxy for requests (optional)", action="store_true")
    parser.add_argument("--proxy-file", help="File containing list of proxies")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, handler)

    num_threads = args.threads
    num_requests_per_thread = args.requests
    target_url = args.url
    use_proxies = args.use_proxies

    proxies = None
    if use_proxies:
        if args.proxy_file:
            proxies = load_proxies(args.proxy_file)
        else:
            print("Error: --use-proxy specified but no --proxy-file provided.")
            sys.exit(1)

    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(target_url, num_requests_per_thread, use_proxies, proxies))
        thread.start()

if __name__ == "__main__":
    main()
