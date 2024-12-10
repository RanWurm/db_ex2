import mysql.connector


q = """
CREATE TABLE order_customer (
    order_id INT,
    customer_id VARCHAR(15),
    PRIMARY KEY (order_id, customer_id),
    FOREIGN KEY (order_id) REFERENCES company_order(order_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
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

