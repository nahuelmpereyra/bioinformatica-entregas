"""Listado de Aminoácidos existentes en los seres vivos:

HIS - H - Histidine - Histidina
ARG - R - Arginine - Arginina
lYS - K - Lysine - Lisina
ILE - I - Isoleucine - Isoleucina
PHE - F - Phenylalanine - Felinamina
LEU - l - Leucine - Leucina
TRP - W - Tryptophan - Triptofano
ALA - A - Alanine - Alanina
MET - M - Methionine - Metionina
PRO - P - Proline - Prolina
CYS - C - Cysteine - Cisteina
ASN - N - Asparagine - Asparagina
VAL - V - Valine - Valina
GLY - G - Glycine - Glicina
SER - S - Serine - Serina
GLN - Q - Glutamine - Glutamina
TYR - Y - Tyrosine - Tirosina
ASP - D - Aspartic Acid - Ácido Aspartico
GLU - E - Glutamic Acid - Ácido Glutaminico
THR - T - Threonine - Treonina

Los 3 tipos de Estructuras Secundarias son:

H - Hélice
B - Hoja Beta plegada
L - Bucle o Loop
"""
# Lo primero es asociar cada letra de los aminoácidos al grupo más probable (tabla de tendencias):
# Por lo tanto se crean los siguientes 3 conjuntos de letras
# Helice ó H = ACLMEQHK
# Hoja Beta ó B = VIFYWTR
# Loop ó L = GSDNP

print("Ingrese la secuencia proteica a ser predecida:")
secuenciaProteica = input()
prediccionEstructural = ''
for i in secuenciaProteica:
    if (i =='G') or (i =='S') or (i =='D') or (i =='N') or (i =='P'):
        prediccionEstructural += 'L'

print(prediccionEstructural)