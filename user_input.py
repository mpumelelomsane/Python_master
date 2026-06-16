# The input() function pauses your program and waits for the user to enter some text
# message=input("Tell me something ,i will repeat back to you: ")
# print(message)
"""the input()function takes one argument:the prompt, or instructions,that we want to display to the user so they know what to do."""
#NB
"""The program waits while the user enters their response and continues after the user presses enter. The response is
stored in the variable message, then print(message) displays the input back to the user."""

name = input("\nplease enter your name: ")
lastname=input("please enter your last name: ")
age = input("How old are you?: ")
print("\nHello "+ name.title(),lastname.title() + " ,you are now "+ age + " years old!")

#say we want to write a prompt thats longer than one line.
# you can store a prompt in a variable and pass that variable to the input() function.
prompt="Welcome to Python Learning by Mpumelelo! "
prompt+="\nPlease enter your email: "
#the operator += takes the string that was stored in prompt and adds the new string onto the end.
greetings=input(prompt)
status= input("Are you a Developer, Student or a graduate? ")
print("\nWelcome to DevLelo's corner," + status + "s are also allowed.")

#using int() to accept Numerical Input 
height= input("Do you like problem-solving? (Rate yourself in a scale of 10 to 100 ): ")
height=int(height)#python can compare height now ,the int(height) converts the input value to a numerical representation before the comparison is made.

if height<=10:
    print("Oops! Sorry you can't join for now: ")
else:
    print("Welcome you will start tomorrow.")

#The modulo Operator 
"""The modulo operator doesn’t tell you how many times one number fits
into another; it just tells you what the remainder is."""

number=input("Wait, before you go! please enter a number,and i'll tell you if its even or odd: ")
number=int(number)

if number % 2 ==0: 
    print("The number " +str(number)+ " is even. Haha! Bye enjoy your day! ")
else:
    print("The number "+str(number) + " is odd. Haha! Have a nice day! ")

#NB
"""Even numbers are always divisible by two, so if the modulo of a number
and two is zero (here, if number % 2 == 0) the number is even. Otherwise,
it’s odd.""" 
 

