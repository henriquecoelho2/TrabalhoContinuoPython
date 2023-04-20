ListadeUnidades=['bit', 'byte', 'Kbyte', 'Mbyte', 'Gbyte', 'Tbyte', 'Pbyte']
Numero=80000
UnidadeInicial= 'bit'
UnidadeFinal= 'Mbyte'

def calcularConversao (UnidadeInicial, UnidadeFinal, Numero):
    posicaoinicial=0
    posicaofinal=0
    variacaoDasUnidades=0
    if UnidadeInicial == 'bit':
        Numero /= 8
        UnidadeInicial = 'byte'
    if UnidadeFinal == 'bit':
        Numero /= 8
        UnidadeFinal = 'byte'
    for i in ListadeUnidades:
        if i == UnidadeInicial:
            posicaoinicial = ListadeUnidades.index(i)
    for i in ListadeUnidades:
        if i == UnidadeFinal:
            posicaofinal = ListadeUnidades.index(i)
    variacaoDasUnidades= posicaofinal-posicaoinicial
    conversor= 1024**variacaoDasUnidades
    if variacaoDasUnidades > 0:
        resp= Numero * conversor
    if variacaoDasUnidades < 0:
        resp= Numero / conversor
    return resp