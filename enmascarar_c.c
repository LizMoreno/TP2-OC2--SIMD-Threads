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

// Main
int main(int argc, char *argv[])
{
    if (argc != 6)
    {
        printf("Error al ingresar los parametros\n");
        return 1;
    }
    
    //Parametros
    char *imagen1 = argv[1]; //imagen1
    char *imagen2 = argv[2]; //imagen2
    char *mask = argv[3]; //mascara
    int ancho = atoi(argv[4]); //para pasar el argumento a int 
    int alto = atoi(argv[5]); //para pasar el argumento a int
    
    int cantidadxPixel = 3; //RGB 3 bytes por pixel
    int cant = ancho * alto * cantidadxPixel;
    
    //Reservar memoria dinámica
    unsigned char *a = malloc(cant);
    unsigned char *b = malloc(cant);
    unsigned char *mascara = malloc(cant);

    //Abrimos las imagenes
    abrirArchivo(imagen1, cant, a);
    abrirArchivo(imagen2, cant, b);
    abrirArchivo(mask, cant, mascara);

    enmascarar_c(a, b, mascara, cant);    
    enmascarar_asm(a, b, mascara, cant);

    guardarArchivo("salida_c.rgb", cant, a);
    guardarArchivo("salida_asm.rgb", cant, a);
    
    //Liberar memoria
    free(a);
    free(b);
	free(mascara);

    return 0;
}
