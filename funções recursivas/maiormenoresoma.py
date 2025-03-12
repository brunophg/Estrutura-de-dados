#Maior e menor elemento de um vetor e soma dos seus elementos. Imagine a como um vetor de
#inteiros. Apresente algoritmos recursivos para calcular:

# - O maior elemento do vetor.

# - O menor elemento do vetor.

# - A soma dos elementos do vetor.

# from math import *

# def max(vetor):
#     n = len(vetor)
#     if n == 1:
#         return vetor[0]



# vetor = [10, 20, 30]
# print(max(vetor))


def recursivesum(vetor, i, soma):
    if i < 0:
        return soma
    return recursivesum(vetor, i - 1, soma + vetor[i])
    
vetor = [10, 20, 30]

print(f"Soma dos elementos: {recursivesum(vetor, len(vetor) - 1, 0)}")