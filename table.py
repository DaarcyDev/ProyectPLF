import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook

# Cargar el archivo Excel
workbook = load_workbook(filename='Boris.xlsx')
sheet = workbook.active

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Archivo Excel")

# Crear un Treeview para mostrar los datos
tree = ttk.Treeview(root)

# Agregar columnas al Treeview
tree["columns"] = tuple(sheet[1])
tree.column("#0", width=0, stretch=tk.NO) # columna oculta
for column in tree["columns"]:
    tree.column(column, anchor=tk.CENTER)
    tree.heading(column, text=column, anchor=tk.CENTER)

# Agregar filas al Treeview
for row in sheet.iter_rows(min_row=2, values_only=True):
    tree.insert("", tk.END, text="", values=tuple(row))

# Empaquetar el Treeview en la ventana
tree.pack(expand=tk.YES, fill=tk.BOTH)

# Iniciar el bucle principal de Tkinter
root.mainloop()
