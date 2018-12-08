import os

print(os.path.join('folder1', 'folder2', 'folder3'))  # gets the correct filesystem depending on os

print(os.getcwd())  # get current work directory

os.chdir('c:\\')  # change to root folder
print(os.getcwd())

total_size = 0
for file_name in os.listdir('C:\\Users\\Jacob\\Documents\\HIST 450'):
    if not os.path.isfile(os.path.join('C:\\Users\\Jacob\\Documents\\HIST 450', file_name)):
        continue
    total_size += os.path.getsize(os.path.join('C:\\Users\\Jacob\\Documents\\HIST 450', file_name))

print(total_size)


os.makedirs('c:\\test\\test2\\test3')  # creates dir
