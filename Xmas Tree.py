def tree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ',end=' ')
        for k in range(2*i+1):
            print('@',end=' ')
        print()

def pole(n):
    for i in range(n-4):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')

height=int(input('Enter height: '))
tree(height)
pole(height)
