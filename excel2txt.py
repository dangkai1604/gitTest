import xlrd
fileName = 'f:\\book1.xlsx'
sheetName = 'Sheet1'
rbk = xlrd.open_workbook(fileName)
rsh = rbk.sheet_by_name(sheetName)
data = rsh.col_values(0)
file = open('f:\\data.c','w')
file.write('// write by python\n')
file.write('uchar code dataTab[]={\n')
num = 0
for i in data:
    s = str(int(i))
    if len(s)== 1:
        file.write('   ')
    elif len(s)== 2:
        file.write('  ')
    elif len(s)== 3:
        file.write(' ')   
    file.write(s)
    file.write(', ')
    num = num +1
    if num%10 == 0:
        file.write('\n')
file.write('};\n')    
file.close()
    
