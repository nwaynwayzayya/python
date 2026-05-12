import sys
import requests

# Adding headers here is necessary because sometimes the requests get blocked if they detect a script without a proper User-Agent.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36'
}

def urls(out_file):
    # --- OPTION 1: READING FROM A FILE DIRECTLY ---
    # with open("url_list.txt", "r") as f:
    #     url2 = f.read().splitlines()

    # --- OPTION 2: UNIVERSAL PIPING (Works on Windows & Linux) ---
    # .read().splitlines() handles the incoming piped data.
    url2 = sys.stdin.read().splitlines()

    good_urls = []

    for url in url2:
        url = url.strip()
        if not url:
            continue
            
        try:
            # timeout=5 prevents the script from hanging on broken links
            response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                print(f"[+] Valid: {url}")
                good_urls.append(url)
            else:
                print(f"[-] Status {response.status_code}: {url}")

        except requests.exceptions.RequestException:
             continue

    with open(out_file, 'w') as file:
         file.write('\n'.join(good_urls))

    print(f"\nDone! Checked URLs saved to {out_file}")

# Set your output file name
out_file = "checked_urls.txt"
urls(out_file)

# Since we are using sys.stdin, you "feed" the file to the script via the command line:
# On Windows (PowerShell): Get-Content url_list.txt | python main.py
# On Linux / Mac / WSL:cat url_list.txt | python3 main.py
