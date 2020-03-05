letter="AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCAGATCATCTATCTATAGATCAGATCAGATCAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGAGATCAGATC"
a = []
b = "AGATC"
i = 0
n = False
while True: 
    if letter[i:i + len(b)]  == b and letter[i + len(b):i + len(b) * 2] == b:
        if n == False:
            a.append(2)
            n = True 
        else:
            a[-1] += 1
    else:
        n = False
        if i > len(letter):
            break
        i += 1
        continue
    i += len(b)
a.sort()
print(a)
a = a[-1]
print(a)