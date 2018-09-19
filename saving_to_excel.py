import xlsxwriter

arrayncar=[]
workbook=xlsxwriter.Workbook('ncarfile.xlsx')
worksheet=workbook.add_worksheet()

for h in g_hps: #Uses the relationship above to estimate the number of cars in the frame.
    ncar = (h - b)/m;
    ncar = math.ceil(ncar);
    arrayncar.append(ncar);
worksheet.write(0,0,'the values')
for value in range(1,len(arrayncar)):
    worksheet.write_column(arrayncar[value])
workbook.close()