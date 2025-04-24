def find_max(arr):
     def body(arr,min,max):
              if min == max: # base case
                  return arr[min]
              mid = (min + max) // 2
              left_max = body(arr, min, mid) # division
              right_max = body(arr, mid + 1, max)
              if left_max > right_max:
                    return left_max
              else:
                    return right_max
                

            #   return left_max if left_max >  right_max else right_max # combination
            
     return body(arr,0,len(arr)-1)

# arr = [12, 3, 5, 7, 19, 11]
# print(find_max(arr))


def searchPosition(arr,target):
      def body(arr, min, max):
            if min max:
                  return arr[min]
            mid = (min + max) // 2
            left = body(arr, min, mid)
            right = body(arr, mid + 1, max)

            if left == target:
                  return i
            else:
                  return i
      return body(arr, 0, len(arr) - 1)

arr = [12, 3, 5, 7, 19, 11]
print(searchPosition(arr, 5))
