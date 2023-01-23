# Task 4.3
print("Welcome to the currency converter programme")
#Gives options
print("You can convert from:" '\n' "Option 1: GBP/Euro" '\n' "Option 2: Euro/GBP")
option = int(input("Please type 1 for Option 1 or 2 for Option 2:"))

#Gives relevant conversion rates for option 1
if option == 1:
    print("Ok, we shall convert GBP into Euros." '\n' "The conversion rate is £1 = €1.10")
    pounds_to_euros = float(input("Please enter the amount of Pounds you would like to convert to Euros:"))
    final_euros = "{:.2f}".format(pounds_to_euros * 1.1)
    print("£" + str(pounds_to_euros) + " converted to Euros is €" + str(final_euros))
    
# Gives relevant conversion rates for option 2
elif option == 2:
    print("Ok, we shall convert Euros into GBP." '\n' "the conversion rate is €1 = £0.91")
    euros_to_pounds = float(input("Please enter the amount of Euros you would like to convert to Pounds:"))
    final_pounds = "{:.2f}".format(euros_to_pounds * 0.91)
    print("€" + str(euros_to_pounds) + " converted to Pounds is £" + str(final_pounds))

# tells user other numbers aren't an option
else:
    print("Sorry, that number is not an option")
    
    
    
    
