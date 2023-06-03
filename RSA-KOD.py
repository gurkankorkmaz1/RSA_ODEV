import time


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd == 1:
        return x % m, m


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(public_key, message):
    e, n = public_key
    encrypted = pow(message, e, n)
    return encrypted


def decrypt(private_key, encrypted_message):
    d, n = private_key
    decrypted = pow(encrypted_message, d, n)
    return decrypted


# Örnek p ve q değerleri
p = 10691097123712491259
q = 44444444443333332221

# Anahtar çiftini oluştur
public_key, private_key = generate_keypair(p, q)
n = public_key[1]
q_n = (p - 1) * (q - 1)

# Açık Anahtar (E) değerini al
e = int(input("Açık Anahtar (E) değerini girin: "))
public_key = (e, n)

# Gizli anahtarı hesapla
d_start_time = time.perf_counter()
private_key = mod_inverse(public_key[0], q_n)
d_end_time = time.perf_counter()
d_time = d_end_time - d_start_time

# Gizli anahtarı yazdır
print("Gizli Anahtar (D):", private_key)

# Şifrelenecek sayıyı al
message = int(input("Şifrelenecek sayıyı girin: "))

# Şifreleme işlemi
encryption_start_time = time.perf_counter()
encrypted_message = encrypt(public_key, message)
encryption_end_time = time.perf_counter()
encryption_time = encryption_end_time - encryption_start_time

# Şifreli metni yazdır
print("Şifreli metin:", encrypted_message)

# Şifre çözme işlemi
decryption_start_time = time.perf_counter()
decrypted_message = decrypt(private_key, encrypted_message)
decryption_end_time = time.perf_counter()
decryption_time = decryption_end_time - decryption_start_time

# Süreleri saniye cinsinden yazdır
print("Gizli Anahtar Hesaplama Süresi (D Time):", '{:.8f}'.format(d_time), "saniye")
print("Şifreleme Süresi:", '{:.8f}'.format(encryption_time), "saniye")
print("Deşifreleme Süresi:", '{:.8f}'.format(decryption_time), "saniye")
