def mistery(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return mistery(a+a, b // 2)
    return mistery(a + a, b // 2) + a

# print(mistery(4, 3))  


def f(a, b):
    if a > b:
        return a + b
    return f(a+1, b-1) + a

print(f(1, 3))


def fx(n):
    if n == 0:
        return 0
    return 1 + fx(n // 10)

print(fx(12345))
#Retorna a quantidade de algarismos/numeros de N, no caso 5
#Ela chama fx(n // 10) recursivamente, o que vai “tirando” um dígito por vez de n, e soma 1 a cada chamada. 
# Quando n vira 0, para.


    