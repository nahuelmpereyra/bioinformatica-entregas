#Denominada caja TATA consistente en una secuencia de nucleotidos 'TATAAA'
#Por lo que tomamos TAT = V y AAA = Q

peptido = "ATVEKGGKHKTGPNEKGKKIFVQKCSQCHYKTVLHGLFGRKTGQA"

tata = peptido.find("VQ")

result = ""

#Se suma dos para avanzar dos posiciones para empezar a contar desde ahi
for i in range(tata+2, len(peptido)):
    result = result + peptido[i]

print(result)

