mysql -u root -p
SELECT User, Host FROM mysql.user WHERE User = 'hbnb_evo_2';

CREATE USER 'hbnb_evo_2'@'localhost' IDENTIFIED BY 'hbnb_evo_2_pwd';
GRANT ALL PRIVILEGES ON hbnb_evo_2_db.* TO 'hbnb_evo_2'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS hbnb_evo_2_db;
USE hbnb_evo_2_db;
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(120) NOT NULL UNIQUE,
  `password` varchar(128) NOT NULL,
  `is_admin` bool DEFAULT FALSE,
  PRIMARY KEY (`id`)
) 


- hbnb_evo_2_db.users definition

CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;