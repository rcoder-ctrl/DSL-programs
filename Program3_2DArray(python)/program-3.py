#Write a python program to compute following computation on matrix:
#a) Addition of two matrices
#b) Subtraction of two matrices
#c) Multiplication of two matrices
#d) Transpose of a matrix

#During programming matrices are generally stored in array with its number of rows and columns in first and second position of array

def get_matrix(row,column,n):
    matrix=[]
    print("Enter values for matrix",n,":")
    for i in range(row):
        row=[]
        for j in range(column):
            value=int(input(f"Enter value in matrix at {i+1}X{j+1}:"))
            row.append(value)
        matrix.append(row)
    return matrix

def addition_matrix(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) and len(matrix1[0])!=len(matrix2[0]):
        return -1
    else:
        matrix=[]
        for i in range(len(matrix1)):
            row=[]
            for j in range(len(matrix1[i])):
                row.append(matrix1[i][j]+matrix2[i][j])
            matrix.append(row)
        return matrix
    
def subtraction_matrix(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) and len(matrix1[0])!=len(matrix2[0]):
        return -1
    else:
        matrix=[]
        for i in range(len(matrix1)):
            row=[]
            for j in range(len(matrix1[i])):
                row.append(matrix1[i][j]-matrix2[i][j])
            matrix.append(row)
        return matrix

def multiplication_matrix(matrix1,matrix2):
    if len(matrix1[0])!=len(matrix2):
        return -1
    else:
        matrix=[]
        for i in range(len(matrix1)):
            row=[]
            for j in range(len(matrix2[0])):
                value=0
                for k in range(len(matrix2)):
                    value=value+matrix1[i][k]*matrix2[k][j]
                row.append(value)
            matrix.append(row)
        return matrix
    
def transpose_matrix(matrix):
    matrixT=[]
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            value=matrix[j][i]
            row.append(value)
        matrixT.append(row)
    return matrixT

def display_matrix(matrix):
    print("[",end="")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        if len(matrix)-i==1:
            pass
        else:
            print(" ")
    print("]")
    return 0

def main():
    print("Welcome to Matrix Calculator")
    row1=int(input("Enter number of rows for first matrix:"))
    row2=int(input("Enter number of rows for second matrix:"))
    column1=int(input("Enter number of columns for first matrix:"))
    column2=int(input("Enter number of columns for second matrix:"))
    matrix1=get_matrix(row1,column1,1)
    display_matrix(matrix1)
    matrix2=get_matrix(row2,column2,2)
    display_matrix(matrix2)
    print("Enter corresponding number to fill the choices\n1:To perform addition of two matrices\n2:To perform subtraction of two matrices\n3:To perform multiplication of two matrices\n4:To perform transpose of two matrices\n5:Exit")
    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            matrix=addition_matrix(matrix1,matrix2)
            if matrix==-1:
                print("Matrix addition is not possible")
            else:
                print("Addition of two matrices:")
                display_matrix(matrix)
        elif choice==2:
            matrix=subtraction_matrix(matrix1,matrix2)
            if matrix==-1:
                print("Matrix subtraction is not possible")
            else:
                print("Subtraction of two matrices")
                display_matrix(matrix)
        elif choice==3:
            matrix=multiplication_matrix(matrix1,matrix2)
            if matrix==-1:
                print("Matrix multiplication is not possible")
            else:
                print("Multiplication of two matrices")
                display_matrix(matrix)
        elif choice==4:
            matrix=transpose_matrix(matrix1)
            print("Transpose of matrix 1:")
            display_matrix(matrix)
            matrix=transpose_matrix(matrix2)
            print("Transpose of matrix 2:")
            display_matrix(matrix)
        elif choice==5:
            exit(0)
        else:
            print("Invalid input")
main()