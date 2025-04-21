

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

# arr = [12, 3, 5, 7, 19, 11]
# print(find_min(arr))

def find_sum(arr):
    def body(arr, min, max):
        if min == max:
            return arr[min]
        mid = (min + max) // 2
        left_sum = body(arr, min, mid)
        rigth_sum = body (arr, mid + 1, max)

        return left_sum + rigth_sum
    return body(arr, 0, len(arr) - 1)

arr = [12, 3, 5, 7, 19, 11]
print(find_sum(arr))


