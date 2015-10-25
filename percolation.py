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
	
	def adj_cases(M,c): # Trouve les coordoonées autour de celle choisie. Attention, len(v)=dim(M)
		def adj_cases_fixed(n,f_c,c): #Trouve les coordonnées des cases autour de celles choisie, certaines coordonnées sont fixées.
			dim = len(c)
			dim_fixed = len(f_c)
			#Séparation du tenseur en lignes
			if(dim - dim_fixed > 1):
				if c[dim - dim_fixed - 1] == 0: return ([a for a in adj_cases_fixed(n,f_c.insert(-1,len(f_c) - 1),c)]).extend([a for a in adj_cases_fixed(n,f_c.insert(-1,len(f) - 1),c)])#début d'une ligne
				elif c[dim - dim_fixed - 1] == n[dim - dim_fixed - 1] - 1: return [a for a in adj_cases_fixed(n,f_c.insert(-1,len(f_c) - 1),c)] #Fin d'une ligne
				else: return ([a for a in adj_cases_fixed(M,f_c.insert(-1,len(f_c) - 1),c)]).extend([a for a in adj_cases_fixed(n,f_c.insert(1,len(f_c) - 1),c)]).extend([a for a in adj_cases_fixed(n,f_c.insert(,len(f_c) - 1),c)]) # milieu
			else: 
				if c[0] == 0: return [f_c.insert([-1,len(f_c) - 1]),f_c.insert([0,len(f_c) - 1]).]  #début d'une ligne
				elif c[0] == n[0] - 1: return [f_c.insert([0,len(f_c) - 1])] #Fin d'une ligne
				else: return [f_c.insert([-1,len(f_c) - 1]),f_c.insert([0,len(f_c) - 1]),f_c.insert([1,len(f_c) - 1])] # milieu
		result = adj_cases_fixed(n,[],v).remove([0 for i in range(len(c)))
		return result
		
	def get_coord_id(c, n): #Avoir la numérotation d'une case d'une liste, c coord, n: vecteur dimention
		l = len(c)
		return sum([c[i]*(i==0 ? 1 : prod_list([n[0:i])) for i in range(l)]
	
	def access_coord(M,c): #accede la la coord. (x1,x2, ..., xn) du tenseur.
		return (len(n)>1 ? access_coord(M[c[len(c)-1]]], c[0:len(c)-2]) : M[c[0]])

	def enumerate_coord(n) # enumere toutes les coordonnées de la matrice M
		return (len(n)>1 ? [ [n[0].extend(i) for i in enumerate_mat(n[1:]) : [[i] in range(n[0]))
		
	A=[[0 for i in range(prod_list(n)) ] for j in range(prod_list(n))]
	
	for i in enumerate_coord(n):
		for j in adj_cases(M,i):
			if access_coord(M,j) == 1 and A[get_coord_id(j, n)][get_coord_id(i, n)]==0:
				 A[get_coord_id(i, n)][get_coord_id(j, n)]=1
			
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

