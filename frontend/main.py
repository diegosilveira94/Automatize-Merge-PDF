from tkinter.filedialog import askdirectory, askopenfilename
from tkinter import *

#arq_comp = askopenfilename(title="Selecione um arquivo do computador")
#print(arq_comp)

janela = Tk()
janela.title("Mesclagem PDF")

texto_orientacao = Label(janela, text="Selecione os pratos")
texto_orientacao.grid(column=0, row=0)


janela.mainloop()