# MINI PROJECT HRD GAJI KARYAWAN
import os
os.system("cls")
karyawan = [
    ["Faiz",5000000],
    ["Adit",3500000],
    ["Jerry",8000000]
]
print("=== SISTEM GAJI KARYAWAN ===")
print("1. Tampilkan data")
print("2. Tambah karyawan")
print("3. Hapus karyawan")
print("4. Total gaji dan rata-rata")
print("5. Update gaji")
print("6. Gaji tertinggi & terendah")
print("7. Keluar")
menu = input(": ")

if menu == "1":
    '''Output karyawan'''
    print(f"{"No":>3} {"Nama":>6} {"Gaji":>10}")
    for index,data_karyawan in enumerate (karyawan, start=1):
        print(f"{index:>2} {data_karyawan[0]:^11} {data_karyawan[1]:>10}")

elif menu == "2":
    '''Input karyawan'''
    nama_karyawan = input("Masukkan nama karyawan : ")
    gaji_karyawan = int(input("Masukkan gaji : "))
    karyawan.append([nama_karyawan,gaji_karyawan])
    print(f"{"No":>3} {"Nama":>6} {"Gaji":>10}")
    for index,data_karyawan in enumerate (karyawan, start=1):
        print(f"{index:>2} {data_karyawan[0]:^11} {data_karyawan[1]:>10}")

elif menu == "3":
    '''Hapus karyawan berdasarkan nama'''
    hapus_karyawan = input("Masukkan nama karyawan yang ingin dihapus : ")
    dihapus = False
    for i in range(len(karyawan)):
        if karyawan[i][0].title() == hapus_karyawan.title():
            del karyawan[i]
            dihapus = True
            break
    print(f"{hapus_karyawan} berhasil dihapus")
    print(f"{"No":>3} {"Nama":>6} {"Gaji":>10}")
    for index,data_karyawan in enumerate (karyawan, start=1):
        print(f"{index:>2} {data_karyawan[0]:^11} {data_karyawan[1]:>10}")

elif menu == "4":
    '''Mencari total dan rata rata gaji'''
    jumlah = sum(data[1] for data in karyawan)
    rata_rata = sum(data[1] for data in karyawan) / len(karyawan)
    print(f"Total gaji karyawan : {jumlah}")
    print(f"Rata-rata gaji karyawan : {rata_rata}")

elif menu == "5":
    '''Update gaji karyawan'''
    nama_karyawan_update =input("Masukkan nama karyawan yang ingin diupdate : ")
    gaji_update = int(input("Masukkan gaji baru : "))
    for i in range (len(karyawan)):
        if karyawan[i][0].title() == nama_karyawan_update.title():
            karyawan[i][1] = gaji_update
            break
    print(f"Gaji {nama_karyawan_update} berhasil diupdate")
    print(f"{"No":>3} {"Nama":>6} {"Gaji":>10}")
    for index,data_karyawan in enumerate (karyawan, start=1):
        print(f"{index:>2} {data_karyawan[0]:^11} {data_karyawan[1]:>10}")

elif menu == "6":
    '''Cari gaji tertinggi dan terendah'''
    gaji_tertinggi = karyawan[0]
    gaji_terendah = karyawan[0]
    for i in range (1, len(karyawan)):
        if karyawan[i][1] > gaji_tertinggi[1]:
            gaji_tertinggi = karyawan[i]
        elif karyawan[i][1] < gaji_terendah[1]:
            gaji_terendah = karyawan[i]
    print(f"Gaji tertinggi : {gaji_tertinggi[1]}")
    print(f"Gaji terendah : {gaji_terendah[1]}")

elif menu == "7":
    print("Terimakasih, silahkan boleh tutup aplikasi")

