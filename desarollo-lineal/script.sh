nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -o main_lineal_asm enmascarar_asm.o enmascara_asm_lineal.c;
