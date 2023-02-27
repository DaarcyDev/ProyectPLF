from tkinter import ttk
import tkinter.messagebox
from tkinter.font import Font
import customtkinter
from PIL import Image, ImageTk


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()

# window.geometry("400x780")
window.title("Proyecto Tkinter")
# window.resizable(0,0)
# window.grid_columnconfigure(1, weight=1)
# window.grid_rowconfigure(0, weight=0)


class Actions:
    btn_font = customtkinter.CTkFont(family="Roboto Cn", size=25) 

    indexFramePic = customtkinter.CTkFrame(window)

    indexFrame = customtkinter.CTkFrame(window)
    indexFrame2 = customtkinter.CTkFrame(window)

    aboutFrame = customtkinter.CTkFrame(window)
    aboutFrame2 = customtkinter.CTkFrame(window)
    

    aboutFrame3 = customtkinter.CTkFrame(window)

    menuFrame = customtkinter.CTkFrame(window)

    # productsBox = customtkinter.Treeview(window,height=19, columns=("#0","#1"), selectmode="extended")
    productsBox = ttk.Treeview(window,height=19, columns=("#0","#1"), selectmode="extended")


    def destroy():
        for widget in Actions.aboutFrame.winfo_children():
            widget.destroy()
        for widget in Actions.aboutFrame2.winfo_children():
            widget.destroy()
        for widget in Actions.aboutFrame3.winfo_children():
            widget.destroy()
        for widget in Actions.indexFrame.winfo_children():
            widget.destroy()
        for widget in Actions.indexFrame2.winfo_children():
            widget.destroy()
        for widget in Actions.indexFramePic.winfo_children():
            widget.destroy()
        for widget in Actions.productsBox.winfo_children():
            widget.destroy()
        Actions.productsBox.delete(*Actions.productsBox.get_children())


    def Generar():
        Actions.destroy()

        
        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")



        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, width=300, height=50,command=lambda: Actions.menu(), text="regresar",font=Actions.btn_font)
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()
        Actions.indexFramePic.pack_forget()


    def Horarios():
        Actions.destroy()

                
        Actions.productsBox.pack(pady=40, padx=60)

        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")

        Actions.productsBox['columns'] = ('Maestros', 'Creditos', 'Grupos','Lunes','Martes','Miercoles','Jueves','Viernes')

        Actions.productsBox.column("#0", width=0)
        Actions.productsBox.column("Maestros", width=100)
        Actions.productsBox.column("Creditos",width=150)
        Actions.productsBox.column("Grupos",width=150)
        Actions.productsBox.column("Lunes",width=150)
        Actions.productsBox.column("Martes",width=150)
        Actions.productsBox.column("Miercoles",width=150)
        Actions.productsBox.column("Jueves",width=150)
        Actions.productsBox.column("Viernes",width=150)
        # Actions.productsBox.column("player_states",width=80)
        # Actions.productsBox.column("player_city",width=80)

        Actions.productsBox.heading("#0",text="")
        Actions.productsBox.heading("Maestros",text="Maestros")
        Actions.productsBox.heading("Creditos",text="Creditos")
        Actions.productsBox.heading("Grupos",text="Grupos")
        Actions.productsBox.heading("Lunes",text="Lunes")
        Actions.productsBox.heading("Martes",text="Martes")
        Actions.productsBox.heading("Miercoles",text="Miercoes")
        Actions.productsBox.heading("Jueves",text="Jueves")
        Actions.productsBox.heading("Viernes",text="Viernes")

        # Actions.productsBox.heading("player_states",text="States")
        # Actions.productsBox.heading("player_city",text="States")

        # Actions.productsBox.insert(parent='',index='end',iid=0,text='',
        # values=('asd','Ninja','101'))
        # Actions.productsBox.insert(parent='',index='end',iid=1,text='',
        # values=('asd','Ranger','102'))
        # Actions.productsBox.insert(parent='',index='end',iid=2,text='',
        # values=('asd','Deamon','103'))
        # Actions.productsBox.insert(parent='',index='end',iid=3,text='',
        # values=('asd','Dragon','104'))
        # Actions.productsBox.insert(parent='',index='end',iid=4,text='',
        # values=('asd','CrissCross','105'))
        # Actions.productsBox.insert(parent='',index='end',iid=5,text='',
        # values=('asd','ZaqueriBlack','106'))

        # Actions.productsBox.pack()

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, width=300, height=50,command=lambda: Actions.menu(), text="regresar",font=Actions.btn_font)
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()
        Actions.indexFramePic.pack_forget()

    def Maestros():
        Actions.destroy()

        
        Actions.productsBox.pack(pady=40, padx=60)

        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")

        Actions.productsBox['columns'] = ('maestros', 'HPlazas', 'HAsignadas')

        Actions.productsBox.column("#0", width=0)
        Actions.productsBox.column("maestros", width=100)
        Actions.productsBox.column("HPlazas",width=150)
        Actions.productsBox.column("HAsignadas",width=150)
        # Actions.productsBox.column("player_states",width=80)
        # Actions.productsBox.column("player_city",width=80)

        Actions.productsBox.heading("#0",text="")
        Actions.productsBox.heading("maestros",text="Maestros")
        Actions.productsBox.heading("HPlazas",text="Horas de plaza")
        Actions.productsBox.heading("HAsignadas",text="Horas Asignadas")
        # Actions.productsBox.heading("player_states",text="States")
        # Actions.productsBox.heading("player_city",text="States")

        Actions.productsBox.insert(parent='',index='end',iid=0,text='',
        values=('asd','Ninja','101'))
        # Actions.productsBox.insert(parent='',index='end',iid=1,text='',
        # values=('asd','Ranger','102'))
        # Actions.productsBox.insert(parent='',index='end',iid=2,text='',
        # values=('asd','Deamon','103'))
        # Actions.productsBox.insert(parent='',index='end',iid=3,text='',
        # values=('asd','Dragon','104'))
        # Actions.productsBox.insert(parent='',index='end',iid=4,text='',
        # values=('asd','CrissCross','105'))
        # Actions.productsBox.insert(parent='',index='end',iid=5,text='',
        # values=('asd','ZaqueriBlack','106'))

        # Actions.productsBox.pack()


        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, width=300, height=50,command=lambda: Actions.menu(), text="regresar",font=Actions.btn_font)
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()
        Actions.indexFramePic.pack_forget()
        Actions.menuFrame.pack_forget()
        # Actions.productsBox.pack_forget()

    def menu():
        Actions.destroy()

        Actions.aboutFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.aboutFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")

        aboutButton1 = customtkinter.CTkButton(
            Actions.aboutFrame, width=300, height=50,command=lambda: Actions.Maestros(), text="Maestros",font=Actions.btn_font)
        aboutButton1.pack(pady=10, padx=10)

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame, width=300, height=50,command=lambda: Actions.Horarios(), text="Horarios",font=Actions.btn_font)
        aboutButton2.pack(pady=10, padx=10)

        aboutButton3 = customtkinter.CTkButton(
            Actions.aboutFrame, width=300, height=50,command=lambda: Actions.Generar(), text="Generar",font=Actions.btn_font)
        aboutButton3.pack(pady=10, padx=10)

        aboutButton4 = customtkinter.CTkButton(
            Actions.aboutFrame2, width=300, height=50,command=lambda: Actions.index(), text="regresar",font=Actions.btn_font)
        aboutButton4.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame3.pack_forget()
        
        
        Actions.indexFramePic.pack_forget()
        Actions.productsBox.pack_forget()

    def about():
        Actions.destroy()

        Actions.aboutFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.aboutFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")


        aboutLabel1 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="Alvarez Peralta Liam",font=Actions.btn_font)
        aboutLabel1.pack(pady=10, padx=10)

        aboutLabel2 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="5 Julio 2001",font=Actions.btn_font)
        aboutLabel2.pack(pady=10, padx=10,)

        aboutLabel3 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="Cuernavaca Morelos Mexico",font=Actions.btn_font)
        aboutLabel3.pack(pady=10, padx=10,)

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame2, width=300, height=50,command=lambda: Actions.index(), text="regresar",font=Actions.btn_font)
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.indexFramePic.pack_forget()

    def exit():
        window.destroy()

    def index():

        Actions.indexFramePic.pack(
            pady=20, padx=60, expand=True, fill="both", anchor="n")
        Actions.indexFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.indexFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")
        Actions.indexFramePic.pack(
            pady=20, padx=60, expand=False, anchor="w")


        imagen = Image.open("itz.png")
        nuevo_tamano = (300, 300)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.indexFramePic, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("tnm.jpg")
        nuevo_tamano = (300, 300)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.indexFramePic, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")
        

        indexLabel1 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Tecnologico Nacional de Mexico",font=Actions.btn_font)
        indexLabel1.pack(pady=100, padx=10)

        indexLabel2 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Instituto Tecnologico de Zacatepec",font=Actions.btn_font)
        indexLabel2.pack(pady=30, padx=10)

        indexLabel3 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Ingenieria en Sistemas Computacionales",font=Actions.btn_font)
        indexLabel3.pack(pady=30, padx=10)

        indexLabel4 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Programacion Logica y Funcional",font=Actions.btn_font)
        indexLabel4.pack(pady=30, padx=10)

        

        indexButton1 = customtkinter.CTkButton(
            Actions.indexFrame2, width=300, height=50,command=lambda: Actions.menu(), text="Menu",font=Actions.btn_font)
        indexButton1.pack(pady=10, padx=10, side="left")

        indexButton2 = customtkinter.CTkButton(
            Actions.indexFrame2, width=300, height=50,command=lambda: Actions.about(), text="Acerca de",font=Actions.btn_font)
        indexButton2.pack(pady=10, padx=10, side="left")

        indexButton3 = customtkinter.CTkButton(
            Actions.indexFrame2, width=300, height=50,command=lambda: Actions.exit(), text="Salir",font=Actions.btn_font)
        indexButton3.pack(pady=10, padx=10, side="left")

        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()


Actions.index()
window.mainloop()
