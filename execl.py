import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
import time

fileName = 'f:\\write9.xls'
sheetName = 'sheet1'

print ('write excel')

wbk = xlwt.Workbook()
sheet = wbk.add_sheet(sheetName)
for row in range(10):
	for col in range(10):
		sheet.write(row,col,row*col)

    
wbk.save(fileName)
time.sleep(10)

print ('read excel')
rbk = xlrd.open_workbook(fileName)
sh = rbk.sheet_by_name(sheetName)
r = sh.nrows
c = sh.ncols
print (type(sh.cell_value(0,0)))
for row in range(r):
	for col in range(c):
		print(sh.cell_value(row, col))


print ('read write excel')

rbk = xlrd.open_workbook(fileName)
wbk = copy(rbk)
rsh = rbk.sheet_by_name(sheetName)
wsh = wbk.get_sheet(0)
r = rsh.nrows
c = rsh.ncols
for row in range(r):
        for col in range(c):
                data= rsh.cell_value(row, col)
                wsh.write(row,col,data*2)

wbk.save(file)




