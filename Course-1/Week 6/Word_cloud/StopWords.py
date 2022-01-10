from stop_words import get_stop_words

a = get_stop_words('en')
a = get_stop_words('english')

type(a)

print(a)

b = get_stop_words('ru')
print(b)
