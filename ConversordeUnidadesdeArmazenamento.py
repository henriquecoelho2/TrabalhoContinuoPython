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
    print('Valor convertido de byte para Mbyte')
    MbytesCalculado = ValoremKByte / 1024
    return MbytesCalculado
