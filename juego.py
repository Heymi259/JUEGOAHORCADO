import tkinter as tk
from tkinter import messagebox
import random

# Lista 
palabras = ["python", "motocross", "enduro", "refrigeradora", "comida", "teclado"]
palabra = random.choice(palabras).upper()
letras_adivinadas = ["_" for _ in palabra]
intentos = 6
letras_usadas = set()

#  interfaz grafica
def actualizar_interfaz():
    lbl_palabra.config(text=" ".join(letras_adivinadas))
    lbl_intentos.config(text=f"Intentos restantes: {intentos}")
    lbl_letras_usadas.config(text=f"Letras usadas: {', '.join(letras_usadas)}")
    dibujar_muñeco()

#  muñeco 
def dibujar_muñeco():
    # Limpiar el lienzo
    canvas.delete("all")
    
    # soporte
    canvas.create_line(50, 250, 150, 250, width=5)  # base
    canvas.create_line(100, 250, 100, 50, width=5)  # palo vertical
    canvas.create_line(100, 50, 200, 50, width=5)  # palo horizontal
    canvas.create_line(200, 50, 200, 100, width=5) # cuerda
    
    #  intentos restantes , muñeco dibujandose 
    if intentos <= 5:  # Cabeza
        canvas.create_oval(180, 100, 220, 140, width=3)
    if intentos <= 4:  # Cuerpo
        canvas.create_line(200, 140, 200, 180, width=3)
    if intentos <= 3:  # Brazo izquierdo
        canvas.create_line(200, 150, 170, 170, width=3)
    if intentos <= 2:  # Brazo derecho
        canvas.create_line(200, 150, 230, 170, width=3)
    if intentos <= 1:  # Pierna izquierda
        canvas.create_line(200, 180, 170, 210, width=3)
    if intentos <= 0:  # Pierna derecha
        canvas.create_line(200, 180, 230, 210, width=3)

#intentos
def intentar_letra():
    global intentos
    letra = entrada_letra.get().upper()
    entrada_letra.delete(0, tk.END)
    
    if letra in letras_usadas or not letra.isalpha() or len(letra) != 1:
        messagebox.showwarning("Error", "Ingrese una letra no repetida.")
        return
    
    letras_usadas.add(letra)
    
    if letra in palabra:
        for i, l in enumerate(palabra):
            if l == letra:
                letras_adivinadas[i] = letra
    else:
        intentos -= 1
    
    if "_" not in letras_adivinadas:
        messagebox.showinfo("¡Felicidades!", "¡Has ganado!")
        ventana.quit()
    elif intentos == 0:
        messagebox.showinfo("Lo siento", f"Has perdido. La palabra era {palabra}")
        ventana.quit()
    
    actualizar_interfaz()

# ventana
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x600")

# ventana para el muñeco
canvas = tk.Canvas(ventana, width=300, height=250)
canvas.pack()

lbl_palabra = tk.Label(ventana, text=" ".join(letras_adivinadas), font=("Arial", 20))
lbl_palabra.pack(pady=20)

lbl_intentos = tk.Label(ventana, text=f"Intentos restantes: {intentos}")
lbl_intentos.pack()

lbl_letras_usadas = tk.Label(ventana, text=f"Letras usadas: {', '.join(letras_usadas)}")
lbl_letras_usadas.pack()

entrada_letra = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_letra.pack(pady=10)

btn_intentar = tk.Button(ventana, text="Intentar", command=intentar_letra)
btn_intentar.pack()

actualizar_interfaz()
ventana.mainloop()