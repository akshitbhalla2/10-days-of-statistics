# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin: 
    mystdin.append(line.strip())

n = int(mystdin[0])
arr = mystdin[1].split()
arr = [int(a) for a in arr]
arr = sorted(arr)

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
    
print(q1)
print(q2)
print(q3)

