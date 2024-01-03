import sqlite3

class ProductDB:
    def __init__(self, connect: sqlite3.Connection) -> None:
        self.__connect = connect
        self.__cursor = connect.cursor()


    def get_all_products(self):
        sql = "SELECT name, price, description, img, id FROM coffee_products"
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print("ошибка чтения из базы данных")
            return []

    def get_product(self, id):
        sql = "SELECT * FROM coffee_products WHERE id = ?"
        self.__cursor.execute(sql, tuple([id]))
        return self.__cursor.fetchone()
    