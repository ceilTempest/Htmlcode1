import psycopg2 as p
#For connection
connection = p.connect(host="localhost",user="postgres",password="root123",dbname="New1")
#Cursoe declare
cur =connection.cursor() 
#Table create kela DBMS
drop = "drop table stud"
cur.execute(drop)
create = "create table if not exists stud(roll int primary key ,name varchar)"
cur.execute(create) #to execute cursor
#Value insert like DBMS
insert = "insert into stud values(10,'sah')"
cur.execute(insert)
insert = "insert into stud values(12,'SHU')"
cur.execute(insert) #Value exccute

connection.commit() #connection commit 
cur.close() #Cursor close
connection.close()

