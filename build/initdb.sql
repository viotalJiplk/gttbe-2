-- Adminer 4.8.1 MySQL 10.11.4-MariaDB-1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;

SET NAMES utf8mb4;

CREATE DATABASE `gtt` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `gtt`;

DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `userId` bigint(20) unsigned NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `adminType` enum('admin','gameOrganizer') NOT NULL,
  KEY `userId` (`userId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `admins_ibfk_2` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `gameId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `maxCaptains` int(10) unsigned NOT NULL,
  `maxMembers` int(11) unsigned NOT NULL,
  `maxReservists` int(11) unsigned NOT NULL,
  PRIMARY KEY (`gameId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `registrations`;
CREATE TABLE `registrations` (
  `userId` bigint(20) unsigned NOT NULL,
  `teamId` int(10) unsigned NOT NULL,
  `nick` varchar(100) NOT NULL,
  `role` enum('Captain','Member','Reservist') NOT NULL,
  `rank` int(11) NOT NULL,
  `maxRank` int(11) NOT NULL,
  KEY `teamId` (`teamId`),
  KEY `userId` (`userId`),
  CONSTRAINT `registrations_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `registrations_ibfk_2` FOREIGN KEY (`teamId`) REFERENCES `teams` (`teamId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DELIMITER ;;

CREATE TRIGGER `registrations_bi` BEFORE INSERT ON `registrations` FOR EACH ROW
IF ((SELECT COUNT(*) FROM registrations LEFT JOIN teams ON registrations.teamId=teams.teamId WHERE registrations.userId=NEW.userId AND teams.gameId=(SELECT gameId FROM teams WHERE teamId=NEW.teamId)) <> 0) THEN
  SET NEW.userId = NULL;
END IF;;

DELIMITER ;

DROP TABLE IF EXISTS `schools`;
CREATE TABLE `schools` (
  `schoolId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`schoolId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;


DROP TABLE IF EXISTS `states`;
CREATE TABLE `states` (
  `state` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `teams`;
CREATE TABLE `teams` (
  `teamId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `gameId` int(10) unsigned NOT NULL,
  `joinString` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`teamId`),
  UNIQUE KEY `joinLink` (`joinString`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `teams_ibfk_3` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userId` bigint(20) unsigned NOT NULL,
  `surname` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `adult` bit(1) NOT NULL,
  `schoolId` int(10) unsigned NOT NULL,
  `access_token` varchar(100) NOT NULL,
  `refresh_token` varchar(100) NOT NULL,
  `expires_in` datetime NOT NULL,
  PRIMARY KEY (`userId`),
  KEY `schoolId` (`schoolId`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`schoolId`) REFERENCES `schools` (`schoolId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- 2023-08-06 14:22:56