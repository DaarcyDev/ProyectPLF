import tkinter
import tkinter.messagebox
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

    indexFrame = customtkinter.CTkFrame(window)
    indexFrame2 = customtkinter.CTkFrame(window)

    aboutFrame = customtkinter.CTkFrame(window,width=800, height=600)
    aboutFrame2 = customtkinter.CTkFrame(window,width=800, height=600)
    
    picFrame = customtkinter.CTkFrame(window,width=800, height=600)
    picFrame2 = customtkinter.CTkFrame(window,width=800, height=600)

    aboutFrame3 = customtkinter.CTkFrame(window)

    menuFrame = customtkinter.CTkFrame(window)

    def destroy():
        for widget in Actions.picFrame.winfo_children():
            widget.destroy()
        for widget in Actions.picFrame2.winfo_children():
            widget.destroy()
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

    def futuro():
        Actions.destroy()

        Actions.picFrame.pack(
            pady=20, padx=60, expand=False, )
        Actions.picFrame2.pack(
            pady=20, padx=60, expand=False, )
        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")

        imagen = Image.open("friends.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("viajes.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        imagen = Image.open("dep.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("mic.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, command=lambda: Actions.menu(), text="regresar")
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()


    def actualidad():
        Actions.destroy()

        Actions.picFrame.pack(
            pady=20, padx=60, expand=False, )
        Actions.picFrame2.pack(
            pady=20, padx=60, expand=False, )
        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")

        imagen = Image.open("lol.jpg")
        nuevo_tamano = (500, 300)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("arch.jpg")
        nuevo_tamano = (300, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        imagen = Image.open("serv.jpg")
        nuevo_tamano = (300, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("bat.jpg")
        nuevo_tamano = (300, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, command=lambda: Actions.menu(), text="regresar")
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()

    def hobbies():
        Actions.destroy()

        Actions.picFrame.pack(
            pady=20, padx=60, expand=False, )
        Actions.picFrame2.pack(
            pady=20, padx=60, expand=False, )
        Actions.aboutFrame3.pack(
            pady=20, padx=60, expand=False, anchor="center")

        imagen = Image.open("dev.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("dog.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        imagen = Image.open("valo.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="left")

        imagen = Image.open("gym.jpg")
        nuevo_tamano = (600, 400)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.picFrame2, image=imagen_tk, text="")
        label.pack(pady=10, padx=10,side="right")

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame3, command=lambda: Actions.menu(), text="regresar")
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()

    def menu():
        Actions.destroy()

        Actions.aboutFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.aboutFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")

        aboutButton1 = customtkinter.CTkButton(
            Actions.aboutFrame, command=lambda: Actions.hobbies(), text="Hobbies")
        aboutButton1.pack(pady=10, padx=10)

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame, command=lambda: Actions.actualidad(), text="Actualidad")
        aboutButton2.pack(pady=10, padx=10)

        aboutButton3 = customtkinter.CTkButton(
            Actions.aboutFrame, command=lambda: Actions.futuro(), text="Futuro")
        aboutButton3.pack(pady=10, padx=10)

        aboutButton4 = customtkinter.CTkButton(
            Actions.aboutFrame2, command=lambda: Actions.index(), text="regresar")
        aboutButton4.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()
        Actions.aboutFrame3.pack_forget()
        Actions.picFrame.pack_forget()
        Actions.picFrame2.pack_forget()

    def about():
        Actions.destroy()

        Actions.aboutFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.aboutFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")

        imagen = Image.open("about.jpg")
        nuevo_tamano = (600, 800)
        imagen = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen)

        label = customtkinter.CTkLabel(
            Actions.aboutFrame, image=imagen_tk, text="")
        label.pack(side="left")

        aboutLabel1 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="Alvarez Peralta Liam")
        aboutLabel1.pack(pady=10, padx=10,)

        aboutLabel2 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="5 Julio 2001")
        aboutLabel2.pack(pady=10, padx=10,)

        aboutLabel3 = customtkinter.CTkLabel(
            master=Actions.aboutFrame, justify=customtkinter.LEFT, text="Cuernavaca Morelos Mexico")
        aboutLabel3.pack(pady=10, padx=10,)

        aboutButton2 = customtkinter.CTkButton(
            Actions.aboutFrame2, command=lambda: Actions.index(), text="regresar")
        aboutButton2.pack(pady=10, padx=10, side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()

    def exit():
        window.destroy()

    def index():

        Actions.indexFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.indexFrame2.pack(
            pady=20, padx=60, expand=True, anchor="center")

        indexLabel1 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Tecnologico Nacional de Mexico")
        indexLabel1.pack(pady=10, padx=10)

        indexLabel2 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Instituto Tecnologico de Zacatepec")
        indexLabel2.pack(pady=10, padx=10)

        indexLabel3 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Ingenieria en Sistemas Computacionales")
        indexLabel3.pack(pady=10, padx=10)

        indexLabel4 = customtkinter.CTkLabel(
            master=Actions.indexFrame, justify=customtkinter.LEFT, text="Programacion Logica y Funcional")
        indexLabel4.pack(pady=10, padx=10)

        indexButton1 = customtkinter.CTkButton(
            Actions.indexFrame2, command=lambda: Actions.menu(), text="Menu")
        indexButton1.pack(pady=10, padx=10, side="left")

        indexButton2 = customtkinter.CTkButton(
            Actions.indexFrame2, command=lambda: Actions.about(), text="Acerca de")
        indexButton2.pack(pady=10, padx=10, side="left")

        indexButton3 = customtkinter.CTkButton(
            Actions.indexFrame2, command=lambda: Actions.exit(), text="Salir")
        indexButton3.pack(pady=10, padx=10, side="left")

        Actions.aboutFrame.pack_forget()
        Actions.aboutFrame2.pack_forget()


Actions.index()
window.mainloop()
