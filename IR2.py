# Mendefinisikan objek-objek

# Empat baris ini digunakan untuk mendefinisikan objek-objek yang akan digunakan untuk membuat inverted index. 
# Pada contoh ini, terdapat empat objek berupa kalimat yang terkait dengan mahasiswa, universitas, dan program studi.
obj1 = "mahasiswa fasilkom universitas jember adalah mahasiswa hebat"
obj2 = "universitas jember memiliki 30.000 mahasiswa"
obj3 = "saat ini fasilkom universitas jember memiliki tiga prodi"
obj4 = "prodi pertama fasilkom universitas jember saat ini adalah prodi sistem informasi"


# Membuat dictionary kosong untuk menyimpan inverted index

# Baris ini digunakan untuk membuat sebuah dictionary kosong yang akan digunakan untuk menyimpan hasil inverted index.
inverted_index = {}


for i, obj in enumerate([obj1, obj2, obj3, obj4], start=1):
    words = obj.split() # memecah objek menjadi kata-kata
    
    # Menampilkan representasi dari setiap objek
    print(f"obj {i} -> D {i} = {words}")
    
    # Memperbarui inverted index
    for word in words:
        # Jika kata sudah ada di dalam inverted index, tambahkan ID dokumen
        if word in inverted_index:
            if i not in inverted_index[word]:
                inverted_index[word].append(i)
        # Jika kata belum ada di dalam inverted index, buat entri baru
        else:
            inverted_index[word] = [i]


# Baris-baris ini menampilkan dictionary dan inverted index ke layar. 
print("\nDictionary\t| Inverted Index")
print("="*80)
# Menampilkan inverted index secara urut berdasarkan urutan kata secara ascending
for word in sorted(inverted_index.keys()):
# Menampilkan kata dan ID dokumen di mana kata tersebut muncul
    print("{:<15} | {}".format(word, inverted_index[word]))


query = input("\nMembangun Query\n---------------\nKetik yang anda cari: ").split()

# Find the relevant documents for the query
relevant_docs = []
for word in query:
    if word in inverted_index:
        relevant_docs.append(inverted_index[word])
    
# Print 
print("\nDokumen yang sesuai dengan query")
print("-----------------------------------")
print(relevant_docs)
print(f"{' '.join(query)} (S 1 ): {relevant_docs}")

# logika AND
retrieved_docs = set.intersection(*[set(doc) for doc in relevant_docs])
print("\nRetrieved object (R) dengan logika 'AND'")
for doc in retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")

# logika OR
retrieved_docs = set.union(*[set(doc) for doc in relevant_docs])
print("\nRetrieved object (R) dengan logika 'OR'")
for doc in retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")

# logika NOT (logika AND dengan kata-kata yang tidak ada dalam query)
not_query = [word for word in inverted_index.keys() if word not in query]
not_relevant_docs = []
for word in not_query:
    if word in inverted_index:
        not_relevant_docs.append(inverted_index[word])

not_retrieved_docs = set.intersection(*[set(doc) for doc in not_relevant_docs])
print("\nRetrieved object (R) dengan logika 'NOT'")
for doc in not_retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")