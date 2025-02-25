'''
Subsequence - any char can include/taken/pick
              any char can exclude/not taken/not pick
the string form is Subsequnce
Note : Maintain Relative ordering always

eg: abc
subsequnce is a, b, c, ab, ac, bc
ca is not relative ordering voilates
always : 2^n similar to power set

Pattern - AT Char - Either Incude or Exclude

TRY: WITh BIT MASKING ALSO

'''


def PrintSubSequnce(str, index, ans):
    # note: ans shoud be local in every stack
    # if ans make global than need of backtracking is required
    # base case
    if index == len(str):
        print(ans, end=' ')
        return
    # include in ans
    PrintSubSequnce(str, index+1, ans + str[index])
    # exclude in ans no add in ans
    PrintSubSequnce(str, index+1, ans)


def PrintSubSequnce2(str, index, ans, output):
    # note: ans shoud be local in every stack
    # if ans make global than need of backtracking is required
    # base case
    if index == len(str):
        # print(ans, end=' ')
        output.append(ans)
        return
    # include in ans
    PrintSubSequnce2(str, index+1, ans + str[index], output)
    # exclude in ans no add in ans
    PrintSubSequnce2(str, index+1, ans, output)


# Add two number string x = '43' y = '343' sum is output
# its string so convert it into integer
# carry = 0
# add from Right most
# i + j + carry = sum
# carry = sum // 10
# i <0, j <0 and carry <= 0 stop

def addString(a, b, i, j, carry, ans):
    if i < 0 and j < 0 and carry == 0:
        return
    first = 0
    second = 0
    if i >= 0:
        first = int(a[i])
    if j >= 0:
        second = int(b[j])
    sum = first + second + carry
    lastDigit = sum % 10
    carry = sum // 10
    ans.append(str(lastDigit))
    addString(a, b, i-1, j-1, carry, ans)


'''
str = 'abc'
ans = ''
PrintSubSequnce(str, 0, ans)


str = 'abc'
ans = ''
output = []
PrintSubSequnce2(str, 0, ans, output)
print(output)
'''

ans = []
a = '43'
b = '343'
addString(a, b, len(a)-1, len(b)-1, 0, ans)
print(''.join(ans))
