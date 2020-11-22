# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [int(a) for a in arr]
p, n = arr
p = p/100

def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        
    return f
    
def Binomial(p, n, i):
    fact_n = Factorial(n)
    fact_i = Factorial(i)
    fact_n_i = Factorial(n-i)

    comb = fact_n / (fact_i * fact_n_i)

    return comb * (p**i) * ((1-p)**(n-i))

prob1 = 0
for i in range(2+1):
    prob1 += Binomial(p, n, i)

prob2 = 0
for i in range(2):
    prob2 += Binomial(p, n, i)

prob2 = 1 - prob2

print("{:.3}".format(prob1))
print("{:.3}".format(prob2))
