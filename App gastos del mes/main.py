from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime



class Application(ttk.Frame):
    #Variables totales
    totalGastos = 0
    totalIngresos = 0
    totalBalance = 0
    
    def __init__(self, root):
        global campoFecha, comboTipo, campoIngreso, campoConcepto, tablaMovimientos, campoTotalIngresos, campoTotalGastos, campoBalance
        #Inicialización ventana
        super().__init__(root)        

        #Frame widgets
        widgetFrame = Frame(root)
        widgetFrame.pack(fill="y", pady=5, padx=5)

        #Frame izquierdo
        leftFrame = ttk.LabelFrame(widgetFrame, text="Insertar movimiento", height=500)
        leftFrame.grid(row=0, column=0, padx=3)

        #Campos frame
        fieldsFrame = Frame(leftFrame)
        fieldsFrame.pack()
        labelTipo = Label(fieldsFrame, text="Tipo:")
        labelTipo.grid(row=1,column=0)        
        comboTipo = ttk.Combobox(fieldsFrame,
                                 values=["Ingreso","Gasto"], state="readonly", )
        comboTipo.grid(row=1,column=1,pady=5, padx=5)
        comboTipo.set("Ingreso")

        labelIngreso = Label(fieldsFrame, text="Cantidad:")
        labelIngreso.grid(row=2,column=0)
        campoIngreso = Entry(fieldsFrame)
        campoIngreso.grid(row=2,column=1)

        labelConcepto = Label(fieldsFrame, text="Concepto:")
        labelConcepto.grid(row=3, column=0)
        campoConcepto = Entry(fieldsFrame)
        campoConcepto.grid(row=3, column=1)

        labelFecha = Label(fieldsFrame, text="Fecha:")
        labelFecha.grid(row=4, column=0,pady=5, padx=5)
        campoFecha = Entry(fieldsFrame)
        campoFecha.grid(row=4, column=1,pady=5, padx=5)
        campoFecha.insert(0, datetime.today().strftime('%d/%m/%Y'))
        campoFecha.bind("<1>", self.pick_date)
        
        #Frame botones
        buttonsFrame = Frame(fieldsFrame)
        buttonsFrame.grid(row=5, column=0, columnspan=2)
        anyadirButton = Button(buttonsFrame, text="Añadir")
        anyadirButton.pack(side=LEFT, pady=5, padx=2)
        anyadirButton.bind("<1>", self.anyadirATabla)

        borrarButton = Button(buttonsFrame, text="Borrar")
        borrarButton.pack(side=LEFT, pady=5, padx=2)
        borrarButton.bind("<1>", self.borrarFila)

        #Ingresos, gastos y balance
        labelTotalIngresos = Label(fieldsFrame, text="Total ingresos: ")
        labelTotalIngresos.grid(row=6, column=0, padx=5, sticky = W)
        campoTotalIngresos = Label(fieldsFrame, text= str(self.totalIngresos) + "€")
        campoTotalIngresos.grid(row=6, column=1, padx=5, sticky = E)

        labelTotalGastos = Label(fieldsFrame, text="Total gastos: ")
        labelTotalGastos.grid(row=7, column=0, padx=5,sticky = W)
        campoTotalGastos = Label(fieldsFrame, text= str(self.totalGastos) + "€")
        campoTotalGastos.grid(row=7, column=1, padx=5,sticky = E)

        labelBalance = Label(fieldsFrame, text="Balance: ")
        labelBalance.grid(row=8, column=0, padx=5, sticky = W)
        campoBalance = Label(fieldsFrame, text= str(self.totalBalance) + "€")
        campoBalance.grid(row=8, column=1, padx=5, sticky = E)
        
        #Frame derecho movimientos
        movimientosFrame = ttk.Frame(widgetFrame, width=350, height=500)
        movimientosFrame.grid(row=0, column=1, padx=3)
        columnasMovimientos = ("Fecha", "Tipo", "Concepto", "Cantidad")
        movimientosScroll = ttk.Scrollbar(movimientosFrame)
        movimientosScroll.pack(side="right", fill=Y)
        tablaMovimientos = ttk.Treeview(movimientosFrame, show="headings", columns=columnasMovimientos, yscrollcommand=movimientosScroll.set)
        tablaMovimientos.heading("Fecha", text="Fecha")
        tablaMovimientos.heading("Tipo", text="Tipo")
        tablaMovimientos.heading("Concepto", text="Concepto")
        tablaMovimientos.heading("Cantidad", text="Cantidad")
        tablaMovimientos.pack()

    def anyadirATabla(self,event):
        tipo = comboTipo.get()
        fecha = campoFecha.get()
        concepto = campoConcepto.get()
        cantidad = campoIngreso.get()

        #Validación campo cantidad. (Tiene que ser numérico)
        if cantidad.isnumeric():            
            self.actualizarTotales(tipo,cantidad,"Insertar")
            cantidad = cantidad + '€'
            tablaMovimientos.insert('', END, values=(fecha,tipo,concepto,cantidad))
            self.cleanFields()
        else:
            cantidad = ''
            campoIngreso.delete(0,END) 
        

    def borrarFila(self,event):
        if (tablaMovimientos.get_children()):
            filaSeleccionada = tablaMovimientos.selection()

            if(len(filaSeleccionada) == 0):
                filaSeleccionada = tablaMovimientos.get_children()[-1]
                itemABorrar = tablaMovimientos.item(filaSeleccionada)
                # El ítem es un diccionario, con list(item.values()) se obtiene una lista de todos los valores del dic, dentro de esos valores, 
                # hay otra lista con los valores que nos interesa, por lo que accedemos a dos posiciones para obtener el valor que queremos. 
                listaValoresFila = list(itemABorrar.values())         
                tipo = listaValoresFila[2][1]      
                cantidadBorrada = listaValoresFila[2][3]
                cantidadBorrada = str.replace(cantidadBorrada, "€","")

                self.actualizarTotales(tipo,cantidadBorrada,"Borrar")

                tablaMovimientos.delete(filaSeleccionada)
            elif(tablaMovimientos.exists):
                # Método .item con el index obtenido en selection() para obtener el item y sus valores.
                itemABorrar = tablaMovimientos.item(filaSeleccionada) 
                # El ítem es un diccionario, con list(item.values()) se obtiene una lista de todos los valores del dic, dentro de esos valores, 
                # hay otra lista con los valores que nos interesa, por lo que accedemos a dos posiciones para obtener el valor que queremos. 
                listaValoresFila = list(itemABorrar.values())         
                tipo = listaValoresFila[2][1]      
                cantidadBorrada = listaValoresFila[2][3]
                cantidadBorrada = str.replace(cantidadBorrada, "€","")

                self.actualizarTotales(tipo,cantidadBorrada,"Borrar")

                tablaMovimientos.delete(filaSeleccionada)
            
    def actualizarTotales(self,tipo,cantidad,accion) :

        if accion == "Insertar":
            if tipo == "Ingreso":
                # str() para pasar a String algo, int() para pasar a Integer un string (numérico).
                self.totalIngresos = self.totalIngresos + int(cantidad)
                # con .config de un Label podemos alterar las propiedades del mismo.
                campoTotalIngresos.config(text = str(self.totalIngresos) + "€")
            elif tipo == "Gasto":
                self.totalGastos = self.totalGastos + int(cantidad)
                campoTotalGastos.config(text = str(self.totalGastos) + "€")
        elif accion == "Borrar":
            if tipo == "Ingreso":
                # str() para pasar a String algo, int() para pasar a Integer un string (numérico).
                self.totalIngresos = self.totalIngresos - int(cantidad)
                # con .config de un Label podemos alterar las propiedades del mismo.
                campoTotalIngresos.config(text = str(self.totalIngresos) + "€")
            elif tipo == "Gasto":
                self.totalGastos = self.totalGastos - int(cantidad)
                campoTotalGastos.config(text = str(self.totalGastos) + "€")

        

    def cleanFields(self):
        campoConcepto.delete(0,END)
        campoIngreso.delete(0,END)
        comboTipo.delete(0,END)
    
    #Función para abrir y seleccionar la fecha.
    def pick_date(self, event):
        global calendar, date_root
        date_root = Toplevel()
        date_root.grab_set
        date_root.title('Fecha del movimiento:')
        date_root.geometry('250x220+590+370')

        calendar = Calendar(date_root, selectmode='day', datepattern='dd/mm/Y')
        calendar.place(x=0,y=0)

        aceptarBoton = Button(date_root, text='Aceptar', command=self.grab_date)
        aceptarBoton.place(x=80, y=190)

    #Obtiene la fecha, limpia el campo e inserta la fecha escogida en él.
    def grab_date(self):
        campoFecha.delete(0, END)
        campoFecha.insert(0, datetime.strptime(calendar.get_date(), '%m/%d/%y').strftime('%d/%m/%Y'))
        date_root.destroy()

#Creación ventana
root=Tk()

root.title("Gastos del mes")

app = Application(root)

app.mainloop()