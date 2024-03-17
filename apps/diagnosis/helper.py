

def getTotalPrice(objpatientDiagnosis):
    # do code using username and slug for data1 and data2 here 
   diagnosisList = {}   
   total=0
   patientName= "" 
   for pd in objpatientDiagnosis:
            current_key = pd.myPatientReport_id
            patientName=pd.patient            
            diagnosisList.setdefault(current_key, []).append( 
                  { 'patientdiagnosisId':pd.id, 'name':pd.Diagnosis.name, 'price':pd.Diagnosis.price,'Diagnosis_id':pd.Diagnosis.id,
                   'specimen':pd.Diagnosis.specimen,'specimen_id':pd.Diagnosis.specimen_id,'myPatientSpecimen_id':pd.myPatientSpecimen_id,'isChecked':pd.isChecked})
            total+=pd.Diagnosis.price

   return (diagnosisList, total,patientName)
