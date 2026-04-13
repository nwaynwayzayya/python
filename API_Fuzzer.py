import requests

import sys

def loop():
    # sys.stdin  -- standard input -- receives text from another input like "cat small.txt | python [filename]"
    for word in sys.stdin:
        res = requests.get(url=f"http://10.10.11.161/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)
        # print(res)
        # data = res.json()
        # print(data)


loop()