;%include "io.inc"

section .data
    cantidad dd 0
    
section .text
    global enmascarar_asm
   
enmascarar_asm:
    push ebp ;apunta a la base de la pila
    mov ebp, esp 
    
    ;void enmascarar_asm(unsigned char *a, unsigned char *b, unsigned char *mask, int cant);
    mov ecx, 0 ;contador
  
    mov edx,[ebp+20] ;apunta a cant
    mov [cantidad],edx
    
  ciclo:
    cmp ecx, [cantidad]  
    JE salir
    
    ;parametros
    mov eax,[ebp+8]  ;imagen a
    MOVQ mm0,[eax+ecx] 
   
    mov eax,[ebp+12]  ;imagen b
    MOVQ mm1,[eax+ecx]
    
    mov eax,[ebp+16] ;mascara
    MOVQ mm2,[eax+ecx]

   
    PAND mm1, mm2 ;mantiene la imagen b cuando el pixel es negro 
    PANDN mm2, mm0 ;mantiene la imagen a cuando el pixel es distinto de FFFFFF
    POR mm1, mm2
       
    ;debe devolver la imagen a - combinada con a y b 
    mov eax,[ebp+8]
    MOVQ [eax+ecx], mm1
 
    add ecx, 8 ; manejamos registros de mmx , se desplaza de a 64 bits
    JMP ciclo
    
   salir:
    mov esp, ebp ;reinicio la pila
    pop ebp 
    
    ret