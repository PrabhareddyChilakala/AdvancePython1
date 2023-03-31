from mysqladvance.CRUDoperations import Crudoperations
obj=Crudoperations()
while(True):
    print("1. Insert a record")
    print("2. Delete a record")
    print("3. Display")
    print("4. Update a record")
    print("5. Creating table")
    print("6. Exit")
    data=int(input("Enter your choice:"))
    if(data==6):
        break
    if data==1:
        empid = int(input("Enter the emp_id"))
        name=input("Enter the name")
        place=input("Enter the place")
        data=(empid,name,place)
        obj.insert(data)
    elif data==2:
        Name=input("Enter the row to delete")
        data=(Name)
        obj.deleting(data)
    elif data==3:
        print("The table is consists..")
        obj.read()
    elif data==4:
        Name=input("Enter the name to update..")
        em=int(input("Enter the empid.."))
        data=(Name,em)
        obj.updating(data)
    elif data==5:
        obj.creating()
    else:
        print("Exiting...")
    break
