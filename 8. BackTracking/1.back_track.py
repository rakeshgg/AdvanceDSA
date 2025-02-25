'''
find all permutaion for Input string
a, b, c

- every char should put at one position(index) once
- number of permutaion = n!

case1 - x at first position   x (y, z) - reverse y, z
case2 - x at 2nd position
case3 - x at 3rd position
similarly y, z

Logic to Create:
- Think using SWAP
- string length - postion - 0 to n-1
  loop i = 0 to n-1
     put x at it's position
  swap string[i], string[j]

index 0 , 1, 2
3 - calls
- Jis index me khade haii uske age wala call karenge

solve
  # base case out of array
  if i == len(arr) # out from arr
     # store ans
     # and return
     return
  # jis vi string pe khade ho uska call maro which depend on j
  for j = i, j < len(arr), j ++
   # i and j elemnts swapped
   # next call for recursion
   # i and j elemnts again swapped --- this is called backtracking why swapped again
original state - x, y, z
(i, j) = (0, 1) -> swapped with same index ans = y, x, z - let say return if string is by refernce
string = y, x, z
(i, j) = (0, 2) -> z, x, y - this is not match with original state
so once backtracking done i want to make it as original state - x, y, z

eg: 1, 2, 3, 4  ---- swapped ---> 3, 2, 1, 4
    3, 2, 1, 4 ---- same operation again --- 1, 2, 3, 4 (original one)
Note:
Jab Recursion call se wapas aa raha hu
jo change maine kia tha usko maine undo
kar dia - so dubara swap kar dia
# if not byrefernce than no need to backtrack

'''


def toString(List):
    return ''.join(List)


def printALLPermutaion(index, output, a):
    # base case
    if index == len(a):
        output.append(toString(a))
        return
    # har char ko rakhna haii index pe
    # if j = 0 than permutation repeat
    # so take index
    for j in range(index, len(a)):
        a[index], a[j] = a[j], a[index]
        # recursive call
        printALLPermutaion(index+1, output, a)
        # backtrack code - action undeo that is backtracking
        # make it at original state
        a[index], a[j] = a[j], a[index]


a = list('xyz')
output = []
index = 0
printALLPermutaion(index, output, a)
print(output)
# ['xyz', 'xzy', 'yxz', 'yzx', 'zyx', 'zxy']
# if backtrack removed than also ans is same
# backtrack line is commented
# ['xyz', 'xzy', 'zxy', 'zyx', 'xyz', 'xzy']
