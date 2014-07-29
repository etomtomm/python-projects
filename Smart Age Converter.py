name = input("What is your name? ")

print("Hello {}.".format(name))

age = input("How old are you? ")

age = int(age)

days = age * 365.242

if age > 120:
    print("If you are really that old then how are you still alive?")
    print("Whatever, you are {} days old".format(days))

elif age < 5:
    print("Your really young to type.")
    print("Whatever, you are {} days old".format(days))

elif age < 0:
    print("How is that even possible?!")
    print("Whatever, you are {} days old".format(days))

else:
    print("You are {} days old".format(days))
