sigma = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def sigex(a):
    if isinstance(a, str):
        return sigma.index(a.lower())
    if isinstance(a, int):
        return sigma[a]


def ek(key, plaintext):
    y = ""
    for i in range(len(plaintext)):
        y += sigex((sigex(plaintext[i])+key) % 26)
    return y

p = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
k = 10
# op = ek(k,p)
# print(op)


def exhaust(plaintext):
    for i in range(len(sigma)):
        print("k = "+str(i))
        print(ek(i, plaintext)+"\n")

exhaust(p)
