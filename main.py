import xlsxwriter
from func_parser import array # импортируем нашу функцию генератор


# Функция создания файла CSV и строк со столбцами
def writer(args):
	book = xlsxwriter.Workbook(r'укажите свой путь до папки дата') # укажите путь для сохранения CSV файла пример: C:\Users\emely\Рабочий стол\project\book_parser\data + \название_файла.xlsx
	page = book.add_worksheet('Товар')


	row = 0
	column = 0

	# размеры столбцов
	page.set_column('A:A', 100)
	page.set_column('B:B', 50)
	page.set_column('C:C', 20)
	page.set_column('D:D', 50)


	# проходимся по переданным кортежам и расставляем всё на своё место в таблице
	for item in args():
		page.write(row, column, item[0])
		page.write(row, column+1, item[1])
		page.write(row, column+2, item[2])
		page.write(row, column+3, item[3])
		row += 1


	# цикл спрашивающий о перазаписи файла и закрытии программы
	while True:
		try:
			book.close()
		except xlsxwriter.exceptions.FileCreateError as e:
			decision = input("Exception caught in book.close(): %s\n"
					"Please close the file if it is open in Excel.\n"
					"Try to write file again? [Y/n]: " % e)
			if decision != 'n':
				continue

		break

# запуск

writer(array) # запускаем функцию записи в CSV передавая аргументом импортированную функцию генератор
