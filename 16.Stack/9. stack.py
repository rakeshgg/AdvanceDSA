'''
https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/
https://www.geeksforgeeks.org/remove-all-redundant-parenthesis/
Remove Redundent Brackets
(()(a+b))

Logic:
- Operator - operator present inside brackets than not redudent
  (op) -> useful brackets
- Implementation-> stack, closing brackets
- pixe jake check kia(stack ke andar) koi opening haii ki nahi stack is used here
- stack track which exp comese till now
  opening brack -> push
  operator -> push

'''
