# s = int(input("Введите список чисел"))
# n = int(input("Введите число среза"))
spis = []

while True:
    s = input("Введите число")
    if s != 'y' :
        spis.append(s)
    else:
        break

n = int(input("Введите число среза"))

c = spis[n:] + spis[:n]

print(c)
