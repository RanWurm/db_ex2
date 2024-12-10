import mysql.connector


q = """
CREATE TABLE country (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(63) NOT NULL
   )
"""


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host=" localhost ",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307",
    )
    cursor = mydb.cursor()
    cursor.execute(q)
    print(','.join(str(row) for row in cursor.fetchall()))

