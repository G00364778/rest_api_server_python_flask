-- MySQL dump 10.13  Distrib 8.0.14, for Win64 (x86_64)
--
-- Host: localhost    Database: jattie$default
-- ------------------------------------------------------
-- Server version	8.0.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pisense`
--

DROP TABLE IF EXISTS `pisense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pisense` (
  `idx` int(11) NOT NULL AUTO_INCREMENT,
  `dts` datetime DEFAULT NULL,
  `tempexternal` int(11) DEFAULT NULL,
  `temponboard` int(11) DEFAULT NULL,
  `brightness` int(11) DEFAULT NULL,
  `humidity` int(11) DEFAULT NULL,
  `barotemp` int(11) DEFAULT NULL,
  `baropressure` int(11) DEFAULT NULL,
  `motiondetected` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pisense`
--

LOCK TABLES `pisense` WRITE;
/*!40000 ALTER TABLE `pisense` DISABLE KEYS */;
INSERT INTO `pisense` VALUES (1,'2019-12-11 12:04:43',21,26,-2,20,27,1009,0),(2,'2019-12-11 12:05:08',21,26,-2,20,27,1009,0),(3,'2019-12-11 12:05:10',20,25,-2,23,27,1009,0),(4,'2019-12-11 12:05:11',21,26,-2,26,27,996,0),(5,'2019-12-11 12:05:12',21,26,-2,22,27,997,0),(6,'2019-12-11 12:05:12',21,26,-2,17,27,997,0),(7,'2019-12-11 12:05:13',20,26,-2,16,27,997,0),(8,'2019-12-11 12:05:14',20,26,-2,17,27,998,0),(9,'2019-12-11 12:05:15',21,26,-2,16,27,997,0),(10,'2019-12-11 12:05:15',19,26,-2,15,27,997,0),(11,'2019-12-11 12:05:16',19,26,-2,15,27,995,0),(12,'2019-12-11 12:05:17',19,26,-2,15,27,995,0),(13,'2019-12-11 12:05:18',20,26,-2,15,27,994,0),(14,'2019-12-11 12:05:19',19,26,-2,15,27,993,0),(15,'2019-12-11 12:05:20',20,26,-2,20,27,994,0),(16,'2019-12-11 12:05:21',21,26,-2,15,27,994,0),(17,'2019-12-11 12:05:22',21,26,-2,21,27,994,0),(18,'2019-12-11 12:05:22',21,26,-2,17,27,994,0),(19,'2019-12-11 12:05:23',20,26,-2,17,27,994,0),(20,'2019-12-11 12:05:24',20,26,-2,16,27,995,0);
/*!40000 ALTER TABLE `pisense` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-12 11:44:03