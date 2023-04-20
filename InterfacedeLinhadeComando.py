from ConversordeUnidadesdeArmazenamento import converterStringParaFloat, bitParaByte, ByteParaKByte, KByteParaMByte, MByteParaGByte, GByteParaTByte, TByteParaPByte, PbyteParaTbyte, TbyteParaGbyte, GbyteParaMbyte, MbyteParaKbyte, KbyteParabyte, byteParaBit
print('Escreva 1 para converter de bit para Byte \n Escreva 2 para converter de byte para Kbyte \n Escreva 3 para converter de Kbyte para Mbyte \n Escreva 4 para converter de Mbyte para Gbyte \n Escreva 5 para converter de Gbyte para Tbyte \n Escreva 6 para converter de Tbyte para Pbyte \n Escreva 7 para converter de Pbyte para Tbyte \n Escreva 8 para converter de Tbyte para Gbyte \n Escreva 9 para converter de Gbyte para Mbyte \n Escreva 10 para converter de Mbyte para Kbyte \n Escreva 11 para converter de Kbyte para byte \n Escreva 12 para converter de byte para bit \n')

funcEscolha = input()

if (funcEscolha == '1'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '2'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = ByteParaKByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '3'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KByteParaMByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '4'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MByteParaGByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '5'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GByteParaTByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '6'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TByteParaPByte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '7'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PbyteParaTbyte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '8'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TbyteParaGbyte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '9'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GbyteParaMbyte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '10'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MbyteParaKbyte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '11'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KbyteParabyte (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

elif (funcEscolha == '12'):
    entradaDotecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit (entradaDotecladoValorASerConvertido)
    print (valorConvertido)

else:
    print('nenhum valor encontrado')
