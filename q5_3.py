import mysql.connector


query = """
UPDATE Sizes
SET uk_number = 7
WHERE us_number = 9;
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
