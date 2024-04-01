import os, shutil
#file handling: open file, close file, read file, write and maintain file
path= r"D:\Python\12.File Handling/test.txt"
# my_file=open(path)
# print(my_file)
# print(my_file.read())   #to read the file
# print(my_file.writable())   #to check whether to write in file or not 
# print(my_file.close())
# print(my_file.read())


# a_file=open(path,'r+')
# print(a_file.writable())
# print(a_file.readable())
# print(a_file.read())
# a_file.write("Hello\n")

# a_file=open(path,'w+')
# print(a_file.writable())
# print(a_file.readable())
# a_file.write("Hello\n")
# a_file.seek(0)
# # a_file.seek(1) 
# print(a_file.read())

n_file=open('next.txt','a+')
print(n_file.readable())
print(n_file.writable())
# print(n_file.write("Hello World\n"))
# n_file.seek(0)
# print(n_file.read())
# list1=['\nRam\n','\nSita\n','\nPema\n']
# print(n_file.writelines(list1))
print(n_file.seek(0))
print(n_file.readline())
print(n_file.readlines())
      
# shutil.copy('next.txt','next1.txt')
# os.remove('next1.txt')
# os.remove('copy.txt')
# shutil.move('test.txt','next1.txt')

