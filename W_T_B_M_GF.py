import tkinter as tk
import random
import winsound # Librería nativa de Windows para audio

def esquivar_boton(event):
    # Calcula una nueva posición aleatoria para el botón "No"
    # Basado en el ancho y alto real de la pantalla
    ancho_ventana = root.winfo_screenwidth()
    alto_ventana = root.winfo_screenheight()
    
    # Margen para que no se salga de los bordes
    nuevo_x = random.randint(50, ancho_ventana - 150)
    nuevo_y = random.randint(50, alto_ventana - 100)
    btn_no.place(x=nuevo_x, y=nuevo_y)

def salir_pantalla_completa(event=None):
    # Permite salir con la tecla Esc
    root.attributes("-fullscreen", False)

def decir_si():
# --- REPRODUCIR LA CANCIÓN ---
    try:
        # IMPORTANTE: El archivo DEBE ser .wav para que winsound funcione
        winsound.PlaySound("C:\\Users\\USUARIO\\Documents\\Codes\\Python\\Bésame-Darviin.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    except Exception as e:
        print("No se pudo reproducir la música.")

    # 1. Hacemos que el "TE AMO", el Corazón aparezcan y el mensaje central se actualice
    lbl_te_amo.pack(pady=(100, 0), before=lbl_pregunta)
    lbl_corazon.pack(pady=(0, 10), before=lbl_pregunta)
    lbl_ya_sabia.pack(pady=(0, 50), before=lbl_pregunta)
    
    # 2. Ocultamos los botones permanentemente
    btn_si.place_forget()
    btn_no.place_forget()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Propuesta a Den")
root.configure(bg='black')

# --- CONFIGURACIÓN DE PANTALLA COMPLETA ---
root.attributes("-fullscreen", True)
root.bind("<Escape>", salir_pantalla_completa)

# Dimensiones de la pantalla para posicionamiento
ancho_p = root.winfo_screenwidth()
alto_p = root.winfo_screenheight()

# --- ELEMENTOS OCULTOS AL INICIO ---
# Texto superior
lbl_te_amo = tk.Label(root, text="TE AMO", font=("Courier", 70, "bold"), bg='black', fg="#a017df")
# Corazón gigante
lbl_corazon = tk.Label(root, text="❤", font=("Courier", 280), bg='black', fg="#594CAF")
# El mensaje central se mantiene visible pero se actualizará al hacer clic en "Sí"
lbl_ya_sabia = tk.Label(root, text="Ya sabía que dirías que sí 😉 \n ❤ Te amo Wundershöne ❤", font=("Courier", 30, "bold"), bg='black', fg="white")

# --- ELEMENTOS VISIBLES DESDE EL INICIO ---
# Pregunta central (posicionada inicialmente con un margen superior)
lbl_pregunta = tk.Label(root, text="¿Quieres ser mi novia?", font=("Courier", 45, "bold"), bg='black', fg='white')
lbl_pregunta.pack(pady=(alto_p//3, 0))

# Botones posicionados respecto al centro
btn_si = tk.Button(root, text="Sí", font=("Courier", 24, "bold"), bg="#594CAF", fg='white', 
                   command=decir_si, width=10, cursor="heart", bd=0)
btn_si.place(x=ancho_p//2 - 250, y=alto_p//2 + 150)

btn_no = tk.Button(root, text="No", font=("Courier", 24, "bold"), bg='#f44336', fg='white', width=10, bd=0)
btn_no.place(x=ancho_p//2 + 50, y=alto_p//2 + 150)

# Evento para que el botón "No" escape
btn_no.bind("<Enter>", esquivar_boton)

# Iniciar la interfaz
root.mainloop()