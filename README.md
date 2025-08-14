# BookScraper - это Python-скрипт для автоматического сбора информации о книгах с учебного сайта Book to Scrape.

Скрипт получает данные о каждой книге и сохраняет их в CSV-файл для дальнейшего анализа

## Функционал
- Сбор данных с карточек книг:
	- Название
	- Цена
	- Описание книги
	- Ссылка на книгу  
- Запись результатов в CSV-файл через отдельную функцию
- Обход всех страниц каталога

## Используемые технологии:
- Python 3
- requests - для HTTP-запросов
- BeautifulSoup - для парсинга HTML
- csv - для записи данных в файл

## Автор:

Zebra_Developer

Моя визитка - https://my-business-card-4qs2.onrender.com 

## Установка и запуск:

```bash
git clone https://github.com/Zebra-developer/book-scraper.git
pip install -r requirements.txt

python main.py
