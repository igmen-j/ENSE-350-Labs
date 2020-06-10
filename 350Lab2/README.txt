Justin Igmen
200364880
ENSE 350 Lab 2

Step 1: 
- Program will prompt the user the enter two prime numbers, p and q
- It will check if the number is and integer, positive, and prime

Step 2: 
- n = p*q
- phi = (p-1)*(q-1)

Step 3: 
- To generate e, divide phi by 3
- Find the gcd of this value and phi
- If gcd != 1, increment this value
- Loop until gcd = 1

Step 4:
- To find d, use pulverizer with e and phi
- If d is negative, add phi to it until it is positive

Step 5:
- Message must be positive, and gcd(m,n)=1

Step 6:
- Encoding: m'=(m^e)%n

Step 7:
- Decoding: m=(m'^d)%n

