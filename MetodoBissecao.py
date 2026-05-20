import math
import time

def f(x):
    #return FUNÇÃO DE TESTE
   return x**3 - 9*x + 3

def bissecao(f, a, b, tolerancia=1e-3, max_iter=100): #EDITAR TOLERÂNCIA
    if f(a) * f(b) >= 0:
        raise ValueError(
            "Não há mudança de sinal no intervalo."
        )
 
    inicio = time.perf_counter()

    fa = f(a)
   
    raiz = (a + b) / 2
  
    for n_iter in range(1, max_iter + 1):
       
        raiz = (a + b) / 2
     
        f_raiz = f(raiz)
        if (
            abs(f_raiz) < tolerancia
            or abs(b - a) / 2 < tolerancia
        ):
            break                               
        if fa * f_raiz < 0:
            b = raiz
        else:
            a = raiz
            fa = f_raiz                            
  
    fim = time.perf_counter()
   
    tempo_ms = (fim - inicio) * 1000

    return raiz, n_iter, tempo_ms

#Intervalo [A, B] e tolerância 
A = 0
B = 1
TOLERANCIA = 1e-3

raiz, n_iter, tempo_ms = bissecao(
    f,
    A,
    B,
    TOLERANCIA
)

#RESPOSTAS COM 10 CASAS DECIMAIS 
print("─" * 66)
print(f"Raiz aproximada (x*)                               =  {raiz:.10f}")
print(f"f(x*)                                              =  {f(raiz):.10f}")
print(f"Iterações                                          =  {n_iter}")
print(f"Tolerância                                         =  {TOLERANCIA:.2e}")
print(f"Tempo de execução                                  =  {tempo_ms:.4f} ms")
print("─" * 66)

