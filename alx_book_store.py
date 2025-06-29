import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="alx_book_store"
)

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        price DOUBLE,
        publication_date DATE
    )
""")

mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS authors(
                     author_id INT PRIMARY KEY,
                     author_name VARCHAR(215)
                 )
                 """)


mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS customers(
                     customer_id INT PRIMARY KEY,
                     customer_name VARCHAR(215),
                     email VARCHAR(251),
                     address TEXT
                 )
                 """)


mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS orders(
                     order_id INT PRIMARY KEY,
                     customer_id INT,
                     FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                     order_date DATE
                 )
                 """)

mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS order_details(
                     order_detail_id INT PRIMARY KEY,
                     order_id INT,
                     FOREIGN KEY (order_id) REFERENCES orders(order_id),
                     book_id INT,
                     FOREIGN KEY (book_id) REFERENCES books(book_id),
                     quantity DOUBLE
                 )
                 """)


print("table created")
# Close connection to the databasse  
mycursor.close()
mydb.close()

