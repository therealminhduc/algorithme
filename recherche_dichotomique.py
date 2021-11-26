#la recherche dichotomique, methode recursive 
def r_dicho_recursive(e, tab, deb, fin):
	m = (deb + fin)	// 2
	
	if deb > fin : 
		return
	else : 
		if  tab[m] == e:
			indice = m
			while indice :
				indice = r_dicho_recursive(tab, e, deb, m-1) 
			return m
		elif tab[m] > e :
			return r_dicho_recursive(e, tab, deb, m-1)
		else : 
			return r_dicho_recursive(e, tab, m+1, fin)


tab = [2,5,9,14,20]
print(r_dicho_recursive(5, tab, 0, len(tab)-1))



'''
Complexite :

Dans le pire des cas : O(log2(n))

Cas moyen : log2(n)/2 = O(log2(n))

Meilleur cas : O(1)
''' 
