# try except with finally
try:
  i = int(input("Entera number"))
  c = 1/i
except Exception as e:
  print(e)
  exit()
finally:
  print("We are done") # prints both case
print("thanks for using the program") # when prints you input right
# Entera number1
# We are done
# thanks for using the program

# Example 5 else / try with else clause
try:
  i = int(input("Enter a number"))
  c = 1 / i
except Exception as e:
  print(e)
else:
  print("We were Successful")
# Enter a number4
# We were Successful

# Example 4 add / Raising exceptions
def increment(num):
  try:
    return int(num) + 1
  except:
    raise ValueError("This is not good- Ankit")
a = increment('50')
print(a)

# Example 3 multiple errors
try:
  a = int(input("Enter a number : "))
  c = 1/a
  print(c)
except ValueError as e:
  print("Please Enter a valid Value")
except ZeroDivisionError as e:
  print("Make sure you are not dividing by 0")
print("Thanks for using this code")

# Example 2 error of result
try:
  a = int(input("Enter a number : "))
  c = 1 / a
  print(c)
except Exception as e:
  print("Exception occured")
  # print(e) # -> gives result of error
print("Thanks for using this code") 

# write a program to display a / b where a and b are integers if b = 0, display infinite by handling the zero division error
a = int(input("enter number a : "))
b = int(input("enter number b : "))
try:
  print(a/b)
except:
  print("Infinite")
