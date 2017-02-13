import sqlite3

conn = sqlite3.connect('bangazon_cli.db')

c = conn.cursor()




customers = [(1, 'Bob', 'Bobbins', 'd@d.com', '615-999-1111', 'Smyrna', 'Tennessee', 37167, '111 Front Street', 'False'), (2, 'Joe', 'Mammy', 'joe@mammy.com', '625-444-4444', 'Smyrna', 'Tennessee', 38933, '222 Back', 'False'), (3, 'Drew', 'Martin', 'Drew@drew.com', '615-481-0464', 'Nashville', 'Tennessee', 37122, '1111 Back', 'False'), (4, 'Zach', 'Cline', 'Zach@z.com', '615-111-2222', 'Nashville', 'Tennessee', 37167, '2222 Block', 'False'), (5, 'Pete', 'Staggs', 'Pete@pete.pete', '617-222-3332', 'Mt. Juliet', 'Tennessee', 37111, '444 Hole Road', 'False'), (6, 'Ben', 'Marks', 'Ben@ben.ben', '617-432-2344', 'Nashville', 'Tennessee', 37131, '321 countdown road', 'False'), (7, 'Loki', 'Destroyer', 'BringHell@space.com', '123-456-7890', 'Asgard', 'Valhalla', 0, 'Good Luck', 'False')]

c.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', customers)

c.execute('SELECT * FROM Customers')
print(c.fetchall())

conn.commit()

conn.close()

