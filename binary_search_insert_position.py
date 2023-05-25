#Buatlah sebuah fungsi yang menggunakan binary search untuk mencari posisi sisipan sebuah elemen dalam sebuah daftar yang sudah diurutkan secara menaik
def binary_search_insert_position(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Contoh penggunaan
data = [2, 4, 6, 8, 10, 12, 14]
target = 7
insert_position = binary_search_insert_position(data, target)
print(f"Elemen {target} dapat disisipkan pada indeks {insert_position} untuk menjaga daftar tetap terurut.")