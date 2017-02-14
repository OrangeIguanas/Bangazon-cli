import sqlite3

conn = sqlite3.connect('bangazon_cli.db')

c = conn.cursor()

customers = [(1, 'Bob', 'Bobbins', 'd@d.com', '615-999-1111', 'Smyrna', 'Tennessee', 37167, '111 Front Street', 'False'), (2, 'Joe', 'Mammy', 'joe@mammy.com', '625-444-4444', 'Smyrna', 'Tennessee', 38933, '222 Back', 'False'), (3, 'Drew', 'Martin', 'Drew@drew.com', '615-481-0464', 'Nashville', 'Tennessee', 37122, '1111 Back', 'False'), (4, 'Zach', 'Cline', 'Zach@z.com', '615-111-2222', 'Nashville', 'Tennessee', 37167, '2222 Block', 'False'), (5, 'Pete', 'Staggs', 'Pete@pete.pete', '617-222-3332', 'Mt. Juliet', 'Tennessee', 37111, '444 Hole Road', 'False'), (6, 'Ben', 'Marks', 'Ben@ben.ben', '617-432-2344', 'Nashville', 'Tennessee', 37131, '321 countdown road', 'False'), (7, 'Loki', 'Destroyer', 'BringHell@space.com', '123-456-7890', 'Asgard', 'Valhalla', 0, 'Good Luck', 'False')]

categories = [(1, 'Appliances'), (2, 'Video Games'), (3, 'Weapondry'), (4, 'Pool Toys'), (5, 'Memes')]

products = [(1, 'Boomarang', 4.00, 'Throw and It will Return!', 15, 3), (2, 123.99, 'Whippinator', 1), (3, 69.99,  'Madden 09', 2 ), (4, 3.00,  'Pool Noodle', 4), (5, 100.00 , 'Dickbutt', 5)]

# c.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', customers)

# c.execute('SELECT * FROM Customers')
# print(c.fetchall())

# c.executemany('INSERT INTO Categories VALUES (? , ?)', categories )

# c.execute('SELECT * FROM Categories')
# print(c.fetchall())


c.executemany('INSERT INTO Products VALUES (? , ? , ? , ? , ?, ?)', [(1, "Boomarang", 4, "Throw and It will Return!", 15, 3), (2, "Whippinator", 5, "A Whip for Whipped Cream", 12,  1), (3, "Madden 09", 69, "Video Game that is Awesome?", 23, 2 ), (4, "Pool Noodle", 3, "Noodling in the Pool", 100, 4), (5, "Dickbutt", 1000, "Dickbutt needs no description", 1,  5)] )

c.execute('SELECT * FROM Products')
print(c.fetchall)

conn.commit()

conn.close()

