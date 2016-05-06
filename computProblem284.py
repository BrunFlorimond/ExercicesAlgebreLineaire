# Coding the matrix
# Computational Problem 2.8.4

from functools import reduce
from itertools import combinations
import GF2
import myVec


#Puzzle
s = {(1, 2): GF2.one, (3, 2): 0, (0, 0): GF2.one, (3, 0): 0, (0, 4): 0, (1, 4): GF2.one, (1, 3): 0, (2, 3): 0, (2, 1): GF2.one, (4, 2): 0,
(1, 0): GF2.one, (0, 3): GF2.one, (4, 0): GF2.one, (0, 1): GF2.one, (0, 2): GF2.one, (3, 3): GF2.one, (4, 1): GF2.one, (3, 1): 0, (4, 4): one, (2, 4): one,
(2, 0): GF2.one, (4, 3): GF2.one, (2, 2): GF2.one, (3, 4): GF2.one, (1, 1): GF2.one}

# map (int,int) GF2 -> [(Vec,[(Int,Int)])]
# Fonction qui résout le puzzle : prend un puzzle et retourne une liste de tuple chacun comprenant le vecteur s et les
# appuis successifs de cadrans nécéssaires pour le résoudre
def resolveLightsOut(s):
    minmax = [[reduce(fun, [x[y] for x in s.keys()]) for y in [0, 1]]
              for fun in [min, max]]
    buttons = produceAllButtons(s,minmax)
    #Puzzle en vecteur
    sVec = chap2.Vec(set(s.keys()), s)
    result=[]
    n=0
    # [(Vec,(int,int))] -> [(Vec,[(Int,Int)])]
    # (filterWrongResults s) . reduceCombinations . produceCombinations $ n buttons
    go = lambda n: filterWrongResults(sVec,reduceCombinations(produceCombinations(n,buttons),minmax))
    while (not result) and n <= len(buttons):
        n = n+1
        result = go(n)
    return result


# map (int,int) GF2 -> [(Vec,(int,int))]
# Produit tous les boutons et leurs impacts du puzzle
def produceAllButtons(s,minmax):
    return [createButton(i,j,minmax)
            for i in range(minmax[0][0],minmax[1][0]+1)
            for j in range (minmax[0][1],minmax[1][1]+1)]

# Int -> Int -> [[Int]] -> (Vec,(int,int))
# Produit l'appui sur i,j (switch des 4 boutons a cotés)
def createButton(i,j,minmax):
    max1Diff = lambda k,l: abs(k-i)+abs(l-j) <= 1
    checkBound = lambda k,l:  minmax[0][0] <= k <= minmax[1][0] and minmax[0][1] <= l <= minmax[1][1]
    dict = {(k,l): GF2.one for k in range (i-1,i+2) for l in range (j-1,j+2) if max1Diff(k, l) and checkBound(k, l) }
    return (myVec.Vec(set(dict.keys()),dict),(i,j))


# Int -> [(Vec,(int,int)] -> [[(Vec,(int,int))]]
# Produit toutes les n-combinaisons de boutons:
def produceCombinations(n,lob):
    return list(combinations(lob,n))


# [((Vec,(int,int)))] -> [(Vec,[(int,int)]]
# Additionne chaque combinaison de bouton
def reduceCombinations(llob,minmax):
    def reduceSubsets(tos):
        r = (myVec.zeroVec({(i, j) for i in range(minmax[0][0], minmax[1][0]) for j in range(minmax[0][1], minmax[1][1])}), [])
        for i in tos:
            r = (myVec.add(r[0], i[0]), r[1] + [i[1]])
        return r
    return list(map(reduceSubsets,llob))


# [(Vec,[(Int,Int)]] -> [(Vec,[(Int,Int)])]
# Renvoi les combinaison de boutons égale à s si elle existe sinon une liste vide
def filterWrongResults(s,xs):
    equals = lambda x: all([myVec.getItem(s,k) == myVec.getItem(x[0],k) for k in s.D])
    return list(filter(equals, xs))





