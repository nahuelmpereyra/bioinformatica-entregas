peptido = "ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA"
tabla = {
    'V':'GUA','A':'GCU',
    'L':'CUC','P':'CCG',
    'T':'ACG','G':'GGA',
    'K':'AAA','S':'AGU',
    'w':'UGG','C':'UGC',
    'H':'CAC','N':'AAU',
    'F':'UUU','Q':'CAA',
    'I':'AUA','Y':'UAU',
    'R':'AGA','D':'GAC',
    'M':'AUG','E':'GAA'
}

print("".join(list(map(lambda x: tabla[x], peptido))))

