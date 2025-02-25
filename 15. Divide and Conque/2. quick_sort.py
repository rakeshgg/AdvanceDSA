'''
Quick Sort  - O(nlogn)-AVG case
A. Partion Logic
  s = 0, e = n-1
  - pivot element se kitna xota haii count
  - swap(arr[pivot], arr[s+count])
B. Recursive Logic


1 number ko sahi jgh paucha de baaki recursion dekhega
Sahi Jgh Paucha:
[8, 3, 4, 1, 20, 50, 30]
Partion Logic - Pivoit -> random or first index, or last index
8 right position is 3rd index
8 se xote left side
8 se vada right side

ALGO:
A. Partion Logic  -- O(2N)
   1. choose pivot -> pivotIndex = s
   2. pivot ko sahi position pe place karna haii - How?
   3. count=0, count number < pivot elements let count=3
      aapse xote 3 log haii to common sense aap 4th index pe aeoge na
      s+count -> 4
      swap(arr[pivotIndex], arr[s+count])
   4. Left me pivot se xota, right me pivot se vada using 2 pointer approch
      i, j
   5. Recursive calls - sort left, right array  - let alwaya at mid break

'''


def partition(arr, s, e):
    # step-1, choose pivotelement
    pivotIndex = s
    pivotElement = arr[s]
    # step-2, find right pos for pivot elements and place there
    count = 0
    for i in range(s+1, e+1):
        if arr[i] <= pivotElement:
            count += 1
    # jab loop se vhar aya then pivot ka right position index ready haii
    rightIndex = s + count
    # swap
    arr[pivotIndex], arr[rightIndex] = arr[rightIndex], arr[pivotIndex]
    pivotIndex = rightIndex
    # step-3 left me xota right me vada
    # 2 pointer approch
    i = s
    j = e
    while i < pivotIndex and j > pivotIndex:
        while arr[i] <= pivotElement:
            i += 1
        while arr[j] > pivotElement:
            j -= 1
        # two case ho sakta haii
        # you found elemnts to swap - case A
        # no need to swap - Case B
        if i < pivotIndex and j > pivotIndex:
            arr[i], arr[j] = arr[j], arr[i]
    return pivotIndex


def quickSort(arr, s, e):
    # base case
    # single element sorted, invalid range
    if s >= e:
        return
    # partion logic
    p = partition(arr, s, e)
    # recursive calls
    quickSort(arr, s, p-1)
    quickSort(arr, p+1, e)


if __name__ == '__main__':
    arr = [8, 1, 3, 4, 20, 50, 30, 30]
    n = len(arr)
    s = 0
    e = n - 1
    quickSort(arr, s, e)
    print(arr)
