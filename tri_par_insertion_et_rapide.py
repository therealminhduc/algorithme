from math import *
	
#permet d'inserer des elements dans une array
tab = []

#preciser le nb d'element de la liste
n = int(input("Inserez le nb d'element dans une liste : "))
for i in range(0,n):
	ele=int(input())
	tab.append(ele)

'-----------------------------------------------------------------------' 
cpt1 = 0
cpt2 = 0 

#fonction de tri par insertion
def tri_par_insertion(tab):
 
	for i in range (1, len(tab)):
		index = tab[i]
		j = i - 1
		global cpt1
		cpt1 += 1  

		while j>=0 and index < tab[j] : 
			tab[j+1] = tab[j]
			j-=1
		tab[j+1] = index		
		global cpt2		
		cpt2 += 1


def insertion_croissant(tab, e):
	tab.append(5)
	i = len(tab) - 2
	while i>0 and tab[i] > e: 
		tab[i+1] = tab[i]
		i -= 1
	tab[i+1] = e

print(cpt1, cpt2) 

'-----------------------------------------------------------------------' 

#les elements qui sont les plus petits se situent vers la gauche et l'inverse

def partition(tab, deb, fin):
	x = (deb - 1)
	pivot = tab[fin]

	for y in range(deb, fin):
		if tab[y] <= pivot : 
			x = x + 1
			tab[x], tab[y] = tab[y], tab[x]
	tab[x+1], tab[fin] = tab[fin], tab[x+1]
	return (x+1)
   

#fonction de tri rapide 
def tri_rapide(tab, deb, fin):
		
	if deb < fin : 
		piv = partition(tab, deb, fin)
		tri_rapide(tab, deb, piv - 1) #partie gauche
		tri_rapide(tab, piv + 1, fin) #partie droite	
	

#programme test
tab = [28,2,34,12,16]
tri_par_insertion(tab)

print ("tri par insertion :")
for i in range(len(tab)): 
    print ("% d" % tab[i])

print("-------------------------------------")

print ("tri rapide : ")
tri_rapide(tab, 0, -1)
for i in range(len(tab)): 
    print ("% d" % tab[i])

'''
insertion_croissant(tab,e)
for i in range(len(tab)): 
    print ("% d" % tab[i]) 
'''





