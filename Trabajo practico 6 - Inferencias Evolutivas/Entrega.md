# Entrega trabajo práctico Bioinformática Nº6 - Inferencias Evolutivas

Integrantes: 
- Leonardo Di Carlo
- Lucio Francioni
- Nahuel Pereyra

#### 👇 RETO I: Detalla las tácticas y/o metodologías que deberían utilizarse para darles una respuesta a los padres del niño.
    a) Dadas las secuencias de Mosca, humano y Moscahumano ¿Qué criterios se les ocurren para comparar las secuencias? ¿Qué resultados obtienen del análisis anterior?
    
A través de NCBI se obtuvo la secuencia del ser humano, de la mosca y de la “Bartmosca”:
>NP_061820.1 cytochrome c [Homo sapiens]
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE

>AFP62086.1 Cytochrome c [Mosca domestica]
MGVPAGDVEKGKKLFVQRCAQCHTVEAGGKHKVGPNLHGLFGRKTGQAAGFAYTDANKSKGITWNEDTLFEYLENPKKYIPGTKMIFAGLKKPGDRADLIAYLKSATA

>bartmosca
MGSGDAENGKKIFVQKCAQCHTYEVGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE

Luego, se compararon las 3 secuencias a través de Clustal Omega, obteniendo como resultado que la Bartmosca posee mas similitudes para con el Humano que para con la Mosca (los papás del chico se pueden quedar tranquilos…):

![alt text](https://github.com/nahuelmpereyra/bioinformatica-entregas/blob/master/resources/phylogramtp3.png)

El árbol filogenético también muestra más similitud con el Humano (si bien no sirve mucho esta comparación porque solo hay tres muestras):

![alt text](https://github.com/nahuelmpereyra/bioinformatica-entregas/blob/master/resources/phylogenetictreetp3.png)

    b) ¿Qué resultado esperaría obtener si utilizara el resto de las secuencias en el análisis? ¿Por qué?

Para el caso en el que se usaran todas las secuencias que se utilizaron en el TP anterior(Gallo, Chimpancé, Caballo, Perro, Rana, etc..), la BartMosca se alinearía más hacia la secuencia del Humano y mostraría como ancestro a la Mosca y al Humano. 

#### 👇 RETO II: Como vimos anteriormente existen algunos softwares optimizados para confeccionar alineamientos de secuencias. En particular hemos trabajado con Clustal (Larkin et al. 2007). Confecciona los alineamientos para los del punto Ia y Ib análisis.




#### 👇 RETO II: Mediante el uso del servidor de IQtree (Trifinopoulos et al. 2016), confecciona los árboles filogenéticos para los alineamientos obtenidos en el punto II.
    a) Como vemos, el servidor nos permite elegir el modelo de sustitución ¿A qué se refiere?

Los modelos de sustitución son aquellos que nos permiten calcular las distancias entre las distintas secuencias que se están comparando. Hay modelos simples y complejos, y su precisión está relacionada a su complejidad. Para elegir el modelo de sustitución óptimo para realizar una comparación hay que tener en cuenta muchas variables, como cantidad de datos a evaluar, formato de la información, etc.
Dicho esto, la herramienta IQtree nos permite elegir el modelo de sustitución si sabemos cuál es el más óptimo para el Input que estamos realizando, y una opción “auto” si no lo sabemos; de esta forma delegamos esta responsabilidad a la herramienta.

    b) ¿Qué es el Bootstrap? ¿De qué manera nos habla de la calidad de nuestro árbol? ¿Cómo influye el número de Bootstraps en el resultado?

El Bootstrap es un método de validación de árboles. Básicamente lo que realiza este método es crear réplicas de distintos alineamientos a partir de un alineamiento original, eliminando cierto número de posiciones al azar en cada réplica. El número final de posiciones se mantiene constante, añadiendo duplicaciones de los sitios que han permanecido. Luego, para cada réplica se aplica el método de reconstrucción filogenética y se genera un árbol. El paso final es evaluar para cada nodo el porcentaje de árboles en los que aparece: los nodos con un alto valor de Bootstrap tienen una probabilidad alta de ser correctos (se estiman en >= 90%), mientras los que tienen un bajo valor de Bootstrap podrían haberse generado por azar (se estiman en <= 50%).
Cuantas más réplicas se generen, más probabilidad tendremos de quedarnos con los nodos correctos. Ésta posibilidad permite IQtree, ya que permite seleccionar la cantidad de alineamientos de Bootstraps.

    c) Interpreten los resultados obtenidos, mediante la visualización de los árboles con la herramienta FigTree . ¿Es necesario realizar algún paso extra, previo a la interpretación del árbol? ¿Por qué?

Antes de interpretar un árbol debiera realizarse una validación previa (como es el caso de Bootstrap o algún otro método). De esta manera, nos quedaremos con los Clados que realmente comparten ancestros. 
