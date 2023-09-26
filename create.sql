-- Adminer 4.8.1 MySQL 10.11.4-MariaDB-1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `gtt` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `gtt`;

DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `gameId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `registrationStart` date NOT NULL,
  `registrationEnd` date NOT NULL,
  `maxCaptains` int(10) unsigned NOT NULL,
  `maxMembers` int(11) unsigned NOT NULL,
  `maxReservists` int(11) unsigned NOT NULL,
  PRIMARY KEY (`gameId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `games` (`gameId`, `name`, `registrationStart`, `registrationEnd`, `maxCaptains`, `maxMembers`, `maxReservists`) VALUES
(1,	'CS:GO',	'2023-09-26',	'2023-10-26',	1,	1,	1),
(2,	'LOL',	'2023-08-26',	'2023-10-26',	1,	1,	1),
(3,	'MC',	'2023-07-26',	'2023-11-17',	1,	1,	1);

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

DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `userId` bigint(20) unsigned NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `role` enum('admin','gameOrganizer','gameStreamer') NOT NULL,
  KEY `userId` (`userId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `roles_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `roles_ibfk_2` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `schools`;
CREATE TABLE `schools` (
  `schoolId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`schoolId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_czech_ci;


DROP TABLE IF EXISTS `states`;
CREATE TABLE `states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
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
  `surname` varchar(200) NOT NULL DEFAULT '""',
  `name` varchar(200) NOT NULL DEFAULT '""',
  `adult` bit(1) NOT NULL DEFAULT b'0',
  `schoolId` int(10) unsigned DEFAULT NULL,
  `access_token` varchar(100) NOT NULL,
  `refresh_token` varchar(100) NOT NULL,
  `expires_in` datetime NOT NULL,
  PRIMARY KEY (`userId`),
  KEY `schoolId` (`schoolId`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`schoolId`) REFERENCES `schools` (`schoolId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `users` (`userId`, `surname`, `name`, `adult`, `schoolId`, `access_token`, `refresh_token`, `expires_in`) VALUES
(264449522329976832,	'Surname',	'Name12',	CONV('1', 2, 10) + 0,	1,	'ZqgOnszCA6xIx9rakTkVLX4bh8n4yT',	'dnb4HhHr62MkPKu6zZE4yDs9Z2ULS5',	'2023-10-02 11:03:43'),
(810820857290948619,	'surName1',	'Name123',	CONV('1', 2, 10) + 0,	1,	'peef29AsDDHSr2LepBB763wNxu6nVY',	't1UXqMqgbF6YGPT65hoDd63mXbm6dy',	'2023-10-02 11:00:35');

-- 2023-09-25 09:17:27
