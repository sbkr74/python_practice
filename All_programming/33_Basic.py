# print fibbonacci using recursion
def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
for i in range(10):
    print(fibbo(i))