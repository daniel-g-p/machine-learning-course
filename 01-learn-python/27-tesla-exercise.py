

def check_driver_age(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off.")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


age_1 = input("How old are you? ")
check_driver_age(age_1)

age_2 = input("How old are you? ")
check_driver_age(age_2)

age_3 = input("How old are you? ")
check_driver_age(age_3)
