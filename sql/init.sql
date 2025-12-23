CREATE DATABASE database;

CREATE TABLE contacts(
  Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  First_name VARCHAR(50) NOT NULL,
  Last_name VARCHAR(50) NOT NULL,
  Phone_number VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO contacts(First_name, Last_name, Phone_number)
VALUES ("Yoseph", "Rechdiener", "054-2985519")
       ("David", "Rechdiener", "054-2986210")
       ("Talya", "Rechdiener", "054-2980112");
       ("Eli", "Rechdiener", "054-3979494");

