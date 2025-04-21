#scan

def scan(array, key):
    for i in range(0, len(array)):
        print(i)
        if array[i] == key:
            return i
        if array[i] > key:
            return "NOT FOUND"
    return "NOT FOUND"
    
arr = [10,25,30,45,50,55,60,90,100,110,115,120]

print(scan(arr, 50))

def f(n):
    pass