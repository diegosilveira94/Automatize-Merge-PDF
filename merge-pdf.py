#Basicamente nessa primeira versão será mesclados todos os pdf's contidos em uma determinada pasta

import PyPDF2
import os
merger = PyPDF2.PdfMerger() #inicializa merger
list_arq = os.listdir("PDF_ESCOLHIDOS")
for arq in list_arq:
    if ".pdf" in arq:
        merger.append(f"PDF_ESCOLHIDOS/{arq}")
merger.write("PDF_FINAL.pdf")