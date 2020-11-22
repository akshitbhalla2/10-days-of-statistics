# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys 

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

m = float(mystdin[0])
x = int(mystdin[1])

def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        
    return f

fact_x = Factorial(x)
prob = (m**x)*math.exp(-m)/fact_x

print("{:.2}".format(prob))
