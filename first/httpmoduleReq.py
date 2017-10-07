import http.client

conn = http.client.HTTPConnection("www.ya.ru")
conn.request("GET", "/")
res = conn.getresponse()
print(res.reason)