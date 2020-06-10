
# Justin Igmen
# 200364880
# 350 Lab 3a

import math

#F = (qQx) / (4pie(x^2+a^2)^(5/2)
def f_x(e, q, Q, a, x):
    num = q*Q*x
    denum = 4*math.pi*e*((x**2+a**2)**(3/2))
    return num/denum - 1

#F' = (qQ(a^2-2x^2)) / (4pie(x^2+a^2)^(5/2)
def f_prime(e, q, Q, a, x):
    num = q*Q*(a**2-2*x**2)
    denum = 4*math.pi*e*((x**2+a**2)**(5/2))
    return num/denum

def error_check(fx_value, fprime_value, x):
    new_x = x - fx_value/fprime_value

    error = abs((new_x - x)/new_x) * 100
    return new_x, error

e = 8.85e-12
q = 2e-5
Q = 2e-5
x = 0.1 #initial value
a = 0.9
error = 100

while(error > 0.01):
    fx_value = f_x(e, q, Q, a, x)
    fprime_value = f_prime(e, q, Q, a, x)
    x, error = error_check(fx_value, fprime_value, x)
    print("X =", x)
    print("F(x) =", fx_value)
    print("F'(x) =", fprime_value)
    print("Error = %f\n" %(error))