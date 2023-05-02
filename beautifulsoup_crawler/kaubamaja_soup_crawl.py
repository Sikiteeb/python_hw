import requests
from bs4 import BeautifulSoup
import json


def scrape_page(url):
    items = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.select('.products-grid__link'):
        title = item.get('title')
        price = item.select_one('.price').text.replace('\xa0', ' ')

        img_element = item.select_one('.products-grid__image img:nth-child(2)')
        if img_element:
            picture_href = img_element.get('src')
        else:
            picture_href = None
        # null also if the picture is loaded dynamically with Javascript

        items.append({
            'Title': title,
            'Price': price,
            'Picture href': picture_href,
        })

    next_page = soup.select_one('.pagination__link.pagination__link--next')
    if next_page:
        next_page_url = next_page['href']
        if url != next_page_url:
            items.extend(scrape_page(next_page_url))

    return items


if __name__ == '__main__':
    url = 'https://www.kaubamaja.ee/kodu/lemmikloomade-aksessuaarid'
    scraped_data = scrape_page(url)

    with open('kaubamaja_bs_result.json', 'w') as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)
