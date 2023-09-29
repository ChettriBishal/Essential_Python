'''
There's a limit to number of files which can be open simultaneously
'''
import os

my_file = open("data.txt",'r')


file_content = my_file.read()
print(file_content)

my_file.close()


#we can open a file for writing now
writing_file = open('data.txt','w')
writing_file.write("Bishal")

writing_file.close()