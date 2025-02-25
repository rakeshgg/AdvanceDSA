'''
Kth Symbol Grammar

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each
occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a
table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

solve in 3-ways
- complemnts
- tree term
- 2's power

complements  : same row(from upper) + its complements
2 Power pattern: convert in decimal and see tha pattern


Tree Approch:
1st level node 0
2nd level node 0, 1
3rd level node 0, 1, 1, 0

I,p - n , k
n is independet
depend on k, k's parent and k is even or odd
than kth number can find
kth parent is 0 than -- than gurantee left 0, right 1
              1 than  - than gurantee left 1, right 0

kth even or odd:
left node is odd
right node is even

if parent 0, k is even (right child) than ans is
if parent 1, k is odd (left child) than ans is

2nd way:
how to find parents any node than want to go parents
if k is even than parents = k//2
if k is odd than parents = (k+1)//2
you can update k on the basis of this

Kth Symbol -> Kth parents, even or odd
parents=0, k is odd left ans is 0
parents=0, k is even right ans is 1

k ka parent pata hona chaiie, k even or odd ho pata hona chaiie

SOLN:
    0(k1)      1(k2) -- Row1
0(k1)  1(k2)  1(k3)  0(k4) -- Row2
k-odd, k-even
you can use Ceil Also
Lets take k2 = 2/2 + 2%2 = 1 -> Parents in Row1(k1)
Lets take k3 = 3/2 + 3%2 = 1 + 1 = 2, Pernts is -> Row1(k2)

Rule-> if we find 0 than 0 creates 01 in next row
       if we find 1 than 1 creates 10 in next row

*Points
if we find 0 parents - first postion of target pair is 0, if not 1
if we find 1 parents - first postion of target pair is 1, if not 0 - k value is odd
'''


def kthGrammar(n, k):
    # base case
    # 1st row
    if n == 1:
        # 1st row may always zero
        return 0
    # find parent
    # go to previous row and find parents
    # parent = quotient + reminder (k//2 + k % 2) find upar wali row pe k kha haii exit
    # n-1, obove row as parent is above position of it is- math.ceil(k/2)
    parent = kthGrammar(n-1, k//2 + k % 2)
    print(parent)
    # during return it will move through the path
    if parent == 0:
        if k & 1:
            # k is odd
            # Left child
            return 0
        else:
            return 1
    else:
        # parent == 1
        if k & 1:
            # left child
            return 1
        else:
            return 0


print(kthGrammar(10, 2))
