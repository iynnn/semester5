# Import Module
import os
# Folder Path
path = "C:/Users/yanto/Documents/STIS/Semester 5/Mata Kuliah/Information Retrieval/Praktikum/Pertemuan 1/berita"
# List all files in a directory using os.listdir



def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read() 
         
         
         
text_list =[]
# iterate through all file
for file in os.listdir(path):
# Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
 
        # call read text file function
        #read_text_file(file_path)
        query1 = "corona"
        
        if query1 in read_text_file(file_path):
            text_list.append(file)

print("")
print("nama file yang ada coronanya:")
for text in text_list:
    print(text)