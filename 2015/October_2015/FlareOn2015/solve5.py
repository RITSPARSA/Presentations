from base64 import b64decode as b64d

e = "UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=="
k = "flarebearstare"
omap = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
nmap = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'
d = ""
for i, b in enumerate(e):
    if b == '=':
        d += b
        continue
    d += omap[nmap.find(e[i])]
print d
key = ""
for i, b in enumerate(b64d(d)):
    key += chr(ord(b) - ord(k[i % len(k)]))
print key
