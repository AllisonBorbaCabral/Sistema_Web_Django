-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: sistema_web
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sistema_cidade`
--

DROP TABLE IF EXISTS `sistema_cidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_cidade` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NM_CIDADE` varchar(100) NOT NULL,
  `DDD` varchar(2) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `ID_ESTADO` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_ESTADO` (`ID_ESTADO`),
  CONSTRAINT `sistema_cidade_ibfk_1` FOREIGN KEY (`ID_ESTADO`) REFERENCES `sistema_estado` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_cidade`
--

LOCK TABLES `sistema_cidade` WRITE;
/*!40000 ALTER TABLE `sistema_cidade` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_cidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_cliente`
--

DROP TABLE IF EXISTS `sistema_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_cliente` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NM_PESSOA_RAZAO_SOCIAL` varchar(255) NOT NULL,
  `CPF_CNPJ` varchar(14) NOT NULL,
  `RUA` varchar(255) NOT NULL,
  `BAIRRO` varchar(255) NOT NULL,
  `NUMERO` varchar(255) NOT NULL,
  `COMPLEMENTO` varchar(255) DEFAULT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `ID_CIDADE` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CPF_CNPJ` (`CPF_CNPJ`),
  KEY `ID_CIDADE` (`ID_CIDADE`),
  CONSTRAINT `sistema_cliente_ibfk_1` FOREIGN KEY (`ID_CIDADE`) REFERENCES `sistema_cidade` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_cliente`
--

LOCK TABLES `sistema_cliente` WRITE;
/*!40000 ALTER TABLE `sistema_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_condicao_pagto`
--

DROP TABLE IF EXISTS `sistema_condicao_pagto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_condicao_pagto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DS_CONDICAO_PAGTO` varchar(255) NOT NULL,
  `MULTA` decimal(19,2) NOT NULL,
  `JUROS` decimal(19,2) NOT NULL,
  `DESC_FINANCEIRO` decimal(19,2) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_condicao_pagto`
--

LOCK TABLES `sistema_condicao_pagto` WRITE;
/*!40000 ALTER TABLE `sistema_condicao_pagto` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_condicao_pagto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_contas_receber`
--

DROP TABLE IF EXISTS `sistema_contas_receber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_contas_receber` (
  `ID_VENDA` int NOT NULL,
  `ID_PEDIDO` int NOT NULL,
  `ID_CLIENTE` int NOT NULL,
  PRIMARY KEY (`ID_VENDA`,`ID_PEDIDO`,`ID_CLIENTE`),
  KEY `ID_PEDIDO` (`ID_PEDIDO`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  CONSTRAINT `sistema_contas_receber_ibfk_1` FOREIGN KEY (`ID_VENDA`) REFERENCES `sistema_venda` (`ID`),
  CONSTRAINT `sistema_contas_receber_ibfk_2` FOREIGN KEY (`ID_PEDIDO`) REFERENCES `sistema_venda` (`ID_PEDIDO`),
  CONSTRAINT `sistema_contas_receber_ibfk_3` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `sistema_venda` (`ID_CLIENTE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_contas_receber`
--

LOCK TABLES `sistema_contas_receber` WRITE;
/*!40000 ALTER TABLE `sistema_contas_receber` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_contas_receber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_cor`
--

DROP TABLE IF EXISTS `sistema_cor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_cor` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DS_COR` varchar(255) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `SITUACAO` char(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_cor`
--

LOCK TABLES `sistema_cor` WRITE;
/*!40000 ALTER TABLE `sistema_cor` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_cor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_cor_grade`
--

DROP TABLE IF EXISTS `sistema_cor_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_cor_grade` (
  `ID_COR` int NOT NULL,
  `ID_GRADE_COR` int NOT NULL,
  PRIMARY KEY (`ID_COR`,`ID_GRADE_COR`),
  KEY `ID_GRADE_COR` (`ID_GRADE_COR`),
  CONSTRAINT `sistema_cor_grade_ibfk_1` FOREIGN KEY (`ID_COR`) REFERENCES `sistema_cor` (`ID`),
  CONSTRAINT `sistema_cor_grade_ibfk_2` FOREIGN KEY (`ID_GRADE_COR`) REFERENCES `sistema_grade_cor` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_cor_grade`
--

LOCK TABLES `sistema_cor_grade` WRITE;
/*!40000 ALTER TABLE `sistema_cor_grade` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_cor_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_estado`
--

DROP TABLE IF EXISTS `sistema_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_estado` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NM_ESTADO` varchar(100) NOT NULL,
  `UF` varchar(2) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `ID_PAIS` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_PAIS` (`ID_PAIS`),
  CONSTRAINT `sistema_estado_ibfk_1` FOREIGN KEY (`ID_PAIS`) REFERENCES `sistema_pais` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_estado`
--

LOCK TABLES `sistema_estado` WRITE;
/*!40000 ALTER TABLE `sistema_estado` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_estoque`
--

DROP TABLE IF EXISTS `sistema_estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_estoque` (
  `ID_PRODUTO` int NOT NULL,
  `ID_COR` int NOT NULL,
  `ID_TAMANHO` int NOT NULL,
  `REFERENCIA` varchar(255) NOT NULL,
  `QTD` int NOT NULL,
  `VALOR_COMPRA` decimal(19,2) NOT NULL,
  `VALOR_VENDA` decimal(19,2) NOT NULL,
  `PERC_VENDA` decimal(3,2) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID_PRODUTO`,`ID_COR`,`ID_TAMANHO`),
  KEY `ID_COR` (`ID_COR`),
  KEY `ID_TAMANHO` (`ID_TAMANHO`),
  CONSTRAINT `sistema_estoque_ibfk_1` FOREIGN KEY (`ID_PRODUTO`) REFERENCES `sistema_produto` (`ID`),
  CONSTRAINT `sistema_estoque_ibfk_2` FOREIGN KEY (`ID_COR`) REFERENCES `sistema_cor` (`ID`),
  CONSTRAINT `sistema_estoque_ibfk_3` FOREIGN KEY (`ID_TAMANHO`) REFERENCES `sistema_tamanho` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_estoque`
--

LOCK TABLES `sistema_estoque` WRITE;
/*!40000 ALTER TABLE `sistema_estoque` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_forma_pagto`
--

DROP TABLE IF EXISTS `sistema_forma_pagto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_forma_pagto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DS_FORMA_PAGTO` varchar(255) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `SITUACAO` char(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_forma_pagto`
--

LOCK TABLES `sistema_forma_pagto` WRITE;
/*!40000 ALTER TABLE `sistema_forma_pagto` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_forma_pagto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_grade_cor`
--

DROP TABLE IF EXISTS `sistema_grade_cor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_grade_cor` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_grade_cor`
--

LOCK TABLES `sistema_grade_cor` WRITE;
/*!40000 ALTER TABLE `sistema_grade_cor` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_grade_cor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_grade_tamanho`
--

DROP TABLE IF EXISTS `sistema_grade_tamanho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_grade_tamanho` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_grade_tamanho`
--

LOCK TABLES `sistema_grade_tamanho` WRITE;
/*!40000 ALTER TABLE `sistema_grade_tamanho` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_grade_tamanho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_pais`
--

DROP TABLE IF EXISTS `sistema_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_pais` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NM_PAIS` varchar(100) NOT NULL,
  `DDI` varchar(5) NOT NULL,
  `SIGLA` varchar(3) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_pais`
--

LOCK TABLES `sistema_pais` WRITE;
/*!40000 ALTER TABLE `sistema_pais` DISABLE KEYS */;
INSERT INTO `sistema_pais` VALUES (1,'BRASIL','+55','BRA','2023-03-17 23:53:17',NULL);
/*!40000 ALTER TABLE `sistema_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_parcela_condpagto`
--

DROP TABLE IF EXISTS `sistema_parcela_condpagto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_parcela_condpagto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_CONDICAO_PAGTO` int NOT NULL,
  `ID_FORMA_PAGTO` int NOT NULL,
  PRIMARY KEY (`ID`,`ID_CONDICAO_PAGTO`,`ID_FORMA_PAGTO`),
  KEY `ID_CONDICAO_PAGTO` (`ID_CONDICAO_PAGTO`),
  KEY `ID_FORMA_PAGTO` (`ID_FORMA_PAGTO`),
  CONSTRAINT `sistema_parcela_condpagto_ibfk_1` FOREIGN KEY (`ID_CONDICAO_PAGTO`) REFERENCES `sistema_condicao_pagto` (`ID`),
  CONSTRAINT `sistema_parcela_condpagto_ibfk_2` FOREIGN KEY (`ID_FORMA_PAGTO`) REFERENCES `sistema_forma_pagto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_parcela_condpagto`
--

LOCK TABLES `sistema_parcela_condpagto` WRITE;
/*!40000 ALTER TABLE `sistema_parcela_condpagto` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_parcela_condpagto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_pedido`
--

DROP TABLE IF EXISTS `sistema_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_pedido` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DT_PEDIDO` datetime NOT NULL,
  `DT_CANCELAMENTO` datetime DEFAULT NULL,
  `ID_CLIENTE` int NOT NULL,
  PRIMARY KEY (`ID`,`ID_CLIENTE`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  CONSTRAINT `sistema_pedido_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `sistema_cliente` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_pedido`
--

LOCK TABLES `sistema_pedido` WRITE;
/*!40000 ALTER TABLE `sistema_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_produto`
--

DROP TABLE IF EXISTS `sistema_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_produto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DS_PRODUTO` varchar(255) NOT NULL,
  `NCM` int NOT NULL,
  `UND` varchar(3) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  `ID_GRADE_COR` int NOT NULL,
  `ID_GRADE_TAMANHO` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_GRADE_COR` (`ID_GRADE_COR`),
  KEY `ID_GRADE_TAMANHO` (`ID_GRADE_TAMANHO`),
  CONSTRAINT `sistema_produto_ibfk_1` FOREIGN KEY (`ID_GRADE_COR`) REFERENCES `sistema_grade_cor` (`ID`),
  CONSTRAINT `sistema_produto_ibfk_2` FOREIGN KEY (`ID_GRADE_TAMANHO`) REFERENCES `sistema_grade_tamanho` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_produto`
--

LOCK TABLES `sistema_produto` WRITE;
/*!40000 ALTER TABLE `sistema_produto` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_tamanho`
--

DROP TABLE IF EXISTS `sistema_tamanho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_tamanho` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DS_TAMANHO` varchar(10) NOT NULL,
  `DT_CADASTRO` datetime NOT NULL,
  `DT_ULT_ALTERACAO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_tamanho`
--

LOCK TABLES `sistema_tamanho` WRITE;
/*!40000 ALTER TABLE `sistema_tamanho` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_tamanho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_tamanho_grade`
--

DROP TABLE IF EXISTS `sistema_tamanho_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_tamanho_grade` (
  `ID_TAMANHO` int NOT NULL,
  `ID_GRADE_TAMANHO` int NOT NULL,
  PRIMARY KEY (`ID_TAMANHO`,`ID_GRADE_TAMANHO`),
  KEY `ID_GRADE_TAMANHO` (`ID_GRADE_TAMANHO`),
  CONSTRAINT `sistema_tamanho_grade_ibfk_1` FOREIGN KEY (`ID_TAMANHO`) REFERENCES `sistema_tamanho` (`ID`),
  CONSTRAINT `sistema_tamanho_grade_ibfk_2` FOREIGN KEY (`ID_GRADE_TAMANHO`) REFERENCES `sistema_grade_tamanho` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_tamanho_grade`
--

LOCK TABLES `sistema_tamanho_grade` WRITE;
/*!40000 ALTER TABLE `sistema_tamanho_grade` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_tamanho_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_venda`
--

DROP TABLE IF EXISTS `sistema_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_venda` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_PEDIDO` int NOT NULL,
  `ID_CLIENTE` int NOT NULL,
  `ID_CONDICAO_PAGTO` int NOT NULL,
  `DT_VENDA` datetime NOT NULL,
  `DT_CANCELAMENTO` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`,`ID_PEDIDO`,`ID_CLIENTE`),
  KEY `ID_PEDIDO` (`ID_PEDIDO`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  KEY `ID_CONDICAO_PAGTO` (`ID_CONDICAO_PAGTO`),
  CONSTRAINT `sistema_venda_ibfk_1` FOREIGN KEY (`ID_PEDIDO`) REFERENCES `sistema_pedido` (`ID`),
  CONSTRAINT `sistema_venda_ibfk_2` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `sistema_pedido` (`ID_CLIENTE`),
  CONSTRAINT `sistema_venda_ibfk_3` FOREIGN KEY (`ID_CONDICAO_PAGTO`) REFERENCES `sistema_condicao_pagto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_venda`
--

LOCK TABLES `sistema_venda` WRITE;
/*!40000 ALTER TABLE `sistema_venda` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'sistema_web'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-17 21:43:50
