# def palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

num = int(input("Enter a number: "))    # Read an integer number from the user

# Convert the number to a string and check if it's equal to its reverse
if str(num) == str(num)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")