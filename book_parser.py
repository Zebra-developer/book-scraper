import requests
from bs4 import BeautifulSoup


# скрапинг страницы с нужными данными для дальнейшей работы
url = 'https://quotes.toscrape.com'

sessia = requests.Session()

response = sessia.get(url)

html_content = response.content


soup = BeautifulSoup(html_content, 'html.parser')

data = soup.findAll('div', class_='quote')

with open('results.txt', 'w', encoding='utf-8') as f:
    for texts in data:
        text = texts.find('span', class_='text')
        author = texts.find('small', class_='author')
        tags = texts.find('div', class_='tags')
        print(text.text, author.text, sep='\n')
        print(tags.text)

        f.write(f'{text.text}\n{author.text}\n{tags.text}\n')
        f.write(f'{"-"*100}\n')
