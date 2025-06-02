'''SUPER MINI PROJECT KALKULATOR PARKIR'''

import os
os.system("cls")

# membuat header
def header():
    '''HEADER'''
    print("-"*50)
    print("="*5 + " 🅿 KALKULATOR PARKIR MALL GRAND SENAYAN 🅿 " + "="*5)
    print("-"*50)

# input lama parkir
def waktu_parkir():
    '''INPUT LAMA PARKIR'''
    while True:
        try:
            lama_parkir = int(input("Durasi parkir : "))
            return lama_parkir
        except ValueError:
            print("Durasi parkir harus angka, bukan huruf atau elemen lain!!")

# penghitungan lama parkir 
def hitung_parkir_motor (lama_parkir):
    '''MENGHITUNG LAMA PARKIR MOTOR'''
    hasil_parkir_motor = lama_parkir * 2000
    return hasil_parkir_motor

def hitung_parkir_mobil (lama_parkir):
    '''MENGHITUNG LAMA PARKIR MOBIL'''
    hasil_parkir_mobil = lama_parkir * 5000
    return hasil_parkir_mobil

def hitung_parkir_truk (lama_parkir):
    '''MENGHITUNG LAMA PARKIR TRUK'''
    hasil_parkir_truk = lama_parkir * 10000
    return hasil_parkir_truk

# OUTPUT SEMUA
def output_parkir_motor (lama_parkir,hasil_parkir_motor):
    '''OUTPUT PARKIR MOTOR'''
    print(f"- Jenis kendaraan : {"Motor"}")
    print(f"- Biaya parkir motor : {"Rp. 2.000 per jam"}")
    print(f"- Durasi parkir : {lama_parkir}")
    print(f"- Total biaya parkir : Rp.{hasil_parkir_motor:,}")

def output_parkir_mobil (lama_parkir,hasil_parkir_mobil):
    '''OUTPUT PARKIR MOBIL'''
    print(f"- Jenis kendaraan : {"Mobil"}")
    print(f"- Biaya parkir mobil : {"Rp. 5.000 per jam"}")
    print(f"- Durasi parkir : {lama_parkir}")
    print(f"- Total biaya : Rp.{hasil_parkir_mobil:,}")

def output_parkir_truk (lama_parkir,hasil_parkir_truk):
    '''OUTPUT PARKIR TRUK'''
    print(f"- Jenis kendaraan : {"Truk"}")
    print(f"- Biaya parkir mobil : {"Rp. 10.000 per jam"}")
    print(f"- Durasi parkir : {lama_parkir}")
    print(f"- Total biaya : Rp.{hasil_parkir_truk:,}")

save_output = []
keluar_isLoop = True
while keluar_isLoop:
    header()
    if save_output:
            for number, output in enumerate (save_output, start = 1):
                print(f"{number}. {output}")
    while True:
        print()
        print("Pilih jenis kendaraan")
        print("1. Motor --> Rp 2.000 per jam")
        print("2. Mobil --> Rp 5.000 per jam")
        print("3. Truk --> Rp 10.000 per jam")
        choosing = input("--> ")
        if choosing == "1":
            print("-"*31)
            print(f"Jenis kendaraan : {'Motor'}")
            LAMA_PARKIR = waktu_parkir()
            print()
            print("Biaya total : ")
            PARKIR_MOTOR = hitung_parkir_motor(LAMA_PARKIR)
            save_output.append(f"Jenis Kendaraan : {"Motor"}, Durasi parkir : {LAMA_PARKIR} --> Rp.{PARKIR_MOTOR:,} ")
            OUTPUT_PARKIR_MOTOR = output_parkir_motor(LAMA_PARKIR,PARKIR_MOTOR)
        elif choosing == "2":
            print("-"*31)
            print(f"Jenis kendaraan : {'Mobil'}")
            LAMA_PARKIR = waktu_parkir()
            print()
            print("Biaya total : ")
            PARKIR_MOBIL = hitung_parkir_mobil(LAMA_PARKIR)
            print("-"*31)
            save_output.append(f"Jenis kendaraan : {'Mobil'}, Durasi parkir : {LAMA_PARKIR} --> Rp.{PARKIR_MOBIL:,} ")
            OUTPUT_PARKIR_MOBIL = output_parkir_mobil(LAMA_PARKIR,PARKIR_MOBIL)
        elif choosing == "3":
            print("-"*31)
            print(f"Jenis kendaraan : {'Truk'}")
            LAMA_PARKIR = waktu_parkir()
            print()
            print("Biaya total : ")
            PARKIR_TRUK = hitung_parkir_truk(LAMA_PARKIR)
            save_output.append(f"Jenis kendaraan : {'Truk'}, Durasi parkir : {LAMA_PARKIR} --> Rp.{PARKIR_TRUK:,} ")
            OUTPUT_PARKIR_TRUK = output_parkir_truk(LAMA_PARKIR,PARKIR_TRUK)
        else:
            print("Mohon input sesuai angka di menu")
        while True:
            ulanginput = False
            print("-"*31)
            isLoop = input("Apakah anda ingin menghitung lagi (y/n): ").lower()
            if isLoop == "n":
                keluar_isLoop = False
                break
            elif isLoop == "y":
                break
        if isLoop:
            break
for number, output in enumerate (save_output, start = 1):
    print(f"{number}. {output}")
print("Terimakasih")









