
V=[]#Original array with file data
P=[]#array del segundo Algoritmo
Max=[]#array para los indices
Orden=[]#Lo uso para el output 
def leer():
        filename=input("Dime el nombre del Archivo (.txt) ")
        
        with open(filename) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        V.append(int(line))
                print(V)

leer()
n=V[0]
A=[0]*n
#Parte 1 del Programa 1/2
def wis():#El algoritmo 1 lo que hara es elegir entre el vertice penultimo o el  vertice ultimo vertice 
    
    
    #A=[0]
    A[1]=V[1]
    print(A)
    for i in range(2, n):
        A[i]=max(A[i-1],A[i-2]+V[i]) #Aqui se elegira los Maximum IS
    print(A)

wis()#Llamada al algoritmo 1

def recon_algo(): #Este algoritmo Estara Imprimiendo los Maximum Independent sets que luego se sumaran en la funcion suma 
    
    i=n
    while(i>0):
        if (A[i-2] + V[i]>=A[i-1]):   
            P.append(V[i])
            Max.append(i)
            i=i-2
        else: 
            i = i-1

    print(P)
    
recon_algo()



def suma(arr):  #This function 
    sum=0
    for i in P:
       sum = sum + i
       print(i) 

    return(sum) 

n = len(P) 
ans = suma(P) 

Orden = Max[::-1] #Ascendiente el Array 
print ('Sum of Maximum Weight Independent Set ', ans) # Suma de Los pesos 
print ('Maximum Weight Independent Set Vertices  : ',Orden)  #Los Verices que se utilizaron para encontrar la suma