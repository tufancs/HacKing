from time import sleep
from random import random, randint


while True:
    if input('Type "basla" to Start HacKing.\n> ') == 'basla':
        print('\n' * 1000)
        break
    else:
        print('\n' * 1000)
        pass
print('islem Baslatiliyor')
sleep(2)
for percent in range(1, 101):
    print(f'\rislem suruyor | {percent}% |')
    if randint(1, 3) == 2:
        sleep(random())
    if percent == 100:
        sleep(3)
print('HacKing Basarili')
sleep(2)
print('\n' * 1000)
print('  T U F A N')
sleep(.75)
print('  C A R P T I')
sleep(.75)
print('  S Y S T E M')
sleep(.75)
print('  H A C K E D')
sleep(.75)
print('\n' * 1000)
sleep(.75)
print ('İG:TUFANDINC0')

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Device name is:" + hostname)
print("Your Device IP Address is:" + IPAddr)