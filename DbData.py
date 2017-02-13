import sqlite3

conn = sqlite3.connect('bangazon_cli.db')

c = conn.cursor()




customers = [(3, 'Drew', 'Martin' , 'Drew@drew.com', '615-481-0464' , 'Nashville', 'Tennessee', 37122, '1111 Back' , 'False') , (4, 'Zach' , 'Cline', 'Zach@z.com', '615-111-2222' , 'Nashville', 'Tennessee' , 37167, '2222 Block', 'False'), (5, 'Pete', 'Staggs' , 'Pete@pete.pete' , '617-222-3332' , 'Mt. Juliet' , 'Tennessee' , 37111, '444 Hole Road', 'False')]

c.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', customers)

c.execute('SELECT * FROM Customers')
print(c.fetchall())

# for row in c.execute('SELECT * FROM Customers ORDER BY customer_id'):
# 	print row