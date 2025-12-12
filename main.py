import math

def calcular_quadrado(lado, unidade):
    """
    Calcula a metade da diagonal de um quadrado (distância do centro ao vértice)
    """
    if lado <= 0:
        return "O comprimento do lado deve ser um número positivo."

    # 1. Calcular a Diagonal (D): D = L * sqrt(2)
    # Pelo Teorema de Pitágoras: D² = L² + L² -> D² = 2*L² -> D = L * sqrt(2)
    diagonal = lado * math.sqrt(2)

    # 2. O "Raio" é metade da Diagonal (R = D / 2)
    raio = diagonal / 2

    print(f"\n--- Resultado ---")
    print(f"Lado (L): {lado} {unidade}")
    print(f"Diagonal (D): {diagonal:.4f} {unidade}")
    print(f"**'Raio' (Metade da Diagonal): {raio:.4f} {unidade}**")
    print("-" * 17)
    return raio

# --- Execução do Programa ---

try:
    # Solicita o lado do quadrado e a unidade
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    unidade = input("Digite a unidade de medida (ex: metros, km): ").strip()

    # Chama a função de cálculo
    calcular_quadrado(lado, unidade)

except ValueError:
    print("\nErro: O comprimento do lado deve ser um número válido (ex: 5, 10.5).")
