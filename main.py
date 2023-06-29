from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import random
import time
import sqlite3

class BrainTrain:
    def __init__(self,window):
        self.root=window
        self.root.title("Brain Train")
        self.root.config(bg="#4f4339")
        self.start_time = None
        self.crear_bbdd()
        
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

        self.numeros = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8,
                   self.n9, self.n10, self.n11, self.n12, self.n13, self.n14, self.n15, self.n16]

        self.r1 = StringVar()
        self.r2 = StringVar()
        self.r3 = StringVar()
        self.r4 = StringVar()
        
        self.frame1 = LabelFrame(self.root,text="Buena suerte!!!")
        self.frame1.grid(row=3, column=0)

        self.frame2 = LabelFrame(self.root,text="Records!!!")
        self.frame2.grid(row=4, column=0)

      
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


        self.alert1 = Label(self.frame, text="   ",bg="red")
        self.alert1.grid(row=2,column=5)
        self.alert2 = Label(self.frame, text="   ",bg="red")
        self.alert2.grid(row=3,column=5)
        self.alert3 = Label(self.frame, text="   ",bg="red")
        self.alert3.grid(row=4,column=5)
        self.alert4 = Label(self.frame, text="   ",bg="red")
        self.alert4.grid(row=5,column=5)

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

        # Responses
        self.respuesta1 = Entry(self.frame, width="5", font=('arial', 15), textvariable=self.r1)
        self.respuesta1.grid(row=2,column=4)

        self.respuesta2 = Entry(self.frame, width="5", font=('arial', 15), textvariable=self.r2)
        self.respuesta2.grid(row=3,column=4)

        self.respuesta3 = Entry(self.frame, width="5", font=('arial', 15), textvariable=self.r3)
        self.respuesta3.grid(row=4,column=4)

        self.respuesta4 = Entry(self.frame, width="5", font=('arial', 15), textvariable=self.r4)
        self.respuesta4.grid(row=5,column=4)
        

        com_buton=Button(self.frame1,text="¡Voy a sumar!",command=self.num_random,
                         font=('arial',20,BOLD),relief=GROOVE)
        com_buton.grid(row=0,column=0)
        
        get_buton=Button(self.frame1,text="Sumas",command=self.sumar_numeros,
                         font=('arial',20,BOLD),relief=GROOVE)
        get_buton.grid(row=2,column=0)

        self.treeview = ttk.Treeview(self.frame2)
        self.treeview.grid(row=0, column=0)
        self.treeview['columns'] = ('tiempo', 'fecha')
        self.treeview.heading('#0', text='', anchor='center')
        self.treeview.column('#0', width=0) 
        self.treeview.heading('tiempo', text='Tiempo')
        self.treeview.heading('fecha', text='Fecha')
        self.mostrar_records()

    def mostrar_records(self):
        con = sqlite3.connect('records.db')
        cur = con.cursor()
        cur.execute("""SELECT tiempo, fecha 
                    FROM registros
                    ORDER BY tiempo ASC
                    LIMIT 8
                    """)
        datos = cur.fetchall()
        con.close()
        
        # Insertar datos en el Treeview
        for dato in datos:
            self.treeview.insert('', 'end', values=dato)
        

    def num_random(self):
        # Iniciar tiempo de juego
        self.start_time = time.time()
        for num in self.numeros:
            num.set(random.randint(0, 100))

    def crear_bbdd(self):
        # Crear tabla
        con = sqlite3.connect("records.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS registros 
                    (id INTEGER PRIMARY KEY,
                     tiempo FLOAT, 
                     fecha DATE DEFAULT (DATE('now')))""")
        con.commit()
        con.close()

    def insertar_datos(self, values):
        con = sqlite3.connect("records.db")
        cur = con.cursor()
        cur.execute("INSERT INTO registros (tiempo) VALUES(?)", (values,))
        con.commit()
        con.close()

    def sumar_numeros(self):
        # Sumas fila uno
        n1, n2, n3, n4 = [var.get() for var in (self.n1, self.n2, self.n3, self.n4)]
        suma_fila_1 = [n1, n2,n3,n4]

        suma_1 = sum(map(int,suma_fila_1))
        intento_f1 = self.r1.get()

        #  Sumas fila dos
        n5, n6, n7, n8 = [var.get() for var in (self.n5, self.n6, self.n7, self.n8)]
        suma_fila_2 = [n5, n6,n7,n8]

        suma_2 = sum(map(int,suma_fila_2))
        intento_f2 = self.r2.get()

        # Sumas fila tres
        n9, n10, n11, n12 = [var.get() for var in (self.n9, self.n10, self.n11, self.n12)]
        suma_fila_3 = [n9, n10,n11,n12]

        suma_3 = sum(map(int,suma_fila_3))
        intento_f3 = self.r3.get()

        n13, n14, n15, n16 = [var.get() for var in (self.n13, self.n14, self.n15, self.n16)]
        suma_fila_4 = [n13, n14,n15,n16]

        # Sumas fila 4
        suma_4 = sum(map(int,suma_fila_4))
        intento_f4 = self.r4.get()

        print(suma_1, suma_2, suma_3, suma_4)# SACAR ESTO DESPUES
        condicones = 0

        try:
            if suma_1 == int(intento_f1):
                condicones += 1
                self.alert1 = Label(self.frame, text="   ",bg="green")
                self.alert1.grid(row=2,column=5)

            if suma_2 == int(intento_f2):
                condicones += 1
                self.alert2 = Label(self.frame, text="   ",bg="green")
                self.alert2.grid(row=3,column=5)
            
            if suma_3 == int(intento_f3):
                condicones += 1
                self.alert3 = Label(self.frame, text="   ",bg="green")
                self.alert3.grid(row=4,column=5)
            
            if suma_4 == int(intento_f4):
                condicones += 1
                self.alert4 = Label(self.frame, text="   ",bg="green")
                self.alert4.grid(row=5,column=5)

        except:
            print("Los campos estan vacíos")

        if condicones == 4:
            if self.start_time is not None:
                time_enlapsed = time.time() - self.start_time
                minutes, seconds = divmod(time_enlapsed, 60)
                print("Tiempo transcurrido: {:.0f} minutos {:.2f} segundos".format(minutes, seconds))
                tiempo = f'{round(minutes)}.{round(seconds)}'
                self.insertar_datos(tiempo)
                self.mostrar_records()
                self.start_time = None

        
if __name__=='__main__':
    window=Tk()
    app=BrainTrain(window)
    window.mainloop()
