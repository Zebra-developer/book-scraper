import requests
from bs4 import BeautifulSoup
from time import sleep


# заголовки для парсинга
headers = {
	'User-Agent': 'Mozilla/5.0'
	}


# функция генератор - парсит данные со страницы переходя с одной страницы на другую
def get_url():
	for count in range(1, 8):

		url = f'https://books.toscrape.com/catalogue/page-{count}.html'

		response = requests.get(url, headers=headers)

		soup = BeautifulSoup(response.text, 'lxml') # html.parser

		books = soup.findAll('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

		for book in books:
			card_url = 'https://books.toscrape.com/catalogue/' + book.find('a').get('href')
			yield card_url # возвращаем каждый раз url карту товара


# функция генератор - достаем данные из функции генератора и распределяем их в конкеретные переменные
def array():
	for card_url in get_url(): # берем по одной url карточке товара

		response = requests.get(card_url, headers=headers) # запрашиваем даные

		sleep(3)

		soup = BeautifulSoup(response.text, 'lxml') # html.parser/ парсим страницу с карточкой товара

		book_info = soup.find('div', class_='content')

		name_book = book_info.find('h1').text
		info_book = book_info.findAll('p', limit=4)[-1].text
		price_book = book_info.find('p', class_='price_color').text
		img_book = 'https://books.toscrape.com/' + book_info.find('img').get('src')


		yield (name_book, info_book, price_book, img_book) # возвращаем кортежи с данными по товару
