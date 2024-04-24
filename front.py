###################HUFFMAN_FRONT###################
### Rivera Reos Fernando de Jesus, UdeG, Cucei ####
###################################################

###########LIBRERIAS##############
import tkinter as tk
from tkinter import filedialog  #Modulo para explorar y leer archivos
import collections              #Modulo para crear de manera mas dinamica y sencilla la lista de frecuencia

############FUNCIONES#############
def openFile():                                    #Funcion para leer el archivo y leer su frecuencia de caracteres

    filePath = filedialog.askopenfilename()         #Recupera y guarda la ruta del archivo
    if filePath:                                    #Revisa que esta ruta sea de un archivo existente
        file = open(filePath, 'r')                  #Abre el archivo y guarda el objeto del mismo
        content = file.read()                       #Guarda el contenido del archivo en forma de string
        file.close()                                #Cierra el archivo
        charFreq = collections.Counter(content)     #Counter, se encarga de contar la frecuencia de caracteres del string content
        frequencyListbox.delete(0, tk.END)          #Limpia la listbox de la ventana, en caso de que tenga contenido no deseado
        
        #Se imprime la frecuencia en la listbox de la ventana
        for char, freq in charFreq.items():
            frequencyListbox.insert(tk.END, f"' {char} ' : {freq}")


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
compressButton = tk.Button(buttonFrame, text="Comprimir")
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
