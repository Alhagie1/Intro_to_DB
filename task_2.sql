

CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;
-- The Authors table
CREATE TABLE authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255)
);


-- The Books table
CREATE TABLE Books(
    book_id INT PRIMARY KEY, -- This is the primary key
    title VARCHAR(130),
    author_id INT, -- This is the foreign key
    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE
);
--  The customers table
CREATE TABLE Customers(
    customer_id  INT PRIMARY KEY, -- This is the primary key
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);
-- The Orders table
CREATE TABLE Orders(
    order_id INT PRIMARY KEY, -- This is the primary key
    customer_id INT, -- This is the foreign key
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);
 
--  The Order Details table
CREATE TABLE Order_Details(
    orderdetailid INT PRIMARY KEY, -- This is the primary key
    order_id INT, -- This the foreign key
    book_id INT , -- This is a foreign key
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    quantity DOUBLE
);