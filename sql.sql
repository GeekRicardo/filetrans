-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: Ricardo
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Table structure for table `Msg`
--

DROP TABLE IF EXISTS `Msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `msg` mediumtext COLLATE utf8mb4_bin,
  `time` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Msg`
--

LOCK TABLES `Msg` WRITE;
/*!40000 ALTER TABLE `Msg` DISABLE KEYS */;
INSERT INTO `Msg` VALUES (1,'ricardo','b87ecf3c-4883-11ea-8da1-52540011c219','20-02-06 11:14:37'),(2,'ricardo','test','20-02-06 11:29:50'),(3,'ricardo','测试','20-02-06 11:37:09'),(4,'ricardo','新的赛季带来了新的地图，也带来了新的通行证；这一期的通行证名字为“全面崩坏”，在新内容里，游戏可以进行大规模的破坏，也第一次出现了“黑圈”，当你在黑圈的时候，建筑物不再是你的保护伞，而会成为你的“埋盒之地”，快跑吧，远离建筑物！\n\n通行证等级\n通行证满级依然为100级，每次所需经验10，000点，和之前通行证是一样的。\n通行证时间\n通行证的的持续时间和第六赛季将会同步进行，于1月22日更新，并持续至2020年4月15日。共计12周，合计84天。\n升级卡：5/20/30/50\n价格：5/17.99/24.99/34.99（美元）\n通行证奖励\n每个通行证大家最最最关注的环节，通行证的奖励到底怎么样呢，这一次的通行证中一共有：服饰34件、武器皮肤12个、装备皮肤8个、下赛季通行证升级券14级、装扮动作12个，载具皮肤1个。\n通行证的实际奖励图放在本文最末尾，这里先放上最令人关注的猫喵头盔和绷带血迹AK：\n\n\n挑战枪械\n\n蟒蛇系列，分别为蟒蛇之吻与蟒蛇之血，枪身上刻有一条处于进攻状态的毒蛇，张开的嘴巴与微微弓起的身子，无一不是在彰显着危险二字，其中冷色调的为蟒蛇之吻，暖色调的为蟒蛇之血。\n\n这一次的挑战任务取消了服装的设定，只需要达到相应的等级就可以开始进行挑战任务，获取枪械皮肤。\n票券商店\n测试服并没有更新相应的票券服装，只有等正式服上线后我们才能知道有什么新物品了。\n任务与经验\n\n任务与经验依然与上一次通行证相等，分为社区任务、每日生存奖励、每日任务、每周任务、进程任务、赛季任务、挑战任务。\n社区任务\n\n社区任务依然是在游戏内拾取光盘，上一期通行证是让大家做免费的打工仔，这一期通行证进行了优化改进，拾取光盘后能够自身做出的贡献数，而且达到一定数量还有相应的经验奖励，这也提高了大家拾取光盘的积极度。\n每日生存奖励\n\n每日生存会根据你每场游戏的生存时间进行经验奖励，一句话只要你够肝，你就能拿经验。\n每日任务奖励\n\n每日任务都比较简单，完成三个任务后可以使用BP开启新的每日任务，总共经验8600。\n每周任务奖励\n\n每周任务是经验获取的重要途径，每周的豪华任务需要购买通行证才能完成。\n这一期的每周任务增加了新的任务类型，例如：攀爬、接受弹药等等，一定程度上优化了任务结构，让任务更有趣也更加简便了。\n进程任务\n\n进程任务一般比较简单，根据相应的要求来完成就可以了，其中有特殊的的里程碑任务，经验获取很高。\n赛季任务\n\n赛季任务必须要购买通行证才能进行，其中分为三个模块，第一个模块为：毁灭，完成后奖励两件服装，后续两个模块被锁定了，需要等待一定时间才能解锁。\n挑战任务\n挑战任务需要通行证达到相应等级进行解锁，这一次挑战任务取消了装备服装的限制，相信大家能够更快的获取到挑战皮肤了。\n结尾\n这一次的通行证质量还是属于中规中矩，个人感觉“蟒蛇系列”的皮肤十分的精美，但有相应的获取门槛，在通行证中出现的猫喵头盔和绷带AK让我眼前一亮，但其它部分皮肤都是属于偶尔穿穿的存在。\n通行证满等级依旧为100，大部分任务都能够完成，上一期的通行证因为并没有太多时间玩游戏，但我还是升到了90级，只要能够完成每周任务，通行证升满级还是很简单的，更别说这一次还有上个赛季赠送的升级券；后续大家根据自己的实际需求和时间来购买通行证和升级券就好了。\n以上就是生存通行证：全面崩坏的全部内容了，接下来我会更新游戏新内容以及新地图的测评，继续关注我吧！\n通行证奖励内容一览\n','20-02-06 11:37:24');
/*!40000 ALTER TABLE `Msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(50) NOT NULL,
  `Passwd` varchar(50) NOT NULL,
  `Level` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'ricardo','qqqqq',0),(2,'dong','11111',10),(3,'pangfoud','11111',10),(4,'test','test',100);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-07 12:37:44
