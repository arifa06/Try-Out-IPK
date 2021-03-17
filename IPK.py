# Jumlah Mahasiswa
mahasiswa = int(input('Jumlah Mahasiswa : '))
print('')

# Data Mahasiswa
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

for i in range(mahasiswa):
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
    print('')

# Nilai IPK Akhir
for i in range(mahasiswa):
    totalIPK.append((ipkAwal[i]+(0.3*uts[i]+0.4*uas[i]+0.3*tm[i]))/2)
    print('IPK Akhir adalah',totalIPK)
    print('')
    # Beasiswa
    if kodeProdi[i] == 'TI':
        if 75 < totalIPK[i] < 85:
            print('Beasiswa 20 %')
        elif 85 < totalIPK[i] < 100:
            print('Beasiswa 30 %')
    elif kodeProdi[i] == 'SI':
        if 75 < totalIPK[i] < 85:
            print('Beasiswa 20 %')
        elif 85 < totalIPK[i] < 100:
            print('Beasiswa 30 %')
    elif kodeProdi[i] == 'DKV':
            print('Beasiswa 25 %')
        elif 85 < totalIPK[i] < 100:
            print('Beasiswa 35 %')
    elif kodeProdi[i] == 'Teknik Industri':
            print('Beasiswa 25 %')
        elif 85 < totalIPK[i] < 100:
            print('Beasiswa 35 %')
    else:
        print('Tidak Ada Beasiswa')