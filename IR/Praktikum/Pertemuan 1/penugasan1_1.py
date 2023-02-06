# import module
import os

# folder path
# path = "C:\ANZPython\\news"

# error
# path = "C:/Users/ASUS/Downloads/news"

path = "C:/Users/ASUS/Downloads/berita"
# path = "C:\\Users\\ASUS\\Downloads\\news"

# list all files in a directory using os.listdir
# for file in os.listdir(path):
#     if os.path.isfile(os.path.join(path,file)):
#         print(file)

def read_text_file(file_path):
    with open(file_path,'r') as f:
        return f.read() # return value print null

# # iterate through all file
# for file in os.listdir(path):
#     # check whether file is in text format or not
#     if file.endswith(".txt"):   # endswith
#         file_path = f"{path}\{file}"
#         # call read text file function
#         read_text_file(file_path)

# iterate through all file
text_list = []
for file in os.listdir(path):
    # check whether file is in text format or not
    if file.endswith(".txt"):   # endswith
        file_path = f"{path}/{file}"

        query = "corona"
        if query in read_text_file(file_path):
            text_list.append(file)
        # call read text file function
        # text_list.append(read_text_file(file_path))

for text in text_list:
    print (text)
# # first way
# text_1 = "Wilayah Kamu Sudah 'Bebas' COVID-19? Cek 34 Kab/Kota Zona Hijau Terbaru"
# text_2 = "Vaksin COVID-19 Bakal Rutin Setiap Tahun? Tergantung, Ini Penjelasannya"
# text_3 = "RI Mulai Suntikkan Booster di 2022, Masihkah Ampuh Lawan Varian Delta Cs?"
# text_4 = "COVID-19, U R DONE"
# query = "COVID-19"
# docs = [text_1,text_2,text_3,text_4]
# for doc in docs:
#     if query in doc:
#         print(doc)

# # second way
# import re
# for doc in docs:
#     if re.search(query,doc):
#         print(doc)

# query = "corona"
# for text in text_list:
#     if query in text:
#         print(text)