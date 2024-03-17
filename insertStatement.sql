INSERT INTO userauth_role (name,description,is_active) VALUES
	 ('Admin','Admin',1),
	 ('Staff','Staff',1),
	 ('Doctor','Doctor',1),
	 ('Pathologist','Pathologist',1),
	 ('Patient','Patient',1);

INSERT INTO userauth_user (password,email,name,phone,is_active,is_superuser,is_staff,date_joined,last_login,role_id) VALUES
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','nazmul@test.com','Nazmul','012345678',1,0,1,'2024-03-09 06:18:41','2024-03-17 03:30:55.401433',3),
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','kamrul@test.com','Kamrul','0158456',1,1,1,'2024-03-09 06:20:14','2024-03-17 06:22:01.338341',3),
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','islam@test.com','Islam','01985236477',1,0,0,'2024-03-09 11:11:54',NULL,3),
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','ashraf@test.com','Ash Raf','01254788',1,0,1,'2024-03-12 02:48:25','2024-03-17 05:58:41.427002',4),
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','zahid@test.com','Zahid','01985233',1,0,0,'2024-03-12 02:49:40','2024-03-12 10:00:16.654228',4),
	 ('pbkdf2_sha256$720000$bbs5dptm5Zc7rrGtzcJG2q$JNl0inn1Y8JHdRC0QD6t81qkQmYqomeqvucYXP7CXog=','staff@test.com','Staff','01478522369',1,0,0,'2024-03-15 09:26:42','2024-03-17 06:23:18.104153',2);


INSERT INTO patient_bloodgroup (created_at,updated_at,is_active,name,created_by_id,updated_by_id) VALUES
	 ('2024-03-08 13:58:26.483490','2024-03-08 13:58:26.483490',1,'O+',1,1),
	 ('2024-03-08 13:58:33.656396','2024-03-08 13:58:33.656396',1,'O-',1,1),
	 ('2024-03-08 13:58:39.825620','2024-03-08 13:58:39.825620',1,'A+',1,1),
	 ('2024-03-08 13:58:48.888554','2024-03-08 13:58:48.888554',1,'B+',1,1),
	 ('2024-03-08 13:58:58.005932','2024-03-08 13:58:58.005932',1,'AB+',1,1);

INSERT INTO diagnosis_specimen (created_at,updated_at,is_active,name,description,created_by_id,updated_by_id) VALUES
	 ('2024-03-12 02:39:23.110122','2024-03-12 02:39:23.110122',1,'Blood','Blood',1,1),
	 ('2024-03-12 02:39:38.752814','2024-03-12 02:39:38.752814',1,'Urine','Urine',1,1),
	 ('2024-03-12 02:39:48.902392','2024-03-12 02:39:48.902392',1,'Stool','Stool',1,1),
	 ('2024-03-12 02:40:08.239421','2024-03-12 02:40:08.239421',1,'Skin Tissue','Skin Tissue',1,1),
	 ('2024-03-12 02:41:57.125928','2024-03-12 02:41:57.125928',1,'Radiography','Radiography',1,1);

INSERT INTO diagnosis_diagnosiscategory (created_at,updated_at,is_active,name,description,created_by_id,updated_by_id) VALUES
	 ('2024-03-05 07:05:09.701086','2024-03-05 07:31:54.615019',1,'Radiology & Imaging','Radiology & Imaging',1,1),
	 ('2024-03-05 07:05:34.008373','2024-03-05 07:31:24.871047',1,'Pathology','Pathology',1,1);

INSERT INTO diagnosis_diagnosis (created_at,updated_at,is_active,name,description,created_by_id,updated_by_id,category_id,price,specimen_id) VALUES
	 ('2024-03-05 07:34:50.227402','2024-03-12 02:43:34.867054',1,'CBC','Complete blood count',1,1,4,400,1),
	 ('2024-03-05 07:35:20.874545','2024-03-12 02:43:30.892944',1,'ESR','Erythrocyte Sedimentation Rate',1,1,4,300,1),
	 ('2024-03-05 07:37:22.527695','2024-03-17 02:46:06.693757',1,'Dengue IgG & IgM','Dengue IgG & IgM',1,1,4,300,1),
	 ('2024-03-05 07:37:57.362122','2024-03-17 02:45:58.451607',1,'Tripple Antigen','Tripple Antigen',1,1,4,500,1),
	 ('2024-03-05 07:38:17.787111','2024-03-12 02:43:11.197178',1,'Blood Culture','Blood Culture',1,1,4,800,1),
	 ('2024-03-05 07:38:40.895709','2024-03-12 02:43:04.738854',1,'Urine Routine Exam','Urine Routine Exam',1,1,4,600,2),
	 ('2024-03-05 07:39:06.316754','2024-03-12 02:42:49.617514',1,'X-Ray Chest PA View','X-Ray Chest PA View',1,1,3,700,5),
	 ('2024-03-05 07:39:28.026297','2024-03-12 02:42:32.509500',1,'USG of Whole Abdomen','USG of Whole Abdomen',1,1,3,400,5),
	 ('2024-03-05 10:16:28.489490','2024-03-12 02:42:27.607862',1,'Liver function tests ( LFT )','Liver function tests ( LFT )',1,1,4,100,1);

INSERT INTO doctors_doctorspecialization (created_at,updated_at,is_active,name,description,created_by_id,updated_by_id) VALUES
	 ('2024-03-09 06:16:42.187399','2024-03-09 06:16:42.187399',1,'Sonologist','Sonologist',1,1),
	 ('2024-03-09 06:17:23.118462','2024-03-09 06:17:23.118462',1,'Pathologist','Pathologist',1,1);

INSERT INTO doctors_doctor (created_at,updated_at,is_active,firstname,lastname,age,picture,address,city,state,zip,mobile,created_by_id,updated_by_id,user_id,specialization_id,diagnosisCategory_id) VALUES
	 ('2024-03-09 06:20:07.790369','2024-03-09 06:20:07.790369',1,'Nazmul','Islam',55,'','27 Bonogram','Dhaka','Dhaka','1200','012121212',1,1,2,2,3),
	 ('2024-03-09 06:21:16.441972','2024-03-09 06:21:16.441972',1,'Kamrul','Islam',52,'','12 Link Road','Dhaka','Dhaka','1300','012121210',1,1,3,1,4);






