str = input()
result = ''
for i in str:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    result += i  
print(result)