print('Hi! Here your calc')
while True:
    c = input ("Choose first options (+, -):")
    if c in ('+', '-'):
        a = float(input('a='))
        b = float(input('b='))
        c1 = input("Choose second options(+, -):")
        if c1 in ('+', '-'):
        	z = float(input('z='))
        if c == '+':
            d = a + b
            if c1 == '+':
                print("Result = ", d+z)
            elif c == '+':
                if c1 == '-':
                    print("Result = ", d-z)
        if c == '-':
            e = a - b
            if c1 == '+':
                print("Result = ", e+z)
            elif c == '-':
                if c1 == '-':
                    print("Result = ", e-z)
    else:
        print("Wrong element!")


