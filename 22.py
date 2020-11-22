# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

mystdin = []
for line in sys.stdin: 
    mystdin.append(line.strip())

n = int(mystdin[0])
arr = mystdin[1].split()
arr = [int(a) for a in arr]

mean = sum(arr)/n

SOS = 0
for a in arr:
    SOS += (a-mean)**2
    
VAR = SOS/n
STD = VAR**0.5

# Printing
print("{:.1f}".format(STD))
