# Challenge Task 4.4

# Asks user whether they want a filled box or an unfilled box
print("In this programme you type a number and we'll create the box filled or unfilled")
choice = int(input("Please choose either:" '\n' "Option 1: Unfilled Box" '\n' "Option 2: Filled Box" '\n'))

# Gives The Unfilled Box Option
if choice == 1:

    # Entering the size of the box
   size_unfilled = int(input("Please enter the width of the box: "))

    # Work out size of box
   print("*" * size_unfilled)
   for i in range (size_unfilled - 2):
      print("*" + " " * (size_unfilled - 2) + "*")
   print("*" * size_unfilled)


# Gives the Filled Box Option
if choice == 2:

    # Entering the size of the box
   size_filled = int(input("Please enter the width of the box: "))

    # Work out size of box
   print("*" * size_filled)
   for i in range (size_filled - 2):
       print("*" + (size_filled - 2) * "*" + "*")
   print("*" * size_filled)    

    
    

