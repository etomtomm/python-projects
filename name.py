
while True:
    name = input("What is your name? ")

    if name == "Dereck":
        print("I hate Dereck!")
        break

    elif name == "Bill Gates":
        print("Your name is Bill Gates? That's cool.")
        break

    elif name == "Albert Einstein":
        print("Really? That's weird, I also meet someone earlier called Bill Gates.")
        break

    else:
        print("Hello " + name)


age_in_years = input("How old are you? ")
age_in_years = int(age_in_years)


age_in_days = age_in_years * 365.242

print("You are " + str(age_in_days) + " days old.")
