from mysqladvance.mysqlconnection import Connection
class Crudoperations(Connection):
    def __init__(self):
        super().__init__('localhost','root','Prabha@23','myhcl',3306)
        self.cur=self.connection.cursor()
    def creating(self):
        sql='create table prabha_table(emp_id int,Name varchar(20),Place varchar(20));'
        self.cur.execute(sql)
    def insert(self,data):
        self.data=data
        sql="insert into prabha_table values(%s,%s,%s);"
        self.cur.execute(sql,(self.data))
        self.connection.commit()
    def read(self):
        sql='select * from prabha_table;'
        self.cur.execute(sql)
        print(self.cur.fetchall())
    def deleting(self,data):
        self.data = data
        sql='delete from prabha_table where emp_id = %s;'
        self.cur.execute(sql,(self.data))
        self.connection.commit()
    def updating(self,data):
        self.data = data
        sql='update prabha_table set name=%s where emp_id=%s;'
        self.cur.execute(sql,(self.data))
        self.connection.commit()
# try:
#     objcrud=Crudoperations()
#     print(objcrud.connection.is_connected())
# except Exception as e:
#     print(e)
# objcrud.creating()
# objcrud.insert()
# objcrud.read()
# objcrud.deleting()
# objcrud.updating()


