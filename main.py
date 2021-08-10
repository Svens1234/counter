from collections import Counter

number_list = [1, 1, 1, 4, 4, 5, 77, 77, 3, 3, 3, 3, 3]

print(Counter(number_list))

sentence = "Hello, how are you doing ? Hello, I'm fine. How do you do ? Hey, hey, hey!"

#print(Counter(sentence. split(' ')))

c = Counter(sentence.split(' '))

#print(list(c))
#print(set(c))
#print(list(c))

#print(c.items())

#c = c.items()
#c = Counter(dict(c))
#print(c)

print(c.most_common())
print(c.most_common(2)) # 2 самых часто встречающихся
print(c.most_common()[:-3-1:-1]) # 3 самых редко встречающихся
