-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 24, 2025 at 02:24 AM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_biobinconnect`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 3, 'add_permission'),
(6, 'Can change permission', 3, 'change_permission'),
(7, 'Can delete permission', 3, 'delete_permission'),
(8, 'Can view permission', 3, 'view_permission'),
(9, 'Can add group', 2, 'add_group'),
(10, 'Can change group', 2, 'change_group'),
(11, 'Can delete group', 2, 'delete_group'),
(12, 'Can view group', 2, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add tbl_ district', 6, 'add_tbl_district'),
(22, 'Can change tbl_ district', 6, 'change_tbl_district'),
(23, 'Can delete tbl_ district', 6, 'delete_tbl_district'),
(24, 'Can view tbl_ district', 6, 'view_tbl_district'),
(25, 'Can add tbl_location', 7, 'add_tbl_location'),
(26, 'Can change tbl_location', 7, 'change_tbl_location'),
(27, 'Can delete tbl_location', 7, 'delete_tbl_location'),
(28, 'Can view tbl_location', 7, 'view_tbl_location'),
(29, 'Can add tbl_residentsassociation', 8, 'add_tbl_residentsassociation'),
(30, 'Can change tbl_residentsassociation', 8, 'change_tbl_residentsassociation'),
(31, 'Can delete tbl_residentsassociation', 8, 'delete_tbl_residentsassociation'),
(32, 'Can view tbl_residentsassociation', 8, 'view_tbl_residentsassociation'),
(33, 'Can add custom user', 11, 'add_customuser'),
(34, 'Can change custom user', 11, 'change_customuser'),
(35, 'Can delete custom user', 11, 'delete_customuser'),
(36, 'Can view custom user', 11, 'view_customuser'),
(37, 'Can add household', 13, 'add_household'),
(38, 'Can change household', 13, 'change_household'),
(39, 'Can delete household', 13, 'delete_household'),
(40, 'Can view household', 13, 'view_household'),
(41, 'Can add farmer', 12, 'add_farmer'),
(42, 'Can change farmer', 12, 'change_farmer'),
(43, 'Can delete farmer', 12, 'delete_farmer'),
(44, 'Can view farmer', 12, 'view_farmer'),
(45, 'Can add compost manager', 10, 'add_compostmanager'),
(46, 'Can change compost manager', 10, 'change_compostmanager'),
(47, 'Can delete compost manager', 10, 'delete_compostmanager'),
(48, 'Can view compost manager', 10, 'view_compostmanager'),
(49, 'Can add collector', 9, 'add_collector'),
(50, 'Can change collector', 9, 'change_collector'),
(51, 'Can delete collector', 9, 'delete_collector'),
(52, 'Can view collector', 9, 'view_collector'),
(53, 'Can add tbl_ collector assignment', 14, 'add_tbl_collectorassignment'),
(54, 'Can change tbl_ collector assignment', 14, 'change_tbl_collectorassignment'),
(55, 'Can delete tbl_ collector assignment', 14, 'delete_tbl_collectorassignment'),
(56, 'Can view tbl_ collector assignment', 14, 'view_tbl_collectorassignment'),
(57, 'Can add tbl_ route', 15, 'add_tbl_route'),
(58, 'Can change tbl_ route', 15, 'change_tbl_route'),
(59, 'Can delete tbl_ route', 15, 'delete_tbl_route'),
(60, 'Can view tbl_ route', 15, 'view_tbl_route'),
(61, 'Can add tbl_ collection request', 16, 'add_tbl_collectionrequest'),
(62, 'Can change tbl_ collection request', 16, 'change_tbl_collectionrequest'),
(63, 'Can delete tbl_ collection request', 16, 'delete_tbl_collectionrequest'),
(64, 'Can view tbl_ collection request', 16, 'view_tbl_collectionrequest'),
(65, 'Can add tbl_ pickup request', 17, 'add_tbl_pickuprequest'),
(66, 'Can change tbl_ pickup request', 17, 'change_tbl_pickuprequest'),
(67, 'Can delete tbl_ pickup request', 17, 'delete_tbl_pickuprequest'),
(68, 'Can view tbl_ pickup request', 17, 'view_tbl_pickuprequest'),
(69, 'Can add tbl_ bin type', 18, 'add_tbl_bintype'),
(70, 'Can change tbl_ bin type', 18, 'change_tbl_bintype'),
(71, 'Can delete tbl_ bin type', 18, 'delete_tbl_bintype'),
(72, 'Can view tbl_ bin type', 18, 'view_tbl_bintype'),
(73, 'Can add tbl_ household payment', 19, 'add_tbl_householdpayment'),
(74, 'Can change tbl_ household payment', 19, 'change_tbl_householdpayment'),
(75, 'Can delete tbl_ household payment', 19, 'delete_tbl_householdpayment'),
(76, 'Can view tbl_ household payment', 19, 'view_tbl_householdpayment');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'MyApp', 'tbl_district'),
(7, 'MyApp', 'tbl_location'),
(8, 'MyApp', 'tbl_residentsassociation'),
(9, 'GuestApp', 'collector'),
(10, 'GuestApp', 'compostmanager'),
(11, 'GuestApp', 'customuser'),
(12, 'GuestApp', 'farmer'),
(13, 'GuestApp', 'household'),
(14, 'MyApp', 'tbl_collectorassignment'),
(15, 'MyApp', 'tbl_route'),
(16, 'MyApp', 'tbl_collectionrequest'),
(17, 'MyApp', 'tbl_pickuprequest'),
(18, 'MyApp', 'tbl_bintype'),
(19, 'MyApp', 'tbl_householdpayment');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-12-23 09:33:00.065940'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-12-23 09:33:00.127385'),
(3, 'auth', '0001_initial', '2025-12-23 09:33:00.394966'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-12-23 09:33:00.430008'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-12-23 09:33:00.449417'),
(6, 'auth', '0004_alter_user_username_opts', '2025-12-23 09:33:00.455483'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-12-23 09:33:00.460285'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-12-23 09:33:00.461932'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-12-23 09:33:00.469499'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-12-23 09:33:00.475563'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-12-23 09:33:00.481604'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-12-23 09:33:00.514545'),
(13, 'auth', '0011_update_proxy_permissions', '2025-12-23 09:33:00.521901'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-12-23 09:33:00.529911'),
(15, 'MyApp', '0001_initial', '2025-12-23 09:33:00.685128'),
(16, 'GuestApp', '0001_initial', '2025-12-23 09:33:01.509436'),
(17, 'admin', '0001_initial', '2025-12-23 09:33:01.746918'),
(18, 'admin', '0002_logentry_remove_auto_add', '2025-12-23 09:33:01.762865'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2025-12-23 09:33:01.774989'),
(20, 'sessions', '0001_initial', '2025-12-23 09:33:01.814059'),
(21, 'MyApp', '0002_tbl_route_tbl_collectorassignment', '2025-12-23 09:48:10.851170'),
(22, 'GuestApp', '0002_household_house_no', '2025-12-23 09:55:01.586833'),
(23, 'MyApp', '0003_tbl_route_end_house_no_and_more', '2025-12-23 09:55:01.713535'),
(24, 'MyApp', '0004_tbl_collectionrequest_tbl_pickuprequest', '2025-12-23 10:12:18.798038'),
(25, 'MyApp', '0005_tbl_bintype_tbl_pickuprequest_actual_weight_kg_and_more', '2025-12-23 14:51:22.084268'),
(26, 'MyApp', '0006_tbl_pickuprequest_payment_amount_and_more', '2025-12-23 15:37:41.708457');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6cuoe2owfvb49dzwqi1bzv0db0gnsesg', '.eJxVjEEOwiAQRe_C2pDSAgMu3fcMZAamUjWQlHZlvLtt0oVu_3vvv0XAbc1ha7yEOYmrUOLyuxHGJ5cDpAeWe5WxlnWZSR6KPGmTY038up3u30HGlvfaMlCcjGdCtFFb57vBAjmAaLBHpuQZrfXdLnoDblKge5eYlSOjBxCfL_q4N_8:1vY3WW:aOqeZlGY3pLisPRsn-NHlPidLmntVXIvHAo6jZk5blg', '2026-01-06 14:38:04.881063'),
('4hbbnqzqcnlks0rayfyxr0iyfffba003', '.eJxVjDEOwyAUQ-_CXCEgfAgdu-cM6AOfkrYiUkimqncvkTK0ky0_22_mcd-K3xutfk7sygZ2-c0CxifVA6QH1vvC41K3dQ78qPCTNj4tiV63s_t3ULCVvhYSwqhJRcwQrSRhRwRpgKx2lBxC14zRyRhQKyOMhO5BDw41qizZ5wvbNTdy:1vY3Vw:lR6ojEGUuOHYWW1xHbhtrOsy4RWD1HcuTd6Zla6zD5s', '2026-01-06 14:37:28.300141');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_collector`
--

DROP TABLE IF EXISTS `guestapp_collector`;
CREATE TABLE IF NOT EXISTS `guestapp_collector` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `collector_name` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `license_image` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_collector`
--

INSERT INTO `guestapp_collector` (`id`, `collector_name`, `phone`, `address`, `license_image`, `is_active`, `user_id`) VALUES
(1, 'Jibin Jino', '9685748574', 'Chunkom', 'collector_licenses/license2_KfBOsj3.jpg', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_compostmanager`
--

DROP TABLE IF EXISTS `guestapp_compostmanager`;
CREATE TABLE IF NOT EXISTS `guestapp_compostmanager` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `compostmanager_name` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `license_number` varchar(100) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `license_number` (`license_number`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_compostmanager`
--

INSERT INTO `guestapp_compostmanager` (`id`, `compostmanager_name`, `phone`, `address`, `license_number`, `is_active`, `user_id`) VALUES
(1, 'Rohit P Rajeev', '7548757412', 'Kanjiramatoom,\r\nThodupuhza', '6565542154', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_customuser`
--

DROP TABLE IF EXISTS `guestapp_customuser`;
CREATE TABLE IF NOT EXISTS `guestapp_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(191) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `role` varchar(20) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_customuser`
--

INSERT INTO `guestapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `name`, `email`, `phone`, `role`, `is_verified`, `is_active`, `is_staff`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1200000$A72hyEnyPRmDy4Nz0XFSsQ$ythB27voBa5erUEtlUzDS1Vkb9DgWDnbZL9zt4AUoA4=', '2025-12-23 16:27:53.351024', 1, 'admin', 'admin@gmail.com', NULL, 'admin', 0, 1, 1, '2025-12-23 09:34:49.101631'),
(2, 'pbkdf2_sha256$1200000$2wC94R4QjwPKyedhI2uPHD$SikQV7Dug0/WF3qY+TvdmVu9yGd+PK168dWgV8egK88=', '2025-12-23 14:36:58.891223', 0, 'Sonit Jolly', 'sonit@gmail.com', '9447512454', 'household', 1, 1, 0, '2025-12-23 09:36:49.630503'),
(3, 'pbkdf2_sha256$1200000$7Y8Pp0EWeEZoHuBsfjvrHh$bGwkT/6SJSmhbF3WSlzvTFbJamRHkophyw5paCmdDzg=', '2025-12-23 14:37:28.298663', 0, 'Jibin Jino', 'jibin@gmail.com', '9685748574', 'collector', 1, 1, 0, '2025-12-23 09:37:33.449651'),
(4, 'pbkdf2_sha256$1200000$B85Cr7bFLbNc59jWZQIq3Y$TNzcshBNlMfjiQ5gcijIMKGEHWhjjaE7BTL7+dRZXHI=', NULL, 0, 'Rohit P Rajeev', 'rohit@gmail.com', '7548757412', 'compost_manager', 1, 1, 0, '2025-12-23 09:38:23.782225'),
(5, 'pbkdf2_sha256$1200000$SZpxM8tnysTZHTWgCaog9r$E2vb3m09Qccdw2cxHiGh1qql4kc6mk7LwuoyNtpEiAM=', '2025-12-23 09:39:34.782301', 0, 'Jolly Varkey', 'jolly@gmail.com', '9447613494', 'farmer', 1, 1, 0, '2025-12-23 09:38:54.169177');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_customuser_groups`
--

DROP TABLE IF EXISTS `guestapp_customuser_groups`;
CREATE TABLE IF NOT EXISTS `guestapp_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `GuestApp_customuser_groups_customuser_id_group_id_b8e157fc_uniq` (`customuser_id`,`group_id`),
  KEY `GuestApp_customuser_groups_customuser_id_c70dc858` (`customuser_id`),
  KEY `GuestApp_customuser_groups_group_id_8330f831` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_customuser_user_permissions`
--

DROP TABLE IF EXISTS `guestapp_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `guestapp_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `GuestApp_customuser_user_customuser_id_permission_b6ac8a60_uniq` (`customuser_id`,`permission_id`),
  KEY `GuestApp_customuser_user_permissions_customuser_id_819ef22e` (`customuser_id`),
  KEY `GuestApp_customuser_user_permissions_permission_id_37b6a88f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_farmer`
--

DROP TABLE IF EXISTS `guestapp_farmer`;
CREATE TABLE IF NOT EXISTS `guestapp_farmer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `farmer_name` varchar(100) NOT NULL,
  `aadhaar_image` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_farmer`
--

INSERT INTO `guestapp_farmer` (`id`, `farmer_name`, `aadhaar_image`, `phone`, `address`, `is_active`, `user_id`) VALUES
(1, 'Jolly Varkey', 'farmer_aadhaar_images/john.png', '9447613494', 'Anachalil(H), Mariyilkalunku,\r\nAVJ FARM\r\nthodupuzha', 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_household`
--

DROP TABLE IF EXISTS `guestapp_household`;
CREATE TABLE IF NOT EXISTS `guestapp_household` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `household_name` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `aadhaar_image` varchar(100) NOT NULL,
  `registered_on` datetime(6) NOT NULL,
  `district_id` int NOT NULL,
  `location_id` int NOT NULL,
  `residents_association_id` int NOT NULL,
  `user_id` bigint NOT NULL,
  `house_no` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `GuestApp_household_district_id_32bdd425` (`district_id`),
  KEY `GuestApp_household_location_id_9a310686` (`location_id`),
  KEY `GuestApp_household_residents_association_id_1d8b3b00` (`residents_association_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_household`
--

INSERT INTO `guestapp_household` (`id`, `household_name`, `phone`, `address`, `aadhaar_image`, `registered_on`, `district_id`, `location_id`, `residents_association_id`, `user_id`, `house_no`) VALUES
(1, 'Sonit Jolly', '9447512454', 'Anachalil(H), Mariyilkalunku,\r\nAVJ FARM\r\nthodupuzha', 'household_aadhaar_images/license2.jpg', '2025-12-23 09:36:49.630870', 1, 1, 1, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_bintype`
--

DROP TABLE IF EXISTS `myapp_tbl_bintype`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_bintype` (
  `BinType_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `capacity_kg` int NOT NULL,
  `price_rs` decimal(10,2) NOT NULL,
  PRIMARY KEY (`BinType_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_bintype`
--

INSERT INTO `myapp_tbl_bintype` (`BinType_id`, `name`, `capacity_kg`, `price_rs`) VALUES
(1, 'Medium', 25, 50.00),
(2, 'Large', 50, 100.00);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_collectionrequest`
--

DROP TABLE IF EXISTS `myapp_tbl_collectionrequest`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_collectionrequest` (
  `Request_id` int NOT NULL AUTO_INCREMENT,
  `total_quantity_kg` decimal(10,2) NOT NULL,
  `farmer_supply_kg` decimal(10,2) NOT NULL,
  `leftover_compost_kg` decimal(10,2) NOT NULL,
  `collection_date` datetime(6) NOT NULL,
  `status` varchar(50) NOT NULL,
  `collector_id` bigint NOT NULL,
  `household_id` bigint NOT NULL,
  PRIMARY KEY (`Request_id`),
  KEY `MyApp_tbl_collectionrequest_collector_id_88ddd704` (`collector_id`),
  KEY `MyApp_tbl_collectionrequest_household_id_5b80e140` (`household_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_collectionrequest`
--

INSERT INTO `myapp_tbl_collectionrequest` (`Request_id`, `total_quantity_kg`, `farmer_supply_kg`, `leftover_compost_kg`, `collection_date`, `status`, `collector_id`, `household_id`) VALUES
(1, 25.00, 0.00, 0.00, '2025-12-23 10:27:56.964702', 'Completed', 1, 1),
(2, 23.00, 0.00, 0.00, '2025-12-23 15:12:15.734350', 'Completed', 1, 1),
(3, 25.00, 0.00, 0.00, '2025-12-23 15:12:21.983313', 'Completed', 1, 1),
(4, 25.00, 0.00, 0.00, '2025-12-23 15:52:57.306943', 'Completed', 1, 1),
(5, 25.00, 0.00, 0.00, '2025-12-23 15:53:02.152036', 'Completed', 1, 1),
(6, 25.00, 0.00, 0.00, '2025-12-23 16:03:36.746796', 'Completed', 1, 1),
(7, 22.00, 0.00, 0.00, '2025-12-23 16:04:46.089894', 'Completed', 1, 1),
(8, 25.00, 0.00, 0.00, '2025-12-23 16:10:44.410132', 'Completed', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_collectorassignment`
--

DROP TABLE IF EXISTS `myapp_tbl_collectorassignment`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_collectorassignment` (
  `Assign_id` int NOT NULL AUTO_INCREMENT,
  `day_of_week` varchar(50) NOT NULL,
  `collector_id` bigint NOT NULL,
  `Route_id_id` int NOT NULL,
  PRIMARY KEY (`Assign_id`),
  KEY `MyApp_tbl_collectorassignment_collector_id_2a489362` (`collector_id`),
  KEY `MyApp_tbl_collectorassignment_Route_id_id_8bdc554a` (`Route_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_collectorassignment`
--

INSERT INTO `myapp_tbl_collectorassignment` (`Assign_id`, `day_of_week`, `collector_id`, `Route_id_id`) VALUES
(1, 'Monday', 1, 1),
(2, 'Tuesday', 1, 1),
(3, 'Wednesday', 1, 1),
(4, 'Thursday', 1, 1),
(5, 'Thursday', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_district`
--

DROP TABLE IF EXISTS `myapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_district` (
  `District_id` int NOT NULL AUTO_INCREMENT,
  `District_Name` varchar(100) NOT NULL,
  PRIMARY KEY (`District_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_district`
--

INSERT INTO `myapp_tbl_district` (`District_id`, `District_Name`) VALUES
(1, 'Idukki');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_householdpayment`
--

DROP TABLE IF EXISTS `myapp_tbl_householdpayment`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_householdpayment` (
  `Payment_id` int NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `payment_date` datetime(6) NOT NULL,
  `payment_for_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `bin_type_id` int NOT NULL,
  `household_id` bigint NOT NULL,
  PRIMARY KEY (`Payment_id`),
  KEY `MyApp_tbl_householdpayment_bin_type_id_3cafb6d7` (`bin_type_id`),
  KEY `MyApp_tbl_householdpayment_household_id_b64e5a6c` (`household_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_householdpayment`
--

INSERT INTO `myapp_tbl_householdpayment` (`Payment_id`, `amount`, `payment_date`, `payment_for_date`, `status`, `transaction_id`, `bin_type_id`, `household_id`) VALUES
(13, 100.00, '2025-12-23 16:10:27.825950', '2025-12-31', 'Completed', 'TXN1766506227600', 2, 1),
(12, 50.00, '2025-12-23 16:04:11.328070', '2025-12-24', 'Completed', 'TXN1766505851952', 1, 1),
(11, 100.00, '2025-12-23 16:02:43.170513', '2025-12-23', 'Completed', 'TXN1766505763679', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_location`
--

DROP TABLE IF EXISTS `myapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_location` (
  `Location_id` int NOT NULL AUTO_INCREMENT,
  `Ward_No` int NOT NULL,
  `Ward_Name` varchar(100) NOT NULL,
  `District_id` int NOT NULL,
  PRIMARY KEY (`Location_id`),
  KEY `MyApp_tbl_location_District_id_aeef7669` (`District_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_location`
--

INSERT INTO `myapp_tbl_location` (`Location_id`, `Ward_No`, `Ward_Name`, `District_id`) VALUES
(1, 26, 'Arackkapara', 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_pickuprequest`
--

DROP TABLE IF EXISTS `myapp_tbl_pickuprequest`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_pickuprequest` (
  `Pickup_id` int NOT NULL AUTO_INCREMENT,
  `scheduled_date` date NOT NULL,
  `request_time` time(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `assigned_collector_id` bigint DEFAULT NULL,
  `household_id` bigint NOT NULL,
  `actual_weight_kg` decimal(10,2) DEFAULT NULL,
  `bin_type_id` int DEFAULT NULL,
  `payment_id` int DEFAULT NULL,
  `payment_amount` decimal(10,2) DEFAULT NULL,
  `payment_date` datetime(6) DEFAULT NULL,
  `payment_method` varchar(20) DEFAULT NULL,
  `payment_status` varchar(20) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Pickup_id`),
  KEY `MyApp_tbl_pickuprequest_assigned_collector_id_7c3bfac0` (`assigned_collector_id`),
  KEY `MyApp_tbl_pickuprequest_household_id_071f0928` (`household_id`),
  KEY `MyApp_tbl_pickuprequest_bin_type_id_94b84ff5` (`bin_type_id`),
  KEY `MyApp_tbl_pickuprequest_payment_id_74a31eed` (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_pickuprequest`
--

INSERT INTO `myapp_tbl_pickuprequest` (`Pickup_id`, `scheduled_date`, `request_time`, `status`, `assigned_collector_id`, `household_id`, `actual_weight_kg`, `bin_type_id`, `payment_id`, `payment_amount`, `payment_date`, `payment_method`, `payment_status`, `transaction_id`) VALUES
(17, '2025-12-31', '22:12:00.000000', 'Completed', 1, 1, 25.00, 2, 13, 100.00, '2025-12-23 16:10:27.826866', 'UPI', 'Completed', 'TXN1766506227600'),
(16, '2025-12-24', '00:00:00.000000', 'Completed', 1, 1, 22.00, 1, 12, 50.00, '2025-12-23 16:04:11.329422', 'COD', 'Completed', 'TXN1766505851952'),
(15, '2025-12-23', '23:01:00.000000', 'Completed', 1, 1, 25.00, 2, 11, 100.00, '2025-12-23 16:02:43.172711', 'COD', 'Completed', 'TXN1766505763679');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_residentsassociation`
--

DROP TABLE IF EXISTS `myapp_tbl_residentsassociation`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_residentsassociation` (
  `RA_id` int NOT NULL AUTO_INCREMENT,
  `Association_Name` varchar(200) NOT NULL,
  `Location_id` int NOT NULL,
  PRIMARY KEY (`RA_id`),
  KEY `MyApp_tbl_residentsassociation_Location_id_d683a09a` (`Location_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_residentsassociation`
--

INSERT INTO `myapp_tbl_residentsassociation` (`RA_id`, `Association_Name`, `Location_id`) VALUES
(1, 'Chaithanya Nagar', 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_route`
--

DROP TABLE IF EXISTS `myapp_tbl_route`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_route` (
  `Route_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `location_id` int NOT NULL,
  `end_house_no` int DEFAULT NULL,
  `residents_association_id` int DEFAULT NULL,
  `start_house_no` int DEFAULT NULL,
  PRIMARY KEY (`Route_id`),
  UNIQUE KEY `name` (`name`),
  KEY `MyApp_tbl_route_location_id_2c6c2a9b` (`location_id`),
  KEY `MyApp_tbl_route_residents_association_id_278d4697` (`residents_association_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_route`
--

INSERT INTO `myapp_tbl_route` (`Route_id`, `name`, `location_id`, `end_house_no`, `residents_association_id`, `start_house_no`) VALUES
(1, 'A', 1, 3, 1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
