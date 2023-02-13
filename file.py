import tkinter
import tkinter.messagebox
import customtkinter



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()

    # window.geometry("400x780")
window.title("Proyecto Tkinter")
    # window.resizable(0,0)
# window.grid_columnconfigure(1, weight=1)
# window.grid_rowconfigure(0, weight=0)

class Actions:


    indexFrame = customtkinter.CTkFrame(window)
    indexFrame2 = customtkinter.CTkFrame(window,width=450,height=350)

    aboutFrame = customtkinter.CTkFrame(window)
    aboutFrame2 = customtkinter.CTkFrame(window,width=450,height=350)
    

    def about():
        for widget in Actions.aboutFrame.winfo_children():
            widget.destroy()
        for widget in Actions.aboutFrame2.winfo_children():
            widget.destroy()
        for widget in Actions.indexFrame.winfo_children():
            widget.destroy()
        for widget in Actions.indexFrame2.winfo_children():
            widget.destroy()

        Actions.aboutFrame.pack(pady=20, padx=60, fill="both", expand=True)
        Actions.aboutFrame2.pack(pady=20, padx=60, expand=True,anchor="center")

        # Crea nuevos widgets en el frame
        aboutLabel1 = customtkinter.CTkLabel(master=Actions.aboutFrame, justify=customtkinter.LEFT,text="ola")
        aboutLabel1.pack(pady=10, padx=10)

        aboutLabel2 = customtkinter.CTkLabel(master=Actions.aboutFrame, justify=customtkinter.LEFT,text="Instituto Tecnologico de Zacatepec")
        aboutLabel2.pack(pady=10, padx=10)

        aboutLabel3 = customtkinter.CTkLabel(master=Actions.aboutFrame, justify=customtkinter.LEFT,text="Ingenieria en Sistemas Computacionales")
        aboutLabel3.pack(pady=10, padx=10)

        aboutLabel4 = customtkinter.CTkLabel(master=Actions.aboutFrame, justify=customtkinter.LEFT,text="Programacion Logica y Funcional")
        aboutLabel4.pack(pady=10, padx=10)

        aboutButton3 = customtkinter.CTkButton(Actions.aboutFrame2, command=lambda:Actions.index(),text="regresar")
        aboutButton3.pack(pady=10, padx=10,side="left")

        Actions.indexFrame.pack_forget()
        Actions.indexFrame2.pack_forget()

    def exit():
            window.destroy()


    def index():
        

            Actions.indexFrame.pack(pady=20, padx=60, fill="both", expand=True)
            Actions.indexFrame2.pack(pady=20, padx=60, expand=True,anchor="center")

            indexLabel1 = customtkinter.CTkLabel(master=Actions.indexFrame, justify=customtkinter.LEFT,text="Tecnologico Nacional de Mexico")
            indexLabel1.pack(pady=10, padx=10)

            indexLabel2 = customtkinter.CTkLabel(master=Actions.indexFrame, justify=customtkinter.LEFT,text="Instituto Tecnologico de Zacatepec")
            indexLabel2.pack(pady=10, padx=10)

            indexLabel3 = customtkinter.CTkLabel(master=Actions.indexFrame, justify=customtkinter.LEFT,text="Ingenieria en Sistemas Computacionales")
            indexLabel3.pack(pady=10, padx=10)

            indexLabel4 = customtkinter.CTkLabel(master=Actions.indexFrame, justify=customtkinter.LEFT,text="Programacion Logica y Funcional")
            indexLabel4.pack(pady=10, padx=10)
            

            indexButton1 = customtkinter.CTkButton(Actions.indexFrame2, command=print("hola"),text="Menu")
            indexButton1.pack(pady=10, padx=10,side="left")

            indexButton2 = customtkinter.CTkButton(Actions.indexFrame2, command=lambda:Actions.about(),text="Acerca de")
            indexButton2.pack(pady=10, padx=10,side="left")

            indexButton3 = customtkinter.CTkButton(Actions.indexFrame2, command=lambda:Actions.exit(),text="Salir")
            indexButton3.pack(pady=10, padx=10,side="left")
            
            Actions.aboutFrame.pack_forget()
            Actions.aboutFrame2.pack_forget()

            
            

Actions.index()
window.mainloop()