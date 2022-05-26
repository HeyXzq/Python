def greet(name):
    print('Hello', name)
    print('How do you do?')

greet('Jack')

def add_numbers(n1, n2):
    result = n1 + n2
    return result


N1 = 1.2
N2 = 3.4
result = add_numbers(N1,N2)
print('The sum is',result)

marks = [1, 2, 4, 8]

length = len(marks)
print('length is', length)

marks_sum = sum(marks)
print('sum is', marks_sum)



from html.entities import name2codepoint


marks = [55, 64, 75, 80, 65]
length = len(marks)
marks_sum = sum(marks)
average = marks_sum / length
print('The average marks is', average)

def grade(x):
    if 100 >= x >= 80:
        print('Grade A')
    elif 60 <= x <= 80:
        print('Grade B')
    elif 50 <= x <= 60:
        print('Grade C')
    elif x <= 50:
        print('Grade F')
    else:
        print('Invalid')
    return

x = int(input('Input your marks：'))
grade(x)



def add_numbers(N1, N2):
    SUM = N1 + N2
    return SUM
def multiply_numbers(N1, N2):
    PRODUCT = N1 * N2
    return PRODUCT

N1 = float(input('input one real number:'))
N2 = float(input('input another real number:'))

SUM = add_numbers(N1, N2)
PRODUCT = multiply_numbers(N1, N2)

print('the sum of two numbers is', SUM)
print('the product of two numbers is', PRODUCT)




