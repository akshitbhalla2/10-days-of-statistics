# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

n = int(mystdin[0])
m = int(mystdin[1])
s = float(mystdin[2])
p = float(mystdin[3])
z = float(mystdin[4])

a = -z*(s/math.sqrt(n)) + m
b = z*(s/math.sqrt(n)) + m

print("{:.2f}".format(a))
print("{:.2f}".format(b))
