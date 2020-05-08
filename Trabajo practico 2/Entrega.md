# Entrega trabajo práctico Bioinformática Nº2

Integrantes: 
- Leonardo Di Carlo
- Lucio Francioni
- Nahuel Pereyra

---
#### ¿Por qué una célula querría destruir sus propias proteínas?

#### ¿Qué información nos provee esta página?

*Nos muestra un Base de Datos que nuclea informacion sobre las estructuras de las proteinas que han sido cristalizadas (estructura para que se quede quieta) a lo largo de varios experimentos y ademas toda la informacion del experimento en cual se determino esa estructura.*

#### ¿Cómo se determinó la estructura de esta proteína?

*Esta estrucutra de la proteina se determino cristalizando las proteinas debido a que las proteinas estan en solucion ya sea que esten en una celula o en un tubo de ensayo, pero en general se tienen en solucion para poder saber como es su estructura terciaria hay que dejarlas estaticas para poder sacarle una foto debido que en solucion las moleculas tienen movimientos.*

#### A la izquierda vemos una representación de la estructura de ubiquitina. ¿Qué significan las cintas, las flechas y las regiones angostas?

* Cintas → 

  Flechas → Estructura secundaria representada, se reprensanta en una flecha ya que es la hoja beta plegada.
  
  Regiones Angostas → *

#### ¿Representa esa imagen a la realidad del sistema biológico?

*No debido a que esta en constante movimiento, ya que esta en un medio acuoso. Puede ser que en algun momento de todo ese movimiento adopte esa conformacion pero las proteinas en su estado nativo tienen multiples conformacion posibles.*

#### La estructura 1UBQ fue “refinada a una resolución de 1.8 Angstroms”.Éste es el error asociado al experimento: mientras mayor es la resolución, menor es la certeza al determinar la posición de cada átomo. ¿Cuál es la utilidad y los condicionamientos de usar un modelo científico que sabemos inexacto?

*La resolucion nos dice la posibilidad para determinar o distinguir entre dos puntos que esten cercanos, es decir, si yo tengo una resolucion mas chica(puntos mas cercas) se puede diferenciar pero si la resolucion es mas grande solo se va poder diferenciar dos cosas que esten a esa distancia.
Este metodo no es exacto pero es el unico que da la posibilidad de tener una idea de como es una proteina en cuestion.*

#### ¿Qué diferencias y similitudes notamos respecto de la representación inicial?

#### En el menú de la izquierda hay opciones de distintos tipos de representación y formas de colorear la estructura tridimensional. ¿Para qué podría ser útil visualizar lo mismo de distintas maneras?

#### ¿Qué información esperaría encontrar como resultado un experimento destinado a determinar la estructura terciaria de una molécula biológica?

*Se esperaria encontrar como resultado datos que se mostrarian en representacion matematica en un eje de coordenadas de lo que se observo de la cristalizacion de un proteina.*

#### ¿En qué consiste un archivo PDB?

*Nos informa toda la informacion del experimento en cual se determino esa estructura esto no nos da el inicia que si utilizamos esta informacion se va a replicar el experimento ya que no se cargan los datos en su totalidad*

#### Desplacémonos por el archivo hasta encontrar las líneas que comienzan con la palabra ATOM. ¿Qué tipo de información brinda esta sección?

* ATOM → posicion(coordenadas) de cada uno de los atomos que conforman cada uno de los aminoacidos que conforman la proteinas.
Seccion ATOM:

Columna 1 → ATOM

Columna 2 → Numero de atomo que estan

Columna 3 → Atomo que estan mirando mas unos modificados donde va estar ese atomo.

Columna 4 → de que aminoacido es

Columna 5 → cadenas ya que la proteinas tienen mas de una cadena

Columna 6 → en que residuo estan parados (que aminoacidos estan viendo)

Columna 7,8,9 → representan los puntos en el eje x, y, z, valores de coordenas que tienen ese atomo

Columna 10 → valor de ocupancia, en todos los cristales que se obtuvieron del aminoacido el primer atomo que estuvo en una posicion.

Columna 12 →  Atomo que estan mirando

TITLE → es el titulo del documento
REMARK → procedimiento experimental en que se cristalizo esa proteina.
SEQRES → secuencia de residuo, es decir la estructura primaria.
*

#### ¿Podríamos extraer de este archivo información sobre la estructura primaria de la proteína en cuestión? ¿Cómo se presenta dicha información y qué significa la representación? Desde el punto de vista computacional:¿de qué tipo de dato se trata esta información?

#### ¿Considera que el formato PDB es útil para presentar los resultados del experimento?

*Se puede decir que es util ya que en la actualidad es el que se utiliza mas esto no implica que puede ser el mejor.*

#### Observamos que la información respeta cierta estructura interna. ¿Cuáles son los beneficios y las limitaciones de imponer una estructura para comunicar los resultados de un experimento?

#### Hemos visto que las proteínas tienen estructura tridimensional y hemos podido observar algunas características de las mismas. ¿Será igual con los ácidos nucléicos?

#### Rosalind Franklin es una científica muy relevante, que tuvo menos reconocimiento del merecido. Contanos sobre los procedimientos que puso a punto Rosalind.

*Rosalind Franklin fue una científica Inglesa que realizó grandes contribuciones a la ciencia en la época de la Segunda Guerra Mundial. Mediante el estudio bajo la técnica de difracción de Rayos X pudo describir la estructura del ADN, descubriendo así la forma de "doble hélice" de las moléculas.
Hay quienes sostienen incluso que ella habia llegado a la conclusion de la estructura helicoidal unos meses antes de la publicacion realizada por Watson y Crick. Pero que por no haber realizado ninguna publicación aún con los resultados de sus investigaciones e imágenes tomadas, que resultaron fundamentales para sostener la propuesta, no logró tener el reconocimiento merecido.*




