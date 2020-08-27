# standard C language
import time

m = 2**31
a = 1103515245
c = 12345
sess = [time.time()]

def rand(x):
    return (((x*a)+c) % m)

for i in range(10):
    sess.append(int(rand(sess[i])))
sess.pop(0)

print(f'({len(sess)}) {sess}')


