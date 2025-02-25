"""
Templates fixed Size Sliding window

1. Window Size is Given
2. repeating works using 2 for loops #overlapping elements between the array
3. array/string - Largest/maximum - subaaray/substring - continous
4. k window size is given
   ws = (j-i+1)

Fixed Size Templates: -
k - given in problems if not find that  
ws < k - increment window size using j
ws == k - find ans, remove calculation for i, shift window by doing i++, j++

i, j = 0
while j < len(array):
calculation() ## do some calculation
if ws < k: # increment j window size
j++
elif ws == k: # k is one possible candidate to be answer
ans = calculation() ## get one ans from calculations # some calcultion to remove i
window size need to maintains so do
i++
j++
return ans

"""

Problems Related to Fixed Size window
eg:

1. max/min subaaray of size k
2. 1st negative in every window of size k
3. count occurance of anagrams

###################
Variable Size Window

- ws size not given we need to find window size
- some condition given we need to maximize ws based on that condition
- In place of WS comapre Conditions

condition - given in problems  
condition < k - increment window size using j
condition == k - ans find increment j
condition > k -- out of condition so need to maintain condition # remove calculation of i
'''
i,j = 0
while j < len(arr):
calculation() # do calculation required
if condition < k:
j++ # incremnet j till satisfy condition
elif condition == k:
ans <- calculation() ## get ans best on calculations
j++
elif condition > k:
while condition > k:
remove calculation() for i
i++
j++
return ans
'''

Problems Related to Variable Size window
eg:

1. Largest/smallest subarray of sum k
2. largest substring of k distinct character
3. length of largest substring with no repeating character
4. pick toys
5. minimum window substing

### Note : J incremnet in all cases
