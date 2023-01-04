#InsertionSortMy
A = []
n = 9
for i in range (0,n):
    number = int(input("Enter"))
    A.append(number)
    if(number>10 and number<20):
        A.append(number)
        
    else:
        print("Invalid number")
    i=i+1
    
print(A)

def INSERTIONSORT(A):
    for j in range (2,len(A)):
        key = A[j]
        i = j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

INSERTIONSORT(A)
print("Sortd",A)
    
    
