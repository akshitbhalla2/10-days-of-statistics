# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin: 
    mystdin.append(line.strip())

n = int(mystdin[0])

arr = mystdin[1].split()
arr = [int(a) for a in arr]

wts = mystdin[2].split()
wts = [int(w) for w in wts]

# Mean
summation = 0
for i, j in list(zip(arr, wts)):
    summation += i * j
    
mean = summation/sum(wts)

# Printing
print("{:.1f}".format(mean))

