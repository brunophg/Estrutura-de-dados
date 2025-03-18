def find_max(array):
    maior = array[0]
    for i in range(1, len(array)):
        if array[i] > maior:
            maior = array[i]
    return maior

arr = [34, 25, 89, 92]

print(find_max(arr))


    