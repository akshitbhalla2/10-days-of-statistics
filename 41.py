# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [float(a) for a in arr]
b, g = arr

def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        
    return f

p = b/(b+g)
q = g/(b+g)   
    
sum = 0
fact_6 = Factorial(6)
for i in range(3):
    fact_i = Factorial(i)
    fact_6_i = Factorial(6 - i)
    
    combi = fact_6/(fact_i * fact_6_i)
    sum += combi *  (p**i) * (q**(6-i))
    
prob = 1 - sum
print("{:.3}".format(prob))
