###################HUFFMAN_FRONT###################
### Rivera Reos Fernando de Jesús, UdeG, Cucei ####
###################################################

###########LIBRERIAS##############
import os
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


def comprimir():
    global charFreq, filePath

    node = make_tree(charFreq)
    encoding = code_tree(node)

    if filePath:
        dir_path = os.path.dirname(filePath) # Ruta de la carpeta del archivo
        # file_name es nombre del archivo (sin extensión)
        file_name, file_extension = os.path.splitext(os.path.basename(filePath))  

        # Ruta del archivo sin la extensión del archivo
        file_path_extensionless = os.path.join(dir_path, file_name)
        # Ruta del archivo binario a generar (misma carpeta que el arhivo elegido)
        file_path_bin = file_path_extensionless + ".bin"

        # Intertar extensión del archivo y datos para regenerar el árbol de huffman
        with open(file_path_bin, "w") as wf:
            # Extensión del archivo
            wf.write(file_extension)
            wf.write('\n')
            # Caracteres del texto (del más frecuente al menos)
            for i in charFreq:
                wf.write(i[0])
            wf.write('\n')
            # Número de incidencias (del mayor al menor)
            for i in charFreq:
                wf.write(str(i[1]))
                wf.write('\t') # Tab como separador
            wf.write('\n')
    else:
        print("Abre un archivo")

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
compressButton = tk.Button(buttonFrame, text="Comprimir", command=comprimir)
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
