# Import Module
import os
# Folder Path
path = "C:/Users/yanto/Documents/STIS/Semester 5/Mata Kuliah/Information Retrieval/Praktikum/Pertemuan 1/berita"
# List all files in a directory using os.listdir
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

# iterate through all file
for file in os.listdir(path):
# Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
 
        # call read text file function
        read_text_file(file_path)


text_1 = "Wilayah Kamu Sudah 'Bebas' COVID-19? Cek 34 Kab/Kota Zona Hijau Terbaru"
text_2 = "Vaksin COVID-19 Bakal Rutin Setiap Tahun? Tergantung, Ini Penjelasannya"
text_3 = "RI Mulai Suntikkan Booster di 2022, Masihkah Ampuh Lawan Varian Delta Cs?"
query = "COVID-19"
docs = [text_1, text_2, text_3]
for doc in docs:
    if query in doc:
        print(doc)

import re
for doc in docs:
    if re.search(query, doc):
        print(doc)


text_list =[]
# iterate through all file
for file in os.listdir(path):
# Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
 
        # call read text file function
        #read_text_file(file_path)
        query1 = "corona"
        
        if query1 in read_text_file(file_path):
            text_list.append(file)
            print(text_list)