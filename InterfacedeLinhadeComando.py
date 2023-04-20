from ConversordeUnidadesdeArmazenamento import calcularConversao
print(f'Digite as unidadades a converter')

escolhaNumero = int(input())
escolhaUnidadeInicial = str(input())
escolhaUnidadeFinal = str(input())

print (f'{calcularConversao(escolhaUnidadeInicial, escolhaUnidadeFinal, escolhaNumero)}')