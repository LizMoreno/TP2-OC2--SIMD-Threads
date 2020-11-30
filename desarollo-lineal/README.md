## Tratamiento de imagenes de forma lineal

El codigo itera por sobre las imagenes que se encuentran en un directorio pasado por parametro y guarda los resultados.

Para compilar el codigo y generar un nuevo ejecutable se pueden ejecutar los siguientes comandos:

2. para ASM: 
```
nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -o main_lineal_asm enmascarar_asm.o enmascara_asm_lineal.c;

```
o ejecutar el script que se encuentra en este directorio ./script


1. Para C: 

```
gcc  main_lineal  enmascara_c_lineal.c;

```
o ejecutar el script que se encuentra en este directorio ./script-c

