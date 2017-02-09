import sqlite3


class PaymentMethod():

    def __init__(self, card_number, card_type, exp_date, cvv, name_on_card, client):
        self.__name_on_card = name_on_card
        self.__card_type = card_type
        self.__card_number = card_number
        self.__exp_date = exp_date
        self.__cvv = cvv
        self.__client= client
        # self.__is_active = True

    def get_name_on_card(self):
        return self.__name_on_card

    def get_card_type(self):
    	return self.__card_type

    def get_card_number(self):
        return self.__card_number

    def get_exp_date(self):
        return self.__exp_date

    def get_cvv(self):
        return self.__cvv

    def get_client(self):
        return self.__client

        

    # def get_active_status(self):
    # 	return self.__is_active
