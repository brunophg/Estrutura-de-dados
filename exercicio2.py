#Maior elemento do vetor. Dados um vetor de inteiros, fazer uma rotina para retornar o maior
#elemento deste 𝑎𝑟𝑟𝑎𝑦. OBS: O Python já possui implementado o método 𝑚𝑎𝑥


def find_max(array):
    maior = array[0]
    for i in range(1, len(array)):
        if array[i] > maior:
            maior = array[i]
    return maior

arr = [34, 25, 89, 92]

print(find_max(arr))