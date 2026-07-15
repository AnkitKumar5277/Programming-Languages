# read a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# write a file
file = open("sample.txt", "w")
file.write("hello, python")
file.close()

# With statement 
with open('file.txt', 'w') as f:
  a = f.write("you are the best")
  print(a)
