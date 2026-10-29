# Python Output / Print
print('Hello world')
print('Hello', 'world') # When you give multiple arguments to print, they are separated by space when displaying
print('Name', 'Dipesh Thakur', sep=":") # You can control what the separator between multiple arguments of the print be when displayed
print('Hello', end=" "); print('world') # By default a print statement ends with a newline. We can change that

# Python Output Numbers
print(3000) # You enter numbers without quotes
print('I am ', 35) # You can mix numbers and strings in print function
print(3+4) # You can do math inside the print function

# Python Comments
'''
This
is
a 
multi-line
string
'''
# Since python ignores string literals not assigned to variables, you can use multi line string as comment

# Python Variables: containers for storing data values

# only letters, numbers and underscores
# must start with a letter or underscore
# case sensitive and can't use reserved keywords as variable names

x = 5
print(x)

# Python has no command to declare a variable. It is created when value is assigned. We can change variable type.

x = str(3) # You can specify the data type with casting
print(type(x)) # You can get the data type with type() function

# Global Variables: A variable with global scope. It's defined at the top level of a file (outside function or class).

# if, else, for, and while blocks don't create their own scope so a variable created inside it belongs to the scope of whatever conditional statement it is inside of

a = 'awesome' # global variables can be used by everyone
def print_awesome():
  print(a)
print_awesome()

x = 'awesome'
def print_something():
  x = 'fantastic' # If you create a variable inside a function, its local variable and can be used only inside the function
  print(x)
print_something()
print('Python is ', x) # Local variable with same name can't affect the global variable

def a_function():
  global a # To create global variable inside a function, use global keyword
  a = 'awesome'
a_function()
print(a)

a = 'awesome'
def b_function():
  global a # Use global keyword if you want to change a global variable inside a function
  a = 'fantastic'
b_function()
print(a)

# Python Variable - Assign Multiple Values

x, y, z = "orange", "banana", "cherry"
print(x, y, z)

x = y = z = "orange"
print(x, y, z)

fruits = ["orange", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

first, *rest = ["orange", "banana", "cherry"]
print(first, rest);

*start, last = ["orange", "banana", "cherry"]
print(start, last)