from matplotlib import pyplot
from openpyxl import load_workbook
XL = load_workbook('data_analysis_lab.xlsx')
TAB = XL['Data']
TAB['A'][1:]