#Samra Ahmed
#samraahmed3291@gmail.com
#Q: create the Random Password Generator by using python
#create and initialize the variable
Hi="Welcome to the Random Password Generator!" 
# print the variable
print(Hi)
#using the necessary modules(string and random)
import string 
import random
#create all characters by using string.ascii
letter=string.ascii_letters
#print the result
print(letter)
#to create and initialize the upper and lowercase
upperD=string.ascii_uppercase
#print the result
print(upperD)
lowerD=string.ascii_lowercase
#print the result
print(lowerD)
#to define digits and symbols
digits=string.digits
#print the variable
print(digits)
symbol=string.punctuation
#print the variable
print(symbol)
#set the length of password
length=int(input("Enter the length of Password that you want :"))
#print the result
print(f"For Random Password Generator the length is :{length}")
#combine the data
data=letter+upperD+lowerD+digits+symbol
print(data)
# for list
abc=[ ]
abc.extend(list(upperD))
abc.extend(list(lowerD))
abc.extend(list(digits))
abc.extend(list(symbol))
#print the list
print(abc)
#to generate password by using random.sample
password=("".join(random.sample(data,length)))
#or we can also  use list in random.sample if we want to use it 
chart="".join(random.sample(abc,length))
print("Password is :",chart)
#print the password with the message 
print(f"Random Password Generator is :  {password}")
#at last i want to thanks 
print("<THANKS>" )

