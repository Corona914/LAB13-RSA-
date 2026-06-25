import math
import random
from Crypto.Util.number import getPrime

# --- 1.1 Generación de números primos ---
def generar_primos_prueba():
    print("--- 1.1 Números Primos Aleatorios ---")
    tamaños = [16, 32, 512, 2048]

    for size in tamaños:
        primo = getPrime(size)
        print(f"Primo de {size} bits: {primo}")

    print()


if __name__ == "__main__":
    generar_primos_prueba()