# Nome: Newton-Raphson Multivariável
# O que faz? Encontrar o vetor X que zera um sistema de equações F(X)
# Qual caminho aborda? Usa a Jacobiana para corrigir todas as variáveis ao mesmo tempo

# Recomendação:
# Sistema não linear com variáveis acopladas
# Jacobiana conhecida
# Bom chute inicial
# Preciso de rapidez

# Não recomendado:
# Jacobiana difícil ou inexistente
# Sistema instável
# Mau chute inicial
# Pode divergir

# Como funciona?
# 1 - Escolha um chute inicial X0
# 2 - Calcule F(X)
# 3 - Calcule J(X)
# 4 - Resolva: J * dX = -F
# 5 - Atualize: X_novo = X + dX
# 6 - Parar quando ||dX|| < tolerancia


import numpy as np


def newton_multivariavel(F, J, X0, tolerancia=1e-6, max_iter=100):
    # F = função vetorial, J = jacobiana, X0 = chute inicial

    X = np.array(X0, dtype=float)

    for i in range(max_iter):

        FX = F(X)
        JX = J(X)

        try:
            dX = np.linalg.solve(JX, -FX)
        except:
            raise ValueError("Jacobiana singular. Método falhou.")

        X_novo = X + dX

        erro = np.linalg.norm(dX)

        if erro < tolerancia:
            return {
                "raiz": X_novo,
                "iteracoes": i + 1,
                "erro": erro
            }

        X = X_novo

    return {
        "raiz": X,
        "iteracoes": max_iter,
        "erro": erro
    }


# ---------------------------
# EXEMPLO DE USO
# ---------------------------

# Sistema de equações
def F(X):
    x, y = X
    return np.array([
        x**2 + y**2 - 4,
        x - y - 1
    ])


# Jacobiana
def J(X):
    x, y = X
    return np.array([
        [2*x, 2*y],
        [1,   -1]
    ])


# Chute inicial
X0 = [1.5, 0.5]


# Chamada do método
resultado = newton_multivariavel(F, J, X0, tolerancia=1e-6, max_iter=100)


# Resultados
print("\n--- RESULTADOS ---")

raiz = resultado["raiz"]
iteracoes = resultado["iteracoes"]
erro = resultado["erro"]

print("Solução:", raiz)
print("Número de iterações:", iteracoes)
print("Erro final:", erro)