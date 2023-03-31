import openpyxl as xl
from dataclasses import dataclass
@dataclass
class Person:
    name:str
    contact:int
    email:str
    location:str
wb=xl.Workbook()
ws=wb.active
persons=[
    Person(name="Raju",contact=454545,email='raju@gmail.com',location='bangalore'),
    Person(name='Rahul',contact=565656,email='rahul@gmail.com',location='Chennai'),
    Person(name='Mahek',contact=676767,email='mahek@yahoo.com',location='Mumbai')
]
data=[[p.name,p.contact,p.email,p.location]for p in persons]
mydata=[['Name','Contact','Email','Location']]+data
print(mydata)
for row in mydata:
    ws.append(row)
