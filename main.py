# read operation on the file
'''
file = open("demo.txt", "r")
result = file.read()
print("The content present in the file is:-")
print(result)
file.close()
'''

# write operation on the file
'''
file = open("output.txt", "w")
file.write("this is the new data!")
file.close()
'''

# append operation on the file
'''
file = open("output.txt", "a")
file.write("hello world this is the new data get added in the end of the past data or previous data!")
file.close()
'''

# with statement
# with open("demo.txt", "r") as f:
#     print(f.read())

# exclusive creation mode!
# file = open("newfile.txt", "x")
# print("file is created successfully!")

