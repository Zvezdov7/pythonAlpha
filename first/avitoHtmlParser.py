import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''

        try:
            metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
        except:
            metro = ''
        data = {
            'title': title,
            'price': price,
            'metro': metro,
            'url': url
        }
        print(data)


def main():
    url = 'https://www.avito.ru/moskva/kvartiry/sdam?p=1'
    base_url = 'https://www.avito.ru/moskva/kvartiry/sdam'
    page_part = '?p='

    total_pages = get_total_pages(get_html(url))
    for i in range(1, 3):
        url_gen = base_url + page_part + str(i)
        get_page_data(get_html(url_gen))


if __name__ == '__main__':
    main()
