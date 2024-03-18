# Pathology Lab Management System (PLMS) (Version 1.0)

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

## How to Run
   
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




```
## Use Docker to run the preoject
 Run the below commands 
 
```bash
 docker-compose build

 docker-compose run

```
open the link on browser

http://localhost:8000


# Step 1

Login as a staff user (staff@test.com). 


![Login](https://github.com/mfrony2003/LabReport/assets/26355258/46dde89f-c025-4f95-9ec8-23eddec7021a)

Add patient and add new diafonosis. View existing reports.

[
![patient](https://github.com/mfrony2003/LabReport/assets/26355258/1946b334-da53-4ffc-9ac8-3755d89881f0)
](url)

![MakePay](https://github.com/mfrony2003/LabReport/assets/26355258/633d2395-91c2-46e8-b1db-e83aeca1f208)


![bill](https://github.com/mfrony2003/LabReport/assets/26355258/f33950b6-7a49-41b6-8785-1c3132afc708)



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

Populate the data and click Save

[
![patholgist](https://github.com/mfrony2003/LabReport/assets/26355258/41f58f9a-31a0-42ea-bb7f-756275491a00)
](url)

Click Print

[
![doctorView](https://github.com/mfrony2003/LabReport/assets/26355258/7e8131c2-dd10-45e1-869d-559898453e32)
](url)

### Report generate

The doctor can generate the report by clicking on "Print" button after filling all the required details. This will generate the PDF report and send
[
![printreport](https://github.com/mfrony2003/LabReport/assets/26355258/a2bc8b0f-15eb-4335-8304-f7a3ad471ad9)
](url)


   

