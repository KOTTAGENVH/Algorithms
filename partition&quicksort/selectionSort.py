A = []
for v in range (1,5):
    A.append(int(input('Enter the number: ')))
    size = len(A)



def SelectionSort(A,size):
    for ind in range(size):
        min = ind

    for j in range (ind +1 , size):
        if A[j] < a [min]:
            min =j

    (A[ind],A[min]) = (A[min],A[ind])



SelectionSort(A,size)
print('The sorted Array: ')
print(A)
