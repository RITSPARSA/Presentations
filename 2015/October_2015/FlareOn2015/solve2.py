c = bytearray([0xa8, 0x9a, 0x90, 0xb3, 0xb6, 0xbc, 0xb4, 0xab, 0x9d, 0xae, 0xf9, 0xb8, 0x9d, 0xb8, 0xaf, 0xba, 0xa5, 0xa5, 0xba, 0x9a, 0xbc, 0xb0, 0xa7, 0xc0, 0x8a, 0xaa, 0xae, 0xaf, 0xba, 0xa4, 0xec, 0xaa, 0xae, 0xeb, 0xad, 0xaa, 0xaf])
key = ""
bx = 0
for b in c:
    key += chr((b-(1 << (bx & 3))-1) ^ 199)
    bx += b
print key
