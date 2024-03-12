print ('Menghapus SALAH SATU isi daftar buku dengan metode list comprehension')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
del daftar_buku[3]
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenghapus SEMUA isi daftar buku metode list comprehension')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
del daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenghapus daftar buku metode list comprehension dengan start end 0:1')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
del daftar_buku[0:1] # 0 adalah titik start dan 2 adalah titik end
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenghapus daftar buku metode list comprehension dengan start end nya minus 0:-1')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra']
del daftar_buku[0:-1] # 0 adalah titik start dan 2 adalah titik end
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMenghapus daftar buku metode list comprehension dengan START END STEP dan 2')
daftar_buku = ['Python','Video editing','Coreldraw','Iqra','DragonBall','Cooking','Sholat']
del daftar_buku[0::2] # angka 2 adalah menghapus dengan melangkahi
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nMembuat list baru dengan comprehension :ganjil')
daftar_buku = ['1.Python','2.Video editing','3.Coreldraw','4.Iqra','5.DragonBall','6.Cooking','7.Sholat']
daftar_buku_baru = daftar_buku[0::2]
for i in range (0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print ('\nMembuat list baru dengan comprehension :genap')
daftar_buku = ['1.Python','2.Video editing','3.Coreldraw','4.Iqra','5.DragonBall','6.Cooking','7.Sholat']
daftar_buku_baru = daftar_buku[1::2]
for i in range (0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print ('\nMembuat list baru dengan comprehension (hapus dari ujung)')
daftar_buku = ['1.Python','2.Video editing','3.Coreldraw','4.Iqra','5.DragonBall','6.Cooking','7.Sholat']
daftar_buku_baru = daftar_buku[0:-1]
for i in range (0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print ('\nMembuat list baru dengan comprehension (hapus dari ujung dan melompat)')
daftar_buku = ['1.Python','2.Video editing','3.Coreldraw','4.Iqra','5.DragonBall','6.Cooking','7.Sholat']
daftar_buku_baru = daftar_buku[0:-1:2] # hapus dari ujung dan melompat
for i in range (0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])
