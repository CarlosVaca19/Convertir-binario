import tkinter as tk
from tkinter import messagebox

def convertir_a_binario():
    try:
        decimal = int(entry_numero.get())
        binario = ""
        num_original = decimal  # Guardar el número original para mostrar en el mensaje
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        binario = str(decimal) + binario
        messagebox.showinfo("Resultado", f"El número {num_original} en binario es: {binario}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor Decimal a Binario")
ventana.geometry("300x200")

# Etiqueta y campo para ingresar el número
label_numero = tk.Label(ventana, text="Ingrese el número decimal:")
label_numero.pack(pady=5)
entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5)

# Botón para convertir
boton_convertir = tk.Button(ventana, text="Convertir a Binario", command=convertir_a_binario)
boton_convertir.pack(pady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
