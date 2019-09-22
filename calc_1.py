print('Hi! Here your calc')
while True:
    c = input ("Choose options (+, -, *, /):")
    if c  in ('+', '-', '*', '/'):
        a = float(input('a='))
        b = float(input('b='))
        if c == '+':
            print(a+b)
        elif c == '-':
            print(a-b)
        elif c == '*':
            print(a*b)
        elif c == '/':
            if b != 0:
                print(a/b)
            else:
                print("Cannot be divided by zero")
    else:
        print("Wrong element!")


