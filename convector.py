""" Імпортую високорівневу бібліотеку для роботи з даними - Pandas """
import pandas as pd


""" Зчитую CSV файл та змінюю дату на вірний формат для коректного сортування """
df = pd.read_csv('acme_worksheet.csv', index_col='Date', parse_dates=True)


""" Створюю зведену таблицю по заданих параметрах """
pvt = df.pivot_table(index=['Employee Name'], columns=['Date'], values='Work Hours', fill_value=int(0))


""" Записую створену таблицю в новий CSV файл """
pvt.to_csv('out1.csv')
