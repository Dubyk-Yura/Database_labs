CREATE SCHEMA iot_db ;
CREATE TABLE iot_db.client_type
(
    id INT NOT NULL AUTO_INCREMENT,
    type VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE iot_db.client
(
 name VARCHAR(45) NOT NULL,
    number INT NOT NULL AUTO_INCREMENT,
 client_type_id INT NOT NULL,
    PRIMARY KEY (number),
 FOREIGN KEY (client_type_id)
    REFERENCES iot_db.client_type (id)
);

INSERT INTO iot_db.client_type(id, type)
VALUES
(1, 'customer'), (2, 'staff'), (3, 'manager'), (4, 'friend');

INSERT INTO iot_db.client (name, number, client_type_id)
VALUES
('Pavelchak Andrii', 10023,  4),
('Veres Zenovii', 10026, 1),
('Yatsuk Yurii', 10030, 1),
('Samotyi Volodymyr', 20011, 2),
('Shevchenko Petro', 30028, 3);