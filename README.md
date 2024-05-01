# Algoritmo de Compresión de Huffman

## Introducción

### Archivos

#### Funcionamiento de los Archivos

Los **archivos** (texto, imágenes, videos, etc.) contienen un su interior _bytes de información_ los cuales, al ser decodificados por el algoritmo correcto o, dicho de otra manera, al ser abiertos por el programa correcto, pueden transmitir la información al usuario (texto, imágenes, videos, etc.) o hacer uso de ella.

#### Compresión de un Archivo

Los _archivos convencionales_ pueden consumir mucha memoria. Sin embargo, cuando estos archivos no son utilizados frecuentemente, estos archivos pueden ser codificados o convertidos a otros formatos (archivos de compresión) para disminuir su tamaño. Cabe destacar que, para poder ser utilizados normalmente, tienen que ser convertidos/decodificados devuelta al formato original (descomprimir). Los algoritmos que hacen lo previamente mencionado son conocidos como **algoritmos de compresión**.

### Algoritmo de Huffman

#### Compresión

La **compresión de Huffman**, o también conocida como la **codificación de Huffman** (desarrollada por David Huffman), es una técnica utilizada para comprimir/codificar cualquier formato de archivo sin pérdida de información (_lossless_).

Este algoritmo consiste en:

1. Contar cuántas veces aparece un mismo byte de información en un archivo y así sucesivamente con cada uno de los diferentes tipos de bytes.

> [!NOTE]
>
> En archivos de texto plano, un carácter equivaldría a un byte de información (mientras no sea UTF-16 o mayor). Por lo que consistiría en contar cuántas veces aparece cada letra/caracter.

2. Organizar el conteo de los bytes descendentemente mayor a menor.

3. Generar el árbol binario de Huffman empezando desde abajo hacia arriba.

> [!IMPORTANT]
>
> El nodo raíz y los nodos hojas tienen que estar ordenados descendentemente tal como se describe en el paso 2.

4. Generar el índice: Guardar cada uno de los tipos de bytes descendentemente.

5. Codificar el archivo original haciendo uso del árbol: Leer cada byte, guardar el recorrido que hace cada byte en el árbol en el archivo nuevo.

#### Descompresión

1. Reconstruir el árbol leyendo los bytes del _índice del archivo de compresión_.

2. Leer el archivo y decodificar el archivo comprimido haciendo uso del árbol.

3. Guardar cada uno de los bytes decodificados en el archivo nuevo.

## Objetivos

### Objetivos Generales

- [x] Desarrollar el algoritmo de codificación/compresión de Huffman para la compresión de archivos en python.

### Objetivos Especificos

- [x] Desarrollar una interfaz gráfica en la que existan 3 botones:
  - [x] **Abrir archivo**: Deberá permitir al usuario escoger el archivo a comprimir.
  - [x] **Comprimir archivo**:
    - [x] Hará el conteo de cada uno de los bytes, generará una lista y la imprimirá.
    - [x] Construirá el árbol de huffman a partir de la lista generada.
  - [x] **Descomprimir archivo**:
    - [x] Seleccionar el archivo a descomprimir.
    - [x] Generar archivo descomprimido.

## Desarrollo

### Implementación del Algoritmo

#### Frontend

Desarrollé las siguientes funciones:

- `openFile`: Despliega un gestor de archivos para que el usuario seleccione un archivo y lo guarda en la variable global `filePath`.

- `count_chars()`: Cuenta cada una de las instancias de cada byte/carácter del archivo. Guarda el conteo en el _counter_ `chars`, teniendo como _key_ el conteo y como _value_ el conteo; lo ordena descendentemente y lo convierte en una lista de tuplas y lo guarda en la variable global `charFreq`.

#### Backend

##### huffman.py

Desarrollé la clase `NordTree` la cual simplemente establece el nodo izquierdo o derecho de un árbol (o subárbol) y además como método regresa cada uno de estos nodos.

Desarrollé las siguientes funciones:

- `code_tree(node, binString='')`: Se encarga de generar los códigos para cada uno de los nodos, de los carácteres.

`make_tree(nodes)`: Se encarga de generar el árbol de Huffman. Regresa la raíz del árbol

##### frontend.py

- `comprimir()`: Usa la función `count_chars` para después con ayuda de `make_tree()` y `code_tree()` generar el árbol y los códigos respectivamente, luego guarda los datos para regenerar estos dos datos en el archivo .bin y por último utiliza la función `data_compression`.

- `data_compression(filePath, file_bin, encoding)`: Añade al archivo .bin cada uno de los caracteres del archivo original, codificados con el árbol de Huffman.

- `get_extensions`: Función auxiliar que sirve para renombrar el arhivo a comprimir o descomprimir con la extensión adecuada.

- `get_tree_data(file, char_freq)`: Extrae del archivo .bin los valores necesarios para regenerar el árbol de Huffman. Regresa estos valores.

- `descomprimir()`: Utiliza la función `get_tree_data()` para obtener la frecuencia de carácteres y la extensión del archivo. Después, al igual que `compresión`, genera el árbol de Huffman, extra el contenido del archivo .bin y lo decodifica haciendo uso de los códigos generados a través del árbol de Huffman.

## Conclusión

En retrospectiva los **algoritmos voraces** permiten resolver un problema tomando la mejor opción disponible en el momento. Estos algoritmos son muy importantes debido a que permiten establecer soluciones a problemas que son imposible o muy difíciles de abordar para conseguir la mejor respuesta.

La codificación de huffman resuelve uno de los principales problemas en la actualidad, el reducir el tamaño de los archivos sin pérdida de información. Este algoritmo también permite reducir el costo de envio de paquetes a través de redes, compriéndolo al enviarlo y descomprimiendo al ser recibido.

Respecto al trabajo de un proyecto ajeno, se me hizo una experiencia muy interesante ya que me permitió ver la manera en que trabaja otro desarrollador, el ver cómo colaborar a un proyecto, aprender a interpretar el código y a adaptarme a la implementación de otro desarrollador. Fue una experiencia muy interesante, divertida, pero agotadora.

Por último, es importante mencionar que este es un algoritmo voraz debido que no existe una manera perfecta de comprimir datos, pero este toma la mejor opción posible para la compresión. Divide el problema en subproblemas al resolver la compresión del archivo al trabajar con cada uno de los bytes. Y una que ha sido codificado un byte, este no puede ser revertido

## Referencias

- [Vega, F.](https://platzi.com/profes/freddier/) (marzo 16, 2017). _Cómo funciona .zip: Árboles binarios_. Platzi. https://platzi.com/new-home/clases/1098-ingenieria/6574-como-funciona-zip-arboles-binarios/

- Programmiz (s. f.). _Huffman Coding_. https://www.programiz.com/dsa/huffman-coding

- Reducible (julio, 29, 2021). _Huffman Codes: An Information Theory Perspective_. https://odysee.com/@Reducible:8/huffman-codes-an-information-theory
