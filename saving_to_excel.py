import xlsxwriter

arrayncar=[9,2,4,4,5,6,7,56,5,4]# sample data array
workbook=xlsxwriter.Workbook('ncarfile.xlsx')#creates excel file name
worksheet=workbook.add_worksheet()#allows user to input info to excel page

for value in range(1,len(arrayncar)): # appends every value vertically to the sheet
    worksheet.write(value,0,arrayncar[value])
workbook.close() 
