'''
Simplify Path
https://leetcode.com/problems/simplify-path/

Given a string path, which is an absolute path (starting with a slash '/')
to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory,
a double period '..' refers to the directory up a level, and any multiple
consecutive slashes (i.e. '//') are treated as a single slash '/'. For
this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the
root directory to the target file or directory
(i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op,
as the root level is the highest level you can go.

Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

SOLN:
/. -=> as same directore ignore
/.. -> ek pixe ka directory
c/ -> last slash have no work
/ -> single slash ignore
/a/./b/../../c/ -> simplified version /c

-> Directory me age push ho rahe ho
-> .. directory me pixe aa rahe ho
pushing and popping directory name on the basis of
/.. -> come out from current directory
/name -> going inside directory

Aprroch:
using stack
- push /a
- /. do nothing
- /b -> push
- /.. -> pop # jha khada hu ek pixe anan haii
- /.. -> pop top of stack
- /c -> push
- / -> last slash -> Ignore
Final ans lie in stack

TC -> O(N), SC->O(N)

'''


def simplifyPath(path):
    # stack
    s = []
    i = 0
    while i < len(path):
        start = i
        end = i+1
        # min path /a -> ek salsh se next slash se pahle tak
        while end < len(path) and path[end] != '/':
            end += 1
        # /a
        minPath = path[start:end]
        print(start, end, minPath)
        i = end
        if minPath == '/' or minPath == '/.':
            # ignore
            continue
        if minPath != "/..":
            s.append(minPath)
        elif len(s):
            s.pop()
    # reverse stack
    if not len(s):
        # stack empty
        # you are at root
        ans = '/'
    else:
        ans = ''.join(s)
    return ans


path = "/home//foo/"
print(simplifyPath(path))
# op - /home/foo
