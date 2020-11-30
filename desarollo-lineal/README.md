## Tratamiento de imagenes de forma lineal

El codigo itera por sobre las imagenes que se encuentran en un directorio pasado por parametro y guarda los resultados.

Para compilar el codigo y generar un nuevo ejecutable se pueden ejecutar los siguientes comandos:
```
nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -o mian_lineal enmascarar_asm.o enmascarar_asm.c;

```
o ejecutar el script que se encuentra en este directorio.
