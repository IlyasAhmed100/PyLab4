# Challenge Task 4.5

#Asks user to input any string of his choosing
string = str(input("Write down anything you want in the space below and we'll put a box around it:" '\n'))

# Creates the box around the string
width = len(string) + 4
width_star = "*" * width
print(width_star)
print("* " + string + " *")
print(width_star)
