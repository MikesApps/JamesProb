import pandas as pd
from itertools import product
df = pd.read_csv('matrizx.csv')
value_cols = df.drop(['Subgroup','Group'], axis=1).columns

#Tries one solution. Df is your dataframe, sol is a potential solution (binary list). 
def testOneSol(df, sol):
    y = df[value_cols] * sol
    y['Group']=df['Group']
    z= y.groupby('Group', sort=False).sum()
    return z.sum(axis=1)

#Tries all solutions and returns the best one. 
def tryEverything(df, max):
    bestSol = []
    bestResult = -1
    for sol in [i for i in product(range(2), repeat=22)]:
        ans = testOneSol(df, sol)
        if ans.le(max).all() and bestResult < ans.sum():
            bestSol = sol
            bestResult = ans.sum()
            if bestSol == max * len(ans):
                return bestSol #Early exit because perfect solution has been found
    return bestSol




y = tryEverything(df, 10)
print(y)
