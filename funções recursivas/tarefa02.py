
def recursiveMDC(x,y):
     if y == 0:
          return x
     else:
          return recursiveMDC(y, x % y)
     
print(f"o MDC recursivo é: {recursiveMDC(48, 18)}");

def recursiveProduto(x, y):
     if x == 0 or y == 0:
          return 0
     else:
          return x + recursiveProduto(x, y - 1)

print(f"O produto recursivo é: {recursiveProduto(4, 6)}");

def recursiveMax(arr, indice, valor_max):
    if valor_max == 0:
        valor_max = arr[0]
    
    if indice == len(arr):
        return valor_max
    
    maior_atual = arr[indice]
    valor_max = max(maior_atual, valor_max)

    return recursiveMax(arr, indice + 1, valor_max)


vetor =  [10, 20, 60]
print(f"O valor maximo do array é: {recursiveMax(vetor, 0, 0)}")
      
def recursiveMin(arr, indice, valor_min):
    if valor_min == 0:
        valor_min = arr[0]
    
    if indice == len(arr):
        return valor_min

    valor_atual = arr[indice]
    valor_min = min(valor_atual, valor_min)

    return recursiveMin(arr, indice + 1, valor_min)


vetor = [10, 20, 60, -5]
print(f"O valor mínimo do array é: {recursiveMin(vetor, 0, 0)}")

def recursiveSum(arr, indice, soma):
    if indice == len(arr):
        return soma

    soma += arr[indice]
    return recursiveSum(arr, indice + 1, soma)


vetor = [10, 20, 60]
print(f"A soma dos elementos do array é: {recursiveSum(vetor, 0, 0)}")


def somaRecursiva(a, b):
    def sucessor(a):
        return a + 1
    
    def antecessor(b):
        return b - 1
    
    if b == 0:
        return a
    return somaRecursiva(sucessor(a), antecessor(b))

a = 2
b = 3
print(f"A soma recursiva é: {somaRecursiva(a, b)}");


def recursivenumerodezeros(n):
    if n == 0:
        return 1
    if n < 10:
        return 0
    else:
        if n % 10 == 0:
            return 1 + recursivenumerodezeros(n // 10)
        else:
            return recursivenumerodezeros(n // 10)    

print(f"O numero de zeros de n é: {recursivenumerodezeros(0)}");


def somaAlgarismos(n):
    if n < 10:
        return n
    else:
        return n % 10 + somaAlgarismos(n // 10)
    
print(f"A soma dos algarismos: { somaAlgarismos(1234)}")