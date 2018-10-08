import numpy as np

def iterative_levenshtein(sourceString, targetString):

    rows = len(sourceString)+1
    cols = len(targetString)+1
    dist = np.zeros((rows+1,cols+1))
    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if sourceString[row-1] == targetString[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution



    return dist[row][col]

