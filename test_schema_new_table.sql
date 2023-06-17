-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: test_schema
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `new_table`
--

DROP TABLE IF EXISTS `new_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_table` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `discount` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_table`
--

LOCK TABLES `new_table` WRITE;
/*!40000 ALTER TABLE `new_table` DISABLE KEYS */;
INSERT INTO `new_table` VALUES (1,'Ori and the Will of the Wisps','-80%','21,59 zĹ‚'),(2,'Subnautica','-67%','35,63 zĹ‚'),(3,'INSIDE','-90%','7,19 zĹ‚'),(4,'Moons of Madness','-70%','26,99 zĹ‚'),(5,'Deep Rock Galactic','-67%','35,63 zĹ‚'),(6,'Metal: Hellsinger','-34%','72,59 zĹ‚'),(7,'Grand Theft Auto IV: The Complete Edition','-70%','25,47 zĹ‚'),(8,'Bright Memory','-40%','17,39 zĹ‚'),(9,'Call of Duty: Vanguard','-50%','144,50 zĹ‚'),(10,'Bridge Constructor Portal','-88%','4,31 zĹ‚'),(11,'SUPERHOT','-70%','8,99 zĹ‚'),(12,'A Plague Tale: Requiem','-35%','110,49 zĹ‚'),(13,'Bright Memory: Infinite','-25%','53,99 zĹ‚'),(14,'Momodora: Reverie Under The Moonlight','-60%','14,39 zĹ‚'),(15,'La-Mulana 2','-50%','44,99 zĹ‚'),(16,'Moonlighter','-85%','10,49 zĹ‚'),(17,'The Wandering Village','-20%','71,99 zĹ‚'),(18,'Loot River','-35%','38,99 zĹ‚'),(19,'BLACKTAIL','-34%','79,19 zĹ‚'),(20,'Subnautica Sub-Sonic Edition','-70%','42,75 zĹ‚'),(21,'House of the Dying Sun','-70%','21,59 zĹ‚'),(22,'Resident Evil 3','-75%','44,75 zĹ‚'),(23,'Capcom Fighting Collection','-50%','89,50 zĹ‚'),(24,'Steelrising','-50%','89,99 zĹ‚'),(25,'ICEY','-50%','19,99 zĹ‚'),(26,'TASOMACHI: Behind the Twilight','-50%','35,99 zĹ‚'),(27,'Resident Evil 2','-75%','42,25 zĹ‚'),(28,'Sun Haven','-20%','71,99 zĹ‚'),(29,'Hatsune Miku: Project DIVA Mega Mix+','-44%','81,95 zĹ‚'),(30,'Halo Infinite (Campaign)','-50%','124,95 zĹ‚'),(31,'Dead by Daylight','-60%','28,79 zĹ‚'),(32,'Devil May Cry 4 Special Edition','-70%','31,20 zĹ‚'),(33,'Devil May Cry 5','-67%','39,60 zĹ‚'),(34,'Conan Unconquered','-70%','21,59 zĹ‚'),(35,'Need for Speed Unbound','-50%','149,95 zĹ‚'),(36,'DNF Duel','-50%','109,99 zĹ‚'),(37,'Hardspace: Shipbreaker','-35%','77,99 zĹ‚'),(38,'Total War: WARHAMMER III','-33%','147,39 zĹ‚'),(39,'The Silver Case','-60%','28,79 zĹ‚'),(40,'Mighty Goose','-50%','35,99 zĹ‚'),(41,'Red Dead Redemption 2','-67%','82,46 zĹ‚'),(42,'Mega Man 11','-67%','40,92 zĹ‚'),(43,'Phoenix Wright: Ace Attorney Trilogy','-50%','62,00 zĹ‚'),(44,'Streets of Rage 4','-50%','57,49 zĹ‚'),(45,'DuckTales: Remastered','-75%','14,49 zĹ‚'),(46,'Dune: Spice Wars','-20%','87,99 zĹ‚'),(47,'MONSTER HUNTER RISE','-80%','21,59 zĹ‚'),(48,'Monster Hunter: World','-80%','21,99 zĹ‚'),(49,'Ghosts \'n Goblins Resurrection','-50%','~32,72 zĹ‚'),(50,'The Riftbreaker','-50%','89,50 zĹ‚'),(51,'Dreamfall: The Longest Journey','-50%','62,50 zĹ‚'),(52,'Escape Simulator','-35%','62,45 zĹ‚'),(53,'Project Warlock II','-70%','64,35 zĹ‚');
/*!40000 ALTER TABLE `new_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 21:39:17
