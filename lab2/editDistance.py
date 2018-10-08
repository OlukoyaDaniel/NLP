import numpy as np


def minEditDistance(sourceString, targetString):
    rows = len(sourceString) + 1
    cols = len(targetString) + 1
    dist = np.zeros((rows + 1, cols + 1))
    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if sourceString[row - 1] == targetString[col - 1]:
                cost = 0
            else:
                cost = 2
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution

    return dist[row][col]


def run():
    sourceString = input('Enter source string: ')
    targetString = input('Enter target string: ')
    med = minEditDistance(str(sourceString), str(targetString))
    print('The min edit distance between "' + str(sourceString) + '" and "' + str(targetString) + '" is ' + str(med))

run()
