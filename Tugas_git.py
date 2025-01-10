data_panen = {
    'Lokasi1' : {
        'nama_lokasi' : 'kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500,
        }
    },
    'Lokasi2' :{
        'nama_lokasi' : 'kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 800,
            'kedelai' : 450
        }  
    },
    'Lokasi3' :{
        'nama_lokasi' : 'kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 850,
            'kedelai' : 600
        }  
    },
    'Lokasi4' :{
        'nama_lokasi' : 'kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }      
    },
    'Lokasi5' :{
        'nama_lokasi' : 'kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }  
    }
}
# no.1
for data , info in data_panen.items():
     print(f"\nnama lokasi : {info['nama_lokasi']}")
     print(f"hasil panen : {info['hasil_panen']}")

# no.2
lokasi2 = data_panen['Lokasi2']['hasil_panen']['jagung']
print(f"\nHasil panen jagung di lokasi 2 : ", lokasi2)

# no.3
lokasi3 =data_panen['Lokasi3']['nama_lokasi']
print("\nnama lokasi 3 :",lokasi3)

# no.4
hasil_panen_padi = {}
hasil_panen_kedelai = {}

for i , j in data_panen.items():
     hasil_panen_padi[i] = j['hasil_panen']['padi']
     hasil_panen_kedelai[i] = j['hasil_panen']['kedelai']
print(f"\nhasil panen padi :", hasil_panen_padi)
print(f"hasil panen kedelai :" ,hasil_panen_kedelai)

# no.5
# variabel untuk memisahkan setiap hasil panen padi
hasil_padi_lokasi1 = data_panen['Lokasi1']['hasil_panen']['padi']
hasil_padi_lokasi2 = data_panen['Lokasi2']['hasil_panen']['padi']
hasil_padi_lokasi3 = data_panen['Lokasi3']['hasil_panen']['padi']
hasil_padi_lokasi4 = data_panen['Lokasi4']['hasil_panen']['padi']
hasil_padi_lokasi5 = data_panen['Lokasi5']['hasil_panen']['padi']

# Variabel untuk memisahkan setiap hasil panen kedelai
hasil_kedelai_lokasi1 = data_panen['Lokasi1']['hasil_panen']['kedelai']
hasil_kedelai_lokasi2 = data_panen['Lokasi2']['hasil_panen']['kedelai']
hasil_kedelai_lokasi3 = data_panen['Lokasi3']['hasil_panen']['kedelai']
hasil_kedelai_lokasi4 = data_panen['Lokasi4']['hasil_panen']['kedelai']
hasil_kedelai_lokasi5 = data_panen['Lokasi5']['hasil_panen']['kedelai']

# Print untuk memastikan hasil
print(f"\nHasil Panen Padi per Lokasi:")
print("Lokasi 1:", hasil_padi_lokasi1)
print("Lokasi 2:", hasil_padi_lokasi2)
print("Lokasi 3:", hasil_padi_lokasi3)
print("Lokasi 4:", hasil_padi_lokasi4)
print("Lokasi 5:", hasil_padi_lokasi5)

print("\nHasil Panen Kedelai per Lokasi:")
print("Lokasi 1:", hasil_kedelai_lokasi1)
print("Lokasi 2:", hasil_kedelai_lokasi2)
print("Lokasi 3:", hasil_kedelai_lokasi3)
print("Lokasi 4:", hasil_kedelai_lokasi4)
print("Lokasi 5:", hasil_kedelai_lokasi5)

# no.6

for data , info in data_panen.items():
    a = info['hasil_panen']['padi']
    b = info['hasil_panen']['jagung']
    
    if a > 1300 or b > 800 :
        print(f"\n{data} memerlukan perhatian khusus")
    else :
        print(f"\n{data} aman")
     
     

