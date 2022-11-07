############################## CSV ##############################
################ COMMA SEPARATED VALUES ################
# You can import from banking apps, web, fitbit, linkedin etc and practice these exercises. 
# For example, 'how many times have I sent a smiley face in Linkedin across all messages? 

##  # Demonstrate:
##  # 1. How to read data from a csv file in a list.
##  # 2. How to store data from a CSV file in a list.
##  # 3. How to write to a csv file.

# first file openeing. second the 'mode' (eg write; read; etc)
## If you've not got a file you're calling, doing the f = x will create the file for you. 
### The file, if created or opened, you have to be in the desired/correct location in the terminal 
# my_file_var = open('file.txt',mode='r') # 'r' for read. 
# my_file_var = open('file.txt', 'w') # 'w' for write. 
# my_file_var = open('file.txt', 'a') # will allow you to add to the file (inline) rather than overwriting the contents (w)
# my_file_var.write("Hello world again")
# my_file_var.close()
# print(my_file_var.read())
# print(my_file_var.read())
# If you want to read it multiple times, you'll have to add a command to set that behaviour
# Alternatively, you can open, close, open again etc. 
# Note. When you are working in these files in this way, there is a literal cursor banging about in the file.txt
# the curser will only run once, as opposed to code, that can re-run.

# with open('file.txt',mode='r') as my_file:
#     print(my_file.read())
# This is neat, becuase the contents renders in the terminal, meaning for me - fewer files to jump around. 

# Over in the playground:
# import csv

# with open('2016_pilbara.csv') as csv_file:
#     csv.reader
# here, csv.reader, refers to the import. 
# you will need to be in the appropriate directory to work with this import, 
# alternatively, you are able to reference the entire file location in the method (not the import, like js)