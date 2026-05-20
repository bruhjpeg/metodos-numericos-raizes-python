import time
import math

def f(x):
    return x - 1 / (1 + math.exp(-10 * x))


INTERVALO  = (0.0, 1.0)
TOLERANCIA = 1e-6
MAX_ITER   = 1000


def falsa_posicao(f, intervalo, tol, max_iter):

    a, b = intervalo

    fa = f(a)
    fb = f(b)

    # verifica mudança de sinal
    if fa * fb > 0:
        raise ValueError(
            "O intervalo não possui mudança de sinal.\n"
            "Escolha um intervalo onde f(a) * f(b) < 0."
        )

    historico = []

    inicio = time.perf_counter()

    for k in range(1, max_iter + 1):

        # fórmula da falsa posição
        x = (a * fb - b * fa) / (fb - fa)

        fx = f(x)

  
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        
        historico.append({
            "iterações": k,
            "a": a,
            "b": b,
            "x": x,
            "f(a)": fa,
            "f(b)": fb,
            "f(x)": fx
        })

       
        if abs(fx) < tol:
            break

    else:
        print(f"[aviso] Não convergiu em {max_iter} iterações.\n")

    tempo_ms = (time.perf_counter() - inicio) * 1000

    return x, k, historico, tempo_ms



raiz, n_iter, hist, tempo_ms = falsa_posicao(
    f,
    INTERVALO,
    TOLERANCIA,
    MAX_ITER
)


print("\n\n")

print("              Histórico de iterações do método da Falsa Posição:")
print("─" * 110)

print(f"{'Iter':<6}"
      f"{'a':<18}"
      f"{'b':<18}"
      f"{'x':<18}"
      f"{'f(a)':<18}"
      f"{'f(b)':<18}"
      f"{'f(x)':<18}")

print("─" * 110)

for h in hist:

    print(f"{h['iterações']:<6}"
          f"{h['a']:<18.8f}"
          f"{h['b']:<18.8f}"
          f"{h['x']:<18.8f}"
          f"{h['f(a)']:<18.8f}"
          f"{h['f(b)']:<18.8f}"
          f"{h['f(x)']:<18.8f}")

print("\n\n")



print("              Resultado final do método da Falsa Posição:")
print("─" * 70)

print(f"Raiz aproximada (x*)                    = {raiz:<.10f}")
print(f"f(x*)                                   = {f(raiz):.2e}")
print(f"Iterações                               = {n_iter}")
print(f"Tolerância                              = {TOLERANCIA:<.0e}")
print(f"Tempo de execução                       = {tempo_ms:<.4f} ms")

print("─" * 70)

print("\n\n")
