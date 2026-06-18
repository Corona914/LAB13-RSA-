import math
import random
from Crypto.Util.number import getPrime

# --- 1.1 Generación de números primos  ---
def generar_primos_prueba():
    print("--- 1.1 Números Primos Aleatorios ---")
    tamaños = [16, 32, 512, 2048]
    for size in tamaños:
        # Genera un número primo para cada tamaño especificado [cite: 10, 11, 12, 13, 14]
        primo = getPrime(size)
        print(f"Primo de {size} bits: {primo}")
    print("\n")

# --- 1.2 Generación de claves para Schoolbook RSA [cite: 16] ---
def generar_claves_rsa(bits):
    """
    Recibe como parámetro el tamaño en bits de los números primos[cite: 19].
    """
    # Ambos primos del mismo tamaño pero diferentes 
    p = getPrime(bits)
    q = getPrime(bits)
    while p == q:
        q = getPrime(bits)
        
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Elegir 'e' al azar [cite: 22]
    while True:
        e = random.randrange(2, phi_n)
        # NO usar e=3 o e=65537, y comprobar que gcd(e, phi(n)) == 1 
        if e not in (3, 65537) and math.gcd(e, phi_n) == 1:
            break
            
    # Función de Python (pow) para encontrar el inverso multiplicativo de e 
    d = pow(e, -1, phi_n)
    
    return (e, n), d

def prueba_generacion_claves():
    print("--- 1.2 Generación de Claves RSA ---")
    bits = int(input("Ingresa el tamaño de los primos en bits (ej. 32, 512, 2048)[cite: 20]: "))
    public_key, private_d = generar_claves_rsa(bits)
    
    print("\n[+] Claves generadas exitosamente:")
    print(f"Clave Pública (e, n): {public_key}") # Imprimir clave pública [cite: 25]
    print(f"Exponente Privado d: {private_d}\n")   # Imprimir exponente privado [cite: 26]

    # --- 2.2 Cifrado usando RSA [cite: 31] ---
def cifrar_rsa():
    print("--- 2.2 Cifrar Mensaje (TBC16) ---")
    # a) Pedir al usuario la clave pública (e, n) [cite: 33]
    e = int(input("Ingresa la clave pública 'e': "))
    n = int(input("Ingresa la clave pública 'n': "))
    
    # b) Generar número r aleatorio de 16 bits e imprimirlo [cite: 34]
    r = random.getrandbits(16)
    print(f"\nNúmero aleatorio generado (r): {r}")
    
    # c) Cifrar r: c = r^e mod n [cite: 36]
    c = pow(r, e, n)
    # Imprimir el valor de c como entero [cite: 37]
    print(f"Texto cifrado (c): {c}\n")

# --- 2.3 Descifrado usando RSA [cite: 38] ---
def descifrar_rsa():
    print("--- 2.3 Descifrar Mensaje ---")
    # a) Pedir al usuario la clave privada d y n [cite: 41]
    d = int(input("Ingresa tu exponente privado 'd': "))
    n = int(input("Ingresa el módulo 'n': "))
    
    # b) Pedir al usuario el valor de c [cite: 42]
    c = int(input("Ingresa el texto cifrado 'c' a descifrar: "))
    
    # c) Descifrar c: m = c^d mod n [cite: 43]
    m = pow(c, d, n)
    
    # Imprimir el valor recuperado [cite: 44]
    print(f"\nMensaje descifrado (m): {m}\n")

    
if __name__ == "__main__":
    while True:
        print("====== PRÁCTICA 13: SCHOOLBOOK RSA ======")
        print("1. Imprimir números primos aleatorios (16, 32, 512, 2048 bits)")
        print("2. Generar par de claves RSA")
        print("3. Cifrar un mensaje")
        print("4. Descifrar un mensaje")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            generar_primos_prueba()
        elif opcion == '2':
            prueba_generacion_claves()
        elif opcion == '3':
            cifrar_rsa()
        elif opcion == '4':
            descifrar_rsa()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")