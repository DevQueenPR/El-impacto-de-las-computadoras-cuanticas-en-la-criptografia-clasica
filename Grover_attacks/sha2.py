from Cryptodome.Hash import SHA3_256
import itertools
import time
import random
import math

# Función para calcular SHA3-256
def hash_sha3_256(data):
    hasher = SHA3_256.new()
    hasher.update(data)
    return hasher.digest()

# Función de fuerza bruta con clave de 2 bytes
def brute_force_attack_2bytes(target_hash, plaintext):
    start_time = time.time()
    input("Press Enter to start brute force attack...")  # Mensaje para iniciar ataque
    for count, key_tuple in enumerate(itertools.product(range(256), repeat=2)):
        key = bytes(key_tuple)
        print(f'Trying key: {key.hex()}')  # Mostrar clave probada
        test_hash = hash_sha3_256(key + plaintext)
        if test_hash == target_hash:
            end_time = time.time()
            return key, count + 1, end_time - start_time
    return None, count + 1, time.time() - start_time

# Simulación de Grover (teórico)
def grover_simulation(classical_time):
    quantum_time = math.sqrt(classical_time)
    return quantum_time

# Definir mensaje de prueba
plaintext = b'Hello, world!'

# Generar clave aleatoria de 2 bytes
random_key = bytes([random.randint(0, 255), random.randint(0, 255)])
print(f'Generated key (hidden): {random_key.hex()}')

# Calcular hash con SHA3-256
target_hash_sha3_256 = hash_sha3_256(random_key + plaintext)
print(f'SHA3-256 Hash: {target_hash_sha3_256.hex()}')

# Ejecutar ataque de fuerza bruta para SHA3-256
found_key, attempts, elapsed_time = brute_force_attack_2bytes(target_hash_sha3_256, plaintext)
quantum_time = grover_simulation(elapsed_time)

# Mostrar resultados
if found_key:
    print(f'Brute-force SHA3-256 succeeded! Key found: {found_key.hex()} in {elapsed_time:.4f} seconds after {attempts} attempts')
    print(f'Grover’s Algorithm Simulation: Estimated quantum time {quantum_time:.4f} seconds')
else:
    print('Brute-force attack on SHA3-256 failed to find the key')
