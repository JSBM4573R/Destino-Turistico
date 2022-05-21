# Destino-Turistico
Reto 3 Python - Desarrollo de un programa que valida la disponibilidad de un destino turistico segun los criterios ingresados.

Reto:

La entrada estará conformada por N + 1 líneas:
La primera línea recibirá un número N que equivale a la cantidad de destinos que se analizarán. 
Cada registro representa una posibilidad de destino para las vacaciones.
Cada una de las siguientes N líneas estará formada por 5 números separados por espacios 
que representan las diferentes características de una casa. 
Por ejemplo,la fila 5 4 28 6 3000 representa un destino con 5 camas dobles, 4 piscinas, 
un tiempo de viaje de 28 minutos en avión, 6 tipos de comida y un valor de 3000 dólares.

El programa imprimirá el precio de cada uno de los destinos que cumplen con los 
criterios de Andrés.
Si no existe ningún destino que cumpla los criterios de Andrés, el programa 
imprimirá 'NO DISPONIBLE'.

Criterios:
Que tenga 3 o más camas dobles.
Que tenga 2 o más Piscinas.
Que el tiempo de viaje en avión no sea superior a 35 minutos.
Que tenga 4 o más tipos de comida en el plan todo incluido.

Casos de prueba:

3
<br>
2 1 50 3 3100
<br>
2 2 45 2 2850
<br>
3 3 30 4 3250
<br>


4
<br>
2 2 50 4 2900
<br>
3 2 30 4 3050
<br>
2 2 50 4 3350
<br>
2 2 55 3 3100
<br>


6
<br>
3 3 40 2 3450
<br>
1 1 25 4 2800
<br>
2 3 25 2 3000
<br>
3 1 25 2 2550
<br>
1 1 25 3 2500
<br>
3 3 40 3 3400
