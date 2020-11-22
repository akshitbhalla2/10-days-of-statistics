# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin: 
    mystdin.append(line.strip())

X = mystdin[1].split()
X = [int(a) for a in X]
F = mystdin[2].split()
F = [int(f) for f in F]

arr = []
for x, f in zip(X, F):
    arr += [x]*f
    
arr = sorted(arr)
n = len(arr)

# Median
def GetMedian(n, arr):
    a = n//2
    if n%2==0:
        median = (arr[a] + arr[a-1])/2
    else:
        median = arr[a]
        
    return int(median)

q2 = GetMedian(n, arr)

a = n//2
if n%2==0:
    q1 = GetMedian(a, arr[:a])
    q3 = GetMedian(a, arr[a:])
else:
    q1 = GetMedian(a, arr[:a-1])
    q3 = GetMedian(a, arr[a+1:])
    
IQR = q3-q1

# Printing
print("{:.1f}".format(IQR))

