import time
import math

# função:
def f(x):
    return x**3 - x - 2         

# derivada:
def df(x):
    h = 0.0001
    return (f(x + h) - f(x)) / h 

# parâmetros de partida:
INTERVALO   = (1.0, 2.0)         # ← (a, b) é ponto inicial = centro do intervalo
TOLERANCIA  = 1e-6               # ← critério de parada  (ex: 1e-6, 1e-8, 1e-12)
MAX_ITER    = 1000               # ← para evitar loops infinitos 

# função que aplica o método de Newton
def newton_raphson(f, df, intervalo, tol, max_iter):
    a, b = intervalo
    x = (a + b) / 2.0          

    historico = []

    inicio = time.perf_counter()

    for k in range(1, max_iter + 1):
        fx  = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-14:
            raise ZeroDivisionError(
                f"Derivada nula em x = {x:.6f}. "
                "Escolha outro ponto inicial ou verifique a função."
            )

        x_novo = x - fx / dfx
        
        historico.append({
            "iterações":  k,
            "x":     x,
            "f(x)":  fx,
            "f'(x)": dfx,
            "x_novo": x_novo,
        })

        # critério de parada
        if abs(x_novo - x) < tol:
            x = x_novo
            break

        x = x_novo
    else:
        # caso não consiga convergir no meu limite máximo de interações
        print(f"[aviso] Não convergiu em {max_iter} iterações.\n")

    tempo_ms = (time.perf_counter() - inicio) * 1000

    # retorna a variável final, o número de interações, o histórico das interações e o tempo.
    return x, k, historico, tempo_ms

# chamando a função 
raiz, n_iter, hist, tempo_ms = newton_raphson(
    f, df, INTERVALO, TOLERANCIA, MAX_ITER
)

# imprimindo a tabela de interações
print("\n\n")
print("          Histórico de iterações do método Newton-Raphson:")
print("  " + "─" * 64)
print(f"  {'Iter':>4}  {'xₙ':>14}  {'f(xₙ)':>14}  {'f\'(xₙ)':>12}  {'xₙ₊₁':>14}")
print("  " + "─" * 64)

for h in hist:
    dfx_val = h["f'(x)"]
    print(f" {h['iterações']:>4}  {h['x']:>14.8f}  {h['f(x)']:>14.8f}"
          f" {dfx_val:>12.6f}  {h['x_novo']:>14.8f}")

print("\n\n")

# imprimindo o resultado final
print("\n             Resultado final do método Newton-Raphson:")
print("─" * 66)
print(f"Raiz aproximada (x*)                               =  {raiz:<.10f}")
print(f"f(x*)                                              =  {f(raiz):.2e}")
print(f"Iterações                                          =  {n_iter}")
print(f"Tolerância                                         =  {TOLERANCIA:<.0e}")
print(f"Tempo de execução                                  =  {tempo_ms:<.4f} ms")
print("─" * 66)
print("\n\n")
