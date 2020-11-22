# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [int(a) for a in arr]
m, s = arr

a = int(mystdin[1])
b = int(mystdin[2])

def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    return (1.0 + q) / 2.0

p1 = 1 - normal_cdf((a-m)/s)
p3 = normal_cdf((b-m)/s)
p2 = 1 - p3

print("{:.2f}".format(p1*100))
print("{:.2f}".format(p2*100))
print("{:.2f}".format(p3*100))
