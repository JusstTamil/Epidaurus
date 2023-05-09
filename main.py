from tkinter import *

window = Tk()
window.geometry("780x488")
window.title('Epidaurus')
window.resizable(width=False, height=False)

def clearFrame(e):
    for widget in e.winfo_children():
       widget.destroy()

def createCanvas():
    c=Canvas(window, width=780,height=488)
    c.pack(fill='both',expand=True)
    c.create_image(0,0, anchor=NW, image=b)

def getDetails():
    clearFrame(window)
    createCanvas()
    Label(window, text='Name').place(x=220, y=100)
    nameInput = Entry(window, width=50)
    nameInput.place(x=270, y=100)
    name = nameInput.get()
    Label(window, text='Age').place(x=220, y=150)
    ageInput = Entry(window, width=50)
    ageInput.place(x=270, y=150)
    age = ageInput.get()

def sicknessAnalysis():
    clearFrame(window)
    createCanvas()
    Label(window, text="Sickness Analysis", font=("Bookman Old Style", 20, "bold"), bg="#000000", fg="#ecf0f3", padx=10, pady=10).place(x=255, y=20)
    Label(window, text='Please Select the Symptoms that you have been experiencing.').place(x=225, y= 90)
    commonSymptoms=Canvas(window)
    commonSymptoms.place(x=40, y=120)
    Label(commonSymptoms, text='Common Symptoms : ',width=20, anchor='w').grid(column=0, row=0)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=0, row=1, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=1, row=1, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=2, row=1, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=3, row=1, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=0, row=2, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=1, row=2, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=2, row=2, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=3, row=2, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=0, row=3, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=1, row=3, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=2, row=3, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=3, row=3, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=0, row=4, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=1, row=4, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=2, row=4, padx=2, pady=2)
    Button(commonSymptoms, text='Lorem Ipsum', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10).grid(column=3, row=4, padx=2, pady=2)

b=PhotoImage(file="D:/EPIDAURUSMARK1/bg.png")
c=Canvas(window, width=780,height=488)
c.pack(fill='both',expand=True)
c.create_image(0,0, anchor=NW, image=b)
c.create_text(400,100,text='EPIDAURUS',font=('Pristina',50 ,'bold'), fill='#ecf0f3')

Button(window, text='Sickness Analysis', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'), command=getDetails).place(x=300, y=180)
Button(window, text='Diets', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial')).place(x=300, y=250)
Button(window, text='About', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial')).place(x=300, y=320)
Label(window, text='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium quae, libero amet architecto cumque, repellat, delectus cum eius maiores nisi dolor! Inventore suscipit repellat dolorum.', wraplength=781, bg='#000', fg='#fff').place(x=7, y=449)

window.mainloop()
