
import html  # used in removing html tags
import re    # used to check what is contained in a string
# Html encoding  
name = 'John12'

# Using html.escape() method 
escaped_string = html.escape(name) 
print(escaped_string)

# variable validation
# check if its empty , reject if its empty
if escaped_string == '':
  print("Cannot be empty")

# check if its length is between 4 to 10 x-ters, 
# reject if its out of bound 
elif len(escaped_string) >= 3 and len(escaped_string) > 10:
  print("Should be between 4 x-ters - 10 x-ters")

# check if the string has numbers, reject if it has a number
elif re.search("[0-9]", escaped_string): 
            print("Names cannot contain numbers")

# check if the string has symbols, reject if it has a symbol
elif re.search("[_@$]", escaped_string): 
            print("Names cannot contain symbols")

# finnaly, accept
else:
   print("It valid")












