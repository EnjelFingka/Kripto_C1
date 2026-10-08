import hashlib
import os

password_asli = "Password123"

def buat_hash_sha256(teks):
    return hashlib.sha256(teks.encode()).hexdigest()

def buat_hash_pbkdf2(teks, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        teks.encode(),
        salt,
        200000
    )

hash_biasa = buat_hash_sha256(password_asli)

salt = os.urandom(16)
hash_aman = buat_hash_pbkdf2(password_asli, salt)

print("=== SHA-256 LANGSUNG ===")
print("Password :", password_asli)
print("Hash     :", hash_biasa)

print("\n=== PBKDF2 + SALT ===")
print("Salt     :", salt.hex())
print("Hash     :", hash_aman.hex())

password_login = input("\nMasukkan password: ")

if buat_hash_pbkdf2(password_login, salt) == hash_aman:
    print("Login berhasil")
else:
    print("Password salah")

print("\n=== COBA TEBAK PASSWORD ===")

daftar_tebakan = [
    "123456",
    "admin",
    "password",
    "Password123",
    "qwerty"
]

for tebakan in daftar_tebakan:
    print("Mencoba:", tebakan)

    if buat_hash_sha256(tebakan) == hash_biasa:
        print("Password ditemukan:", tebakan)
        break