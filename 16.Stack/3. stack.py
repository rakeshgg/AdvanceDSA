'''
Reverse string using Stack

'''

str = "rakesh"
stack = []
for i in range(len(str)):
    stack.append(str[i])
while len(stack):
    print(stack[-1])
    stack.pop()
