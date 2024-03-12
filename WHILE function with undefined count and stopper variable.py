'''
Perulangan while dengan variabel pemberhenti
'''

book_count = 10
print ("read all books")
read_count = 0

understood_count = 0
print (f'Jumlah buku yang sudah dibaca dan dipahami = {understood_count}')

while read_count < book_count * 2 :
    read_count = read_count + 1
    if understood_count == 9:
        print (f'Buku ke {understood_count + 1} belum paham ')
    else:
        understood_count = understood_count + 1
        print (f'Buku ke {read_count} sudah paham')