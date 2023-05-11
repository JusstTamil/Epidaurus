disease = {
    'Typhoid':["High fever","Weakness","Stomach pain","Constipation","Headache","Loss of apetite"],
    'Pneumonia':["Fever","Chills","Cough","Headache","Bluish lips and nails"],
    'Dysentry':["Abdominal pain","Blood and mucus in the stool"],
    'BPlague':["High fever", "Headache","Enlargement of axillary lymph nodes"],
    'PPlague':["High fever", "Headache","Chest pain","Blood in sputum","Shortness of breath"],
    'SPlague':["High fever","Extreme weakness","Skin turns black"],
    'Diphtheria':["High fever","Suffocation"],
    'Tetanus':["Contraction of voluntary muscles"],
    'Common_Cold':["Nasal Congestion and discharge","Sore throat","Hoarseness","Cough"],
    'Chikungunya':["Fever","Joint pain","Enlargement of lymph nodes"],
    'Dengue':["Fever","Severe frontal headache","Pain in muscle and joints","Dizziness","Bleeding from mouth,nose and gums"],
    'HepatitisB':["Jaundice","Fatigue","Nausea"],
    'Malaria':["Vomiting","Bodyache","Fatigue","Shivering","Muscular pain"],
    'Amoebiasis':["Constipation","Abdominal pain and cramps"],
    'Ascariasis':["Internal bleeding","Anaemia","Muscular pain"],
    'Ring_worms':["Dry","scaly lesions accompanied with itching"]
}

BMI={"18-29":22.5,"30-39":29.9,"40-49":24.9,"50-59":29.9,"60-70":30}
Diet={"Normal":1900,"Under weight":2200,"Over weight":1700}

def diseasePrediction(symptoms):
    pdisease = []

    for i in disease:
        for j in disease[i]:
            for k in symptoms:
                if j == k:
                    pdisease.append(i)
    x = {}
    for i in pdisease:
        x[pdisease.count(i)] = i

    y = list(x.keys())

    z = max(y)

    predictedDisease = x[z] 

    return predictedDisease

# print(diseasePrediction(["Fever","Stomach pain","Jaundice","Cough","Chill"]))