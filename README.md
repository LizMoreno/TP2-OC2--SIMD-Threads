# TP2-OC2--SIMD-Threads

### Primera Parte
se debe implementar la función enmascarar_asm en lenguaje ensamblador de
32 bits usando instrucciones SIMD y respetando la convención de C de pasaje de parámetros. Al igual
que enmascarar_c en el lenguaje C. Ambas funciones deben pisar el contenido del buffer a, con el
resultado de combinar a y b usando la máscara mask.
Además se debe implementar un programa en C que reciba los parámetros mencionados por
línea de comandos y que llame a las dos funciones para generar dos archivos (salida_c.rgb y
salida_asm.rgb) que corresponden a las imágenes producidas por las dos llamadas.

Funciones desarrolladas:
* Función enmascarar_c ( unsigned char *a, unsigned char *b, unsigned char *mask, int
cant );
* Función enmascarar_asm ( unsigned char *a, unsigned char *b, unsigned char *mask,
int cant);

El codigo se encuentra [Aqui.](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/tree/master/funciones)

### Ejecucion del programa:
Una primera version del programa ejecuta ambas funciones devolviendo las imagenes nuevas generadas.

* ./main "disney.rgb" "anomalia.rgb" "mascara640.rgb" 640 360

## Paralelismo

se requiere medir la performance incorporando paralelismo. Para ello, se deberá implementar la lógica en C para
procesar un conjunto de imágenes utilizando threads. Cabe mencionar que el tamaño de las
imágenes del conjunto puede variar. Se requieren de ciertas métricas para evidenciar los
resultados obtenidos luego de las ejecuciones. Para ello, se debe realizar un breve documento
(README) donde se analice los resultados obtenidos basándose en los tiempos de respuesta
para las pruebas realizadas y gráficos comparativos.

### Desarrollo lineal

### Ejecucion del programa:
Implementamos un programa que toma in directorio del en el que se encuentran las imagenes. De esta forma contamos con la logica necesaria para procesar un conjunto de imagenes utilizando las funciones *enmascarar_c* y *enmascarar_asm*.

El codigo se encuentra [Aqui.](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/tree/master/desarollo-lineal)

#### Implementacion en C

Para ejecutar el programa en C se encontrara en la siguiente carpeta. El programa recibe una serie de parametros que vamos a mecionar a continuacion:

1. el primer parametro es el directorio de donde recuperara las imagenes.
2. el segundo parametro es la imagen que se aplica sobre la mascara.
3. el tercer parametro es la mascara a aplicar.
4. el cuarto es el ancho.
5. el quinto es el alto.
Aqui dejamos un ejemplo de como ejecutar el programa

Recibe: 

1er parametro: un directorio del cual toma las imagenes que van en el fondo

2do parametro: la imagen que se aplica sobre la mascara

3er parametro: la mascara

4to y 5to parametro: ancho y largo

Demostracion de como seria el llamado:
```
  $./main_lineal "[tu-directorio-de-imagenes]" "imagen-a-aplicar" "mascara" ancho alto
```
ejemplo:
* ./main_lineal "/home/lapassesungs/Descargas/TP2-OC2--SIMD-Threads-branchLizz/imagenes/" "disney.rgb" "mascara640.rgb" 640 360

Para ver como compilar el Codigo y generar un nuevo ejecutable, Aqui.

#### Implementacion en ASM

La forma de ejecutar es igual a la implementacion en C (misma forma de invocar al proceso).

Demostracion de como seria el llamado:
```
  $./main_lineal_nasm "[tu-directorio-de-imagenes]" "imagen-a-aplicar" "mascara" ancho alto
```
ejemplo:
* ./main_lineal_nasm "/home/lapassesungs/Descargas/TP2-OC2--SIMD-Threads-branchLizz/imagenes/" "disney.rgb" "mascara640.rgb" 640 360

### Desarrollo con hilos
En esta ocasion contamos con hilos para el procesamiento de las imagenes que se encuentran en el directorio.
El codigo se encuentra [Aqui.](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/tree/master/desarrollo-hilos)

#### Implementacion en C
El programa actua similar a su respectuva implementacion en de forma lineal, solo que al recuperar 3 archivos de la carpeta, dispara un hilo que se encarga de procesar las imagenes, mientras continua recorriendo los archivos. Asi, cada 3 archivos/imagenes encontados dispara un hilo para que procese esa informacion.

Demostracion de como seria el llamado:
```
  $./main_hilos_c "[tu-directorio-de-imagenes]" "imagen-a-aplicar" "mascara" ancho alto
```
ejemplo:
* ./main_hilos_c "/home/lapassesungs/Descargas/TP2-OC2--SIMD-Threads-branchLizz/imagenes/" "disney.rgb" "mascara640.rgb" 640 360

Para ver como compilar el Codigo y generar un nuevo ejecutable, Aqui.

#### Implementacion en ASM

La forma de ejecutar es igual a la implementacion en C.

Demostracion de como seria el llamado:
```
  $./main_hilos_asm "[tu-directorio-de-imagenes]" "imagen-a-aplicar" "mascara" ancho alto
```
ejemplo:
* ./main_hilos_asm "/home/lapassesungs/Descargas/TP2-OC2--SIMD-Threads-branchLizz/imagenes/" "disney.rgb" "mascara640.rgb" 640 360


## Resultados de las comparaciones

Para analizar los distintos tiempos sobre los procesamientos de imagenes tomamos un total de 13 imagenes en **rgb** para comparar los tiempos.
Los resultados arrojados por cada proceso

1. De forma lineal en C:
![alt text](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/blob/master/img-sources/tiempo-lineal-c.png)

2. Utilizando hilos en C:
![alt text](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/blob/master/img-sources/tiempo-hilos-c.png)

3. De forma lineal en ASM:
![alt text](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/blob/master/img-sources/tiempo-lineal-asm.png)

4. Utilizando hilos en ASM:
![alt text](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/blob/master/img-sources/tiempo-hilos-asm.png)

### Comparaciones
En retrospectiva, comparando el tiempo entre C y ASM marca una notable diferencia. Por un lado los procesos en ASM son mucho mas rapidos que los procesos en C. Algo que nos sorprende es como el proceso que recorre de forma lineal demostro ser mas veloz que el proceso que utilizaba paralelismo para el procesamiento de imagenes. Podemos considerar que nuestra implementacion untroduzco un overhead por sobre las tareas.

A continuacion tenemos un diagrama para comparar las pruebas realizadas:

![alt text](https://github.com/LizMoreno/TP2-OC2--SIMD-Threads/blob/master/img-sources/chart-procesos.png)


