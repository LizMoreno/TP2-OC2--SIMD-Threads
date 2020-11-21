nasm -f elf32 enmascarar_asm.s -o enmascarar.o;
gcc -m32 -o main enmascarar.o enmascarar_c.c;
