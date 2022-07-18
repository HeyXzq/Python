def fib(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    elif x >= 2:
        y = fib(x-1) + fib(x-2)
        return y
        
#def fibonacci_F(x):
   #return fib()
    
a = int(input('斐波那契数列第几项：'))
output = fib(a)
print(output)



