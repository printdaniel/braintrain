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

        # Instancia de variables
        
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()
        self.n5 = StringVar()
        self.n6 = StringVar()
        self.n7 = StringVar()
        self.n8 = StringVar()
        self.n9 = StringVar()
        self.n10 = StringVar()
        self.n11 = StringVar()
        self.n12 = StringVar()
        self.n13 = StringVar()
        self.n14 = StringVar()
        self.n15 = StringVar()
        self.n16 = StringVar()

        self.r1 = StringVar()
        self.r2 = StringVar()
        self.r3 = StringVar()
        self.r4 = StringVar()
        
        self.frame1 = LabelFrame(self.root,text="Buena suerte!!!")
        self.frame1.grid(row=3, column=0)
                
        self.num1 = Label(self.frame,font=('arial',15),textvariable=self.n1)
        self.num2 = Label(self.frame,font=('arial',15),textvariable=self.n2)
        self.num3 = Label(self.frame,font=('arial',15),textvariable=self.n3)
        self.num4 = Label(self.frame,font=('arial',15),textvariable=self.n4)
        self.num5 = Label(self.frame,font=('arial',15),textvariable=self.n5)
        self.num6 = Label(self.frame,font=('arial',15),textvariable=self.n6)
        self.num7 = Label(self.frame,font=('arial',15),textvariable=self.n7)
        self.num8 = Label(self.frame,font=('arial',15),textvariable=self.n8)
        self.num9 = Label(self.frame,font=('arial',15),textvariable=self.n9)
        self.num10 = Label(self.frame,font=('arial',15),textvariable=self.n10)
        self.num11 = Label(self.frame,font=('arial',15),textvariable=self.n11)
        self.num12 = Label(self.frame,font=('arial',15),textvariable=self.n12)
        self.num13 = Label(self.frame,font=('arial',15),textvariable=self.n13)
        self.num14 = Label(self.frame,font=('arial',15),textvariable=self.n14)
        self.num15 = Label(self.frame,font=('arial',15),textvariable=self.n15)
        self.num16 = Label(self.frame,font=('arial',15),textvariable=self.n16)
        

        # Grid
        self.num1.grid(row=2,column=0)
        self.num2.grid(row=2,column=1)
        self.num3.grid(row=2,column=2)
        self.num4.grid(row=2,column=3)
        
        self.num5.grid(row=3,column=0)
        self.num6.grid(row=3,column=1)
        self.num7.grid(row=3,column=2)
        self.num8.grid(row=3,column=3)
        
        self.num9.grid(row=4,column=0)
        self.num10.grid(row=4,column=1)
        self.num11.grid(row=4,column=2)
        self.num12.grid(row=4,column=3)

        self.num13.grid(row=5,column=0)
        self.num14.grid(row=5,column=1)
        self.num15.grid(row=5,column=2)
        self.num16.grid(row=5,column=3)


        self.respuesta1 = Entry(self.frame, width="5", font=('arial', 15), textvariable=self.r1)
        self.respuesta1.grid(row=2,column=4)
        
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
        self.n5.set(random.randint(0,100))
        self.n6.set(random.randint(0,100))
        self.n7.set(random.randint(0,100))
        self.n8.set(random.randint(0,100))
        self.n9.set(random.randint(0,100))
        self.n10.set(random.randint(0,100))
        self.n11.set(random.randint(0,100))
        self.n12.set(random.randint(0,100))
        self.n13.set(random.randint(0,100))
        self.n14.set(random.randint(0,100))
        self.n15.set(random.randint(0,100))
        self.n16.set(random.randint(0,100))

    def sumar_numeros(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        n3 = self.n3.get()
        n4 = self.n4.get()
        lista_de_sumas = [n1, n2,n3,n4]

        print(sum(map(int,lista_de_sumas)))
        print(self.r1.get())
        
            
if __name__=='__main__':
    window=Tk()
    app=BrainTrain(window)
    window.mainloop()
