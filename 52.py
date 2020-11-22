# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [int(a) for a in arr]
num, den = arr

p = num/den
n = int(mystdin[1])

prob = 1 - (1-p)**n
print("{:.3}".format(prob))
