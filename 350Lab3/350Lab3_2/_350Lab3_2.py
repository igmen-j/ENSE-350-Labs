def valueChecker():    
    while True:

        num1 = input("Enter first value for bisection method: ")
        num2 = input("Enter second value for bisection method: ")
        try:
            val1 = float(num1)
            val2 = float(num2)
            f_l = 230*(val1**4)+18*(val1**3)+9*(val1**2)-221*(val1)-9
            f_u = 230*(val2**4)+18*(val2**3)+9*(val2**2)-221*(val2)-9
            if (f_l*f_u) > 0:
                print ("Sign does not change. Enter another pair")
                print ("f(%f) = %f and f(%f) = %f" %(val1, f_l, val2, f_u))
            else:
                break;
        except ValueError:
            print ("At least one of the values is not a number")

    return val1, val2

def valueChecker2():    
    while True:
        num1 = input("Enter first estimate for secant method: ")
        num2 = input("Enter second estimate for secant method: ")
        try:
            val2 = float(num2)
            val1 = float(num1)
            break;
        except ValueError:
            print ("At least one of the values is not a number")

    return val1, val2

def bisection_method(x_l, x_u):
    error = 100

    x_m = (x_l+x_u)/2
    while (error > 0.01):
        f_l = 230*(x_l**4)+18*(x_l**3)+9*(x_l**2)-221*(x_l)-9
        f_u = 230*(x_u**4)+18*(x_u**3)+9*(x_u**2)-221*(x_u)-9
        x_old = x_m

        f_m = 230*(x_m**4)+18*(x_m**3)+9*(x_m**2)-221*(x_m)-9

        if ((f_l*f_m) < 0):
            x_u = x_m
        elif ((f_l*f_m) > 0):
            x_l = x_m
        else:
            return x_m
        x_m = (x_l+x_u)/2
        error = abs((x_m-x_old)/x_m)*100
    return x_m, error

def secant_method(x0, x1):
    error = 100
    while error > 0.01:
        f1 = 230*(x1**4)+18*(x1**3)+9*(x1**2)-221*(x1)-9
        f0 = 230*(x0**4)+18*(x0**3)+9*(x0**2)-221*(x0)-9

        x2 = x1-(f1*(x1-x0))/(f1-f0)
        error = abs((x2-x1)/x2)*100
        x0 = x1
        x1 = x2
    return x2, error



x_l, x_u = valueChecker()
x0, x1 = valueChecker2()

root, error = bisection_method(x_l, x_u)
print("\nBisection method:")
print("Root:", root)
print("Error: %f\n" %(error))


root, error = secant_method(x0, x1)
print("Secant method:")
print("Root:", root)
print("Error: %f\n" %(error))