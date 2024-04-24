# huffman

El código es una aplicación básica de interfaz gráfica de usuario (GUI) escrita en Python utilizando la biblioteca Tkinter. La aplicación tiene la funcionalidad de examinar archivos, calcular la frecuencia de caracteres en el archivo seleccionado y mostrar esta frecuencia en una lista en la interfaz gráfica.

1. Librerías Utilizadas:

tkinter: Para crear la interfaz gráfica.
filedialog: Para proporcionar una interfaz de exploración de archivos.
Collections: Para manejar la lista de frecuencia de caracteres de manera más eficiente.


2. Funciones:

openFile(): Esta función se activa cuando se hace clic en el botón "Examinar". Abre un cuadro de diálogo para que el usuario seleccione un archivo. Luego, lee el contenido del archivo, calcula la frecuencia de los caracteres en el contenido y muestra esta frecuencia en la ventana de la aplicación.

3. Interfaz de Usuario:

Se crea una ventana principal (root) con el título "Compresión Huffman".
Se crea un marco para los botones (buttonFrame) que contiene tres botones: "Examinar", "Comprimir" y "Descomprimir".
Se crea otro marco (frequencyFrame) para mostrar la frecuencia de caracteres del archivo seleccionado.
Se utiliza una etiqueta para indicar el propósito de la lista que muestra la frecuencia.
Se utiliza una Listbox para mostrar la frecuencia de caracteres.
La lista de frecuencia se actualiza cada vez que se selecciona un nuevo archivo.

4. Ejecución:

El programa se ejecuta mediante root.mainloop(), lo que inicia el bucle principal de la interfaz gráfica.
