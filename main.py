#Searching a Matrix

#Given a matrix that is organized such that the numbers will always be sorted left to right, and the first
#number of each row will always be greater than the last element of the previous row
#(mat[1][0])>(mat[i-1][[-1]), search for a specific value in the matrix and return whether it exists

def searchMatrix(mat, value):
    if len(mat)==0:
        return False
    row_len=len(mat)
    col_len=len(mat[0])

    low=0
    high=row_len + col_len

    while low<high:
        mid=(low+high)//2
        if mat[mid//col_len][mid%col_len] == value:
            return True
        elif mat[mid//col_len][mid%col_len] < value:
            low=mid+1
        else:
            high=mid

    return False

mat =[[1,3,5,8],[10,11,15,16],
[24,27,30,31]]

print(searchMatrix(mat, 8))