import mysql.connector


quary = """
CREATE DATABASE biu_shoes;
"""



if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute(quary)
mydb.commit()
cursor.close()
mydb.close()
