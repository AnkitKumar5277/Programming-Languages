# read a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# write a file
file = open("sample.txt", "w")
file.write("hello, python")
file.close()
