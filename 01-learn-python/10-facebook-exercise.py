from datetime import date

birth_year = input("What year were you born in? ")
current_year = date.today().year

age = current_year - int(birth_year)

print(f"You are roughly {age} years old.")