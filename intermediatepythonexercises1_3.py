def count_letters(string):
    letter_count = {}
    for letter in string.lower():
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

string = input("Enter a string: ")
letter_count = count_letters(string)
print(letter_count)


#i used https://stackoverflow.com/questions/60941943/how-to-count-the-frequency-of-letters-in-text-excluding-whitespace-and-numbers. for help