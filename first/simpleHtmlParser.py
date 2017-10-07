from bs4 import BeautifulSoup
import urllib.request
import dryscrape
import ssl


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
context = ssl._create_unverified_context()
f = urllib.request.urlopen("https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok?s=101", context=context)
doc = f.read()

soup = BeautifulSoup(doc, 'html.parser')

# print(soup.prettify())
# print(soup.findAll("a", class_='title item-description-title'))
links = soup.find_all("div", class_="item")
for link in links:
    print(link.contents[5].h3.a.string.strip(), link.contents[5].div.contents[3].contents[0].strip())
    # print(link)

# print(links)