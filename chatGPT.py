import random

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Ambos números deben ser primos.")
    elif p == q:
        raise ValueError("Los números no pueden ser iguales.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

p = int(input("Introduce un número primo (17, 19, 23, etc.): "))
q = int(input("Introduce otro número primo distinto del anterior: "))
public, private = generate_keypair(p, q)

mensaje = input("Introduce un mensaje a encriptar: ")
cifrado = encrypt(public, mensaje)
print("Mensaje encriptado:", ''.join(map(lambda x: str(x), cifrado)))
print("Mensaje desencriptado:", decrypt(private, cifrado))
