
## Tratamiento de imagenes de utilizando hilos

El codigo itera por sobre las imagenes que se encuentran en un directorio pasado por parametro y guarda los resultados.

Para compilar el codigo y generar un nuevo ejecutable se pueden ejecutar los siguientes comandos:
2. para ASM: 
```
nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -pthreads -o main_hilos_asm enmascarar_asm.o enmascarar_hilos_asm.c;

```
o ejecutar el script que se encuentra en este directorio ./script
1. Para C: 

```
gcc -pthreads main_hilos_c enmascarar_asm.o enmascarar_hilos_c.c;

```
o ejecutar el script que se encuentra en este directorio ./script-c



