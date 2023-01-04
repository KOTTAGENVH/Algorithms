arr=[]
for V in range(7):
    arr.append(int(input('Enter a number ')))
print (arr)
def partition(arr,low,high):
    i = (low-1) #index of smaller element
    pivot = arr[high] #pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            #increement index of smaller element
            i = i+1;
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(arr,0,len(arr)-1)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])
