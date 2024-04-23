import tkinter as tk
from tkinter import filedialog
import collections

def open_file():
    filePath = filedialog.askopenfilename()
    if filePath:
        file = open(filePath, 'r')
        content = file.read()
        file.close()
        charFreq = collections.Counter(content)
        frequencyListbox.delete(0, tk.END)
        for char, freq in charFreq.items():
            frequencyListbox.insert(tk.END, f"' {char} ' : {freq}")

root = tk.Tk()
root.title("Compresion Huffman")

buttonFrame = tk.Frame(root)
buttonFrame.pack(pady=10)

examineButton = tk.Button(buttonFrame, text="Examinar", command=open_file)
examineButton.grid(row=0, column=0, padx=10)

compressButton = tk.Button(buttonFrame, text="Comprimir")
compressButton.grid(row=0, column=1, padx=10)

decompressButton = tk.Button(buttonFrame, text="Descomprimir")
decompressButton.grid(row=0, column=2, padx=10)

frequencyFrame = tk.Frame(root)
frequencyFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

frequencyLabel = tk.Label(frequencyFrame, text="Frecuencia de Caracteres:")
frequencyLabel.pack(side=tk.LEFT)

frequencyListbox = tk.Listbox(frequencyFrame, width=50, height=10)
frequencyListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
