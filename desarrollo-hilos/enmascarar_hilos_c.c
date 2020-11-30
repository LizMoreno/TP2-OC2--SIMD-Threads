#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <time.h>
#include <pthread.h>


struct parametros {
    char * imagen_1;
    char * imagen_2;
    char * imagen_3;

    char * imagen_aplicable;
    char * mascara;
    int ancho;
    int alto;
};



/* Obtiene el nombre del fichero con la ruta completa */
char *getFullName(char *ruta, struct dirent *ent);
void procesarArchivos(char * imagen1, char *imagen2, char *mask, int ancho, int alto);
char *getAFancyFileName(char *a, char* b);
char* cut_four (char* s);


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

void funcion_hilos(void *arg){
    struct parametros *p;
    p = (struct parametros *) arg;
    //->
    procesarArchivos(p -> imagen_1, p -> imagen_aplicable, p -> mascara, p -> ancho, p -> alto);

    //procesarArchivos(p.imagen_1, p.imagen_aplicable, p.mascara, p.ancho, p.alto):
    procesarArchivos(p -> imagen_2, p -> imagen_aplicable, p -> mascara, p -> ancho, p -> alto);
    procesarArchivos(p -> imagen_3, p -> imagen_aplicable, p -> mascara, p -> ancho, p -> alto);


}

void procesarArchivos(char * imagen1, char *imagen2, char *mask, int ancho, int alto) {

    
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
    char * coolFileName  = getAFancyFileName(imagen1,imagen2);
    guardarArchivo(coolFileName, cant, a);

    //Liberar memoria
    free(a);
    free(b);
    free(mascara);
}

int main (int argc, char* argv[]) {
 

    clock_t tiempo_inicio, tiempo_final;
    double segundos = 0.0;
    int contador = 0;
    pthread_t hilo;
    struct parametros param;
    tiempo_inicio = clock();
    if (argc != 6)
    {
        printf("Error al ingresar los parametros\n");
        return 1;
    }
  DIR* directorio;
 
  struct dirent* elemento;
 
  //Parametros
  char * ruta = argv[1]; //directorio de imagenes
  char *imagen2 = argv[2]; //imagen2
  char *mask = argv[3]; //mascara
  int ancho = atoi(argv[4]); //para pasar el argumento a int 
  int alto = atoi(argv[5]); //para pasar el argumento a int

    //strcpy(param.imagen_aplicable,imagen2);
    //strcpy(param.mascara,mask);
    param.imagen_aplicable=imagen2;
    param.mascara=mask;
    param.ancho = ancho;
    param.alto = alto;

  directorio=opendir (ruta);
 
  if (directorio==NULL) {
    printf ("Error de Lectura en el Directorio \n");
    return EXIT_FAILURE;
  }
 
  elemento=readdir (directorio);
  
 
  while (elemento!=NULL) {
    char * nombreCompleto; 

    if ( (strcmp(elemento->d_name, ".")!=0) && (strcmp(elemento->d_name, "..")!=0) ){

    nombreCompleto = getFullName(ruta, elemento);
     // elemento->d_name;
   
    // aca van las operaciones sobre los elementos

 

    if ( contador == 2 ){
        param.imagen_3 = nombreCompleto;
        contador++;
    }
        
    if ( contador == 1 ){
        param.imagen_2 = nombreCompleto;
        contador++;
    }
    if ( contador ==0 ){
        param.imagen_1 = nombreCompleto;
        contador = contador+1;
    }

       if ( contador == 3 ){
        //creamos el hilo
        printf("Creamos hilo\n");
        contador = 0;
        pthread_create(&hilo, NULL, funcion_hilos, (void *)&param);
        pthread_join(hilo,NULL);

    }
    }
   
    elemento=readdir (directorio);
   
  }
  closedir (directorio);

    tiempo_final = clock();

    segundos = (double)(tiempo_final - tiempo_inicio) / CLOCKS_PER_SEC;
    printf("%.16g milisegundos\n", segundos * 1000.0);

  return EXIT_SUCCESS;
 
}

char *getFullName(char *ruta, struct dirent *ent)
{
  char *nombrecompleto;
  int tmp;

  tmp=strlen(ruta);
  nombrecompleto=malloc(tmp+strlen(ent->d_name)+2); /* Sumamos 2, por el \0 y la barra de directorios (/) no sabemos si falta */
  if (ruta[tmp-1]=='/')
    sprintf(nombrecompleto,"%s%s", ruta, ent->d_name);
  else
    sprintf(nombrecompleto,"%s/%s", ruta, ent->d_name);
  
  return nombrecompleto;
}

char *getAFancyFileName(char *a, char* b)
{
  char *nombrecompleto= NULL;
  nombrecompleto = strdup(cut_four(a));

  nombrecompleto = strcat(nombrecompleto,cut_four(b) );
  strcat(nombrecompleto, ".rgb");
  
  printf("Nombre del file generado %s\n", nombrecompleto);

  return nombrecompleto;
}

char* cut_four (char* s){
    int n;
    int i;
    char* new;
    for (i = 0; s[i] != '\0'; i++);
    // lenght of the new string
    n = i - 4 + 1;
    if (n < 1)
        return NULL;
    new = (char*) malloc (n * sizeof(char));
    for (i = 0; i < n - 1; i++)
        new[i] = s[i];
    new[i] = '\0';
    return new;
}