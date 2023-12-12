#def
def my_func():
    print('Hello!')
my_func()
my_func()

print('===')
def fa(line):
    print(line)
fa('hello')
fa('world')
fa(str)

print('***')
def faa(line, abcd, aaa):
    print(line, abcd, aaa)
faa('hello', ',', 'world!')

#именованные аргументы
print('===')
def fb(line1, line2):
    print(line1, line2)
fb(line2='world!', line1='Hello,')

#аргумент в значении None
print('===')
def fc(line1, line2=None):
    print(line1, line2)
fc('hello!', 'hi')

def fcc(line, symbol=None):
    if symbol is None:
        print(line)
    else:
        print(f'{symbol} {line} {symbol}')
fcc('aloha')
fcc('aloha', 'Eahhh!')

#Возвращение одного значения
print('===')
def fd(a, b, c):
    return a+b-c
aa = fd(2,3,4)
print(aa)
assert aa == 1

#Возвращение нескольких значений
print('===')
def ff():
    return 2,4,8,16
fff = ff()
print(fff)
print('***')
#a,b,c,d = fff
#print(a,b,c,d)
#a,_,c,d = fff
#print(a,c)

a,b,*_ = fff
print(a,b)

print('===')
def ffa(*abc):
    print(abc)
ffa('hi','my','friend')


