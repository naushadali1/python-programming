def lung(): # this function shows the list of diseases and their treatment for Lung
    print("Lungs diseases are:\n 1.Asthma \n 2.Pnemonia \n 3.TB \n 4. Lung Cancer\n")
    disease = input("Enter Disese name for the list of treatments: ")
    if disease.upper =='ASTHMA':
        print('Asthma Treatments  are: \n 1.Bronchial thermoplasty \n 2. nebulizer \n 3. Complementary Therapies \n 4. Antibiotics')
    elif disease.upper() == "PNEMONIA" :
        print ("Pneumonia Treatments are: \n 1.Antibiotic(Azithromycin, Clarithromycin etc) \n 2.Penicillin \n 3.Erythromyci")
    elif disease.upper() == 'TB' :
        print("TB Treatments are: \n 1. 2 Atibiotics(iosoniazid and rafimpaci)\n 2. 2 Additional Antibiotics(pyrazinamiole and Ethambutol)")
    elif disease.upper() == 'LUNG CANCER' :
        print("Lung Cancer Treatments are: \n 1. Radiotherapy \n 2. Chemotherapy\n 3. Surgery \n 4. Alternative Medicine \n")
    else :
        print("Please input the correct disease name as mentioned above")  #testing
                                   
def heart(): # this function shows the list of diseases and their treatment for Heart
     print("Heart Diseases are: \n1. Heart attack \n 2. Angina \n 3. Hypertension \n 4. Arrythmia\n")
     disease=input("Enter Diseases Name for treatment List: ")
     if disease.upper()== 'HEART ATTACK' :
        print("Heart Attack Treatments are: \n 1. Surgery \n 2. Statin \n 3. morphine \n 4. Asprin \n 5. Clot busters \n")
     elif disease.upper()=='ANGINA':
        print("Angina Treatments are: \n 1. Calcium Channel Blockers \n 2. Randazine \n 3. Beta Blockers \n 4. Nitrates")
     elif disease.upper()== 'HYPERTENSION':
        print("Hypertension Treatments are: \n 1. Aldosteron Antagonist\n 2. Renin Inhibators \n 3. Vasodilators \n 3. Water Pills(Diuretics) \n ")
     elif disease.upper()=='ARRYTHMIA':
        print("Arrythmia Treatments are: \n 1. surgery\n ---> coronary bypass \n ---> Pacemaker\n ---> C  athetar Abalation \n 2. Cardioversion\(therapy)")
     else :
        print("Please input the correct disease name as mentioned above")

def liver(): # this function shows the list of diseases and their treatment for Liver
    print("Liver Diseases are: \n 1. Hepatitis \n 2. Liver Cirrhosis \n 3. Bile Duct \n 4. Jaundice \n")
    disease =input("Enter disease name for treatment list: ")
    if disease.upper()=='HEPATITIS':
        print(" Hepatitis Treatments are: \n 1. Corticosteriod \n 2. Azithioprine \n 3. Cyclosporine")
    elif disease.upper() == 'LIVER CIRRHOSIS':
        print("Liver Cirrhosis Treatments are: \n 1. Transplant Surgery \n 2. Metroprolol 3. Nadolol\n  4. Timolol")
    elif disease.upper()== 'BILE DUCT':
        print("Bile Duct Treatments are: \n 1. Cholecystectomy(Removal of Gall Bladder) \n 2. Antibiotics \n 3. Nepotoportoenterostomy(srgery to drain bile from live) \n")
    elif disease.upper()=='JAUNDICE':
        print("Jaundice Treatments are: \n 1. Antihistamines \n 2. Cholestyramine \n 3. Colestipol \n 4. Ceftriaxone \n")
    else :
        print("Please input the correct disease name as mentioned abovee")

def kidney(): # this function shows the list of diseases and their treatment for Kidney
    print("Kidney Diseases are: \n 1. Aquired Cystic Disease \n 2. Diabetes Insipidus \n 3. Kidney Stone \n 4. Renal Cancer \n")
    disease =input("Enter disease name for the list of treatments: ")
    if disease.upper()=='AQUIRED CYSTIC DISEASE':
        print("Acquired Cystic Diease Treatments are: \n 1. Surgery to reove cyst \n 2. Piercing and draing cyst")
    elif disease.upper()=='DIABETES INSIPIDUS':
        print("Diabetes Insipidus Treatments are: \n 1. Harmone Desmopressin \n 2. Ibuprofen \n 3. Tetracyclin \n 4. Lithium")
    elif disease.upper()=='KIDNEY STONE' :
        print("Kidney Stone Treatments are: \n 1. Surgery \n 2. Shock wave Lithotripsy \n 3. Ureteroscopy \n 4. Parcutaneous nephrolithotomy \n")
    elif disease.upper()=='RENAL CANCER':
        print("Renal cancer Treatments are: \n 1. Surgery: nephrectomy(removing the affected kidney) \n 2. Partial nephrectomy\(removing the tumor) \n 3. Rathiatherapy \n 4. Chemiotherapy \n")
    else :
        print("Please input the correct disease name as mentioned above")

    # from here the main program starts
print ("The program includes these organ names: \n 1.Lung \n 2.Heart \n 3.Liver \n 4.Kidney") 
i=""
while(i.upper()!="EXIT" ):  # execute the program while the user input "Exit"
 organ=input("Enter Organ Name :")
 if  organ.upper()=='LUNG':
    lung() #lung function call

 elif organ.upper()=='HEART':
    heart() # heart function call

 elif organ.upper()=='LIVER':
    liver() #liver function call

 elif organ.upper()=='KIDNEY':
    kidney() # lidney function call
 else : # it returns the statement when the user inputs an incorrect organ name
   print("Please enter correct Organ name")
 i=(input('Enter "Exit" to terminate the program Or Enter any character to Continue: '))