
str="the quick brown fox jumps over the lazy dog"

'''print(str) 
print(len(str))
print(str.upper())
print(str.lower())
print(str.title())
print(str.replace('the','a'))
print(str.count('a'))
print(str.count('the'))


people=['jane','john','jack','janet']
sex=['female','male','male','female']
age=[23,34,16,28]
for people,sex,age in zip(people,sex,age):
    print(f'{people} the {sex} is {age} years old')'''

from collections import Counter
counts=Counter(str) 
for i in str:
    print(i,counts[i])

