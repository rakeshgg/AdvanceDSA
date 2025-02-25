'''
Stack Creation


'''


class Stack:

    def __init__(self, size):
        self.arr = [0] * size
        # index of top elemnts
        # empty case -1
        self.top = -1
        self.size = size

    def push(self, data):
        # top ko aage vadeo
        # top pe data insert kar do
        if self.size - self.top > 1:
            # space available
            self.top += 1
            self.arr[self.top] = data
        else:
            # space not availble
            print("Stack Overflow")

    def pop(self):
        # no elements in stack UnderFlow
        if self.top == -1:
            print("stack underflow")
        else:
            self.top -= 1

    def getTop(self):
        # stack Empty
        # stack not Empty
        if self.top == -1:
            print("There is no elements in Stack")
        else:
            return self.arr[self.top]

    def getSize(self):
        # number of valid elemnts present in stack
        return self.top + 1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


if __name__ == '__main__':
    # creation
    st = Stack(10)
    # insertion
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    # remove
    st.pop()
    # check elements on top
    print(st.getTop())
    # check size
    print(st.getSize())
    print(st.isEmpty())
    while not st.isEmpty():
        print(st.getTop())
        st.pop()
    print(st.getSize())
