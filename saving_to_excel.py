import xlsxwriter

arrayncar=[9,2,4,4,5,6,7,56,5,4]# include the array with the actual data in it
workbook=xlsxwriter.Workbook('ncarfile.xlsx')
worksheet=workbook.add_worksheet()

worksheet.write(0,0,'the values')
for value in range(1,len(arrayncar)):
    worksheet.write(value,0,arrayncar[value])
workbook.close() 
