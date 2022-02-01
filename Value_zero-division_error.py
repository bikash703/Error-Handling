a=input('Enter a Number: ')
try:
    a=int(a)
    c=1/a
    print(c)
except ValueError as e:
    print(f'Oops!,Value Error !!!Please entered a valid value.!, You Entered {e}')
except ZeroDivisionError as e:
    print('Zero Division Error!!,The value is not divisible by zero')

print('Thank you for trying this')