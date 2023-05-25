#Menemukan nomor telepon Jane menggunakan sequential search
def sequential_search(telepon, nama):
    for i in range(len(telepon)):
        if telepon[i][0] == nama:
            return telepon[i][1]
    return "Nomor telepon tidak ditemukan."

telepon = [["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

nama_jane = "Jane Smith"
nomor_jane = sequential_search(telepon, nama_jane)

print("Nomor telepon Jane Smith adalah:", nomor_jane)
