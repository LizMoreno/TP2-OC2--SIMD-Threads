nasm -f elf32 enmascarar_asm.s -o enmascarar_asm.o;
gcc -m32 -pthreads -o main_hilos_asm enmascarar_asm.o enmascarar_hilos_asm.c;
