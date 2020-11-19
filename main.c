#include <stdio.h>
#include <stdlib.h>


void enmascarar_c(unsigned char *a, unsigned char *b, unsigned char *mask, int cant);
void enmascarar_asm(unsigned char *a, unsigned char *b, unsigned char *mask, int cant);


void enmascarar_c(unsigned char *a, unsigned char *b, unsigned char *mask, int cant)
{
    for(int i=0;i<cant;i++){
        if(mask[i]!=0){ //0 si es negro - 255 si es blanco
	        a[i] = b[i];
	    }
    }
}

void abrirArchivo(char *nombreArchivo, int cantidad, unsigned char *buffer)
{
    FILE *fp;
    fp = fopen(nombreArchivo,"rb"); 
    if (fp == NULL){
        printf("Error al abrir el archivo\n");
    }else{
    	fread(buffer, cantidad, 1,fp); 
    }
    fclose(fp);
}

void guardarArchivo(char *nombreArchivo, int cantidad, unsigned char *buffer)
{
    FILE *fp;
    fp = fopen(nombreArchivo,"wb"); 
    fwrite(buffer, 1, cantidad, fp);
    fclose(fp);
}
int main (int argc, char *argv[]){
	if (argc != 6)
    {
        printf("Error al ingresar los parametros\n");
        return 1;
    }

    
	
    return 0;
}
