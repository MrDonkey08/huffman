###################HUFFMAN_FRONT###################
### Rivera Reos Fernando de Jesús, UdeG, Cucei ####
###################################################

###########LIBRERIAS##############
import tkinter as tk
from tkinter import filedialog  #Módulo para explorar y leer archivos
from collections import Counter #Módulo para crear de manera mas dinamica y sencilla la lista de frecuencia
from huffman import (NodeTree, code_tree, make_tree)

charFreq: Counter
filepath: str

############Funciones#############
def openFile():                                     #Función para leer el archivo y leer su frecuencia de caracteres
    global charFreq, filePath

    filePath = filedialog.askopenfilename()         #Recupera y guarda la ruta del archivo
    if filePath:                                    #Revisa que esta ruta sea de un archivo existente
        file = open(filePath, 'r')                  #Abre el archivo y guarda el objeto del mismo
        content = file.read()                       #Guarda el contenido del archivo en forma de string
        file.close()                                #Cierra el archivo
        charFreq = Counter(content)                 #Counter, se encarga de contar la frecuencia de caracteres del string content
        frequencyListbox.delete(0, tk.END)          #Limpia la listbox de la ventana, en caso de que tenga contenido no deseado
                
        # Se ordena descendentemente, de mayor a menor en un diccionario
        charFreq = dict(sorted(charFreq.items(), key=lambda x: x[1], reverse=True))
        
        #Se imprime la frecuencia en la listbox de la ventana
        for char, freq in charFreq.items():
            frequencyListbox.insert(tk.END, f"' {char} ' : {freq}")

        charFreq = list(charFreq.items()) # Lista de Tuplas

def huffman_tree():
    global charFreq

    node = make_tree(charFreq)
    encoding = code_tree(node)
    for i in encoding:
        print(f"{i} : {encoding[i]}")

    return encoding

#############VENTANA#############

####Ventana principal#####
root = tk.Tk()
root.title("Compresion Huffman")    

###Marco para los botones###
buttonFrame = tk.Frame(root)
buttonFrame.pack(pady=10)
#Boton para examinar archivos
examineButton = tk.Button(buttonFrame, text="Examinar", command=openFile)
examineButton.grid(row=0, column=0, padx=10)
#Boton para mandar a comprimir
compressButton = tk.Button(buttonFrame, text="Comprimir", command=huffman_tree)
compressButton.grid(row=0, column=1, padx=10)
#Boton para descomprimir
decompressButton = tk.Button(buttonFrame, text="Descomprimir")
decompressButton.grid(row=0, column=2, padx=10)

###Marco para mostrar las frecuencias al usuario###
frequencyFrame = tk.Frame(root)
frequencyFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#Etiqueta del marco
frequencyLabel = tk.Label(frequencyFrame, text="Frecuencia de Caracteres:")
frequencyLabel.pack(side=tk.LEFT)
#Caja para mostrar la lista
frequencyListbox = tk.Listbox(frequencyFrame, width=50, height=10)
frequencyListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
