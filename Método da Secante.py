import time
import math

def f(x):

    return (
        1 / math.sqrt(x)
        +
        2 * math.log10(
            (0.001 / 3.7)
            +
            (2.51 / (100000 * math.sqrt(x)))
        )
    )



X0         = 0.01
X1         = 0.05
TOLERANCIA = 1e-6
MAX_ITER   = 1000


def secante(f, x0, x1, tol, max_iter):

    if abs(x1 - x0) < 1e-15:
        raise ValueError(
            "Os pontos iniciais x0 e x1 devem ser diferentes."
        )

    fx0 = f(x0)
    fx1 = f(x1)

    historico = []

    inicio = time.perf_counter()

    for k in range(1, max_iter + 1):

        if abs(fx1 - fx0) < 1e-15:
            raise ZeroDivisionError(
                "Diferença f(x1) - f(x0) muito pequena.\n"
                "Escolha pontos iniciais diferentes."
            )

        # fórmula da secante
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        fx2 = f(x2)

        historico.append({
            "iterações": k,
            "x0": x0,
            "x1": x1,
            "x2": x2,
            "f(x0)": fx0,
            "f(x1)": fx1,
            "f(x2)": fx2
        })

        if (
            abs(fx2) < tol
            and abs(x2 - x1) < tol
        ):
            break

        x0, fx0 = x1, fx1
        x1, fx1 = x2, fx2

    else:
        print(f"[aviso] Não convergiu em {max_iter} iterações.\n")

    tempo_ms = (time.perf_counter() - inicio) * 1000

    return x2, k, historico, tempo_ms



raiz, n_iter, hist, tempo_ms = secante(
    f,
    X0,
    X1,
    TOLERANCIA,
    MAX_ITER
)


print("\n\n")

print("              Histórico de iterações do método da Secante:")
print("─" * 110)

print(f"{'Iter':<6}"
      f"{'x0':<18}"
      f"{'x1':<18}"
      f"{'x2':<18}"
      f"{'f(x0)':<18}"
      f"{'f(x1)':<18}"
      f"{'f(x2)':<18}")

print("─" * 110)

for h in hist:

    print(f"{h['iterações']:<6}"
          f"{h['x0']:<18.8f}"
          f"{h['x1']:<18.8f}"
          f"{h['x2']:<18.8f}"
          f"{h['f(x0)']:<18.8f}"
          f"{h['f(x1)']:<18.8f}"
          f"{h['f(x2)']:<18.8f}")

print("\n\n")



print("              Resultado final do método da Secante:")
print("─" * 70)

print(f"Raiz aproximada (x*)                    = {raiz:<.10f}")
print(f"f(x*)                                   = {f(raiz):.2e}")
print(f"Iterações                               = {n_iter}")
print(f"Tolerância                              = {TOLERANCIA:<.0e}")
print(f"Tempo de execução                       = {tempo_ms:<.4f} ms")

print("─" * 70)

print("\n\n")