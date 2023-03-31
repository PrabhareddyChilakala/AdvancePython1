import openpyxl as xl
from openpyxl.chart import BarChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
rows=[["product","online","store"],
      [1,2,3],
      [43,4,6],
      [65,76,6],
      [3,4,5],
      [3,4,5],
      ]
for row in rows:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,
               min_row=1,
               max_row=8,
               min_col=2,
               max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("C://exceldata//chart.xlsx")