# store the multipication tables generated in problem 3 in a file named tables table.txt
n = int(input("enter your number : "))

table = [n*i for i in range(1,11)]
print(table)
with open("tables.txt","a") as f:
  f.write(str(table))
  f.write('\n')

# real method is below ->
def readFile(filename):
  try:
    with open(filename,'r') as f :
      print(f.read())
  except FileNotFoundError:
    print(f"File{filename} is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")

def readFile(filename):
  with open(filename,"r") as f:
    print(f.read())

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")

dir = r'C:\pramod\n.txt'
print(dir)

dir = r"C:\pramod\t.txt"
print(dir)

dir = "C:\pramod\t.txt"
print(dir)

# program_to_count_the_number_of_capital_letter.py
with open("SOME_LARGE_FILE.txt","r") as file:
    count = 0
    text = file.read()
    for character in text:
        if character.isupper():
            count +=1

    print("Number of uppercase letters:", count)


# pickling_unpickling
import pickle
# Sample data (a dictionary)
data = {"name": "Alice", "age": 25, "city": "New York"}
# Pickling: Saving the object to a file
with open("data.pkl", "wb") as file:  # 'wb' means write binary
    pickle.dump(data, file)
    print("Data pickled successfully!")
# Unpickling: Loading the object from the file
with open("data.pkl", "rb") as file:  # 'rb' means read binary
    loaded_data = pickle.load(file)
    print("Unpickled data:", loaded_data)
