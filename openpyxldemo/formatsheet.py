import openpyxl as xl
from openpyxl.styles import Font,Alignment
wb=xl.load_workbook("C://exceldata//mysheet.xlsx")
sh=wb.active
font=Font(italic=True,size=20)
alignment=Alignment(horizontal='center')
sh['A1'].font=font
sh['A1'].alignment=alignment
wb.save("C://exceldata//mysheet.xlsx")
