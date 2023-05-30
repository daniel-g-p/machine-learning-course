age = 21
has_license = False

is_old_enough = True if age >= 18 else False

if is_old_enough and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")