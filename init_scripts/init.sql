
CREATE USER 'tbjuechen'@'%' IDENTIFIED BY 'a20030613';
GRANT ALL PRIVILEGES ON *.* TO 'tbjuechen'@'%';

SELECT USER();

SELECT User, Host FROM mysql.user;

SHOW GRANTS FOR CURRENT_USER();


CREATE DATABASE graduation_project;