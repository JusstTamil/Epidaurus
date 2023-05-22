common_symptoms={
    "Fever":["Pneumonia","Chikungunya","Dengue"],
    "High fever":["Typhoid","BPlague","PPlague","SPlague","Diphteria"],
    "Stomach pain":["Typhoid"],
    "Constipation":["Typhoid","Amoebiasis"],
    "Headache":["Dengue","Pneumonia","BPlague","PPlague"],
    "Chills":["Common cold","Pneumonia"],
    "Cough":["Common cold","Pneumonia"],
    "Tiredness":["Common cold","Pneumonia"],
    "Sore throat":["Common cold"],
    "Muscle & joint pain":["Chikungunya","Dengue","Ascariasias","Malaria"],
    "Weakness":["Typhoid","SPlague"],
    "Fatigue":["HepatitisB","Malaria"],
    "Abdominal pain":["Dysentry","Amoebiasis"]
}

delicate_symptoms={
    "Loss of apetite":"Typhoid",
    "Bluish lips & nails":"Pneumonia",
    "Blood & mucus in stool":"Dysentry",
    "Swellings in under arm region":"BPlague",
    "Chest pain & shortness of breath":"PPlague",
    "Skin turns black(suddenly)":"SPlague",
    "Suffocation":"Diphteria",
    "Contraction of voluntary muscles":"Tetanus",
    "Nasal congestion & discharge":"Common cold",
    "Swellings in body":"Chikungunya",
    "Bleeding from mouth,nose & gum":"Dengue",
    "Jaundice & nausea":"HepatitisB",
    "Vomiting & shivering":"Malaria",
    "Scaly lesions with itching":"Ring worms",
}
'''x=[]
y=int(input("Enter no. of entries:"))
z=""
for a in range(y):
    z=input("Enter the symptom:")
    x.append(z)
    z=""
print(x)
'''


#Similarity check
def diseasePrediction(x):
    predictcommon=list()
    predictdelicate=[]

    for i in x:
        for j in common_symptoms:
            if i==j:
                predictcommon.extend(common_symptoms[j])
        else:
            for j in delicate_symptoms:
                if i==j:
                    predictdelicate.append(delicate_symptoms[j])

    def find_common(list1, list2):
        
        common = []
        for item in list1:
            if item in list2:
                common.append(item)
        return common
    
    predictfinal=[]
    predictfinal.extend(find_common(predictcommon,predictdelicate))
    
    def der(list):
        global predictedDisease
        predictedDisease = []
        xsd=[]
        jay={}
        main=[]
        for i in list:
            jay[list.count(i)]=i
        xsd.extend(jay.keys())
        main.append(jay[max(xsd)])
        return main 
    pd = der(predictcommon)
    pd.extend(predictfinal)
    for i in pd:
        if i in predictedDisease:
            continue
        else:
            predictedDisease.append(i)
    return predictedDisease
