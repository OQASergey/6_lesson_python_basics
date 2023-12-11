#Boolean - 3 состояния

b = bool

t = True
f = False
n = None

if not True:
    print('Истина')

else:
    print('Ложь')

# if/elif/else

code = 200

if code < 400:
    print('хороший код')

elif 400 <= code < 500:
    print ('плохой код')

elif code >= 500:
    print('плохо серверу')

else:
    print('что-то произошло')

#===============
print('=======')

print(bool(123))
print(bool(-100))
print(bool(0))

print(bool('Hello, world!'))
print(bool(" "))
print(bool(""))

print(bool([1,2,3]))
print(bool([1, 2, 2, 3]))
print(bool([]))
print(bool([False]))
print(bool([True]))