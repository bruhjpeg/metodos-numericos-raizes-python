# Métodos Numéricos para o Cálculo de Raízes

> **Cálculo Numérico | Seminário 1 | UFPB — CI**  
> Professor: Moises Dantas dos Santos
> Alunas: Maria Vitória de Holanda, Jennifer Freire, Bruna Aquino e Gabriella Xavier
> Curso: Engenharia da Computação

---

Implementações didáticas em Python dos principais métodos numéricos para encontrar raízes de funções reais, usando Bisseção, Falsa Posição, Newton-Raphson e Secante. Este projeto é voltado para o primeiro seminário da disciplina de Cálculo Numérico, aplicando os conhecimos em algoritmos implementados com os métodos que resolvem problemas da realidade.

## Métodos Implementados

### 1. Método da Bisseção
**Arquivo:** `MetodoBissecao.py`

**Teoria:**
- Baseado no Teorema de Bolzano
- Requer um intervalo `[a, b]` onde `f(a) * f(b) < 0`
- A cada iteração, o intervalo é dividido ao meio

**Fórmula principal:**
x = (a + b) / 2

---

### 2. Método da Falsa Posição (Regula Falsi)
**Arquivo:** `MetodoFalsaPosicao.py`

**Teoria:**
- Similar à bisseção, mas usa interpolação linear
- Mantém o intervalo onde ocorre a troca de sinal
- Converge mais rápido que a bisseção em muitos casos

**Fórmula principal:**
x = (a * f(b) - b * f(a)) / (f(b) - f(a))

---

### 3. Método de Newton-Raphson
**Arquivo:** `NewtonRaphson.py`

**Teoria:**
- Usa a derivada da função para encontrar a raiz
- Requer um chute inicial `x₀`
- Convergência quadrática (muito rápida) quando funciona bem

**Fórmula principal:**
x_{n+1} = x_n - f(x_n) / f'(x_n)


---

### 4. Método da Secante
**Arquivo:** `Secante.py`

**Teoria:**
- Versão do Newton-Raphson sem necessidade de derivada
- Usa dois pontos iniciais e aproxima a derivada por diferenças finitas
- Boa alternativa quando `f'(x)` é difícil de calcular

**Fórmula principal:**
x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

---

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (apenas `time`, que é nativa)

---

## Saída dos programas

- Histórico de interações
- A raiz aproximada
- O valor de f(raiz)
- O número total de interações
- O tempo total de execução em (ms)



## Como Executar

```bash
python MetodoBissecao.py
python MetodoFalsaPosicao.py
python NewtonRaphson.py
python Secante.py

Scripts:
- `MetodoBissecao.py` — método da bisseção
- `MetodoFalsaPosicao.py` — falsa posição (regula falsi)
- `NewtonRaphson.py` — Newton–Raphson
- `Secante.py` — método da secante

Requisitos: Python 3.8+

Execução:

```bash
python "MetodoBissecao.py"
python MetodoFalsaPosicao.py
python NewtonRaphson.py
python Secante.py
```

Personalize a função `f(x)` e os parâmetros (intervalo, tolerância, iterações) no início de cada script.

Feito para fins didáticos — para produção, adicione validações e testes.

