# Entrega trabajo práctico Bioinformática Nº7

Integrantes: 
- Leonardo Di Carlo
- Lucio Francioni
- Nahuel Pereyra

---
#### RETO I: ¿Podés descubrir y anotar el orden en que se ha ejecutado cada operación?
Orden de ejecucion:
	- Suma entre parentesis
	- Multiplicacion
	- Division
	
#### RETO II: Crea una variable llamada ​ doble, que sea el doble de la suma entre a y b.

Respuesta -> doble = (a + b) * 2

#### RETO III: Digamos que el ADN no es más que un mensaje en clave, que debe ser descifrado o interpretado para la síntesis de proteínas. El mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G y C. Dentro de la célula, el mensaje es transportado por otra molécula, el ARN, muy similar al ADN pero con U en vez de T. En este mensaje, cada triplete o grupo de tres letras del ARN se denomina codón, y cada aminoácido de las proteínas está codificado por uno o varios codones. Así por ejemplo el codón ‘AUG’ codifica para el aminoácido Metionina , el codón ‘AAA’ para Lisina, el codón ‘CUA’ para Leucina, etc. ¿Podrías escribir una cadena de ARN que codifica para el péptido (una cadena corta de aminoácidos) ‘Met-Lis-Lis-Lis-Leu-Leu-Met’ combinando las variables met = ‘AUG’ , lis = ‘AAA’ y leu = ‘CUA’ utilizando operadores matemáticos?

Respuesta -> peptido = met + lis + lis + lis + leu + leu + met (AUGAAAAAAAAACUACUAAUG)

#### RETO IV: ¿Cadenas? ¿letras? Si hablamos de cadenas y letras en Biología, lo primero que se nos viene a la cabeza son las macromoléculas. Como bien sabemos, el ADN es un mensaje en clave que guía la síntesis de proteínas. Este mensaje está escrito por una secuencia determinada de 4 nucleótidos distintos representados por las letras A, T, G y C. El contenido de C y G (es decir el porcentaje de CG) presente en el ADN de un organismo es una característica distintiva: por ejemplo las Actinobacterias tienen un contenido característicamente más alto de CG que otros organismos. Ahora, contar la cantidad de C y G en una cadena de ADN larguísima a mano puede ser un verdadero tedio ¿Podrías crear un programa que calcule el porcentaje de C y G de una cadena dada de ADN?
```python
cadenaDeADN = ""
total = len(cadenaDeADN)
porcentaje_c = (cadenaDeADN.count("C") * 100) / total
porcentaje_g = (cadenaDeADN.count("G") * 100) / total
```
#### RETO V: La Asombrosa Maravillosa es nuestra valiente superheroína. Sus poderes son producto de mutaciones en un gen muy común, cuya secuencia en la mayoría de las personas es 'ATGGAACTTGCAATCGAAGTTGGC'. A diferencia de nosotros, el gen mutado de la Asombrosa Maravillosa incluye la secuencia 'GTTTGTGGTTG' en su interior. La Asombrosa Maravillosa adquirió sus poderes al beber Jugo Vencido. El primer sorbo de esta poción prohibida causa el cambio de todas las citosinas (C) por timinas (T). El siguiente sorbo cambia todas las adeninas (A) por guaninas (G). El tercer sorbo cambia las citosinas (C) por adeninas (A). El cuarto sorbo... puede ser mortal. ¿Podés escribir un programa que nos diga cuántos sorbos de Jugo Vencido debe beber un portador del gen normal, para ganar los poderes de la Asombrosa Maravillosa?



#### RETO VI:

#### RETO VII: Ya que encontramos el espécimen de rana con pelo en marte, nos gustaría contrastar sus características con las ranas terrestres. Sabiendo que el gen de la proteína diminuta es ‘ATGGAAGTTGGAATCCAAGTTGGA’ y el gen de una proteína similar de rana terrestre es ‘ATGGAAGTTAATGGAAGTTGGAGGAGA’ ¿podés crear un programa que compare la longitud de ambos genes y según cuál sea más grande nos imprima un mensaje informándonos el resultado?
```python
ranaEnMarte = "ATGGAAGTTGGAATCCAAGTTGGA"
ranaTerrestre = "ATGGAAGTTAATGGAAGTTGGAGGAGA"

if len(ranaEnMarte) > len(ranaTerrestre):
  print("Rana de marte")
else:
  print("Rana terrestre")
```
#### RETO VIII: Si nos ponemos un poco más estrictos, y siguiendo con el tema de los clones de bacterias, el programa que creamos antes tiene algunas fallas ‘numéricas’: en cada vuelta de división celular binaria se generarán dos clones, no uno. ¿Podrías escribir un programa que imprima ‘¡Somos 2 clones nuevos!’ en cada una de 20 vueltas?
```python
for i in range(0,20):
  print('¡Somos 2 clones nuevos!')
```

#### RETO IX: Si ahora queremos hacer nuestro programa un poco más estricto, por cada vuelta deberíamos sumar el total de células que tenemos e imprimir ese número en el mensaje. Entonces, por ejemplo, como en la primer vuelta tenemos dos células, imprimiríamos como mensaje ‘¡Somos 2 clones!’ , pero en la segunda vuelta serán en total 4 células y el mensaje a imprimir debería ser ‘¡Somos 4 clones!’. ¿Podrías escribir esta modificación del programa?
```python
for i in range(0,20):
  print(f'¡Somos {i * 2} clones nuevos!')
```



