CREATE DATABASE paper_trading;

USE paper_trading;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    balance FLOAT(10, 2)
);

INSERT INTO users (id, name, email, balance) VALUES (1, 'John jose', 'john@example.com', 10000.00);


CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    symbol VARCHAR(10),
    action VARCHAR(4),
    quantity INT,
    price FLOAT(10, 2),
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
