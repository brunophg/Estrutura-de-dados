
def recursiveMDC(x,y):
     if y == 0:
          return x
     else:
          return recursiveMDC(y, x % y)
     
print(recursiveMDC(48, 18))

def recursiveproduto(x, y):
     if x == 0 or y == 0:
          return 0
     else:
          return x + recursiveproduto(x, y - 1)

print(recursiveproduto(4, 6))

def recursiveMax(x):
     pass
     
     