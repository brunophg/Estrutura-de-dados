from bisect import bisect_left, bisect_right


def find_min(arr):
    def body(arr, min, max):
        if min == max:
            return arr[max]
        mid = (min + max) // 2
        left_min = body(arr, min, mid)
        right_min = body(arr, mid + 1, max)

        if left_min < right_min:
            return left_min
        else:
            return right_min
    return body(arr, 0, len(arr) - 1)


arr = [12, 3, 5, 7, 19, 11]
print(f"Menor elemento do vetor: {find_min(arr)}")


def find_sum(arr):
    def body(arr, min, max):
        if min == max:
            return arr[min]
        mid = (min + max) // 2
        left_sum = body(arr, min, mid)
        rigth_sum = body(arr, mid + 1, max)

        return left_sum + rigth_sum
    return body(arr, 0, len(arr) - 1)


arr = [12, 3, 5, 7, 19, 11]
print(f"Soma do vetor: {find_sum(arr)}")


def searchPosition(arr, target):
    def body(arr, low, high):
        if low > high:
            return -1
        if low == high:
            if arr[low] == target:
                return low
            else:
                return -1
        mid = (low + high) // 2
        left = body(arr, low, mid)
        if left != -1:
            return left
        return body(arr, mid + 1, high)

    return body(arr, 0, len(arr) - 1)


arr = [12, 3, 5, 7, 19, 11]
print(f"A posição do alvo é: {searchPosition(arr, 19)}")


def bisect_right(arr, target):
    def body(arr, low, high):
        if low >= high:
            return low
        mid = (low + high) // 2
        if arr[mid] <= target:
            return body(arr, mid + 1, high)
        else:
            return body(arr, low, mid)
    return body(arr, 0, len(arr))


arr = [12, 3, 5, 5, 7, 19, 11]
print(f"Posição mais a direita: {bisect_right(arr, 5)}")


def bisect_left(arr, target):
    def body(arr, low, high):
        if low >= high:
            return low
        mid = (low + high) // 2
        if arr[mid] < target:
            return body(arr, mid + 1, high)
        else:
            return body(arr, low, mid)
    return body(arr, 0, len(arr))


arr = [12, 3, 5, 5, 7, 19, 11]
print(f"Posição mais a esquerda: {bisect_left(arr, 5)}")
