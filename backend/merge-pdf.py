#Nessa primeira versão será mesclados todos os pdf's contidos em uma determinada pasta

import  PyPDF2
import os
from tkinter.filedialog import askdirectory

def merge_pdfs():
    
merger = PyPDF2.PdfMerger() #vincular a função a variável merger
list_arq = os.listdir("Cardápio 2025")
for arq in list_arq:
    if ".pdf" in arq:
        merger.append(f"Pratos Escolhidos/{arq}")
destination = askdirectory(title="Salvar")
merger.write(f"{destination}/PDF-Merged.pdf")
print("PDFs mesclados com sucesso")