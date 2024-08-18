SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';
SET NAMES utf8mb4;

DELIMITER ;;

DROP PROCEDURE IF EXISTS `UpdateTeamPlayStatus`;;
CREATE PROCEDURE `UpdateTeamPlayStatus`(updateTeamId INT)
BEGIN
    DECLARE Captains INT;
    DECLARE Members INT;
    DECLARE Reservists INT;
    DECLARE expCaptains INT;
    DECLARE expMembers INT;
    DECLARE expReservists INT;

    SELECT COUNT(teamId) INTO Captains FROM registrations WHERE teamId = updateTeamId AND role = 'Captain';
    SELECT COUNT(teamId) INTO Members FROM registrations WHERE teamId = updateTeamId AND role = 'Member';
    SELECT COUNT(teamId) INTO Reservists FROM registrations WHERE teamId = updateTeamId AND role = 'Reservist';
    SELECT minCaptains INTO expCaptains FROM games WHERE gameId = (SELECT gameId FROM teams WHERE teamId = updateTeamId);
    SELECT minMembers INTO expMembers FROM games WHERE gameId = (SELECT gameId FROM teams WHERE teamId = updateTeamId);
    SELECT minReservists INTO expReservists FROM games WHERE gameId = (SELECT gameId FROM teams WHERE teamId = updateTeamId);

    IF ((Captains >= expCaptains) AND (Members >= expMembers) AND (Reservists >= expReservists)) THEN
        IF (SELECT canPlaySince FROM teams WHERE teamId = updateTeamId) IS NULL THEN
            UPDATE teams SET canPlaySince = NOW() WHERE teamId = updateTeamId;
        END IF;
    ELSE
        IF (SELECT canPlaySince FROM teams WHERE teamId = updateTeamId) IS NOT NULL THEN
            UPDATE teams SET canPlaySince = NULL WHERE teamId = updateTeamId;
        END IF;
    END IF;
END;;

DELIMITER ;

DROP TABLE IF EXISTS `assignedRolePermissions`;
CREATE TABLE `assignedRolePermissions` (
  `rolePermissionId` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(20) NOT NULL,
  `assignedRoleId` int(11) NOT NULL,
  PRIMARY KEY (`rolePermissionId`),
  UNIQUE KEY `unique_combination` (`permission`,`assignedRoleId`),
  KEY `assignedRoleId` (`assignedRoleId`),
  CONSTRAINT `assignedRolePermissions_ibfk_1` FOREIGN KEY (`permission`) REFERENCES `permissions` (`permission`),
  CONSTRAINT `assignedRolePermissions_ibfk_2` FOREIGN KEY (`assignedRoleId`) REFERENCES `assignedRoles` (`assignedRoleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `assignedRolePermissions` (`rolePermissionId`, `permission`, `assignedRoleId`) VALUES
(10,	'event.create',	1),
(12,	'event.delete',	1),
(13,	'event.listAll',	3),
(3,	    'event.read',	5),
(11,	'event.update',	1),
(14,	'game.listAll',	5),
(18,	'game.update',	1),
(16,	'gamePage.read',	5),
(17,	'gamePage.update',	1),
(23,	'match.create',	1),
(26,	'match.delete',	1),
(24,	'match.read',	5),
(25,	'match.update',	1),
(27,	'page.read',	5),
(28,	'school.listAll',	5),
(20,	'stage.create',	1),
(22,	'stage.delete',	1),
(19,	'stage.read',	5),
(21,	'stage.update',	1),
(44,	'team.create',	4),
(48,	'team.genJoinStr',	1),
(47,	'team.genJoinStrMy',	4),
(46,	'team.join',	4),
(51,	'team.kick',	1),
(50,	'team.kickTeam',	4),
(49,	'team.leave',	4),
(42,	'team.listPartic',	5),
(43,	'team.listParticDisc',	1),
(45,	'team.read',	5),
(36,	'user.delete',	1),
(35,	'user.deleteMe',	4),
(37,	'user.exists',	4),
(41,	'user.listTeams',	1),
(40,	'user.listTeamsMe',	4),
(39,	'user.permissionList',	1),
(38,	'user.permsListMe',	4),
(30,	'user.read',	1),
(29,	'user.readMe',	4),
(33,	'user.update',	1),
(32,	'user.updateMe',	4);

DROP TABLE IF EXISTS `assignedRoles`;
CREATE TABLE `assignedRoles` (
  `assignedRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `gameId` int(10) unsigned DEFAULT NULL,
  `roleName` varchar(20) NOT NULL,
  `discordRoleId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`assignedRoleId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `assignedRoles_ibfk_1` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `assignedRoles` (`assignedRoleId`, `gameId`, `roleName`, `discordRoleId`) VALUES
(1,	NULL,	'admin',	NULL),
(2,	NULL,	'gameOrganizer',	NULL),
(3,	NULL,	'public',	NULL),
(4,	NULL,	'user',	NULL),
(5,	NULL,	'public',	NULL),
(6,	2,	'admin1',	NULL);

DROP VIEW IF EXISTS `eligibleTeams`;
CREATE TABLE `eligibleTeams` (`teamId` int(10) unsigned, `name` varchar(200), `gameId` int(10) unsigned, `canPlaySince` timestamp, `joinString` varchar(200), `userId` bigint(20) unsigned, `nick` varchar(100), `role` enum('Captain','Member','Reservist'), `rank` int(11), `maxRank` int(11));


DROP TABLE IF EXISTS `events`;
CREATE TABLE `events` (
  `eventId` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `beginTime` time NOT NULL,
  `endTime` time NOT NULL,
  `gameId` int(10) unsigned NOT NULL,
  `description` tinytext NOT NULL,
  `eventType` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`eventId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `events_ibfk_1` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `gameId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `registrationStart` date NOT NULL,
  `registrationEnd` date NOT NULL,
  `maxCaptains` int(10) unsigned NOT NULL,
  `maxMembers` int(11) unsigned NOT NULL,
  `maxReservists` int(11) unsigned NOT NULL,
  `minCaptains` int(11) unsigned NOT NULL,
  `minMembers` int(11) unsigned NOT NULL,
  `minReservists` int(11) unsigned NOT NULL,
  `gamePage` mediumtext NOT NULL,
  `maxTeams` int(10) unsigned NOT NULL,
  PRIMARY KEY (`gameId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `matches`;
CREATE TABLE `matches` (
  `matchId` int(11) NOT NULL AUTO_INCREMENT,
  `stageId` int(11) NOT NULL,
  `firstTeamId` int(10) unsigned NOT NULL,
  `secondTeamId` int(10) unsigned NOT NULL,
  `firstTeamResult` int(11) NOT NULL,
  `secondTeamResult` int(11) NOT NULL,
  PRIMARY KEY (`matchId`),
  KEY `firstTeamId` (`firstTeamId`),
  KEY `secondTeamId` (`secondTeamId`),
  KEY `stageId` (`stageId`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`firstTeamId`) REFERENCES `teams` (`teamId`),
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`secondTeamId`) REFERENCES `teams` (`teamId`),
  CONSTRAINT `matches_ibfk_4` FOREIGN KEY (`stageId`) REFERENCES `stages` (`stageId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `page`;
CREATE TABLE `page` (
  `name` varchar(10) NOT NULL,
  `value` mediumtext NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `permissions`;
CREATE TABLE `permissions` (
  `permission` varchar(20) NOT NULL,
  PRIMARY KEY (`permission`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `permissions` (`permission`) VALUES
('event.create'),
('event.delete'),
('event.listAll'),
('event.listMatches'),
('event.read'),
('event.update'),
('game.listAll'),
('game.read'),
('game.update'),
('gamePage.read'),
('gamePage.update'),
('match.create'),
('match.delete'),
('match.read'),
('match.update'),
('page.read'),
('perms.team.leave'),
('school.listAll'),
('stage.create'),
('stage.delete'),
('stage.read'),
('stage.update'),
('team.create'),
('team.genJoinStr'),
('team.genJoinStrAny'),
('team.genJoinStrMy'),
('team.join'),
('team.kick'),
('team.kickTeam'),
('team.leave'),
('team.listPartic'),
('team.listParticDisc'),
('team.read'),
('user.delete'),
('user.deleteMe'),
('user.exists'),
('user.listTeams'),
('user.listTeamsMe'),
('user.permissionList'),
('user.permsListMe'),
('user.read'),
('user.readMe'),
('user.update'),
('user.updateMe');

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

CREATE TRIGGER `UPDATE_REGISTERED` AFTER UPDATE ON `registrations` FOR EACH ROW
BEGIN
    CALL UpdateTeamPlayStatus(NEW.teamId);
END;;

CREATE TRIGGER `INSERT_REGISTERED` AFTER INSERT ON `registrations` FOR EACH ROW
BEGIN
    CALL UpdateTeamPlayStatus(NEW.teamId);
END;;

CREATE TRIGGER `DELETE_REGISTERED` AFTER DELETE ON `registrations` FOR EACH ROW
BEGIN
    CALL UpdateTeamPlayStatus(OLD.teamId);
END;;

DELIMITER ;

DROP TABLE IF EXISTS `roleTypes`;
CREATE TABLE `roleTypes` (
  `role` varchar(20) NOT NULL,
  `discordRoleId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles`(
  `roleId` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `userId` bigint(20) unsigned NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `role` enum('admin','gameOrganizer','gameStreamer') NOT NULL,
  UNIQUE KEY `unique_role` (`userId`,`role`,`gameId`),
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


DROP TABLE IF EXISTS `stages`;
CREATE TABLE `stages` (
  `stageId` int(11) NOT NULL AUTO_INCREMENT,
  `eventId` int(11) NOT NULL,
  `stageName` text NOT NULL,
  `stageIndex` int(11) NOT NULL,
  PRIMARY KEY (`stageId`),
  KEY `eventId` (`eventId`),
  CONSTRAINT `stages_ibfk_1` FOREIGN KEY (`eventId`) REFERENCES `events` (`eventId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `states`;
CREATE TABLE `states` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(200) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP VIEW IF EXISTS `teamInfo`;
CREATE TABLE `teamInfo` (`teamId` int(10) unsigned, `name` varchar(200), `gameId` int(10) unsigned, `canPlaySince` timestamp, `joinString` varchar(200), `userId` bigint(20) unsigned, `nick` varchar(100), `role` enum('Captain','Member','Reservist'), `rank` int(11), `maxRank` int(11));


DROP TABLE IF EXISTS `teams`;
CREATE TABLE `teams` (
  `teamId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `gameId` int(10) unsigned NOT NULL,
  `canPlaySince` timestamp NULL DEFAULT NULL,
  `joinString` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`teamId`),
  UNIQUE KEY `joinLink` (`joinString`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `teams_ibfk_3` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `userRoles`;
CREATE TABLE `userRoles` (
  `userRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `assignedRoleId` int(11) NOT NULL,
  `userId` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`userRoleId`),
  UNIQUE KEY `assignedRoleId_userId` (`assignedRoleId`,`userId`),
  KEY `userId` (`userId`),
  CONSTRAINT `userRoles_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `userRoles_ibfk_4` FOREIGN KEY (`assignedRoleId`) REFERENCES `assignedRoles` (`assignedRoleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userId` bigint(20) unsigned NOT NULL,
  `surname` varchar(200) NOT NULL DEFAULT '',
  `name` varchar(200) NOT NULL DEFAULT '',
  `adult` bit(1) DEFAULT b'0',
  `schoolId` int(10) unsigned DEFAULT NULL,
  `access_token` varchar(100) NOT NULL,
  `refresh_token` varchar(100) NOT NULL,
  `expires_in` datetime NOT NULL,
  PRIMARY KEY (`userId`),
  KEY `schoolId` (`schoolId`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`schoolId`) REFERENCES `schools` (`schoolId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `matches`;
CREATE TABLE `matches` (
  `matchId` int(11) NOT NULL AUTO_INCREMENT,
  `stageId` int(11) NOT NULL,
  `firstTeamId` int(10) unsigned NOT NULL,
  `secondTeamId` int(10) unsigned NOT NULL,
  `firstTeamResult` int(11) NOT NULL,
  `secondTeamResult` int(11) NOT NULL,
  PRIMARY KEY (`matchId`),
  KEY `firstTeamId` (`firstTeamId`),
  KEY `secondTeamId` (`secondTeamId`),
  KEY `stageId` (`stageId`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`firstTeamId`) REFERENCES `teams` (`teamId`),
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`secondTeamId`) REFERENCES `teams` (`teamId`),
  CONSTRAINT `matches_ibfk_4` FOREIGN KEY (`stageId`) REFERENCES `stages` (`stageId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `stages`;
CREATE TABLE `stages` (
  `stageId` int(11) NOT NULL AUTO_INCREMENT,
  `eventId` int(11) NOT NULL,
  `stageName` text NOT NULL,
  `stageIndex` int(11) NOT NULL,
  PRIMARY KEY (`stageId`),
  KEY `eventId` (`eventId`),
  CONSTRAINT `stages_ibfk_1` FOREIGN KEY (`eventId`) REFERENCES `events` (`eventId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP VIEW IF EXISTS `matchesAll`;
CREATE TABLE `matchesAll` (`matchId` int(11), `stageId` int(11), `firstTeamId` int(10) unsigned, `secondTeamId` int(10) unsigned, `firstTeamResult` int(11), `secondTeamResult` int(11), `eventId` int(11), `stageName` text, `stageIndex` int(11), `date` date, `beginTime` time, `endTime` time, `gameId` int(10) unsigned, `description` tinytext, `eventType` varchar(10));

DROP TABLE IF EXISTS `matchesAll`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `matchesAll` AS select `matches`.`matchId` AS `matchId`,`matches`.`stageId` AS `stageId`,`matches`.`firstTeamId` AS `firstTeamId`,`matches`.`secondTeamId` AS `secondTeamId`,`matches`.`firstTeamResult` AS `firstTeamResult`,`matches`.`secondTeamResult` AS `secondTeamResult`,`stages`.`eventId` AS `eventId`,`stages`.`stageName` AS `stageName`,`stages`.`stageIndex` AS `stageIndex`,`events`.`date` AS `date`,`events`.`beginTime` AS `beginTime`,`events`.`endTime` AS `endTime`,`events`.`gameId` AS `gameId`,`events`.`description` AS `description`,`events`.`eventType` AS `eventType` from ((`matches` left join `stages` on(`stages`.`stageId` = `matches`.`stageId`)) left join `events` on(`stages`.`eventId` = `events`.`eventId`));

DROP TABLE IF EXISTS `teamInfo`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `teamInfo` AS select `teams`.`teamId` AS `teamId`,`teams`.`name` AS `name`,`teams`.`gameId` AS `gameId`,`teams`.`canPlaySince` AS `canPlaySince`,`teams`.`joinString` AS `joinString`,`registrations`.`userId` AS `userId`,`registrations`.`nick` AS `nick`,`registrations`.`role` AS `role`,`registrations`.`rank` AS `rank`,`registrations`.`maxRank` AS `maxRank` from (`teams` join `registrations` on(`teams`.`teamId` = `registrations`.`teamId`)) order by `teams`.`teamId`,`registrations`.`role`;

DROP TABLE IF EXISTS `eligibleTeams`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `eligibleTeams` AS select `teamInfo`.`teamId` AS `teamId`,`teamInfo`.`name` AS `name`,`teamInfo`.`gameId` AS `gameId`,`teamInfo`.`canPlaySince` AS `canPlaySince`,`teamInfo`.`joinString` AS `joinString`,`teamInfo`.`userId` AS `userId`,`teamInfo`.`nick` AS `nick`,`teamInfo`.`role` AS `role`,`teamInfo`.`rank` AS `rank`,`teamInfo`.`maxRank` AS `maxRank` from `teamInfo` where `teamInfo`.`canPlaySince` is not null order by `teamInfo`.`canPlaySince`, `teamInfo`.`teamId`, `teamInfo`.`role`;

DROP EVENT IF EXISTS `Delete orphaned state`;
CREATE EVENT `Delete orphaned state` ON SCHEDULE EVERY 1 HOUR STARTS '2023-10-10 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO delete from states where date < (NOW() - INTERVAL 45 MINUTE);

DELIMITER ;;
CREATE TRIGGER `registrations_restrict` BEFORE INSERT ON `registrations` FOR EACH ROW
IF (
        (SELECT COUNT(*) FROM registrations LEFT JOIN teams ON registrations.teamId=teams.teamId WHERE registrations.userId=NEW.userId AND teams.gameId=(
            SELECT gameId FROM teams WHERE teamId=NEW.teamId)
        ) <> 0
    ) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Already registered for game';
END IF;;
