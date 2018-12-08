import shelve
import shutil
import send2trash
import os

fin = open('hello.txt')

fin_read = fin.read()
print(fin_read)
fin.close()

fin = open('hello.txt')

print(fin.readlines())  # returns each line as a list element
fin.close()

fin = open('hello.txt', 'w')  # open file in write mode will overwrite , 'a' would be append mode
fin.write("testing!")

fin.write("Hello!!!!!")
fin.close()

shelf_file = shelve.open('hello')
shelf_file['Cats'] = ['Zombie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
print(shelf_file['Cats'])
shelf_file.close()

shelf_file = shelve.open('hello')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))

shutil.copy('hello.txt', 'd:\\copied_from_script.txt')

# shutil.copytree('C:\\Users\\Jacob\\Documents\\Python_Projects', 'd:\\copied')  # copy a folder and move it and rename
#
# shutil.move('d:\\copied_from_script.txt', 'd:\\renamed.txt') # how to rename files
# shutil.move('d:\\renamed.txt', 'c:\\users\jacob\desktop')

send2trash.send2trash('d:\\important.txt')  # sends file to trash

# os.unlink deletes file, os.rmdir removes empty folders, shutil.rmtree removes folders

for folder_name, sub_folder, file_name in os.walk('c:\\python_projects'):
    print("The folder name: " + folder_name)
    print("The sub-folder in : " + folder_name + "are: " + str(sub_folder))
    print("The file name in: " + folder_name + "are: " + str(file_name) + "\n")
