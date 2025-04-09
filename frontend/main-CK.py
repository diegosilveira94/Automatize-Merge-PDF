#Tela gráfica desenvolvida com apoio do tutorial do site customtkinter

import customtkinter as ck

#Initial
app = ck.CTk()
app.title("Cardápio Hausmesse 2025 - PDF")
app.geometry("800x600")


#button merger
def button_callback():
    
button = ck.CTkButton(app, text="Mesclar", command=button)

app.mainloop()