from random import *
import numpy as np
import matplotlib.pyplot as plt



d=2 # Dimention
n = [170, 170] #Taille des dimentions de Matrice
p=49 #Proportion de "1" dans la matrice

def creer_mat_perco(pourcent:int,n:list):
	l=len(n)
	if l > 1:
		M = [ creer_mat_perco(pourcent,n.copy()[0:l-2]) for i in range(n[l-1])]
	elif l=1:
		M = [0 for i in range(n[0])
		for i in range(n[0]):
			if randint(0,99)<pourcent:
				M[i] = 1
	return M

def creer_mat_adj(M, n:list):
	def prod_list(p: list):
		l = len(n)
		if l > 1: return n[l-1]*prod_list(n[0,l-2])
		else : return 1
	
	def adj_cases(M,v): # Trouve les coordoonées autour de celle choisie. Attention, len(v)=dim(M)
		def adj_cases_fixed(M,f,v): #Trouve les coordonnées autour de celles choisie, certaines coordonnées sont fixées.
			t = len(M)
			dim = len(v)
			dim_fixed = len(f)
			#Séparation du tenseur en lignes
			if(dim - dim_fixed > 1):
				if v[dim - dim_fixed - 1] == 0: return ([c for c in adj_cases_fixed(M,f.insert(-1,len(f) - 1),v)]).extend([c for c in adj_cases_fixed(M,f.insert(-1,len(f) - 1),v)])#début d'une ligne
				elif v[dim - dim_fixed - 1] == t - 1: return [c for c in adj_cases_fixed(M,f.insert(-1,len(f) - 1),v)] #Fin d'une ligne
				else: return ([c for c in adj_cases_fixed(M,f.insert(-1,len(f) - 1),v)]).extend([c for c in adj_cases_fixed(M,f.insert(1,len(f) - 1),v)]).extend([c for c in adj_cases_fixed(M,f.insert(,len(f) - 1),v)]) # milieu
			else: 
				if v[0] == 0: return [f.insert([-1,len(f) - 1]),f.insert([0,len(f) - 1]).]  #début d'une ligne
				elif v[0] == t - 1: return [f.insert([0,len(f) - 1])] #Fin d'une ligne
				else: return [f.insert([-1,len(f) - 1]),f.insert([0,len(f) - 1]),f.insert([1,len(f) - 1])] # milieu
		result = adj_cases_fixed(M,[],v).remove([0 for i in range(len(v)))
		return result
	def get_coord_num(c, n): #Avoir la numérotation d'une case d'une liste, c coord, n: vecteur dimention
		l = len(c)
		return sum([c[i]*(i==0 ? 1 : prod_list([n[0:i])) for i in range(l)]
	def find_coord_with_id(n,i): #retourne le vecteur coord en fonction de l'id de la case.
		return (len(n)>1 ? [i//prod_list(n[0:len(n)-1])].insert(find_coord_with_id(n[1:],i%prod_list(n[0:len(n)-1])): [i//n[0])[::-1]
	def find_coords_with_id(n,t):
		return [find_coord_with_id(n,i) for i in t]
	def access_coord(M,c): #accede la la coord. (x1,x2, ..., xn) du tenseur.
		
	def enumerate_mat(M,d): #retourne un vecteur constitué des valeurs de la matrice mise bout à bout.
		
	A=[[0 for i in range(prod_list(n)) ] for j in range(prod_list(n))]
	v=enumerate_mat(M,len(n))
	for i in len(v):
		for j in get_coord_num(adj_cases(M,find_coord_with_id(n,i)))
	
	return A

def calcul_chemins(A, p,xy1,xy2): # p: longueure du chemin
	chemins = []
	if p > 0 : 
		for i in range(len(A)):
			if A[xy1][i] == 1:
				for j in calcul_chemins(A, p-1, i, xy2):
					if j != []:
						chemins.append([xy1]+j)
		return chemins
	elif p==0 and xy1 == xy2:
		return [[xy1]]
	else : return [[]]

def calcul_nb_chemins(A, p, xy1,xy2):
	return (sum_matrix_power(A, p))[xy1,xy2]

def matrix_power(A,k):
	if k == 0: return np.diag([1]*len(A))
	if k == 1: return np.array(A)
	if k > 1: return np.dot(A,matrix_power(A,k-1))

def sum_matrix_power(A,k):
	if k == 0: return np.diag([1]*len(A))
	if k == 1: return np.add(np.array(A),np.diag([1]*len(A)))
	if k > 1: return np.add(matrix_power(A,k),sum_matrix_power(A,k-1))

def print_tab(T):
	for i in T:
		print("[ ",end='')
		for j in i:
			print(str(j)+" ",end='')
		print("]")


M = creer_mat_perco(p,n,n)
A = creer_mat_adj(M)

if n<10 or p<50:
	print("chemins possibles : ")
	print_tab(calcul_chemins(A,n-1,0,n*(n-1)))
else:
	print("nombres de chemins  : ")
	print(calcul_nb_chemins(A,n-1,0,n*(n-1)))

plt.figure()
plt.imshow(np.array(M))
plt.colorbar()
plt.show()

