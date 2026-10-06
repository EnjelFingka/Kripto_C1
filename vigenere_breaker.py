from collections import defaultdict, Counter

def bersihkan(teks):
    return ''.join(c.upper() for c in teks if c.isalpha())

def cari_panjang_kunci(teks):
    posisi = defaultdict(list)
    kandidat = Counter()

    for i in range(len(teks) - 2):
        pola = teks[i:i+3]
        posisi[pola].append(i)

    for pola, pos in posisi.items():
        if len(pos) > 1:
            print("Pola:", pola, "Posisi:", pos)

            for i in range(len(pos) - 1):
                jarak = pos[i+1] - pos[i]

                for faktor in range(2, 13):
                    if jarak % faktor == 0:
                        kandidat[faktor] += 1

    if not kandidat:
        return []

    return [x[0] for x in kandidat.most_common(5)]

def skor(teks):
    frekuensi = {
        'A': 0.20, 'B': 0.02, 'C': 0.01, 'D': 0.04,
        'E': 0.08, 'F': 0.00, 'G': 0.04, 'H': 0.03,
        'I': 0.08, 'J': 0.01, 'K': 0.05, 'L': 0.03,
        'M': 0.04, 'N': 0.09, 'O': 0.02, 'P': 0.03,
        'Q': 0.00, 'R': 0.04, 'S': 0.05, 'T': 0.06,
        'U': 0.05, 'V': 0.00, 'W': 0.00, 'X': 0.00,
        'Y': 0.02, 'Z': 0.00
    }

    hitung = Counter(teks)
    total = len(teks)

    nilai = 0

    for huruf, target in frekuensi.items():
        aktual = hitung.get(huruf, 0) / total
        nilai += abs(aktual - target)

    return nilai

def cari_kunci(teks, panjang):
    kunci = ""

    for i in range(panjang):
        grup = teks[i::panjang]

        shift_terbaik = 0
        skor_terbaik = 999

        for shift in range(26):
            hasil = ""

            for c in grup:
                hasil += chr((ord(c) - 65 - shift) % 26 + 65)

            nilai = skor(hasil)

            if nilai < skor_terbaik:
                skor_terbaik = nilai
                shift_terbaik = shift

        kunci += chr(shift_terbaik + 65)

    return kunci

def decrypt(cipher, kunci):
    hasil = ""
    indeks = 0

    for c in cipher:
        if c.isalpha():
            shift = ord(kunci[indeks % len(kunci)]) - 65

            hasil += chr(
                (ord(c.upper()) - 65 - shift) % 26 + 65
            )

            indeks += 1
        else:
            hasil += c

    return hasil


ciphertext = input("Masukkan ciphertext: ")

teks = bersihkan(ciphertext)

kandidat = cari_panjang_kunci(teks)

if not kandidat:
    print("\nPola tidak cukup untuk menebak kunci.")

else:
    print("\nKandidat panjang kunci:", kandidat)

    panjang = int(input("Pilih panjang kunci: "))

    kunci = cari_kunci(teks, panjang)

    plaintext = decrypt(ciphertext, kunci)

    print("\nOutput")
    print("Plaintext :", plaintext)
    print("Key       :", kunci)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", plaintext)