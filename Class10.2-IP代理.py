import requests
proxy = 'IP代理地址'
proxies = {"http":"http://" + proxy, "https":"https://" + proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, proxies = proxies).text
