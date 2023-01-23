# Challenge Task 4.6

#Tells user to input a temprature

print("We will work out whether water is ice, water or steam with the temprature in Celcius, Farenheit or Kelvin")
raw_input = input("Please enter a temprature followed by c, k or f:" '\n')
temp, degrees = int(raw_input[:-1]), raw_input[-1]

#Working out for C
if degrees == "c":
    print("Let's work out what water's state is...")
    if temp < 0:
        print("At " + str(temp) + ", water is a solid therefore it is ice.")
    elif 0 <= temp < 100:
        print("At " + str(temp) + ", water is a liquid therefore it is normal water.")
    else:
        print("At " + str(temp) + ", water is a gas therefore it is steam")

#Working out for F
elif degrees == "f":
    print("Let's work out what water's state is...")
    if temp < 32:
        print("At " + str(temp) + ", water is a solid therefore it is ice.")
    elif 32 < temp < 212:
        print("At " + str(temp) + ", water is a liquid therefore it is normal water.")
    else:
        print("At " + str(temp) + ", water is a gas therefore it is steam")

#Working out for K
elif degrees == "k":
    print("Let's work out what water's state is...")
    if temp < 273:
        print("At " + str(temp) + ", water is a solid therefore it is ice.")
    elif 273 < temp < 373:
        print("At " + str(temp) + ", water is a liquid therefore it is normal water.")
    else:
        print("At " + str(temp) + ", water is a gas therefore it is steam")

#Fun Fact
print("Did you know when water is 0.01 C, 32.018 F or 273.16 K it is all three, a solid, liquid and a gas. This is called the triple point of water.")    
        
    
