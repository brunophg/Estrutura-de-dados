def find_min(array):
    minimo = array[0]
    for num in array:
        if num < minimo:
            minimo = num
        return minimo
    
array = [10, 20, 30, 40, 50, 60, 70, 80]
print(find_min(array))