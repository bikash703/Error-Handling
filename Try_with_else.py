try:
    a=int(input('Enter a Number: '))
    c=1/a
    print(c)
except Exception as e:
    print(e)
else:
    print('We were Successful')