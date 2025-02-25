'''
https://www.geeksforgeeks.org/painting-fence-algorithm/
Painting Fence Algorithm

Given a fence with n posts and k colors,
find out the number of ways of painting the
fence such that at most 2 adjacent posts have
the same color. Since the answer can be large
return it modulo 10^9 + 7.


Input : n = 2 k = 4
Output : 16
Explanation: We have 4 colors and 2 posts.
Ways when both posts have same color : 4
Ways when both posts have diff color :
4(choices for 1st post) * 3(choices for 2nd post) = 12

Input : n = 3 k = 2
Output : 6

Not more than two ajacent post have same colors
no of post = 4
color = 2 (r, b)

what is pattern:
how to know 2 red already taken
what if colour count is more

NOTE: if not visualize
try to solve on small input to
identify patterns

Soln:
current index any color want to put which index it depends
- depends on last of two colors
  - last two colors same
  - last two colors different

3 color (r,g,b)

last two color same
if n = 2
rr
gg
bb
last two color different
rg
rb
br
bg
gr
gb
Total n = 2, k =3 => 3 + 6 = 9 (ans)

if n = 3 post
can we add r, g, b in above no 3 colors same

rgg
rbb
brr
bgg
grr
gbb     f(n-1) * (k-1)
n = 3 ans deoendes in n = 2 last two color same

exploring differnt one
- add diffent diffenrt in all case 9 formed
rrg
rrb
ggr
ggb
bbr
bbg

# differnt
rgr
rgb
rbr
rbg
brb
brg
bgr
bgb
grb
grg
gbg
gbr
ans  = 18

PATTERN:
n = 1, smae/diff not exit - ans = 3 (r, g, b)
n = 2,
  same -> [][] = ans = k = 3
  differnt -> [][] -> ans = 6, k * (k-1)
  ans = 9
n = 3
  same -> [][][] = ans = 6 is equal to n-1 different ans
  differnt -> [][][] -> ans = 12

Formula:
last two same color - k-color ways exist
          # last two post same colors
f(n, k) = f(n-2, k) * (k-1)
last two different color
f(n, k) = f(n-1, K) * (k-1)

k = 3, post = 7
n = 5 # dabba

'''


def countWays(n, k):
    # base case
    if n == 1:
        return k
    if n == 2:
        # [][] - kways for each
        return k * k
    # n-2, 2 dabba last me, same
    same = countWays(n-2, k) * (k-1)
    # n -1, 1 dabba last me, differnt
    diff = countWays(n-1, k) * (k-1)
    ans = same + diff
    return ans


print(countWays(5, 3))
# 180
