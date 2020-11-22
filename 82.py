# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

n = int(mystdin[0])

def Parse(i):
    try:
        val = float(i)
    except:
        val = float(int(i))
        
    return val

x = mystdin[1].split()
x = [Parse(i) for i in x]

y = mystdin[2].split()
y = [Parse(i) for i in y]

rank_x = [sorted(x).index(i) for i in x]
rank_y = [sorted(y).index(i) for i in y]

d_2 = [(i-j)**2 for i, j in zip(rank_x, rank_y)]
sum_d_2 = sum(d_2)

r = 1 - 6*sum_d_2/(n*(n**2 - 1))

print("{:.3}".format(r))
