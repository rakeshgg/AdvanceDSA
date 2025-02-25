# Stack OverFlow in Recursion
- Result in Program Crash
- Function call stored in stack which has Finite number of Capacity
- Number of Function exceed capacity that is called stack overflow

# Overflow Condition
- No base case in recusive functions - Infinite call cause stack overflow
 eg: fact(n):
       return n * fact(n-1)
 recusive call n = 5, 4, 3, 2, 1, 0, -1, .......Infinite
 stack memory overflow

- When Recursive call doesnot align towards the base case
  eg: factorial(n):
       if n <= 1:
          return 1
       return n * fact(n+1)

 n = 5, recusive call = 5, 6, 7, 8, 9 ..... Never Reach to base Conditions


# Recusrion:
  - fun call itself
  - base case defined - fun call stop
  - Recursive call should align towards base case

# How Recursion Works

Factorial using Recursion
fact(6) = 6 * 5 * 4 * 3 * 2 * 1
fact(N) = N * (N -1) * (N-2) * .........1
Recursive call = N * fun(N-1)
Base case : N == 1

# Recursion to Itertive Function
Q: Given N print n to 1

Iterative Logic:

def Iteration(n):
    while n >= 1:
        print(n)
        n -= 1

Convert to Recursion
- Loop - Recursive Function Calls
- Termination - base case


def recursion(n)
    if n < 1:
       return
    print(n)
    recursion(n-1)

# Recursion VS Iteration
 - Control Variable and Termination Logic
   In Iteration value of control varaible moves towards termination conditions
   In Recursion Function calls keep moving towards the base case

- Storage
  In Iteration control variable hold value based on need incremented or decremented
  updated value of control varibale checked on termination conditions

  In recursion every function state is maintained on stack memory when base
  case meet the execution will follow last in first out principle
  Last inserted function will executes first and result will return 
  to its calling function

- Infinite Loops
  In Iteration if control variables not moves towards the termination condition
  loop executed infinite time

  In recursion if no base case the recursive function calls pushed on to the stack
  memory continiously, overflow memory

# Type of Recursion
1. Direct Recursion: Function call itself
    A.Tail Recursion:
        fun()
            //op
            //op
            fun()
    B.Head Recursion:
        fun()
            fun()
            //op
            //op
    C.Nested Recursion
        fun()
         // base case
         fun(fun(n+k))
    D.Tree or Binary Recursion - functin call itself twice
        fun()
         // base case
         fun()
         fun()

2. Indirect recursion: More than one function call mutually

# Tail Recursion

- Recursive call is at last of funnction
fun()
  //op1
  //op2
  fun()  -- tail of functions executed at last

- All recrsive call will pop out from stack after its execution
- This kind of Tail Recursion was optimized by compiler before execution
- Its called Tail call Elimination or Optimization
- use start --- goto sart which turns it in Loops - optimized memory
- so efficent along all of recursion calls

# Head Recursion
- Recursive call first executed by functions
fun()
   fun() - head recursion
   //op1
   //op2
- operation happens while returing
- Recursive call made first than on return logic of function executed

# Nested Recursion
- arg passed is recursive function itself
fun()
  // base case
  fun(fun(n+k))
- Recursion inside recursion

# Indirect Recursion
A()
  B()

B()
  A()

Mutual recursion
Calling
A() --> B()
B() --> A()

# Binary Recursion/Tree Recursion
- Function call itself twice
func()
  //operation 1
  //operation 2
  fun()
  fun()

eg nth term in fibonacail series










   



  


