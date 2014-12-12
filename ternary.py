import math

t = "10212110221102211011020110120201202110111012111021110221020210122102201100201201102001101011001012020121210121021200121102112100000121110122"

def ternaryToDecimal(inp):
    return int(inp, 3)

def decimalToTernary(inp):
    out = []
    n = inp
    while True:
        out.append(str(n%3))
        n = math.floor(n / 3)              
        if n == 0:
            break
    return "".join(out)[::-1]

def decodeTernary(ternary):
    chunks = [ternary[i:i+5] for i in range(0, len(ternary), 5)]
    chars = [chr(ternaryToDecimal(chunk)) for chunk in chunks]
    return "".join(chars)

def encodeTernary(string):
    b = [decimalToTernary(ord(character)).zfill(5) for character in string]
    return "".join(b)

"""
This code 'decodes' the original turnary string, which had been encoded faultily

def decodeFaultyTernary(inp):
    #Faulty ternary conversion of sorts. Works on small numbers, not big
    b = "0"+str(bin(ternaryToDecimal(inp)))[2:]

    #Hardcoded binary value to decode. Uncomment to get link
    #b = "011100000110000101110011011101000110010101100010011010010110111000101110011000110110111101101101001011110011001001100001010001010011000101000100010100010011000101100010"

    chunks = [b[i:i+8] for i in range(0, len(b), 8)]
    a = []
    for chunk in chunks:
        a.append(chr(int(chunk, 2)))
    print("".join(a))
"""
