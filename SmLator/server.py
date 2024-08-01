#!/usr/bin/env python3

import urllib.request
import time
import sys

# Color definitions
R = '\033[1;31m'
G = '\033[1;32m'
W = '\033[1;37m'

def check_server_status(url):
    try:
        print(f"{G}[{W}-{G}] Connecting to Smlator Servers...")
        time.sleep(3)
        
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            response_text = response.read().decode('utf-8')

            if status_code == 200:
                if "Opened" in response_text:
                    return True
                else:
                    print(f"{R}[{W}-{R}] Failed to connect to Smlator servers ..")
                    return False
            else:
                print(f"{R}[{W}-{R}] Failed to fetch server status ..")
                return False
    except urllib.error.HTTPError as e:
        print(f"{R}[{W}-{R}] HTTP Error: {e.code} - {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"{R}[{W}-{R}] URL Error: {e.reason}")
        print(f"{R}[{W}-{R}] No internet connection ")
        return False
    except Exception as e:
        print(f"{R}[{W}-{R}] Error: {e}")
        print(f"{R}[{W}-{R}] No internet connection ")
        return False

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/wa-inc/Sm_Lator/main/SmLator/status"
    if check_server_status(url):
        sys.exit(0)
    else:
        sys.exit(1)
