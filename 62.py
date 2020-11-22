# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split(" ")
arr = [float(a) for a in arr]
lam1, lam2 = arr

e1 = 160 + 40*(lam1**2 + lam1)
e2 = 128 + 40*(lam2**2 + lam2)

print("{:.3f}".format(e1))
print("{:.3f}".format(e2))
