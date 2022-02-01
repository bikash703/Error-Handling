def Increment(num):
    try:
        num=int(num)
        return num+1
    except:
        raise ValueError('Please Enter a valid Number')
n=input('enter a no.: ')
a=Increment(n)
print(a)