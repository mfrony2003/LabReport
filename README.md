# Lab Report sample application

## Sequence Diagram
```mermaid




sequenceDiagram
 autonumber
  participant   Patient
  box Hospital
  participant   Lab-Staff
  participant   Pathologiest
  participant   Doctor
  end
  title LabReport
  
  Patient->>Lab-Staff: I need to do some diagnosis

  Lab-Staff->>Patient: Ok,Let me collect your diagnosis list s , pay the bill and a pathologist will collect sample to the lab

 Patient->>Pathologiest: Here is the diagnosis list and payment receipt 
 activate Pathologiest
 Pathologiest->>Patient: Ok ,  Let me scan the barcode on the receipt and collect your samples in the lab, you will receive alink on your given mobile no to view the reports when ready 

 Pathologiest-->Doctor:Colleced the sample and report will automatically assign to the appropriated doctor

 Doctor->Doctor: Login , and diagnosis the report and prescribe the treatment plan, also send the report link to the patient mobile number

Note right of Doctor: As soon as doctor finish a lik send to patient mobile to view report


```

## How to install
   
```bash
mkdir my_project
cd my_project
git init
git pull https://github.com/mfrony2003/LabReport.git
```
Create virtual Environment and install the requried packages
```bash
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
RUN
```bash
python manage.py migrate
python manage.py createsuperuser
execute the inserctStatement.sql -- it will populate the data pre loaded data


| User                   | Password | Role |
| :--------------------  | :------: | ----: |
| staff@test.com         | 123456   | staff     |
| doctor1@test.com       | 123456   | doctor    |
| doctor2@test.com       | 123456   | doctor    |
| doctor3@test.com       | 123456   | doctor    |
| pathologist1@test.com  | 123456   | pathologist 
| pathologist2@test.com  | 123456   | pathologist 


$ python manage.py runserver

```
http://localhost:8000

# Step 1

Login as a staff user (staff@test.com). 


![Login](https://github.com/mfrony2003/LabReport/assets/26355258/46dde89f-c025-4f95-9ec8-23eddec7021a)

Add patient and add new diafonosis. View existing reports.

[
![patient](https://github.com/mfrony2003/LabReport/assets/26355258/1946b334-da53-4ffc-9ac8-3755d89881f0)
](url)

# Step 2

Login as pathologist user (pathologist1@test.com). and Collect Specimen 

[
![patholgist](https://github.com/mfrony2003/LabReport/assets/26355258/ceb50e93-ab01-4674-a57e-3169b05fb3e2)
](url)

# Step 3
Login as a doctor user (doctor1@test.com).you will get the info for whom its assign to . Diagnose the report and prescribe treatment plan.

[
![doctor](https://github.com/mfrony2003/LabReport/assets/26355258/478937f1-cdd5-4972-97e0-6ea6b3229f28)
](url)

Save

[
![report](https://github.com/mfrony2003/LabReport/assets/26355258/ace1cfc7-14c7-45d4-af6f-88dd383daf04)
](url)



## DB Info
 url : http://localhost:8000/admin
 user :faisal
 pwd:test@123
 
 ## Change the Static text copy the below url to the browser
   http://localhost:8000/rosetta

![dynamic_text](https://github.com/mfrony2003/djangoMultilingual/assets/26355258/165adea5-5f06-489a-9aad-3f2bdd9ff49f)
   
![static_text](https://github.com/mfrony2003/djangoMultilingual/assets/26355258/3cf8e36c-8b34-4e9d-a65e-5664b119a073)
   

