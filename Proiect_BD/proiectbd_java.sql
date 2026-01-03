create database proiectBD_Java;
show schemas;
use proiectbd_java;

DROP TABLE IF EXISTS `clasa`;
CREATE TABLE `clasa` (
  `idclasa` int(11) NOT NULL AUTO_INCREMENT,
  `idprofesor` int(11) DEFAULT NULL,
  `idcurs` int(11) DEFAULT NULL,
  `DataCurs` varchar(45) DEFAULT NULL,
  `Clasa` varchar(45) DEFAULT NULL,
  `NumarElevi` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idclasa`),
  KEY `fk_link_1_idx` (`idcurs`),
  KEY `fk_link_2_idx` (`idprofesor`),
  CONSTRAINT `fk_link_1` FOREIGN KEY (`idcurs`) REFERENCES `curs` (`idcurs`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_link_2` FOREIGN KEY (`idprofesor`) REFERENCES `profesori` (`idprofesor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;


LOCK TABLES `clasa` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `curs`;
CREATE TABLE `curs` (
  `idcurs` int(11) NOT NULL AUTO_INCREMENT,
  `Nume` varchar(45) DEFAULT NULL,
  `Disciplina` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcurs`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

LOCK TABLES `curs` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `profesori`;
CREATE TABLE `profesori` (
  `idprofesor` int(11) NOT NULL AUTO_INCREMENT,
  `Nume` varchar(45) DEFAULT NULL,
  `Prenume` varchar(45) DEFAULT NULL,
  `Disciplina` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idprofesor`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

LOCK TABLES `profesori` WRITE;
UNLOCK TABLES;


select user from mysql.user