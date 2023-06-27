from tkinter import*
from tkinter.font import BOLD
import random

class BrainTrain:
    def __init__(self,window):
        self.root=window
        self.root.title("Brain Train")
        self.root.config(bg="#f8e91a")
        
        # self.imagen=PhotoImage(file="quini.png")
        # self.imgquini=Label(self.root,image=self.imagen)
        # self.imgquini.grid(row=0,column=0)
        
        self.frame = LabelFrame(self.root,text="Números para jugar")
        self.frame.grid(row=1, column=0)
        
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()
        
        self.frame1 = LabelFrame(self.root,text="Buena suerte!!!")
        self.frame1.grid(row=3, column=0)
                
        self.num1 = Label(self.frame,width="5",font=('arial',15),textvariable=self.n1)
        self.num2 = Label(self.frame,width="5",font=('arial',15),textvariable=self.n2)
        self.num3 = Label(self.frame,width="5",font=('arial',15),textvariable=self.n3)
        self.num4 = Label(self.frame,width="5",font=('arial',15),textvariable=self.n4)
        
        self.num1.grid(row=2,column=0)
        self.num2.grid(row=2,column=1)
        self.num3.grid(row=2,column=2)
        self.num4.grid(row=2,column=3)
        
        com_buton=Button(self.frame1,text="¡Voy a tener suerte!",command=self.num_random,
                         font=('arial',20,BOLD),relief=GROOVE)
        com_buton.grid(row=0,column=0)
        
        get_buton=Button(self.frame1,text="Sumas",command=self.sumar_numeros,
                         font=('arial',20,BOLD),relief=GROOVE)
        get_buton.grid(row=2,column=0)
    

    def num_random(self):
        self.n1.set(random.randint(0,100))
        self.n2.set(random.randint(0,100))
        self.n3.set(random.randint(0,100))
        self.n4.set(random.randint(0,100))

    def sumar_numeros(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        n3 = self.n3.get()
        n4 = self.n4.get()
        lista_de_sumas = [n1, n2,n3,n4]

        print(sum(map(int,lista_de_sumas)))
        
            

if __name__=='__main__':
    window=Tk()
    app=BrainTrain(window)
    window.mainloop()
