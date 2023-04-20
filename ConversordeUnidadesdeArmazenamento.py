ListadeUnidades=['bit', 'byte', 'Kbyte', 'Mbyte', 'Gbyte', 'Tbyte', 'Pbyte']
Numero=10
UnidadeInicial= 'Mbyte'
UnidadeFinal= 'byte'

def calcularConversao (UnidadeInicial, UnidadeFinal, Numero):
    posicaoinicial=0
    posicaofinal=0
    variacaoDasUnidades=0
    for i in ListadeUnidades:
        if i == UnidadeInicial:
            posicaoinicial = ListadeUnidades.index(i)
    for i in ListadeUnidades:
        if i == UnidadeFinal:
            posicaofinal = ListadeUnidades.index(i)
    variacaoDasUnidades= posicaofinal-posicaoinicial
    conversor= 1024**variacaoDasUnidades
    resp= Numero / conversor
    return resp