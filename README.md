# TP2-OC2--SIMD-Threads


```
sudo sh script.sh
```
* Ejecutar programa
```
./main "disney.rgb" "anomalia.rgb" "mascara640.rgb" 640 360
```
* Para convertir jpg a rgb o viceversa
```
gm convert -size 640x360 -depth 8 salida_asm.rgb salida_asm.jpg
gm convert -size 640x360 -depth 8 salida_c.rgb salida_c.jpg
```
* Visualizar
```
gm display salida_c.jpg
```
