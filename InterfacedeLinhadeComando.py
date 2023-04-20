from ConversordeUnidadesdeArmazenamento import calcularConversao
print(f'Digite o número a converter')
escolhaNumero = int(input())
print(f'Escolha a unidade do número')
escolhaUnidadeInicial = str(input())
print(f'Escolha a unidade desejada')
escolhaUnidadeFinal = str(input())

print (f'o valor obtido é: {str(calcularConversao(escolhaUnidadeInicial, escolhaUnidadeFinal, escolhaNumero))+escolhaUnidadeFinal}')