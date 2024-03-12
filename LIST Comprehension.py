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
