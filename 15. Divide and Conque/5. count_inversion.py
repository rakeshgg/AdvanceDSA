'''
count Inversion
https://www.hackerrank.com/challenges/ctci-merge-sort/problem
Merge Sort: Counting Inversions

In an array, arr, the elements at indices i and j (where i < j) form an inversion if
arr[i] > arr[j]
In other words, inverted elements arr[i] and arr[j] are considered to be "out of order".
To correct an inversion, we can swap adjacent elements.

Inversion Kab Hoga
- i, j, if i < j => a[i] > a[j]

[8, 4, 2, 1]  -> ek unsorted array sorted banne me kitna swap lagega so  it become sorted
              -> This is called Inversion Count

[8, 4, 2, 1]
 i, j

 (8, 4)  (4, 2)
 (8, 2)  (4, 1)
 (8, 1)  (2, 1)
 i < j, arr[i] > arr[j]
 - 6 inversion, if swaps these pairs than sorted
[1, 2, 4, 8]

Approch 1:
 for i=0 to N
   for j = i + 1, to N
     # i < j always
     if a[i] > a[j]
       count++
  TC: O(n^2)

Approch 2: using Merge Sort
- Divide array
- Merge Operations -> two input sorted
- Modification on Merge Sort -> Count Inversion -> Swapping point
  [4, 8] [1, 2] - Inversion count - (4, 1), (8, 1), (4, 1), (8, 2)
   j      i
# ->


'''


def countInversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


if __name__ == '__main__':
    arr = [8, 4, 2, 1]
    result = countInversions(arr)
    print(result)
