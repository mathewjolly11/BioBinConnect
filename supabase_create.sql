-- RUN THIS SECOND TO RECREATE DB
SET search_path TO public;


DROP TABLE IF EXISTS "auth_group" CASCADE;
CREATE TABLE "auth_group" (
  "id" SERIAL,
  "name" VARCHAR(150) NOT NULL,
  CONSTRAINT "auth_group_pk" PRIMARY KEY ("id"),
  CONSTRAINT "auth_group_name_unique" UNIQUE ("name")
);

DROP TABLE IF EXISTS "auth_group_permissions" CASCADE;
CREATE TABLE "auth_group_permissions" (
  "id" SERIAL,
  "group_id" INTEGER NOT NULL,
  "permission_id" INTEGER NOT NULL,
  CONSTRAINT "auth_group_permissions_pk" PRIMARY KEY ("id"),
  CONSTRAINT "auth_group_permissions_auth_group_permissions_group_id_permission_id_0cd325b0_uniq_unique" UNIQUE ("group_id","permission_id")
);

DROP TABLE IF EXISTS "auth_permission" CASCADE;
CREATE TABLE "auth_permission" (
  "id" SERIAL,
  "name" VARCHAR(255) NOT NULL,
  "content_type_id" INTEGER NOT NULL,
  "codename" VARCHAR(100) NOT NULL,
  CONSTRAINT "auth_permission_pk" PRIMARY KEY ("id"),
  CONSTRAINT "auth_permission_auth_permission_content_type_id_codename_01ab375a_uniq_unique" UNIQUE ("content_type_id","codename")
);
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (21, 'Can add tbl_ bin type', 6, 'add_tbl_bintype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (22, 'Can change tbl_ bin type', 6, 'change_tbl_bintype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (23, 'Can delete tbl_ bin type', 6, 'delete_tbl_bintype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (24, 'Can view tbl_ bin type', 6, 'view_tbl_bintype');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (25, 'Can add tbl_ district', 7, 'add_tbl_district');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (26, 'Can change tbl_ district', 7, 'change_tbl_district');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (27, 'Can delete tbl_ district', 7, 'delete_tbl_district');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (28, 'Can view tbl_ district', 7, 'view_tbl_district');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (29, 'Can add tbl_ collection request', 8, 'add_tbl_collectionrequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (30, 'Can change tbl_ collection request', 8, 'change_tbl_collectionrequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (31, 'Can delete tbl_ collection request', 8, 'delete_tbl_collectionrequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (32, 'Can view tbl_ collection request', 8, 'view_tbl_collectionrequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (33, 'Can add tbl_ compost batch', 9, 'add_tbl_compostbatch');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (34, 'Can change tbl_ compost batch', 9, 'change_tbl_compostbatch');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (35, 'Can delete tbl_ compost batch', 9, 'delete_tbl_compostbatch');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (36, 'Can view tbl_ compost batch', 9, 'view_tbl_compostbatch');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (37, 'Can add tbl_ farmer supply', 10, 'add_tbl_farmersupply');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (38, 'Can change tbl_ farmer supply', 10, 'change_tbl_farmersupply');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (39, 'Can delete tbl_ farmer supply', 10, 'delete_tbl_farmersupply');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (40, 'Can view tbl_ farmer supply', 10, 'view_tbl_farmersupply');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (41, 'Can add tbl_ household payment', 11, 'add_tbl_householdpayment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (42, 'Can change tbl_ household payment', 11, 'change_tbl_householdpayment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (43, 'Can delete tbl_ household payment', 11, 'delete_tbl_householdpayment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (44, 'Can view tbl_ household payment', 11, 'view_tbl_householdpayment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (45, 'Can add tbl_location', 12, 'add_tbl_location');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (46, 'Can change tbl_location', 12, 'change_tbl_location');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (47, 'Can delete tbl_location', 12, 'delete_tbl_location');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (48, 'Can view tbl_location', 12, 'view_tbl_location');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (49, 'Can add tbl_ order', 13, 'add_tbl_order');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (50, 'Can change tbl_ order', 13, 'change_tbl_order');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (51, 'Can delete tbl_ order', 13, 'delete_tbl_order');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (52, 'Can view tbl_ order', 13, 'view_tbl_order');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (53, 'Can add tbl_ order item', 14, 'add_tbl_orderitem');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (54, 'Can change tbl_ order item', 14, 'change_tbl_orderitem');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (55, 'Can delete tbl_ order item', 14, 'delete_tbl_orderitem');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (56, 'Can view tbl_ order item', 14, 'view_tbl_orderitem');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (57, 'Can add tbl_ payment transaction', 15, 'add_tbl_paymenttransaction');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (58, 'Can change tbl_ payment transaction', 15, 'change_tbl_paymenttransaction');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (59, 'Can delete tbl_ payment transaction', 15, 'delete_tbl_paymenttransaction');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (60, 'Can view tbl_ payment transaction', 15, 'view_tbl_paymenttransaction');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (61, 'Can add tbl_ pickup request', 16, 'add_tbl_pickuprequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (62, 'Can change tbl_ pickup request', 16, 'change_tbl_pickuprequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (63, 'Can delete tbl_ pickup request', 16, 'delete_tbl_pickuprequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (64, 'Can view tbl_ pickup request', 16, 'view_tbl_pickuprequest');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (65, 'Can add tbl_residentsassociation', 17, 'add_tbl_residentsassociation');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (66, 'Can change tbl_residentsassociation', 17, 'change_tbl_residentsassociation');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (67, 'Can delete tbl_residentsassociation', 17, 'delete_tbl_residentsassociation');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (68, 'Can view tbl_residentsassociation', 17, 'view_tbl_residentsassociation');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (69, 'Can add tbl_ route', 18, 'add_tbl_route');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (70, 'Can change tbl_ route', 18, 'change_tbl_route');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (71, 'Can delete tbl_ route', 18, 'delete_tbl_route');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (72, 'Can view tbl_ route', 18, 'view_tbl_route');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (73, 'Can add tbl_ collector assignment', 19, 'add_tbl_collectorassignment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (74, 'Can change tbl_ collector assignment', 19, 'change_tbl_collectorassignment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (75, 'Can delete tbl_ collector assignment', 19, 'delete_tbl_collectorassignment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (76, 'Can view tbl_ collector assignment', 19, 'view_tbl_collectorassignment');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (77, 'Can add tbl_ waste inventory', 20, 'add_tbl_wasteinventory');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (78, 'Can change tbl_ waste inventory', 20, 'change_tbl_wasteinventory');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (79, 'Can delete tbl_ waste inventory', 20, 'delete_tbl_wasteinventory');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (80, 'Can view tbl_ waste inventory', 20, 'view_tbl_wasteinventory');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (81, 'Can add collector', 21, 'add_collector');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (82, 'Can change collector', 21, 'change_collector');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (83, 'Can delete collector', 21, 'delete_collector');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (84, 'Can view collector', 21, 'view_collector');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (85, 'Can add compost manager', 22, 'add_compostmanager');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (86, 'Can change compost manager', 22, 'change_compostmanager');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (87, 'Can delete compost manager', 22, 'delete_compostmanager');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (88, 'Can view compost manager', 22, 'view_compostmanager');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (89, 'Can add farmer', 23, 'add_farmer');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (90, 'Can change farmer', 23, 'change_farmer');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (91, 'Can delete farmer', 23, 'delete_farmer');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (92, 'Can view farmer', 23, 'view_farmer');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (93, 'Can add household', 24, 'add_household');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (94, 'Can change household', 24, 'change_household');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (95, 'Can delete household', 24, 'delete_household');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (96, 'Can view household', 24, 'view_household');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (97, 'Can add custom user', 25, 'add_customuser');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (98, 'Can change custom user', 25, 'change_customuser');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (99, 'Can delete custom user', 25, 'delete_customuser');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (100, 'Can view custom user', 25, 'view_customuser');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (101, 'Can add System Setting', 26, 'add_systemsettings');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (102, 'Can change System Setting', 26, 'change_systemsettings');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (103, 'Can delete System Setting', 26, 'delete_systemsettings');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (104, 'Can view System Setting', 26, 'view_systemsettings');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (105, 'Can add password reset otp', 27, 'add_passwordresetotp');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (106, 'Can change password reset otp', 27, 'change_passwordresetotp');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (107, 'Can delete password reset otp', 27, 'delete_passwordresetotp');
INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES (108, 'Can view password reset otp', 27, 'view_passwordresetotp');

DROP TABLE IF EXISTS "django_admin_log" CASCADE;
CREATE TABLE "django_admin_log" (
  "id" SERIAL,
  "action_time" TIMESTAMP(6) NOT NULL,
  "object_id" TEXT,
  "object_repr" VARCHAR(200) NOT NULL,
  "action_flag" SMALLINT NOT NULL,
  "change_message" TEXT NOT NULL,
  "content_type_id" INTEGER DEFAULT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "django_admin_log_pk" PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "django_content_type" CASCADE;
CREATE TABLE "django_content_type" (
  "id" SERIAL,
  "app_label" VARCHAR(100) NOT NULL,
  "model" VARCHAR(100) NOT NULL,
  CONSTRAINT "django_content_type_pk" PRIMARY KEY ("id"),
  CONSTRAINT "django_content_type_django_content_type_app_label_model_76bd3d3b_uniq_unique" UNIQUE ("app_label","model")
);
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (1, 'admin', 'logentry');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (2, 'auth', 'permission');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (3, 'auth', 'group');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (5, 'sessions', 'session');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (6, 'MyApp', 'tbl_bintype');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (7, 'MyApp', 'tbl_district');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (8, 'MyApp', 'tbl_collectionrequest');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (9, 'MyApp', 'tbl_compostbatch');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (10, 'MyApp', 'tbl_farmersupply');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (11, 'MyApp', 'tbl_householdpayment');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (12, 'MyApp', 'tbl_location');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (13, 'MyApp', 'tbl_order');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (14, 'MyApp', 'tbl_orderitem');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (15, 'MyApp', 'tbl_paymenttransaction');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (16, 'MyApp', 'tbl_pickuprequest');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (17, 'MyApp', 'tbl_residentsassociation');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (18, 'MyApp', 'tbl_route');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (19, 'MyApp', 'tbl_collectorassignment');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (20, 'MyApp', 'tbl_wasteinventory');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (21, 'GuestApp', 'collector');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (22, 'GuestApp', 'compostmanager');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (23, 'GuestApp', 'farmer');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (24, 'GuestApp', 'household');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (25, 'GuestApp', 'customuser');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (26, 'MyApp', 'systemsettings');
INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES (27, 'GuestApp', 'passwordresetotp');

DROP TABLE IF EXISTS "django_migrations" CASCADE;
CREATE TABLE "django_migrations" (
  "id" SERIAL,
  "app" VARCHAR(255) NOT NULL,
  "name" VARCHAR(255) NOT NULL,
  "applied" TIMESTAMP(6) NOT NULL,
  CONSTRAINT "django_migrations_pk" PRIMARY KEY ("id")
);
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (1, 'contenttypes', '0001_initial', '2025-12-28 04:45:39.078443');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2025-12-28 04:45:39.198768');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (3, 'auth', '0001_initial', '2025-12-28 04:45:39.544674');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2025-12-28 04:45:39.598522');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (5, 'auth', '0003_alter_user_email_max_length', '2025-12-28 04:45:39.607078');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (6, 'auth', '0004_alter_user_username_opts', '2025-12-28 04:45:39.613723');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (7, 'auth', '0005_alter_user_last_login_null', '2025-12-28 04:45:39.618244');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (8, 'auth', '0006_require_contenttypes_0002', '2025-12-28 04:45:39.619347');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2025-12-28 04:45:39.628246');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (10, 'auth', '0008_alter_user_username_max_length', '2025-12-28 04:45:39.633584');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2025-12-28 04:45:39.640899');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (12, 'auth', '0010_alter_group_name_max_length', '2025-12-28 04:45:39.698977');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (13, 'auth', '0011_update_proxy_permissions', '2025-12-28 04:45:39.705302');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2025-12-28 04:45:39.709654');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (15, 'GuestApp', '0001_initial', '2025-12-28 04:45:39.762187');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (16, 'MyApp', '0001_initial', '2025-12-28 04:45:41.813199');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (17, 'GuestApp', '0002_initial', '2025-12-28 04:45:42.702440');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (18, 'admin', '0001_initial', '2025-12-28 04:45:43.006807');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (19, 'admin', '0002_logentry_remove_auto_add', '2025-12-28 04:45:43.023948');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (20, 'admin', '0003_logentry_add_action_flag_choices', '2025-12-28 04:45:43.038007');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (21, 'sessions', '0001_initial', '2025-12-28 04:45:43.075376');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (22, 'MyApp', '0002_alter_tbl_collectorassignment_options_and_more', '2025-12-31 15:31:23.675764');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (23, 'MyApp', '0003_tbl_wasteinventory_salary_paid', '2025-12-31 16:21:56.839942');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (24, 'MyApp', '0004_tbl_compostbatch_salary_paid', '2025-12-31 16:22:19.702670');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (25, 'MyApp', '0005_systemsettings', '2026-01-04 11:50:24.359107');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (26, 'GuestApp', '0003_customuser_account_status', '2026-01-04 13:50:55.859071');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (27, 'MyApp', '0006_alter_tbl_farmersupply_collection_id', '2026-01-12 11:42:45.327742');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (28, 'MyApp', '0007_fix_grade_system_and_cleanup', '2026-01-22 01:47:25.403358');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (29, 'GuestApp', '0004_passwordresetotp', '2026-02-06 05:56:40.236277');
INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES (30, 'MyApp', '0008_alter_tbl_compostbatch_price_per_kg', '2026-02-06 05:56:40.246011');

DROP TABLE IF EXISTS "django_session" CASCADE;
CREATE TABLE "django_session" (
  "session_key" VARCHAR(40) NOT NULL,
  "session_data" TEXT NOT NULL,
  "expire_date" TIMESTAMP(6) NOT NULL,
  CONSTRAINT "django_session_pk" PRIMARY KEY ("session_key")
);
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('vpili4uro6r04ht7pv76y839ufo9g9gi', '.eJxVjDsOwjAQBe_iGlm2N_4sJT1niLzZNQ6gRIqTCnF3iJQC2jcz76X6vK2135os_cjqrKw6_W6Uh4dMO-B7nm6zHuZpXUbSu6IP2vR1ZnleDvfvoOZWv3WxBiGCJ-pM4Ig-dSYGFudQiG0ZEgckhFSCCYAMCB5QioteXEdWvT_CxTcE:1vb8rK:ZQ3QK7KvnGZniJHt5mjnDbq4V2NNLTBNMJ5amLrv6nM', '2026-01-15 02:56:18.079237');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('duafwdgn555lq0kpp26fauvhx36am1ut', '.eJxVjEEOwiAQRe_C2hBIYQCX7j0DYRhGqqYkpV013t026UK3_733NxHTutS49jLHkcRVaC0uvyOm_CrTQeiZpkeTuU3LPKI8FHnSLu-Nyvt2un8HNfW610zWeCZQAzivXQpEKgxIMGR0YDwwAypgBcEVcNYg2kImazY7IhafLwc0OIs:1varwf:lyEGrn4p3_b00lXiMzQr_O2Ckz_7qfESPFipHAArdnE', '2026-01-14 08:52:41.189442');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('8e2rmu2vloqn6poyap5kdsz6z4tn2xl2', '.eJxVjDsOwjAQBe_iGllef1ibkj5nsNbrDQmgRIqTCnF3iJQC2jcz76UybeuQtyZLHqu6KAjq9DsW4odMO6l3mm6z5nlal7HoXdEHbbqbqzyvh_t3MFAbvjVjQSMIQi5yIPHeRyfV-TMYtpCklx4jYCzOVgSuydjAkHprMLho1PsDB843eQ:1vayQ3:7pqtfA6agGiJ_wraIuJohezrFLuC3rkR-g8pQwroVBM', '2026-01-14 15:47:27.485702');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('brrg44i94hp1q6w7dt4xa89b8bd7rnhe', '.eJxVjDsOwjAQBe_iGll2vP5R0nMGa9cfHEC2FCcV4u4QKQW0b2beiwXc1hq2kZcwJ3Zmk2Gn35EwPnLbSbpju3Uee1uXmfiu8IMOfu0pPy-H-3dQcdRv7SA5aVMsXvkcLYJwQGoirbTRpkTwPjmTQUhbjCteKIWy-EgCyWUC9v4A_MQ39A:1vayUF:HpdpVpxMrR--RCnWveKAmtzQUj4mYqcCuZeL9nq-UGg', '2026-01-14 15:51:47.168645');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('qtzjewrpvx1l5lcoa6s17faha7vi6wnp', '.eJxVjMsOwiAQRf-FtSFAGR4u3fsNZIaHVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZKctOvyNhfOS2k3THdus89rYuM_Fd4Qcd_NpTfl4O9--g4qjfmpRzfhIwWRF9RO2icZo0KC-VJYeTLUVkMEQWrDKmJEDwWaH0CEIm9v4A5L83Vg:1vcML0:UY237ukFqdnpa2U3AkBfkIVyCMAr8SjHXKvCOAmw5Ms', '2026-01-18 11:31:58.058481');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('yvnnmazhfack7tpi49pv3q85yb6niudh', '.eJxVjDsOwjAQBe_iGllef1ibkj5nsNbrDQmgRIqTCnF3iJQC2jcz76UybeuQtyZLHqu6KAjq9DsW4odMO6l3mm6z5nlal7HoXdEHbbqbqzyvh_t3MFAbvjVjQSMIQi5yIPHeRyfV-TMYtpCklx4jYCzOVgSuydjAkHprMLho1PsDB843eQ:1vcOoC:jxgXokVcFvoi_VpsoBPI1lqRLrR1jETpzvy0G3r0ccU', '2026-01-18 14:10:16.434486');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('qxifwpjj9iscjw3pqncdmk8ny2zaqtbv', '.eJxVjMsOwiAQRf-FtSE8hlZcuu83kGEYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXocXpd4tID647SHestyap1XWZo9wVedAup5b4eT3cv4OCvXxrAo1Z5zha9hYAKaZktMvAyqNS0Z-tsahGPYBCYJNpiJkco-PMQFq8P_XvOKM:1voaQp:v1GWofQ701qyN_ogfWozM2nXahNCnBZTc6vWx3Sly00', '2026-02-21 05:00:31.378934');
INSERT INTO "django_session" ("session_key", "session_data", "expire_date") VALUES ('w6bww4ha5zsypvwzyr6cm7voh60kro3f', '.eJxVjDsOwjAQBe_iGll28CdLSZ8zWLveNQ6gRIqTCnF3iJQC2jcz76USbmtNW5MljawuykZ1-h0J80OmnfAdp9us8zyty0h6V_RBmx5mluf1cP8OKrb6rVFC7yxAjiTRgiPxPRfKpZyDt-zRMQBjMBINdRaQwBnocoDQoQej3h8eZzgg:1vb0xI:kgPCXLr-kGj3NbzafyVsX3FV2d4HJFIWVf08i3k7er4', '2026-01-14 18:29:56.178486');

DROP TABLE IF EXISTS "GuestApp_collector" CASCADE;
CREATE TABLE "GuestApp_collector" (
  "id" BIGSERIAL,
  "collector_name" VARCHAR(100) NOT NULL,
  "phone" VARCHAR(15) NOT NULL,
  "address" TEXT NOT NULL,
  "license_image" VARCHAR(100) NOT NULL,
  "is_active" BOOLEAN NOT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "guestapp_collector_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_collector_user_id_unique" UNIQUE ("user_id")
);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (1, 'Ashin Aji', '9788578554', 'Thodupuzha', 'collector_licenses/license2_a5cpAe3.jpg', TRUE, 15);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (2, 'Nikhil Biby', '9685745125', 'Vazhakulam,\r\nThodupuzha', 'collector_licenses/john.png', TRUE, 16);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (3, 'Nikitha Biby', '8585745968', 'Thodupuzha', 'collector_licenses/license2_jJMwJyj.jpg', TRUE, 17);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (4, 'Jobin Jose', '9685748574', 'Thodupuzha', 'collector_licenses/mary.png', TRUE, 18);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (5, 'Aashish Shoby', '9685857487', 'Thodupuzha', 'collector_licenses/mary_Max62cS.png', TRUE, 19);
INSERT INTO "GuestApp_collector" ("id", "collector_name", "phone", "address", "license_image", "is_active", "user_id") VALUES (6, 'Jacob Suni', '9685214152', 'Thodupuzha', 'collector_licenses/license1.jpg', TRUE, 20);

DROP TABLE IF EXISTS "GuestApp_compostmanager" CASCADE;
CREATE TABLE "GuestApp_compostmanager" (
  "id" BIGSERIAL,
  "compostmanager_name" VARCHAR(100) NOT NULL,
  "phone" VARCHAR(15) NOT NULL,
  "address" TEXT NOT NULL,
  "license_number" VARCHAR(100) NOT NULL,
  "is_active" BOOLEAN NOT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "guestapp_compostmanager_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_compostmanager_license_number_unique" UNIQUE ("license_number"),
  CONSTRAINT "GuestApp_compostmanager_user_id_unique" UNIQUE ("user_id")
);
INSERT INTO "GuestApp_compostmanager" ("id", "compostmanager_name", "phone", "address", "license_number", "is_active", "user_id") VALUES (1, 'Soorya Sunil', '9685441412', 'tdpa', '4141414', TRUE, 26);
INSERT INTO "GuestApp_compostmanager" ("id", "compostmanager_name", "phone", "address", "license_number", "is_active", "user_id") VALUES (2, 'Gibin Jose', '9685748596', 'TDPA', '3516456', TRUE, 27);

DROP TABLE IF EXISTS "GuestApp_customuser" CASCADE;
CREATE TABLE "GuestApp_customuser" (
  "id" BIGSERIAL,
  "password" VARCHAR(128) NOT NULL,
  "last_login" TIMESTAMP(6) DEFAULT NULL,
  "is_superuser" BOOLEAN NOT NULL,
  "name" VARCHAR(100) NOT NULL,
  "email" VARCHAR(191) NOT NULL,
  "phone" VARCHAR(15) DEFAULT NULL,
  "role" VARCHAR(20) NOT NULL,
  "is_verified" BOOLEAN NOT NULL,
  "is_active" BOOLEAN NOT NULL,
  "is_staff" BOOLEAN NOT NULL,
  "date_joined" TIMESTAMP(6) NOT NULL,
  "account_status" VARCHAR(20) NOT NULL,
  CONSTRAINT "guestapp_customuser_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_customuser_email_unique" UNIQUE ("email")
);
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (1, 'pbkdf2_sha256$1200000$gdS5uKFlPIMFR1edXc58Mq$9R9ef5AMavquPUw3z+7ULSFZrEKyQAWTtAUcD5dJYXo=', '2026-02-07 05:00:31.373895', TRUE, 'Admin', 'admin@gmail.com', NULL, 'admin', TRUE, TRUE, TRUE, '2025-12-28 04:46:53.683344', 'Pending');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (2, 'pbkdf2_sha256$1200000$wLDce9Vt82FqJ9A9Rqckt7$dYzoqTn47ukUcYFm6XmH5cU5a1JxOT+VtzhoWixKSSI=', '2026-02-07 05:01:44.007707', FALSE, 'Sonit Jolly', 'sonitjollyavj@gmail.com', '9447984821', 'household', TRUE, TRUE, FALSE, '2025-12-28 04:52:33.900886', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (3, 'pbkdf2_sha256$1200000$6C00nalPBU6wPPwGGFnBtm$iO5I6oTEm/ibf2znTb6PKVWIHLOTzR7U+kvJ3T3724o=', '2026-02-07 05:09:35.022816', FALSE, 'Maria Jolly', 'maria@gmail.com', '9447568542', 'household', TRUE, TRUE, FALSE, '2025-12-28 04:56:23.335834', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (4, 'pbkdf2_sha256$1200000$xpGcF901fXJckIRTfrfn6o$eIUOJBaz1wwbdYNiJmUKRebtJEixDFI4NqU6kP93Trk=', '2026-02-07 05:10:40.200623', FALSE, 'Henna Maria Jiju', 'henna@gmail.com', '9685457512', 'household', TRUE, TRUE, FALSE, '2025-12-28 04:57:20.780667', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (5, 'pbkdf2_sha256$1200000$U058kJLTb8IaV1B2arKVsv$XyKBcR7BFrJojtjxpmrLuGkZIuglwMKTI9MJPU5RZRo=', '2026-02-07 05:11:49.208045', FALSE, 'Joseph Sojan', 'joseph@gmail.com', '9685214152', 'household', TRUE, TRUE, FALSE, '2025-12-28 04:58:25.870305', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (6, 'pbkdf2_sha256$1200000$z8PDPZqTRcpsBhygu2KJDJ$c4x0DA6NbK+2Fr8jC28md4fZCBlM7zb1lK+qbHGGMAM=', '2026-02-07 05:13:15.749867', FALSE, 'Nebin Reji', 'nebin@gmail.com', '9652634512', 'household', TRUE, TRUE, FALSE, '2025-12-29 02:29:02.978122', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (7, 'pbkdf2_sha256$1200000$YTG1GIJDV0pbHFWrpy20nP$6s4rxpe17jkmbvMG/u5+gO2OtniYK4ljXoq37X298rE=', '2026-02-07 05:14:19.061580', FALSE, 'Rohit P Rajeev', 'rohit@gmail.com', '8574859615', 'household', TRUE, TRUE, FALSE, '2025-12-29 02:32:33.245530', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (8, 'pbkdf2_sha256$1200000$fAYYO6KdUsRam0SvktMNWf$+UVHh5RaGpb9hriVAOsOSnQtaxpbHdu5x2TAfIia/P8=', '2026-02-07 05:15:52.515708', FALSE, 'Joju Sibi', 'joju@gmail.com', '8574561252', 'household', TRUE, TRUE, FALSE, '2025-12-29 02:50:31.353746', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (9, 'pbkdf2_sha256$1200000$9ShpyntqMvi9t24DvkQx3R$5ST5klY7YAkK5T6IXBlFla2ClTgjxryu+4nRE68kekA=', '2026-02-07 05:17:00.175359', FALSE, 'Jishin Aji', 'jishin@gmail.com', '8574859615', 'household', TRUE, TRUE, FALSE, '2025-12-29 04:25:24.378394', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (10, 'pbkdf2_sha256$1200000$NyUN88IL7UFJ3Ij6Nmun8u$XF+yoSOFwy6+A0zWVOIw3P+V2060fOhNEmioxKX+IVM=', '2026-02-07 05:17:54.016741', FALSE, 'Vishnu P G', 'vishnu@gmail.com', '7458965675', 'household', TRUE, TRUE, FALSE, '2025-12-29 05:56:50.660428', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (11, 'pbkdf2_sha256$1200000$WMcsEBz7nHWHXNxG07tjWm$YFZJAwLbeakZJqE62/a2MNpTr9Txx9wW3pR4Jn/kOlI=', '2026-02-07 05:18:43.948526', FALSE, 'Abin Joy', 'abin@gmail.com', '9874124222', 'household', TRUE, TRUE, FALSE, '2025-12-29 05:58:27.463103', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (12, 'pbkdf2_sha256$1200000$mnN6JMaSAdxopjMhPbpKgy$8CCigYGqyZdYHU1XLPT2M6CjZDBVJE6Td6E/riE7a+E=', '2026-02-07 05:19:36.643907', FALSE, 'Sani Tomy', 'sani@gmail.com', '9685745125', 'household', TRUE, TRUE, FALSE, '2025-12-29 06:00:21.628529', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (13, 'pbkdf2_sha256$1200000$vlQeoGcW55yQdKS9QL1kbz$m2DmInt+dp7eeorDUZPQZ3oFM6XOdTaDXDCONpJB4Wg=', '2026-02-07 05:20:28.486859', FALSE, 'Mejo John', 'mejo@gmail.com', '9685854156', 'household', TRUE, TRUE, FALSE, '2025-12-29 06:01:15.426499', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (14, 'pbkdf2_sha256$1200000$jnj3jUwHJhyfiplnGOXaHD$RMKguQjgjJak0O6WC6kqQ3XpZAp5s/wj06QosWTeI0E=', '2026-02-07 05:21:23.049105', FALSE, 'Antony Jose', 'antonyjose@gmail.com', '7451531312', 'household', TRUE, TRUE, FALSE, '2025-12-29 06:02:26.773984', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (15, 'pbkdf2_sha256$1200000$wiRlT9VWMO2jueBxN30DGu$f85/WLGnU/tpD01mpYk6f9HX8JzVctkQ28HobZG2Udo=', '2026-02-07 05:22:27.617058', FALSE, 'Ashin Aji', 'ashin@gmail.com', '9788578554', 'collector', TRUE, TRUE, FALSE, '2025-12-29 06:51:16.104682', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (16, 'pbkdf2_sha256$1200000$XW9zRKMNfk4LIM2s3iP0lf$Kf0vDAG9dzhkOBsw//1COederMQzWMldrd6rarBz+cA=', '2026-02-07 05:35:26.309811', FALSE, 'Nikhil Biby', 'nikhil@gmail.com', '9685745125', 'collector', TRUE, TRUE, FALSE, '2025-12-30 05:08:01.755887', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (17, 'pbkdf2_sha256$1200000$K3bWX3sXaOsDil6EGHwY32$STvB+hqwLNSi9l//f0nrWss8dEPQgKlC7plBmaOtvZw=', '2026-02-07 05:37:09.584596', FALSE, 'Nikitha Biby', 'nikitha@gmail.com', '8585745968', 'collector', TRUE, TRUE, FALSE, '2025-12-30 05:09:26.180019', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (18, 'pbkdf2_sha256$1200000$4YMyY1KAqnxhdPRUwz2ztb$phZklJ+Z2XSaV9fM374pJ5WKNUIIpyFTzJsgzlKDaXQ=', '2026-02-07 05:38:27.518141', FALSE, 'Jobin Jose', 'jobin@gmail.com', '9685748574', 'collector', TRUE, TRUE, FALSE, '2025-12-30 05:14:46.961708', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (19, 'pbkdf2_sha256$1200000$MV2rG31fEo31s0u7bc2P0p$/IeCyZzwng014EhE/wQbv4dBGqPFvS3vz1vTIlcCeIA=', '2026-02-07 05:39:13.524412', FALSE, 'Aashish Shoby', 'aashish@gmail.com', '9685857487', 'collector', TRUE, TRUE, FALSE, '2025-12-30 05:16:21.609354', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (20, 'pbkdf2_sha256$1200000$adWz5XyQDDMXqyZPPQQHrc$ZJn9WQZa/S3MOSKPDKJH2N32IjpLa+8/Pj6jpzipq8I=', '2026-02-07 06:01:26.043011', FALSE, 'Jacob Suni', 'jacob@gmail.com', '9685214152', 'collector', TRUE, TRUE, FALSE, '2025-12-30 05:46:35.774110', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (21, 'pbkdf2_sha256$1200000$GunCaWuz1jXONYwxs7RtcN$S3/IS6MrdsXcr9OJA+sgkSqUri9l4mtzJAiD+yQI2Ws=', '2026-02-07 05:49:46.012947', FALSE, 'Mathew Jolly', 'mathewjollyavj11@gmail.com', '9685748596', 'farmer', TRUE, TRUE, FALSE, '2025-12-31 09:23:42.161926', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (22, 'pbkdf2_sha256$1200000$eYXrCyHacMlk1yEBn9aZSd$pcuOV+HxS7s5zFy4N3IsRrfMp2QDFe9xtvaomf+39Lg=', '2026-01-21 16:16:00.061241', FALSE, 'Edwin Jose', 'edwin@gmail.com', '9685748578', 'farmer', TRUE, TRUE, FALSE, '2025-12-31 09:26:54.401725', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (23, 'pbkdf2_sha256$1000000$9Zakrd3zboGEyrpwSeYQQx$AIWKcNmrph6JFocOK2jB9h5qM+shDV97YQRN3n4V3gY=', '2026-01-22 04:18:51.184116', FALSE, 'Jeevan Johnson', 'jeevan@gmail.com', '9685748574', 'farmer', TRUE, TRUE, FALSE, '2025-12-31 09:30:38.615286', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (25, 'pbkdf2_sha256$1200000$x9hOef6pdmGaoHlST8qOiB$KBZg0whI/U5/B+Y73SVp3iQJLm1zHdt/1gC1uNoJ97A=', '2026-02-07 05:58:15.269377', FALSE, 'Jees Johnson', 'mathewiqoocam1@gmail.com', '9685747474', 'farmer', TRUE, TRUE, FALSE, '2025-12-31 10:44:26.727897', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (26, 'pbkdf2_sha256$1000000$1Nit1ZhNBpAupAgllQfM2q$lRo2BWBZUIuk+FMG+LUyDxhK2HWPyAEeev+gJtKA5q0=', '2026-01-21 18:01:47.125747', FALSE, 'Soorya Sunil', 'soorya@gmail.com', '9685441412', 'compost_manager', TRUE, TRUE, FALSE, '2025-12-31 15:50:45.033615', 'Approved');
INSERT INTO "GuestApp_customuser" ("id", "password", "last_login", "is_superuser", "name", "email", "phone", "role", "is_verified", "is_active", "is_staff", "date_joined", "account_status") VALUES (27, 'pbkdf2_sha256$1200000$kfWdEKfqyoPdIdN4TPXoiz$Zt3xEytbF3mR0tVXCnLTQ5E1100w6KFhfSPBpZoFVWA=', '2026-02-07 05:50:51.558070', FALSE, 'Gibin Jose', 'gibin@gmail.com', '9685748596', 'compost_manager', TRUE, TRUE, FALSE, '2026-01-02 10:38:11.772618', 'Approved');

DROP TABLE IF EXISTS "GuestApp_customuser_groups" CASCADE;
CREATE TABLE "GuestApp_customuser_groups" (
  "id" SERIAL,
  "customuser_id" BIGINT NOT NULL,
  "group_id" INTEGER NOT NULL,
  CONSTRAINT "guestapp_customuser_groups_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_customuser_groups_GuestApp_customuser_groups_customuser_id_group_id_b8e157fc_uniq_unique" UNIQUE ("customuser_id","group_id")
);

DROP TABLE IF EXISTS "GuestApp_customuser_user_permissions" CASCADE;
CREATE TABLE "GuestApp_customuser_user_permissions" (
  "id" SERIAL,
  "customuser_id" BIGINT NOT NULL,
  "permission_id" INTEGER NOT NULL,
  CONSTRAINT "guestapp_customuser_user_permissions_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_customuser_user_permissions_GuestApp_customuser_user_customuser_id_permission_b6ac8a60_uniq_unique" UNIQUE ("customuser_id","permission_id")
);

DROP TABLE IF EXISTS "GuestApp_farmer" CASCADE;
CREATE TABLE "GuestApp_farmer" (
  "id" BIGSERIAL,
  "farmer_name" VARCHAR(100) NOT NULL,
  "aadhaar_image" VARCHAR(100) NOT NULL,
  "phone" VARCHAR(15) NOT NULL,
  "address" TEXT NOT NULL,
  "is_active" BOOLEAN NOT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "guestapp_farmer_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_farmer_user_id_unique" UNIQUE ("user_id")
);
INSERT INTO "GuestApp_farmer" ("id", "farmer_name", "aadhaar_image", "phone", "address", "is_active", "user_id") VALUES (1, 'Mathew Jolly', 'farmer_aadhaar_images/license2.jpg', '9685748596', 'Thodupuzha', TRUE, 21);
INSERT INTO "GuestApp_farmer" ("id", "farmer_name", "aadhaar_image", "phone", "address", "is_active", "user_id") VALUES (2, 'Edwin Jose', 'farmer_aadhaar_images/mary_VpMRm9x.png', '9685748578', 'Thodupuzha', TRUE, 22);
INSERT INTO "GuestApp_farmer" ("id", "farmer_name", "aadhaar_image", "phone", "address", "is_active", "user_id") VALUES (3, 'Jeevan Johnson', 'farmer_aadhaar_images/license2_RIHUUKv.jpg', '9685748574', 'Thodpuzha', TRUE, 23);
INSERT INTO "GuestApp_farmer" ("id", "farmer_name", "aadhaar_image", "phone", "address", "is_active", "user_id") VALUES (5, 'Jees Johnson', 'farmer_aadhaar_images/license3.jpg', '9685747474', 'tdpa', TRUE, 25);

DROP TABLE IF EXISTS "GuestApp_household" CASCADE;
CREATE TABLE "GuestApp_household" (
  "id" BIGSERIAL,
  "household_name" VARCHAR(100) NOT NULL,
  "phone" VARCHAR(15) NOT NULL,
  "address" TEXT NOT NULL,
  "aadhaar_image" VARCHAR(100) NOT NULL,
  "house_no" INTEGER DEFAULT NULL,
  "registered_on" TIMESTAMP(6) NOT NULL,
  "district_id" INTEGER NOT NULL,
  "location_id" INTEGER NOT NULL,
  "residents_association_id" INTEGER NOT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "guestapp_household_pk" PRIMARY KEY ("id"),
  CONSTRAINT "GuestApp_household_user_id_unique" UNIQUE ("user_id")
);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (1, 'Sonit Jolly', '9447984821', 'Anachalil ,\r\nMariyilaklunku,\r\nThodupuzha', 'household_aadhaar_images/insurance_NJG9fPa.avif', 1, '2025-12-28 04:52:33.901382', 1, 1, 1, 2);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (2, 'Maria Jolly', '9447568542', 'Anachalil\r\nthodupuzha', 'household_aadhaar_images/license3.jpg', 1, '2025-12-28 04:56:23.336330', 1, 1, 2, 3);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (3, 'Henna Maria Jiju', '9685457512', 'Vannapuram,\r\nThodupuzha', 'household_aadhaar_images/licence.png', 1, '2025-12-28 04:57:20.781143', 1, 1, 3, 4);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (4, 'Joseph Sojan', '9685214152', 'Karimkunnam,\r\nThodupuzha', 'household_aadhaar_images/license3_jvHcc2o.jpg', 2, '2025-12-28 04:58:25.870897', 1, 1, 1, 5);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (5, 'Nebin Reji', '9652634512', 'Vazhakulam,\r\nMuvattupuzha', 'household_aadhaar_images/licence_wIL0IMI.png', 1, '2025-12-29 02:29:02.981404', 1, 1, 3, 6);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (6, 'Rohit P Rajeev', '8574859615', 'Karimkunnam \r\nThodupuzha', 'household_aadhaar_images/license3_Ads7qjG.jpg', 2, '2025-12-29 02:32:33.248058', 1, 1, 3, 7);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (7, 'Joju Sibi', '8574561252', 'Muthalakodam po', 'household_aadhaar_images/licence_luLyVXh.png', 3, '2025-12-29 02:50:31.354297', 1, 1, 3, 8);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (8, 'Jishin Aji', '8574859615', 'Chunkom,\r\nThodupuzha', 'household_aadhaar_images/license2_THWHdQt.jpg', 4, '2025-12-29 04:25:24.378918', 1, 1, 3, 9);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (9, 'Vishnu P G', '7458965675', 'Udumbanoor,\r\nThodupuzha', '', 3, '2025-12-29 05:56:50.660997', 1, 1, 1, 10);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (10, 'Abin Joy', '9874124222', 'Olamattom,\r\nThodupuzha', 'household_aadhaar_images/license1.jpg', 4, '2025-12-29 05:58:27.463461', 1, 1, 1, 11);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (11, 'Sani Tomy', '9685745125', 'AnaKudiyil,\r\nThodupuzha', 'household_aadhaar_images/license2_3Dt2URY.jpg', 2, '2025-12-29 06:00:21.628866', 1, 1, 2, 12);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (12, 'Mejo John', '9685854156', 'Thodupuzha', 'household_aadhaar_images/john.png', 3, '2025-12-29 06:01:15.426936', 1, 1, 2, 13);
INSERT INTO "GuestApp_household" ("id", "household_name", "phone", "address", "aadhaar_image", "house_no", "registered_on", "district_id", "location_id", "residents_association_id", "user_id") VALUES (13, 'Antony Jose', '7451531312', 'Mutoom,\r\nThodupuzha', 'household_aadhaar_images/license1_WwjV1fJ.jpg', 4, '2025-12-29 06:02:26.774375', 1, 1, 2, 14);

DROP TABLE IF EXISTS "GuestApp_passwordresetotp" CASCADE;
CREATE TABLE "GuestApp_passwordresetotp" (
  "id" BIGSERIAL,
  "otp_code" VARCHAR(6) NOT NULL,
  "created_at" TIMESTAMP(6) NOT NULL,
  "expires_at" TIMESTAMP(6) NOT NULL,
  "is_used" BOOLEAN NOT NULL,
  "user_id" BIGINT NOT NULL,
  CONSTRAINT "guestapp_passwordresetotp_pk" PRIMARY KEY ("id")
);
INSERT INTO "GuestApp_passwordresetotp" ("id", "otp_code", "created_at", "expires_at", "is_used", "user_id") VALUES (26, '975906', '2026-02-06 07:30:42.116075', '2026-02-06 07:35:42.106064', TRUE, 21);

DROP TABLE IF EXISTS "MyApp_systemsettings" CASCADE;
CREATE TABLE "MyApp_systemsettings" (
  "setting_key" VARCHAR(100) NOT NULL,
  "setting_value" VARCHAR(255) NOT NULL,
  "description" TEXT NOT NULL,
  "last_updated" TIMESTAMP(6) NOT NULL,
  CONSTRAINT "myapp_systemsettings_pk" PRIMARY KEY ("setting_key")
);
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('compost_conversion_ratio', '4', 'Waste to compost conversion ratio (kg waste per 1kg compost)', '2026-02-07 05:45:01.297723');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('low_stock_threshold', '50', 'Low stock warning threshold in kg', '2026-02-07 05:45:01.299938');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('expiry_warning_days', '7', 'Days before expiry to show warning', '2026-02-07 05:45:01.303722');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('auto_unavailable_days', '30', 'Days after which waste is automatically marked unavailable', '2026-02-07 05:45:01.309304');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('waste_price_per_kg', '10.00', 'Default price for waste sold to farmers per kilogram (in ₹)', '2026-02-07 05:45:01.311345');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('auto_assign_collectors', 'true', 'Automatically assign collectors to farmer waste orders based on day rotation', '2026-02-07 05:59:52.367178');
INSERT INTO "MyApp_systemsettings" ("setting_key", "setting_value", "description", "last_updated") VALUES ('email_notifications_enabled', 'False', 'Master switch to enable/disable all system emails', '2026-02-07 05:45:01.313184');

DROP TABLE IF EXISTS "MyApp_tbl_bintype" CASCADE;
CREATE TABLE "MyApp_tbl_bintype" (
  "BinType_id" SERIAL,
  "name" VARCHAR(50) NOT NULL,
  "capacity_kg" INTEGER NOT NULL,
  "price_rs" DECIMAL(10,2) NOT NULL,
  CONSTRAINT "myapp_tbl_bintype_pk" PRIMARY KEY ("BinType_id")
);
INSERT INTO "MyApp_tbl_bintype" ("BinType_id", "name", "capacity_kg", "price_rs") VALUES (3, 'Large', 50, 100.00);
INSERT INTO "MyApp_tbl_bintype" ("BinType_id", "name", "capacity_kg", "price_rs") VALUES (4, 'Medium', 25, 50.00);

DROP TABLE IF EXISTS "MyApp_tbl_collectionrequest" CASCADE;
CREATE TABLE "MyApp_tbl_collectionrequest" (
  "Request_id" SERIAL,
  "total_quantity_kg" DECIMAL(10,2) NOT NULL,
  "farmer_supply_kg" DECIMAL(10,2) NOT NULL,
  "leftover_compost_kg" DECIMAL(10,2) NOT NULL,
  "collection_date" TIMESTAMP(6) NOT NULL,
  "status" VARCHAR(50) NOT NULL,
  "collector_id" BIGINT NOT NULL,
  "household_id" BIGINT NOT NULL,
  CONSTRAINT "myapp_tbl_collectionrequest_pk" PRIMARY KEY ("Request_id")
);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (1, 48.00, 0.00, 0.00, '2025-12-31 09:07:23.916363', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (2, 49.00, 0.00, 0.00, '2025-12-31 09:07:30.081012', 'Collected', 1, 4);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (3, 40.00, 0.00, 0.00, '2025-12-31 09:09:25.813626', 'Collected', 2, 9);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (4, 50.00, 0.00, 0.00, '2025-12-31 09:11:58.438694', 'Collected', 2, 10);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (45, 50.00, 0.00, 0.00, '2026-01-21 16:05:36.400295', 'Collected', 5, 6);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (44, 50.00, 0.00, 0.00, '2026-01-21 16:05:14.655077', 'Collected', 5, 5);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (43, 50.00, 0.00, 0.00, '2026-01-21 16:04:57.211333', 'Collected', 5, 3);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (8, 50.00, 0.00, 0.00, '2025-12-31 09:14:48.895765', 'Collected', 4, 12);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (9, 50.00, 0.00, 0.00, '2025-12-31 09:15:18.585838', 'Collected', 5, 3);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (10, 50.00, 0.00, 0.00, '2025-12-31 09:15:24.673930', 'Collected', 5, 5);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (11, 23.00, 0.00, 0.00, '2025-12-31 09:15:32.074356', 'Collected', 5, 6);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (12, 50.00, 0.00, 0.00, '2025-12-31 09:16:04.066382', 'Collected', 6, 7);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (13, 50.00, 0.00, 0.00, '2025-12-31 09:16:09.888448', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (14, 50.00, 0.00, 0.00, '2026-01-01 04:05:17.587461', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (15, 50.00, 0.00, 0.00, '2026-01-01 04:05:27.155606', 'Collected', 1, 4);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (16, 50.00, 0.00, 0.00, '2026-01-01 04:08:33.047362', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (17, 45.00, 0.00, 0.00, '2026-01-01 04:09:46.160936', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (18, 50.00, 0.00, 0.00, '2026-01-01 04:10:59.509289', 'Collected', 5, 3);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (19, 25.00, 0.00, 0.00, '2026-01-02 09:53:19.057453', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (20, 50.00, 0.00, 0.00, '2026-01-02 09:53:37.511774', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (21, 50.00, 0.00, 0.00, '2026-01-04 14:10:32.515769', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (22, 50.00, 0.00, 0.00, '2026-01-12 10:53:32.287848', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (23, 50.00, 0.00, 0.00, '2026-01-12 10:53:47.855968', 'Collected', 6, 7);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (24, 50.00, 0.00, 0.00, '2026-01-12 10:54:21.988081', 'Collected', 5, 6);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (25, 50.00, 0.00, 0.00, '2026-01-12 10:55:29.034770', 'Collected', 4, 13);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (26, 25.00, 0.00, 0.00, '2026-01-12 10:55:43.626330', 'Collected', 4, 12);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (27, 50.00, 0.00, 0.00, '2026-01-12 10:56:13.667026', 'Collected', 3, 2);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (28, 50.00, 0.00, 0.00, '2026-01-12 10:56:31.812585', 'Collected', 3, 11);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (29, 50.00, 0.00, 0.00, '2026-01-12 10:57:10.559325', 'Collected', 2, 10);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (30, 24.00, 0.00, 0.00, '2026-01-12 10:57:25.427554', 'Collected', 2, 9);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (31, 50.00, 0.00, 0.00, '2026-01-17 09:20:57.197559', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (32, 25.00, 0.00, 0.00, '2026-01-17 09:23:30.630218', 'Collected', 1, 4);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (33, 25.00, 0.00, 0.00, '2026-01-17 09:29:22.930993', 'Collected', 2, 9);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (34, 50.00, 0.00, 0.00, '2026-01-17 09:34:10.699451', 'Collected', 2, 10);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (35, 25.00, 0.00, 0.00, '2026-01-17 09:38:09.586289', 'Collected', 3, 2);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (36, 40.00, 0.00, 0.00, '2026-01-21 15:04:48.742572', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (37, 50.00, 0.00, 0.00, '2026-01-21 15:12:34.828865', 'Collected', 1, 4);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (38, 50.00, 0.00, 0.00, '2026-01-21 15:21:25.189327', 'Collected', 2, 10);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (39, 25.00, 0.00, 0.00, '2026-01-21 15:24:22.105569', 'Collected', 2, 9);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (40, 25.00, 0.00, 0.00, '2026-01-21 15:27:52.182509', 'Collected', 3, 11);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (41, 25.00, 0.00, 0.00, '2026-01-21 15:29:11.736189', 'Collected', 3, 2);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (42, 50.00, 0.00, 0.00, '2026-01-21 15:48:39.075034', 'Collected', 3, 11);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (46, 50.00, 0.00, 0.00, '2026-01-21 16:05:51.070563', 'Collected', 5, 3);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (47, 50.00, 0.00, 0.00, '2026-01-21 16:06:07.422923', 'Collected', 5, 5);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (48, 25.00, 0.00, 0.00, '2026-01-21 16:06:25.937591', 'Collected', 5, 6);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (49, 50.00, 0.00, 0.00, '2026-01-21 16:07:39.786337', 'Collected', 6, 7);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (50, 50.00, 0.00, 0.00, '2026-01-21 16:07:53.451006', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (51, 50.00, 0.00, 0.00, '2026-01-21 16:08:09.154599', 'Collected', 6, 7);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (52, 50.00, 0.00, 0.00, '2026-01-21 16:13:22.596142', 'Collected', 6, 8);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (53, 50.00, 0.00, 0.00, '2026-01-21 17:16:02.992783', 'Collected', 4, 12);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (54, 50.00, 0.00, 0.00, '2026-01-21 17:16:16.494750', 'Collected', 4, 13);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (55, 50.00, 0.00, 0.00, '2026-01-21 17:16:26.909577', 'Collected', 4, 12);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (56, 50.00, 0.00, 0.00, '2026-01-21 17:16:36.955865', 'Collected', 4, 13);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (57, 50.00, 0.00, 0.00, '2026-01-22 04:18:04.890195', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (58, 50.00, 0.00, 0.00, '2026-01-22 04:27:38.678120', 'Collected', 3, 2);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (59, 50.00, 0.00, 0.00, '2026-01-24 13:22:55.838151', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (60, 50.00, 0.00, 0.00, '2026-02-07 05:22:38.626556', 'Collected', 1, 1);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (61, 50.00, 0.00, 0.00, '2026-02-07 05:34:50.261750', 'Collected', 1, 4);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (62, 50.00, 0.00, 0.00, '2026-02-07 05:35:37.341223', 'Collected', 2, 9);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (63, 50.00, 0.00, 0.00, '2026-02-07 05:36:45.771642', 'Collected', 2, 10);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (64, 50.00, 0.00, 0.00, '2026-02-07 05:37:19.773085', 'Collected', 3, 2);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (65, 50.00, 0.00, 0.00, '2026-02-07 05:37:44.581304', 'Collected', 3, 11);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (66, 50.00, 0.00, 0.00, '2026-02-07 05:38:37.769267', 'Collected', 4, 12);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (67, 50.00, 0.00, 0.00, '2026-02-07 05:38:49.248971', 'Collected', 4, 13);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (68, 25.00, 0.00, 0.00, '2026-02-07 05:39:27.212161', 'Collected', 5, 3);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (69, 50.00, 0.00, 0.00, '2026-02-07 05:39:38.272269', 'Collected', 5, 5);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (70, 50.00, 0.00, 0.00, '2026-02-07 05:39:48.318050', 'Collected', 5, 6);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (71, 50.00, 0.00, 0.00, '2026-02-07 05:40:17.888691', 'Collected', 6, 7);
INSERT INTO "MyApp_tbl_collectionrequest" ("Request_id", "total_quantity_kg", "farmer_supply_kg", "leftover_compost_kg", "collection_date", "status", "collector_id", "household_id") VALUES (72, 50.00, 0.00, 0.00, '2026-02-07 05:40:33.518086', 'Collected', 6, 8);

DROP TABLE IF EXISTS "MyApp_tbl_collectorassignment" CASCADE;
CREATE TABLE "MyApp_tbl_collectorassignment" (
  "Assign_id" SERIAL,
  "day_of_week" VARCHAR(50) NOT NULL,
  "collector_id" BIGINT NOT NULL,
  "Route_id_id" INTEGER NOT NULL,
  CONSTRAINT "myapp_tbl_collectorassignment_pk" PRIMARY KEY ("Assign_id"),
  CONSTRAINT "MyApp_tbl_collectorassignment_MyApp_tbl_collectorassig_collector_id_Route_id_id_a755187b_uniq_unique" UNIQUE ("collector_id","Route_id_id","day_of_week")
);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (1, 'Monday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (2, 'Tuesday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (3, 'Wednesday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (4, 'Thursday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (5, 'Friday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (6, 'Saturday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (7, 'Sunday', 1, 1);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (8, 'Monday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (9, 'Tuesday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (10, 'Wednesday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (11, 'Thursday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (12, 'Friday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (13, 'Saturday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (14, 'Sunday', 2, 2);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (15, 'Monday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (16, 'Tuesday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (17, 'Wednesday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (18, 'Thursday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (19, 'Friday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (20, 'Saturday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (21, 'Sunday', 3, 3);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (45, 'Wednesday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (46, 'Thursday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (47, 'Friday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (44, 'Tuesday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (43, 'Monday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (52, 'Wednesday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (53, 'Thursday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (54, 'Friday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (50, 'Monday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (51, 'Tuesday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (62, 'Saturday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (61, 'Friday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (60, 'Thursday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (59, 'Wednesday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (57, 'Monday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (58, 'Tuesday', 6, 6);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (48, 'Saturday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (49, 'Sunday', 4, 4);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (55, 'Saturday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (56, 'Sunday', 5, 5);
INSERT INTO "MyApp_tbl_collectorassignment" ("Assign_id", "day_of_week", "collector_id", "Route_id_id") VALUES (63, 'Sunday', 6, 6);

DROP TABLE IF EXISTS "MyApp_tbl_compostbatch" CASCADE;
CREATE TABLE "MyApp_tbl_compostbatch" (
  "Batch_id" SERIAL,
  "Batch_name" VARCHAR(100) NOT NULL,
  "Source_Waste_kg" DECIMAL(10,2) NOT NULL,
  "Date_Created" DATE NOT NULL,
  "Status" VARCHAR(20) NOT NULL,
  "Grade" VARCHAR(20) NOT NULL,
  "Stock_kg" DECIMAL(10,2) NOT NULL,
  "price_per_kg" DECIMAL(10,2) NOT NULL,
  "CompostManager_id_id" BIGINT NOT NULL,
  "salary_paid" BOOLEAN NOT NULL,
  CONSTRAINT "myapp_tbl_compostbatch_pk" PRIMARY KEY ("Batch_id")
);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (1, 'AA', 160.00, '2025-12-31', 'Sold', 'A', 0.00, 200.00, 1, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (2, 'BB', 245.00, '2026-01-01', 'Sold', 'A', 0.00, 200.00, 1, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (3, 'rr', 75.00, '2026-01-02', 'Sold', 'A', 0.00, 200.00, 2, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (4, 'CC', 50.00, '2026-01-04', 'Sold', 'A', 0.00, 200.00, 2, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (5, 'cv', 49.00, '2026-01-12', 'Sold', 'Premium', 0.00, 200.00, 2, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (6, 'SS', 175.00, '2026-01-20', 'Sold', 'A', 0.00, 200.00, 1, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (7, 'dddj', 325.00, '2026-01-21', 'Sold', 'Premium', 0.00, 200.00, 2, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (8, 'xbxcbx', 375.00, '2026-01-21', 'Sold', 'A', 0.00, 200.00, 1, TRUE);
INSERT INTO "MyApp_tbl_compostbatch" ("Batch_id", "Batch_name", "Source_Waste_kg", "Date_Created", "Status", "Grade", "Stock_kg", "price_per_kg", "CompostManager_id_id", "salary_paid") VALUES (9, 'DDD', 685.00, '2026-02-07', 'Ready', 'A', 0.75, 200.00, 2, TRUE);

DROP TABLE IF EXISTS "MyApp_tbl_district" CASCADE;
CREATE TABLE "MyApp_tbl_district" (
  "District_id" SERIAL,
  "District_Name" VARCHAR(100) NOT NULL,
  CONSTRAINT "myapp_tbl_district_pk" PRIMARY KEY ("District_id")
);
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (1, 'Idukki');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (2, 'Kasaragod');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (3, 'Kannur');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (4, 'Wayanad');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (5, 'Kozhikode');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (6, 'Malappuram');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (7, 'Palakkad');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (8, 'Thrissur');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (9, 'Ernakulam');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (10, 'Kottayam');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (11, 'Alappuzha');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (12, 'Pathanamthitta');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (13, 'Kollam');
INSERT INTO "MyApp_tbl_district" ("District_id", "District_Name") VALUES (14, 'Thiruvananthapuram');

DROP TABLE IF EXISTS "MyApp_tbl_farmersupply" CASCADE;
CREATE TABLE "MyApp_tbl_farmersupply" (
  "Supply_id" SERIAL,
  "Quantity" DECIMAL(10,2) NOT NULL,
  "Supply_Date" TIMESTAMP(6) NOT NULL,
  "unit_price" DECIMAL(10,2) NOT NULL,
  "total_amount" DECIMAL(10,2) NOT NULL,
  "payment_status" VARCHAR(20) NOT NULL,
  "delivery_address" TEXT NOT NULL,
  "delivery_status" VARCHAR(20) NOT NULL,
  "Collection_id_id" INTEGER DEFAULT NULL,
  "Farmer_id_id" BIGINT NOT NULL,
  "Payment_id_id" INTEGER DEFAULT NULL,
  CONSTRAINT "myapp_tbl_farmersupply_pk" PRIMARY KEY ("Supply_id")
);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (9, 200.00, '2025-12-31 15:56:48.650340', 10.00, 2000.00, 'Paid', 'Thodupuzha', 'Delivered', 2, 2, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (8, 100.00, '2025-12-31 15:47:05.280953', 10.00, 1000.00, 'Paid', 'Thodupuzha', 'Delivered', 2, 1, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (10, 200.00, '2026-01-12 11:43:03.926101', 10.00, 2000.00, 'Paid', 'Thodpuzha', 'Delivered', NULL, 3, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (11, 150.00, '2026-01-12 11:43:12.223717', 10.00, 1500.00, 'Paid', 'tdpa', 'Delivered', NULL, 5, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (12, 50.00, '2026-01-21 16:14:39.150618', 10.00, 500.00, 'Paid', 'Thodupuzha', 'Delivered', NULL, 1, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (13, 70.00, '2026-01-21 16:16:31.195561', 10.00, 700.00, 'Paid', 'Thodupuzha', 'Delivered', NULL, 2, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (14, 120.00, '2026-01-21 16:25:23.471365', 10.00, 1200.00, 'Paid', 'Thodpuzha', 'Delivered', NULL, 3, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (15, 50.00, '2026-01-22 04:23:30.128896', 10.00, 500.00, 'Paid', 'Thodpuzha', 'Delivered', 26, 3, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (16, 20.00, '2026-01-22 04:28:13.193739', 10.00, 200.00, 'Paid', 'Thodupuzha', 'Delivered', 26, 1, NULL);
INSERT INTO "MyApp_tbl_farmersupply" ("Supply_id", "Quantity", "Supply_Date", "unit_price", "total_amount", "payment_status", "delivery_address", "delivery_status", "Collection_id_id", "Farmer_id_id", "Payment_id_id") VALUES (17, 20.00, '2026-02-07 05:59:56.554040', 10.00, 200.00, 'Paid', 'Thodupuzha', 'Delivered', 23, 1, NULL);

DROP TABLE IF EXISTS "MyApp_tbl_householdpayment" CASCADE;
CREATE TABLE "MyApp_tbl_householdpayment" (
  "Payment_id" SERIAL,
  "amount" DECIMAL(10,2) NOT NULL,
  "payment_date" TIMESTAMP(6) NOT NULL,
  "payment_for_date" DATE NOT NULL,
  "status" VARCHAR(20) NOT NULL,
  "transaction_id" VARCHAR(100) DEFAULT NULL,
  "bin_type_id" INTEGER NOT NULL,
  "household_id" BIGINT NOT NULL,
  CONSTRAINT "myapp_tbl_householdpayment_pk" PRIMARY KEY ("Payment_id")
);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (19, 100.00, '2026-01-01 03:05:19.908773', '2026-01-01', 'Completed', 'TXN1767236719395', 3, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (18, 100.00, '2026-01-01 02:59:39.894525', '2026-01-01', 'Completed', 'TXN1767236379100', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (3, 100.00, '2025-12-30 07:00:05.949606', '2025-12-30', 'Completed', 'TXN1767078005505', 3, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (4, 100.00, '2025-12-31 08:39:14.985835', '2025-12-31', 'Completed', 'TXN1767170354680', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (5, 100.00, '2025-12-31 08:40:53.504081', '2025-12-31', 'Completed', 'TXN1767170453915', 3, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (6, 100.00, '2025-12-31 08:42:35.669854', '2025-12-31', 'Completed', 'TXN1767170555501', 3, 3);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (7, 100.00, '2025-12-31 08:43:52.872962', '2025-12-31', 'Completed', 'TXN1767170632898', 3, 4);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (8, 100.00, '2025-12-31 08:45:00.442346', '2025-12-31', 'Completed', 'TXN1767170700830', 3, 5);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (9, 50.00, '2025-12-31 08:46:44.519810', '2025-12-31', 'Completed', 'TXN1767170804191', 4, 6);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (10, 100.00, '2025-12-31 08:47:45.667292', '2025-12-31', 'Completed', 'TXN1767170865958', 3, 7);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (11, 100.00, '2025-12-31 08:48:40.771959', '2025-12-31', 'Completed', 'TXN1767170920755', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (12, 100.00, '2025-12-31 08:49:11.417495', '2026-01-01', 'Completed', 'TXN1767170951296', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (13, 50.00, '2025-12-31 08:49:37.703496', '2026-01-02', 'Completed', 'TXN1767170977410', 4, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (14, 100.00, '2025-12-31 08:50:52.673991', '2025-12-31', 'Completed', 'TXN1767171052280', 3, 9);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (15, 100.00, '2025-12-31 08:53:02.330431', '2025-12-31', 'Completed', 'TXN1767171182520', 3, 10);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (16, 100.00, '2025-12-31 08:54:03.320238', '2025-12-31', 'Completed', 'TXN1767171243947', 3, 11);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (17, 50.00, '2025-12-31 08:55:02.701464', '2025-12-31', 'Completed', 'TXN1767171302776', 4, 12);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (20, 100.00, '2026-01-01 03:55:55.866391', '2026-01-01', 'Completed', 'TXN1767239755315', 3, 3);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (21, 100.00, '2026-01-01 04:04:10.533070', '2026-01-01', 'Completed', 'TXN1767240250379', 3, 4);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (22, 100.00, '2026-01-02 09:41:54.526240', '2026-01-02', 'Completed', 'TXN1767346914734', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (23, 100.00, '2026-01-04 14:06:37.499531', '2026-01-04', 'Completed', 'TXN1767535597325', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (24, 100.00, '2026-01-12 09:33:36.825585', '2026-01-12', 'Completed', 'TXN1768210416162', 3, 13);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (25, 50.00, '2026-01-12 09:36:04.500750', '2026-01-12', 'Completed', 'TXN1768210564587', 4, 12);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (26, 100.00, '2026-01-12 09:38:35.685128', '2026-01-12', 'Completed', 'TXN1768210715230', 3, 11);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (27, 100.00, '2026-01-12 09:41:27.950939', '2026-01-12', 'Completed', 'TXN1768210887977', 3, 10);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (28, 50.00, '2026-01-12 09:46:41.239707', '2026-01-12', 'Completed', 'TXN1768211201379', 4, 9);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (29, 100.00, '2026-01-12 09:48:14.257177', '2026-01-12', 'Completed', 'TXN1768211294740', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (30, 100.00, '2026-01-12 10:51:25.307750', '2026-01-12', 'Completed', 'TXN1768215085686', 3, 6);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (31, 100.00, '2026-01-12 10:52:19.346349', '2026-01-12', 'Completed', 'TXN1768215139951', 3, 7);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (32, 100.00, '2026-01-17 08:59:24.560707', '2026-01-17', 'Completed', 'TXN1768640364800', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (33, 50.00, '2026-01-17 09:02:01.827875', '2026-01-17', 'Completed', 'TXN1768640521814', 4, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (34, 100.00, '2026-01-17 09:03:32.109349', '2026-01-17', 'Completed', 'TXN1768640612412', 3, 3);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (35, 50.00, '2026-01-17 09:05:14.398188', '2026-01-17', 'Completed', 'TXN1768640714179', 4, 4);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (36, 100.00, '2026-01-17 09:07:26.412875', '2026-01-17', 'Completed', 'TXN1768640846601', 3, 5);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (37, 100.00, '2026-01-17 09:08:21.753435', '2026-01-17', 'Completed', 'TXN1768640901974', 3, 6);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (38, 100.00, '2026-01-17 09:10:00.916106', '2026-01-17', 'Completed', 'TXN1768641000531', 3, 7);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (39, 100.00, '2026-01-17 09:11:06.946218', '2026-01-17', 'Completed', 'TXN1768641066345', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (40, 50.00, '2026-01-17 09:12:20.188874', '2026-01-17', 'Completed', 'TXN1768641140177', 4, 9);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (41, 100.00, '2026-01-17 09:13:22.781890', '2026-01-17', 'Completed', 'TXN1768641202883', 3, 10);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (42, 50.00, '2026-01-17 09:14:30.516054', '2026-01-17', 'Completed', 'TXN1768641270593', 4, 11);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (43, 100.00, '2026-01-17 09:18:23.181315', '2026-01-17', 'Completed', 'TXN1768641503653', 3, 12);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (44, 100.00, '2026-01-17 09:19:23.872523', '2026-01-17', 'Completed', 'TXN1768641563298', 3, 13);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (45, 100.00, '2026-01-21 14:52:21.099235', '2026-01-21', 'Completed', 'TXN1769007141716', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (46, 50.00, '2026-01-21 14:53:35.403891', '2026-01-21', 'Completed', 'TXN1769007215456', 4, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (47, 100.00, '2026-01-21 14:54:32.262300', '2026-01-21', 'Completed', 'TXN1769007272244', 3, 3);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (48, 100.00, '2026-01-21 14:55:22.549987', '2026-01-21', 'Completed', 'TXN1769007322412', 3, 4);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (49, 100.00, '2026-01-21 14:56:11.250386', '2026-01-21', 'Completed', 'TXN1769007371846', 3, 5);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (50, 50.00, '2026-01-21 14:56:57.194171', '2026-01-21', 'Completed', 'TXN1769007417546', 4, 6);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (51, 100.00, '2026-01-21 14:58:05.734094', '2026-01-21', 'Completed', 'TXN1769007485939', 3, 7);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (52, 100.00, '2026-01-21 14:58:57.708443', '2026-01-21', 'Completed', 'TXN1769007537362', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (53, 100.00, '2026-01-21 15:00:24.821109', '2026-01-21', 'Completed', 'TXN1769007624823', 3, 10);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (54, 50.00, '2026-01-21 15:01:18.942857', '2026-01-21', 'Completed', 'TXN1769007678398', 4, 9);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (55, 100.00, '2026-01-21 15:02:12.955043', '2026-01-21', 'Completed', 'TXN1769007732483', 3, 11);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (56, 100.00, '2026-01-21 15:03:17.063014', '2026-01-21', 'Completed', 'TXN1769007797615', 3, 12);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (57, 100.00, '2026-01-21 15:04:13.962614', '2026-01-21', 'Completed', 'TXN1769007853817', 3, 13);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (58, 100.00, '2026-01-22 04:17:21.387645', '2026-01-22', 'Completed', 'TXN1769055441632', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (59, 100.00, '2026-01-22 04:26:15.130197', '2026-01-22', 'Completed', 'TXN1769055975510', 3, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (60, 100.00, '2026-01-24 13:21:41.468051', '2026-01-24', 'Completed', 'TXN1769260901459', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (61, 100.00, '2026-02-07 05:08:32.247432', '2026-02-07', 'Completed', 'TXN1770440912123', 3, 1);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (62, 100.00, '2026-02-07 05:10:02.697121', '2026-02-07', 'Completed', 'TXN1770441002583', 3, 2);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (63, 50.00, '2026-02-07 05:11:10.536646', '2026-02-07', 'Completed', 'TXN1770441070421', 4, 3);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (64, 100.00, '2026-02-07 05:12:15.706860', '2026-02-07', 'Completed', 'TXN1770441135130', 3, 4);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (65, 100.00, '2026-02-07 05:13:39.176537', '2026-02-07', 'Completed', 'TXN1770441219646', 3, 5);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (66, 100.00, '2026-02-07 05:14:46.999131', '2026-02-07', 'Completed', 'TXN1770441286638', 3, 6);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (67, 100.00, '2026-02-07 05:16:13.058471', '2026-02-07', 'Completed', 'TXN1770441373664', 3, 7);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (68, 100.00, '2026-02-07 05:17:21.393898', '2026-02-07', 'Completed', 'TXN1770441441651', 3, 8);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (69, 100.00, '2026-02-07 05:18:18.351481', '2026-02-07', 'Completed', 'TXN1770441498768', 3, 9);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (70, 100.00, '2026-02-07 05:19:06.012299', '2026-02-07', 'Completed', 'TXN1770441546525', 3, 10);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (71, 100.00, '2026-02-07 05:19:57.761527', '2026-02-07', 'Completed', 'TXN1770441597370', 3, 11);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (72, 100.00, '2026-02-07 05:20:53.907689', '2026-02-07', 'Completed', 'TXN1770441653534', 3, 12);
INSERT INTO "MyApp_tbl_householdpayment" ("Payment_id", "amount", "payment_date", "payment_for_date", "status", "transaction_id", "bin_type_id", "household_id") VALUES (73, 100.00, '2026-02-07 05:21:47.767784', '2026-02-07', 'Completed', 'TXN1770441707401', 3, 13);

DROP TABLE IF EXISTS "MyApp_tbl_location" CASCADE;
CREATE TABLE "MyApp_tbl_location" (
  "Location_id" SERIAL,
  "Ward_No" INTEGER NOT NULL,
  "Ward_Name" VARCHAR(100) NOT NULL,
  "District_id" INTEGER NOT NULL,
  CONSTRAINT "myapp_tbl_location_pk" PRIMARY KEY ("Location_id")
);
INSERT INTO "MyApp_tbl_location" ("Location_id", "Ward_No", "Ward_Name", "District_id") VALUES (1, 28, 'Arackappara', 1);

DROP TABLE IF EXISTS "MyApp_tbl_order" CASCADE;
CREATE TABLE "MyApp_tbl_order" (
  "Order_id" SERIAL,
  "Order_Date" TIMESTAMP(6) NOT NULL,
  "Total_Amount" DECIMAL(10,2) NOT NULL,
  "Delivery_Address" TEXT NOT NULL,
  "Payment_Status" VARCHAR(20) NOT NULL,
  "Buyer_id_id" BIGINT NOT NULL,
  "assigned_collector_id" BIGINT DEFAULT NULL,
  "assignment_status" VARCHAR(20) NOT NULL,
  CONSTRAINT "myapp_tbl_order_pk" PRIMARY KEY ("Order_id")
);
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (6, '2025-12-31 16:12:32.001622', 7000.00, 'Thodpuzha', 'Paid', 3, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (3, '2025-12-31 15:41:40.120244', 1000.00, 'Thodupuzha', 'Paid', 1, 1, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (5, '2025-12-31 15:56:19.593920', 2000.00, 'Thodupuzha', 'Paid', 2, 1, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (9, '2026-01-01 04:31:12.142049', 9000.00, 'Thodupuzha', 'Paid', 2, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (8, '2026-01-01 04:23:40.482320', 8000.00, 'tdpa', 'Paid', 5, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (10, '2026-01-02 10:40:41.298731', 4200.00, 'Thodupuzha', 'Paid', 2, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (11, '2026-01-12 11:33:04.702873', 1500.00, 'tdpa', 'Paid', 5, 4, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (12, '2026-01-12 11:34:12.400805', 2000.00, 'Thodpuzha', 'Paid', 3, 1, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (13, '2026-01-12 11:37:12.620621', 4800.00, 'Thodupuzha', 'Paid', 1, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (14, '2026-01-20 06:55:38.308359', 4000.00, 'Thodupuzha', 'Paid', 1, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (15, '2026-01-20 07:10:08.875466', 4800.00, 'Thodpuzha', 'Paid', 3, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (16, '2026-01-21 16:14:20.402603', 500.00, 'Thodupuzha', 'Paid', 1, 4, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (17, '2026-01-21 16:16:15.509755', 700.00, 'Thodupuzha', 'Paid', 2, 4, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (18, '2026-01-21 16:18:13.979543', 1200.00, 'Thodpuzha', 'Paid', 3, 4, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (19, '2026-01-21 18:16:03.391225', 35000.00, 'Thodpuzha', 'Paid', 3, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (20, '2026-01-22 04:19:27.549898', 500.00, 'Thodpuzha', 'Paid', 3, 4, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (21, '2026-01-22 04:28:13.000000', 200.00, 'Restored Address', 'Paid', 1, NULL, 'Unassigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (22, '2026-02-07 05:50:23.403791', 200.00, 'Thodupuzha', 'Paid', 1, 6, 'Assigned');
INSERT INTO "MyApp_tbl_order" ("Order_id", "Order_Date", "Total_Amount", "Delivery_Address", "Payment_Status", "Buyer_id_id", "assigned_collector_id", "assignment_status") VALUES (23, '2026-02-07 05:58:35.762884', 34200.00, 'tdpa', 'Paid', 5, NULL, 'Unassigned');

DROP TABLE IF EXISTS "MyApp_tbl_orderitem" CASCADE;
CREATE TABLE "MyApp_tbl_orderitem" (
  "Item_id" SERIAL,
  "Item_Type" VARCHAR(20) NOT NULL,
  "Quantity_kg" DECIMAL(10,2) NOT NULL,
  "Unit_Price" DECIMAL(10,2) NOT NULL,
  "Delivery_Status" VARCHAR(20) NOT NULL,
  "Batch_id_id" INTEGER DEFAULT NULL,
  "FarmerSupply_id_id" INTEGER DEFAULT NULL,
  "Order_id_id" INTEGER NOT NULL,
  CONSTRAINT "myapp_tbl_orderitem_pk" PRIMARY KEY ("Item_id")
);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (14, 'Compost', 40.00, 200.00, 'Delivered', 2, NULL, 8);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (13, 'Compost', 29.29, 200.00, 'Pending', 2, NULL, 7);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (12, 'Compost', 10.71, 200.00, 'Pending', 1, NULL, 7);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (11, 'Compost', 35.00, 200.00, 'Delivered', 1, NULL, 6);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (10, 'Waste', 200.00, 10.00, 'Delivered', NULL, 9, 5);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (8, 'Waste', 100.00, 10.00, 'Delivered', NULL, 8, 3);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (15, 'Compost', 45.00, 200.00, 'Delivered', 2, NULL, 9);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (16, 'Compost', 21.00, 200.00, 'Delivered', 3, NULL, 10);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (17, 'Waste', 150.00, 10.00, 'Delivered', NULL, 11, 11);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (18, 'Waste', 200.00, 10.00, 'Delivered', NULL, 10, 12);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (19, 'Compost', 12.50, 200.00, 'Delivered', 4, NULL, 13);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (20, 'Compost', 11.50, 200.00, 'Delivered', 5, NULL, 13);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (21, 'Compost', 0.75, 200.00, 'Delivered', 5, NULL, 14);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (22, 'Compost', 19.25, 200.00, 'Delivered', 6, NULL, 14);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (23, 'Compost', 24.00, 200.00, 'Delivered', 6, NULL, 15);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (24, 'Waste', 50.00, 10.00, 'Delivered', NULL, 12, 16);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (25, 'Waste', 70.00, 10.00, 'Delivered', NULL, 13, 17);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (26, 'Waste', 120.00, 10.00, 'Delivered', NULL, 14, 18);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (27, 'Compost', 0.50, 200.00, 'Delivered', 6, NULL, 19);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (28, 'Compost', 81.25, 200.00, 'Delivered', 7, NULL, 19);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (29, 'Compost', 93.25, 200.00, 'Delivered', 8, NULL, 19);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (30, 'Waste', 50.00, 10.00, 'Delivered', NULL, 15, 20);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (32, 'Waste', 20.00, 10.00, 'Delivered', NULL, 17, 22);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (33, 'Compost', 0.50, 200.00, 'Delivered', 8, NULL, 23);
INSERT INTO "MyApp_tbl_orderitem" ("Item_id", "Item_Type", "Quantity_kg", "Unit_Price", "Delivery_Status", "Batch_id_id", "FarmerSupply_id_id", "Order_id_id") VALUES (34, 'Compost', 170.50, 200.00, 'Delivered', 9, NULL, 23);

DROP TABLE IF EXISTS "MyApp_tbl_paymenttransaction" CASCADE;
CREATE TABLE "MyApp_tbl_paymenttransaction" (
  "Transaction_id" SERIAL,
  "Amount" DECIMAL(10,2) NOT NULL,
  "transaction_type" VARCHAR(30) NOT NULL,
  "Reference_id" INTEGER DEFAULT NULL,
  "transaction_date" TIMESTAMP(6) NOT NULL,
  "status" VARCHAR(20) NOT NULL,
  "Payer_id_id" BIGINT NOT NULL,
  "Receiver_id_id" BIGINT NOT NULL,
  CONSTRAINT "myapp_tbl_paymenttransaction_pk" PRIMARY KEY ("Transaction_id")
);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (12, 1000.00, 'CollectorSalary', NULL, '2025-12-31 17:04:59.662452', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (11, 1000.00, 'CollectorSalary', NULL, '2025-12-31 17:02:25.107496', 'Success', 1, 19);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (10, 7000.00, 'CompostSale', 6, '2025-12-31 16:12:32.011788', 'Success', 23, 23);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (9, 2000.00, 'WasteSale', 5, '2025-12-31 15:56:48.654712', 'Success', 22, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (8, 1000.00, 'WasteSale', 3, '2025-12-31 15:47:05.292268', 'Success', 21, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (13, 1000.00, 'ManagerSalary', NULL, '2025-12-31 17:07:15.766564', 'Success', 1, 26);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (14, 8000.00, 'CompostSale', 7, '2026-01-01 04:23:36.010355', 'Success', 25, 25);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (15, 8000.00, 'CompostSale', 8, '2026-01-01 04:23:40.493212', 'Success', 25, 25);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (16, 9000.00, 'CompostSale', 9, '2026-01-01 04:31:12.149702', 'Success', 22, 22);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (17, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:19.061439', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (18, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:22.944371', 'Success', 1, 19);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (19, 1000.00, 'CollectorSalary', NULL, '2026-01-01 04:32:27.175922', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (20, 1000.00, 'ManagerSalary', NULL, '2026-01-01 04:32:32.433867', 'Success', 1, 26);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (21, 4200.00, 'CompostSale', 10, '2026-01-02 10:40:41.307651', 'Success', 22, 22);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (22, 1000.00, 'CollectorSalary', NULL, '2026-01-04 15:40:31.508704', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (23, 1000.00, 'CollectorSalary', NULL, '2026-01-04 15:40:37.023828', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (24, 4800.00, 'CompostSale', 13, '2026-01-12 11:37:12.636203', 'Success', 21, 21);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (25, 2000.00, 'WasteSale', 12, '2026-01-12 11:43:03.939406', 'Success', 23, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (26, 1500.00, 'WasteSale', 11, '2026-01-12 11:43:12.231636', 'Success', 25, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (27, 1000.00, 'CollectorSalary', NULL, '2026-01-13 15:49:16.117470', 'Success', 1, 16);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (28, 1000.00, 'CollectorSalary', NULL, '2026-01-13 15:49:19.668680', 'Success', 1, 17);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (29, 1000.00, 'CollectorSalary', NULL, '2026-01-13 15:49:23.186913', 'Success', 1, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (30, 1000.00, 'CollectorSalary', NULL, '2026-01-13 15:49:27.399820', 'Success', 1, 19);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (31, 1000.00, 'CollectorSalary', NULL, '2026-01-13 15:50:15.206406', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (32, 3000.00, 'ManagerSalary', NULL, '2026-01-13 15:50:23.693399', 'Success', 1, 27);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (33, 4000.00, 'CompostSale', 14, '2026-01-20 06:55:38.316646', 'Success', 21, 21);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (34, 4800.00, 'CompostSale', 15, '2026-01-20 07:10:08.894013', 'Success', 23, 23);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (35, 1000.00, 'CollectorSalary', NULL, '2026-01-20 07:10:52.472311', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (36, 1000.00, 'CollectorSalary', NULL, '2026-01-20 07:10:56.089599', 'Success', 1, 16);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (37, 1000.00, 'CollectorSalary', NULL, '2026-01-20 07:10:59.758488', 'Success', 1, 17);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (38, 1000.00, 'ManagerSalary', NULL, '2026-01-21 08:49:53.328483', 'Success', 1, 26);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (39, 500.00, 'WasteSale', 16, '2026-01-21 16:14:39.162547', 'Success', 21, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (40, 700.00, 'WasteSale', 17, '2026-01-21 16:16:31.200284', 'Success', 22, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (41, 1200.00, 'WasteSale', 18, '2026-01-21 16:25:23.488763', 'Success', 23, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (42, 35000.00, 'CompostSale', 19, '2026-01-21 18:16:03.403821', 'Success', 23, 23);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (43, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:02.341186', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (44, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:07.626424', 'Success', 1, 16);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (45, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:12.670897', 'Success', 1, 17);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (46, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:20.193896', 'Success', 1, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (47, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:24.473236', 'Success', 1, 19);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (48, 1000.00, 'CollectorSalary', NULL, '2026-01-21 18:26:28.310908', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (49, 1000.00, 'ManagerSalary', NULL, '2026-01-21 18:26:32.646273', 'Success', 1, 26);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (50, 1000.00, 'ManagerSalary', NULL, '2026-01-21 18:26:37.008761', 'Success', 1, 27);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (51, 500.00, 'WasteSale', 20, '2026-01-22 04:23:30.134834', 'Success', 23, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (52, 200.00, 'WasteSale', 21, '2026-01-22 04:28:13.201138', 'Success', 21, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (53, 1000.00, 'CollectorSalary', NULL, '2026-01-24 13:15:02.062009', 'Success', 1, 17);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (54, 2000.00, 'CollectorSalary', NULL, '2026-02-02 09:34:50.801314', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (55, 34200.00, 'CompostSale', 23, '2026-02-07 05:58:35.775765', 'Success', 25, 25);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (56, 200.00, 'WasteSale', 22, '2026-02-07 05:59:56.562877', 'Success', 21, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (57, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.349782', 'Success', 1, 15);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (58, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.366629', 'Success', 1, 16);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (59, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.371415', 'Success', 1, 17);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (60, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.375358', 'Success', 1, 18);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (61, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.382753', 'Success', 1, 19);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (62, 1000.00, 'CollectorSalary', NULL, '2026-02-07 06:38:53.387503', 'Success', 1, 20);
INSERT INTO "MyApp_tbl_paymenttransaction" ("Transaction_id", "Amount", "transaction_type", "Reference_id", "transaction_date", "status", "Payer_id_id", "Receiver_id_id") VALUES (63, 1000.00, 'ManagerSalary', NULL, '2026-02-07 06:49:27.052125', 'Success', 1, 27);

DROP TABLE IF EXISTS "MyApp_tbl_pickuprequest" CASCADE;
CREATE TABLE "MyApp_tbl_pickuprequest" (
  "Pickup_id" SERIAL,
  "scheduled_date" DATE NOT NULL,
  "request_time" TIME(6) NOT NULL,
  "status" VARCHAR(20) NOT NULL,
  "actual_weight_kg" DECIMAL(10,2) DEFAULT NULL,
  "payment_method" VARCHAR(20) DEFAULT NULL,
  "payment_amount" DECIMAL(10,2) DEFAULT NULL,
  "payment_status" VARCHAR(20) NOT NULL,
  "transaction_id" VARCHAR(100) DEFAULT NULL,
  "payment_date" TIMESTAMP(6) DEFAULT NULL,
  "assigned_collector_id" BIGINT DEFAULT NULL,
  "bin_type_id" INTEGER DEFAULT NULL,
  "household_id" BIGINT NOT NULL,
  "payment_id" INTEGER DEFAULT NULL,
  CONSTRAINT "myapp_tbl_pickuprequest_pk" PRIMARY KEY ("Pickup_id")
);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (19, '2026-01-01', '09:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767236719395', '2026-01-01 03:05:19.910460', 3, 3, 2, 19);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (18, '2026-01-01', '09:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767236379100', '2026-01-01 02:59:39.897944', 1, 3, 1, 18);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (3, '2025-12-30', '13:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767078005505', '2025-12-30 07:00:05.953796', 3, 3, 2, 3);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (4, '2025-12-31', '14:20:00.000000', 'Completed', 48.00, 'COD', 100.00, 'Completed', 'TXN1767170354680', '2025-12-31 08:39:14.989442', 1, 3, 1, 4);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (5, '2025-12-31', '14:22:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170453915', '2025-12-31 08:40:53.507203', 3, 3, 2, 5);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (6, '2025-12-31', '14:20:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170555501', '2025-12-31 08:42:35.672436', 5, 3, 3, 6);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (7, '2025-12-31', '14:20:00.000000', 'Completed', 49.00, 'UPI', 100.00, 'Completed', 'TXN1767170632898', '2025-12-31 08:43:52.875185', 1, 3, 4, 7);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (8, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170700830', '2025-12-31 08:45:00.444639', 5, 3, 5, 8);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (9, '2025-12-31', '14:30:00.000000', 'Completed', 23.00, 'UPI', 50.00, 'Completed', 'TXN1767170804191', '2025-12-31 08:46:44.522437', 5, 4, 6, 9);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (10, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170865958', '2025-12-31 08:47:45.668706', 6, 3, 7, 10);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (11, '2025-12-31', '14:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767170920755', '2025-12-31 08:48:40.772903', 6, 3, 8, 11);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (12, '2026-01-01', '16:00:00.000000', 'Completed', 45.00, 'UPI', 100.00, 'Completed', 'TXN1767170951296', '2025-12-31 08:49:11.419086', 6, 3, 8, 12);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (13, '2026-01-02', '16:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1767170977410', '2025-12-31 08:49:37.704320', 6, 4, 8, 13);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (14, '2025-12-31', '14:40:00.000000', 'Completed', 40.00, 'UPI', 100.00, 'Completed', 'TXN1767171052280', '2025-12-31 08:50:52.674920', 2, 3, 9, 14);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (15, '2025-12-31', '14:40:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767171182520', '2025-12-31 08:53:02.330995', 2, 3, 10, 15);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (16, '2025-12-31', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767171243947', '2025-12-31 08:54:03.321078', 3, 3, 11, 16);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (17, '2025-12-31', '15:00:00.000000', 'Completed', 50.00, 'UPI', 50.00, 'Completed', 'TXN1767171302776', '2025-12-31 08:55:02.702368', 4, 4, 12, 17);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (20, '2026-01-01', '10:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767239755315', '2026-01-01 03:55:55.868903', 5, 3, 3, 20);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (21, '2026-01-01', '10:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767240250379', '2026-01-01 04:04:10.535446', 1, 3, 4, 21);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (22, '2026-01-02', '16:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1767346914734', '2026-01-02 09:41:54.530567', 6, 3, 8, 22);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (23, '2026-01-04', '20:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1767535597325', '2026-01-04 14:06:37.501394', 1, 3, 1, 23);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (24, '2026-01-12', '15:45:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1768210416162', '2026-01-12 09:33:36.829766', 4, 3, 13, 24);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (25, '2026-01-12', '15:45:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1768210564587', '2026-01-12 09:36:04.504414', 4, 4, 12, 25);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (26, '2026-01-12', '15:45:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768210715230', '2026-01-12 09:38:35.687887', 3, 3, 11, 26);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (27, '2026-01-12', '15:45:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768210887977', '2026-01-12 09:41:27.952571', 2, 3, 10, 27);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (28, '2026-01-12', '15:45:00.000000', 'Completed', 24.00, 'UPI', 50.00, 'Completed', 'TXN1768211201379', '2026-01-12 09:46:41.241042', 2, 4, 9, 28);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (29, '2026-01-12', '15:45:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768211294740', '2026-01-12 09:48:14.258247', 6, 3, 8, 29);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (30, '2026-01-12', '16:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768215085686', '2026-01-12 10:51:25.310708', 5, 3, 6, 30);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (31, '2026-01-12', '16:30:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768215139951', '2026-01-12 10:52:19.351927', 6, 3, 7, 31);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (32, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768640364800', '2026-01-17 08:59:24.569823', 1, 3, 1, 32);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (33, '2026-01-17', '15:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1768640521814', '2026-01-17 09:02:01.837503', 3, 4, 2, 33);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (34, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768640612412', '2026-01-17 09:03:32.123794', 5, 3, 3, 34);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (35, '2026-01-17', '15:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1768640714179', '2026-01-17 09:05:14.399830', 1, 4, 4, 35);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (36, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768640846601', '2026-01-17 09:07:26.414547', 5, 3, 5, 36);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (37, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768640901974', '2026-01-17 09:08:21.754701', 5, 3, 6, 37);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (38, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1768641000531', '2026-01-17 09:10:00.917062', 6, 3, 7, 38);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (39, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768641066345', '2026-01-17 09:11:06.947199', 6, 3, 8, 39);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (40, '2026-01-17', '15:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1768641140177', '2026-01-17 09:12:20.190235', 2, 4, 9, 40);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (41, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768641202883', '2026-01-17 09:13:22.783842', 2, 3, 10, 41);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (42, '2026-01-17', '15:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1768641270593', '2026-01-17 09:14:30.516934', 3, 4, 11, 42);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (43, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768641503653', '2026-01-17 09:18:23.182243', 4, 3, 12, 43);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (44, '2026-01-17', '15:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1768641563298', '2026-01-17 09:19:23.873236', 4, 3, 13, 44);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (45, '2026-01-21', '21:00:00.000000', 'Completed', 40.00, 'UPI', 100.00, 'Completed', 'TXN1769007141716', '2026-01-21 14:52:21.101630', 1, 3, 1, 45);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (46, '2026-01-21', '21:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1769007215456', '2026-01-21 14:53:35.406131', 3, 4, 2, 46);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (47, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1769007272244', '2026-01-21 14:54:32.263386', 5, 3, 3, 47);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (48, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007322412', '2026-01-21 14:55:22.551006', 1, 3, 4, 48);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (49, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007371846', '2026-01-21 14:56:11.251217', 5, 3, 5, 49);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (50, '2026-01-21', '21:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1769007417546', '2026-01-21 14:56:57.195221', 5, 4, 6, 50);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (51, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007485939', '2026-01-21 14:58:05.735875', 6, 3, 7, 51);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (52, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007537362', '2026-01-21 14:58:57.710233', 6, 3, 8, 52);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (53, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007624823', '2026-01-21 15:00:24.821922', 2, 3, 10, 53);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (54, '2026-01-21', '21:00:00.000000', 'Completed', 25.00, 'UPI', 50.00, 'Completed', 'TXN1769007678398', '2026-01-21 15:01:18.945801', 2, 4, 9, 54);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (55, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769007732483', '2026-01-21 15:02:12.963076', 3, 3, 11, 55);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (56, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1769007797615', '2026-01-21 15:03:17.063399', 4, 3, 12, 56);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (57, '2026-01-21', '21:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1769007853817', '2026-01-21 15:04:13.963429', 4, 3, 13, 57);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (58, '2026-01-22', '11:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769055441632', '2026-01-22 04:17:21.389658', 1, 3, 1, 58);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (59, '2026-01-22', '23:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769055975510', '2026-01-22 04:26:15.131519', 3, 3, 2, 59);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (60, '2026-01-24', '21:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1769260901459', '2026-01-24 13:21:41.470794', 1, 3, 1, 60);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (61, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'UPI', 100.00, 'Completed', 'TXN1770440912123', '2026-02-07 05:08:32.254825', 1, 3, 1, 61);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (62, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441002583', '2026-02-07 05:10:02.699400', 3, 3, 2, 62);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (63, '2026-02-07', '11:00:00.000000', 'Completed', 25.00, 'COD', 50.00, 'Completed', 'TXN1770441070421', '2026-02-07 05:11:10.538825', 5, 4, 3, 63);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (64, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441135130', '2026-02-07 05:12:15.708479', 1, 3, 4, 64);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (65, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441219646', '2026-02-07 05:13:39.177938', 5, 3, 5, 65);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (66, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441286638', '2026-02-07 05:14:46.999789', 5, 3, 6, 66);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (67, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441373664', '2026-02-07 05:16:13.059299', 6, 3, 7, 67);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (68, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441441651', '2026-02-07 05:17:21.394493', 6, 3, 8, 68);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (69, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441498768', '2026-02-07 05:18:18.352211', 2, 3, 9, 69);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (70, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441546525', '2026-02-07 05:19:06.012942', 2, 3, 10, 70);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (71, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441597370', '2026-02-07 05:19:57.762986', 3, 3, 11, 71);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (72, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441653534', '2026-02-07 05:20:53.908319', 4, 3, 12, 72);
INSERT INTO "MyApp_tbl_pickuprequest" ("Pickup_id", "scheduled_date", "request_time", "status", "actual_weight_kg", "payment_method", "payment_amount", "payment_status", "transaction_id", "payment_date", "assigned_collector_id", "bin_type_id", "household_id", "payment_id") VALUES (73, '2026-02-07', '11:00:00.000000', 'Completed', 50.00, 'COD', 100.00, 'Completed', 'TXN1770441707401', '2026-02-07 05:21:47.768233', 4, 3, 13, 73);

DROP TABLE IF EXISTS "MyApp_tbl_residentsassociation" CASCADE;
CREATE TABLE "MyApp_tbl_residentsassociation" (
  "RA_id" SERIAL,
  "Association_Name" VARCHAR(200) NOT NULL,
  "Location_id" INTEGER NOT NULL,
  CONSTRAINT "myapp_tbl_residentsassociation_pk" PRIMARY KEY ("RA_id")
);
INSERT INTO "MyApp_tbl_residentsassociation" ("RA_id", "Association_Name", "Location_id") VALUES (1, 'Chaithanya Nagar', 1);
INSERT INTO "MyApp_tbl_residentsassociation" ("RA_id", "Association_Name", "Location_id") VALUES (2, 'Divine Nagar', 1);
INSERT INTO "MyApp_tbl_residentsassociation" ("RA_id", "Association_Name", "Location_id") VALUES (3, 'Perukoni', 1);

DROP TABLE IF EXISTS "MyApp_tbl_route" CASCADE;
CREATE TABLE "MyApp_tbl_route" (
  "Route_id" SERIAL,
  "name" VARCHAR(100) NOT NULL,
  "start_house_no" INTEGER DEFAULT NULL,
  "end_house_no" INTEGER DEFAULT NULL,
  "location_id" INTEGER NOT NULL,
  "residents_association_id" INTEGER DEFAULT NULL,
  CONSTRAINT "myapp_tbl_route_pk" PRIMARY KEY ("Route_id"),
  CONSTRAINT "MyApp_tbl_route_name_unique" UNIQUE ("name")
);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (1, 'AOne', 1, 2, 1, 1);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (2, 'ATwo', 3, 4, 1, 1);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (3, 'BOne', 1, 2, 1, 2);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (4, 'BTwo', 2, 4, 1, 2);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (5, 'COne', 1, 2, 1, 3);
INSERT INTO "MyApp_tbl_route" ("Route_id", "name", "start_house_no", "end_house_no", "location_id", "residents_association_id") VALUES (6, 'CTwo', 3, 4, 1, 3);

DROP TABLE IF EXISTS "MyApp_tbl_wasteinventory" CASCADE;
CREATE TABLE "MyApp_tbl_wasteinventory" (
  "Inventory_id" SERIAL,
  "available_quantity_kg" DECIMAL(10,2) NOT NULL,
  "price_per_kg" DECIMAL(10,2) NOT NULL,
  "collection_date" TIMESTAMP(6) NOT NULL,
  "status" VARCHAR(20) NOT NULL,
  "collection_request_id" INTEGER NOT NULL,
  "collector_id" BIGINT NOT NULL,
  "salary_paid" BOOLEAN NOT NULL,
  "expiry_date" TIMESTAMP(6) DEFAULT NULL,
  CONSTRAINT "myapp_tbl_wasteinventory_pk" PRIMARY KEY ("Inventory_id")
);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (10, 37.00, 10.00, '2025-12-31 09:15:24.676404', 'Used', 10, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (11, 23.00, 10.00, '2025-12-31 09:15:32.076181', 'Used', 11, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (12, 50.00, 10.00, '2025-12-31 09:16:04.067852', 'Used', 12, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (13, 50.00, 10.00, '2025-12-31 09:16:09.890196', 'Used', 13, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (14, 50.00, 10.00, '2026-01-01 04:05:17.590083', 'Used', 14, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (15, 50.00, 10.00, '2026-01-01 04:05:27.158231', 'Used', 15, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (16, 50.00, 10.00, '2026-01-01 04:08:33.049065', 'Used', 16, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (17, 45.00, 10.00, '2026-01-01 04:09:46.162583', 'Used', 17, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (18, 50.00, 10.00, '2026-01-01 04:10:59.510387', 'Used', 18, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (19, 25.00, 10.00, '2026-01-02 09:53:19.060147', 'Used', 19, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (20, 50.00, 10.00, '2026-01-02 09:53:37.513822', 'Used', 20, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (21, 50.00, 10.00, '2026-01-04 14:10:32.519652', 'Used', 21, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (22, 0.00, 10.00, '2026-01-12 10:53:32.290822', 'Available', 22, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (23, 0.00, 10.00, '2026-01-12 10:53:47.858318', 'Available', 23, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (24, 0.00, 10.00, '2026-01-12 10:54:21.989563', 'Available', 24, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (25, 0.00, 10.00, '2026-01-12 10:55:29.035789', 'Available', 25, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (26, 0.00, 10.00, '2026-01-12 10:55:43.628611', 'Available', 26, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (27, 0.00, 10.00, '2026-01-12 10:56:13.668733', 'Available', 27, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (28, 0.00, 10.00, '2026-01-12 10:56:31.815048', 'Available', 28, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (29, 25.00, 10.00, '2026-01-12 10:57:10.562595', 'Used', 29, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (30, 24.00, 10.00, '2026-01-12 10:57:25.429935', 'Used', 30, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (31, 50.00, 10.00, '2026-01-17 09:20:57.199509', 'Used', 31, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (32, 25.00, 10.00, '2026-01-17 09:23:30.635252', 'Used', 32, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (33, 25.00, 10.00, '2026-01-17 09:29:22.932920', 'Used', 33, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (34, 50.00, 10.00, '2026-01-17 09:34:10.701942', 'Used', 34, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (35, 25.00, 10.00, '2026-01-17 09:38:09.599542', 'Used', 35, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (36, 0.00, 10.00, '2026-01-21 15:04:48.744083', 'Available', 36, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (37, 0.00, 10.00, '2026-01-21 15:12:34.830630', 'Available', 37, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (38, 0.00, 10.00, '2026-01-21 15:21:25.191279', 'Available', 38, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (39, 0.00, 10.00, '2026-01-21 15:24:22.106540', 'Available', 39, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (40, 0.00, 10.00, '2026-01-21 15:27:52.187351', 'Available', 40, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (41, 0.00, 10.00, '2026-01-21 15:29:11.737121', 'Available', 41, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (42, 25.00, 10.00, '2026-01-21 15:48:39.078291', 'Used', 42, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (43, 50.00, 10.00, '2026-01-21 16:04:57.213329', 'Used', 43, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (44, 50.00, 10.00, '2026-01-21 16:05:14.655733', 'Used', 44, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (45, 50.00, 10.00, '2026-01-21 16:05:36.401965', 'Used', 45, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (46, 50.00, 10.00, '2026-01-21 16:05:51.073007', 'Used', 46, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (47, 50.00, 10.00, '2026-01-21 16:06:07.423693', 'Used', 47, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (48, 25.00, 10.00, '2026-01-21 16:06:25.939932', 'Used', 48, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (49, 50.00, 10.00, '2026-01-21 16:07:39.786969', 'Used', 49, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (50, 50.00, 10.00, '2026-01-21 16:07:53.451773', 'Used', 50, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (51, 50.00, 10.00, '2026-01-21 16:08:09.155271', 'Used', 51, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (52, 50.00, 10.00, '2026-01-21 16:13:22.602238', 'Used', 52, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (53, 50.00, 10.00, '2026-01-21 17:16:03.034678', 'Used', 53, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (54, 50.00, 10.00, '2026-01-21 17:16:16.503124', 'Used', 54, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (55, 50.00, 10.00, '2026-01-21 17:16:26.917969', 'Used', 55, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (56, 50.00, 10.00, '2026-01-21 17:16:36.968088', 'Used', 56, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (57, 0.00, 10.00, '2026-01-22 04:18:04.895502', 'Sold', 57, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (58, 10.00, 10.00, '2026-01-22 04:27:38.679640', 'Used', 58, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (59, 50.00, 10.00, '2026-01-24 13:22:55.843964', 'Used', 59, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (60, 50.00, 10.00, '2026-02-07 05:22:38.633179', 'Used', 60, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (61, 50.00, 10.00, '2026-02-07 05:34:50.275256', 'Used', 61, 1, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (62, 50.00, 10.00, '2026-02-07 05:35:37.343869', 'Used', 62, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (63, 50.00, 10.00, '2026-02-07 05:36:45.776436', 'Used', 63, 2, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (64, 50.00, 10.00, '2026-02-07 05:37:19.776905', 'Used', 64, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (65, 50.00, 10.00, '2026-02-07 05:37:44.585828', 'Used', 65, 3, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (66, 50.00, 10.00, '2026-02-07 05:38:37.778975', 'Used', 66, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (67, 50.00, 10.00, '2026-02-07 05:38:49.252214', 'Used', 67, 4, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (68, 25.00, 10.00, '2026-02-07 05:39:27.218596', 'Used', 68, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (69, 50.00, 10.00, '2026-02-07 05:39:38.279730', 'Used', 69, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (70, 50.00, 10.00, '2026-02-07 05:39:48.321392', 'Used', 70, 5, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (71, 50.00, 10.00, '2026-02-07 05:40:17.889865', 'Used', 71, 6, TRUE, NULL);
INSERT INTO "MyApp_tbl_wasteinventory" ("Inventory_id", "available_quantity_kg", "price_per_kg", "collection_date", "status", "collection_request_id", "collector_id", "salary_paid", "expiry_date") VALUES (72, 50.00, 10.00, '2026-02-07 05:40:33.521149', 'Used', 72, 6, TRUE, NULL);