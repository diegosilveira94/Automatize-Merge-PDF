#Tela gráfica desenvolvida com apoio do tutorial do site customtkinter

import customtkinter as ctk
from backend.main import merge_Pdf

def button_callback():
    print("botão pressionado")

#Inicio
app = ctk.CTk()
app.title("Cardápio Hausmesse 2025 - PDF")
app.geometry("800x600")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=2)

#Título
titulo = ctk.CTkLabel(app, text="Cardápio Hausmesse 2025")
titulo.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

#Caixa de texto

cx_texto = ctk.CTkEntry(app, bg_color='white', placeholder_text="Digite as opções")
cx_texto.grid(row=1, column=0, padx=20, pady=20, sticky="ew)

#Botão
button = ctk.CTkButton(app, text="Mesclar", command=merge_Pdf)
button.grid(row=2, column=0, padx=20, pady=20)

app.mainloop()