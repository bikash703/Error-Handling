try:
    a=int(input('Enter a Number: '))
    c=10/a
    print(c)
except Exception as e:
    print(e)
    exit()
finally:  #If program is error or not error then it ofcourse print.
    print('We are done')

print('Thanks for using this program')    #if program is error then it not print.