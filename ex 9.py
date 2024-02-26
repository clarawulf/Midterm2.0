# birthday of the user
birthday = input("Insert your birthday in the format 'DD-MM-YYYY': ")

# Extract day, month, and year from the input string
day, month, year = map(int, birthday.split('-'))

# Define days in each month
days_in_month = [31, 28 if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Calculate the number of days passed since the birthdate
days_passed = sum(days_in_month[month:] - day for month, day in enumerate(days_in_month[month - 1:]))
days_passed += sum(days_in_month[:current_month - 1]) + current_day - 1

#  result
print("Number of days passed since your birthday (excluding birth year and current year):", days_passed)