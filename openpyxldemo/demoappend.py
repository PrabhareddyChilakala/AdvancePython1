import openpyxl as xl
from openpyxl import Workbook
rows=[["product","online","store"],
      [1,2,3],
      [43,4,6],
      [65,76,6],
      [3,4,5],
      [3,4,5],
      ]
wb=Workbook()
sh=wb.active
for row in rows:
    sh.append(row)
wb.save("C://exceldata//mysheet.xlsx")