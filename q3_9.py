import mysql.connector


query = """
INSERT INTO order_shoe (order_id, shoe_id) VALUES
(1, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7,
8), (8, 9), (9, 10)
"""



if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute(query)
mydb.commit()
cursor.close()
mydb.close()