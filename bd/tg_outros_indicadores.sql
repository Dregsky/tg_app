CREATE DATABASE  IF NOT EXISTS `tg` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `tg`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tg
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `outros_indicadores`
--

DROP TABLE IF EXISTS `outros_indicadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outros_indicadores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome_UNIQUE` (`nome`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outros_indicadores`
--

LOCK TABLES `outros_indicadores` WRITE;
/*!40000 ALTER TABLE `outros_indicadores` DISABLE KEYS */;
INSERT INTO `outros_indicadores` VALUES (11,'indicadores_da_conjuntura_economica_emprego_na_industria_de_transformacao'),(10,'indicadores_da_conjuntura_economica_horas_trabalhadas_na_producao_na_industria_de_transformacao'),(12,'indicadores_da_conjuntura_economica_salario_real_na_industria_de_transformacao'),(9,'indicadores_da_conjuntura_economica_vendas_industriais_reais'),(6,'indicadores_de_nivel_de_emprego_formal_comercio'),(8,'indicadores_de_nivel_de_emprego_formal_construcao_civil'),(5,'indicadores_de_nivel_de_emprego_formal_industria_de_transformacao'),(7,'indicadores_de_nivel_de_emprego_formal_servico'),(1,'indice_de_commodites_agropecuaria'),(4,'indice_de_commodites_crb'),(3,'indice_de_commodites_energia'),(2,'indice_de_commodites_metal'),(13,'taxa_de_desocupacao_media');
/*!40000 ALTER TABLE `outros_indicadores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-04  2:18:57
