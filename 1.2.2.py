#!/usr/bin/env python3

def tri_a_bulles(transactions):
   for i in reversed(range(0,len(transactions))):
        tableau_trie = True
        for j in range(0,i):
            if (transactions[j+1][2] < transactions[j][2]):
                tmp = transactions[j]
                transactions[j] = transactions[j+1]
                transactions[j+1] = tmp
                tableau_trie = False
        if (tableau_trie):
            return transactions

# tableau à deux dimensions pour stocker les transactions
# les sous tableaux contiennent la taille du bloc, le pourboire ainsi qu'un ration indiquant la rentabilité d'une transaction
transactions = [
                  [2000, 13000, 0],
                  [6000, 9000, 0],
                  [800, 2000, 0],
                  [700, 1500, 0],
                  [1200, 3500, 0],
                  [1000, 1800, 0],
                  [1300, 5000, 0],
                  [600, 1500, 0],
              ]
# on parcours les transactions pour calculer leur ratio de rentabilité
for i in range(0,len(transactions)):
   transactions[i][2] = transactions[i][0] / transactions[i][1]
# On tri le tablea des transactions par rentabilité
transactions = tri_a_bulles(transactions)

print("Les meilleures transactions à inclure sont : ")
taille = 0
for i in range(0,len(transactions)):
   if (taille + transactions[i][0] <= 6000):
      taille = taille + transactions[i][0]
      print ("Taille : " + str(transactions[i][0]) + " Pourboire : " + str(transactions[i][1]))

