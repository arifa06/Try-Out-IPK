# Jumlah Mahasiswa
mahasiswa = int(input('Jumlah Mahasiswa : '))
print('')

# Membuat Variabel Kosong Untuk Menampung Nilai Baru dari Hasil Perulangan
nim = []
nama = []
alamat = []
asalSekolah = []
kodeProdi = []
ipkAwal = []
uts = []
uas = []
tm = []
totalIPK = []

# Pengulangan Untuk Mengisi Variable Kosong
for i in range (mahasiswa):
    print('Data Mahasiswa ke -', i+1)
    print('')
    nim.append(int(input('Masukkan NIM : ')))
    nama.append(input('Masukkan Nama : '))
    alamat.append(input('Masukkan Alamat : '))
    asalSekolah.append(input('Masukkan Asal Sekolah : '))
    kodeProdi.append(input('Masukkan Kode Prodi : '))
    ipkAwal.append(int(input('Masukkan IPK Awal : ')))
    uts.append(int(input('Masukkan UTS Awal : ')))
    uas.append(int(input('Masukkan UAS Awal : ')))
    tm.append(int(input('Masukkan TM Awal : ')))
    totalIPK.append((ipkAwal[i]+(0.3*uts[i]+0.4*uas[i]+0.3*tm[i]))/2)
    print('')

# Beasiswa
    if kodeProdi[i] == 'TI' or kodeProdi[i] == 'SI':
        if 75 <= totalIPK[i] < 85:
            print('Total IPK Akhir adalah',totalIPK[i],'| Maka Beasiswa 20 %')
        elif 85 <= totalIPK[i] < 100:
            print('Total IPK Akhir adalah',totalIPK[i],'| Maka Beasiswa 30 %')
        else:
            print('Total IPK Akhir adalah',totalIPK[i],'| Nilai Kurang, Tidak Mendapat Beasiswa')

    elif kodeProdi[i] == 'DKV' or kodeProdi[i] == 'Teknik Industri':
        if 75 <= totalIPK[i] < 85:
            print('Total IPK Akhir adalah',totalIPK[i],'| Maka Beasiswa 25 %')
        elif 85 <= totalIPK[i] < 100:
            print('Total IPK Akhir adalah',totalIPK[i],'| Maka Beasiswa 35 %')
        else:
            print('Total IPK Akhir adalah',totalIPK[i],'| Nilai Kurang, Tidak Mendapat Beasiswa')

    else:
        print('Tidak Ada Program Beasiswa')

    print('')
    print(50*'=')
    print('')
