str="the quick brown fox jumps over the lazy dog"

# a.Print the string to the page
print(str)

# b.Print the length of the string to the page
length=len(str)
print(length)

# c.Print the string in all uppercase letters
str_upper=str.upper()
print(str_upper)

# d.Print the string in all lowercase letters
str_lower=str.lower()
print(str_lower)

# e.Print the string in the title case
str_title=str.title()
print(str_title)

# f.Print the string in reverse
str_reverse=str[::-1]
print(str_reverse)

# g.Print the string in reverse title case
print(str_reverse.title())
str_reverse_title=str_reverse.title()
print(str_reverse_title[::-1])

# h.Count the number of times the letter “a” appears in the string
count_a=str.count('a')
print(count_a)

# i.Count the number of times the word “the” appears in the string
count_the=str.count("the")
print(count_the)

# j.Replace the word “the” with the word “a”
str_replace=str.replace('the', 'a')
print(str_replace)

# Question - 4
letter_freq = {}
for i in str:
    letter_freq[i]= str.count(i)
print(letter_freq) 


# Question - 5
people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for people,sex,age in zip(people, sex, age):
    print(f"{people} the {sex} is {age} years old")

