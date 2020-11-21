# TP2-OC2--SIMD-Threads


```
sudo sh script.sh
```

* Prueba 1
Ejecutar programa
```
./main "disney.rgb" "anomalia.rgb" "mascara640.rgb" 640 360
```
* Para convertir jpg a rgb o viceversa
```
gm convert -size 640x360 -depth 8 salida_asm.rgb 1salida_asm.jpg
gm convert -size 640x360 -depth 8 salida_c.rgb 1salida_c.jpg
```
Visualizar
```
gm display salida_c.jpg
```
* Prueba 2
Ejecutar programa

```
./main "1sticker.rgb" "2sticker.rgb" "mascara.rgb" 3840 2160
```
convertir jpg a rgb o viceversa
```
gm convert -size 3840x2160 -depth 8 salida_asm.rgb 2salida_asm.jpg
gm convert -size 3840x2160 -depth 8 salida_c.rgb 2salida_c.jpg
```
* Prueba 3
Ejecutar programa
```
./main "flores.rgb" "arcoiris.rgb" "cruz.rgb" 400 250
```
convertir jpg a rgb o viceversa
```
gm convert -size 400x250 -depth 8 salida_asm.rgb 3salida_asm.jpg
gm convert -size 400x250 -depth 8 salida_c.rgb 3salida_c.jpg
```

* Prueba 4
Ejecutar programa
```
./main "2scirocco.rgb" "scirocco.rgb" "star.rgb" 662 736
```
Convertir
```
gm convert -size 662x736 -depth 8 salida_asm.rgb 4salida_asm.jpg
gm convert -size 662x736 -depth 8 salida_c.rgb 4salida_c.jpg
```
