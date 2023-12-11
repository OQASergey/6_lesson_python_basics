# while - цикл с прерыванием условием
import random

rn = 7
un = random.randint(0,10)

while un != rn:
    print(f'User_Number ({un}) не равен {rn}')
    un = random.randint(0, 10)