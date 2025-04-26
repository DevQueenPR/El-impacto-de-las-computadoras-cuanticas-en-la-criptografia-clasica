import random
import time

# Define parámetros de la curva elíptica
class EllipticCurve:
    def __init__(self, a, b, p, G, n):
        self.a = a  # Parámetro de la curva a
        self.b = b  # Parámetro de la curva b
        self.p = p  # Módulo primo
        self.G = G  # Punto generador (x, y)
        self.n = n  # Orden del grupo

# Curva pequeña de ejemplo (No segura, solo para simulación educativa)
curve = EllipticCurve(
    a=2,
    b=3,
    p=97,
    G=(3, 6),
    n=101
)

# Generación de claves ECC
private_key = random.randint(1, curve.n - 1)
public_key = (private_key * curve.G[0] % curve.p, private_key * curve.G[1] % curve.p)

print(f"Generated ECC keys:")
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

input("\nPress ENTER to start brute force attack...")

# Ataque por fuerza bruta (Probando todas las posibles claves privadas)
print("\nStarting brute force attack...")
start_time = time.time()

found_key = False
for attempt in range(1, curve.n):  # Búsqueda de clave privada por fuerza bruta
    generated_point = (attempt * curve.G[0] % curve.p, attempt * curve.G[1] % curve.p)
    print(f"Trying private key = {attempt}", flush=True)  # Imprime cada intento
    time.sleep(0.005)  # Pequeña demora para visibilidad
    if generated_point == public_key:
        found_key = True
        break

end_time = time.time()
brute_force_time = end_time - start_time  # Guarda el tiempo del ataque por fuerza bruta

if found_key:
    print(f"\nBrute Force Attack: Key found! Private Key = {attempt}")
else:
    print("\nBrute Force Attack: Key not found within range.")

print(f"Brute Force took: {brute_force_time:.4f} seconds")

# Simulación del algoritmo de Shor
print("\nPress ENTER to simulate Shor’s Algorithm...")
input()
print("\nSimulating Shor’s Algorithm...")

# Ajuste de simulación de Shor basado en los bits del módulo primo
bits_of_p = curve.p.bit_length()
k = 0.000001  # Ajuste para hacer el tiempo razonable en la simulación
shor_time = k * (bits_of_p ** 3)

# Resultado simulado
print(f"\nSimulated Shor’s Algorithm: Private Key = {private_key}")
print(f"Shor's time = {k} * ({bits_of_p}^3) = {shor_time:.10f} seconds")
