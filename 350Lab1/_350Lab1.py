#Justin Igmen
#200364880
#ENSE 350 Lab 1

def valueChecker():    
    while True:
        num1 = input("Enter first value: ")

        try:
            val1 = int(num1)
            if val1 <= 0:
                print ("Please enter a valid number")
            else:
                break;
        except ValueError:
            print ("This is not an integer. Please enter a valid number")

    while True:
        num2 = input("Enter second value: ")

        try:
            val2 = int(num2)
            if val2 <= 0:
                print ("Please enter a valid number")
            else:
                break;
        except ValueError:
            print ("This is not an integer. Please enter a valid number")

    return val1, val2

#This function uses recursion to take the GCD of two values
def gcd(a, b):
    if a < b:   
        temp = b
        b = a
        a = temp
 
    r = a % b
    if r == 0:
        return b
    else:
        return gcd (b, r) 

#This function uses recursion and pulverizer to find s and t in gcd(a, b) = sa+tb
def pulverizer(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = pulverizer(b % a, a)
        return (gcd, y - (b//a) * x, x)

#This function finds the lowest value of the numerator and denominator
def numDenum(num, denum, gcd):
    lowNum = num/gcd
    lowDenum = denum/gcd
    return lowNum, lowDenum

    

#---------------------------------------------
#---------------------------------------------
#---------------------------------------------

values = valueChecker()

print("\nQuestion 1:")
print("gcd (%i, %i) = %i \n" %(values[0], values[1], gcd (abs(values[0]), abs(values[1]))))

print("Question 2:")
#values = valueChecker()
pulVal = pulverizer(abs(values[0]), abs(values[1]))
print("gcd (%i, %i) = %i" %(values[0], values[1], pulVal[0]))
print("%i = %i*%i + %i*%i\n" %(pulVal[0], pulVal[1], values[0], pulVal[2], values[1]))

print("Question 3:")
#values = valueChecker()
gcd = gcd(abs(values[0]), abs(values[1]))
lowestVal = numDenum(values[0], values[1], gcd)
print("Input: %i/%i" %(abs(values[0]), abs(values[1])))
print("Output: %i/%i\n" %(lowestVal[0], lowestVal[1]))
