# Reverso de um vetor. Escreva uma função que retorna o 𝑎𝑟𝑟𝑎𝑦 informado como parâmetro
# (𝑎𝑟𝑟) em ordem inversa. OBS: O Python já possui implementado o método reverse()


class Array:
    def __init__(self, array):
        self.array = array

    def reverseArray(self, array):
        self.reversedarray = array
        return array[::-1]


# Testando a função
arr = Array([1, 2, 3])

print(arr.reverseArray(arr.array))
