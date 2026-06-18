import math
import random
from Crypto.Util.number import getPrime

# =====================================================================
# 1. GENERACIÓN DE CLAVES Y COPIADO A ARCHIVOS
# =====================================================================
def generar_claves_rsa(bits):
    """Genera el par de claves asegurando las condiciones de la práctica."""
    p = getPrime(bits)
    q = getPrime(bits)
    while p == q:
        q = getPrime(bits)
        
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi_n)
        if e not in (3, 65537) and math.gcd(e, phi_n) == 1:
            break
            
    d = pow(e, -1, phi_n)
    return (e, n), d

def guardar_claves_en_archivos(public_key, d):
    """Guarda la clave pública y privada en archivos txt separados."""
    e, n = public_key
    
    # Guardar clave pública (e y n en líneas separadas)
    with open("publica.txt", "w") as f:
        f.write(f"{e}\n{n}")
        
    # Guardar clave privada (d y n en líneas separadas)
    with open("privada.txt", "w") as f:
        f.write(f"{d}\n{n}")
        
    print("\n[+] Archivos de texto generados exitosamente:")
    print("    -> 'publica.txt' (Contiene e y n)")
    print("    -> 'privada.txt' (Contiene d y n)")

def menu_generar_claves():
    print("\n--- 1. Generación de Claves RSA ---")
    bits = int(input("Ingresa el tamaño de los primos en bits (32, 512, 2048): "))
    public_key, private_d = generar_claves_rsa(bits)
    
    print(f"\n[+] Clave Pública generada: (e={public_key[0]}, n={public_key[1]})")
    print(f"[+] Exponente Privado d generado: {private_d}")
    
    guardar_claves_en_archivos(public_key, private_d)


# =====================================================================
# 2. CIFRADO LEYENDO LA LLAVE PÚBLICA DESDE UN ARCHIVO
# =====================================================================
def cifrar_rsa_desde_archivo():
    print("\n--- 2. Cifrar Mensaje (TBC16) desde Archivo ---")
    archivo_pub = input("Nombre del archivo de clave pública a usar (ej. 'publica.txt'): ").strip()
    
    try:
        with open(archivo_pub, "r") as f:
            lineas = f.read().splitlines()
            e = int(lineas[0])
            n = int(lineas[1])
        print(f"[+] Clave pública cargada correctamente de {archivo_pub}")
    except FileNotFoundError:
        print(f"[-] Error: No se encontró el archivo '{archivo_pub}'.")
        return
    except Exception as err:
        print(f"[-] Error al procesar el archivo: {err}")
        return

    # Generar r aleatorio de 16 bits
    r = random.getrandbits(16)
    print(f"Número aleatorio de 16 bits generado (r): {r}")
    
    # Cifrar usando la clave pública: c = r^e mod n
    c = pow(r, e, n)
    print(f"Texto cifrado resultante (c): {c}")
    
    # Guardar el texto cifrado en un archivo para compartirlo fácilmente
    with open("cifrado.txt", "w") as f:
        f.write(str(c))
    print("[+] El texto cifrado se ha exportado a 'cifrado.txt'")


# =====================================================================
# 3. DESCIFRADO LEYENDO LA LLAVE PRIVADA DESDE UN ARCHIVO
# =====================================================================
def descifrar_rsa_desde_archivo():
    print("\n--- 3. Descifrar Mensaje desde Archivo ---")
    archivo_priv = input("Nombre del archivo de tu clave privada (por defecto 'privada.txt'): ").strip()
    
    try:
        with open(archivo_priv, "r") as f:
            lineas = f.read().splitlines()
            d = int(lineas[0])
            n = int(lineas[1])
        print(f"[+] Clave privada cargada correctamente de {archivo_priv}")
    except FileNotFoundError:
        print(f"[-] Error: No se encontró el archivo '{archivo_priv}'.")
        return
    except Exception as err:
        print(f"[-] Error al procesar el archivo: {err}")
        return

    # Opción de leer el criptograma desde archivo o consola
    opcion_c = input("¿Deseas leer el texto cifrado 'c' desde un archivo .txt? (s/n): ").strip().lower()
    if opcion_c == 's':
        archivo_c = input("Nombre del archivo cifrado (ej. 'cifrado.txt'): ").strip()
        try:
            with open(archivo_c, "r") as f:
                c = int(f.read().strip())
            print(f"[+] Texto cifrado cargada: c = {c}")
        except Exception as err:
            print(f"[-] Error al leer el archivo cifrado: {err}")
            return
    else:
        c = int(input("Ingresa el valor de 'c' manualmente: "))

    # Descifrar usando la clave privada: m = c^d mod n
    m = pow(c, d, n)
    print(f"\n[+] Mensaje original recuperado exitosamente (m): {m}\n")


# =====================================================================
# MENÚ INTERACTIVO PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    while True:
        print("====== LAB 13: RSA CON PERSISTENCIA EN TEXTO ======")
        print("1. Generar llaves y guardarlas en archivos (.txt)")
        print("2. Cifrar leyendo clave pública desde un archivo")
        print("3. Descifrar leyendo clave privada desde un archivo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            menu_generar_claves()
        elif opcion == '2':
            cifrar_rsa_desde_archivo()
        elif opcion == '3':
            descifrar_rsa_desde_archivo()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")