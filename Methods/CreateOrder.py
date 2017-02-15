import sqlite3

class Order():
    """
    Purpose: Allow a Customer to create an order
    Author: Abby
    Methods: 
        get_customer_full_name,
        get_order_complete, 
        set_order_to_completed
        create_order
    """

    def __init__(self, customer, payment, order_complete):
        self.__customer = customer
        self.__payment = payment
        self.__order_complete = False


    def get_customer_full_name(self):
        return self.__customer.get_full_name()


    def get_order_complete(self):
        return self.__order_complete


    def set_order_to_completed(self):
        self.__order_complete = True
        return self.__order_complete


    def create_order(self, order, customer):

        with sqlite3.connect("bangazon_cli.db") as bang:
            cursor = bang.cursor()

            try: 
                cursor.execute("SELECT * FROM CustomerOrder")
                orders = cursor.fetchall()
            except sqlite3.OperationalError:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS `CustomerOrder`
                    (
                        customer_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER NOT NULL,
                        payment_id INTEGER,
                        order_complete BOOLEAN,
                        FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`),
                        FOREIGN KEY(`payment_id`) REFERENCES `PaymentMethod`(`payment_method_id`)
                    )
                """)

            # There needs to be a getter for payment_id. 
            # While order complete == False, the order is not complete
            # order_id, customer_id, payment_id, order_complete
            cursor.execute("""
                INSERT INTO CustomerOrder VALUES (null, "{}", "{}", "{}")
                """.format(
                        customer.get_customer_id(customer),
                        1,
                        order.get_order_complete()
                    )
                )


    def get_order_id(self, order, customer):
        """Method To return the Order's ID"""

        # connect to the database
        with sqlite3.connect("bangazon_cli.db") as bang:
            cursor = bang.cursor()

            try: 
                # select order_id that matches the customer's id and is false
                cursor.execute("SELECT * FROM CustomerOrder c WHERE c.customer_id = '{}' AND c.order_complete = 'False'".format(customer.get_customer_id(customer)))
                
                # fetch the data [(1, 1, 1, 'False')]
                # order_id, customer_id, payment_id, order_complete
                data = cursor.fetchall()
                return data[0][0]
                

            except sqlite3.OperationalError:
                print("NOPE.")



    def order_is_complete(self, order, customer):
        """Method to return if the order is complete"""

        #connect to the database
        with sqlite3.connect("bangazon_cli.db") as bang:
            cursor = bang.cursor()
        
            # update False to True based on customer id 
            cursor.execute("UPDATE CustomerOrder SET order_complete='True' WHERE customer_id='{}'".format(customer.get_customer_id(customer)))

            # select the new row
            cursor.execute("SELECT * FROM CustomerOrder WHERE customer_id='{}'".format(customer.get_customer_id(customer)))

            # [(1, 1, 1, 'True')]
            # order_id, customer_id, payment_id, T/F 
            data = cursor.fetchall()
            return data[0][3]