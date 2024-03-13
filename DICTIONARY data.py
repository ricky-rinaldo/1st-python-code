user1 = {
    'id': 1,
    'name': 'Ricky Rinaldo',
    'gender': 'male',
    'age': '43 yro',
    'address': {
        'jalan': 'rawa tengah 6',
        'kelurahan': 'galur',
        'kecamatan': 'johar baru',
        'rt/rw': {
            'rt': '02',
            'rw': '07',
        }
    }
}

user2 = {
    'id': 2,
    'name': 'Sri Nurmayasari',
    'gender': 'female',
    'age': '35 yro',
    'address': {
        'jalan': 'buki permata',
        'kelurahan': 'desa ngamprah',
        'kecamatan': 'bandung barat',
        'rt/rw': {
            'rt': '04',
            'rw': '09',
        }
    }
}

print (user1)
print (user2)
print ('\n')
print (user1['name'])
print (user1['gender'])
print (user1['age'])

print ('\n')
print (user2['name'])
print (user2['gender'])
print (user2['age'])

print ('\nCara menampilkan detail data dict didalam suatu data dict')
print (user1['address']['jalan'])
print (user1['address']['kelurahan'])

print ('\nCara menampilkan detail suatu data dict')
print (user1['address']['rt/rw'])
print (user2['address']['rt/rw'])

# merubah data dictionary python dari (') ke data json yg berupa (")
print ('\nMerubah data dict python ke data dict json')
import json
result = json.dumps(user1)
print (result)

# cara cek tipe data atas user1
print ('\ncara cek type data user1')
print (type(user1)) # --> data dict python
print (type(result)) # --> data dict json

