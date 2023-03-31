import openpyxl as xl
from openpyxl.chart import (ScatterChart,Reference,Series)
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
rows=[["Experience","Salary"],
      [1,4.5],
      [2,6.0],
      [3,7.6],
      [4,9.2],
      [6,10.5],
      [8,15.0],
      [10,20.5]
      ]
for row in rows:
    sheet.append(row)
chart=ScatterChart()
xdata=Reference(worksheet=sheet,
               min_row=1,
               max_row=8,
               min_col=1)
ydata=Reference(worksheet=sheet,
                min_row=1,
                max_row=8,
                min_col=1)
chart.add_data(xdata,ydata,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("C://exceldata//scatterchartexample.xlsx")