#Soma dos elementos do vetor. Dados um 𝑎𝑟𝑟𝑎𝑦 de inteiros, fazer uma rotina para retornar
#a soma de todos os elementos desse 𝑎𝑟𝑟𝑎𝑦. OBS:O Python já possui implementado o método 𝑠𝑢𝑚.

class vetor:
    def __init__(self, array):
        self.array = array

    def somar_array(self):
        soma = 0
        for num in self.array:
            soma += num
        
        return soma
    

arr = [1, 2, 3, 4, 5]   

v = vetor(arr)

print(v.somar_array())