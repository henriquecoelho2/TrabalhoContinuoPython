ListadeUnidades=['bit', 'byte', 'Kbyte', 'Mbyte', 'Gbyte', 'Tbyte', 'Pbyte']
Numero=10
UnidadeInicial= 'byte'
UnidadeFinal= 'Mbyte'

def calcularConversao ():
    posicaoinicial=0
    for i in ListadeUnidades:
        if i == UnidadeInicial:
            posicaoinicial = ListadeUnidades.index(i)
    return posicaoinicial

print (calcularConversao())