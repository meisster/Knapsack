import time
import random
import itertools


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
    print(result[wynik])
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

itemValue = [60, 100, 120, 80, 65]
itemWeight = [10, 20, 30, 20, 10]
sackWeight = 50
result = {}
print(naiveKnapSack(sackWeight , itemWeight , itemValue , result))
result = {}
print(greedyKnapSack(sackWeight , itemWeight , itemValue , result))
result = []
print(dynamicKnapSack(sackWeight , itemWeight , itemValue , result))

