import time
import random
import itertools
from termcolor import colored


def naiveKnapSack(sackWeight: int, itemWeight: list, itemValue: list, result: dict):
    tempMax = 0
    tempMaxW = 0
    for i in range(2**(len(itemValue)), 2**(len(itemValue)+1)):
        temp = bin(i)[3:]
        sum = 0
        wSum = 0
        for j in range(len(itemValue)):
            sum += itemValue[j]*int(temp[j])
            wSum += itemWeight[j]*int(temp[j])
        if wSum <= sackWeight:
            if sum >= tempMax:
                tempMax = sum
                tempMaxW = wSum
                result.setdefault(tempMax, [])
                result[tempMax].append(temp)
    wynik = list(result.keys())[len(result)-1]
    listawynikowa = []
    for i in range(len(result[wynik])):
        for j in range(len(itemValue)):
            if int(result[wynik][i][j]):
                listawynikowa.append(itemValue[j])
        listawynikowa.append(';')
    return wynik, listawynikowa #[itemValue[j] for j in range(len(itemValue)) for k in range(len(result[wynik])) if int(result[wynik][k][j])>0]


def greedyKnapSack(sackWeight: int, itemWeight: list, itemValue: list, result: dict):
    itemWeight2Val = [itemValue[i]/itemWeight[i] for i in range(len(itemValue))]
    indexes = [i for i in range(len(itemWeight2Val))]
    indexes.sort(key=itemWeight2Val.__getitem__)
    indexes.reverse()
    itemValue = list(map(itemValue.__getitem__, indexes))
    itemWeight = list(map(itemWeight.__getitem__, indexes))
    itemWeight2Val = list(map(itemWeight2Val.__getitem__, indexes))
    tempWeight = 0
    resultVal = 0
    result = []
    for i in range(len(itemValue)):
        if tempWeight + itemWeight[i] < sackWeight:
            resultVal += itemValue[i]
            result.append(itemValue[i])
            tempWeight += itemWeight[i]
    return resultVal, result


def dynamicKnapSack(sackWeight: int, itemWeight: list, itemValue: list, result: list):
    matrix = [0]*(len(itemValue)+1)
    for i in range(len(itemValue)+1):
        matrix[i] = [0]*(sackWeight+1)
    if sackWeight == 0 or not itemValue:
        return 0
    else:
        for i in range(1, len(itemValue)+1):
            for j in range(1, sackWeight+1):
                if itemWeight[i-1] > j:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-itemWeight[i-1]]+itemValue[i-1])
    result = []
    done = False
    i = len(itemValue)
    j = sackWeight
    while not done:
        if matrix[i][j] == matrix[i-1][j]:
            i -= 1
        else:
            if matrix[i-1][j-itemWeight[i-1]] == 0:
                result.append(itemValue[i-1])
                done = True
            else:
                result.append(itemValue[i-1])
                i -= 1
                j -= itemWeight[i]
                if matrix[i][j] == 0:
                    done = True

    return matrix[len(itemValue)][sackWeight], result


#itemValue = [60, 100, 120, 80, 65]
#itemWeight = [10, 20, 30, 20, 10]
#sackWeight = 50
itemValue = []
itemWeight = []
sackWeight = 0
done = False
while not done:
    while True:
        try:
            size = int(input('Wprowadz wielkość plecaka(ilość przedmiotów): '))
            break
        except ValueError:
            print(colored('Niepoprawna wartość, spróbuj ponownie.', 'red'))

    while True:
        try:
            sackWeight = int(input('Wprowadź maksymalną wagę plecaka: '))
            break
        except ValueError:
            print(colored('Niepoprawna wartość, spróbuj ponownie.', 'red'))
    print('\nWprowadź wartość przedmiotów. ')
    for i in range(size, 0, -1):
        while True:
            try:
                item = int(input('Pozostało ' + str(i) + ' przedmiotów\n'))
                break
            except ValueError:
                print(colored('Niepoprawna wartość, spróbuj ponownie.', 'red'))
        itemValue.append(item)
    print('\nWprowadź wagę przedmiotów. ')
    for i in range(size, 0, -1):
        while True:
            try:
                item = int(input('Pozostało ' + str(i) + ' przedmiotów\n'))
                break
            except ValueError:
                print(colored('Niepoprawna wartość, spróbuj ponownie.', 'red'))
        itemWeight.append(item)
    print('Oto wprowadzone dane: ')
    print('Waga plecaka: ', sackWeight)
    print('Wartość przedmiotów: ', itemValue)
    print('Waga przedmiotów: ', itemWeight)
    print('\nCzy chcesz wykonać algorytmy dla powyższych danych?', '0 -- nie', '1 -- tak', sep='\n')
    ifCalculate = int(input())
    if ifCalculate == 1:
        result = {}
        print('Algorytm plecakowy naiwny', naiveKnapSack(sackWeight , itemWeight , itemValue , result), sep='\n')
        result = {}
        print('Algorytm plecakowy zachłanny', greedyKnapSack(sackWeight , itemWeight , itemValue , result), sep='\n')
        result = []
        print('Algorytm plecakowy dynamiczny', dynamicKnapSack(sackWeight , itemWeight , itemValue , result), sep='\n')
        print('\nCzy chcesz wykonać algorytm ponownie?')
        print('0 -- nie')
        print('1 -- tak')
        x = int(input())
        if x == 0:
            done = True
            print('Do widzenia!')
    else:
        print('Czy chcesz wprowadzić dane ponownie?', '0 -- nie', '1 -- tak', sep='\n')
        ifEnter = int(input())
        if ifEnter == 0:
            done = True
            print(colored('Do widzenia!', 'green'))

