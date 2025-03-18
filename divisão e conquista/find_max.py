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

arr = [12, 3, 5, 7, 19, 2, 11]
print(find_max(arr))