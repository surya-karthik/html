vowels = {'a','e','i','o','u'}
word = input("type your word, ")

r = vowels.intersection(set(word))
print(r)
