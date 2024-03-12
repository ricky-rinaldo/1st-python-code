'''
Perulangan while dengan variabel pemberhenti
'''

<<<<<<< HEAD
jumlah_buku = 15
=======
jumlah_buku = 10
>>>>>>> origin/main
print ("read all books")
total_baca = 0

jumlah_paham = 0
print (f'Jumlah buku yang sudah dibaca dan dipahami = {jumlah_paham}')

while total_baca < jumlah_buku * 2 :
    total_baca = total_baca + 1
<<<<<<< HEAD
    if jumlah_paham == 15:
=======
    if jumlah_paham == 9:
>>>>>>> origin/main
        print (f'Buku ke {jumlah_paham + 1} belum paham ')
    else:
        jumlah_paham = jumlah_paham + 1
        print (f'Buku ke {total_baca} sudah paham')
