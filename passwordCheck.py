import re 
# define a function to check password strength
password = 'qwert123'
if (len(password)<8): 
            print("inValid Password less than 8") 

elif not re.search("[a-z]", password): 
            print("inValid Password no small letter") 

elif not re.search("[A-Z]", password): 
            print("inValid Password no caps") 

elif not re.search("[0-9]", password): 
            print("inValid Password no numbers") 

elif not re.search("[_@$]", password): 
            print("inValid Password no symbol") 
else: 
      
            print("Valid Password") 

            
        
  
