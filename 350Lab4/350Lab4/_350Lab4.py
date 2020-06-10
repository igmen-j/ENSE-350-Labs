#Justin Igmen
#200364880
#ENSE 350
#Lab 4
#Reference: https://www.tutorialspoint.com/cplusplus-program-to-perform-lu-decomposition-of-any-matrix
#Modified and updated in Python

def getValues():
    print("LU Decomposition \n")
    n=int(input("Enter size of the square matrix: "))+1         #3 here
    #print("\n")
    a=[]                                                #use list for storing 2D array

    #get the user input and store it in list (here IN : 1 to 9)
    for i in range(n-1): 
        row_list=[]
        for j in range(n-1):
            row_list.append(float(input("Enter value %i of row %i: " %(j, i))))
        row_list.append(float(input("Enter solution for row %i: " %(i))))    
        print()
        a.append(row_list)                               #add the row to the list

    print("Matrix A: \n") 

    #Display the 2D array
    for i in range(n-1):
        for j in range(n):

            if j == n-2:
                print (str((a[i][j])).rjust(6), end="   |") 
            elif j ==n-1:
                print(str((a[i][j])).rjust(6), end="  ")
                print();
            else:
                print(str((a[i][j])).rjust(6), end="  ")
    return a, n
    

def LU():

    l = []
    u = []

    for i in range(n-1):
        row_list=[]
        for j in range(n):
            if j < i:
                row_list.append(0)
            else:
                row_list.append(a[j][i])
                for k in range(i):
                    row_list[j][i] = row_list[j][i] - row_list[j][k] * u[k][i]
        l.append(row_list)
        print(l)


        



 
a, n = getValues()
LU()

#eq1_x, eq1_y, eq1_z, eq1_sol = valueChecker(1)
#print("\n")
#eq2_x, eq2_y, eq2_z, eq2_sol = valueChecker(2)
#print("\n")
#eq3_x, eq3_y, eq3_z, eq3_sol = valueChecker(3)

#LU(eq1, eq2, eq3)
