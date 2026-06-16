#the while loop runs as long as,or while, a certain condition is true.
current_number = 1 #start counting at 1 setting the value of curr_no to 1
while current_number <= 5: #keep running as long as the value of current_num is less or equals to 5 
    print(current_number) 
    current_number += 1 #add 1 on each current_number
"""Once the value of current_number is greater than 5, the loop stops running and the
program ends:"""

prompt ='Tell me something, i will say it back. '
prompt +="\nEnter 'quit' to end the program: "
message=''  #to store whatever value the user enters , We define message as an empty string, "", so Python has something to check the first
#time it reaches the while line. 
while message != 'quit': # the while loop runs as long as the value of message is not 'quit'
    message =input(prompt) #displays the prompt and waits for the user to enter their input
    print(message) 
    if message != 'quit':#only prints the message if it does not match the quit value
        print(message)

#USING A FLAG (differnt events could cause the program to stop, where many conditions are True)
flaggo = True #variable flag is a flag will monitor whether or not the program should continue running 
while flaggo:
    message= input(prompt)
    if message=='quit': #checks the value of the message once the users enters 'quit', 
        flaggo=False #the while loop stops, cause now flaggo is set to False 
    else:
        print(message) # if the users enters anything other than quit message, print the input message

# using BREAK to exit a loop
         
 #the break statement control which lines of code are executed and which aren't.
               