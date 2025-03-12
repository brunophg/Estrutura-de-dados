def find_sum(array):
    soma = 0
    for num in array:
        soma += num # (soma = soma + num)
    return soma

arr = [25, 20, 10]
print(find_sum(arr))
