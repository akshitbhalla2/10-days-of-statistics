# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin: 
    mystdin.append(line.strip())

n = int(mystdin[0])
arr = mystdin[1].split()
arr = [int(a) for a in arr]
arr = sorted(arr)

# Mean
summation = 0
for i in arr:
    summation += i
    
mean = summation/n

# Median
a = n//2
if n%2==0:
    median = (arr[a] + arr[a-1])/2
else:
    median = arr[a]

# Mode
mode = max(set(arr), key=arr.count)

# Printing
print("{:.1f}".format(mean))
print("{:.1f}".format(median))
print(mode)

