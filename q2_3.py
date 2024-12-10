import mysql.connector


q = """
CREATE TABLE shoe_size (
    shoe_id INT,
    size_id INT,
    PRIMARY KEY (shoe_id, size_id),
    FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
    FOREIGN KEY (size_id) REFERENCES Sizes(size_id)
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

