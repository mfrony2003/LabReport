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

INSERT INTO diagnosis_diagnosisparameters (created_at,updated_at,is_active,investigationName,Unit,Reverence_Range,created_by_id,diagnosisName_id,updated_by_id) VALUES
	 ('2024-03-05 10:10:29.323194','2024-03-05 10:10:29.323194',1,'Hematocrit','g/dL','Male: 38.3% to 48.6% Female: 35.5% to 44.9%',1,1,1),
	 ('2024-03-05 10:11:18.400958','2024-03-05 14:20:02.382224',1,'Total Count','k/ul','4.0-10.0',1,1,1),
	 ('2024-03-05 10:12:08.079825','2024-03-05 14:19:38.003548',1,'Total WBC Count','k/ul','3.4 to 9.6 billion cells/L',1,1,1),
	 ('2024-03-05 10:12:31.799803','2024-03-05 14:18:52.078519',1,'Platelet count','k/ul','150-410',1,1,1),
	 ('2024-03-05 10:17:56.372286','2024-03-05 10:17:56.372286',1,'Alanine transaminase (ALT)','U/L','Male: UP TO 50 Female : Up to 35',1,14,1),
	 ('2024-03-05 10:18:49.839937','2024-03-05 10:18:49.839937',1,'Aspartate transaminase (AST)','U/L','UP TO 37',1,14,1),
	 ('2024-03-05 10:19:29.241712','2024-03-05 10:19:29.241712',1,'alkaline phosphatase (ALP)','U/L','38-128',1,14,1),
	 ('2024-03-10 02:20:10.411292','2024-03-10 02:20:10.411292',1,'ESR','mm/hr.','Men under 50 years old: less than 15 mm/hr. Men over 50 years less 20 mm/hr.    Women under 50 years old: less than 20 mm/hr. Women over 50 years old: less than 30 mm/hr.',1,2,1),
	 ('2024-03-10 02:24:41.137955','2024-03-10 02:24:41.137955',1,'Color','','colorless ,dark yellow, Pale yellow or amber (May be stained by certain foods)',1,8,1),
	 ('2024-03-10 02:25:34.697473','2024-03-10 02:25:34.697473',1,'pH','','4.5-8',1,8,1),
	 ('2024-03-10 02:26:14.868395','2024-03-10 02:26:14.868395',1,'Glucose: at or below','mg/dL.','130 mg/dL.',1,8,1),
	 ('2024-03-16 14:57:47.947893','2024-03-16 14:57:47.947893',1,'IGM','','',1,5,1),
	 ('2024-03-16 14:58:09.245568','2024-03-16 14:58:09.245568',1,'IgG','','',1,5,1),
	 ('2024-03-16 14:59:02.049596','2024-03-16 14:59:02.049596',1,'TO','','1.8',1,6,1),
	 ('2024-03-16 14:59:20.225870','2024-03-16 14:59:20.225870',1,'TH','','1.8',1,6,1),
	 ('2024-03-16 14:59:46.407349','2024-03-16 14:59:46.407349',1,'AH','','1.8',1,6,1),
	 ('2024-03-16 14:59:59.708622','2024-03-16 14:59:59.708622',1,'BH','','1.8',1,6,1),
	 ('2024-03-16 15:01:34.855026','2024-03-16 15:01:34.855026',1,'Culture & Sensivity Report','','',1,7,1),
	 ('2024-03-17 03:15:42.330873','2024-03-17 03:15:42.330873',1,'Radiology','','',1,9,1),
	 ('2024-03-17 03:16:24.850268','2024-03-17 03:16:24.850268',1,'Radiology','','',1,10,1);

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






