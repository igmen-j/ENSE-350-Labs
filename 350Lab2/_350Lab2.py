#Justin Igmen
#200364880
#ENSE 350 Lab 2


def get_p_q():
    while True:
        isPrime = True;
        num1 = input("Enter first prime number: ")
        try:
            val1 = int(num1)
            if val1 <= 0:
                print ("Not a prime. Please enter a valid prime number.")
            elif val1 == 1:
                print ("Not a valid prime. Please enter a valid prime number.")
            else:
                for i in range(2, val1):
                    if (val1 % i) == 0:
                        isPrime = False                       
                        break;
                if isPrime:
                    break;
                else:
                    print ("Not a prime. Please enter a valid prime number.")

        except ValueError:
            print ("This is not an integer. Please enter a valid prime number.")

    while True:
        isPrime = True;
        num2 = input("Enter second prime number: ")
        try:
            val2 = int(num2)
            if val2 <= 0:
                print ("Not a prime. Please enter a valid prime number.")
            elif val2 == 1:
                print ("Not a valid prime. Please enter a valid prime number.")
            elif val2 == val1:
                print ("First and second number cannot be equal. Please enter another prime.")
            else:
                for i in range(2, val2):
                    if (val2 % i) == 0:
                        isPrime = False                       
                        break;
                if isPrime:
                    break;
                else:
                    print ("Not a prime. Please enter a valid number.")
        except ValueError:
            print ("This is not an integer. Please enter a valid prime number.")
    return val1, val2

def get_gcd(a, b):
    if a < b:   
        temp = b
        b = a
        a = temp
 
    r = a % b
    if r == 0:
        return b
    else:
        return get_gcd (b, r) 

def get_e(phi):
    
    e = phi // 3
    while e < phi:
        if get_gcd(e, phi) == 1:
            return e
        else:
            e += 1

def get_d(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = get_d(b % a, a)
        return (y - (b//a) * x, x)

def get_m(n):
    while True:
        m = input("The message to be encrypted (this is an integer): ")

        try:
            val = int(m)
            if val <= 0:
                print ("Please enter a valid number")
            else:
                if val > n:
                    print ("M > %i. Please enter a number less than %i" %(n, n))
                elif get_gcd(val,n) != 1:
                    print ("gcd(%i, %i) != 1. Please enter a number for m" %(val, n))
                else:
                    break;
        except ValueError:
            print ("This is not an integer. Please enter a valid number")

    return val

def encode(m, n, e):
    return (m**e)%n
        
def decode(m_prime, n, d):
    return (m_prime**d)%n


#main function

p, q = get_p_q()
n = p*q
phi = (p-1)*(q-1)
e = get_e(phi)
d, s = get_d(e, phi)

while d <= 0:
    d += phi

m = get_m(n)
m_prime = encode(m, n, e)
new_m = decode(m_prime, n, d)


print("\nValues:")
print("First value, p: ", p)
print("Second value, q: ", q)
print("Message, m: ", m)
print("Public key (e, n): (%i, %i)" %(e, n))
print("Private key (d, n): (%i, %i)" %(d, n))
print("Encoded message m': ", m_prime)
print("Decoded message m: ", new_m)