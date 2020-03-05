# given string 
letter="AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCAGATCATCTATCTATAGATCAGATCAGATCAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGAGATCAGATC"
# list for the possible substring present back to back in string
a = []
# substing to find 
b = "AGATC"
i = 0
n = False
while True: 
    # checking if the given substring is present back to back or not
    if letter[i:i + len(b)]  == b and letter[i + len(b):i + len(b) * 2] == b:
        # appending the value to list if the given substing is the first in series of substing 
        if n == False:
            a.append(2)
            n = True 
         # adding the value if the substing is not first in the series
        else:
            a[-1] += 1
    else:
        n = False
        # breaking out of loop if i is out of range 
        if i > len(letter):
            break
        # adding 1 only if the back to back substing is not found 
        i += 1
        continue
    # adding the length of substing if the back to back substring is found 
    i += len(b)
a.sort()
print(a)
a = a[-1]
print(a)
