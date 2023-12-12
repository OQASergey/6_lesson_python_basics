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





