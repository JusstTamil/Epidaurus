from tkinter import *

class Window(Frame):
    def __init__(self, master=None, bg="#88f8bc"):
        Frame.__init__(self, master)
        self.master = master
        self.master.configure(background=bg)

window = Tk()
window.geometry("400x400")
window.title('Epidaurus')
window.resizable(width=False, height=False)
root = Window(window)

def sicknessAnalysis():
    print('Hi')

Label(window, text="Epidaurus", background='#7bb4e3', font=('Pristina', 40), padx=10, pady=10).place(x= 105, y= 50)
Button(window, text='Sickness Analysis', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial'), command=sicknessAnalysis).place(x=108, y=180)
Button(window, text='Diets', background='#1c3599', fg="#ecf0f3", padx=10, pady=10, width=19, font=('Arial')).place(x=108, y=250)
Label(window, text='Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium quae, libero amet architecto cumque, repellat, delectus cum eius maiores nisi dolor! Inventore suscipit repellat dolorum.', wraplength=400, bg='#000', fg='#fff').place(x=4, y=350)

window.mainloop()