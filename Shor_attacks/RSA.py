# Importa funciones necesarias
import random
import math
import time

# Función auxiliar para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Genera un número primo random
def generate_prime():
    while True:
        num = random.randint(10, 100)
        if is_prime(num):
            return num

# Calcula el inverso modular usando fuerza bruta
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Generación de claves RSA
p = generate_prime()
q = generate_prime()
while p == q:
    q = generate_prime()

n = p * q
phi = (p - 1) * (q - 1)

# Elige e tal que 1 < e < phi y gcd(e, phi) = 1
e = random.choice([3, 5, 7, 11, 13, 17, 19, 23])
while math.gcd(e, phi) != 1:
    e += 2  # Asegura que sea coprimo con phi

d = mod_inverse(e, phi)

print(f"RSA keys generated:")
print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d})")

# Encripta un mensaje usando RSA
def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

# Desencripta un mensaje usando RSA
def decrypt(ciphertext, d, n):
    return "".join([chr(pow(char, d, n)) for char in ciphertext])

message = "HELLO"
ciphertext = encrypt(message, e, n)

print(f"\nOriginal message: {message}")
print(f"Encrypted text: {ciphertext}")

input("\nPress ENTER to start brute force attack...")

# Ataque por fuerza bruta
print("\nStarting brute force attack...")
start_time = time.time()

found_key = False
for d_attempt in range(1, phi):  # Búsqueda de d por fuerza bruta
    print(f"Trying d = {d_attempt}", flush=True)
    time.sleep(0.005)
    if d_attempt == d:
        found_key = True
        break

end_time = time.time()
brute_force_time = end_time - start_time  # Guarda el tiempo del ataque

if found_key:
    print(f"\nBrute force attack: Key found! d = {d_attempt}")
else:
    print("\nBrute force attack: Key not found in range.")

print(f"Brute force attack took: {brute_force_time:.4f} seconds")

# Desencripta con la clave encontrada
decrypted_message = decrypt(ciphertext, d_attempt, n)
print(f"\nDecrypted message using brute force: {decrypted_message}")

# Simulación del algoritmo de Shor (Factorización de n)
print("\nPress ENTER to simulate Shor's algorithm...")
input()
print("\nSimulating Shor's algorithm...")

# Simulación basada en tamaño de n
bits_of_n = n.bit_length()
k = 0.000001  # Constante de simulación
shor_time = k * (bits_of_n ** 3)

# Resultado simulado
print(f"\nSimulated Shor’s Algorithm: Factors of n = {p} and {q}")
print(f"Private Key: d = {d}")
print(f"Shor's time = {k} * ({bits_of_n}^3) = {shor_time:.10f} seconds")
