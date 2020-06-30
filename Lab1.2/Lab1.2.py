
from matplotlib import pyplot
from openpyxl import load_workbook as load

XL = load('C:\\test\data_analysis_lab.xlsx')

List = XL['Data']


def val(x): return x.value

Year = list(map(val, List['A'][1:]))
Temp = list(map(val, List['C'][1:]))
Active = list(map(val, List['D'][1:]))

pyplot.plot(Year, Temp, label="Метка")
pyplot.plot(Year, Active, label="Метка")
pyplot.show() #