nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -o mian_lineal enmascarar_asm.o enmascarar_asm.c;
