def celcius_ke_fahrenheit(s_c):
    s_f = (s_c * 9/5) + 32
    return s_f

def fahrenheit_ke_celcius(s_f):
    s_c = (s_f - 32) * 5/9
    return s_c

def celcius_ke_kelvin(s_c):
    s_k = s_c + 273.15
    return s_k

def kelvin_ke_celcius(s_k):
    s_c = s_k - 273.15
    return s_c

def aplikasi() :
    print("=== Kalkulator Konversi Suhu agni eh ===")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")
    print("3. Celcius ke Kelvin")
    print("4. Kelvin ke Celcius")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        s_c = float(input("Masukkan suhu Celcius: "))
        s_f = celcius_ke_fahrenheit(s_c)
        print("Suhu Fahrenheit nya adalah : ", s_f)
    elif pilihan == '2':
        s_f = float(input("Masukkan suhu Fahrenheit: "))
        s_c = fahrenheit_ke_celcius(suhu_f)
        print("Suhu Celcius nya adalah: ", s_c)
    elif pilihan == '3':
        s_c = float(input("Masukkan suhu Celcius: "))
        s_k = celcius_ke_kelvin(s_c)
        print("Suhu Kelvin nya adalah: ", s_k)
    elif pilihan == '4':
        s_k = float(input("Masukkan suhu Kelvin: "))
        s_c = kelvin_ke_celcius(s_k)
        print("Suhu Celcius nya adalah: ", s_c)
    else:
        print("Pilihan tidak valid.")

pil = input("mau ngitung suhu? (y):")
while pil == 'y' or 'Y':
    aplikasi()
    pil = input("mau ngitung lagi? (y):")