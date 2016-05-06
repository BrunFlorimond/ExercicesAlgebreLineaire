# Coding the matrix
# Computational Problem 2.8.7

from functools import reduce
from itertools import combinations
import myVec

# resolveVector :: Vec -> [Vec] -> [(Vec)]
# Retourne une combinaison de vecteurs (tirés de la liste de vecteurs en argument) égale au vecteur entré en argument
def resolveVector(v,lov):
    # combiner :: [Vec] -> Int ->[(Vec,Vec)]
    combiner = lambda n : combinations(lov,n)
    # combinaisons :: [[(Vec,Vec)]]
    combinaisons = map(combiner,range(2,len(lov)))
    # equals :: Vec -> Bool
    equals = lambda x: all([myVec.getItem(v, k) == myVec.getItem(x, k) for k in v.D])
    result = []
    for i in reduceCombinations(combinaisons):
        for j in i:
             if equals(j[0]):
                result = j[1]
                break
    return result

# reduceCombinations :: [[(Vec)]] -> [(Vec,(Vec))]
# Additionne les tuples de vecteurs et renvois le résultat et la liste de vecteur
def reduceCombinations(lloc):
    reduceComb = lambda tov: (reduce(myVec.add,tov,myVec.zeroVec(set())),tov)
    reduceComb1 = lambda lot: map(reduceComb,lot)
    return map(reduceComb1,lloc)