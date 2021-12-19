birth_date = input("Enter just the date that you want to calculate:")
birth_month = input("Now enter the month. If it's January, you write 1, February 2, etc:")
birth_year = input("Now for the year here:")
birth_date = int(birth_date)  # Converting them to integers
birth_month = int(birth_month)
birth_year = int(birth_year)
f = (14 - birth_month) // 12
y = (birth_year - f)
m = (birth_month + (12 * f)) - 2
y_by_4 = y // 4
y_by_400 = y // 400
y_by_100 = y // 100
Fake_Day = (birth_date + y + 31 * m // 12 + y_by_4 + (y_by_400 - y_by_400))
Day = Fake_Day % 7

if birth_date > 31 or birth_date < 1:  # This is gonna ensure no one tries to give a date of 33 or a date of 0
    print("What...what universe are you in? " + str(birth_date) + " is not, in fact a date! What did you expect?!")

    if birth_month > 12 or birth_month < 1:  # And this is so that Nobody gives a month of 13 or a month of 0
        print("WHAT DO YOU MEAN " + str(birth_month) + "?! That's NOT A MONTH THAT EXISTS ON THIS PLANET!")
        quit()
    quit()

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
