import os
import sys
import PyPDF2
from tkinter.filedialog import askdirectory

def resource_path(relative_path):
    """Retorna o caminho absoluto para o recurso, funciona no PyInstaller (.exe) e no Python normal"""
    try:
        base_path = sys._MEIPASS  # usado pelo PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def merge_Pdf():
    merger = PyPDF2.PdfMerger()

    cardapio_path = resource_path("Cardápio 2025")
    pratos_path = resource_path("Pratos Escolhidos")

    list_arq = os.listdir(cardapio_path)
    for arq in list_arq:
        if arq.endswith(".pdf"):
            merger.append(os.path.join(pratos_path, arq))

    destination = askdirectory(title="Salvar")
    merger.write(os.path.join(destination, "PDF-Merged.pdf"))
    print("PDFs mesclados com sucesso")


merge_Pdf()
