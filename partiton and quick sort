#Partition Q2
A=[]
for v in range(5):
    A.append(int(input("Enter Number :")))
print(A)
def partition(A,p,r):
        x=A[r]
        i= (p-1)

        for j in range(p,r):
         if A[j] <= x:
              i = i + 1
              A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i + 1]
        return (i+1)

#Quick Sort Q3
def QuickSort(A,p,r):
        if p < r :
           q = partition(A,p,r)
           QuickSort(A,p,r-1)
           QuickSort(A,p+1,r)


QuickSort(A, 0,len(A)-1)
print("Sorted array is :")
for i in range(len(A)):
    print(A[i])

