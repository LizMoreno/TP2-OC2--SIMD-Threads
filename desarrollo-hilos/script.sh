nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -o enmascarar_asm enmascarar_asm.o enmascarar_asm.c;
gcc enmascarar_c.c -o enmascarar_c;