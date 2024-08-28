SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';
SET NAMES utf8mb4;

DROP EVENT IF EXISTS `Delete orphaned state`;;
CREATE EVENT `Delete orphaned state` ON SCHEDULE EVERY 1 HOUR STARTS '2023-10-10 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO delete from states where date < (NOW() - INTERVAL 45 MINUTE);;

DROP TABLE IF EXISTS `assignedRolePermissions`;
CREATE TABLE `assignedRolePermissions` (
  `rolePermissionId` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(20) NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `assignedRoleId` int(11) NOT NULL,
  PRIMARY KEY (`rolePermissionId`),
  UNIQUE KEY `permission_assignedRoleId_gameId` (`permission`,`assignedRoleId`,`gameId`),
  KEY `assignedRoleId` (`assignedRoleId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `assignedRolePermissions_ibfk_1` FOREIGN KEY (`permission`) REFERENCES `permissions` (`permission`),
  CONSTRAINT `assignedRolePermissions_ibfk_2` FOREIGN KEY (`assignedRoleId`) REFERENCES `assignedRoles` (`assignedRoleId`),
  CONSTRAINT `assignedRolePermissions_ibfk_3` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



INSERT INTO `assignedRolePermissions` (`rolePermissionId`, `permission`, `gameId`, `assignedRoleId`) VALUES
(10,	'event.create',	NULL,	1),
(12,	'event.delete',	NULL,	1),
(13,	'event.listAll',	NULL,	3),
(3,	'event.read',	NULL,	5),
(11,	'event.update',	NULL,	1),
(14,	'game.listAll',	NULL,	5),
(18,	'game.update',	NULL,	1),
(16,	'gamePage.read',	NULL,	5),
(17,	'gamePage.update',	NULL,	1),
(23,	'match.create',	NULL,	1),
(26,	'match.delete',	NULL,	1),
(24,	'match.read',	NULL,	5),
(25,	'match.update',	NULL,	1),
(27,	'page.read',	NULL,	5),
(28,	'school.listAll',	NULL,	5),
(20,	'stage.create',	NULL,	1),
(22,	'stage.delete',	NULL,	1),
(19,	'stage.read',	NULL,	5),
(21,	'stage.update',	NULL,	1),
(44,	'team.create',	NULL,	4),
(48,	'team.genJoinStr',	NULL,	1),
(47,	'team.genJoinStrMy',	NULL,	4),
(46,	'team.join',	NULL,	4),
(51,	'team.kick',	NULL,	1),
(50,	'team.kickTeam',	NULL,	4),
(49,	'team.leave',	NULL,	4),
(42,	'team.listPartic',	NULL,	5),
(43,	'team.listParticDisc',	NULL,	1),
(45,	'team.read',	NULL,	5),
(36,	'user.delete',	NULL,	1),
(35,	'user.deleteMe',	NULL,	4),
(37,	'user.exists',	NULL,	4),
(41,	'user.listTeams',	NULL,	1),
(40,	'user.listTeamsMe',	NULL,	4),
(39,	'user.permissionList',	NULL,	1),
(38,	'user.permsListMe',	NULL,	4),
(30,	'user.read',	NULL,	1),
(29,	'user.readMe',	NULL,	4),
(33,	'user.update',	NULL,	1),
(32,	'user.updateMe',	NULL,	4);

DROP TABLE IF EXISTS `assignedRoles`;
CREATE TABLE `assignedRoles` (
  `assignedRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `roleName` varchar(20) NOT NULL,
  `discordRoleId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`assignedRoleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `assignedRoles` (`assignedRoleId`, `roleName`, `discordRoleId`) VALUES
(1,	'admin',	NULL),
(2,	'gameOrganizer',	NULL),
(3,	'public',	NULL),
(4,	'user',	NULL),
(5,	'public',	NULL);

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
  `gamePage` mediumtext NOT NULL,
  `maxTeams` int(10) unsigned NOT NULL,
  PRIMARY KEY (`gameId`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS `generatedRolePermissions`;
CREATE TABLE `generatedRolePermissions` (
  `generatedRolePermissionsId` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(20) NOT NULL,
  `generatedRoleId` int(11) NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `eligible` bit(1) NOT NULL,
  PRIMARY KEY (`generatedRolePermissionsId`),
  KEY `permission` (`permission`),
  KEY `generatedRoleId` (`generatedRoleId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `generatedRolePermissions_ibfk_1` FOREIGN KEY (`permission`) REFERENCES `permissions` (`permission`),
  CONSTRAINT `generatedRolePermissions_ibfk_2` FOREIGN KEY (`generatedRoleId`) REFERENCES `generatedRoles` (`generatedRoleId`),
  CONSTRAINT `generatedRolePermissions_ibfk_3` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `generatedRoles`;
CREATE TABLE `generatedRoles` (
  `generatedRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `roleName` varchar(40) NOT NULL,
  `discordRoleId` int(11),
  `discordRoleIdEligible` int(11),
  `gameId` int(10) unsigned NOT NULL,
  `default` bit(1) NOT NULL,
  `minimal` int(11) NOT NULL,
  `maximal` int(11) NOT NULL,
  PRIMARY KEY (`generatedRoleId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `generatedRoles_ibfk_1` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
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


DROP VIEW IF EXISTS `matchesAll`;
CREATE TABLE `matchesAll` (`matchId` int(11), `stageId` int(11), `firstTeamId` int(10) unsigned, `secondTeamId` int(10) unsigned, `firstTeamResult` int(11), `secondTeamResult` int(11), `eventId` int(11), `stageName` text, `stageIndex` int(11), `date` date, `beginTime` time, `endTime` time, `gameId` int(10) unsigned, `description` tinytext, `eventType` varchar(10));


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
  `generatedRoleId` int(11) NOT NULL,
  `nick` varchar(100) NOT NULL,
  `rank` int(11) NOT NULL,
  `maxRank` int(11) NOT NULL,
  KEY `teamId` (`teamId`),
  KEY `userId` (`userId`),
  KEY `generatedRoleId` (`generatedRoleId`),
  CONSTRAINT `registrations_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`),
  CONSTRAINT `registrations_ibfk_2` FOREIGN KEY (`teamId`) REFERENCES `teams` (`teamId`),
  CONSTRAINT `registrations_ibfk_3` FOREIGN KEY (`generatedRoleId`) REFERENCES `generatedRoles` (`generatedRoleId`)
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
CREATE TABLE `teamInfo` (`teamId` int(10) unsigned, `name` varchar(200), `gameId` int(10) unsigned, `canPlaySince` timestamp, `joinString` varchar(200), `userId` bigint(20) unsigned, `nick` varchar(100), `rank` int(11), `maxRank` int(11));


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

DROP TABLE IF EXISTS `matchesAll`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `matchesAll` AS select `matches`.`matchId` AS `matchId`,`matches`.`stageId` AS `stageId`,`matches`.`firstTeamId` AS `firstTeamId`,`matches`.`secondTeamId` AS `secondTeamId`,`matches`.`firstTeamResult` AS `firstTeamResult`,`matches`.`secondTeamResult` AS `secondTeamResult`,`stages`.`eventId` AS `eventId`,`stages`.`stageName` AS `stageName`,`stages`.`stageIndex` AS `stageIndex`,`events`.`date` AS `date`,`events`.`beginTime` AS `beginTime`,`events`.`endTime` AS `endTime`,`events`.`gameId` AS `gameId`,`events`.`description` AS `description`,`events`.`eventType` AS `eventType` from ((`matches` left join `stages` on(`stages`.`stageId` = `matches`.`stageId`)) left join `events` on(`stages`.`eventId` = `events`.`eventId`));

DROP TABLE IF EXISTS `teamInfo`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `teamInfo` AS select `teams`.`teamId` AS `teamId`,`teams`.`name` AS `name`,`teams`.`gameId` AS `gameId`,`teams`.`canPlaySince` AS `canPlaySince`,`teams`.`joinString` AS `joinString`,`registrations`.`userId` AS `userId`,`registrations`.`nick` AS `nick`,`registrations`.`rank` AS `rank`,`registrations`.`maxRank` AS `maxRank`, `registrations`.`generatedRoleId` AS `generatedRoleId` from (`teams` join `registrations` on(`teams`.`teamId` = `registrations`.`teamId`)) order by `teams`.`teamId`;

DROP VIEW IF EXISTS `eligibleTeams`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `eligibleTeams` AS select `teamInfo`.`teamId` AS `teamId`,`teamInfo`.`name` AS `name`,`teamInfo`.`gameId` AS `gameId`,`teamInfo`.`canPlaySince` AS `canPlaySince`,`teamInfo`.`joinString` AS `joinString`,`teamInfo`.`userId` AS `userId`,`teamInfo`.`nick` AS `nick`,`teamInfo`.`rank` AS `rank`,`teamInfo`.`maxRank` AS `maxRank`, `teamInfo`.`generatedRoleId` AS `generatedRoleId` from `teamInfo` where `teamInfo`.`canPlaySince` is not null order by `teamInfo`.`canPlaySince`,`teamInfo`.`teamId`;

DROP EVENT IF EXISTS `Delete orphaned state`;
CREATE EVENT `Delete orphaned state` ON SCHEDULE EVERY 1 HOUR STARTS '2023-10-10 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO delete from states where date < (NOW() - INTERVAL 45 MINUTE);

DROP PROCEDURE IF EXISTS `registrations_restrict_user`;
DELIMITER ;;
CREATE PROCEDURE `registrations_restrict_user`(userIdV BIGINT, teamIdV INT)
BEGIN
    IF (
        (SELECT COUNT(*) FROM registrations LEFT JOIN teams ON registrations.teamId=teams.teamId WHERE registrations.userId=userIdV AND teams.gameId=(
            SELECT gameId FROM teams WHERE teamId=teamIdV)
        ) <> 0
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Already registered for game';
    END IF;
END;;

DROP TRIGGER IF EXISTS registrations_restrict_user_insert;
DELIMITER ;;
CREATE TRIGGER `registrations_restrict_user_insert` BEFORE INSERT ON `registrations` FOR EACH ROW BEGIN
    CALL registrations_restrict_user(NEW.userId, NEW.teamId);
END;;

DROP TRIGGER IF EXISTS registrations_restrict_user_update;
DELIMITER ;;
CREATE TRIGGER `registrations_restrict_user_update` BEFORE UPDATE ON `registrations` FOR EACH ROW BEGIN
    CALL registrations_restrict_user(NEW.userId, NEW.teamId);
END;;


DROP PROCEDURE IF EXISTS `registrations_restrict_role`;
DELIMITER ;;
CREATE PROCEDURE `registrations_restrict_role`(generatedRoleIdV INT, teamIdV INT)
BEGIN
    IF ((SELECT gameId FROM `generatedRoles` WHERE `generatedRoleId` = generatedRoleIdV) <> (SELECT gameId FROM `teams` WHERE `teamId` = teamIdV)) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Wrong role';
    END IF;
    IF (
        (SELECT COUNT(registrations.generatedRoleId) FROM registrations WHERE registrations.teamId = teamIdV AND registrations.generatedRoleId = generatedRoleIdV GROUP BY registrations.generatedRoleId)
        >=
        (SELECT generatedRoles.maximal FROM generatedRoles WHERE generatedRoles.generatedRoleId = generatedRoleIdV)) THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No space for this role in this team';
    END IF;
END;;

DROP TRIGGER IF EXISTS registrations_restrict_role_insert;
DELIMITER ;;
CREATE TRIGGER `registrations_restrict_role_insert` BEFORE INSERT ON `registrations` FOR EACH ROW BEGIN
    CALL registrations_restrict_role(NEW.generatedRoleId, NEW.teamId);
END;;

DROP TRIGGER IF EXISTS registrations_restrict_role_update;
DELIMITER ;;
CREATE TRIGGER `registrations_restrict_role_update` BEFORE UPDATE ON `registrations` FOR EACH ROW BEGIN
    CALL registrations_restrict_role(NEW.generatedRoleId, NEW.teamId);
END;;

DROP PROCEDURE IF EXISTS canPlay;
DELIMITER ;;
CREATE PROCEDURE canPlay(IN teamIdV INT)
BEGIN
    IF NOT EXISTS (SELECT expectedRoles.generatedRoleId, expectedRoles.minimal, teamsRole.act FROM
                   (SELECT generatedRoles.generatedRoleId, generatedRoles.minimal FROM teams JOIN games ON teams.gameId = games.gameId JOIN generatedRoles ON generatedRoles.gameId = games.gameId WHERE teams.teamId = teamIdV) AS expectedRoles
                   LEFT JOIN
                   (SELECT registrations.generatedRoleId, COUNT(registrations.generatedRoleId) AS act FROM registrations WHERE registrations.teamId = teamIdV GROUP BY registrations.generatedRoleId) AS teamsRole
                   ON expectedRoles.generatedRoleId = teamsRole.generatedRoleId WHERE expectedRoles.minimal > teamsRole.act OR teamsRole.act IS NULL
    ) THEN
        -- can play
        IF (SELECT canPlaySince FROM teams WHERE teamId = teamIdV) IS NULL THEN
            UPDATE teams SET canPlaySince = NOW() WHERE teamId = teamIdV;
        END IF;
    ELSE
        -- can not play
        IF (SELECT canPlaySince FROM teams WHERE teamId = teamIdV) IS NOT NULL THEN
            UPDATE teams SET canPlaySince = NULL WHERE teamId = teamIdV;
        END IF;
    END IF;
END;;

DROP TRIGGER IF EXISTS canPlay_insert;
DELIMITER ;;
CREATE TRIGGER `canPlay_insert` AFTER INSERT ON `registrations` FOR EACH ROW BEGIN
    CALL canPlay(NEW.teamId);
END;;

DROP TRIGGER IF EXISTS canPlay_update;
DELIMITER ;;
CREATE TRIGGER `canPlay_update` AFTER UPDATE ON `registrations` FOR EACH ROW BEGIN
    CALL canPlay(OLD.teamId);
    CALL canPlay(NEW.teamId);
END;;

DROP TRIGGER IF EXISTS canPlay_delete;
DELIMITER ;;
CREATE TRIGGER `canPlay_delete` AFTER DELETE ON `registrations` FOR EACH ROW BEGIN
    CALL canPlay(OLD.teamId);
END;;
