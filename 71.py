# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

max_wt = int(mystdin[0])
n_boxes = int(mystdin[1])
m = int(mystdin[2])
s = int(mystdin[3])

def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    return (1.0 + q) / 2.0

x = max_wt/n_boxes
z = (x-m)/(s/math.sqrt(n_boxes))
prob = normal_cdf(z)

print("{:.4f}".format(prob))
