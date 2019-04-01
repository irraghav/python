import xlrd

def getList(fname):
    xlsFile = xlrd.open_workbook(fname)
    firstSheet = xlsFile.sheet_by_index(0)

    retVal = []
    for cell in firstSheet.col_values(0):
        if isinstance(cell,str) and cell:
            retVal.append(cell)

    return retVal           
