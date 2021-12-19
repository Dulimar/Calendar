import time
error = "I'm afraid that's not a date."

birth_date = input("The date goes here:")
birth_date = int(birth_date) # Have to convert it into an integer for calculations.
if birth_date > 31 or birth_date < 1: # Making sure nobody writes an invalid date
    print("Did you not attend first grade?.I'm dissapointed in you. Just press enter and leave.")  # An insult
    input()
    quit()
birth_month = input("The month goes here:")
birth_month = int(birth_month)  # Again, converting for convenience
if birth_month > 12 or birth_month < 1:  # Again, No invalidity ensured.
    print("How do you not know the months of the year? Press enter and try again once you get an EDUCATION!")  # SHEESH
    input()
    quit()
if (birth_month == 9 or 4 or 6 or 11) and birth_date == 31:  # Even took care of the 30 - day months!
    print("Here's a reminder of the months with 30 days - April, June, September and November. The date you're "
          "looking for does not exist.")
    input()
    quit()
birth_year = input("Now for the year here:")
birth_year = int(birth_year)  # CONVERSION
if birth_month == 2 and birth_date >= 30:  # Cause February can't have 30 or 31 no matter what
    print(error)
if birth_month == 2 and birth_date == 29 and birth_year % 4 != 0 and birth_year % 100 != 0:  # Taking care of the leap years.
    print(error)
    input()
    quit()
print("Now, you have to wait for three seconds for dramatic effect (because of course).")
time.sleep(3)  # To give the pretence that this actually requires difficult calculation


f = (14 - birth_month) // 12
y = (birth_year - f)
m = (birth_month + (12 * f)) - 2
y_by_4 = y // 4
y_by_400 = y // 400
y_by_100 = y // 100
Fake_Day = (birth_date + y + 31 * m // 12 + y_by_4 + (y_by_400 - y_by_400))
Day = Fake_Day % 7
# That's really all the calculation needed.

if Day == 1:
    print("The last of the weekends is surely a sad sight to see. Its a sunday.")
else:
    if Day == 2:
        print("Yeah you aren't gonna be happy about this one. Its a Monday.")
    else:
        if Day == 3:
            print("That's gonna be a Tuesday according to my super calculations!")
        else:
            if Day == 4:
                print("Yeah, that's gonna be a Wednesday, chief.")
            else:
                if Day == 5:
                    print("Thursdays are pretty bad, arent they? Well, this is gonna be a Thursday. Good luck!")
                else:
                    if Day == 6:
                        print("Be patient! The weekend is tomorrow. Its a Friday.")
                    else:
                        print("REJOICE FOR YOUR SAVIOR IS HERE! Its a SATURDAY. CELEBRATE.")
# That's all the logic needed to get the days
x = input("Press anything to close program ")
