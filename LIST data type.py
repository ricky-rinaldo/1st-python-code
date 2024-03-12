daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
print ('Tampilkan semua daftar buku')
print (daftar_buku)

print ('\nTampilkan daftar buku dengan metode for in')
for buku in daftar_buku:
    print (buku)

print ('\nTampilkan daftar buku dengan metode indeks urutannya')
print (daftar_buku[0])
print (daftar_buku[2])
print (daftar_buku[1])

print ('\nTampilkan penambahan data buku dengan for in range')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

daftar_buku = [2,'The Quest', -707, 3.5]
print ('\nTampilkan penambahan data buku dengan for in range yang elemen nya berbeda2')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenambahkan data pada daftar buku baru dengan metode append')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
daftar_buku.append('Mindset')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenghapus data pada daftar buku baru dengan metode clear')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMengganti isi data pada daftar buku')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
daftar_buku[3] = 'Iqra ver.2'
daftar_buku[2] = 'Coreldraw Pro'
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMengambil isi data pada daftar buku dan disimpan di variabel baru')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
buku = daftar_buku.pop(3)
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenampilkan variabel baru yang tadi di ambil dengan metode pop')
print(buku)