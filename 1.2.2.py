#!/usr/bin/env python3

from itertools import combinations

# tableau à deux dimensions pour stocker les transactions
# les sous tableaux contiennent la taille du bloc et le pourboire
transactions = [
                  [2000, 13000],
                  [6000, 9000],
                  [800, 2000],
                  [700, 1500],
                  [1200, 3500],
                  [1000, 1800],
                  [1300, 5000],
                  [600, 1500],
              ]

max_satoshis = 0;
for i in range(1, len(transactions)+1):    
    for combinaison in combinations(transactions, i):
        octets = 0
        satoshis = 0        
        for transaction in combinaison:
            octets = octets + transaction[0]
            if (octets > 6000):
                break
            satoshis = satoshis + transaction[1]
        if (satoshis > max_satoshis):
            max_satoshis = satoshis
            best_combinaison = combinaison

print ("La meilleure combinaison est " + str(best_combinaison))
        


