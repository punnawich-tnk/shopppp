import database
mycursor = database.mydb.cursor()
#--------------------------------------------------------------------#
def selectdb(table):
    sql = f"SELECT * FROM {table} "
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#print(selectdb('user'))

#--------------------------------------------------------------------#
def insert_product(name,price,stock):
    sql = "INSERT INTO product VALUES (%s, %s ,%s ,%s)"
    val_sql = (1,'name','price','stock')
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_product('test',5000,50))
#--------------------------------------------------------------------#
sql = "DELETE FROM product WHERE id = 12 "
mycursor.execute(sql)
database.mydb.commit()
if mycursor.rowcount > 0:
    print(True)
else:
    print(False)

def deletedb(table,column,id_name,id,val):
    sql = f"UPDATE (table) SET (column) =%s WHERE (id_name) = %s "
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
print(('product',"name_product","id_product",1,"ไอเเพต"))
#--------------------------------------------------------------------#
