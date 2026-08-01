# ask the user for their name 
name = input("What is your name? ")

print("Hello " + name )

#use comma to pass in multiple args 
print("Hey ", name)

#formatted string 
print(f"Hey, {name}")

#WORKING WITH INTERGERS 

x = input("What is x? ") 
y = input(" What is Y? ")

#this is giving us wrong answer 12
z = x+y 
print(z) 

#Now let us classify the input/ out str as intergers 
z = int(x)+int(y)
print(z) 