#Temukan definisi kata menggunakan binary search
def cari_definisi(kata, daftar_kata):
    awal = 0
    akhir = len(daftar_kata) - 1
    
    while awal <= akhir:
        tengah = (awal + akhir) // 2
        kata_tengah = daftar_kata[tengah][0]  # Mengambil kata tengah dari pasangan (kata, definisi)
        
        if kata_tengah == kata:
            return daftar_kata[tengah][1]  # Mengembalikan definisi jika kata ditemukan
        elif kata_tengah < kata:
            awal = tengah + 1
        else:
            akhir = tengah - 1
    
    return "Kata tidak ditemukan"  # Mengembalikan pesan jika kata tidak ditemukan

kamus_ajaib = [
    ("Apple", "Buah Apel"),
    ("Banana", "Buah Pisang"),
    ("Cat", "Kucing"),
    ("Duck", "Bebek"),
    ("Elephant", "Gajah")
]

kata_yang_dicari = "Cat"
definisi = cari_definisi(kata_yang_dicari, kamus_ajaib)
print("Definisi kata '{}' adalah: {}".format(kata_yang_dicari, definisi))