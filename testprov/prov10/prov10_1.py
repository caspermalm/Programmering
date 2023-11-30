def maximum(x, y):
    if x > y:
        return x
    else:
        return y


print(maximum(3, 7))
# Funktionen maximum returnerar det största talet.
# utskrift: 7
print(maximum(11, 3))
# utskrift: 11


def addera(x, y):
    return x + y

print(addera(3, 5))
# Funktionen addera lägger ihop talen och returnerar svaret.
# utskrift 8
print(addera(10, 2))
# utskrift 12


def hej(x):
    return "hej " + x


print(hej("Ada"))
# utskrift: hej Ada
print(hej("Babbage"))
# utskrift: hej Babbage