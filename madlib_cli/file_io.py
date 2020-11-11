#with will close a file once the code block within the with is finished
#you can name the open file to any variable name (in this case file)
#the default option for open is r=reading mode
    #there are many other options like w=writing mode
    #wb=writing in binary
with open('assets/spam.txt',"r") as file:
    #you can read files with the file.read() method
    content=file.read()
    print(content)
    #you can close a file with file.close() method
close = file.close()
#file.closed is a boolean attribute which tells you if the file is closed or not closed
print('was file closed:',file.closed)