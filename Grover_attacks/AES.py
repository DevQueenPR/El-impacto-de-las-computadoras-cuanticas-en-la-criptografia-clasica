from Cryptodome.Cipher import AES
import itertools
import time
import random
import math

# Función para rellenar con PKCS7
def pad_pkcs7(data, block_size=16):
    padding_length = block_size - (len(data) % block_size) #Aplica el módulo para encontrar cuántos bytes tiene la data y luego aplicarle el relleno
    return data + bytes([padding_length] * padding_length) #Crea una lista con los bytes generados y retorna el mensaje

# Función para eliminar el padding PKCS7
def unpad_pkcs7(data):
    padding_length = data[-1] #obtiene el último byte del mensaje (que indica cuánto padding hay)
    return data[:-padding_length] #elimina los bytes de padding

# Función para cifrar con AES en modo ECB
def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad_pkcs7(plaintext)
    return cipher.encrypt(padded_plaintext)

# Función para descifrar con AES en modo ECB
def decrypt_message(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad_pkcs7(decrypted)

# Función de fuerza bruta con clave de 2 bytes
def brute_force_attack_2bytes(ciphertext, plaintext):
    input("Press Enter to start brute force attack...")  # Mensaje para iniciar ataque
    start_time = time.time()  # Iniciar temporizador
    for count, key_tuple in enumerate(itertools.product(range(256), repeat=2)):  # 2 bytes (16 bits)
        key = bytes(key_tuple) + b'\x00' * 14  # Completar a 16 bytes
        print(f'Trying key: {key.hex()}')  # Mostrar clave probada
        
        try:
            decrypted_text = decrypt_message(key, ciphertext)
            if decrypted_text == plaintext:
                end_time = time.time()  # Tiempo de finalización
                return key, count + 1, end_time - start_time  # Devolver clave, intentos y tiempo
        except ValueError:
            continue  # Ignorar errores de padding

    return None, count + 1, time.time() - start_time  # Si no se encuentra la clave

# Simulación de Grover (teórico)
def grover_simulation(classical_time):
    quantum_time = math.sqrt(classical_time)
    return quantum_time

# Definir mensaje de prueba
plaintext = b'Hello, world!'

# Generar clave aleatoria de 2 bytes
random_key = bytes([random.randint(0, 255), random.randint(0, 255)]) + b'\x00' * 14
print(f'Generated key (hidden): {random_key[:2].hex()}')  # Mostrar la clave generada

# Cifrar el mensaje con la clave aleatoria
ciphertext = encrypt_message(random_key, plaintext)
print(f'Ciphertext: {ciphertext.hex()}')

# Ejecutar ataque de fuerza bruta
found_key, attempts, elapsed_time = brute_force_attack_2bytes(ciphertext, plaintext)

# Simular Grover
quantum_time = grover_simulation(elapsed_time)

# Mostrar resultados
if found_key:
    print(f'Brute-force succeeded! Key found: {found_key[:2].hex()} in {elapsed_time:.4f} seconds after {attempts} attempts')
    print(f'Decrypted message: {plaintext.decode()}')
    print(f'Grover’s Algorithm Simulation: Estimated quantum time {quantum_time:.4f} seconds (sqrt speedup)')
else:
    print('Brute-force attack failed to find the key')
