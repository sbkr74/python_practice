# sort words in alphabetic order
s = "I am a python developer"
result = s.split()
print(type(result))
result.sort(key=str.lower)      # if ignoring the case
result.sort()                   # if case_based sorting
print(result)