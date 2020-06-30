#Lab1.2 Создание графика из таблици XL

from matplotlib import pyplot
from openpyxl import load_workbook as load

#Загружаем XL файл
XL = load('data_analysis_lab.xlsx')

#Открываем нужную унигу по названию Data
List = XL['Data']

#Создаем фунецию извлечения значения из ячейки
def val(x): return x.value

#Создаем строку из значений в столбцах A,C,D
Year = list(map(val, List['A'][1:]))
Temp = list(map(val, List['C'][1:]))
Active = list(map(val, List['D'][1:]))

#Создаем 2 графика соотнашения столбцов А-С и А-D
pyplot.plot(Year, Temp, label="Метка")
pyplot.plot(Year, Active, label="Метка")

#Вывод графика
pyplot.show()