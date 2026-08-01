def main(): 

#output using our own function  
    name = input("What is your name? ")
    hello(name)

# output passing the expected args 
    hello()

def hello(to = "World"):
    print("hello", to)

main()    