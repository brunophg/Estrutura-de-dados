def iterativeFactorial(n):
     fat = 1
     for i in range(n,0,-1):
          fat = fat*i
     return fat

def factorial(n):
      return n*factorial(n-1) if n > 0 else 1

def factorial1(n):
     if n == 0: # base case (non-recursive)
          return 1
     elif  n>0:  # recursive case
          return n*factorial1(n-1)
     raise TypeError('inappropriate argument type')

def tailFactorial(n):
     def accumulatedFactorial(n,f):
          if ( n == 0): # base case
               return f
          elif ( n == 1): # base case
               return f          
          else: # recursive case
               return accumulatedFactorial(n-1, n*f)
     return accumulatedFactorial(n, 1)
   
def rec(n):
     if n < 4:
          return n
     else:
          return rec(n-1) + rec(n-2) + rec(n-3)
     
def perfect_square(n):
     if (n == 0):  # base case (non-recursive)
          return 0
     return perfect_square(n-1) +2*n -1    # recursive case
     
def fibonacci(n):
     if( n == 0 ):
          return 0   # base case
     elif( n == 1 ):
          return 1   # base case
     else: # recursive case
          return fibonacci(n-1) + fibonacci(n-2)

def fibonacci1(n,first,second):
     if( n == 0 ):
          return first   # base case
     elif( n == 1 ):
          return second   # base case
     else: # recursive case
          return fibonacci1(n-1,first,second) + fibonacci1(n-2,first,second)


def tailFibonacci(n,current=1,next=1):
     if( n == 0):
          return current
     elif( n == 1):
          return next
     return tailFibonacci(n-1,next,current+next)
     
def even(n):  # par
     if n == 0:
          return True
     elif n > 0:
          return odd(n-1)
     return even(-n)

def odd(n):  # impar
     if n == 0:
          return False
     elif n > 0:
          return even(n-1)
     return odd(-n)

"""-----------------------------------------------------"""

def MMC(x,y):
     return (x*y)/MDC(x,y)

def MDC(x,y):
     pass

def produto(a,b):
     pass

def iterativeMax(a):
     max = a[0]
     for i in range(1,len(a)):
          if max < a[i]:
               max=a[i]
     return max

def max(a):
     pass

def tailMax(a):
     pass

def iterativeMin(a):
     min = a[0]
     for i in range(1,len(a)):
          if min > a[i]:
               min=a[i]
     return min

def min(a):
     pass

def tailMax(a):
     pass

def iterativeSum(a):
     sum = a[0]
     for i in range(1,len(a)):
          sum+=a[i]
     return sum

def sum(a):   
     pass

def tailSum(a):
     pass

def power(b,n):
     pass

def  succesor (x):
     return ( x + 1 )

def  antecesor (x):
     return ( x + 1 )
	
def soma(a,b):
     pass

def zeroes(n):
     pass

def zeroesEasy(n):
     return str(n).count('0')

def digitSum(n):
     pass

def naturalSum(n):
     pass

def  IntegerToBinary(n):
     pass

if __name__ == '__main__':
      # fatorial
      n = 5
      print('iterativeFactorial ' + str(n) + ' : ',iterativeFactorial(n))
      print('recFactorial ' + str(n) + ' : ',factorial(n))
      print('tailFactorial ' + str(n) + ' : ',tailFactorial(n))
      # fibonacci
      res=''
      for i in range(n):
           res+=str(fibonacci(i))+', '
      print('fibonacci ' + str(n) + ' : ',res[:-2])
      res=''
      for i in range(0,n):
           k=fibonacci1(i,0,1)
           res+=str(k)+', '
      print('fibonacci ' + str(n) + ' : ',res[:-2])
      res=''
      current=0;next=1
      for i in range(0,n):
           k=tailFibonacci(i,current,next)
           res+=str(k)+', '
      print('fibonacci ' + str(n) + ' : ',res[:-2])
      # even odd
      print(str(n),' id even ',even(n))
      print(str(n),' id odd ',odd(n))
      # MMC MDC
      print('MMC(6,12) ',MMC(6,12))
      print('MDC(6,12) ',MDC(6,12))
      # produto
      print('produto(6,12) ',produto(6,12))
     
     

