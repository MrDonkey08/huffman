###################HUFFMAN_FRONT###################
### Rivera Reos Fernando de Jesús, UdeG, Cucei ####
###################################################

###########LIBRERIAS##############
from BitVector import BitVector
import os
import tkinter as tk
from tkinter import filedialog  #Módulo para explorar y leer archivos
from collections import Counter #Módulo para crear de manera mas dinamica y sencilla la lista de frecuencia
from huffman import (NodeTree, code_tree, make_tree)

charFreq = []
filepath = ''

############Funciones#############
def openFile():                                     #Función para leer el archivo y leer su frecuencia de caracteres
    global filePath
    filePath = filedialog.askopenfilename()         #Recupera y guarda la ruta del archivo

def count_chars():
    global filePath, charFreq

    if filePath:                                    #Revisa que esta ruta sea de un archivo existente
        file = open(filePath, 'r', encoding='utf-8')#Abre el archivo y guarda el objeto del mismo
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

def get_extensions(file):
    dir_path = os.path.dirname(filePath) # Ruta de la carpeta del archivo
    # file_name es nombre del archivo (sin extensión)
    file_name, file_extension = os.path.splitext(os.path.basename(filePath))  

    # Ruta del archivo sin la extensión del archivo
    file_path_extensionless = os.path.join(dir_path, file_name)
    # Ruta del archivo binario a generar (misma carpeta que el arhivo elegido)

    return dir_path, file_name, file_extension, file_path_extensionless

def comprimir():
    count_chars()

    global charFreq, filePath

    if filePath:
        node = make_tree(charFreq)
        encoding = code_tree(node)

        dir_path, file_name, file_extension, file_path_extensionless = get_extensions(filePath)

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

        data_compression(filePath, file_path_bin, encoding)
    else:
        print("Abre un archivo")

def data_compression(file, file_bin, encoding):
    # Número de carácteres
    n_char = sum(count for _, count in charFreq)
    bits = n_char % 8 # Número de Bits que no completan un Byte

    rchar = True
    codes = ''

    # Lee el archivo, codifica su contenido y lo guarda en `code`
    with open(file, "r") as rf:
        while rchar:
            rchar = rf.read(1)
            for i in encoding:
                if rchar == i:
                    codes += encoding[i]
                    break

    aux = ''
    # Inserción de contenido codificado en el archivo .bin
    with open(file_bin, 'ab') as af:
        for i in codes:
            aux += i

            if len(aux) % 8 == 0:
                bv = BitVector(bitstring = aux)
                bv.write_to_file(af)
                aux = ''

    print("Archivo comprimido")

def descomprimir():
    global charFreq, filePath

    if filePath:
        new_file, charFreq = get_tree_data(filePath, charFreq)
        node = make_tree(charFreq)
        encoding = code_tree(node)

        rchar = True

        with open(filePath, 'rb') as rf:
            with open(new_file, 'w') as wf:
                for _ in range(4):
                    rf.readline()

                line = rf.readline()
                bits = ''

                # Guardando los bits (ceros y unos) en str
                while line:
                    bits += ''.join(format(byte, '08b') for byte in line)
                    line = rf.readline()

                code = ''

                # Decodificando los bits en carácteres
                for bit in bits:
                    for i in encoding:
                        if code == encoding[i]:
                            wf.write(i)
                            code = ''
                            break
                    
                    code += bit

    print("Descomprimido")


def get_tree_data(file, char_freq):
    if file:
        dir_path, file_name, file_extension, file_path_extensionless = get_extensions(filePath)

        charFreq = []
        codes = []

        with open(filePath, 'rb') as rf:
            new_ext = rf.readline().decode('utf-8')
            new_ext = new_ext[:-1] # Para eliminar el último caracter (\n)

            chars = rf.readline().decode('utf-8')
            chars += rf.readline().decode('utf-8')
            chars = chars[:-1]

            nums = rf.readline().decode('utf-8').split('\t')
            nums = nums[:-1]
            codes = [int(code) for code in nums]

        for char, code in zip(chars, codes):
            char_freq.append((char, code))

        new_file = file_path_extensionless + new_ext

    return new_file, char_freq

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
decompressButton = tk.Button(buttonFrame, text="Descomprimir", command=descomprimir)
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
