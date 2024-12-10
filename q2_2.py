import mysql.connector


q = """
CREATE TABLE Sizes (
    size_id INT PRIMARY KEY,
    european_number TINYINT NOT NULL,
    us_number TINYINT NOT NULL
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

