# Remove punctuations from string
string = "abcd-1234-5678"
a = list(string)
b = []
c = str()
for i in range(len(a)):
    if a[i]=='-':
        continue
    else:
        b.append(a[i])
        c=c+''.join(a[i])
print(b)
print(c)