1. Nearest Greater to Left
2. Nearest Greater to Right(Next largest Elemnts)
3. Nearest Smaller to Left(Next smallest Elemnts)
4. Nearest Smaller to Right
5. Stock Span Problems
6. maximum Area of Hisogram 
7. Maxium Area of Rectange in Binary Matrix
8. Rain Water Trapping
9. Implementing a Min Stack
10.Implement Stack using heap
11.The Testibility Problems
12.Longest Valid Paranthesis
13.Itertaive Tower of Hanoi

# refer - https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems


# Monotonic stacks are generally used for solving questions of
the type - next greater element, next smaller element, 
previous greater element and previous smaller element.


What is monotonic stack?
There could be four types of monotonic stacks. Please read them carefully, we'll refer to these types at multiple places in the sections below.

Strictly increasing - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
Non-decreasing - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
Strictly decreasing - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
Non-increasing - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]

-> We also assume that the right most element is at the top of the stack and left most element is at the bottom of the stack.






