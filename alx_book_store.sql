CREATE DATABASE IF NOT EXISTS alx_book_store;




CREATE TABLE IF NOT EXISTS books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        price DOUBLE,
        publication_date DATE);




CREATE TABLE IF NOT EXISTS Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215));



CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(251),
    address TEXT);


CREATE TABLE IF NOT EXISTS Orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    order_date DATE);



CREATE TABLE IF NOT EXISTS Order_Details(
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    quantity DOUBLE
);

