import requests
def fetch(url):
    try:
        r = requests.get(url,timeout=8)
        if r.status_code != 200:
            return None
        return r.json()
    except requests.exceptions.RequestException:
        return None
for url in ["https://httpbin.org/get",
            "https://httpbin.org/status/404",
            "https://no-such-domain-12345.com"]:
    data = fetch(url)
    if not data:
        print(f"跳过:{url} 拿不到数据")
    else:
        print(f"{url} →origin={data['origin']}，顶层键={list(data.keys())}")
