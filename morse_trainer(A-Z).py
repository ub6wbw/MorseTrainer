#Morse Code Trainer

from playsound import playsound
from random import randint
from time import sleep

cnt = 0
Rand5 = []
while True:
    Rand5.append(chr(randint(65, 90)))
    cnt += 1
    if cnt%5 == 0:
        cnt = 0
        playsound('' + Rand5[0] + '.mp3')
        playsound('' + Rand5[1] + '.mp3')
        playsound('' + Rand5[2] + '.mp3')
        playsound('' + Rand5[3] + '.mp3')
        playsound('' + Rand5[4] + '.mp3')
        Input = '.'.join(input()).split('.')
        if Input == Rand5:
            print('Ok !')
        else:
            print('ERROR !')
        print(Rand5[0], Rand5[1], Rand5[2], Rand5[3], Rand5[4], end = '\n\n')
        print()
        sleep(5)
        Rand5.clear()
