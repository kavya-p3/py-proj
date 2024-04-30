from utilities.configurations import *

conn=getConnection()
print(conn.is_connected())
cursor = conn.cursor()
#cursor.execute('select * from CustomerInfo')
query = 'update CustomerInfo set Location = %s where CourseName = %s'
data = ('London113', 'Jmeter')
cursor.execute(query, data)
conn.commit()
