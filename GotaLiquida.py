# Este Script calcula la masa de un nucleo utilizando la formula Semiempirica de Bethe-W.
# Atte: F. Perez-Ramirez.

a1 = 14.1	#MeV
a2 = 13 #MeV
a3 = 0.595	#MeV
a4 = 19	#MeV
a5 = 33.5  #MeV
mp = 939.565
mn = 938.272
uma = 931.49
# Los coeficientes anteriores pertenecen a  Wapstra, A. H. (1958)." Atomic Masses of Nuclides" y pueden consultarse en wikipedia.

Z = input("Numero Atomico: \n")
A = input("Numero de Nucleones \n")
E = input("Masa Experimental \n")


def B (P, N):
	Vol = - a1*N
	Sup = N**(2.0/3.0)
	Col = a3 * (P**2) / (N**(1.0/3.0))
	Sim = a4 *((N - 2*P)**2) /N
	
	if (P+N)%2 != 0:
		Par = 0
	if P%2 == 0 and N%2 == 0:
		Par = - a5 * (N**(-3.0/4.0))
	else:
		Par =  a5 * (N**(-3.0/4.0))
	return (Vol + Sup + Col + Sim + Par)

Masa = Z*mp + (A-Z)*mn + B(Z,A)
print "******************************************"
print "*   M =  %2.4f MeV.		**"%Masa            
print "*   M =  %2.4f uma.			**"% (Masa/ uma)
print "* B.E =  M(A,Z) - %2.4f MeV	**"%(Z*mp + (A-Z)*mn) 
print " Diferencia Exp. : %2.4f, Porcentaje: %2.4f"%( abs(E-Masa), abs(E-Masa)*100/Masa)
print "******************************************"



