import xlrd

fname = './validation_sheet.xlsx'

xlsFile = xlrd.open_workbook(fname)

sheet_names = xlsFile.sheet_names

print("Sheet Names",sheet_names())
