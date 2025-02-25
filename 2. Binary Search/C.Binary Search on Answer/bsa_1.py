'''
Peak Elements
index of peak elements

- Greater than its neighbour then its a peak elemnts
- Peak elemnts can be more than one
- mid is peak or not ?  # criteria
- (mid - 1) mid (mid + 1)
   -  if mid is 1st elements than mid + 1 exit only
   -  if mid is last elements than mid - 1 exit only
arr[mid] > arr[mid-1]
arr[mid] > arr[mid+1]

Criteria of Movements
if not peak - Got to left or Go to Right
Move to that side which one is Greater than Mid beacuse of this mid is
not peak so move that side
arr[mid - 1] > arr[mid] than move to left side

'''


def findPeakElement(arr):
    start = 0
    n = len(arr)
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        # if mid is first elemnts
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                # this is a peak elemnts
                return mid
            elif arr[mid] < arr[mid-1]:
                # move to left as beacuse of grater it cannot be paek
                # may be in future it can be peak
                end = mid - 1
            else:
                start = mid + 1
        # if mid is first elemnts
        elif mid == 0:
            if arr[0] > arr[1]:
                # arr[0] is peak
                return 0
            else:
                return 1
        # if mid is last elements
        elif mid == n - 1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2
    return -1


print(f"{findPeakElement([15,35,85,96,5,6,8,12])}")
