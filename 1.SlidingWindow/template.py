'''
Fixed Window Size
i, j = 0
while j < len(array):
   calculation() ## do some calculation 
   if ws < k:
      # increment j window size
      j++
   elif ws == k: # k is one possible candidate to be answer 
      ans = calculation() ## get one ans from calculations 
      # some calcultion to remove i
      window size need to maintains so do 
      i++
      j++
return ans

-------
Variable Window Size

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