
print('Enter the integer')
print('Enter 1 for True and 0 for False:')
n=int(input())
b=bool(int(input()))
boolean=bool(b)

if boolean == True:
     for i in range(n):
        print("*"*(i+1))
else:
     for i in range(n):
            print("*"*(n-i))








