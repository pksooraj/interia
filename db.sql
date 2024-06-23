/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - color my world
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`color my world` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `color my world`;

/*Table structure for table `architect` */

DROP TABLE IF EXISTS `architect`;

CREATE TABLE `architect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `logid` int(11) DEFAULT NULL,
  `fname` varchar(25) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `architect` */

insert  into `architect`(`id`,`logid`,`fname`,`lname`,`dob`,`gender`,`place`,`qualification`,`email`,`phone`) values 
(1,2,'pranti','u p','2022-03-28','male','udupi','DEGREE','sa@gmail.com',9999999999),
(27,4,'babu','cd','2022-03-28','male','udupi','DEGREE','sa@gmadil.com',2131231233);

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_no` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `balance` varchar(100) DEFAULT NULL,
  `bank` varchar(100) DEFAULT NULL,
  `u_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `compid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `complaint` varchar(20) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`compid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`compid`,`userid`,`complaint`,`reply`,`date`) values 
(1,1,'EFGRDTH','jbj','2022-02-08'),
(2,1,'uybukhhgb','jbj','2022-02-25'),
(3,1,'zdvdf','jbj','2022-02-23'),
(4,19,'','pending','2022-03-14'),
(5,19,'dff','sadas','2022-03-14'),
(6,19,'ff','hg','2022-03-14'),
(7,19,'rr','ghgh','2022-03-14'),
(8,17,'rate high','ayn','2022-03-14'),
(9,17,'tt','asscsad','2022-03-21');

/*Table structure for table `curtaindesigns` */

DROP TABLE IF EXISTS `curtaindesigns`;

CREATE TABLE `curtaindesigns` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `designs` varchar(100) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `curtaindesigns` */

insert  into `curtaindesigns`(`id`,`name`,`designs`,`details`,`price`,`date`) values 
(6,'magenta','door2.png','very funny',4500,'2022-02-19'),
(7,'fyjxfyj','door1.png','zdtrhdt',7525,'2022-02-19'),
(8,'fyjxfyj','door3.png','zdtrhdt',7525,'2022-02-19'),
(9,'fyjxfyj','door4.png','zdtrhdt',7525,'2022-02-19');

/*Table structure for table `discussion` */

DROP TABLE IF EXISTS `discussion`;

CREATE TABLE `discussion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `aid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `discussion` */

insert  into `discussion`(`id`,`user_id`,`comment`,`aid`,`status`) values 
(1,19,'',1,'pending'),
(2,23,'hh',0,'pending'),
(3,1,'nice',1,'gf'),
(4,0,'s',1,'pending'),
(5,19,'ffffffgg',1,'nnjn'),
(6,19,'frr',23,'pending'),
(7,19,'hh',1,'pending'),
(8,19,'hh',27,'pending'),
(9,19,'rr',27,'pending'),
(10,19,'dsfsdf',1,'bjb'),
(11,19,'dd',1,'pending'),
(12,19,'tt',1,'pending'),
(13,17,'gg',1,'pending'),
(23,17,'cdf',27,'hbbhb');

/*Table structure for table `feedbacks` */

DROP TABLE IF EXISTS `feedbacks`;

CREATE TABLE `feedbacks` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `feedbacks` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `feedbacks` */

insert  into `feedbacks`(`fid`,`userid`,`feedbacks`,`date`) values 
(1,1,'lhuol','2022-02-19'),
(2,1,'ss','2022-03-14'),
(3,19,'rr','2022-03-14'),
(4,19,'ff','2022-03-14'),
(5,19,'bb','2022-03-14'),
(6,19,'tt','2022-03-14'),
(7,19,'vv','2022-03-14'),
(8,17,'v good','2022-03-14'),
(9,17,'bb','2022-03-14');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `usertype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'shiyas','3500','admin'),
(2,'abhishek ','2500','architect'),
(3,'hafis','2500','user'),
(4,'asd','123','user'),
(16,'abcd','123w','user'),
(17,'1','1','user'),
(18,'haa','assd','user'),
(20,'sdfsd','sdfds','user');

/*Table structure for table `upload_plans` */

DROP TABLE IF EXISTS `upload_plans`;

CREATE TABLE `upload_plans` (
  `planid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `arch_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`planid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `upload_plans` */

insert  into `upload_plans`(`planid`,`name`,`file`,`date`,`arch_lid`) values 
(2,'niuhala','pexels-photo-11140734.jpeg','2022-02-25',2);

/*Table structure for table `uploadoor` */

DROP TABLE IF EXISTS `uploadoor`;

CREATE TABLE `uploadoor` (
  `doorid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `designs` varchar(500) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`doorid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `uploadoor` */

insert  into `uploadoor`(`doorid`,`name`,`designs`,`price`,`details`,`date`) values 
(1,'ngchnf','pexels-photo-11140734.jpeg',432,'65465','2022-02-19'),
(2,'jhfhjdf','storage_emulated_0_Download_download.jpeg',64545,'hghdf','2022-02-19');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `age` bigint(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`userid`,`fname`,`lname`,`age`,`gender`,`place`,`pin`,`email`,`phone`) values 
(3,1,'lallu','ct',3,'male','chevar',60001,'monnan@CHEVARAMBALAM',6445565),
(4,17,'sreerag','pv',55,'FEMALE','hdhdh',673601,'neyyunni@gmail.com',9876543210),
(5,18,'jaja','hshs',45,'MALE','shhss',456329,'ajs@gmail.com',9847561236),
(6,19,'rdeh','jdhhd',23,'FEMALE','yshs',656261,'haab@gmail.com',9536231525),
(7,20,'ssda','asdads',23,'MALE','asdas',123456,'sdsada@gmail.com',1234567890);

/*Table structure for table `user_uploaded_designs` */

DROP TABLE IF EXISTS `user_uploaded_designs`;

CREATE TABLE `user_uploaded_designs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `designname` varchar(100) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `user_uploaded_designs` */

insert  into `user_uploaded_designs`(`id`,`designname`,`photo`,`uid`) values 
(3,'des','pexels-photo-11140734.jpeg',3),
(4,'sssrr','storage_75A5-1AF9_DCIM_Camera_IMG_20220314_121444.jpg',19),
(5,'SSgt','storage_emulated_0_Download_download.jpeg',19),
(6,'tt','storage_emulated_0_Download_download.jpeg',19),
(7,'sjsj','storage_emulated_0_DCIM_Screenshots_Screenshot_20220321-164903_WhatsApp.jpg',17),
(8,'dde','storage_emulated_0_DCIM_Screenshots_Screenshot_20220321-223231_WhatsApp.jpg',17),
(9,'u','storage_emulated_0_Android_media_com.whatsapp_WhatsApp_Media_WhatsApp_Images_IMG-20220326-WA0002.jpg',17);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
