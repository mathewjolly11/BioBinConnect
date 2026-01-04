-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 04, 2026 at 05:03 PM
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
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=MyISAM AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add tbl_ bin type', 6, 'add_tbl_bintype'),
(22, 'Can change tbl_ bin type', 6, 'change_tbl_bintype'),
(23, 'Can delete tbl_ bin type', 6, 'delete_tbl_bintype'),
(24, 'Can view tbl_ bin type', 6, 'view_tbl_bintype'),
(25, 'Can add tbl_ district', 7, 'add_tbl_district'),
(26, 'Can change tbl_ district', 7, 'change_tbl_district'),
(27, 'Can delete tbl_ district', 7, 'delete_tbl_district'),
(28, 'Can view tbl_ district', 7, 'view_tbl_district'),
(29, 'Can add tbl_ collection request', 8, 'add_tbl_collectionrequest'),
(30, 'Can change tbl_ collection request', 8, 'change_tbl_collectionrequest'),
(31, 'Can delete tbl_ collection request', 8, 'delete_tbl_collectionrequest'),
(32, 'Can view tbl_ collection request', 8, 'view_tbl_collectionrequest'),
(33, 'Can add tbl_ compost batch', 9, 'add_tbl_compostbatch'),
(34, 'Can change tbl_ compost batch', 9, 'change_tbl_compostbatch'),
(35, 'Can delete tbl_ compost batch', 9, 'delete_tbl_compostbatch'),
(36, 'Can view tbl_ compost batch', 9, 'view_tbl_compostbatch'),
(37, 'Can add tbl_ farmer supply', 10, 'add_tbl_farmersupply'),
(38, 'Can change tbl_ farmer supply', 10, 'change_tbl_farmersupply'),
(39, 'Can delete tbl_ farmer supply', 10, 'delete_tbl_farmersupply'),
(40, 'Can view tbl_ farmer supply', 10, 'view_tbl_farmersupply'),
(41, 'Can add tbl_ household payment', 11, 'add_tbl_householdpayment'),
(42, 'Can change tbl_ household payment', 11, 'change_tbl_householdpayment'),
(43, 'Can delete tbl_ household payment', 11, 'delete_tbl_householdpayment'),
(44, 'Can view tbl_ household payment', 11, 'view_tbl_householdpayment'),
(45, 'Can add tbl_location', 12, 'add_tbl_location'),
(46, 'Can change tbl_location', 12, 'change_tbl_location'),
(47, 'Can delete tbl_location', 12, 'delete_tbl_location'),
(48, 'Can view tbl_location', 12, 'view_tbl_location'),
(49, 'Can add tbl_ order', 13, 'add_tbl_order'),
(50, 'Can change tbl_ order', 13, 'change_tbl_order'),
(51, 'Can delete tbl_ order', 13, 'delete_tbl_order'),
(52, 'Can view tbl_ order', 13, 'view_tbl_order'),
(53, 'Can add tbl_ order item', 14, 'add_tbl_orderitem'),
(54, 'Can change tbl_ order item', 14, 'change_tbl_orderitem'),
(55, 'Can delete tbl_ order item', 14, 'delete_tbl_orderitem'),
(56, 'Can view tbl_ order item', 14, 'view_tbl_orderitem'),
(57, 'Can add tbl_ payment transaction', 15, 'add_tbl_paymenttransaction'),
(58, 'Can change tbl_ payment transaction', 15, 'change_tbl_paymenttransaction'),
(59, 'Can delete tbl_ payment transaction', 15, 'delete_tbl_paymenttransaction'),
(60, 'Can view tbl_ payment transaction', 15, 'view_tbl_paymenttransaction'),
(61, 'Can add tbl_ pickup request', 16, 'add_tbl_pickuprequest'),
(62, 'Can change tbl_ pickup request', 16, 'change_tbl_pickuprequest'),
(63, 'Can delete tbl_ pickup request', 16, 'delete_tbl_pickuprequest'),
(64, 'Can view tbl_ pickup request', 16, 'view_tbl_pickuprequest'),
(65, 'Can add tbl_residentsassociation', 17, 'add_tbl_residentsassociation'),
(66, 'Can change tbl_residentsassociation', 17, 'change_tbl_residentsassociation'),
(67, 'Can delete tbl_residentsassociation', 17, 'delete_tbl_residentsassociation'),
(68, 'Can view tbl_residentsassociation', 17, 'view_tbl_residentsassociation'),
(69, 'Can add tbl_ route', 18, 'add_tbl_route'),
(70, 'Can change tbl_ route', 18, 'change_tbl_route'),
(71, 'Can delete tbl_ route', 18, 'delete_tbl_route'),
(72, 'Can view tbl_ route', 18, 'view_tbl_route'),
(73, 'Can add tbl_ collector assignment', 19, 'add_tbl_collectorassignment'),
(74, 'Can change tbl_ collector assignment', 19, 'change_tbl_collectorassignment'),
(75, 'Can delete tbl_ collector assignment', 19, 'delete_tbl_collectorassignment'),
(76, 'Can view tbl_ collector assignment', 19, 'view_tbl_collectorassignment'),
(77, 'Can add tbl_ waste inventory', 20, 'add_tbl_wasteinventory'),
(78, 'Can change tbl_ waste inventory', 20, 'change_tbl_wasteinventory'),
(79, 'Can delete tbl_ waste inventory', 20, 'delete_tbl_wasteinventory'),
(80, 'Can view tbl_ waste inventory', 20, 'view_tbl_wasteinventory'),
(81, 'Can add collector', 21, 'add_collector'),
(82, 'Can change collector', 21, 'change_collector'),
(83, 'Can delete collector', 21, 'delete_collector'),
(84, 'Can view collector', 21, 'view_collector'),
(85, 'Can add compost manager', 22, 'add_compostmanager'),
(86, 'Can change compost manager', 22, 'change_compostmanager'),
(87, 'Can delete compost manager', 22, 'delete_compostmanager'),
(88, 'Can view compost manager', 22, 'view_compostmanager'),
(89, 'Can add farmer', 23, 'add_farmer'),
(90, 'Can change farmer', 23, 'change_farmer'),
(91, 'Can delete farmer', 23, 'delete_farmer'),
(92, 'Can view farmer', 23, 'view_farmer'),
(93, 'Can add household', 24, 'add_household'),
(94, 'Can change household', 24, 'change_household'),
(95, 'Can delete household', 24, 'delete_household'),
(96, 'Can view household', 24, 'view_household'),
(97, 'Can add custom user', 25, 'add_customuser'),
(98, 'Can change custom user', 25, 'change_customuser'),
(99, 'Can delete custom user', 25, 'delete_customuser'),
(100, 'Can view custom user', 25, 'view_customuser'),
(101, 'Can add System Setting', 26, 'add_systemsettings'),
(102, 'Can change System Setting', 26, 'change_systemsettings'),
(103, 'Can delete System Setting', 26, 'delete_systemsettings'),
(104, 'Can view System Setting', 26, 'view_systemsettings');

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
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'MyApp', 'tbl_bintype'),
(7, 'MyApp', 'tbl_district'),
(8, 'MyApp', 'tbl_collectionrequest'),
(9, 'MyApp', 'tbl_compostbatch'),
(10, 'MyApp', 'tbl_farmersupply'),
(11, 'MyApp', 'tbl_householdpayment'),
(12, 'MyApp', 'tbl_location'),
(13, 'MyApp', 'tbl_order'),
(14, 'MyApp', 'tbl_orderitem'),
(15, 'MyApp', 'tbl_paymenttransaction'),
(16, 'MyApp', 'tbl_pickuprequest'),
(17, 'MyApp', 'tbl_residentsassociation'),
(18, 'MyApp', 'tbl_route'),
(19, 'MyApp', 'tbl_collectorassignment'),
(20, 'MyApp', 'tbl_wasteinventory'),
(21, 'GuestApp', 'collector'),
(22, 'GuestApp', 'compostmanager'),
(23, 'GuestApp', 'farmer'),
(24, 'GuestApp', 'household'),
(25, 'GuestApp', 'customuser'),
(26, 'MyApp', 'systemsettings');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-12-28 04:45:39.078443'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-12-28 04:45:39.198768'),
(3, 'auth', '0001_initial', '2025-12-28 04:45:39.544674'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-12-28 04:45:39.598522'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-12-28 04:45:39.607078'),
(6, 'auth', '0004_alter_user_username_opts', '2025-12-28 04:45:39.613723'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-12-28 04:45:39.618244'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-12-28 04:45:39.619347'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-12-28 04:45:39.628246'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-12-28 04:45:39.633584'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-12-28 04:45:39.640899'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-12-28 04:45:39.698977'),
(13, 'auth', '0011_update_proxy_permissions', '2025-12-28 04:45:39.705302'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-12-28 04:45:39.709654'),
(15, 'GuestApp', '0001_initial', '2025-12-28 04:45:39.762187'),
(16, 'MyApp', '0001_initial', '2025-12-28 04:45:41.813199'),
(17, 'GuestApp', '0002_initial', '2025-12-28 04:45:42.702440'),
(18, 'admin', '0001_initial', '2025-12-28 04:45:43.006807'),
(19, 'admin', '0002_logentry_remove_auto_add', '2025-12-28 04:45:43.023948'),
(20, 'admin', '0003_logentry_add_action_flag_choices', '2025-12-28 04:45:43.038007'),
(21, 'sessions', '0001_initial', '2025-12-28 04:45:43.075376'),
(22, 'MyApp', '0002_alter_tbl_collectorassignment_options_and_more', '2025-12-31 15:31:23.675764'),
(23, 'MyApp', '0003_tbl_wasteinventory_salary_paid', '2025-12-31 16:21:56.839942'),
(24, 'MyApp', '0004_tbl_compostbatch_salary_paid', '2025-12-31 16:22:19.702670'),
(25, 'MyApp', '0005_systemsettings', '2026-01-04 11:50:24.359107'),
(26, 'GuestApp', '0003_customuser_account_status', '2026-01-04 13:50:55.859071');

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
('d1wynvduwyvykgijaesv264ue9o4c1xb', '.eJxVjDsOwjAQBe_iGlm2N_4sJT1niLzZNQ6gRIqTCnF3iJQC2jcz76X6vK2135os_cjqrKw6_W6Uh4dMO-B7nm6zHuZpXUbSu6IP2vR1ZnleDvfvoOZWv3WxBiGCJ-pM4Ig-dSYGFudQiG0ZEgckhFSCCYAMCB5QioteXEdWvT_CxTcE:1vcMHh:BAMz8bSoRyGwvEtnrwHGkS0158S4KuclBZwB-uXZHrI', '2026-01-18 11:28:33.150082'),
('vpili4uro6r04ht7pv76y839ufo9g9gi', '.eJxVjDsOwjAQBe_iGlm2N_4sJT1niLzZNQ6gRIqTCnF3iJQC2jcz76X6vK2135os_cjqrKw6_W6Uh4dMO-B7nm6zHuZpXUbSu6IP2vR1ZnleDvfvoOZWv3WxBiGCJ-pM4Ig-dSYGFudQiG0ZEgckhFSCCYAMCB5QioteXEdWvT_CxTcE:1vb8rK:ZQ3QK7KvnGZniJHt5mjnDbq4V2NNLTBNMJ5amLrv6nM', '2026-01-15 02:56:18.079237'),
('qsjqrga8wygwcn6x8ssh98bnz43fuo9b', '.eJxVjMsOwiAQRf-FtSFQeUxduvcbCMwMUjWQlHZl_HfbpAvd3nPueYsQ16WEtfMcJhIXMYjT75YiPrnugB6x3pvEVpd5SnJX5EG7vDXi1_Vw_wIl9rK9EYz3djTxjNmwwUzgAFAr0l45cH5ITHpEdBoMgkp2a7PVidConEl8vuGwOG0:1vcOju:WMEEXBiOdLZFSfvNJChSIjvoHBdh-tyBN3qxFnjr0n0', '2026-01-18 14:05:50.671237'),
('duafwdgn555lq0kpp26fauvhx36am1ut', '.eJxVjEEOwiAQRe_C2hBIYQCX7j0DYRhGqqYkpV013t026UK3_733NxHTutS49jLHkcRVaC0uvyOm_CrTQeiZpkeTuU3LPKI8FHnSLu-Nyvt2un8HNfW610zWeCZQAzivXQpEKgxIMGR0YDwwAypgBcEVcNYg2kImazY7IhafLwc0OIs:1varwf:lyEGrn4p3_b00lXiMzQr_O2Ckz_7qfESPFipHAArdnE', '2026-01-14 08:52:41.189442'),
('8e2rmu2vloqn6poyap5kdsz6z4tn2xl2', '.eJxVjDsOwjAQBe_iGllef1ibkj5nsNbrDQmgRIqTCnF3iJQC2jcz76UybeuQtyZLHqu6KAjq9DsW4odMO6l3mm6z5nlal7HoXdEHbbqbqzyvh_t3MFAbvjVjQSMIQi5yIPHeRyfV-TMYtpCklx4jYCzOVgSuydjAkHprMLho1PsDB843eQ:1vayQ3:7pqtfA6agGiJ_wraIuJohezrFLuC3rkR-g8pQwroVBM', '2026-01-14 15:47:27.485702'),
('brrg44i94hp1q6w7dt4xa89b8bd7rnhe', '.eJxVjDsOwjAQBe_iGll2vP5R0nMGa9cfHEC2FCcV4u4QKQW0b2beiwXc1hq2kZcwJ3Zmk2Gn35EwPnLbSbpju3Uee1uXmfiu8IMOfu0pPy-H-3dQcdRv7SA5aVMsXvkcLYJwQGoirbTRpkTwPjmTQUhbjCteKIWy-EgCyWUC9v4A_MQ39A:1vayUF:HpdpVpxMrR--RCnWveKAmtzQUj4mYqcCuZeL9nq-UGg', '2026-01-14 15:51:47.168645'),
('qtzjewrpvx1l5lcoa6s17faha7vi6wnp', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNZIaHVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZKctOvyNhfOS2k3THdus89rYuM_Fd4Qcd_NpTfl4O9--g4qjfmpRzfhIwWRF9RO2icZo0KC-VJYeTLUVkMEQWrDKmJEDwWaH0CEIm9v4A5L83Vg:1vcML0:UY237ukFqdnpa2U3AkBfkIVyCMAr8SjHXKvCOAmw5Ms', '2026-01-18 11:31:58.058481'),
('yvnnmazhfack7tpi49pv3q85yb6niudh', '.eJxVjDsOwjAQBe_iGllef1ibkj5nsNbrDQmgRIqTCnF3iJQC2jcz76UybeuQtyZLHqu6KAjq9DsW4odMO6l3mm6z5nlal7HoXdEHbbqbqzyvh_t3MFAbvjVjQSMIQi5yIPHeRyfV-TMYtpCklx4jYCzOVgSuydjAkHprMLho1PsDB843eQ:1vcOoC:jxgXokVcFvoi_VpsoBPI1lqRLrR1jETpzvy0G3r0ccU', '2026-01-18 14:10:16.434486');

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
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_collector`
--

INSERT INTO `guestapp_collector` (`id`, `collector_name`, `phone`, `address`, `license_image`, `is_active`, `user_id`) VALUES
(1, 'Ashin Aji', '9788578554', 'Thodupuzha', 'collector_licenses/license2_a5cpAe3.jpg', 1, 15),
(2, 'Nikhil Biby', '9685745125', 'Vazhakulam,\r\nThodupuzha', 'collector_licenses/john.png', 1, 16),
(3, 'Nikitha Biby', '8585745968', 'Thodupuzha', 'collector_licenses/license2_jJMwJyj.jpg', 1, 17),
(4, 'Jobin Jose', '9685748574', 'Thodupuzha', 'collector_licenses/mary.png', 1, 18),
(5, 'Aashish Shoby', '9685857487', 'Thodupuzha', 'collector_licenses/mary_Max62cS.png', 1, 19),
(6, 'Jacob Suni', '9685214152', 'Thodupuzha', 'collector_licenses/license1.jpg', 1, 20);

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_compostmanager`
--

INSERT INTO `guestapp_compostmanager` (`id`, `compostmanager_name`, `phone`, `address`, `license_number`, `is_active`, `user_id`) VALUES
(1, 'Soorya Sunil', '9685441412', 'tdpa', '4141414', 1, 26),
(2, 'Gibin Jose', '9685748596', 'TDPA', '3516456', 1, 27);

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
  `account_status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_customuser`
--

INSERT INTO `guestapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `name`, `email`, `phone`, `role`, `is_verified`, `is_active`, `is_staff`, `date_joined`, `account_status`) VALUES
(1, 'pbkdf2_sha256$1200000$iTguQbPLmZdihCa4mWAhVJ$7VvTuJNupgHcP8ax+wAv7rE4LQgbDETrOcujnABPPpM=', '2026-01-04 11:28:33.128995', 1, 'Admin', 'admin@gmail.com', NULL, 'admin', 0, 1, 1, '2025-12-28 04:46:53.683344', 'Pending'),
(2, 'pbkdf2_sha256$1200000$jTuDyFpVQWXY7H3BWgGeQ4$4hBA75wMCiCjATreKqLYSkfreC4jbwXMNRdx1pxg7sQ=', '2026-01-04 14:05:50.664442', 0, 'Sonit Jolly', 'sonitjollyavj@gmail.com', '9447984821', 'household', 1, 1, 0, '2025-12-28 04:52:33.900886', 'Approved'),
(3, 'pbkdf2_sha256$1200000$cyBNoWmqzEgS2NmbORHpxj$CkAjlfQBRgei2aLzY8ZtzhpfrscAD7SrOxt0MoJd1kE=', '2026-01-01 03:04:53.109414', 0, 'Maria Jolly', 'maria@gmail.com', '9447568542', 'household', 1, 1, 0, '2025-12-28 04:56:23.335834', 'Approved'),
(4, 'pbkdf2_sha256$1200000$52ZW9S67Loy9HJegn08O4T$Y8k37DK1RT0C4px6HcoR5NshUIHF3QBmaxQwt27c+ow=', '2026-01-01 03:52:52.090519', 0, 'Henna Maria Jiju', 'henna@gmail.com', '9685457512', 'household', 1, 1, 0, '2025-12-28 04:57:20.780667', 'Approved'),
(5, 'pbkdf2_sha256$1200000$pO9U4QG5BYrG28f0TELuh2$dARswldPoPTFrQv0r7dxTAiI7VHnbCMIH4g8ZznxWM0=', '2026-01-01 04:00:35.679322', 0, 'Joseph Sojan', 'joseph@gmail.com', '9685214152', 'household', 1, 1, 0, '2025-12-28 04:58:25.870305', 'Approved'),
(6, 'pbkdf2_sha256$1200000$aKbWAvxH5BTMMmtPRPDkZk$UYIT7J9Fukzyr55nl7gdw3cf8BFp66eJQH6F0CpD7Ms=', '2025-12-31 08:44:35.034230', 0, 'Nebin Reji', 'nebin@gmail.com', '9652634512', 'household', 1, 1, 0, '2025-12-29 02:29:02.978122', 'Approved'),
(7, 'pbkdf2_sha256$1200000$VWeZ0tRd6Pycg1BmqaUzPG$zbEWCaQ4B5LQ9NTKc0JiLSfyDlxIXjdJ2AyIFkd3E2w=', '2025-12-31 08:45:53.080487', 0, 'Rohit P Rajeev', 'rohit@gmail.com', '8574859615', 'household', 1, 1, 0, '2025-12-29 02:32:33.245530', 'Approved'),
(8, 'pbkdf2_sha256$1200000$RgbbTHhKQn8Gyu4nZCPeWt$iGc/bAVyY+gPBJZ2W4pG4lz7BNDkcGHYvcKLkspq+Nk=', '2025-12-31 08:47:21.528198', 0, 'Joju Sibi', 'joju@gmail.com', '8574561252', 'household', 1, 1, 0, '2025-12-29 02:50:31.353746', 'Approved'),
(9, 'pbkdf2_sha256$1200000$FFY0jPVNMkyvBxP6WJTrUr$CR6CdQOu8SB2ihXcYMK1swlvp1/4DaEwlleU5XNlBhg=', '2026-01-02 09:40:51.429117', 0, 'Jishin Aji', 'jishin@gmail.com', '8574859615', 'household', 1, 1, 0, '2025-12-29 04:25:24.378394', 'Approved'),
(10, 'pbkdf2_sha256$1200000$irFbQyHOQKQ5IC5SHjud77$t0r64/jPMM7BbzqOYrS0iBxjRBEMTww3vCOIsdS3M3Y=', '2025-12-31 08:50:28.941415', 0, 'Vishnu P G', 'vishnu@gmail.com', '7458965675', 'household', 1, 1, 0, '2025-12-29 05:56:50.660428', 'Approved'),
(11, 'pbkdf2_sha256$1200000$vVvdZHsyuN0xbL4JZIYNIi$ya+kCm69XzD20Xh1t1LKAagMXkF0n2bZUY+CWUwjGKo=', '2025-12-31 08:52:42.575091', 0, 'Abin Joy', 'abin@gmail.com', '9874124222', 'household', 1, 1, 0, '2025-12-29 05:58:27.463103', 'Approved'),
(12, 'pbkdf2_sha256$1200000$RwIWqD5nBwFNmr7ThBKdtO$kuxJVMxuhZc0TVyXwWEbpsNtMTyniBHvlslZXGOQOL8=', '2025-12-31 08:53:33.773575', 0, 'Sani Tomy', 'sani@gmail.com', '9685745125', 'household', 1, 1, 0, '2025-12-29 06:00:21.628529', 'Approved'),
(13, 'pbkdf2_sha256$1200000$x9O75WiSbNBS4qwFzatGBV$1kqx17ytHd46SbPVQcnf1c3KxQzkO3iRI2jiJDSg1ss=', '2025-12-31 08:54:40.651748', 0, 'Mejo John', 'mejo@gmail.com', '9685854156', 'household', 1, 1, 0, '2025-12-29 06:01:15.426499', 'Approved'),
(14, 'pbkdf2_sha256$1200000$ziy6u2PvbSdWR1EAFCHxvf$5EK6VUAcVpMLJojv8fosF5scNI0GvYBdpMORulO+Fec=', '2025-12-29 06:21:06.773740', 0, 'Antony Jose', 'antonyjose@gmail.com', '7451531312', 'household', 1, 1, 0, '2025-12-29 06:02:26.773984', 'Approved'),
(15, 'pbkdf2_sha256$1200000$ZAH1EZXctfiWuj2EFchuij$I8SKDvhq2OPWUoUgZs7UqHzAjaIR4C3Cx3CBtHzi83k=', '2026-01-04 14:10:16.431895', 0, 'Ashin Aji', 'ashin@gmail.com', '9788578554', 'collector', 1, 1, 0, '2025-12-29 06:51:16.104682', 'Approved'),
(16, 'pbkdf2_sha256$1200000$XW9zRKMNfk4LIM2s3iP0lf$Kf0vDAG9dzhkOBsw//1COederMQzWMldrd6rarBz+cA=', '2026-01-01 04:06:05.236713', 0, 'Nikhil Biby', 'nikhil@gmail.com', '9685745125', 'collector', 1, 1, 0, '2025-12-30 05:08:01.755887', 'Approved'),
(17, 'pbkdf2_sha256$1200000$wo39ZBbU9THqHQhmXoMEf2$mS6+squH3FnOZnWRQDTCRvmcXcnxbj6mAsq8THoxjmI=', '2025-12-31 09:12:44.136348', 0, 'Nikitha Biby', 'nikitha@gmail.com', '8585745968', 'collector', 1, 1, 0, '2025-12-30 05:09:26.180019', 'Approved'),
(18, 'pbkdf2_sha256$1200000$vds1biE44l3WWFFnX7cswf$C32geBxq9rS1OfgCo7H0vJ7nh7kLOuqw8saDIcn3eYA=', '2025-12-31 09:14:40.940296', 0, 'Jobin Jose', 'jobin@gmail.com', '9685748574', 'collector', 1, 1, 0, '2025-12-30 05:14:46.961708', 'Approved'),
(19, 'pbkdf2_sha256$1200000$MV2rG31fEo31s0u7bc2P0p$/IeCyZzwng014EhE/wQbv4dBGqPFvS3vz1vTIlcCeIA=', '2026-01-01 04:10:47.911012', 0, 'Aashish Shoby', 'aashish@gmail.com', '9685857487', 'collector', 1, 1, 0, '2025-12-30 05:16:21.609354', 'Approved'),
(20, 'pbkdf2_sha256$1200000$adWz5XyQDDMXqyZPPQQHrc$ZJn9WQZa/S3MOSKPDKJH2N32IjpLa+8/Pj6jpzipq8I=', '2026-01-02 09:53:02.258789', 0, 'Jacob Suni', 'jacob@gmail.com', '9685214152', 'collector', 1, 1, 0, '2025-12-30 05:46:35.774110', 'Approved'),
(21, 'pbkdf2_sha256$1200000$xei2mAGc4jk2D4naIQ62w7$/01iuGPmqgR5L4vqsQFIqjCJfnuoot/nfJ52Bp7kEG0=', '2025-12-31 15:41:17.246505', 0, 'Mathew Jolly', 'mathewjollyavj11@gmail.com', '9685748596', 'farmer', 1, 1, 0, '2025-12-31 09:23:42.161926', 'Approved'),
(22, 'pbkdf2_sha256$1200000$eYXrCyHacMlk1yEBn9aZSd$pcuOV+HxS7s5zFy4N3IsRrfMp2QDFe9xtvaomf+39Lg=', '2026-01-02 10:40:00.859018', 0, 'Edwin Jose', 'edwin@gmail.com', '9685748578', 'farmer', 1, 1, 0, '2025-12-31 09:26:54.401725', 'Approved'),
(23, 'pbkdf2_sha256$1200000$umOTEIm1d7jihPuy8ZlXLE$0BvkdQJjG0mBCGDEN5QFopo+8U6AD9IjLckGmHBcNoc=', '2025-12-31 15:57:27.161284', 0, 'Jeevan Johnson', 'jeevan@gmail.com', '9685748574', 'farmer', 1, 1, 0, '2025-12-31 09:30:38.615286', 'Approved'),
(25, 'pbkdf2_sha256$1200000$x9hOef6pdmGaoHlST8qOiB$KBZg0whI/U5/B+Y73SVp3iQJLm1zHdt/1gC1uNoJ97A=', '2026-01-01 04:21:21.621696', 0, 'Jees Johnson', 'mathewiqoocam1@gmail.com', '9685747474', 'farmer', 1, 1, 0, '2025-12-31 10:44:26.727897', 'Approved'),
(26, 'pbkdf2_sha256$1200000$1akSyrxEro3fuIVMQ1yJLq$eE5oVRnvF2DvmyajA/AWBPqryTT0GjyNUhk9Mk9/qB0=', '2026-01-01 04:11:59.255519', 0, 'Soorya Sunil', 'soorya@gmail.com', '9685441412', 'compost_manager', 1, 1, 0, '2025-12-31 15:50:45.033615', 'Approved'),
(27, 'pbkdf2_sha256$1200000$pLZh528jl0oAH0MFw71NvU$el7KZiqqSOKSATQ7rW7punOXiYnirpPGL8+e4EjMkfo=', '2026-01-04 11:31:58.056767', 0, 'Gibin Jose', 'gibin@gmail.com', '9685748596', 'compost_manager', 1, 1, 0, '2026-01-02 10:38:11.772618', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_customuser_groups`
--

DROP TABLE IF EXISTS `guestapp_customuser_groups`;
CREATE TABLE IF NOT EXISTS `guestapp_customuser_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_farmer`
--

INSERT INTO `guestapp_farmer` (`id`, `farmer_name`, `aadhaar_image`, `phone`, `address`, `is_active`, `user_id`) VALUES
(1, 'Mathew Jolly', 'farmer_aadhaar_images/license2.jpg', '9685748596', 'Thodupuzha', 1, 21),
(2, 'Edwin Jose', 'farmer_aadhaar_images/mary_VpMRm9x.png', '9685748578', 'Thodupuzha', 1, 22),
(3, 'Jeevan Johnson', 'farmer_aadhaar_images/license2_RIHUUKv.jpg', '9685748574', 'Thodpuzha', 1, 23),
(5, 'Jees Johnson', 'farmer_aadhaar_images/license3.jpg', '9685747474', 'tdpa', 1, 25);

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
  `house_no` int DEFAULT NULL,
  `registered_on` datetime(6) NOT NULL,
  `district_id` int NOT NULL,
  `location_id` int NOT NULL,
  `residents_association_id` int NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `GuestApp_household_district_id_32bdd425` (`district_id`),
  KEY `GuestApp_household_location_id_9a310686` (`location_id`),
  KEY `GuestApp_household_residents_association_id_1d8b3b00` (`residents_association_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `guestapp_household`
--

INSERT INTO `guestapp_household` (`id`, `household_name`, `phone`, `address`, `aadhaar_image`, `house_no`, `registered_on`, `district_id`, `location_id`, `residents_association_id`, `user_id`) VALUES
(1, 'Sonit Jolly', '9447984821', 'Anachalil ,\r\nMariyilaklunku,\r\nThodupuzha', 'household_aadhaar_images/insurance_NJG9fPa.avif', 1, '2025-12-28 04:52:33.901382', 1, 1, 1, 2),
(2, 'Maria Jolly', '9447568542', 'Anachalil\r\nthodupuzha', 'household_aadhaar_images/license3.jpg', 1, '2025-12-28 04:56:23.336330', 1, 1, 2, 3),
(3, 'Henna Maria Jiju', '9685457512', 'Vannapuram,\r\nThodupuzha', 'household_aadhaar_images/licence.png', 1, '2025-12-28 04:57:20.781143', 1, 1, 3, 4),
(4, 'Joseph Sojan', '9685214152', 'Karimkunnam,\r\nThodupuzha', 'household_aadhaar_images/license3_jvHcc2o.jpg', 2, '2025-12-28 04:58:25.870897', 1, 1, 1, 5),
(5, 'Nebin Reji', '9652634512', 'Vazhakulam,\r\nMuvattupuzha', 'household_aadhaar_images/licence_wIL0IMI.png', 1, '2025-12-29 02:29:02.981404', 1, 1, 3, 6),
(6, 'Rohit P Rajeev', '8574859615', 'Karimkunnam \r\nThodupuzha', 'household_aadhaar_images/license3_Ads7qjG.jpg', 2, '2025-12-29 02:32:33.248058', 1, 1, 3, 7),
(7, 'Joju Sibi', '8574561252', 'Muthalakodam po', 'household_aadhaar_images/licence_luLyVXh.png', 3, '2025-12-29 02:50:31.354297', 1, 1, 3, 8),
(8, 'Jishin Aji', '8574859615', 'Chunkom,\r\nThodupuzha', 'household_aadhaar_images/license2_THWHdQt.jpg', 4, '2025-12-29 04:25:24.378918', 1, 1, 3, 9),
(9, 'Vishnu P G', '7458965675', 'Udumbanoor,\r\nThodupuzha', '', 3, '2025-12-29 05:56:50.660997', 1, 1, 1, 10),
(10, 'Abin Joy', '9874124222', 'Olamattom,\r\nThodupuzha', 'household_aadhaar_images/license1.jpg', 4, '2025-12-29 05:58:27.463461', 1, 1, 1, 11),
(11, 'Sani Tomy', '9685745125', 'AnaKudiyil,\r\nThodupuzha', 'household_aadhaar_images/license2_3Dt2URY.jpg', 2, '2025-12-29 06:00:21.628866', 1, 1, 2, 12),
(12, 'Mejo John', '9685854156', 'Thodupuzha', 'household_aadhaar_images/john.png', 3, '2025-12-29 06:01:15.426936', 1, 1, 2, 13),
(13, 'Antony Jose', '7451531312', 'Mutoom,\r\nThodupuzha', 'household_aadhaar_images/license1_WwjV1fJ.jpg', 4, '2025-12-29 06:02:26.774375', 1, 1, 2, 14);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_systemsettings`
--

DROP TABLE IF EXISTS `myapp_systemsettings`;
CREATE TABLE IF NOT EXISTS `myapp_systemsettings` (
  `setting_key` varchar(100) NOT NULL,
  `setting_value` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  PRIMARY KEY (`setting_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_systemsettings`
--

INSERT INTO `myapp_systemsettings` (`setting_key`, `setting_value`, `description`, `last_updated`) VALUES
('compost_conversion_ratio', '4.0', 'Waste to compost conversion ratio (kg waste per 1kg compost)', '2026-01-04 12:12:50.305375');

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
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_bintype`
--

INSERT INTO `myapp_tbl_bintype` (`BinType_id`, `name`, `capacity_kg`, `price_rs`) VALUES
(3, 'Large', 50, 100.00),
(4, 'Medium', 25, 50.00);

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
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_collectionrequest`
--

INSERT INTO `myapp_tbl_collectionrequest` (`Request_id`, `total_quantity_kg`, `farmer_supply_kg`, `leftover_compost_kg`, `collection_date`, `status`, `collector_id`, `household_id`) VALUES
(1, 48.00, 0.00, 0.00, '2025-12-31 09:07:23.916363', 'Collected', 1, 1),
(2, 49.00, 0.00, 0.00, '2025-12-31 09:07:30.081012', 'Collected', 1, 4),
(3, 40.00, 0.00, 0.00, '2025-12-31 09:09:25.813626', 'Collected', 2, 9),
(4, 50.00, 0.00, 0.00, '2025-12-31 09:11:58.438694', 'Collected', 2, 10),
(5, 50.00, 0.00, 0.00, '2025-12-31 09:12:53.275188', 'Collected', 3, 2),
(6, 50.00, 0.00, 0.00, '2025-12-31 09:14:16.601595', 'Collected', 3, 2),
(7, 50.00, 0.00, 0.00, '2025-12-31 09:14:23.419955', 'Collected', 3, 11),
(8, 50.00, 0.00, 0.00, '2025-12-31 09:14:48.895765', 'Collected', 4, 12),
(9, 50.00, 0.00, 0.00, '2025-12-31 09:15:18.585838', 'Collected', 5, 3),
(10, 50.00, 0.00, 0.00, '2025-12-31 09:15:24.673930', 'Collected', 5, 5),
(11, 23.00, 0.00, 0.00, '2025-12-31 09:15:32.074356', 'Collected', 5, 6),
(12, 50.00, 0.00, 0.00, '2025-12-31 09:16:04.066382', 'Collected', 6, 7),
(13, 50.00, 0.00, 0.00, '2025-12-31 09:16:09.888448', 'Collected', 6, 8),
(14, 50.00, 0.00, 0.00, '2026-01-01 04:05:17.587461', 'Collected', 1, 1),
(15, 50.00, 0.00, 0.00, '2026-01-01 04:05:27.155606', 'Collected', 1, 4),
(16, 50.00, 0.00, 0.00, '2026-01-01 04:08:33.047362', 'Collected', 6, 8),
(17, 45.00, 0.00, 0.00, '2026-01-01 04:09:46.160936', 'Collected', 6, 8),
(18, 50.00, 0.00, 0.00, '2026-01-01 04:10:59.509289', 'Collected', 5, 3),
(19, 25.00, 0.00, 0.00, '2026-01-02 09:53:19.057453', 'Collected', 6, 8),
(20, 50.00, 0.00, 0.00, '2026-01-02 09:53:37.511774', 'Collected', 6, 8),
(21, 50.00, 0.00, 0.00, '2026-01-04 14:10:32.515769', 'Collected', 1, 1);

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
  UNIQUE KEY `MyApp_tbl_collectorassig_collector_id_Route_id_id_a755187b_uniq` (`collector_id`,`Route_id_id`,`day_of_week`),
  KEY `MyApp_tbl_collectorassignment_collector_id_2a489362` (`collector_id`),
  KEY `MyApp_tbl_collectorassignment_Route_id_id_8bdc554a` (`Route_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_collectorassignment`
--

INSERT INTO `myapp_tbl_collectorassignment` (`Assign_id`, `day_of_week`, `collector_id`, `Route_id_id`) VALUES
(1, 'Monday', 1, 1),
(2, 'Tuesday', 1, 1),
(3, 'Wednesday', 1, 1),
(4, 'Thursday', 1, 1),
(5, 'Friday', 1, 1),
(6, 'Saturday', 1, 1),
(7, 'Sunday', 1, 1),
(8, 'Monday', 2, 2),
(9, 'Tuesday', 2, 2),
(10, 'Wednesday', 2, 2),
(11, 'Thursday', 2, 2),
(12, 'Friday', 2, 2),
(13, 'Saturday', 2, 2),
(14, 'Sunday', 2, 2),
(15, 'Monday', 3, 3),
(16, 'Tuesday', 3, 3),
(17, 'Wednesday', 3, 3),
(18, 'Thursday', 3, 3),
(19, 'Friday', 3, 3),
(20, 'Saturday', 3, 3),
(21, 'Sunday', 3, 3),
(45, 'Wednesday', 4, 4),
(46, 'Thursday', 4, 4),
(47, 'Friday', 4, 4),
(44, 'Tuesday', 4, 4),
(43, 'Monday', 4, 4),
(52, 'Wednesday', 5, 5),
(53, 'Thursday', 5, 5),
(54, 'Friday', 5, 5),
(50, 'Monday', 5, 5),
(51, 'Tuesday', 5, 5),
(62, 'Saturday', 6, 6),
(61, 'Friday', 6, 6),
(60, 'Thursday', 6, 6),
(59, 'Wednesday', 6, 6),
(57, 'Monday', 6, 6),
(58, 'Tuesday', 6, 6),
(48, 'Saturday', 4, 4),
(49, 'Sunday', 4, 4),
(55, 'Saturday', 5, 5),
(56, 'Sunday', 5, 5),
(63, 'Sunday', 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_compostbatch`
--

DROP TABLE IF EXISTS `myapp_tbl_compostbatch`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_compostbatch` (
  `Batch_id` int NOT NULL AUTO_INCREMENT,
  `Batch_name` varchar(100) NOT NULL,
  `Source_Waste_kg` decimal(10,2) NOT NULL,
  `Date_Created` date NOT NULL,
  `Status` varchar(20) NOT NULL,
  `Grade` varchar(20) NOT NULL,
  `Stock_kg` decimal(10,2) NOT NULL,
  `price_per_kg` decimal(10,2) NOT NULL,
  `CompostManager_id_id` bigint NOT NULL,
  `salary_paid` tinyint(1) NOT NULL,
  PRIMARY KEY (`Batch_id`),
  KEY `MyApp_tbl_compostbatch_CompostManager_id_id_e3bd5a89` (`CompostManager_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_compostbatch`
--

INSERT INTO `myapp_tbl_compostbatch` (`Batch_id`, `Batch_name`, `Source_Waste_kg`, `Date_Created`, `Status`, `Grade`, `Stock_kg`, `price_per_kg`, `CompostManager_id_id`, `salary_paid`) VALUES
(1, 'AA', 160.00, '2025-12-31', 'Sold', 'A', 0.00, 200.00, 1, 1),
(2, 'BB', 245.00, '2026-01-01', 'Sold', 'A', 0.00, 200.00, 1, 1),
(3, 'rr', 75.00, '2026-01-02', 'Sold', 'A', 0.00, 200.00, 2, 0),
(4, 'CC', 50.00, '2026-01-04', 'Ready', 'A', 12.50, 200.00, 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_district`
--

DROP TABLE IF EXISTS `myapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_district` (
  `District_id` int NOT NULL AUTO_INCREMENT,
  `District_Name` varchar(100) NOT NULL,
  PRIMARY KEY (`District_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_district`
--

INSERT INTO `myapp_tbl_district` (`District_id`, `District_Name`) VALUES
(1, 'Idukki'),
(2, 'Kasaragod'),
(3, 'Kannur'),
(4, 'Wayanad'),
(5, 'Kozhikode'),
(6, 'Malappuram'),
(7, 'Palakkad'),
(8, 'Thrissur'),
(9, 'Ernakulam'),
(10, 'Kottayam'),
(11, 'Alappuzha'),
(12, 'Pathanamthitta'),
(13, 'Kollam'),
(14, 'Thiruvananthapuram');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_farmersupply`
--

DROP TABLE IF EXISTS `myapp_tbl_farmersupply`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_farmersupply` (
  `Supply_id` int NOT NULL AUTO_INCREMENT,
  `Quantity` decimal(10,2) NOT NULL,
  `Supply_Date` datetime(6) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `delivery_address` longtext NOT NULL,
  `delivery_status` varchar(20) NOT NULL,
  `Collection_id_id` int NOT NULL,
  `Farmer_id_id` bigint NOT NULL,
  `Payment_id_id` int DEFAULT NULL,
  PRIMARY KEY (`Supply_id`),
  KEY `MyApp_tbl_farmersupply_Collection_id_id_aca48a68` (`Collection_id_id`),
  KEY `MyApp_tbl_farmersupply_Farmer_id_id_1ea4de25` (`Farmer_id_id`),
  KEY `MyApp_tbl_farmersupply_Payment_id_id_d523fbbd` (`Payment_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_farmersupply`
--

INSERT INTO `myapp_tbl_farmersupply` (`Supply_id`, `Quantity`, `Supply_Date`, `unit_price`, `total_amount`, `payment_status`, `delivery_address`, `delivery_status`, `Collection_id_id`, `Farmer_id_id`, `Payment_id_id`) VALUES
(9, 200.00, '2025-12-31 15:56:48.650340', 10.00, 2000.00, 'Paid', 'Thodupuzha', 'Delivered', 2, 2, NULL),
(8, 100.00, '2025-12-31 15:47:05.280953', 10.00, 1000.00, 'Paid', 'Thodupuzha', 'Delivered', 2, 1, NULL);

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
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_householdpayment`
--

INSERT INTO `myapp_tbl_householdpayment` (`Payment_id`, `amount`, `payment_date`, `payment_for_date`, `status`, `transaction_id`, `bin_type_id`, `household_id`) VALUES
(19, 100.00, '2026-01-01 03:05:19.908773', '2026-01-01', 'Completed', 'TXN1767236719395', 3, 2),
(18, 100.00, '2026-01-01 02:59:39.894525', '2026-01-01', 'Completed', 'TXN1767236379100', 3, 1),
(3, 100.00, '2025-12-30 07:00:05.949606', '2025-12-30', 'Completed', 'TXN1767078005505', 3, 2),
(4, 100.00, '2025-12-31 08:39:14.985835', '2025-12-31', 'Completed', 'TXN1767170354680', 3, 1),
(5, 100.00, '2025-12-31 08:40:53.504081', '2025-12-31', 'Completed', 'TXN1767170453915', 3, 2),
(6, 100.00, '2025-12-31 08:42:35.669854', '2025-12-31', 'Completed', 'TXN1767170555501', 3, 3),
(7, 100.00, '2025-12-31 08:43:52.872962', '2025-12-31', 'Completed', 'TXN1767170632898', 3, 4),
(8, 100.00, '2025-12-31 08:45:00.442346', '2025-12-31', 'Completed', 'TXN1767170700830', 3, 5),
(9, 50.00, '2025-12-31 08:46:44.519810', '2025-12-31', 'Completed', 'TXN1767170804191', 4, 6),
(10, 100.00, '2025-12-31 08:47:45.667292', '2025-12-31', 'Completed', 'TXN1767170865958', 3, 7),
(11, 100.00, '2025-12-31 08:48:40.771959', '2025-12-31', 'Completed', 'TXN1767170920755', 3, 8),
(12, 100.00, '2025-12-31 08:49:11.417495', '2026-01-01', 'Completed', 'TXN1767170951296', 3, 8),
(13, 50.00, '2025-12-31 08:49:37.703496', '2026-01-02', 'Completed', 'TXN1767170977410', 4, 8),
(14, 100.00, '2025-12-31 08:50:52.673991', '2025-12-31', 'Completed', 'TXN1767171052280', 3, 9),
(15, 100.00, '2025-12-31 08:53:02.330431', '2025-12-31', 'Completed', 'TXN1767171182520', 3, 10),
(16, 100.00, '2025-12-31 08:54:03.320238', '2025-12-31', 'Completed', 'TXN1767171243947', 3, 11),
(17, 50.00, '2025-12-31 08:55:02.701464', '2025-12-31', 'Completed', 'TXN1767171302776', 4, 12),
(20, 100.00, '2026-01-01 03:55:55.866391', '2026-01-01', 'Completed', 'TXN1767239755315', 3, 3),
(21, 100.00, '2026-01-01 04:04:10.533070', '2026-01-01', 'Completed', 'TXN1767240250379', 3, 4),
(22, 100.00, '2026-01-02 09:41:54.526240', '2026-01-02', 'Completed', 'TXN1767346914734', 3, 8),
(23, 100.00, '2026-01-04 14:06:37.499531', '2026-01-04', 'Completed', 'TXN1767535597325', 3, 1);

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
(1, 28, 'Arackappara', 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_order`
--

DROP TABLE IF EXISTS `myapp_tbl_order`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_order` (
  `Order_id` int NOT NULL AUTO_INCREMENT,
  `Order_Date` datetime(6) NOT NULL,
  `Total_Amount` decimal(10,2) NOT NULL,
  `Delivery_Address` longtext NOT NULL,
  `Payment_Status` varchar(20) NOT NULL,
  `Buyer_id_id` bigint NOT NULL,
  `assigned_collector_id` bigint DEFAULT NULL,
  `assignment_status` varchar(20) NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `MyApp_tbl_order_Buyer_id_id_b41f89ef` (`Buyer_id_id`),
  KEY `MyApp_tbl_order_assigned_collector_id_27e539fb` (`assigned_collector_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_order`
--

INSERT INTO `myapp_tbl_order` (`Order_id`, `Order_Date`, `Total_Amount`, `Delivery_Address`, `Payment_Status`, `Buyer_id_id`, `assigned_collector_id`, `assignment_status`) VALUES
(6, '2025-12-31 16:12:32.001622', 7000.00, 'Thodpuzha', 'Paid', 3, NULL, 'Unassigned'),
(3, '2025-12-31 15:41:40.120244', 1000.00, 'Thodupuzha', 'Paid', 1, 1, 'Assigned'),
(5, '2025-12-31 15:56:19.593920', 2000.00, 'Thodupuzha', 'Paid', 2, 1, 'Assigned'),
(9, '2026-01-01 04:31:12.142049', 9000.00, 'Thodupuzha', 'Paid', 2, NULL, 'Unassigned'),
(8, '2026-01-01 04:23:40.482320', 8000.00, 'tdpa', 'Paid', 5, NULL, 'Unassigned'),
(10, '2026-01-02 10:40:41.298731', 4200.00, 'Thodupuzha', 'Paid', 2, NULL, 'Unassigned');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_orderitem`
--

DROP TABLE IF EXISTS `myapp_tbl_orderitem`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_orderitem` (
  `Item_id` int NOT NULL AUTO_INCREMENT,
  `Item_Type` varchar(20) NOT NULL,
  `Quantity_kg` decimal(10,2) NOT NULL,
  `Unit_Price` decimal(10,2) NOT NULL,
  `Delivery_Status` varchar(20) NOT NULL,
  `Batch_id_id` int DEFAULT NULL,
  `FarmerSupply_id_id` int DEFAULT NULL,
  `Order_id_id` int NOT NULL,
  PRIMARY KEY (`Item_id`),
  KEY `MyApp_tbl_orderitem_Batch_id_id_8f85e1a6` (`Batch_id_id`),
  KEY `MyApp_tbl_orderitem_FarmerSupply_id_id_b271a2ac` (`FarmerSupply_id_id`),
  KEY `MyApp_tbl_orderitem_Order_id_id_95f4d1a6` (`Order_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_orderitem`
--

INSERT INTO `myapp_tbl_orderitem` (`Item_id`, `Item_Type`, `Quantity_kg`, `Unit_Price`, `Delivery_Status`, `Batch_id_id`, `FarmerSupply_id_id`, `Order_id_id`) VALUES
(14, 'Compost', 40.00, 200.00, 'Delivered', 2, NULL, 8),
(13, 'Compost', 29.29, 200.00, 'Pending', 2, NULL, 7),
(12, 'Compost', 10.71, 200.00, 'Pending', 1, NULL, 7),
(11, 'Compost', 35.00, 200.00, 'Delivered', 1, NULL, 6),
(10, 'Waste', 200.00, 10.00, 'Delivered', NULL, 9, 5),
(8, 'Waste', 100.00, 10.00, 'Delivered', NULL, 8, 3),
(15, 'Compost', 45.00, 200.00, 'Delivered', 2, NULL, 9),
(16, 'Compost', 21.00, 200.00, 'Delivered', 3, NULL, 10);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_paymenttransaction`
--

DROP TABLE IF EXISTS `myapp_tbl_paymenttransaction`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_paymenttransaction` (
  `Transaction_id` int NOT NULL AUTO_INCREMENT,
  `Amount` decimal(10,2) NOT NULL,
  `transaction_type` varchar(30) NOT NULL,
  `Reference_id` int DEFAULT NULL,
  `transaction_date` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `Payer_id_id` bigint NOT NULL,
  `Receiver_id_id` bigint NOT NULL,
  PRIMARY KEY (`Transaction_id`),
  KEY `MyApp_tbl_paymenttransaction_Payer_id_id_76eabc0d` (`Payer_id_id`),
  KEY `MyApp_tbl_paymenttransaction_Receiver_id_id_bcd281c9` (`Receiver_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_paymenttransaction`
--

INSERT INTO `myapp_tbl_paymenttransaction` (`Transaction_id`, `Amount`, `transaction_type`, `Reference_id`, `transaction_date`, `status`, `Payer_id_id`, `Receiver_id_id`) VALUES
(12, 1000.00, 'CollectorSalary', NULL, '2025-12-31 17:04:59.662452', 'Success', 1, 20),
(11, 1000.00, 'CollectorSalary', NULL, '2025-12-31 17:02:25.107496', 'Success', 1, 19),
(10, 7000.00, 'CompostSale', 6, '2025-12-31 16:12:32.011788', 'Success', 23, 23),
(9, 2000.00, 'WasteSale', 5, '2025-12-31 15:56:48.654712', 'Success', 22, 15),
(8, 1000.00, 'WasteSale', 3, '2025-12-31 15:47:05.292268', 'Success', 21, 15),
(13, 1000.00, 'ManagerSalary', NULL, '2025-12-31 17:07:15.766564', 'Success', 1, 26),
(14, 8000.00, 'CompostSale', 7, '2026-01-01 04:23:36.010355', 'Success', 25, 25),
(15, 8000.00, 'CompostSale', 8, '2026-01-01 04:23:40.493212', 'Success', 25, 25),
(16, 9000.00, 'CompostSale', 9, '2026-01-01 04:31:12.149702', 'Success', 22, 22),
(17, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:19.061439', 'Success', 1, 15),
(18, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:22.944371', 'Success', 1, 19),
(19, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:27.175922', 'Success', 1, 20),
(20, 1000.00, 'ManagerSalary', NULL, '2026-01-01 04:32:32.433867', 'Success', 1, 26),
(21, 4200.00, 'CompostSale', 10, '2026-01-02 10:40:41.307651', 'Success', 22, 22),
(22, 1000.00, 'CollectorSalary', NULL, '2026-01-04 15:40:31.508704', 'Success', 1, 15),
(23, 1000.00, 'CollectorSalary', NULL, '2026-01-04 15:40:37.023828', 'Success', 1, 20);

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
  `actual_weight_kg` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(20) DEFAULT NULL,
  `payment_amount` decimal(10,2) DEFAULT NULL,
  `payment_status` varchar(20) NOT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `payment_date` datetime(6) DEFAULT NULL,
  `assigned_collector_id` bigint DEFAULT NULL,
  `bin_type_id` int DEFAULT NULL,
  `household_id` bigint NOT NULL,
  `payment_id` int DEFAULT NULL,
  PRIMARY KEY (`Pickup_id`),
  KEY `MyApp_tbl_pickuprequest_assigned_collector_id_7c3bfac0` (`assigned_collector_id`),
  KEY `MyApp_tbl_pickuprequest_bin_type_id_94b84ff5` (`bin_type_id`),
  KEY `MyApp_tbl_pickuprequest_household_id_071f0928` (`household_id`),
  KEY `MyApp_tbl_pickuprequest_payment_id_74a31eed` (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_pickuprequest`
--

INSERT INTO `myapp_tbl_pickuprequest` (`Pickup_id`, `scheduled_date`, `request_time`, `status`, `actual_weight_kg`, `payment_method`, `payment_amount`, `payment_status`, `transaction_id`, `payment_date`, `assigned_collector_id`, `bin_type_id`, `household_id`, `payment_id`) VALUES
(19, '2026-01-01', '09:00:00.000000', 'Approved', NULL, 'UPI', 100.00, 'Completed', 'TXN1767236719395', '2026-01-01 03:05:19.910460', 3, 3, 2, 19),
(18, '2026-01-01', '09:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767236379100', '2026-01-01 02:59:39.897944', 1, 3, 1, 18),
(3, '2025-12-30', '13:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767078005505', '2025-12-30 07:00:05.953796', 3, 3, 2, 3),
(4, '2025-12-31', '14:20:00.000000', 'Completed', 48.00, 'COD', 100.00, 'Completed', 'TXN1767170354680', '2025-12-31 08:39:14.989442', 1, 3, 1, 4),
(5, '2025-12-31', '14:22:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170453915', '2025-12-31 08:40:53.507203', 3, 3, 2, 5),
(6, '2025-12-31', '14:20:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170555501', '2025-12-31 08:42:35.672436', 5, 3, 3, 6),
(7, '2025-12-31', '14:20:00.000000', 'Completed', 49.00, 'UPI', 100.00, 'Completed', 'TXN1767170632898', '2025-12-31 08:43:52.875185', 1, 3, 4, 7),
(8, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170700830', '2025-12-31 08:45:00.444639', 5, 3, 5, 8),
(9, '2025-12-31', '14:30:00.000000', 'Completed', 23.00, 'UPI', 50.00, 'Completed', 'TXN1767170804191', '2025-12-31 08:46:44.522437', 5, 4, 6, 9),
(10, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170865958', '2025-12-31 08:47:45.668706', 6, 3, 7, 10),
(11, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170920755', '2025-12-31 08:48:40.772903', 6, 3, 8, 11),
(12, '2026-01-01', '16:00:00.000000', 'Completed', 45.00, 'UPI', 100.00, 'Completed', 'TXN1767170951296', '2025-12-31 08:49:11.419086', 6, 3, 8, 12),
(13, '2026-01-02', '16:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1767170977410', '2025-12-31 08:49:37.704320', 6, 4, 8, 13),
(14, '2025-12-31', '14:40:00.000000', 'Completed', 40.00, 'UPI', 100.00, 'Completed', 'TXN1767171052280', '2025-12-31 08:50:52.674920', 2, 3, 9, 14),
(15, '2025-12-31', '14:40:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767171182520', '2025-12-31 08:53:02.330995', 2, 3, 10, 15),
(16, '2025-12-31', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767171243947', '2025-12-31 08:54:03.321078', 3, 3, 11, 16),
(17, '2025-12-31', '15:00:00.000000', 'Completed', 50.00, 'UPI', 50.00, 'Completed', 'TXN1767171302776', '2025-12-31 08:55:02.702368', 4, 4, 12, 17),
(20, '2026-01-01', '10:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767239755315', '2026-01-01 03:55:55.868903', 5, 3, 3, 20),
(21, '2026-01-01', '10:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767240250379', '2026-01-01 04:04:10.535446', 1, 3, 4, 21),
(22, '2026-01-02', '16:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767346914734', '2026-01-02 09:41:54.530567', 6, 3, 8, 22),
(23, '2026-01-04', '20:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767535597325', '2026-01-04 14:06:37.501394', 1, 3, 1, 23);

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
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_residentsassociation`
--

INSERT INTO `myapp_tbl_residentsassociation` (`RA_id`, `Association_Name`, `Location_id`) VALUES
(1, 'Chaithanya Nagar', 1),
(2, 'Divine Nagar', 1),
(3, 'Perukoni', 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_route`
--

DROP TABLE IF EXISTS `myapp_tbl_route`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_route` (
  `Route_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `start_house_no` int DEFAULT NULL,
  `end_house_no` int DEFAULT NULL,
  `location_id` int NOT NULL,
  `residents_association_id` int DEFAULT NULL,
  PRIMARY KEY (`Route_id`),
  UNIQUE KEY `name` (`name`),
  KEY `MyApp_tbl_route_location_id_2c6c2a9b` (`location_id`),
  KEY `MyApp_tbl_route_residents_association_id_278d4697` (`residents_association_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_route`
--

INSERT INTO `myapp_tbl_route` (`Route_id`, `name`, `start_house_no`, `end_house_no`, `location_id`, `residents_association_id`) VALUES
(1, 'AOne', 1, 2, 1, 1),
(2, 'ATwo', 3, 4, 1, 1),
(3, 'BOne', 1, 2, 1, 2),
(4, 'BTwo', 2, 4, 1, 2),
(5, 'COne', 1, 2, 1, 3),
(6, 'CTwo', 3, 4, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_tbl_wasteinventory`
--

DROP TABLE IF EXISTS `myapp_tbl_wasteinventory`;
CREATE TABLE IF NOT EXISTS `myapp_tbl_wasteinventory` (
  `Inventory_id` int NOT NULL AUTO_INCREMENT,
  `available_quantity_kg` decimal(10,2) NOT NULL,
  `price_per_kg` decimal(10,2) NOT NULL,
  `collection_date` datetime(6) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `status` varchar(20) NOT NULL,
  `collection_request_id` int NOT NULL,
  `collector_id` bigint NOT NULL,
  `salary_paid` tinyint(1) NOT NULL,
  PRIMARY KEY (`Inventory_id`),
  KEY `MyApp_tbl_wasteinventory_collection_request_id_55fad03c` (`collection_request_id`),
  KEY `MyApp_tbl_wasteinventory_collector_id_b3275b51` (`collector_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_tbl_wasteinventory`
--

INSERT INTO `myapp_tbl_wasteinventory` (`Inventory_id`, `available_quantity_kg`, `price_per_kg`, `collection_date`, `is_available`, `status`, `collection_request_id`, `collector_id`, `salary_paid`) VALUES
(10, 37.00, 10.00, '2025-12-31 09:15:24.676404', 0, 'Used', 10, 5, 1),
(11, 23.00, 10.00, '2025-12-31 09:15:32.076181', 0, 'Used', 11, 5, 1),
(12, 50.00, 10.00, '2025-12-31 09:16:04.067852', 0, 'Used', 12, 6, 1),
(13, 50.00, 10.00, '2025-12-31 09:16:09.890196', 0, 'Used', 13, 6, 1),
(14, 50.00, 10.00, '2026-01-01 04:05:17.590083', 0, 'Used', 14, 1, 1),
(15, 50.00, 10.00, '2026-01-01 04:05:27.158231', 0, 'Used', 15, 1, 1),
(16, 50.00, 10.00, '2026-01-01 04:08:33.049065', 0, 'Used', 16, 6, 1),
(17, 45.00, 10.00, '2026-01-01 04:09:46.162583', 0, 'Used', 17, 6, 1),
(18, 50.00, 10.00, '2026-01-01 04:10:59.510387', 0, 'Used', 18, 5, 1),
(19, 25.00, 10.00, '2026-01-02 09:53:19.060147', 0, 'Used', 19, 6, 1),
(20, 50.00, 10.00, '2026-01-02 09:53:37.513822', 0, 'Used', 20, 6, 1),
(21, 50.00, 10.00, '2026-01-04 14:10:32.519652', 0, 'Used', 21, 1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
