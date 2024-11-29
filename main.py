from tkinter import, Tk, LabelFrame, StringVar, Label, Button, GROOVE, END
from tkinter.font import BOLD
from tkinter import ttk
import random
import time
import sqlite3
import logging

"""
Logger basic config
La app es meramente experimental por lo que no es rigurosa en su arquitectura
"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('BrainTrain')


class BrainTrain:
    def __init__(self, window):
        self.root = window
        self.root.title("Brain Train")
        self.root.config(bg="#4f4339")
        self.start_time = None
        self.crear_bbdd()

        self.frame = LabelFrame(self.root, text="Números para jugar")
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

        self.numeros = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6,
                        self.n7, self.n8]

        self.r1 = StringVar()
        self.r2 = StringVar()

        self.frame1 = LabelFrame(self.root, text="Buena suerte!!!")
        self.frame1.grid(row=3, column=0)

        self.frame2 = LabelFrame(self.root, text="Records!!!")
        self.frame2.grid(row=4, column=0)

        # Labels para los 8 números a sumar
        self.num1 = Label(self.frame, font=('arial', 15), textvariable=self.n1)
        self.num2 = Label(self.frame, font=('arial', 15), textvariable=self.n2)
        self.num3 = Label(self.frame, font=('arial', 15), textvariable=self.n3)
        self.num4 = Label(self.frame, font=('arial', 15), textvariable=self.n4)
        self.num5 = Label(self.frame, font=('arial', 15), textvariable=self.n5)
        self.num6 = Label(self.frame, font=('arial', 15), textvariable=self.n6)
        self.num7 = Label(self.frame, font=('arial', 15), textvariable=self.n7)
        self.num8 = Label(self.frame, font=('arial', 15), textvariable=self.n8)

        # Grid
        self.num1.grid(row=2, column=0)
        self.num2.grid(row=2, column=1)
        self.num3.grid(row=2, column=2)
        self.num4.grid(row=2, column=3)

        self.num5.grid(row=3, column=0)
        self.num6.grid(row=3, column=1)
        self.num7.grid(row=3, column=2)
        self.num8.grid(row=3, column=3)

        # Responses
        self.respuesta1 = Entry(self.frame, width="5", font=('arial', 15),
                                textvariable=self.r1)
        self.respuesta1.grid(row=2, column=4)

        self.respuesta2 = Entry(self.frame, width="5", font=('arial', 15),
                                textvariable=self.r2)
        self.respuesta2.grid(row=3, column=4)

        com_buton = Button(self.frame1, text="¡Voy a sumar!", command=self.num_random,
                           font=('arial', 20, BOLD), relief=GROOVE)
        com_buton.grid(row=0, column=0)

        get_buton = Button(self.frame1, text="Sumas", command=self.verificar_sumas,
                           font=('arial', 20, BOLD), relief=GROOVE)
        get_buton.grid(row=2, column=0)

        # Treeview Zone
        self.treeview = ttk.Treeview(self.frame2)
        self.treeview.grid(row=0, column=0)
        self.treeview['columns'] = ('tiempo', 'fecha')
        self.treeview.heading('#0', text='', anchor='center')
        self.treeview.column('#0', width=0)
        self.treeview.heading('tiempo', text='Tiempo')
        self.treeview.heading('fecha', text='Fecha')
        self.mostrar_records()

        self.red_alerts()
        logger.info("Init ready")

    def red_alerts(self):
        self.alert1 = Label(self.frame, text="   ", bg="red")
        self.alert1.grid(row=2, column=5)
        self.alert2 = Label(self.frame, text="   ", bg="red")
        self.alert2.grid(row=3, column=5)

    def limpiar_entrys(self):
        self.respuesta1.delete(0, END)
        self.respuesta2.delete(0, END)

    def mostrar_records(self):
        """
        Muestra los primeros 8 registros de la base de datos en el Treeview.
        Los registros ser odenan de manera ascendente según el tiempo.

        Parameters:
            None
        Returns:
            None
        """
        con = sqlite3.connect('records.db')
        cur = con.cursor()
        # Selecciona los registros de la base de datos
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
        """
        Genera números aleatorios y los asigna a las variables StringVar.

        Parameters:
            None
        Returns:
            None
        """

        # Resetea las alertas en rojo
        self.red_alerts()

        # Iniciar tiempo de juego
        self.start_time = time.time()

        # Generar números aleatorios y asignarlos a las variables StringVar.
        for num in self.numeros:
            num.set(random.randint(0, 100))

    def crear_bbdd(self):
        """
        Crea una base de datos SQLite y una tabla para almacenar registros.

        Parameters:
            None
        Returns:
            None
        """
        # Crear tabla en la base de datos
        logger.info("DB Records sqlite3 creada")
        con = sqlite3.connect("records.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS registros
                    (id INTEGER PRIMARY KEY,
                     tiempo FLOAT,
                     fecha DATE DEFAULT (DATE('now')))""")
        con.commit()
        con.close()

    def insertar_datos(self, values):
        """
        Inserta un nuevo registro en la base de datos.

        Parameters:
            values (float): El valor del tiempo en que se tardó en completar el juego.
        Retruns:
            None
        """
        con = sqlite3.connect("records.db")
        cur = con.cursor()
        cur.execute("INSERT INTO registros (tiempo) VALUES(?)", (values,))
        con.commit()
        con.close()

    def obtener_sumas(self):
        """
        Obtiene las sumas de las filas y los valores de los intentos de cada fila.

        Returns:
            tuple: Una tupla con las sumas de las filas y los intentos de cada fila.
        """
        # Sumas fila uno
        n1, n2, n3, n4 = [var.get()
                          for var in (self.n1, self.n2, self.n3, self.n4)]
        suma_fila_1 = [n1, n2, n3, n4]

        suma_1 = sum(map(int, suma_fila_1))
        logger.info("Suma 1")

        #  Sumas fila dos
        n5, n6, n7, n8 = [var.get()
                          for var in (self.n5, self.n6, self.n7, self.n8)]
        suma_fila_2 = [n5, n6, n7, n8]

        suma_2 = sum(map(int, suma_fila_2))
        logger.info("Suma 2")

        return suma_1, suma_2

    def verificar_sumas(self):
        """
        Verifica si las sumas de las filas coinciden con los intentos y realiza
        las acciones correspondientes.

        Returns:
        None
        """

        # Obtener las sumas de cada fila
        suma_1, suma_2 = self.obtener_sumas()

        # Obtener cada una de las respuestas del usuario.
        intento_f1 = self.r1.get()
        intento_f2 = self.r2.get()

        # Bandera, para saber si se logró dar con las 2 sumas.
        condicones = 0

        try:
            if suma_1 == int(intento_f1):
                condicones += 1
                self.alert1 = Label(self.frame, text="   ", bg="green")
                self.alert1.grid(row=2, column=5)

            if suma_2 == int(intento_f2):
                condicones += 1
                self.alert2 = Label(self.frame, text="   ", bg="green")
                self.alert2.grid(row=3, column=5)

        except:
            logger.warning("Campos vacíos")

        if condicones == 2:
            if self.start_time is not None:
                time_enlapsed = time.time() - self.start_time
                minutes, seconds = divmod(time_enlapsed, 60)
                # print("Tiempo transcurrido: {:.0f} minutos {:.2f} segundos".format(minutes, seconds))
                tiempo = f'{round(minutes)}.{round(seconds)}'
                self.insertar_datos(tiempo)
                self.mostrar_records()
                self.start_time = None
                self.limpiar_entrys()

# TODO: que se guarde únicamente si ambas sumas estan correctas
# TODO: Arreglar la fecha de SQL
if __name__ == '__main__':
    window = Tk()
    app = BrainTrain(window)
    window.mainloop()
