while(True):
    a=input('Enter a Number: ')
    # if a=='q' :
    #     break
    try:
        a=int(a)
        if a>10:
            print('You Entered a Number Greater Than 10')
        else:
            print('You Entered a number Lower than 10')

    except Exception as e :
        print("Value error!,Enter Input result is an error")
        break

print('Thanks for playing this game')
