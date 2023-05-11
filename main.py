from tkinter import *
from sqlite3 import *
from symptomStorage import *

window = Tk()
window.geometry("780x488")
window.title('Epidaurus')
window.resizable(width=False, height=False)
window.iconbitmap(r'favicon.ico')

symptoms = []

def clearFrame(e):
    for widget in e.winfo_children():
       widget.destroy()

def createCanvas():
    global c
    c=Canvas(window, width=780,height=488)
    c.grid(column=0, row=0, sticky='nsew')
    c.create_image(0,0, anchor=NW, image=b)

def getDetails():
    clearFrame(window)
    createCanvas()
    global nameInput, ageInput, bgInput, genderInput, dobInput
    c.create_text(400,50+20,text='Details',font=('Bookman Old Style',30), fill='#ecf0f3')
    # getting name
    Label(window, text='Name :').place(x=220, y=100+20)
    nameInput = Entry(window, width=50)
    nameInput.insert(0,"Enter your Name")
    nameInput.place(x=270, y=100+20)
    # getting age
    Label(window, text='Age :').place(x=220, y=150+20)
    ageInput = Entry(window, width=50)
    ageInput.insert(0,"Enter your Age")
    ageInput.place(x=270, y=150+20)
    # getting blood group
    Label(window, text='Blood Group :').place(x=220, y=250+20)
    bgInput = Entry(window, width=41)
    bgInput.insert(0,"Enter your Blood Group")
    bgInput.place(x=320, y=250+20)
    # getting gender
    Label(window, text="Gender :").place(x=220, y=200+20)
    genderInput = Entry(window, width=47)
    genderInput.place(x=286, y=200+20)
    '''sampleGender = StringVar()
    Radiobutton(window, text="Male", variable='sampleGender', value="male").place(x=290, y=200+20)
    Radiobutton(window, text="Female", variable='sampleGender', value="female").place(x=370, y=200+20)
    Radiobutton(window, text="Other", variable='sampleGender', value="other").place(x=460, y=200+20)'''
    # getting Date of Birth
    Label(window, text="Date of Birth :").place(x=220, y=320)
    dobInput = Entry(window, width=41)
    dobInput.place(x=320, y=300+20)
    # the submit button
    Button(window, text='Submit', bg='#1c3599', fg='#ecf0f3', width=20, padx=5, pady=5, command=sicknessAnalysis).place(x=410, y=360)

def addSymptoms(symptom):
    symptoms.append(symptom)

def sicknessAnalysis():
    global name, age, bloodGroup, dob, gender
    name = nameInput.get()
    age = ageInput.get()
    bloodGroup = bgInput.get()
    gender = genderInput.get()
    dob = dobInput.get()
    clearFrame(window)
    createCanvas()
    Label(window, text="Sickness Analysis", font=("Bookman Old Style", 20, "bold"), bg="#000000", fg="#ecf0f3", padx=10, pady=10).place(x=255, y=20)
    Label(window, text='Please Select the Symptoms that you have been experiencing.').place(x=225, y= 90)
    commonSymptoms=Canvas(window)
    commonSymptoms.place(x=40, y=130)
    createCommonSymptoms(commonSymptoms)

def createCommonSymptoms(createdSymptomsCanvas):
    clearFrame(createdSymptomsCanvas)
    Label(createdSymptomsCanvas, text='Common Symptoms : ',width=20, anchor='w').grid(column=0, row=0)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Next Part -> ', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:createSevereSymptoms(createdSymptomsCanvas)).grid(column=3, row=5, padx=2, pady=2)

def createSevereSymptoms(createdSymptomsCanvas):
    clearFrame(createdSymptomsCanvas)
    Label(createdSymptomsCanvas, text='Severe Symptoms : ',width=20, anchor='w').grid(column=0, row=0)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=1, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=2, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=3, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=0, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=1, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=2, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Lorem Ipsum')).grid(column=3, row=4, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='<- Previous Part', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:createCommonSymptoms(createdSymptomsCanvas)).grid(column=0, row=5, padx=2, pady=2)
    Button(createdSymptomsCanvas, text='Submit', bg='#000', fg='#ecf0f3', width=20, padx=5, pady=5, command=patientHistory).grid(column=3 , row=5, padx=2, pady=2)

predictedDisease = diseasePrediction(symptoms)

def patientHistory():
    global name, age, dob, gender, bloodGroup
    clearFrame(window)
    createCanvas()
    c.create_text(400, 50-20,text="Patient History",font=('Bookman Old Style',30), fill='#ecf0f3')
    # name
    Label(window, text='Name', font=('Cambria')).place(x=70, y=100)
    Label(window, text=str(name), wraplength=300, width=50, font=('Cambria')).place(x=250, y=100-20)   
    # age
    Label(window, text='Age', font=('Cambria')).place(x=70, y=150)
    Label(window, text=str(age), wraplength=300, width=50, font=('Cambria')).place(x=250, y=150-20)
    # date of birth
    Label(window, text='Date of Birth', font=('Cambria')).place(x=70, y=200)
    Label(window, text=str(dob), wraplength=300, width=50, font=('Cambria')).place(x=250, y=200-20)
    # gender
    Label(window, text='Gender', font=('Cambria')).place(x=70, y=250)
    Label(window, text=str(gender), wraplength=300, width=50, font=('Cambria')).place(x=250, y=250-20)
    # Blood Group
    Label(window, text='Blood Group', font=('Cambria')).place(x=70, y=300)
    Label(window, text=str(bloodGroup), wraplength=300, width=50, font=('Cambria')).place(x=250, y=300-20)
    #symptoms
    Label(window, text='Symptoms', font=('Cambria')).place(x=70, y=350)
    Label(window, text= str(symptoms), wraplength=300, width=50, font=('Cambria')).place(x=250, y=350-20)
    # predicted Disease
    Label(window, text='Predicted Diseases: ', font=('Cambria')).place(x=70, y=400)
    Label(window, text=str(predictedDisease), wraplength=300, width=50, font=('Cambria')).place(x=250, y=400-20)
    # go to home button
    Button(window, text='Go to home', padx=2, pady=2, command=goHome).place(x=350, y=445)

def goHome():
    clearFrame(window)
    home()
    
def home():
    global b
    b=PhotoImage(file="bg.png")
    c=Canvas(window, width=780,height=488)
    c.pack(fill='both',expand=True)
    c.create_image(0,0, anchor=NW, image=b)
    c.create_text(400,100,text='EPIDAURUS',font=('Pristina',50 ,'bold'), fill='#ecf0f3')

    Button(window, text='Sickness Analysis', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'), command=getDetails).place(x=300, y=180)
    Button(window, text='Diets', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial')).place(x=300, y=250)
    Button(window, text='About', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial')).place(x=300, y=320)
    Label(window, text='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium quae, libero amet architecto cumque, repellat, delectus cum eius maiores nisi dolor! Inventore suscipit repellat dolorum.', wraplength=781, bg='#000', fg='#fff').place(x=7, y=449)

home()

window.mainloop()
