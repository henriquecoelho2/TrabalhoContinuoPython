Valorembit= 80
ValoremByte= 1024
ValoremKByte= 1024
ValoremMByte= 1024
ValoremGByte= 1024
ValoremTByte= 1024
ValotemPByte= 1024

def bitParaByte(Valorembit):
    print('Valor convertido de bit para byte')
    bytesCalculado = Valorembit / 8
    return bytesCalculado

def ByteParaKByte(ValoremByte):
    print('Valor convertido de byte para Kbyte')
    KbytesCalculado = ValoremByte / 1024
    return KbytesCalculado

def KByteParaMByte(ValoremKByte):
    print('Valor convertido de Kbyte para Mbyte')
    MbytesCalculado = ValoremKByte / 1024
    return MbytesCalculado

def MByteParaGByte(ValoremMByte):
    print('Valor convertido de Mbyte para Gbyte')
    GbytesCalculado = ValoremMByte / 1024
    return GbytesCalculado

def GByteParaTByte(ValoremGByte):
    print('Valor convertido de Gbyte para Tbyte')
    TbytesCalculado = ValoremGByte / 1024
    return TbytesCalculado

def TByteParaPByte(ValoremTByte):
    print('Valor convertido de Tbyte para Pbyte')
    PbytesCalculado = ValoremTByte / 1024
    return PbytesCalculado

# ////////////////////////////////////////////////////////////////////////////////////////
def PbyteParaTbyte(ValoremPbyte):
    print('Valor convertido de Pbyte para Tbyte')
    TbytesCalculado = ValoremPbyte * 1024
    return TbytesCalculado

def TbyteParaGbyte(ValoremTbyte):
    print('Valor convertido de Tbyte para Gbyte')
    GbytesCalculado = ValoremTbyte * 1024
    return GbytesCalculado

def GbyteParaMbyte(ValoremGbyte):
    print('Valor convertido de Gbyte para Mbyte')
    MbytesCalculado = ValoremGbyte * 1024
    return MbytesCalculado

def MbyteParaKbyte(ValoremMbyte):
    print('Valor convertido de Mbyte para Kbyte')
    KbytesCalculado = ValoremMbyte * 1024
    return KbytesCalculado

def KbyteParabyte(ValoremKbyte):
    print('Valor convertido de Kbyte para byte')
    bytesCalculado = ValoremKbyte * 1024
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado


