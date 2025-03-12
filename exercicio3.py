#Menor elemento do vetor. Dados um 𝑎𝑟𝑟𝑎𝑦 de inteiros, fazer uma rotina para retornar o
#menor elemento desse 𝑎𝑟𝑟𝑎𝑦. OBS:O Python já possui implementado o método 𝑚𝑖𝑛.


class Array:
    def __init__(self, array):
        self.array = array

    def achar_minimo(self):
        minimo = self.array[0]
        for i in range(len(self.array)):
            if self.array[i] < minimo:
                minimo = self.array[i]

        return minimo
    

arr = Array([20, 10, 30, 5, 40])

print(arr.achar_minimo()) 