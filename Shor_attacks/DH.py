import random
import time

# Función para verificar si un número es generador
def is_generator(g, p):
    return len(set(pow(g, i, p) for i in range(1, p))) == p - 1

# Función para generar un número primo dentro de un rango
def generate_prime():
    primes = [i for i in range(20, 100) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    return random.choice(primes)

# Función para encontrar un generador
def find_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g
    return None

# Generación de parámetros públicos
p = generate_prime()  # Número primo
while True:
    g = find_generator(p)
    if g:
        break

# Claves privadas
alice_private = random.randint(1, p - 1)
bob_private = random.randint(1, p - 1)

# Claves públicas
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Imprimir la clave privada de Alice antes de la primera entrada
print(f"Alice's Private Key: {alice_private}")
print(f"Generated Diffie-Hellman keys:")
print(f"Public Parameters: p = {p}, g = {g}")
print(f"Alice's Public Key: A = {alice_public}")
print(f"Bob's Public Key: B = {bob_public}")

input("\nPress ENTER to start brute force attack...")

# Ataque por fuerza bruta (probando todas las claves privadas posibles)
print("\nStarting brute force attack...")
start_time = time.time()

found_key = False
for attempt in range(1, p):
    generated_A = pow(g, attempt, p)  # Cálculo de la clave pública de Alice
    print(f"Trying private key = {attempt} (Expected: {alice_public}, Got: {generated_A})")
    time.sleep(0.005)  # Pequeña demora para visibilidad
    if generated_A == alice_public:
        found_key = True
        break

end_time = time.time()
brute_force_time = end_time - start_time  # Guarda el tiempo del ataque

if found_key:
    print(f"\nBrute Force Attack: Key found! Private Key = {attempt}")
else:
    print("\nBrute Force Attack: Key not found within range.")

print(f"Brute Force took: {brute_force_time:.4f} seconds")

# Simulación del algoritmo de Shor
print("\nPress ENTER to simulate Shor’s Algorithm...")
input()
print("\nSimulating Shor’s Algorithm...")

# Calcular y formatear el tiempo de Shor's Algorithm
shor_time = brute_force_time / 1_000_000  # Dividir el tiempo de fuerza bruta por 1,000,000
print(f"\nSimulated Shor’s Algorithm: Private Key = {alice_private}")
print(f"Shor's time= {brute_force_time:.4f} / 1,000,000 = {shor_time:.10f} seconds")
