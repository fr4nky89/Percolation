from random import *
import numpy as np
import matplotlib.pyplot as plt



def creer_mat_perco(pourcent:int,n:int,m:int):
	M=[[0 for j in range(m)] for i in range(n)]
	for i in range(n):
		for j in range(m):
			if randint(0,99)<pourcent:
				M[i][j] = 1
	return M

def creer_mat_adj(M):
	n , m= len(M), len(M[0])
	A=[[0 for i in range(n*m) ] for j in range(n*m)]
	for i in range(n):
		for j in range(m):
			if M[i][j] == 1:
				if j==0 and i<n-1:
					if M[i+1][j] == 1 and A[(i+1)*m+j][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j] = 1
					if M[i+1][j+1] == 1 and A[(i+1)*m+j+1][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j+1] = 1
					if M[i][j+1] == 1 and A[(i)*m+j+1][i*m+j]==0: 
						A[i*m+j][(i)*m+j+1] = 1
				if j== n-1 and i < n-1:
					if M[i][j-1] == 1 and A[i*m+j-1][i*m+j]==0: 
						A[i*m+j][i*m+j-1] = 1
					if M[i+1][j-1] == 1 and A[(i+1)*m+j-1][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j-1] = 1
					if M[i+1][j] == 1 and A[(i+1)*m+j][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j] = 1
				if j < m-1 and j > 0 and i < n-1:
					if M[i][j-1] == 1 and A[i*m+j-1][i*m+j]==0: 
						A[i*m+j][i*m+j-1] = 1
					if M[i+1][j-1] == 1 and A[(i+1)*m+j-1][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j-1] = 1
					if M[i+1][j] == 1 and A[(i+1)*m+j][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j] = 1
					if M[i+1][j+1] == 1 and A[(i+1)*m+j+1][i*m+j]==0: 
						A[i*m+j][(i+1)*m+j+1] = 1
					if M[i][j+1] == 1 and A[i*m+j+1][i*m+j]==0: 
						A[i*m+j][i*m+j+1] = 1

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

n= 170
p=49
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

