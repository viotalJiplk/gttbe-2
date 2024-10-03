SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';
SET NAMES utf8mb4;

DROP EVENT IF EXISTS `Delete orphaned state`;;
CREATE EVENT `Delete orphaned state` ON SCHEDULE EVERY 1 HOUR STARTS '2023-10-10 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO delete from states where date < (NOW() - INTERVAL 45 MINUTE);;

DROP TABLE IF EXISTS `assignedRolePermissions`;
CREATE TABLE `assignedRolePermissions` (
  `assignedRolePermissionId` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(40) NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `assignedRoleId` int(11) NOT NULL,
  PRIMARY KEY (`assignedRolePermissionId`),
  UNIQUE KEY `permission_assignedRoleId_gameId` (`permission`,`assignedRoleId`,`gameId`),
  KEY `assignedRoleId` (`assignedRoleId`),
  KEY `gameId` (`gameId`),
  CONSTRAINT `assignedRolePermissions_ibfk_1` FOREIGN KEY (`permission`) REFERENCES `permissions` (`permission`),
  CONSTRAINT `assignedRolePermissions_ibfk_2` FOREIGN KEY (`assignedRoleId`) REFERENCES `assignedRoles` (`assignedRoleId`),
  CONSTRAINT `assignedRolePermissions_ibfk_3` FOREIGN KEY (`gameId`) REFERENCES `games` (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



INSERT INTO `assignedRolePermissions` (`assignedRolePermissionId`, `permission`, `gameId`, `assignedRoleId`) VALUES
(1, 	'event.create',	        NULL,	1),
(2,	    'event.delete',	        NULL,	1),
(3, 	'event.listAll',	    NULL,	4),
(4,	    'event.read',	        NULL,	4),
(5,	    'event.update', 	    NULL,	1),
(6,	    'event.listStages', 	NULL,	1),
(7,     'event.listMatches',    NULL,   3),
(8, 	'game.listAll',	        NULL,	4),
(9, 	'game.update',	        NULL,	1),
(10, 	'gamePage.read',	    NULL,	4),
(11,	'gamePage.update',	    NULL,	1),
(12,	'match.create',	        NULL,	1),
(13,	'match.delete',	        NULL,	1),
(14,	'match.read',	        NULL,	4),
(15,	'match.update',	        NULL,	1),
(16,	'match.listAll',	    NULL,	1),
(17,	'page.read',	        NULL,	4),
(18,	'school.listAll',	    NULL,	4),
(19,	'stage.create',	        NULL,	1),
(20,	'stage.delete', 	    NULL,	1),
(21,	'stage.read',	        NULL,	4),
(22,	'stage.update', 	    NULL,	1),
(23,	'stage.listAll', 	    NULL,	1),
(24,	'stage.listMatches', 	NULL,	1),
(25,	'team.create',	        NULL,	3),
(26,	'team.generateJoinString',	    NULL,	1),
(27,	'team.generateJoinStringMy',	NULL,	3),
(28,	'team.join',	        NULL,	3),
(29,	'team.kick',	        NULL,	1),
(30,	'team.kickTeam',	    NULL,	3),
(31,	'team.leave',	        NULL,	3),
(32,	'team.listParticipating',	    NULL,	4),
(33,	'team.listParticipatingDiscord',	NULL,	1),
(34,	'team.read',	        NULL,	4),
(35,	'user.delete',	        NULL,	1),
(36,	'user.deleteMe',	    NULL,	3),
(37,	'user.exists',	        NULL,	3),
(38,	'user.listTeams',	    NULL,	1),
(39,	'user.listTeamsMe',	    NULL,	3),
(40,	'user.permissionList',	NULL,	1),
(41,	'user.permsListMe',	    NULL,	3),
(42,	'user.read',	        NULL,	1),
(43,	'user.readMe',	        NULL,	3),
(44,	'user.update',	        NULL,	1),
(45,	'user.updateMe',	    NULL,	3),
(46,	'assignedRole.create',	NULL,	1),
(47,	'assignedRole.read',	NULL,	4),
(48,	'assignedRole.update',	NULL,	1),
(49,	'assignedRole.delete',	NULL,	1),
(50,	'assignedRole.listPermissions',	NULL,	4),
(51,	'assignedRole.listAll',	NULL,	1),
(52,	'assignedRolePermission.create',	NULL,	1),
(53,	'assignedRolePermission.read',	NULL,	4),
(54,	'assignedRolePermission.update',	NULL,	1),
(55,	'assignedRolePermission.delete',	NULL,	1),
(56,	'generatedRole.create',	NULL,	1),
(57,	'generatedRole.read',	NULL,	4),
(58,	'generatedRole.update',	NULL,	1),
(59,	'generatedRole.delete',	NULL,	1),
(60,	'generatedRole.listPermissions',	NULL,	4),
(61,	'generatedRole.listAll',	NULL,	4),
(62,	'generatedRolePermission.create',	NULL,	1),
(63,	'generatedRolePermission.read',	NULL,	4),
(64,	'generatedRolePermission.update',	NULL,	1),
(65,	'generatedRolePermission.delete',	NULL,	1),
(66,	'userRole.create',	NULL,	1),
(67,	'userRole.read',	NULL,	4),
(68,	'userRole.update',	NULL,	1),
(69,	'userRole.delete',	NULL,	1),
(70,    'user.generatedRolesList',  NULL, 1),
(71,    'user.generatedRolesListMe',    NULL, 4),
(72,    'user.assignedRolesList',    NULL, 4),
(73,    'user.assignedRolesListMe', NULL, 1),
(74,    'permission.listAll', NULL, 1);

DROP TABLE IF EXISTS `assignedRoles`;
CREATE TABLE `assignedRoles` (
  `assignedRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `roleName` varchar(20) NOT NULL,
  `discordRoleId` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`assignedRoleId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `assignedRoles` (`assignedRoleId`, `roleName`, `discordRoleId`) VALUES
(1,	'admin',	        NULL),
(2,	'gameOrganizer',	NULL),
(3,	'user',	            NULL),
(4,	'public',	        NULL);

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
  `generatedRolePermissionId` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(40) NOT NULL,
  `generatedRoleId` int(11) NOT NULL,
  `gameId` int(10) unsigned DEFAULT NULL,
  `eligible` bit(1) NOT NULL,
  PRIMARY KEY (`generatedRolePermissionId`),
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
  `firstTeamResult` int(11) DEFAULT NULL,
  `secondTeamResult` int(11) DEFAULT NULL,
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
  `permission` varchar(40) NOT NULL,
  PRIMARY KEY (`permission`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `permissions` (`permission`) VALUES
('event.create'),
('event.delete'),
('event.listAll'),
('event.listMatches'),
('event.read'),
('event.update'),
('event.listStages'),
('game.listAll'),
('game.read'),
('game.update'),
('gamePage.read'),
('gamePage.update'),
('match.create'),
('match.delete'),
('match.read'),
('match.update'),
('match.listAll'),
('page.read'),
('school.listAll'),
('stage.create'),
('stage.delete'),
('stage.read'),
('stage.update'),
('stage.listAll'),
('stage.listMatches'),
('team.create'),
('team.generateJoinString'),
('team.generateJoinStringMy'),
('team.join'),
('team.kick'),
('team.kickTeam'),
('team.leave'),
('team.listParticipating'),
('team.listParticipatingDiscord'),
('team.read'),
('user.delete'),
('user.deleteMe'),
('user.exists'),
('user.listTeams'),
('user.listTeamsMe'),
('user.generatedRolesList'),
('user.generatedRolesListMe'),
('user.assignedRolesList'),
('user.assignedRolesListMe'),
('user.permissionList'),
('user.permsListMe'),
('user.read'),
('user.readMe'),
('user.update'),
('user.updateMe'),
('assignedRole.create'),
('assignedRole.read'),
('assignedRole.update'),
('assignedRole.delete'),
('assignedRole.listPermissions'),
('assignedRole.listAll'),
('assignedRolePermission.create'),
('assignedRolePermission.read'),
('assignedRolePermission.update'),
('assignedRolePermission.delete'),
('generatedRole.create'),
('generatedRole.read'),
('generatedRole.update'),
('generatedRole.delete'),
('generatedRole.listPermissions'),
('generatedRole.listAll'),
('generatedRolePermission.create'),
('generatedRolePermission.read'),
('generatedRolePermission.update'),
('generatedRolePermission.delete'),
('userRole.create'),
('userRole.read'),
('userRole.update'),
('userRole.delete'),
('permission.listAll');

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
  `camera` bit(1) NOT NULL DEFAULT b'0',
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
