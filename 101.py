# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import sys 
import math

mystdin = []
for line in sys.stdin:
    mystdin.append(line)

arr = mystdin[0].split()
m, n = [int(a) for a in arr]

train = []
for t in mystdin[1:n+1]:
    temp = []
    for num in t.split():
        temp.append(float(num))
    
    train.append(temp)
    
train = np.array(train)

X = train[:, :m].reshape(n, m)
X = np.hstack((np.ones(n).reshape(n, 1), X))
Y = train[:,  m].reshape(n, 1)

q = int(mystdin[n+1])

test = []
for t in mystdin[n+2:]:
    temp = []
    for num in t.split():
        temp.append(float(num))
    
    test.append(temp)
    
test = np.array(test)

test = test[:, :m].reshape(q, m)
test = np.hstack((np.ones(q).reshape(q, 1), test))

def GetY(X, Y, test):
    XT_X = np.dot(X.T, X)
    XT_X_inv = np.linalg.inv(XT_X)
    XT_X_inv_XT = np.dot(XT_X_inv, X.T)
    B = np.dot(XT_X_inv_XT, Y)
    
    y = np.dot(test, B)

    return y
    
y = GetY(X, Y, test)

for i in y:
    print("{:.5}".format(i[0]))

