from tkinter import *
from tkinter import font
import time
from sqlite3 import *
from datetime import date
from symptomStorage import *
from webbrowser import *
from tkinter import messagebox

#d:/EPIDAURUS/
w=Tk()

#Using piece of code from old splash screen
width_of_window = 780
height_of_window = 488
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    window = Tk()
    window.geometry("780x488")
    window.title('Epidaurus')
    window.resizable(width=False, height=False)
    window.iconbitmap('favicon.ico')


    def clearFrame(e):
        for widget in e.winfo_children():
           widget.destroy()

    def createCanvas():
        global c
        c=Canvas(window, width=780,height=488)
        c.grid(column=0, row=0, sticky='nsew')
        c.create_image(0,0, anchor=NW, image=b)
    
    #Opening github link
    def callback(url):
        open_new(url)

    def opennewwindow():
     #About page function
     #    
        clearFrame(window)
        createCanvas()
        c.create_text(415,18,text='About',font=('Bookman Old Style',20,"bold"), fill='#ecf0f3')
        label1 = Label(c,bg = "#88f8bc",text = '''What concerns about your health today?
                          
Check your symptoms and find out what could be causing them. It is fast, free and convenient to use. We would also guide you to the correct diet you should follow according to your age group. This app is still underdevelopment so kindly be in touch until the completion.

Legal Notice:
                          This checkup is not a diagnosis. It is for informational purposes only and is not qualified medical opinion. Do not use in emergencies. In case of a health emergency, contact your personal medical consultant or Doctor. Your data is safe with us. Your medical history will not be shared with anyone

Developers:
                          Application development is the process of creating software applications that run on a device, and a typical application utilizes a network connection to work with remote computing resources. we are glad to introduce you the creators of this legendary invention:
                          •	Jayananthan G
                          •	Umaa Jagad Prakash J
                          •	Sivaprakash P 
                          •	SankaraNarayanan S
Note: You can get the source code of the application by clicking the below button

    ''',justify = LEFT,font=("Roquen",11,"bold"),wraplength=700).place(x=40,y=30)
        Button(window,text='Go to home', padx=2,bg="black",fg="white",pady=2, command=goHome).place(x=350, y=460)
        Button(window,text="Github",padx=2,bg="black",fg="white",pady=2, command=lambda:callback("https://github.com/JusstTamil/Epidaurus")).place(x=365,y=418)

    def diets():
            clearFrame(window)
            createCanvas()
            c.create_text(400,30,text='DIET',font=('Bookman Old Style',20,"bold"), fill='#ecf0f3')
            c.create_text(205,105,text='Select your age group:',font=('Bookman Old Style',15,"bold"), fill='#ecf0f3')
            c.create_text(218,235,text='Select your gender:',font=('Bookman Old Style',15,"bold"), fill='#ecf0f3')
            c.create_text(228,285,text='Enter Height(cm):',font=('Bookman Old Style',15,"bold"), fill='#ecf0f3')
            c.create_text(225,315,text='Enter Weight(Kg):',font=('Bookman Old Style',15,"bold"), fill='#ecf0f3')   

            
            def printResults():
                print(var1.get())


            '''age_tf=Label(window, text="Select your Age Group ")
            age_tf.place(x=337,y=60)'''

            var1 = IntVar()
            var1.set(0)


            global age_rb
            age_rb=Radiobutton(window, text="18-24", variable=var1, value=1, command=printResults).place(x=335,y=95)
            age_rb=Radiobutton(window, text="25-29", variable=var1, value=2, command=printResults).place(x=335,y=115)
            age_rb=Radiobutton(window, text="30-34", variable=var1, value=3, command=printResults).place(x=335,y=135)
            age_rb=Radiobutton(window, text="35-39", variable=var1, value=4, command=printResults).place(x=335,y=155)
            age_rb=Radiobutton(window, text="40-44", variable=var1, value=5, command=printResults).place(x=335,y=175)
            age_rb=Radiobutton(window, text="45-49", variable=var1, value=6, command=printResults).place(x=415,y=95)
            age_rb=Radiobutton(window, text="50-54", variable=var1, value=7, command=printResults).place(x=415,y=115)
            age_rb=Radiobutton(window, text="55-59", variable=var1, value=8, command=printResults).place(x=415,y=135)
            age_rb=Radiobutton(window, text="60-64", variable=var1, value=9, command=printResults).place(x=415,y=155)
            age_rb=Radiobutton(window, text="65-70", variable=var1, value=10, command=printResults).place(x=415,y=175)

                    

            var=IntVar()
            var.set(0)

            male_rb = Radiobutton(
                window,
                text = 'Male',
                variable = var,
                value = 1
            )
            male_rb.place(x=335,y=225)

            female_rb = Radiobutton(
                window,
                text = 'Female',
                variable = var,
                value = 2
            )
            female_rb.place(x=415,y=225)
                
            #Ujp the great

            def bmi_index(bmi):
                #for males 
                if var.get()==1:
                    if var1.get()==1:
                        if (bmi < 27.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            2400-2600 calories (for Sedentary lifestyle),
            2600-2800 calories (for Moderately Active Lifestyle),
            2800-3000 calories (for Active Lifestyle).''')
                        elif (27.1<=bmi<=27.6):
                            messagebox.showinfo('bmi-Diets', '''BMI = {bmi} is Normal,
            Calories required :
            2400 calories (for Sedentary Lifestyle),
            2800 calories (for Moderately Active Lifestyle),
            3000 calories (for Active Lifestyle).''' )
                        elif (bmi > 30.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                    
                        elif (bmi > 27.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')
                        
                    elif var1.get()==2:
                        if (bmi < 27.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            2400-2600 calories (for Sedentary lifestyle),
            2600-2800 calories (for Moderately Active Lifestyle),
            2800-3000 calories (for Active Lifestyle).''')
                        elif (27.9<=bmi<=28.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            2400 calories (for Sedentary Lifestyle),
            2800 calories (for Moderately Active Lifestyle),
            3000 calories (for Active Lifestyle).''')
                        elif (bmi > 30.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 28.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!''')

                    elif var1.get()==3:
                        if (bmi < 29.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            2400-2600 calories (for Sedentary lifestyle),
            2600-2800 calories (for Moderately Active Lifestyle),
            2800-3000 calories (for Active Lifestyle).''')
                        elif (29.6<=bmi<=30.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            2400 calories (for Sedentary Lifestyle),
            2800 calories (for Moderately Active Lifestyle),
            3000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==4:
                        if (bmi < 30.2):
                            messagebox.showinfo('''bmi-Diets', f'BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (30.2<=bmi<=30.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 31.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==5:
                        if (bmi < 30.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (30.1<=bmi<=30.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 31.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==6:
                        if (bmi < 29.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (29.7<=bmi<=30.5):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600(for Sedentary Lifestyle),
            1800(for Moderately Active Lifestyle),
            2200(for Active Lifestyle).''')
                        elif (bmi > 32.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==7:
                        if (bmi < 30.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (30.1<=bmi<=30.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 31.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==8:
                        if (bmi < 29.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (29.8<=bmi<=30.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==9:
                        if (bmi < 30.5):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories (for Active Lifestyle).''')
                        elif (30.5<=bmi<=31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 32.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==10:
                        if (bmi < 30.0):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1800-2000 calories (for Sedentary lifestyle),
            2000-2200 calories (for Moderately Active Lifestyle),
            2200-2400 calories(for Active Lifestyle).''')
                        elif (30.0<=bmi<=30.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1600 calories (for Sedentary Lifestyle),
            1800 calories (for Moderately Active Lifestyle),
            2200 calories (for Active Lifestyle).''')
                        elif (bmi > 31.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1100-1300 calories (for Sedentary lifestyle),
            1200-1400 calories (for Moderately Active Lifestyle),
            1300-1500 calories (for Active Lifestyle).''')
                        
                        elif (bmi > 30.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1200-1300 calories (for Sedentary lifestyle),
            1300-1400 calories (for Moderately Active Lifestyle),
            1400-1500 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    else:
                        messagebox.showerror('bmi-Diets', 'wrong')

                #for females

                if var.get()==2:
                    if var1.get()==1:
                        if (bmi < 27.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (27.1<=bmi<=27.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')

                        elif (bmi > 28.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        elif (bmi > 27.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')
                        
                    elif var1.get()==2:
                        if (bmi < 27.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (27.9<=bmi<=28.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 29.42):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 28.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==3:
                        if (bmi < 29.6):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1500-1700 calories (for Sedentary lifestyle),
            1700-1900 calories (for Moderately Active Lifestyle),
            1900-2100 calories (for Active Lifestyle).''')
                        elif (29.6<=bmi<=30.4):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        elif (bmi > 30.4):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                    
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==4:
                        if (bmi < 30.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (30.2<=bmi<=30.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 30.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle). ''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==5:
                        if (bmi < 30.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (30.1<=bmi<=30.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000(for Active Lifestyle).''')
                        elif (bmi > 31.56):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 30.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==6:
                        if (bmi < 29.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (29.7<=bmi<=30.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 30.3):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==7:
                        if (bmi < 30.1):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1500-1700 calories (for Sedentary lifestyle),
            1700-1900 calories (for Moderately Active Lifestyle),
            1900-2100 calories (for Active Lifestyle).''')
                        elif (30.1<=bmi<=30.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.5):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 30.7):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==8:
                        if (bmi < 29.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (29.8<=bmi<=30.4):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 30.4):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==9:
                        if (bmi < 30.5):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (30.5<=bmi<=31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.9):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 31.2):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories (for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')

                    elif var1.get()==10:
                        if (bmi < 30):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Underweight,
            Calories required :
            1600-1800 calories (for Sedentary lifestyle),
            1800-2000 calories (for Moderately Active Lifestyle),
            2000-2200 calories (for Active Lifestyle).''')
                        elif (30<=bmi<=31):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Normal,
            Calories required :
            1400 calories (for Sedentary Lifestyle),
            1600 calories (for Moderately Active Lifestyle),
            2000 calories (for Active Lifestyle).''')
                        elif (bmi > 31.8):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Obesity,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1200 calories (for Moderately Active Lifestyle),
            1200-1300 calories (for Active Lifestyle).''')
                        elif (bmi > 31):
                            messagebox.showinfo('bmi-Diets', f'''BMI = {bmi} is Overweight,
            Calories required :
            1000-1100 calories (for Sedentary lifestyle),
            1100-1300 calories (for Moderately Active Lifestyle),
            1200-1400 calories(for Active Lifestyle).''')
                        else:
                            messagebox.showerror('bmi-Diets', 'something went wrong!')


                    else:
                        messagebox.showerror('bmi-Diets', 'wrong')

            def calculate_bmi():
                kg = int(weight_tf.get())
                m = int(height_tf.get())/100
                bmi = kg/(m*m)
                bmi = round(bmi, 1)
                bmi_index(bmi)

            '''gen_lb = Label(
                window,
                text='Select Gender'
            )
            gen_lb.place(x=300,y=215)'''

            frame2 = Frame(c)
            frame2.place()

            '''height_lb = Label(
                window,
                text="Enter Height (cm)  "
            )
            height_lb.place(x=285,y=245)'''

            '''weight_lb = Label(
                window,
                text="Enter Weight (kg)  ",

            )
            weight_lb.place(x=285,y=275)'''

            height_tf = Entry(
                window,
            )
            height_tf.place(x=335,y=275
                            )

            weight_tf = Entry(
                window,
            )
            weight_tf.place(x=335,y=305)
            
            Button(window,text='Go to home', padx=4,bg="black",fg="white",pady=4, command=goHome).place(x=350, y=420)
            cal_btn = Button(
                window,
                text='Calculate',
                bg='#589a59', fg='#ecf0f3',
                command=calculate_bmi
            )
            cal_btn.place(x=335,y=335)

    def getDetails():
        clearFrame(window)
        createCanvas()
        global nameInput, ageInput, bgInput, genderInput, dobInput
        c.create_text(415,50+20,text='Details',font=('Bookman Old Style',30), fill='#ecf0f3')
        # getting name
        Label(window, text='Name :').place(x=220, y=100+20)
        nameInput = Entry(window, width=50)
        nameInput.place(x=270, y=100+20)
        # getting age
        Label(window, text='Age :').place(x=220, y=150+20)
        ageInput = Entry(window, width=50)
        ageInput.place(x=270, y=150+20)
        # getting blood group
        Label(window, text='Blood Group :').place(x=220, y=250+20)
        bgInput = Entry(window, width=41)
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
        Button(window, text='Submit', bg='#589a59', fg='#ecf0f3', width=20, padx=5, pady=5, command=sicknessAnalysis).place(x=410, y=375)
    
    def addSymptoms(symptom):
        symptoms.append(symptom)
        e = len(symptomDisplay.get())
        symptomDisplay.insert(e, symptom + ', ')

    def sicknessAnalysis():
        global name, age, bloodGroup, dob, gender, symptomDisplay
        name = nameInput.get()
        age = ageInput.get()
        bloodGroup = bgInput.get()
        gender = genderInput.get()
        dob = dobInput.get()
        clearFrame(window)
        createCanvas()
        c.create_text(415,50+20,text='Sickness Analysis',font=('Bookman Old Style',20,"bold"), fill='#ecf0f3')
        Label(window, text='Please Select the Symptoms that you have been experiencing. (For more accurate results, please select more than one)', wraplength=500).place(x=175, y= 100)
        symptomDisplay = Entry(window, width=114)
        symptomDisplay.place(x=40 ,y=160)
        symptomDisplay.insert(0, 'Entered Symptoms : ')
        commonSymptoms=Canvas(window)
        commonSymptoms.place(x=40, y=200)
        createCommonSymptoms(commonSymptoms)
    
    def createCommonSymptoms(createdSymptomsCanvas):
        clearFrame(createdSymptomsCanvas)
        Label(createdSymptomsCanvas, text='Common Symptoms : ',width=20, anchor='w').grid(column=0, row=0)
        Button(createdSymptomsCanvas, text='Fever', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Fever')).grid(column=0, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='High fever', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('High fever')).grid(column=1, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Stomach pain', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Stomach pain')).grid(column=2, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Constipation', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Constipation')).grid(column=3, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Headache', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Headache')).grid(column=0, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Chills', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Chills')).grid(column=1, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Cough', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Cough')).grid(column=2, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Tiredness', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Tiredness')).grid(column=3, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Sore throat', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Sore throat')).grid(column=0, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Muscle & joint pain', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Muscle & joint pain')).grid(column=1, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Weakness', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Weakness')).grid(column=2, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Fatigue', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Fatigue')).grid(column=3, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Abdominal pain', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Abdominal pain')).grid(column=0, row=4, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Next Part -> ', bg='#589a59', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:createSevereSymptoms(createdSymptomsCanvas)).grid(column=3, row=4, padx=2, pady=2)
    
    def createSevereSymptoms(createdSymptomsCanvas):
        clearFrame(createdSymptomsCanvas)
        Label(createdSymptomsCanvas, text='Severe Symptoms : ',width=20, anchor='w').grid(column=0, row=0)
        Button(createdSymptomsCanvas, text='Loss of apetite', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Loss of apetite')).grid(column=0, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Bluish lips & nails', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Bluish lips & nails')).grid(column=1, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Blood & mucus in stool', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Blood & mucus in stool')).grid(column=2, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Swellings in under arm region', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Swellings in under arm region')).grid(column=3, row=1, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Chest pain,shortness of breath', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Chest pain & shortness of breath')).grid(column=0, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Skin turns black(suddenly)', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Skin turns black(suddenly)')).grid(column=1, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Suffocation', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Suffocation')).grid(column=2, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Contraction of muscles', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Contraction of Muscles')).grid(column=3, row=2, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Nasal congestion & discharge', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Nasal congestion & discharge')).grid(column=0, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Swellings in body', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Swellings in body')).grid(column=1, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Bleeding from mouth,nose', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Bleeding from mouth,nose')).grid(column=2, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Jaundice & nausea', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Jaundice & nausea')).grid(column=3, row=3, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Vomiting & shivering', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Vomiting & shivering')).grid(column=1, row=4, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Scaly lesions with itching', bg='#1c3599', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:addSymptoms('Scaly lesions with itching')).grid(column=2, row=4, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='<- Previous Part', bg='#589a59', fg='#ecf0f3', width=20, padx=10, pady=10, activeforeground='#fff', activebackground='#000', command=lambda:createCommonSymptoms(createdSymptomsCanvas)).grid(column=0, row=4, padx=2, pady=2)
        Button(createdSymptomsCanvas, text='Submit', bg='#d2150d', fg='#ecf0f3', width=20, padx=5, pady=5, command=patientHistory).grid(column=3 , row=4, padx=2, pady=2)
    
    def patientHistory():
        global name, age, dob, gender, bloodGroup, predictedDisease
        # Displaying the patient history
        clearFrame(window)
        createCanvas()
        c.create_text(415, 50-20,text="Patient History",font=('Bookman Old Style',30), fill='#ecf0f3')
        # name
        Label(window, text='Name', font=('Cambria')).place(x=70, y=100-20)
        Label(window, text=str(name), wraplength=300, width=50, font=('Cambria')).place(x=250, y=100-20)   
        # age
        Label(window, text='Age', font=('Cambria')).place(x=70, y=150-20)
        Label(window, text=str(age), wraplength=300, width=50, font=('Cambria')).place(x=250, y=150-20)
        # date of birth
        Label(window, text='Date of Birth', font=('Cambria')).place(x=70, y=200-20)
        Label(window, text=str(dob), wraplength=300, width=50, font=('Cambria')).place(x=250, y=200-20)
        # gender
        Label(window, text='Gender', font=('Cambria')).place(x=70, y=250-20)
        Label(window, text=str(gender), wraplength=300, width=50, font=('Cambria')).place(x=250, y=250-20)
        # Blood Group
        Label(window, text='Blood Group', font=('Cambria')).place(x=70, y=300-20)
        Label(window, text=str(bloodGroup), wraplength=300, width=50, font=('Cambria')).place(x=250, y=300-20)
        #symptoms
        Label(window, text='Symptoms', font=('Cambria')).place(x=70, y=350-20)
        Label(window, text= str(symptoms), wraplength=450, width=50, font=('Cambria')).place(x=250, y=350-20)
        # predicted Disease
        predictedDisease = diseasePrediction(symptoms)
        Label(window, text='Predicted Diseases: ', font=('Cambria')).place(x=70, y=415-20)
        Label(window, text=str(predictedDisease), wraplength=450, width=50, font=('Cambria')).place(x=250, y=415-20)
        # entering into the database
        con = connect('patientHistory.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO patientHistory VALUES (?,?,?,?,?,?,?,?)''',(now, name, age, dob, gender, bloodGroup, str(symptoms), str(predictedDisease)))
        con.commit()
        con.close()
        # go to home button
        Button(window, text='Go to home', bg="#d2150d", fg="#ecf0f3",padx=2, pady=2, command=goHome).place(x=350, y=445)
    

    
    def goHome():
        clearFrame(window)
        home()
    
    def home():
        global b, now, symptoms
        now = date.today().strftime('%d/%m/%y')
        symptoms = []
        b=PhotoImage(file="bg.png")
        c=Canvas(window, width=780,height=488)
        c.pack(fill='both',expand=True)
        c.create_image(0,0, anchor=NW, image=b)
        c.create_text(415,100,text='EPIDAURUS',font=('Pristina',50 ,'bold'), fill='#ecf0f3')

        Button(window, text='Sickness Analysis', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'), command=getDetails).place(x=300, y=180)
        Button(window, text='Diets', background='#589a59', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'),command=diets).place(x=300, y=250)
        Button(window, text='About', background='#d2150d', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'),command=opennewwindow).place(x=300, y=320)
        Label(window, text='''DISCLAIMER:
All our results are purely based on statistical analysis and prediction,it may be wrong in some rare cases,so we request you not to take it too serious.If any of those symptoms sustain for a long period of time please consult your medical adviser.''', wraplength=775, bg='#000', fg='#fff').place(x=23, y=433)

    home()

    window.mainloop()


Frame(w, width=780, height=488, bg='#272727').place(x=0,y=0)
label1=Label(w, text='EPIDAURUS', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Pristina", 50, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=170,y=185)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 20))
label2.place(x=10,y=440)

#making animation

image_a=PhotoImage(file='c2.png')
image_b=PhotoImage(file='c1.png')




for i in range(2): #no. of loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=355, y=300)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=375, y=300)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=395, y=300)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=4150, y=300)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=355, y=300)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=375, y=300)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=395, y=300)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=415, y=300)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=355, y=300)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=375, y=300)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=395, y=300)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=415, y=300)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=355, y=300)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=375, y=300)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=395, y=300)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=415, y=300)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()

