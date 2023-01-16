-- Adminer 4.8.1 MySQL 10.6.11-MariaDB-2 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;

SET NAMES utf8mb4;

CREATE DATABASE `gtt` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `gtt`;

DROP TABLE IF EXISTS `sessions`;
CREATE TABLE `sessions` (
  `session` varchar(50) NOT NULL,
  `userid` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`session`),
  KEY `userid` (`userid`),
  CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `states`;
CREATE TABLE `states` (
  `state` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userid` bigint(20) unsigned NOT NULL,
  `access_token` varchar(100) NOT NULL,
  `refresh_token` varchar(100) NOT NULL,
  `expires_in` datetime NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- 2023-01-16 20:17:04