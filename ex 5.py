text_to_search = input("Insert a text:")
def find_pattern_occurrences(text):

    words = text.split() # Split the text into words


    occurrences = 0  # Variable to count occurrences

    for word in words:
        # Check if the word starts with "un" and ends with "an"
        if word.startswith("un") and word.endswith("an"):
            occurrences += 1

    # Return the number of occurrences found
    print("The amount of occurrences is:", occurrences)

