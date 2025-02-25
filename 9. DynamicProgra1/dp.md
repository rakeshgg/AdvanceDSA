# Dynamic programing

- Steps to follow Dynamic programing
- base is Recursion
- Easy than array Question

- Top-Down (REC + MEMOIZATION)
  MEMOIZATION - subproblem store when required return
  i -> 0 to n
  Upar se Niche
  eg: Tree Traversal, maximum sum from root to leaf - include all node till leaf found than update
- Bottom-UP (Table)
  i -> n to 0
  Niche se Upar ja rahe ho

# what is DP?

Bookish Defination

- to solve problem having these two features
- Overlapping Sub problems
- Optimal Substucture - combining smaller subproblems to form bigger problems
  f(5) = f(4)(optimal soln) + f(2)(optimal soln)
  bigger problem depends on smaller problem optimal soln - optimal substucture

DP - Those who cannot remember tha past are condemend to repeat itself

- remember sub problem solved till now

# Life Cycle of DP

1. Solve using Recursion
   1D/2D/3D - DP

# jiten parameter ki value change ho gi wahi DP lagana HAII

2. Recursion + memoization

   # create DP array + pass in fun (Step-1) or Global create(bad habit)

   # Store the ans in DP array (step-2)

   # check if Dp array has alreay ans if yes than return, just after base cases(step-3)

3. Bottom Up solution

   # create DP array + pass in fun (Step-1) or Global create(bad habit)

   # Recursion base cases analyze and do changes in dp array(step-2)

   # for loop range see and copy recursion logic there(step-3)

4. Space Optimization
   # dp ans dependes on which

Q: Fibonacaii Series

- 0, 1, 1, 2, 3, 5, 8, .....
  f(n) = f(n-1) + f(n-2) - Recursive relation
  f(0) = 0
  f(1) = 1

# Summary

A. Top-Down (Recursion + Memoization)

1.  create dp array, pass in function
2.  ans store in dp array and return
3.  after base case if ans already present return it (no need of Recursive call)

B. Tabulation(Bottom-UP)

1.  create dp array (Initialization to be think)
2.  Recursion - base case analyze and update dp array
3.  for loops, reverse top-down range
    copy paste recursion logic
    replace recursive call with dp and return ans

C. Space Optimization

1.  check dependency of current ans - soln exit
2.  remove dp array apply your data stucture
3.  replce dp parameters in for loop
4.  movements code need to be added

Patterns:

# 1-D DP

1. max sum of non-adjacent : inclusion/exclusion
2. rod cutting problems: first, second, third, ans find
3. min coins - for loops se min find
