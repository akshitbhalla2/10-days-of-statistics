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

sum_x = sum(x)
sum_y = sum(y)

sum_x_2 = sum([i**2 for i in x])
sum_y_2 = sum([i**2 for i in y])

sum_x_y = sum([i*j for i, j in zip(x, y)])

num = n*sum_x_y - sum_x*sum_y
den = math.sqrt((n*sum_x_2 - sum_x**2)*(n*sum_y_2 - sum_y**2))

r = num/den

print("{:.3}".format(r))
