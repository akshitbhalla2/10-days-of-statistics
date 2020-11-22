# Enter your code here. Read input from STDIN. Print output to STDOUT

def GetY(X):
    a = 26.78082192
    b = 0.6438356164

    y = a + b*X
    
    return y

y = GetY(80)

print("{:.3}".format(y))
