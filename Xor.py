def nand(a, b):
    return not(a and b)

# def XOR(a: bool, b: bool):
#     print(nand(nand(a, nand(a, b)), nand(b, nand(a,b))))

def XOR(a: bool, b: bool):
    print(False if a and b else a or b )

T = True
F = False
XOR(F, F)
XOR(T, F)
XOR(F, T)
XOR(T, T)