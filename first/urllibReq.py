import urllib.request
import ssl

context = ssl._create_unverified_context()
f = urllib.request.urlopen("http://ya.ru", context=context)
print(f.read())