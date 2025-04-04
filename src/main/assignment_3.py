import numpy

def Question_One():
    # Defining A and b of the matrix
    a=numpy.array([[2, -1, 1], [1, 3, 1], [-1, 5, 4]])
    b=numpy.array([6, 0, -3])
    # Function provides the solution to the matrix
    ans=numpy.linalg.solve(a, b)
    print(ans)
solution_1=Question_One()


def Question_Two():
    # Define matrix A
    a=numpy.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
    # Size of matrix A
    n=a.shape[0]
    # LU Method, gives L and U
    l=numpy.zeros_like(a)
    u=a.astype(float)

    # Calculates L and U
    for i in range(n):
        l[i, i]=1
        for j in range(i+1, n):
            if (u[j, i] != 0):
                mult= (u[j, i])/(u[i, i])
                l[j, i]=mult
                u[j, i:] -= mult*(u[i, i:])

    # Function to give determinant
    determinant=numpy.linalg.det(a)
    print(determinant)
    print()
    print(l)
    print()
    print(u)
print()
solution_2=Question_Two()


def Question_Three():
    # Defining matrix A
    a=numpy.array([[9, 0, 5, 2, 1], [3, 9, 1, 2, 1], [0, 1, 7, 2, 3], [4, 2, 3, 12, 2], [3, 2, 4, 0, 8]])
    n=a.shape[0]

    # Goes through rows to see if sum is greater than the diagonal value
    for i in range(n):
        diagonal=abs(a[i, i])
        sum=0
        for j in range(n):
            if (i!=j):
                sum += abs(a[i, j])
        if(diagonal<sum):
            print("The matrix is not diagonally dominate")
            return
    print("The matrix is diagonally dominate")
print()
solution_3=Question_Three()


def Question_Four():
    a=([[2, 2, 1], [2, 3, 0], [1, 0, 2]])
    # Checks symmetry of matrix
    if not numpy.allclose(a, numpy.transpose(a)):
        print("The matrix is not a positive definite")
        return
    # Calculates eigenvalues
    eigen=numpy.linalg.eigvals(a)

    if (numpy.all(eigen>0)):
        print("The matrix is a positive definite")
print()
solution_4=Question_Four()
