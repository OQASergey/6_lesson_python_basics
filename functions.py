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
def ffa(*abcs):
    for abc in abcs:
        print(abc)
ffa('hi','my','friends')

def ffa(*abcds):
    print(*abcds)
ffa("1","2",'3')

print('===')
def ffb(*words):
    print(words)
    print(*words)
    print(*words, sep="")
ffb('hello', 'my', 'dearest', 'dudes')

print('===')
def ffg(**afsd):
    for item in afsd.values():
        print(item)
ffg(first='hello', second='world')

#Области видимости аргументов
print('===')
n = 10
def func():
    n=15
    print(n)
func()
print(n)

