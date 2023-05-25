#Terdapat daftar bilangan [7, 10, 13, 6, 17, 22, 19]. Temukan bilangan prima dalam daftar tersebut menggunakan sequential search
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

# Daftar bilangan
numbers = [7, 10, 13, 6, 17, 22, 19]

# Mencari bilangan prima dalam daftar
prime_numbers = find_prime_numbers(numbers)

# Menampilkan bilangan prima yang ditemukan
print("Bilangan prima dalam daftar:", prime_numbers)