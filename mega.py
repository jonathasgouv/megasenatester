import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'
import random

def drawNumbers():
    return sorted(random.sample(range(1,61), 6))

def countRights(userchoice, draw):
    return sum(el in userchoice for el in draw)

def mostFrequent(List):
    return max(set(List), key = List.count)

def getMoreProbable(n):
    position1 = []
    position2 = []
    position3 = []
    position4 = []
    position5 = []
    position6 = []

    for i in range(1,n):
        if i % 1000000 == 0:
            print('{:n}'.format(i))
        draw = drawNumbers()
        position1.append(draw[0])
        position2.append(draw[1])
        position3.append(draw[2])
        position4.append(draw[3])
        position5.append(draw[4])
        position6.append(draw[5])

    return [mostFrequent(position1), mostFrequent(position2), mostFrequent(position3), mostFrequent(position4), mostFrequent(position5), mostFrequent(position6)]

def testDraw(draw,n):
    oner = 0
    twor = 0
    threer = 0
    fourr = 0
    fiver = 0
    sixr = 0

    for i in range(1,n):
        if i % 1000000 == 0:
            print('{:n}'.format(i))

        rights = countRights(draw, drawNumbers())

        if rights == 1:
            oner += 1
        elif rights == 2:
            twor += 1
        elif rights == 3:
            threer += 1
        elif rights == 4:
            fourr += 1
        elif rights == 5:
            fiver += 1
        elif rights == 6:
            sixr += 1

    print("----------------JOGO SORTEADO: {}-----------------".format(draw))

    print('Numero de vezes em que o jogador teve um número sorteado: {:n}\n'.format(oner))
    print('Numero de vezes em que o jogador teve dois números sorteados: {:n}\n'.format(twor))
    print('Numero de vezes em que o jogador teve três números sorteados: {:n}\n'.format(threer))
    print('Numero de vezes em que o jogador teve quatro números sorteados: {:n}\n'.format(fourr))
    print('Numero de vezes em que o jogador teve cinco números sorteados: {:n}\n'.format(fiver))
    print('Numero de vezes em que o jogador teve seis números sorteados: {:n}'.format(sixr))
    print("----------------------------------------------------")



#print(getMoreProbable(100000))
#print(testDraw([2, 7, 13, 22, 25, 40], 2000))
