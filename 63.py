# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [float(a) for a in arr]
m, s = arr

x = float(mystdin[1])

arr = mystdin[2].split(" ")
arr = [float(a) for a in arr]
x1, x2 = arr

def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    return (1.0 + q) / 2.0

p1 = normal_cdf((x-m)/s)
p2 = normal_cdf((x2-m)/s) - normal_cdf((x1-m)/s)

print("{:.3f}".format(p1))
print("{:.3f}".format(p2))
